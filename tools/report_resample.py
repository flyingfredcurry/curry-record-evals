"""
report_resample.py - how much a single sample moves: the headline run plus two more samples
per item (`--epochs 2`), every draw scored against the current items file.

  python tools/report_resample.py logs/gold-v1,logs/gold-v1b,logs/gold-v1c,logs/blind-v1 logs/resample-v1 excerpt data/faithful_claim.jsonl > results/resampling-faithful_claim.md
  python tools/report_resample.py logs/blind-v1 logs/resample-v1 text data/same_person.jsonl > results/resampling-same_person.md

Sample 0 is the headline run (the baseline dirs, a later log winning per item, exactly as
report.py merges them); samples 1 and 2 are epochs 1 and 2 of the resample dir. An item
`agrees` when all three verdicts are the same string; the flip rate is the rest. The
majority verdict is the one two or three samples gave; a three-way split is scored as an
abstention.
"""
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from answers import ABSTAIN, MODEL_ORDER, fmt, groups_of, load_answers, load_items, score  # noqa: E402
from report import ci95, metrics  # noqa: E402

LEGEND = (
    "Sample 0 is the headline run; samples 1 and 2 are two more draws of the same prompt (`--epochs 2`), "
    "same model, same evidence. `agree` is the share of items where all three verdicts match; `flip rate` "
    "is the rest. `correct` per sample is the headline metric re-scored on each draw; `spread` is its "
    "lowest to highest across the three. `majority` scores the verdict two or three samples gave, a "
    "three-way split counted as an abstention. `ci95` is on the single-sample (s0) correct share, for "
    "comparison with the spread.\n")


def main(base_dirs, resample_dir, condition, items_path):
    items, task = load_items(items_path)
    abst = ABSTAIN[task]
    base = load_answers(base_dirs, items, condition=condition, standard="untold")
    res = load_answers(resample_dir, items, condition=condition, standard="untold")
    out = [f"# {task}, {condition}: three samples per item\n", LEGEND]
    for group in ["gold", "gold:blind-page"]:
        out.append(f"\n## {group}\n")
        out.append("| model | n | agree | flip rate | correct s0 | s1 | s2 | spread | ci95 | majority correct | wrong | abstained | precision |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        notes = []
        for m in MODEL_ORDER:
            s0 = base.get((m, condition, 1), {})
            s1 = res.get((m, condition, 1), {})
            s2 = res.get((m, condition, 2), {})
            gids = [i for i in items if group in groups_of(items[i])]
            ids = [i for i in gids if i in s0 and i in s1 and i in s2]
            missing = len(gids) - len(ids)
            if not ids:
                continue
            agree = sum((s0[i] or "INVALID") == (s1[i] or "INVALID") == (s2[i] or "INVALID") for i in ids)
            corr = []
            for s in (s0, s1, s2):
                rows = [(score(s[i], items[i], abst), items[i]["label"] == abst) for i in ids]
                corr.append(metrics(rows)["correct"])
            maj_rows = []
            splits = 0
            for i in ids:
                votes = Counter((s[i] or abst) for s in (s0, s1, s2))
                v, n = votes.most_common(1)[0]
                if n == 1:
                    splits += 1
                    v = abst
                maj_rows.append((score(v, items[i], abst), items[i]["label"] == abst))
            k = metrics(maj_rows)
            n = len(ids)
            out.append(f"| {m} | {n} | {agree / n:.2f} | {1 - agree / n:.2f} | {fmt(corr[0])} | {fmt(corr[1])} | "
                       f"{fmt(corr[2])} | {fmt(min(corr))} to {fmt(max(corr))} | {fmt(ci95(corr[0], n))} | "
                       f"{fmt(k['correct'])} | {fmt(k['wrong'])} | {fmt(k['abstained'])} | {fmt(k['precision'])} |")
            if missing or splits:
                notes.append(f"- {m}: {missing} of {len(gids)} items lack one of the three samples and are left out; "
                             f"{splits} three-way splits scored as abstentions.")
        if notes:
            out.append("")
            out.extend(notes)
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
