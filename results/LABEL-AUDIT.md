# Label audit: faithful_claim gold, checked against the page images

Before publishing, Claude read a stratified sample of 30 gold items against the scanned
pages. No label was changed by the check. What it found changed how gold is graded.

## Two findings

**A "kill" on the July sheet meant more than one thing.** The sheet asked whether each
record should keep its tie to a page. A kill could mean the person is not printed, or
that the printed name is another man, or that the record was a duplicate to be merged
into another record. Only the first two mean "this page does not refer to this
person". Two sampled kills were of the third kind: the page prints Joe Savoldi, and a
note on the same sheet says the record duplicated his.

**Some rulings were fast.** 45 of the 85 one-row rulings on the July sheet came two
seconds or less after the previous click. Two sampled kills from those runs disagree
with the print: a 1931 page names Jack Dempsey as the referee of the bout it covers,
and another carries a slanted line, "Jack Dempsey's ten best bouts for the year 1931",
that the OCR text reads as "Map Dempsey's".

The other 22 sampled items that stayed gold agree with the page.

## What was done

- One-row rulings are graded `deliberate` (more than five seconds after the previous
  click, or with a written note) or `rapid`. One click for all of one person's rows is
  `group`. One click that accepted 649 rows at once is excluded entirely.
- Every gold ruling the page text contradicts on its face is held out of gold: a kill
  whose surname is printed on the page, or a keep whose surname is not in the text.
  The held items go to a blind sitting, page in view, without the July call. The
  blind ruling becomes the label; the July ruling stays on the item as `earlier`.

## Caution

The hold rule uses the page text, and two of the baselines also read the page text.
While items are held, gold is missing exactly the items those baselines get wrong.
Read results on gold and held together until the blind rulings return them to gold.
