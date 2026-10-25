# curry-record-evals

Two evaluations built from one family's pro wrestling archive: scanned event programs and
magazines printed from the 1930s to the 1970s. Each puts to a model a judgment the archive's
keeper has already made by hand with the printed page in front of him. Each lets the model
say the page does not settle it, and scores a confident wrong answer as worse than an honest
abstention.

- **faithful_claim**: an extractor says a printed page refers to a named person and cites
  the text it matched. Does the page support that? SUPPORTED, UNSUPPORTED, or CANNOT BE
  PROVEN. 300 hand-labeled items.
- **same_person**: two records carry names that look alike. Are they one person? SAME,
  DIFFERENT, or CANNOT TELL. 90 hand-labeled pairs.

Both run on [Inspect](https://inspect.aisi.org.uk/). The answer key has never been
published; the pages are the archive's own scans.

The rulings are the keeper's. Everything else was built with Claude, Anthropic's model,
working in Claude Code at his direction, and read by him before it was published. The last
section says who did what.

**At a glance.** Four Claude models, October 2026. On the 300 claims, given a fifty-word
excerpt, they score correct 0.70 to 0.79 and wrong 0.03 to 0.05, abstaining on the rest;
given the whole page, correct 0.83 to 0.93. On the 90 pairs, given the transcriptions,
correct 0.47 to 0.61 and wrong 0.02 to 0.07, abstaining on a third to a half; given the page
crops, correct 0.63 to 0.77. The models are reliable when they answer. Told the archive's
standard in so many words, they abstain more, which costs them on the whole set and pays on
the hardest pairs. Every label is one person's. The 95% intervals are about ±0.05 on the 300
and ±0.10 on the 90.

## Why these two questions

The archive's rule is that its public site never says what the record cannot source. These
two judgments decide whether that rule holds, and they come up thousands of times. A string
match fails both ways. A name can be printed and belong to another man: "Freddy Welsh" is
not Flying Fred Curry. A name can be on the paper but not in the OCR text: a slanted 1931
line reads "Jack Dempsey's" in print and "Map Dempsey's" in the text layer. Names repeat
across decades and territories. One family in this archive has three men named Fred Curry.

The same-person standard is strict, and the model is not told it. Two names are one man
only when the pages tie them: one card prints both for one man, or both carry the same
partner, manager, title or billing. They are two people when the pages show two people, or
two sports or decades with nothing joining them. When the only tie is the name, the answer
is CANNOT TELL. That clause is for two men who share a name. One name printed two ways in
the same magazines in the same years, a swapped letter, a line break, a billing, is one man
to the keeper, not a second name. A second run tells the model the standard and measures
what the telling buys.

## Usage

```
pip install -e .
inspect eval curry_record_evals/faithful_claim.py --model anthropic/claude-sonnet-5-5
inspect eval curry_record_evals/same_person.py --model anthropic/claude-sonnet-5-5
```

`-T split=gold|silver|all` picks the labels (default `gold`, the keeper's rulings);
`-T assurance=blind-page` runs one group of rulings (the values are in Dataset);
`-T ids=FC-0001,FC-0002` runs a subset; on same_person, `-T standard=told` puts the standard
in the system prompt. The whole-page conditions (`page_text`, `page_image`, `crops`) need
the archive's private files and do not run from this repository. `tools/report.py`
re-scores stored logs against the current data files; `tools/report_told.py` and
`tools/report_resample.py` write the told-standard and resampling tables;
`baselines/run_baselines.py` scores the no-model baselines; `tools/check_ship.py` checks
that no shipped file carries more than fifty printed words from any page, and no private
path or log.

## Dataset

Each item is one judgment with the evidence a reader needs to check it against the print.
A faithful_claim item carries the publication, date and page, the stored name, the
extractor's cited text, and up to fifty words of OCR text around it. A same_person item
carries each record's name and up to three places it is printed, with a short
transcription. No page images and no full OCR text ship here.

**Who labeled.** Mike Curry, the archive's keeper, made every ruling in the `gold`
split.

- 70 claims and 79 pairs were ruled blind for this eval in October 2026, the page in view,
  no earlier call shown (`assurance` values `blind-page` and `blind`). The 70 claims and 34
  of the pairs were ruled twice in one evening, because the first sheet cropped the page and
  on some cards hid the name. The whole-page ruling is the label; the crop ruling stays on
  the claim items as `crop_ruling`. Six cards were ruled a third time after Claude flagged
  them against the page text (`reruled_after_flag`).
- 230 claims were ruled on the archive's own review sheet in July 2026 (`deliberate`,
  `group` or `rapid`), with a model's proposed verdict in view, so they may lean toward it.
  Every July ruling the page text contradicted on its face was held out and ruled again
  blind; those 30 are among the 70.
- 11 pairs come from the archive's look-alike walk-through of October 2026 (`single`,
  `question`).

A further 236 faithful_claim items carry labels from Claude's reads of the page images,
accepted during the archive's build but never ruled one at a time by a person (the `silver`
split). They were not run and never enter a `gold` number.

