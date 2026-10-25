"""
answers.py - read parsed verdicts out of Inspect logs, one dict per (model, condition, epoch).

Shared by report_told.py and report_resample.py. report.py keeps its own copy of this walk
and keys answers by (model, condition) with a later log winning; this helper keeps the epoch
and the `standard` task argument too, so a told run or a second epoch never overwrites a
headline answer. Labels are always scored against the CURRENT items file, never the log's
stored target.
"""
import glob
import json
import os
import sys
from collections import defaultdict

from inspect_ai.log import read_eval_log

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from curry_record_evals.scoring import outcome  # noqa: E402

ABSTAIN = {"faithful_claim": "CANNOT_BE_PROVEN", "same_person": "CANNOT_TELL"}
MODEL_ORDER = ["claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5", "claude-fable-5-1"]
RANK = {"right": 2, "abstain": 1, "wrong": 0}


def load_items(path):
    items = {}
    for line in open(path, encoding="utf-8"):
        if line.strip():
            it = json.loads(line)
            items[it["id"]] = it
    task = "same_person" if "same_person" in os.path.basename(path) else "faithful_claim"
    return items, task


def load_answers(logdirs, items, condition=None, standard=None):
    """{(model, condition, epoch): {id: answer}} over every successful log in the dirs
    (comma-separated), a later log winning for the same key. `standard` filters on the task
    argument ('told' / 'untold'); a log without the argument counts as 'untold'."""
    files = []
    for d in logdirs.split(","):
        files += glob.glob(os.path.join(d, "**", "*.eval"), recursive=True)
    out = defaultdict(dict)
    for f in sorted(files, key=os.path.basename):     # names start with the run timestamp
        log = read_eval_log(f)
        if log.status != "success" or not log.samples:
            continue
        model = log.eval.model.split("/")[-1]
        cond = log.eval.task_args.get("condition", "?")
        std = log.eval.task_args.get("standard") or "untold"
        if condition and cond != condition:
            continue
        if standard and std != standard:
            continue
        for s in log.samples:
            if s.id not in items:
                continue
            sc = next(iter(s.scores.values()))
            out[(model, cond, s.epoch)][s.id] = None if sc.answer in (None, "INVALID") else sc.answer
    return out


def groups_of(it):
    """The report groups an item belongs to: gold, and gold:blind-page for the whole-page pairs."""
    if it["split"] != "gold":
        return []
    g = ["gold"]
    if it["assurance"] == "blind-page":
        g.append("gold:blind-page")
    return g


def score(answer, it, abst):
    return outcome(answer, it["label"], abst)


def fmt(x):
    return "-" if x is None else f"{x:.2f}"
