# same_person: model results

Scored against the current items file, so a label that moved after a run is scored as it stands now. `correct`, `wrong` and `abstained` are shares of all n items and sum to one: correct is a verdict that matches the ruling, or an abstention on an item the ruling holds undecidable; wrong is a verdict that does not match, including any verdict on an undecidable item; abstained is an abstention on an item the ruling settles. `ci95` is the 95% confidence half-width on correct (1.96 x the binomial standard error, items treated as independent; Miller 2024). `precision` = correct / (correct + wrong), the share of answers that were right when the model did not abstain on a settled item (SimpleQA's "correct given attempted"). `coverage` = share of settled items the model gave a verdict on. `net` = correct - wrong; `net_p3` = correct - 3 x wrong, for a use where a confident error costs three right answers.


## gold

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | both | 90 | 0.58 | 0.07 | 0.36 | 0.10 | 0.90 | 0.58 | 0.51 | 0.38 |
| claude-haiku-5-5 | crops | 90 | 0.63 | 0.04 | 0.32 | 0.10 | 0.93 | 0.62 | 0.59 | 0.50 |
| claude-haiku-5-5 | text | 90 | 0.47 | 0.02 | 0.51 | 0.10 | 0.95 | 0.40 | 0.44 | 0.40 |
| claude-sonnet-5-5 | both | 90 | 0.61 | 0.06 | 0.33 | 0.10 | 0.92 | 0.61 | 0.56 | 0.44 |
| claude-sonnet-5-5 | crops | 90 | 0.63 | 0.06 | 0.31 | 0.10 | 0.92 | 0.64 | 0.58 | 0.47 |
| claude-sonnet-5-5 | text | 90 | 0.54 | 0.03 | 0.42 | 0.10 | 0.94 | 0.51 | 0.51 | 0.44 |
| claude-opus-5-5 | both | 90 | 0.73 | 0.07 | 0.20 | 0.09 | 0.92 | 0.77 | 0.67 | 0.53 |
| claude-opus-5-5 | crops | 90 | 0.76 | 0.06 | 0.19 | 0.09 | 0.93 | 0.78 | 0.70 | 0.59 |
| claude-opus-5-5 | text | 90 | 0.59 | 0.02 | 0.39 | 0.10 | 0.96 | 0.55 | 0.57 | 0.52 |
| claude-fable-5-1 | both | 90 | 0.78 | 0.12 | 0.10 | 0.09 | 0.86 | 0.88 | 0.66 | 0.41 |
| claude-fable-5-1 | crops | 90 | 0.77 | 0.11 | 0.12 | 0.09 | 0.87 | 0.86 | 0.66 | 0.43 |
| claude-fable-5-1 | text | 90 | 0.61 | 0.07 | 0.32 | 0.10 | 0.90 | 0.62 | 0.54 | 0.41 |

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
| claude-haiku-5-5 | both | 34 | 0.41 | 0.15 | 0.44 | 0.17 | 0.74 | 0.35 | 0.26 | -0.03 |
| claude-haiku-5-5 | crops | 34 | 0.44 | 0.09 | 0.47 | 0.17 | 0.83 | 0.30 | 0.35 | 0.18 |
| claude-haiku-5-5 | text | 34 | 0.44 | 0.06 | 0.50 | 0.17 | 0.88 | 0.26 | 0.38 | 0.26 |
| claude-sonnet-5-5 | both | 34 | 0.44 | 0.12 | 0.44 | 0.17 | 0.79 | 0.35 | 0.32 | 0.09 |
| claude-sonnet-5-5 | crops | 34 | 0.44 | 0.15 | 0.41 | 0.17 | 0.75 | 0.39 | 0.29 | 0.00 |
| claude-sonnet-5-5 | text | 34 | 0.50 | 0.06 | 0.44 | 0.17 | 0.89 | 0.35 | 0.44 | 0.32 |
| claude-opus-5-5 | both | 34 | 0.65 | 0.18 | 0.18 | 0.16 | 0.79 | 0.74 | 0.47 | 0.12 |
| claude-opus-5-5 | crops | 34 | 0.68 | 0.15 | 0.18 | 0.16 | 0.82 | 0.74 | 0.53 | 0.24 |
| claude-opus-5-5 | text | 34 | 0.47 | 0.06 | 0.47 | 0.17 | 0.89 | 0.30 | 0.41 | 0.29 |
| claude-fable-5-1 | both | 34 | 0.68 | 0.24 | 0.09 | 0.16 | 0.74 | 0.87 | 0.44 | -0.03 |
| claude-fable-5-1 | crops | 34 | 0.62 | 0.24 | 0.15 | 0.16 | 0.72 | 0.78 | 0.38 | -0.09 |
| claude-fable-5-1 | text | 34 | 0.44 | 0.18 | 0.38 | 0.17 | 0.71 | 0.43 | 0.26 | -0.09 |

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
