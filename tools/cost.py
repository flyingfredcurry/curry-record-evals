"""cost.py - dollar cost of Inspect logs from their recorded token usage.

Prices are Anthropic first-party list prices per million tokens (claude-api skill
table cached 2026-10-06): input, output. Cache writes bill at 1.25x input, cache
reads at 0.1x input. Batch runs bill at half. Usage: python tools/cost.py LOGDIR [--batch]
"""
import glob
import os
import sys

from inspect_ai.log import read_eval_log

PRICES = {
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-opus-5-5": (4.00, 20.00),
    "claude-fable-5-1": (10.00, 50.00),
}


def cost_of(log):
    total = 0.0
    for model, u in (log.stats.model_usage or {}).items():
        name = model.split("/")[-1]
        pin, pout = PRICES.get(name, (0, 0))
        cw = u.input_tokens_cache_write or 0
        cr = u.input_tokens_cache_read or 0
        total += (u.input_tokens * pin + cw * pin * 1.25 + cr * pin * 0.1 + u.output_tokens * pout) / 1e6
    return total


def main(logdir, batch=False):
    grand = 0.0
    for f in sorted(glob.glob(os.path.join(logdir, "**", "*.eval"), recursive=True)):
        log = read_eval_log(f, header_only=True)
        c = cost_of(log) * (0.5 if batch else 1.0)
        grand += c
        n = log.results.completed_samples if log.results else 0
        print(f"{log.eval.model:32s} {log.eval.task_args.get('condition','?'):10s} n={n:4d} ${c:7.3f}  ${c / max(n, 1):.4f}/item  {os.path.basename(f)[:40]}")
    print(f"TOTAL ${grand:.2f}")


if __name__ == "__main__":
    main(sys.argv[1], "--batch" in sys.argv)
