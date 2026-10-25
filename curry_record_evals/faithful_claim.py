"""
faithful_claim: does this printed page refer to this person?

An automated extractor read a scanned page and recorded that it refers to a
named person, citing the printed text it matched. A human ruled each record
against the page. The model gets the claim and the evidence and answers
SUPPORTED, UNSUPPORTED, or CANNOT BE PROVEN.

Conditions (task parameter `condition`):
  excerpt     the public condition: the claim, the page reference, and at most
              fifty words of the page's OCR text around the cited text
  page_text   the page's full OCR text layer        (needs the private items file)
  page_image  the page image, no text               (needs the private items file)
  page_both   the page image and its full OCR text  (needs the private items file)

Run:
  inspect eval curry_record_evals/faithful_claim.py --model anthropic/claude-haiku-5-5
  inspect eval curry_record_evals/faithful_claim.py -T condition=page_text \
      -T items=_private/items/faithful_claim.jsonl --model ...
"""
import json
import os

from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.model import ChatMessageSystem, ChatMessageUser, ContentImage, ContentText, GenerateConfig
from inspect_ai.solver import generate

from curry_record_evals.scoring import verdict_scorer

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ITEMS = os.path.join(os.path.dirname(HERE), "data", "faithful_claim.jsonl")
LABELS = ["SUPPORTED", "UNSUPPORTED", "CANNOT_BE_PROVEN"]
ABSTAIN = "CANNOT_BE_PROVEN"

SYSTEM = """You check records in an archive of printed wrestling and boxing material: event programs and magazines from the 1930s to the 1970s.

Each record says that a printed page refers to a named person, and gives the printed text an automated extractor cited for it. The cited text can be a name as printed, a line around the name, or the headline of the story the person was said to appear in. The page evidence you get is described in each request. Machine OCR text comes from scanned paper and can contain recognition errors.

Decide whether the evidence supports that this page refers to this person.

SUPPORTED: the evidence shows that this page refers to this person.
UNSUPPORTED: the evidence shows that it does not. For example, the cited text refers to someone else, is not a name, or is not about this person.
CANNOT BE PROVEN: the evidence you were given does not settle it either way.

A wrong SUPPORTED or UNSUPPORTED counts against you more than CANNOT BE PROVEN does.

Give your reasoning briefly, then end with one line in exactly this form:
VERDICT: SUPPORTED
or VERDICT: UNSUPPORTED
or VERDICT: CANNOT BE PROVEN"""


def _claim_block(rec):
    c, s = rec["claim"], rec["source"]
    where = f"{s['publication']}, {s['date']}" + (f", {s['city']}" if s.get("city") else "") + f", page {s['pdf_page']} of the scan"
    cited = "\n".join(f"  - \"{m}\"" for m in c["mentions"])
    return (f"RECORD\nPerson: {c['entity']}\nPage: {where}\nCited text from the extractor:\n{cited}\n")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def record_to_sample(condition):
    def convert(rec):
        claim = _claim_block(rec)
        if condition == "excerpt":
            ex = rec.get("excerpt") or ""
            ev = ("EVIDENCE: up to fifty words of the page's OCR text, taken from around the cited text.\n"
                  + (f"\"{ex}\"" if ex else "(The cited text was not found in the page's OCR text, so no excerpt is given.)"))
            content = [ContentText(text=claim + "\n" + ev)]
        elif condition == "page_text":
            content = [ContentText(text=claim + "\nEVIDENCE: the page's full OCR text layer.\n<page_text>\n"
                                   + _read(rec["text_path"]) + "\n</page_text>")]
        elif condition == "page_image":
            content = [ContentImage(image=rec["image_path"]),
                       ContentText(text=claim + "\nEVIDENCE: the image above is the scanned page.")]
        elif condition == "page_both":
            content = [ContentImage(image=rec["image_path"]),
                       ContentText(text=claim + "\nEVIDENCE: the image above is the scanned page, and below is its OCR text layer.\n<page_text>\n"
                                   + _read(rec["text_path"]) + "\n</page_text>")]
        else:
            raise ValueError(f"unknown condition {condition!r}")
        return Sample(
            id=rec["id"],
            input=[ChatMessageSystem(content=SYSTEM), ChatMessageUser(content=content)],
            target=rec["label"],
            metadata={
                "split": rec["split"], "assurance": rec["assurance"], "ruled_by": rec["ruled_by"],
                "label_is_abstain": rec["label"] == ABSTAIN,
                "text_layer_has_mention": rec["text_layer_has_mention"],
                "publication": rec["source"]["publication"],
            },
        )
    return convert


@task
def faithful_claim(condition: str = "excerpt", split: str | list[str] = "gold", items: str = DEFAULT_ITEMS,
                   assurance: str | None = None, ids: str | None = None):
    """split: gold | silver | held | all, or a comma list such as gold,held. assurance: blind-page | deliberate | group | rapid | eyes-read (optional filter). ids: a comma list of item ids, or the path of a file with one id per line (optional filter)."""
    if not os.path.isabs(items) and not os.path.exists(items):
        items = os.path.join(os.path.dirname(HERE), items)   # relative to the repo root
    if condition != "excerpt" and "text_path" not in _read(items).split("\n", 1)[0]:
        raise ValueError(f"condition {condition!r} needs the private items file (with text_path / image_path)")
    recs = [json.loads(l) for l in _read(items).splitlines() if l.strip()]
    if split != "all" and split != ["all"]:
        wanted = set(split) if isinstance(split, (list, tuple)) else set(str(split).split(","))
        recs = [r for r in recs if r["split"] in wanted]
    if assurance:
        wanted_a = set(str(assurance).split(","))
        recs = [r for r in recs if r["assurance"] in wanted_a]
    if ids:
        if not os.path.isabs(ids) and not os.path.exists(ids) and os.path.exists(os.path.join(os.path.dirname(HERE), ids)):
            ids = os.path.join(os.path.dirname(HERE), ids)   # Inspect runs tasks from the task file directory
        if os.path.exists(ids):
            with open(ids, encoding="utf-8") as f:
                wanted_ids = {l.strip() for l in f if l.strip()}
        else:
            wanted_ids = set(str(ids).split(","))
        recs = [r for r in recs if r["id"] in wanted_ids]
    conv = record_to_sample(condition)
    return Task(
        dataset=MemoryDataset([conv(r) for r in recs], name=f"faithful_claim-{'+'.join(split) if isinstance(split, (list, tuple)) else split}-{condition}"),
        solver=generate(),
        scorer=verdict_scorer(LABELS, ABSTAIN),
        config=GenerateConfig(max_tokens=16000, cache_prompt=False),
    )
