# same_person: model results

Scored against the current items file, so a label that moved after a run is scored as it stands now. `correct`, `wrong` and `abstained` are shares of all n items and sum to one: correct is a verdict that matches the ruling, or an abstention on an item the ruling holds undecidable; wrong is a verdict that does not match, including any verdict on an undecidable item; abstained is an abstention on an item the ruling settles. `ci95` is the 95% confidence half-width on correct (1.96 x the binomial standard error, items treated as independent; Miller 2024). `precision` = correct / (correct + wrong), the share of answers that were right when the model did not abstain on a settled item (SimpleQA's "correct given attempted"). `coverage` = share of settled items the model gave a verdict on. `net` = correct - wrong; `net_p3` = correct - 3 x wrong, for a use where a confident error costs three right answers.


## gold

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | both | 90 | 0.57 | 0.07 | 0.37 | 0.10 | 0.89 | 0.58 | 0.50 | 0.37 |
| claude-haiku-5-5 | crops | 90 | 0.62 | 0.04 | 0.33 | 0.10 | 0.93 | 0.62 | 0.58 | 0.49 |
| claude-haiku-5-5 | text | 90 | 0.46 | 0.02 | 0.52 | 0.10 | 0.95 | 0.40 | 0.43 | 0.39 |
| claude-sonnet-5-5 | both | 90 | 0.62 | 0.04 | 0.33 | 0.10 | 0.93 | 0.62 | 0.58 | 0.49 |
| claude-sonnet-5-5 | crops | 90 | 0.64 | 0.04 | 0.31 | 0.10 | 0.94 | 0.64 | 0.60 | 0.51 |
| claude-sonnet-5-5 | text | 90 | 0.53 | 0.03 | 0.43 | 0.10 | 0.94 | 0.50 | 0.50 | 0.43 |
| claude-opus-5-5 | both | 90 | 0.74 | 0.06 | 0.20 | 0.09 | 0.93 | 0.77 | 0.69 | 0.58 |
| claude-opus-5-5 | crops | 90 | 0.77 | 0.04 | 0.19 | 0.09 | 0.95 | 0.78 | 0.72 | 0.63 |
| claude-opus-5-5 | text | 90 | 0.58 | 0.02 | 0.40 | 0.10 | 0.96 | 0.54 | 0.56 | 0.51 |
| claude-fable-5-1 | both | 90 | 0.79 | 0.11 | 0.10 | 0.08 | 0.88 | 0.88 | 0.68 | 0.46 |
| claude-fable-5-1 | crops | 90 | 0.78 | 0.10 | 0.12 | 0.09 | 0.89 | 0.86 | 0.68 | 0.48 |
| claude-fable-5-1 | text | 90 | 0.62 | 0.06 | 0.32 | 0.10 | 0.92 | 0.63 | 0.57 | 0.46 |

## gold:blind

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | both | 45 | 0.69 | 0.02 | 0.29 | 0.14 | 0.97 | 0.71 | 0.67 | 0.62 |
| claude-haiku-5-5 | crops | 45 | 0.80 | 0.02 | 0.18 | 0.12 | 0.97 | 0.82 | 0.78 | 0.73 |
| claude-haiku-5-5 | text | 45 | 0.44 | 0.00 | 0.56 | 0.15 | 1.00 | 0.44 | 0.44 | 0.44 |
| claude-sonnet-5-5 | both | 45 | 0.78 | 0.02 | 0.20 | 0.12 | 0.97 | 0.80 | 0.76 | 0.71 |
| claude-sonnet-5-5 | crops | 45 | 0.82 | 0.00 | 0.18 | 0.11 | 1.00 | 0.82 | 0.82 | 0.82 |
| claude-sonnet-5-5 | text | 45 | 0.60 | 0.02 | 0.38 | 0.14 | 0.96 | 0.62 | 0.58 | 0.53 |
| claude-opus-5-5 | both | 45 | 0.82 | 0.00 | 0.18 | 0.11 | 1.00 | 0.82 | 0.82 | 0.82 |
| claude-opus-5-5 | crops | 45 | 0.84 | 0.00 | 0.16 | 0.11 | 1.00 | 0.84 | 0.84 | 0.84 |
| claude-opus-5-5 | text | 45 | 0.67 | 0.00 | 0.33 | 0.14 | 1.00 | 0.67 | 0.67 | 0.67 |
| claude-fable-5-1 | both | 45 | 0.87 | 0.04 | 0.09 | 0.10 | 0.95 | 0.91 | 0.82 | 0.73 |
| claude-fable-5-1 | crops | 45 | 0.89 | 0.02 | 0.09 | 0.09 | 0.98 | 0.91 | 0.87 | 0.82 |
| claude-fable-5-1 | text | 45 | 0.69 | 0.00 | 0.31 | 0.14 | 1.00 | 0.69 | 0.69 | 0.69 |

## gold:blind-page

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | both | 34 | 0.38 | 0.15 | 0.47 | 0.16 | 0.72 | 0.33 | 0.24 | -0.06 |
| claude-haiku-5-5 | crops | 34 | 0.41 | 0.09 | 0.50 | 0.17 | 0.82 | 0.29 | 0.32 | 0.15 |
| claude-haiku-5-5 | text | 34 | 0.41 | 0.06 | 0.53 | 0.17 | 0.88 | 0.25 | 0.35 | 0.24 |
| claude-sonnet-5-5 | both | 34 | 0.47 | 0.09 | 0.44 | 0.17 | 0.84 | 0.38 | 0.38 | 0.21 |
| claude-sonnet-5-5 | crops | 34 | 0.47 | 0.12 | 0.41 | 0.17 | 0.80 | 0.42 | 0.35 | 0.12 |
| claude-sonnet-5-5 | text | 34 | 0.47 | 0.06 | 0.47 | 0.17 | 0.89 | 0.33 | 0.41 | 0.29 |
| claude-opus-5-5 | both | 34 | 0.68 | 0.15 | 0.18 | 0.16 | 0.82 | 0.75 | 0.53 | 0.24 |
| claude-opus-5-5 | crops | 34 | 0.71 | 0.12 | 0.18 | 0.15 | 0.86 | 0.75 | 0.59 | 0.35 |
| claude-opus-5-5 | text | 34 | 0.44 | 0.06 | 0.50 | 0.17 | 0.88 | 0.29 | 0.38 | 0.26 |
| claude-fable-5-1 | both | 34 | 0.71 | 0.21 | 0.09 | 0.15 | 0.77 | 0.88 | 0.50 | 0.09 |
| claude-fable-5-1 | crops | 34 | 0.65 | 0.21 | 0.15 | 0.16 | 0.76 | 0.79 | 0.44 | 0.03 |
| claude-fable-5-1 | text | 34 | 0.47 | 0.15 | 0.38 | 0.17 | 0.76 | 0.46 | 0.32 | 0.03 |

## gold:question

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | both | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-haiku-5-5 | crops | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-haiku-5-5 | text | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-sonnet-5-5 | both | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-sonnet-5-5 | crops | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-sonnet-5-5 | text | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-opus-5-5 | both | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-opus-5-5 | crops | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-opus-5-5 | text | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-fable-5-1 | both | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-fable-5-1 | crops | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-fable-5-1 | text | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |

## gold:single

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | both | 9 | 0.56 | 0.00 | 0.44 | 0.32 | 1.00 | 0.43 | 0.56 | 0.56 |
| claude-haiku-5-5 | crops | 9 | 0.44 | 0.00 | 0.56 | 0.32 | 1.00 | 0.29 | 0.44 | 0.44 |
| claude-haiku-5-5 | text | 9 | 0.56 | 0.00 | 0.44 | 0.32 | 1.00 | 0.43 | 0.56 | 0.56 |
| claude-sonnet-5-5 | both | 9 | 0.33 | 0.00 | 0.67 | 0.31 | 1.00 | 0.14 | 0.33 | 0.33 |
| claude-sonnet-5-5 | crops | 9 | 0.33 | 0.00 | 0.67 | 0.31 | 1.00 | 0.14 | 0.33 | 0.33 |
| claude-sonnet-5-5 | text | 9 | 0.33 | 0.00 | 0.67 | 0.31 | 1.00 | 0.14 | 0.33 | 0.33 |
| claude-opus-5-5 | both | 9 | 0.56 | 0.00 | 0.44 | 0.32 | 1.00 | 0.43 | 0.56 | 0.56 |
| claude-opus-5-5 | crops | 9 | 0.56 | 0.00 | 0.44 | 0.32 | 1.00 | 0.43 | 0.56 | 0.56 |
| claude-opus-5-5 | text | 9 | 0.56 | 0.00 | 0.44 | 0.32 | 1.00 | 0.43 | 0.56 | 0.56 |
| claude-fable-5-1 | both | 9 | 0.67 | 0.11 | 0.22 | 0.31 | 0.86 | 0.71 | 0.56 | 0.33 |
| claude-fable-5-1 | crops | 9 | 0.67 | 0.11 | 0.22 | 0.31 | 0.86 | 0.71 | 0.56 | 0.33 |
| claude-fable-5-1 | text | 9 | 0.78 | 0.00 | 0.22 | 0.27 | 1.00 | 0.71 | 0.78 | 0.78 |
