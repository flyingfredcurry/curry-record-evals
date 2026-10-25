"""
same_person: are two printed names one person?

The archive holds one record per person. A checker found pairs of records whose
names look alike. For each pair the model sees, per side, the name as recorded and
up to three places it is printed (publication, date, page, a short transcription),
and answers SAME, DIFFERENT, or CANNOT TELL.

The standard the rulings were made under: SAME only when the pages tie the two (one
page, card or issue prints both for one man, or both carry the same partner,
manager, title or billing); DIFFERENT when the pages show two people, or two sports
or decades with nothing joining them; CANNOT TELL when the only tie is the name.
The model is NOT told this standard; the eval measures whether it holds it unprompted.
With `-T standard=told` the standard is appended to the system prompt, to measure what
telling it buys; the default and the headline numbers are `untold`.

Conditions (task parameter `condition`):
  text    the public condition: names, places, short transcriptions (50 words per item)
  crops   the page crops for every place, no transcription   (needs the private items file)
  both    crops and transcriptions                           (needs the private items file)
"""
import json
import os

from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.model import ChatMessageSystem, ChatMessageUser, ContentImage, ContentText, GenerateConfig
from inspect_ai.solver import generate

from curry_record_evals.scoring import verdict_scorer

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ITEMS = os.path.join(os.path.dirname(HERE), "data", "same_person.jsonl")
LABELS = ["SAME", "DIFFERENT", "CANNOT_TELL"]
ABSTAIN = "CANNOT_TELL"

SYSTEM = """You work on an archive of printed wrestling and boxing material: event programs and magazines from the 1930s to the 1970s. The archive keeps one record per person.

Two records have names that look alike. For each, you get the name as recorded and some of the places it is printed. Decide whether the two records are one person.

SAME: they are one person.
DIFFERENT: they are two people.
CANNOT TELL: the evidence you were given does not settle it.

A wrong SAME or DIFFERENT counts against you more than CANNOT TELL does.

Give your reasoning briefly, then end with one line in exactly this form:
VERDICT: SAME
or VERDICT: DIFFERENT
or VERDICT: CANNOT TELL"""

STANDARD_TOLD = """

The archive's standard, which your verdict will be scored against: SAME only when the pages tie the two (one page, card or issue prints both names for one man, or both carry the same partner, manager, title or billing). DIFFERENT when the pages show two people, or two sports or two decades with nothing joining them. CANNOT TELL when the only tie between the records is the name itself, however alike. What you know of a career from outside these pages does not tie them."""


def _side_text(label, side, with_text):
    lines = [f"{label}: {side['name']}"]
    for r in side["receipts"]:
        line = f"  - printed in {r['where']}"
        if with_text and r.get("printed"):
            line += f": \"{r['printed']}\""
        lines.append(line)
    return "\n".join(lines)


def record_to_sample(condition, system=SYSTEM):
    def convert(rec):
        a, b = rec["a"], rec["b"]
        if condition == "text":
            content = [ContentText(text=_side_text("RECORD 1", a, True) + "\n\n" + _side_text("RECORD 2", b, True)
                                   + "\n\nThe quoted text is a short transcription of each printed place.")]
        elif condition in ("crops", "both"):
            with_text = condition == "both"
            content = []
            for lab, side in (("RECORD 1", a), ("RECORD 2", b)):
                content.append(ContentText(text=_side_text(lab, side, with_text) + f"\nThe images below are crops of the pages above, in the same order ({lab})."))
                for r in side["receipts"]:
                    content.append(ContentImage(image=r["crop_path"]))
        else:
            raise ValueError(f"unknown condition {condition!r}")
        return Sample(
            id=rec["id"],
            input=[ChatMessageSystem(content=system), ChatMessageUser(content=content)],
            target=rec["label"],
            metadata={"split": rec["split"], "assurance": rec["assurance"], "ruled_by": rec["ruled_by"],
                      "label_is_abstain": rec["label"] == ABSTAIN},
        )
    return convert


@task
def same_person(condition: str = "text", split: str | list[str] = "gold", items: str = DEFAULT_ITEMS,
                assurance: str | None = None, ids: str | None = None, standard: str = "untold"):
    """split: gold | silver | held | all, or a comma list such as gold,held. assurance: blind-page | blind | blind-outside | single | question | eyes-read (optional filter). ids: a comma list of item ids, or the path of a file with one id per line (optional filter). standard: untold (default; the model is not told the archive's standard) | told (the standard is appended to the system prompt)."""
    if standard not in ("untold", "told"):
        raise ValueError(f"standard must be untold or told, got {standard!r}")
    if not os.path.isabs(items) and not os.path.exists(items):
        items = os.path.join(os.path.dirname(HERE), items)
    with open(items, encoding="utf-8") as f:
        recs = [json.loads(l) for l in f if l.strip()]
    if condition != "text" and "crop_path" not in json.dumps(recs[0]):
        raise ValueError(f"condition {condition!r} needs the private items file (with crop_path)")
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
    conv = record_to_sample(condition, SYSTEM + STANDARD_TOLD if standard == "told" else SYSTEM)
    return Task(
        dataset=MemoryDataset([conv(r) for r in recs], name=f"same_person-{'+'.join(split) if isinstance(split, (list, tuple)) else split}-{condition}" + ("-told" if standard == "told" else "")),
        solver=generate(),
        scorer=verdict_scorer(LABELS, ABSTAIN),
        config=GenerateConfig(max_tokens=16000, cache_prompt=False),
    )
