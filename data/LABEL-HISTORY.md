# How the labels were made

The README gives the short version. This file keeps the whole of it: who ruled each item,
how, in what order, and what moved. The counts come from `CARD.md` and the `assurance`
field on every item.

## Who ruled

Mike Curry, the keeper of the archive, made every expert ruling. Claude (Anthropic's
model, working in Claude Code) built the items, the sitting sheets and the harness, and
made the model-read labels described at the end.

## The expert labels, by how they were made

Every item carries an `assurance` value that says how its ruling was made. From most to
least careful:

**blind-page** (70 claims, 34 pairs). Ruled in October 2026 on a sheet built for this
eval, the whole scanned page in view, no earlier call shown. These were ruled twice in one
evening. The first sheet (2026-10-19, sat 2026-10-21 afternoon) showed a crop of the page cut
around the text the extractor had cited. That design had a flaw: when the cited text was a
column head, the person's name sat outside the crop, and the keeper could only answer
CAN'T TELL. He said so on the sheet: "can't be proven by the page I'm looking at." The
same evening a second sheet showed every one of the 70 claims on its whole page, and every
pair the first sheet had left at CAN'T TELL with each receipt on its whole page, reshuffled,
the model's own question on each card. The whole-page ruling is the label. The crop ruling
stays on the claim items as `crop_ruling`. 31 of the 70 claims moved (16 to SUPPORTED, 11 to
UNSUPPORTED, 4 to CANNOT BE PROVEN) and 23 of the 34 pairs (19 to DIFFERENT, 4 to SAME).

What exposed the crop flaw: on 16 of the 70 claims all four models in all three conditions
had agreed against the crop ruling. Anthropic's own guidance on evals says a failure that
uniform "is most often a signal of a broken task, not an incapable agent", and reading the
items confirmed it. After the whole-page pass 15 of those 16 carry the models' answer; the
one left is a one-word record (below).

Six cards were ruled a third time. After the whole-page rulings, Claude read them against
the page text and flagged four claims in chat (a page that prints the name twice; two pages
about one man ruled two ways; a page that says only "Dempsey drew $4,000"; a note that named
the page's men as others) and two pairs the keeper had called DIFFERENT on the decades alone,
or on two newsprint photographs he did not trust. He looked again and re-ruled all six; the
two pairs went to CANNOT TELL. Those items carry `reruled_after_flag: true` and their
rationale tells the sequence.

Two of the 70 claims (FC-0105, FC-0253) are weaker still: Claude had told the keeper what
those pages print before the first sheet. Their rationale says so.

**blind** (45 pairs). Ruled once on the first sheet, page crops in view, no earlier call
shown. These are the pairs the crops settled as SAME or DIFFERENT. Only the CAN'T TELL pairs
went to the whole-page sheet.

**single** (9 pairs) and **question** (2 pairs). Ruled one at a time in the archive's
look-alike walk-through of 2026-10-03, the crop in front of him; `question` means he ruled
after asking what the page showed.

**deliberate** (23 claims), **group** (168 claims), **rapid** (39 claims). Rulings from the
archive's own review sheet of July 2026, graded after the fact by how they were made:
`deliberate` is one row at a time with more than five seconds since the previous click or
with a written note; `group` is one click for all of one person's rows; `rapid` is one row
within five seconds of the previous click.

Two cautions apply to the July sheet. It showed a model's proposed verdict beside every
row, so those rulings may lean toward the model. And its "kill" sometimes meant "this
record should not carry the line" (a duplicate record, to be merged), which is not the same
as "the page does not refer to this person". A hand check against the page images found
both problems (`../results/LABEL-AUDIT.md`). Every July ruling the page text contradicted
on its face (a kill whose surname is printed on the page, or a keep whose surname is not
in the text) was held out of the expert set until the keeper ruled it again blind. All 30
of those are now among the 70 blind-page claims; he agreed with his own July ruling on 4
of the 30 (`../results/blind-sitting.md`).

## What the labels mean

**CANNOT BE PROVEN means one thing here.** In the keeper's words, "can't be proven by the
page I'm looking at." It is not "I don't know who this is." A model that commits on such
an item is scored wrong, by design.

**The same-person standard** the rulings were made under, which the model is not told: two
names are the same man only when the pages tie them (one card prints both for one man, or
both carry the same partner, manager, title or billing). They are different people when the
pages show two people, or two sports or decades with nothing joining them. When the only tie
is the name, the answer is CANNOT TELL. Spelling likeness alone is never enough.

**Seven of the 70 blind claims carry a one-word name** (FC-0015 Browser, FC-0211 Dorn, FC-0498 and
FC-0503 Dorothy, FC-0500 Weasel, FC-0512 Marshall, FC-0517 Diane). The keeper ruled every
one UNSUPPORTED and wrote the fuller name the page prints ("It is this person, but he should
be in the record as Everett Marshall, not Marshall"). That ruling answers whether the record
should exist in that form, a different question from whether the page refers to the person.
They stay in the expert set as ruled, and `tools/report.py` scores the 70 in two lines,
`gold:blind-page:full-name` (63) and `gold:blind-page:one-word-name` (7), so a reader can
weigh them apart. On the seven, every model's precision is 0.00.

## Agreement with earlier calls

`tools/agreement.py` counts how often the blind rulings agreed with an earlier call the
keeper could not see (`../results/blind-sitting.md`): on 40 claims ruled blind against
Claude's earlier read of the page, 39 agree and none contradict; on the 30 ruled against
his own July ruling, 4 agree and 16 contradict (these 30 were chosen because the page text
contradicted the July call, so low agreement was expected); on 79 pairs against Claude's
call, 60 agree and 7 contradict.

## The model-read labels (silver)

236 faithful_claim items carry Claude's own reads of the page images, made while the
archive was built and accepted at a promote, never ruled one at a time by a person. They
are the `silver` split, reported in their own column and never mixed into an expert number.

## Labels that moved after a run

Labels can move after a model has answered (the whole-page pass moved 56; two pairs moved
again after a flag). `tools/report.py` therefore never trusts the target stored in a log. It
reads each sample's parsed answer and scores it against the item as it stands now. No model
was re-run for the whole-page labels; the stored answers were re-scored.

## The rulings files

The two sitting sheets, the rulings files with every pass kept, and the keeper's notes
stay in the archive's private folder. The data files carry what they established: the
label, who ruled it, how (`assurance`) and when. Every claim item carries a one-line
rationale shaped from his note; the pair items carry one only where a pair was re-ruled
after a flag, until the shaped lines for the rest have his yes.
