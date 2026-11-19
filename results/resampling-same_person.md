# same_person, text: three samples per item

Sample 0 is the headline run; samples 1 and 2 are two more draws of the same prompt (`--epochs 2`), same model, same evidence. `agree` is the share of items where all three verdicts match; `flip rate` is the rest. `correct` per sample is the headline metric re-scored on each draw; `spread` is its lowest to highest across the three. `majority` scores the verdict two or three samples gave, a three-way split counted as an abstention. `ci95` is on the single-sample (s0) correct share, for comparison with the spread.


## gold

| model | n | agree | flip rate | correct s0 | s1 | s2 | spread | ci95 | majority correct | wrong | abstained | precision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | 90 | 0.82 | 0.18 | 0.46 | 0.43 | 0.41 | 0.41 to 0.46 | 0.10 | 0.42 | 0.03 | 0.54 | 0.93 |
| claude-sonnet-5-5 | 90 | 0.94 | 0.06 | 0.53 | 0.53 | 0.51 | 0.51 to 0.53 | 0.10 | 0.51 | 0.03 | 0.46 | 0.94 |
| claude-opus-5-5 | 90 | 0.93 | 0.07 | 0.58 | 0.59 | 0.57 | 0.57 to 0.59 | 0.10 | 0.58 | 0.02 | 0.40 | 0.96 |
| claude-fable-5-1 | 90 | 0.94 | 0.06 | 0.62 | 0.59 | 0.60 | 0.59 to 0.62 | 0.10 | 0.61 | 0.04 | 0.34 | 0.93 |

## gold:blind-page

| model | n | agree | flip rate | correct s0 | s1 | s2 | spread | ci95 | majority correct | wrong | abstained | precision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | 34 | 0.88 | 0.12 | 0.41 | 0.35 | 0.41 | 0.35 to 0.41 | 0.17 | 0.38 | 0.09 | 0.53 | 0.81 |
| claude-sonnet-5-5 | 34 | 0.94 | 0.06 | 0.47 | 0.47 | 0.44 | 0.44 to 0.47 | 0.17 | 0.44 | 0.06 | 0.50 | 0.88 |
| claude-opus-5-5 | 34 | 0.94 | 0.06 | 0.44 | 0.47 | 0.41 | 0.41 to 0.47 | 0.17 | 0.44 | 0.06 | 0.50 | 0.88 |
| claude-fable-5-1 | 34 | 0.91 | 0.09 | 0.47 | 0.41 | 0.44 | 0.41 to 0.47 | 0.17 | 0.44 | 0.12 | 0.44 | 0.79 |
