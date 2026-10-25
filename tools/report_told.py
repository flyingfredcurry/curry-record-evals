"""
report_told.py - same_person with the archive's standard TOLD to the model, against the
headline UNTOLD run, on the same items and the gold split.

  python tools/report_told.py logs/told-v1 logs/blind-v1 data/same_person.jsonl > results/told-standard.md

The told logs come from `-T standard=told` (same_person.py appends STANDARD_TOLD to the
system prompt). Untold is the default and the headline number. A flip is an item whose
verdict changed when told: it counts `toward` gold when the outcome rank rose
(wrong < abstained < correct), `away` when it fell, `lateral` when the verdict changed and
the rank did not (DIFFERENT to SAME on an item where both are wrong).
"""
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from answers import ABSTAIN, MODEL_ORDER, RANK, fmt, groups_of, load_answers, load_items, score  # noqa: E402
from report import metrics  # noqa: E402

LEGEND = (
    "Same items, same models, same page evidence. UNTOLD is the headline run: the model is not given the "
    "archive's same-person standard. TOLD appends the standard to the system prompt (`-T standard=told`): "
    "SAME only when the pages tie the two names, DIFFERENT when the pages show two people, CANNOT TELL when "
    "the only tie is the name. Shares are of all n items and sum to one; `ci95` is 1.96 x the binomial "
    "standard error on correct; `precision` = correct / (correct + wrong). A flip is an item whose verdict "
    "changed when told: `toward` gold when the outcome improved (wrong -> abstained -> correct), `away` when "
    "it worsened, `lateral` when the verdict changed and the outcome did not.\n")


def main(told_dir, untold_dir, items_path):
    items, task = load_items(items_path)
    abst = ABSTAIN[task]
    told = load_answers(told_dir, items, standard="told")
    untold = load_answers(untold_dir, items, standard="untold")
    conds = sorted({c for _, c, _ in told})
    out = [f"# {task}: the standard told against untold\n", LEGEND]
    for group in ["gold", "gold:blind-page"]:
        out.append(f"\n## {group}\n")
        out.append("| model | condition | standard | n | correct | wrong | abstained | ci95 | precision | coverage | net |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|")
        flip_rows = []
        for m in MODEL_ORDER:
            for c in conds:
                a_t = told.get((m, c, 1), {})
                a_u = untold.get((m, c, 1), {})
                gids = [i for i in items if group in groups_of(items[i])]
                ids = [i for i in gids if i in a_t and i in a_u]
                missing = len(gids) - len(ids)
                if not ids:
                    continue
                for label, ans in (("untold", a_u), ("told", a_t)):
                    rows = [(score(ans[i], items[i], abst), items[i]["label"] == abst) for i in ids]
                    k = metrics(rows)
                    out.append(f"| {m} | {c} | {label} | {k['n']} | {fmt(k['correct'])} | {fmt(k['wrong'])} | "
                               f"{fmt(k['abstained'])} | {fmt(k['ci95'])} | {fmt(k['precision'])} | "
                               f"{fmt(k['coverage'])} | {fmt(k['net'])} |")
                trans = Counter()
                toward = away = lateral = 0
                for i in ids:
                    u, t = a_u[i] or "INVALID", a_t[i] or "INVALID"
                    if u == t:
                        continue
                    trans[(u, t)] += 1
                    ru = RANK[score(a_u[i], items[i], abst)]
                    rt = RANK[score(a_t[i], items[i], abst)]
                    if rt > ru:
                        toward += 1
                    elif rt < ru:
                        away += 1
                    else:
                        lateral += 1
                top = ", ".join(f"{u} -> {t} {n}" for (u, t), n in trans.most_common(6))
                tail = f" (missing {missing})" if missing else ""
                flip_rows.append(f"| {m} | {c} | {len(ids)} | {sum(trans.values())} | {toward} | {away} | "
                                 f"{lateral} | {top or '-'}{tail} |")
        out.append("\n| model | condition | n | flips | toward gold | away | lateral | transitions (untold -> told) |")
        out.append("|---|---|---|---|---|---|---|---|")
        out.extend(flip_rows)
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