Every item names who ruled it, how and when. Every claim item carries a one-line rationale
shaped from the keeper's note; the pair items carry Claude's earlier call. `data/CARD.md`
has the counts; `data/LABEL-HISTORY.md` tells what moved, when, and why.

**Balance.** faithful_claim: 184 SUPPORTED, 104 UNSUPPORTED, 12 CANNOT BE PROVEN.
same_person: 48 SAME, 29 DIFFERENT, 13 CANNOT TELL.

**CANNOT BE PROVEN means one thing here.** In the keeper's words, "can't be proven by the
page I'm looking at." It is not "I don't know who this is." A model that commits on such an
item is scored wrong.

**Seven of the 70 blind claims carry a one-word record name** (Browser, Dorn, Dorothy twice,
Weasel, Marshall, Diane). The keeper ruled each UNSUPPORTED because the record should carry
the fuller name the page prints. That is a different question, so the results report the 70
with and without them.

## Scoring

The grader is deterministic: it reads the model's final `VERDICT:` line. **Correct**: the
verdict matches the ruling, or the model abstains on an item ruled undecidable. **Wrong**:
the verdict does not match, or the model commits on an undecidable item. **Abstained**: the
model says CANNOT on an item the keeper settled. The three sum to one. **Correct given
attempted** is correct / (correct + wrong), SimpleQA's measure of how often an answer is
right when the model gives one. The tables in `results/` also give `coverage`, the share of
settled items the model answered; `net`, correct minus wrong; and `net_p3`, correct minus
three times wrong. Every table carries a 95% confidence half-width on correct, 1.96 times
the binomial standard error, as Anthropic's "Adding Error Bars to Evals" recommends.

Labels can move after a run. `tools/report.py` never trusts the target stored in a log; it
scores each stored answer against the item as it stands now.

## Results

October 2026: claude-haiku-5-5, claude-sonnet-5-5, claude-opus-5-5 and claude-fable-5-1,
one sample per item, default settings, through the Batch API, every model on the same items.
The public condition for faithful_claim is `excerpt`, the claim and up to fifty words of OCR
text around the cited text; the archive also ran `page_text` and `page_image`. The public
condition for same_person is `text`, the names, places printed and short transcriptions;
the archive also ran `crops`, the page crops alone, and `both`. Full tables for every
condition and every group of rulings are in `results/`.

**faithful_claim, 300 gold items, excerpt.** The 95% half-width on correct is about ±0.05.

| model | correct | wrong | abstained | correct given attempted |
|---|---|---|---|---|
| Claude Haiku 5.5 | 0.79 | 0.05 | 0.16 | 0.94 |
| Claude Sonnet 5.5 | 0.70 | 0.03 | 0.26 | 0.95 |
| Claude Opus 5.5 | 0.73 | 0.03 | 0.24 | 0.96 |
| Claude Fable 5.1 | 0.75 | 0.03 | 0.22 | 0.96 |

Given the whole page, as text or as image, every model abstains less and stays about as
reliable: correct 0.83 to 0.93, wrong 0.04 to 0.06. On the 70 claims ruled blind for this
eval, the hardest set, correct is 0.69 to 0.76 and wrong 0.10 to 0.16 (±0.10); leave out the
seven one-word records and it is correct 0.76 to 0.84, wrong 0.05 to 0.08. On the seven, no
model gets one right.

Baselines on the 300, same scoring. A rule that says SUPPORTED when every token of the
stored name is in the page's OCR text is correct 0.58, wrong 0.04. Always SUPPORTED is
correct 0.61, wrong 0.39. The model verifier the archive ran in July 2026 is correct 0.42,
wrong 0.13 on the 260 items it saw.

**same_person, 90 gold pairs, text.** The 95% half-width on correct is about ±0.10.

| model | correct | wrong | abstained | correct given attempted |
|---|---|---|---|---|
| Claude Haiku 5.5 | 0.47 | 0.02 | 0.51 | 0.95 |
| Claude Sonnet 5.5 | 0.54 | 0.03 | 0.42 | 0.94 |
| Claude Opus 5.5 | 0.59 | 0.02 | 0.39 | 0.96 |
| Claude Fable 5.1 | 0.61 | 0.07 | 0.32 | 0.90 |

The models are reliable when they answer and abstain on a third to a half of the pairs.
Given the page crops instead, every model abstains less and gets more right:
correct 0.63 to 0.77, wrong 0.04 to 0.11. Crops and transcriptions together are no better
than the crops alone. On the 34 pairs ruled on the whole-page sheet, the hardest, correct
falls to 0.44 to 0.50 on the text (±0.17), and the crops raise wrong for all four models, to
0.09 to 0.24.

**Told the standard** (`results/told-standard.md`). A second same_person run put the
standard above into the system prompt. Told, every model abstains more and gets less right
on the 90: correct 0.36 to 0.48 on the text and 0.44 to 0.62 on the crops. Most of the flips
are SAME to CANNOT TELL, on pairs the keeper ruled SAME. On the 34 hardest pairs it
reverses: correct rises for every model on the text and holds or rises on the crops, and
wrong on the crops falls to 0.03 to 0.09.
Stating the standard buys caution, and on this set the caution paid only on the hardest
pairs.

