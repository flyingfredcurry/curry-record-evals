"""
check_ship.py - the pre-publish check. Run it from the repository root before a push.

  python tools/check_ship.py        exit 0 when clean, 1 with findings listed

What it checks, and why: the pages are the archive's own scans and no page image, full OCR
text layer, Inspect log or private note ships here.
  1. data/faithful_claim.jsonl: every `excerpt` is at most fifty words and no item carries a
     full text layer or an image field.
  2. data/same_person.jsonl: the printed transcriptions total at most fifty words per record
     (each side of a pair).
  3. No shipped file is an Inspect log, an image or a PDF, and nothing under _private/ or
     logs/ is in the shipped tree.
  4. No shipped text file names a Windows drive path or the archive's desktop folder.
  5. Every rationale line is third person (no first-person keeper note shipped raw).
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".venv", "_private", "logs", "__pycache__", "node_modules"}
BAD_EXT = {".eval", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".tif", ".tiff", ".pdf", ".db", ".sqlite"}
TEXT_EXT = {".md", ".py", ".jsonl", ".json", ".toml", ".txt", ".cfg", ".ini", ".yaml", ".yml", ""}
PRIVATE_FIELDS = {"text_layer", "page_text", "image", "image_b64", "page_image", "crop", "crops"}
FIRST_PERSON = re.compile(r"\b(I|I'm|I'd|I've|my|me)\b")
DRIVE = re.compile(r"\b[A-Za-z]:[\\/](?:Users|users|Windows|Program Files)|Desktop[\\/]Curry Legacy|/Users/[A-Za-z]")
WORDS = re.compile(r"\S+")


def words(s):
    return len(WORDS.findall(s or ""))


def shipped_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.endswith(".egg-info")]
        for f in filenames:
            if f == "STAGING-NOTES.md":
                continue
            out.append(os.path.join(dirpath, f))
    return out


def main():
    findings = []
    # 1. faithful_claim
    with open(os.path.join(ROOT, "data", "faithful_claim.jsonl"), encoding="utf-8") as fh:
        fc = [json.loads(l) for l in fh if l.strip()]
    for it in fc:
        n = words(it.get("excerpt"))
        if n > 50:
            findings.append(f"{it['id']}: excerpt is {n} words")
        leak = PRIVATE_FIELDS & set(it.keys())
        if leak:
            findings.append(f"{it['id']}: private field(s) {sorted(leak)}")
        if it.get("rationale") and FIRST_PERSON.search(it["rationale"]):
            findings.append(f"{it['id']}: rationale reads first person")
    # 2. same_person
    with open(os.path.join(ROOT, "data", "same_person.jsonl"), encoding="utf-8") as fh:
        sp = [json.loads(l) for l in fh if l.strip()]
    for it in sp:
        for side in ("a", "b"):
            n = sum(words(r.get("printed")) for r in it[side]["receipts"])
            if n > 50:
                findings.append(f"{it['id']} side {side}: {n} printed words")
            for r in it[side]["receipts"]:
                leak = PRIVATE_FIELDS & set(r.keys())
                if leak:
                    findings.append(f"{it['id']} side {side}: private field(s) {sorted(leak)}")
        if it.get("rationale") and FIRST_PERSON.search(it["rationale"]):
            findings.append(f"{it['id']}: rationale reads first person")
    # 3 and 4. the shipped tree
    files = shipped_files()
    for f in files:
        rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
        ext = os.path.splitext(f)[1].lower()
        if ext in BAD_EXT:
            findings.append(f"{rel}: a {ext} file is in the shipped tree")
            continue
        if rel.startswith("_private/") or rel.startswith("logs/"):
            findings.append(f"{rel}: private path in the shipped tree")
        if ext in TEXT_EXT:
            try:
                with open(f, encoding="utf-8") as fh:
                    body = fh.read()
            except UnicodeDecodeError:
                findings.append(f"{rel}: not UTF-8 text")
                continue
            m = DRIVE.search(body)
            if m:
                findings.append(f"{rel}: names a local path ({m.group(0)})")
    print(f"checked {len(fc)} claim items, {len(sp)} pairs, {len(files)} shipped files")
    if findings:
        print("FINDINGS:")
        for x in findings:
            print("  -", x)
        return 1
    print("clean: no excerpt over fifty words, no private field, no log or image, no local path, no first-person rationale")
    return 0


if __name__ == "__main__":
    sys.exit(main())
