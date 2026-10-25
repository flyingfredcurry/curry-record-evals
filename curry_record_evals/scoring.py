"""
Scoring shared by both tasks: a three-way verdict where abstaining is allowed and
a confident wrong answer costs more than an abstention.

Each sample scores exactly one of:
  right    the model committed and matched the ruling, or the ruling is the
           abstain label and the model abstained
  wrong    the model committed and did not match the ruling (including any
           commitment on an item the ruling holds undecidable)
  abstain  the model abstained on an item the ruling settles
  (an unparseable answer is scored as abstain and flagged as invalid)

Metrics:
  precision   right / (right + wrong): how often a committed answer is right
  coverage    share of settled items the model committed on
  wrong_rate  share of all items answered wrongly with confidence
  net         right_rate - wrong_rate              (a wrong answer costs one right one)
  net_p3      right_rate - 3 * wrong_rate          (a wrong answer costs three)
"""
import re

from inspect_ai.scorer import (
    Metric, SampleScore, Score, Target, metric, scorer, grouped,
)
from inspect_ai.solver import TaskState

VERDICT_RE = re.compile(r"VERDICT\s*:\s*\**\s*([A-Z][A-Z _-]+[A-Z])", re.IGNORECASE)


def parse_verdict(text, allowed):
    """Last 'VERDICT: X' line whose X is one of the allowed labels, or None."""
    norm = {a.replace("_", " "): a for a in allowed}
    found = None
    for m in VERDICT_RE.finditer(text or ""):
        cand = re.sub(r"[\s_-]+", " ", m.group(1).strip().upper())
        for k, v in norm.items():
            if cand.startswith(k):
                found = v
    return found


def _vals(scores: list[SampleScore], key: str):
    return [float((s.score.value or {}).get(key, 0)) for s in scores]


@metric
def precision() -> Metric:
    def m(scores: list[SampleScore]) -> float:
        r, w = sum(_vals(scores, "right")), sum(_vals(scores, "wrong"))
        return r / (r + w) if (r + w) else float("nan")
    return m


@metric
def coverage() -> Metric:
    def m(scores: list[SampleScore]) -> float:
        settled = [s for s in scores if not (s.sample_metadata or {}).get("label_is_abstain")]
        if not settled:
            return float("nan")
        return sum(1.0 - float(s.score.value.get("abstain", 0)) for s in settled) / len(settled)
    return m


@metric
def wrong_rate() -> Metric:
    def m(scores: list[SampleScore]) -> float:
        v = _vals(scores, "wrong")
        return sum(v) / len(v) if v else float("nan")
    return m


@metric
def net() -> Metric:
    def m(scores: list[SampleScore]) -> float:
        if not scores:
            return float("nan")
        return (sum(_vals(scores, "right")) - sum(_vals(scores, "wrong"))) / len(scores)
    return m


@metric
def net_p3() -> Metric:
    def m(scores: list[SampleScore]) -> float:
        if not scores:
            return float("nan")
        return (sum(_vals(scores, "right")) - 3 * sum(_vals(scores, "wrong"))) / len(scores)
    return m


def outcome(answer, label, abstain_label):
    if answer is None or answer == abstain_label:
        return "right" if label == abstain_label else "abstain"
    return "right" if answer == label else "wrong"


def verdict_scorer(labels, abstain_label):
    @scorer(metrics=[
        precision(), coverage(), wrong_rate(), net(), net_p3(),
        grouped(net(), "split", all=False, name_template="net_{group_name}"),
        grouped(precision(), "split", all=False, name_template="precision_{group_name}"),
    ])
    def _scorer():
        async def score(state: TaskState, target: Target) -> Score:
            text = state.output.completion if state.output else ""
            answer = parse_verdict(text, labels)
            label = target.text
            o = outcome(answer, label, abstain_label)
            return Score(
                value={"right": int(o == "right"), "wrong": int(o == "wrong"),
                       "abstain": int(o == "abstain"), "invalid": int(answer is None)},
                answer=answer or "INVALID",
                explanation=text[-1500:],
            )
        return score
    return _scorer()