## Reading the transcripts

Anthropic's guidance on evals says to read the transcripts and ask whether the failures seem
fair. Three items from the public-condition logs, quoted from the models' own reasoning.

**Carl Pojello, The Ring, 1931, and Karl Pojello, Wrestling World, 1964.** Two bare names,
thirty-three years apart. The keeper ruled CANNOT TELL. Fable said SAME, from the career:
"the Lithuanian-American wrestler ... who later managed Maurice Tillet ... Pojello died in
1954." Opus knew the same career and said CANNOT TELL: "Outside knowledge is not record
evidence." The page evidence was identical; what differed was whether a known career counts
as evidence.

**Bob Geigel and Bob Giegel, Wrestling World, 1963 to 1968.** The keeper ruled SAME: one
name, one magazine, the same years. Untold, Sonnet, Opus and Fable said SAME. Told, three
models abstained; Opus: "No page, card or issue prints both 'Geigel' and 'Giegel' for one
man." The standard as written reads a misprint as a second name. The keeper does not. That
gap is most of what the told run measures on the 90.

**"Marshall", a one-word record, on a page that prints Everett Marshall.** The keeper ruled
UNSUPPORTED, because the record should carry the name the page prints. Haiku said SUPPORTED:
"The surname-only person label is a shortened form of the full name in the cited text." The
model answered the question as asked. The keeper answered whether the record should exist in
that form. The results report the seven one-word records apart for that reason.

## Known limitations

- One annotator. Every gold label is one person's, with no second reader. The nearest
  check is his agreement with Claude's earlier reads of the same pages
  (`results/blind-sitting.md`): 39 of 40 blind claims and 60 of 79 pairs agree. A second
  annotator on a sample is the obvious next step.
- Small. 300 and 90 gold items, 70 and 79 of them ruled blind for this eval. The
  intervals say what that buys: ±0.05 on the 300, ±0.10 on the 70 and on the 90, ±0.17 on
  the 34.
- One sample per item in the headline tables. Two more samples per item on the public
  conditions (`results/resampling-faithful_claim.md`, `results/resampling-same_person.md`)
  agree with the first on 0.82 to 0.97 of items and move the correct share by at most 0.02
  on the 300, 0.05 on the 90 and 0.07 on the 70. Items cluster by page and the intervals
  treat them as independent. Model comparisons are not paired.
- The 70 claims and 34 pairs were labeled by one person twice in one evening. 31 of the
  claims and 23 of the pairs changed between the first ruling and the second, and six items
  changed a third time after a flag.
- The 230 July claim rulings were made with a model's verdict in view.
- faithful_claim is mostly one magazine, The Ring, 1931, 1932 and 1934. English-language
  American print only.
- The standard is this archive's and stricter than common sense. A surname alone binds
  nobody, and a model that knows a famous career is scored wrong for committing where the
  pages do not tie the names.
- The standard is stated here in a few sentences, and the keeper's rulings carry more than
  the sentences do: the misprint clause above was written after the told run showed the gap.
  Take the rulings, not the sentences, as the standard.

## How this was made, and by whom

Mike Curry, the archive's keeper, made every ruling with the page in view. Dataset says what
else each group of rulings had in view. Claude, Anthropic's model working in Claude Code,
built everything else at his direction: the items from the archive's records, the two
sitting sheets, the Inspect tasks and the scorer, the baselines, the report tools, the model
runs, and the first draft of every sentence here.

Claude flagged; he ruled. When all four models in every condition disagreed with the answer
key on sixteen claims, Claude read the items and found the sheet had cropped the names off
the cards. He sat the whole-page pass the same evening and the labels moved. Claude read the
new rulings against the page text and flagged six; he looked again and re-ruled all six.
Before this text was called finished he read it word for word against the files on disk,
and nine sentences were narrowed to what the files support. Every number here comes from a
table in `results/` that a tool in `tools/` wrote from the logs. Nothing is quoted from
memory.

What Claude could not do: rule an item, write to the archive's live database (this work
read it and never wrote it), or publish on its own. The keeper created this repository and
gave the word; Claude ran the push. The pages, the full OCR text, Claude's own answer key
for the blind sitting and his raw notes stay in the archive's private folder, so no shipped
file carries more than a short quotation from any printed page.

The model runs cost $71.51 of the $112.95 he set aside, at Batch API prices.

## Related

- [faithful-cite](https://github.com/flyingfredcurry/faithful-cite): the
  deterministic-first claim checker this eval uses as a baseline.
- [curry-legacy-governance](https://github.com/flyingfredcurry/curry-legacy-governance):
  the governance layer the archive is run under.
- The archive itself: [currywrestlinglegacy.com](https://currywrestlinglegacy.com).

## Changelog

- 0.1.0, October 2026: first public release. Four Claude models on both tasks; the
  told-standard, resampling and `both` runs reported.

## License

Code: MIT (`LICENSE`). Data: CC BY 4.0 (`data/LICENSE`).
