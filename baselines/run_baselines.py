"""
run_baselines.py - the no-model baselines for faithful_claim, scored exactly like
the Inspect task (curry_record_evals/scoring.py).

  always_supported   says SUPPORTED to everything
  always_cannot      abstains on everything
  name_present       SUPPORTED when every token of the person's stored name is in
                     the page's OCR text, else CANNOT BE PROVEN
  faithful_cite_t1   faithful-cite Tier 1 in subject mode (the person's name plus
                     the cited text), SUPPORTED on a pass, else CANNOT BE PROVEN;
                     faithful-cite never answers UNSUPPORTED by design
  july_verifier      the verdict the July 2026 verifier (claude-sonnet-4-6 over
                     the OCR text) recorded on the ring-audit sheet before Mike
                     ruled; gold only, and Mike saw it while ruling

name_present and faithful_cite_t1 need the full OCR text, so they run against the
private items file; the scores they print are what gets published.

  python baselines/run_baselines.py _private/items/faithful_claim.jsonl
"""
import json
import math
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
try:
    import faithful_cite  # noqa: F401
except ImportError:  # the sibling staging checkout
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "faithful-cite"))
from faithful_cite.normalize import normalize_reference, name_tokens
from faithful_cite.tier1 import check_subject_claim

from curry_record_evals.scoring import outcome

ABSTAIN = "CANNOT_BE_PROVEN"
JULY = {"keep": "SUPPORTED", "kill": "UNSUPPORTED", "escalate": ABSTAIN}


def baselines(rec, text):
    out = {"always_supported": "SUPPORTED", "always_cannot": ABSTAIN}
    if text is not None:
        ref = normalize_reference(text)
        toks = name_tokens(rec["claim"]["entity"])
        out["name_present"] = "SUPPORTED" if toks and all(t in ref for t in toks) else ABSTAIN
        r = check_subject_claim(rec["claim"]["entity"], " ".join(rec["claim"]["mentions"]), text)
        out["faithful_cite_t1"] = "SUPPORTED" if r.passed else ABSTAIN
    jm = rec.get("july_model") or {}
    if jm.get("verdict") in JULY:
        out["july_verifier"] = JULY[jm["verdict"]]
    return out


def table(rows):
    """rows: list of (groups, baseline, outcome, label_is_abstain); each row counts once per group"""
    agg = defaultdict(lambda: {"n": 0, "right": 0, "wrong": 0, "abstain": 0, "settled": 0, "settled_commit": 0})
    for gs, b, o, lab_abs in rows:
        for key in [(g, b) for g in gs]:
            a = agg[key]
            a["n"] += 1
            a[o] += 1
            if not lab_abs:
                a["settled"] += 1
                a["settled_commit"] += int(o != "abstain")
    res = {}
    for (g, b), a in agg.items():
        n, r, w = a["n"], a["right"], a["wrong"]
        p = r / n
        res[(g, b)] = {
            "n": n,
            "correct": round(p, 3),
            "wrong": round(w / n, 3),
            "abstained": round((n - r - w) / n, 3),
            # 95% half-width on correct: 1.96 x the binomial standard error (Miller 2024)
            "ci95": round(1.96 * math.sqrt(p * (1 - p) / n), 3),
            "precision": round(r / (r + w), 3) if r + w else None,
            "coverage": round(a["settled_commit"] / a["settled"], 3) if a["settled"] else None,
            "net": round((r - w) / n, 3),
            "net_p3": round((r - 3 * w) / n, 3),
        }
    return res


def main(path):
    recs = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    rows = []
    for rec in recs:
        text = None
        if rec.get("text_path") and os.path.exists(rec["text_path"]):
            text = open(rec["text_path"], encoding="utf-8").read()
        groups = ["all", rec["split"]] + ([f"gold-{rec['assurance']}"] if rec["split"] == "gold" else [])
        for b, ans in baselines(rec, text).items():
            o = outcome(ans, rec["label"], ABSTAIN)
            rows.append((groups, b, o, rec["label"] == ABSTAIN))
    res = table(rows)
    groups = ["gold", "gold-blind", "gold-blind-page", "gold-blind-told", "gold-deliberate", "gold-group", "gold-rapid", "held", "silver", "all"]
    order = ["always_supported", "always_cannot", "name_present", "faithful_cite_t1", "july_verifier"]
    lines = ["| split | baseline | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for g in groups:
        for b in order:
            r = res.get((g, b))
            if r:
                lines.append(f"| {g} | {b} | {r['n']} | {r['correct']} | {r['wrong']} | {r['abstained']} | {r['ci95']} | "
                             f"{r['precision']} | {r['coverage']} | {r['net']} | {r['net_p3']} |")
    print("\n".join(lines))
    os.makedirs(os.path.join(os.path.dirname(HERE), "results"), exist_ok=True)
    with open(os.path.join(os.path.dirname(HERE), "results", "baselines-faithful_claim.md"), "w", encoding="utf-8") as f:
        f.write("# faithful_claim: no-model baselines\n\n"
                "Scored with the task's own rules (curry_record_evals/scoring.py). "
                "`all` counts every item once. Held items are reported apart and never counted in gold. "
                "july_verifier exists only on ring-audit items (gold and held).\n\n"
                "gold-blind-page are the 70 items Mike Curry ruled at the blind sitting of 2026-10-21 and ruled again "
                "the same evening at its whole-page pass, the whole page in view, no earlier call shown (the first "
                "sheet had shown a crop around the cited text, which on a column-head cite hid the name): the 30 July "
                "rulings the page text contradicted on its face, held out of gold until then, and 40 items that were "
                "silver before it. Two of the 70 he had been told about before the first sheet; the item says so.\n\n")
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "_private", "items", "faithful_claim.jsonl"))
