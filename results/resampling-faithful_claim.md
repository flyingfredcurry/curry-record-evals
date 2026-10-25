# faithful_claim, excerpt: three samples per item

Sample 0 is the headline run; samples 1 and 2 are two more draws of the same prompt (`--epochs 2`), same model, same evidence. `agree` is the share of items where all three verdicts match; `flip rate` is the rest. `correct` per sample is the headline metric re-scored on each draw; `spread` is its lowest to highest across the three. `majority` scores the verdict two or three samples gave, a three-way split counted as an abstention. `ci95` is on the single-sample (s0) correct share, for comparison with the spread.


## gold

| model | n | agree | flip rate | correct s0 | s1 | s2 | spread | ci95 | majority correct | wrong | abstained | precision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | 300 | 0.90 | 0.10 | 0.79 | 0.79 | 0.78 | 0.78 to 0.79 | 0.05 | 0.79 | 0.06 | 0.15 | 0.93 |
| claude-sonnet-5-5 | 300 | 0.89 | 0.11 | 0.70 | 0.68 | 0.69 | 0.68 to 0.70 | 0.05 | 0.70 | 0.03 | 0.27 | 0.96 |
| claude-opus-5-5 | 300 | 0.97 | 0.03 | 0.73 | 0.72 | 0.73 | 0.72 to 0.73 | 0.05 | 0.73 | 0.03 | 0.24 | 0.96 |
| claude-fable-5-1 | 300 | 0.94 | 0.06 | 0.75 | 0.73 | 0.74 | 0.73 to 0.75 | 0.05 | 0.74 | 0.04 | 0.23 | 0.95 |

## gold:blind-page

| model | n | agree | flip rate | correct s0 | s1 | s2 | spread | ci95 | majority correct | wrong | abstained | precision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | 70 | 0.91 | 0.09 | 0.73 | 0.73 | 0.71 | 0.71 to 0.73 | 0.10 | 0.71 | 0.19 | 0.10 | 0.79 |
| claude-sonnet-5-5 | 70 | 0.84 | 0.16 | 0.73 | 0.71 | 0.66 | 0.66 to 0.73 | 0.10 | 0.69 | 0.11 | 0.20 | 0.86 |
| claude-opus-5-5 | 70 | 0.96 | 0.04 | 0.69 | 0.69 | 0.69 | 0.69 to 0.69 | 0.11 | 0.69 | 0.11 | 0.20 | 0.86 |
| claude-fable-5-1 | 70 | 0.90 | 0.10 | 0.76 | 0.71 | 0.73 | 0.71 to 0.76 | 0.10 | 0.74 | 0.11 | 0.14 | 0.87 |
