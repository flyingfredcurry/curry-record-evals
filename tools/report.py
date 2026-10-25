"""
report.py - score Inspect logs against the CURRENT items file, by split and assurance.

Labels and splits can change after a run (a held item gets Mike's blind ruling), so the
report never trusts the target stored in a log: it reads each sample's parsed answer and
scores it against the item as it stands now, with the task's own rules
(curry_record_evals/scoring.py). Held items are reported apart and never in gold.

  python tools/report.py logs/gold-v1 data/faithful_claim.jsonl > results/faithful_claim.md
"""
import glob
import json
import math
import os
import re
import sys
from collections import defaultdict

from inspect_ai.log import read_eval_log

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from curry_record_evals.scoring import outcome  # noqa: E402

ABSTAIN = {"faithful_claim": "CANNOT_BE_PROVEN", "same_person": "CANNOT_TELL"}
MODEL_ORDER = ["claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5", "claude-fable-5-1"]


def ci95(p, n):
    """95% confidence half-width on a share p of n items: 1.96 x the binomial standard error,
    the items treated as independent draws (Miller, "Adding Error Bars to Evals", 2024)."""
    return 1.96 * math.sqrt(p * (1 - p) / n) if n else None


def metrics(rows):
    n = len(rows)
    r = sum(o == "right" for o, _ in rows)
    w = sum(o == "wrong" for o, _ in rows)
    a = n - r - w
    settled = [o for o, lab_abs in rows if not lab_abs]
    commit = sum(o != "abstain" for o in settled)
    return {"n": n,
            "correct": r / n if n else None, "wrong": w / n if n else None,
            "abstained": a / n if n else None, "ci95": ci95(r / n, n) if n else None,
            "precision": r / (r + w) if r + w else None,
            "coverage": commit / len(settled) if settled else None,
            "net": (r - w) / n if n else None,
            "net_p3": (r - 3 * w) / n if n else None}


LEGEND = (
    "Scored against the current items file, so a label that moved after a run is scored as it stands now. "
    "`correct`, `wrong` and `abstained` are shares of all n items and sum to one: correct is a verdict that "
    "matches the ruling, or an abstention on an item the ruling holds undecidable; wrong is a verdict that does "
    "not match, including any verdict on an undecidable item; abstained is an abstention on an item the ruling "
    "settles. `ci95` is the 95% confidence half-width on correct (1.96 x the binomial standard error, items "
    "treated as independent; Miller 2024). `precision` = correct / (correct + wrong), the share of answers that "
    "were right when the model did not abstain on a settled item (SimpleQA's \"correct given attempted\"). "
    "`coverage` = share of settled items the model gave a verdict on. `net` = correct - wrong; `net_p3` = "
    "correct - 3 x wrong, for a use where a confident error costs three right answers.\n")


def fmt(x):
    return "-" if x is None else f"{x:.2f}"


def main(logdir, items_path):
    items = {json.loads(l)["id"]: json.loads(l) for l in open(items_path, encoding="utf-8") if l.strip()}
    task = "same_person" if "same_person" in os.path.basename(items_path) else "faithful_claim"
    abst = ABSTAIN[task]
    cells = defaultdict(list)       # (model, condition, group) -> [(outcome, label_is_abstain)]
    answers = defaultdict(dict)     # (model, condition) -> {id: answer}; a later log wins
    files = []
    for d in logdir.split(","):
        files += glob.glob(os.path.join(d, "**", "*.eval"), recursive=True)
    for f in sorted(files, key=os.path.basename):     # names start with the run timestamp
        log = read_eval_log(f)
        if log.status != "success" or not log.samples:
            continue
        model = log.eval.model.split("/")[-1]
        cond = log.eval.task_args.get("condition", "?")
        for s in log.samples:
            if s.id not in items:
                continue
            sc = next(iter(s.scores.values()))
            answers[(model, cond)][s.id] = None if sc.answer in (None, "INVALID") else sc.answer
    for (model, cond), by_id in answers.items():
        for sid, ans in by_id.items():
            it = items[sid]
            o = outcome(ans, it["label"], abst)
            lab_abs = it["label"] == abst
            if it["split"] == "held":
                groups = ["held"]
            elif it["split"] == "gold":
                groups = ["gold", f"gold:{it['assurance']}"]
                if task == "faithful_claim" and it["assurance"] == "blind-page":
                    # a record whose stored name is one word (Dorothy, Marshall) was ruled on whether the
                    # record should exist in that form, a different question; show the two apart
                    one = len(re.findall(r"[A-Za-z']+", it["claim"]["entity"])) == 1
                    groups.append("gold:blind-page:" + ("one-word-name" if one else "full-name"))
            else:
                groups = [it["split"]]
            for g in groups:
                cells[(model, cond, g)].append((o, lab_abs))
    conds = sorted({c for _, c, _ in cells})
    groups = sorted({g for _, _, g in cells}, key=lambda g: (g != "gold", g))
    out = [f"# {task}: model results\n", LEGEND]
    if any(it["split"] == "held" for it in items.values()):
        out.append("CAUTION: `held` items carry a July ruling that the page text contradicts on its face; "
                   "they wait on a blind re-ruling and are never counted in gold. Taking them out of gold "
                   "removes the items most likely to disagree with a model, so gold scores run high until "
                   "they return. Read gold and held together.\n")
    for g in groups:
        out.append(f"\n## {g}\n")
        out.append("| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|")
        for m in MODEL_ORDER:
            for c in conds:
                rows = cells.get((m, c, g))
                if rows:
                    k = metrics(rows)
                    out.append(f"| {m} | {c} | {k['n']} | {fmt(k['correct'])} | {fmt(k['wrong'])} | "
                               f"{fmt(k['abstained'])} | {fmt(k['ci95'])} | {fmt(k['precision'])} | "
                               f"{fmt(k['coverage'])} | {fmt(k['net'])} | {fmt(k['net_p3'])} |")
    print("\n".join(out))
    json.dump({f"{m}|{c}": a for (m, c), a in answers.items()},
              open(os.path.join(logdir.split(",")[0], f"answers-{task}.json"), "w", encoding="utf-8"), indent=0)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "data/faithful_claim.jsonl")
