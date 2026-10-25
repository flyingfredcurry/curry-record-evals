# faithful_claim: model results

Scored against the current items file, so a label that moved after a run is scored as it stands now. `correct`, `wrong` and `abstained` are shares of all n items and sum to one: correct is a verdict that matches the ruling, or an abstention on an item the ruling holds undecidable; wrong is a verdict that does not match, including any verdict on an undecidable item; abstained is an abstention on an item the ruling settles. `ci95` is the 95% confidence half-width on correct (1.96 x the binomial standard error, items treated as independent; Miller 2024). `precision` = correct / (correct + wrong), the share of answers that were right when the model did not abstain on a settled item (SimpleQA's "correct given attempted"). `coverage` = share of settled items the model gave a verdict on. `net` = correct - wrong; `net_p3` = correct - 3 x wrong, for a use where a confident error costs three right answers.


## gold

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | excerpt | 300 | 0.79 | 0.05 | 0.16 | 0.05 | 0.94 | 0.84 | 0.74 | 0.63 |
| claude-haiku-5-5 | page_image | 300 | 0.93 | 0.06 | 0.02 | 0.03 | 0.94 | 0.98 | 0.87 | 0.76 |
| claude-haiku-5-5 | page_text | 300 | 0.91 | 0.06 | 0.03 | 0.03 | 0.94 | 0.97 | 0.85 | 0.73 |
| claude-sonnet-5-5 | excerpt | 300 | 0.70 | 0.03 | 0.26 | 0.05 | 0.95 | 0.73 | 0.67 | 0.60 |
| claude-sonnet-5-5 | page_image | 300 | 0.84 | 0.05 | 0.11 | 0.04 | 0.94 | 0.88 | 0.79 | 0.69 |
| claude-sonnet-5-5 | page_text | 300 | 0.83 | 0.05 | 0.12 | 0.04 | 0.95 | 0.87 | 0.78 | 0.69 |
| claude-opus-5-5 | excerpt | 300 | 0.73 | 0.03 | 0.24 | 0.05 | 0.96 | 0.75 | 0.70 | 0.64 |
| claude-opus-5-5 | page_image | 300 | 0.85 | 0.05 | 0.10 | 0.04 | 0.94 | 0.90 | 0.80 | 0.70 |
| claude-opus-5-5 | page_text | 300 | 0.87 | 0.04 | 0.09 | 0.04 | 0.96 | 0.90 | 0.83 | 0.75 |
| claude-fable-5-1 | excerpt | 300 | 0.75 | 0.03 | 0.22 | 0.05 | 0.96 | 0.77 | 0.72 | 0.66 |
| claude-fable-5-1 | page_image | 300 | 0.92 | 0.04 | 0.04 | 0.03 | 0.96 | 0.96 | 0.88 | 0.80 |
| claude-fable-5-1 | page_text | 300 | 0.88 | 0.04 | 0.08 | 0.04 | 0.95 | 0.92 | 0.84 | 0.75 |

## gold:blind-page

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | excerpt | 70 | 0.73 | 0.16 | 0.11 | 0.10 | 0.82 | 0.86 | 0.57 | 0.26 |
| claude-haiku-5-5 | page_image | 70 | 0.76 | 0.23 | 0.01 | 0.10 | 0.77 | 0.98 | 0.53 | 0.07 |
| claude-haiku-5-5 | page_text | 70 | 0.76 | 0.23 | 0.01 | 0.10 | 0.77 | 0.98 | 0.53 | 0.07 |
| claude-sonnet-5-5 | excerpt | 70 | 0.73 | 0.13 | 0.14 | 0.10 | 0.85 | 0.83 | 0.60 | 0.34 |
| claude-sonnet-5-5 | page_image | 70 | 0.70 | 0.19 | 0.11 | 0.11 | 0.79 | 0.86 | 0.51 | 0.14 |
| claude-sonnet-5-5 | page_text | 70 | 0.71 | 0.19 | 0.10 | 0.11 | 0.79 | 0.88 | 0.53 | 0.16 |
| claude-opus-5-5 | excerpt | 70 | 0.69 | 0.11 | 0.20 | 0.11 | 0.86 | 0.76 | 0.57 | 0.34 |
| claude-opus-5-5 | page_image | 70 | 0.69 | 0.19 | 0.13 | 0.11 | 0.79 | 0.85 | 0.50 | 0.13 |
| claude-opus-5-5 | page_text | 70 | 0.67 | 0.16 | 0.17 | 0.11 | 0.81 | 0.80 | 0.51 | 0.20 |
| claude-fable-5-1 | excerpt | 70 | 0.76 | 0.10 | 0.14 | 0.10 | 0.88 | 0.83 | 0.66 | 0.46 |
| claude-fable-5-1 | page_image | 70 | 0.80 | 0.16 | 0.04 | 0.09 | 0.84 | 0.95 | 0.64 | 0.33 |
| claude-fable-5-1 | page_text | 70 | 0.76 | 0.16 | 0.09 | 0.10 | 0.83 | 0.90 | 0.60 | 0.29 |

## gold:blind-page:full-name

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | excerpt | 63 | 0.81 | 0.08 | 0.11 | 0.10 | 0.91 | 0.87 | 0.73 | 0.57 |
| claude-haiku-5-5 | page_image | 63 | 0.84 | 0.14 | 0.02 | 0.09 | 0.85 | 0.98 | 0.70 | 0.41 |
| claude-haiku-5-5 | page_text | 63 | 0.84 | 0.14 | 0.02 | 0.09 | 0.85 | 0.98 | 0.70 | 0.41 |
| claude-sonnet-5-5 | excerpt | 63 | 0.81 | 0.05 | 0.14 | 0.10 | 0.94 | 0.83 | 0.76 | 0.67 |
| claude-sonnet-5-5 | page_image | 63 | 0.78 | 0.10 | 0.13 | 0.10 | 0.89 | 0.85 | 0.68 | 0.49 |
| claude-sonnet-5-5 | page_text | 63 | 0.79 | 0.10 | 0.11 | 0.10 | 0.89 | 0.87 | 0.70 | 0.51 |
| claude-opus-5-5 | excerpt | 63 | 0.76 | 0.06 | 0.17 | 0.11 | 0.92 | 0.79 | 0.70 | 0.57 |
| claude-opus-5-5 | page_image | 63 | 0.76 | 0.11 | 0.13 | 0.11 | 0.87 | 0.85 | 0.65 | 0.43 |
| claude-opus-5-5 | page_text | 63 | 0.75 | 0.11 | 0.14 | 0.11 | 0.87 | 0.83 | 0.63 | 0.41 |
| claude-fable-5-1 | excerpt | 63 | 0.84 | 0.06 | 0.10 | 0.09 | 0.93 | 0.88 | 0.78 | 0.65 |
| claude-fable-5-1 | page_image | 63 | 0.89 | 0.11 | 0.00 | 0.08 | 0.89 | 1.00 | 0.78 | 0.56 |
| claude-fable-5-1 | page_text | 63 | 0.84 | 0.13 | 0.03 | 0.09 | 0.87 | 0.96 | 0.71 | 0.46 |

## gold:blind-page:one-word-name

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | excerpt | 7 | 0.00 | 0.86 | 0.14 | 0.00 | 0.00 | 0.86 | -0.86 | -2.57 |
| claude-haiku-5-5 | page_image | 7 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | -1.00 | -3.00 |
| claude-haiku-5-5 | page_text | 7 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | -1.00 | -3.00 |
| claude-sonnet-5-5 | excerpt | 7 | 0.00 | 0.86 | 0.14 | 0.00 | 0.00 | 0.86 | -0.86 | -2.57 |
| claude-sonnet-5-5 | page_image | 7 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | -1.00 | -3.00 |
| claude-sonnet-5-5 | page_text | 7 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | -1.00 | -3.00 |
| claude-opus-5-5 | excerpt | 7 | 0.00 | 0.57 | 0.43 | 0.00 | 0.00 | 0.57 | -0.57 | -1.71 |
| claude-opus-5-5 | page_image | 7 | 0.00 | 0.86 | 0.14 | 0.00 | 0.00 | 0.86 | -0.86 | -2.57 |
| claude-opus-5-5 | page_text | 7 | 0.00 | 0.57 | 0.43 | 0.00 | 0.00 | 0.57 | -0.57 | -1.71 |
| claude-fable-5-1 | excerpt | 7 | 0.00 | 0.43 | 0.57 | 0.00 | 0.00 | 0.43 | -0.43 | -1.29 |
| claude-fable-5-1 | page_image | 7 | 0.00 | 0.57 | 0.43 | 0.00 | 0.00 | 0.57 | -0.57 | -1.71 |
| claude-fable-5-1 | page_text | 7 | 0.00 | 0.43 | 0.57 | 0.00 | 0.00 | 0.43 | -0.43 | -1.29 |

## gold:deliberate

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | excerpt | 23 | 0.70 | 0.04 | 0.26 | 0.19 | 0.94 | 0.73 | 0.65 | 0.57 |
| claude-haiku-5-5 | page_image | 23 | 0.83 | 0.04 | 0.13 | 0.15 | 0.95 | 0.86 | 0.78 | 0.70 |
| claude-haiku-5-5 | page_text | 23 | 0.78 | 0.04 | 0.17 | 0.17 | 0.95 | 0.82 | 0.74 | 0.65 |
| claude-sonnet-5-5 | excerpt | 23 | 0.43 | 0.04 | 0.52 | 0.20 | 0.91 | 0.45 | 0.39 | 0.30 |
| claude-sonnet-5-5 | page_image | 23 | 0.61 | 0.09 | 0.30 | 0.20 | 0.88 | 0.68 | 0.52 | 0.35 |
| claude-sonnet-5-5 | page_text | 23 | 0.74 | 0.04 | 0.22 | 0.18 | 0.94 | 0.77 | 0.70 | 0.61 |
| claude-opus-5-5 | excerpt | 23 | 0.43 | 0.04 | 0.52 | 0.20 | 0.91 | 0.45 | 0.39 | 0.30 |
| claude-opus-5-5 | page_image | 23 | 0.70 | 0.09 | 0.22 | 0.19 | 0.89 | 0.77 | 0.61 | 0.43 |
| claude-opus-5-5 | page_text | 23 | 0.74 | 0.04 | 0.22 | 0.18 | 0.94 | 0.77 | 0.70 | 0.61 |
| claude-fable-5-1 | excerpt | 23 | 0.52 | 0.04 | 0.43 | 0.20 | 0.92 | 0.55 | 0.48 | 0.39 |
| claude-fable-5-1 | page_image | 23 | 0.78 | 0.04 | 0.17 | 0.17 | 0.95 | 0.82 | 0.74 | 0.65 |
| claude-fable-5-1 | page_text | 23 | 0.74 | 0.09 | 0.17 | 0.18 | 0.89 | 0.82 | 0.65 | 0.48 |

## gold:group

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | excerpt | 168 | 0.89 | 0.02 | 0.09 | 0.05 | 0.97 | 0.91 | 0.86 | 0.82 |
| claude-haiku-5-5 | page_image | 168 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| claude-haiku-5-5 | page_text | 168 | 0.98 | 0.01 | 0.02 | 0.02 | 0.99 | 0.98 | 0.97 | 0.96 |
| claude-sonnet-5-5 | excerpt | 168 | 0.83 | 0.00 | 0.17 | 0.06 | 1.00 | 0.83 | 0.83 | 0.83 |
| claude-sonnet-5-5 | page_image | 168 | 0.94 | 0.00 | 0.06 | 0.04 | 1.00 | 0.94 | 0.94 | 0.94 |
| claude-sonnet-5-5 | page_text | 168 | 0.93 | 0.00 | 0.07 | 0.04 | 1.00 | 0.93 | 0.93 | 0.93 |
| claude-opus-5-5 | excerpt | 168 | 0.90 | 0.00 | 0.10 | 0.05 | 1.00 | 0.90 | 0.90 | 0.90 |
| claude-opus-5-5 | page_image | 168 | 0.97 | 0.00 | 0.03 | 0.03 | 1.00 | 0.97 | 0.97 | 0.97 |
| claude-opus-5-5 | page_text | 168 | 0.98 | 0.00 | 0.02 | 0.02 | 1.00 | 0.98 | 0.98 | 0.98 |
| claude-fable-5-1 | excerpt | 168 | 0.90 | 0.01 | 0.10 | 0.05 | 0.99 | 0.90 | 0.89 | 0.88 |
| claude-fable-5-1 | page_image | 168 | 0.99 | 0.00 | 0.01 | 0.02 | 1.00 | 0.99 | 0.99 | 0.99 |
| claude-fable-5-1 | page_text | 168 | 0.97 | 0.00 | 0.03 | 0.03 | 1.00 | 0.97 | 0.97 | 0.97 |

## gold:rapid

| model | condition | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | excerpt | 39 | 0.54 | 0.00 | 0.46 | 0.16 | 1.00 | 0.54 | 0.54 | 0.54 |
| claude-haiku-5-5 | page_image | 39 | 0.97 | 0.00 | 0.03 | 0.05 | 1.00 | 0.97 | 0.97 | 0.97 |
| claude-haiku-5-5 | page_text | 39 | 0.97 | 0.00 | 0.03 | 0.05 | 1.00 | 0.97 | 0.97 | 0.97 |
| claude-sonnet-5-5 | excerpt | 39 | 0.26 | 0.00 | 0.74 | 0.14 | 1.00 | 0.26 | 0.26 | 0.26 |
| claude-sonnet-5-5 | page_image | 39 | 0.77 | 0.00 | 0.23 | 0.13 | 1.00 | 0.77 | 0.77 | 0.77 |
| claude-sonnet-5-5 | page_text | 39 | 0.64 | 0.00 | 0.36 | 0.15 | 1.00 | 0.64 | 0.64 | 0.64 |
| claude-opus-5-5 | excerpt | 39 | 0.28 | 0.00 | 0.72 | 0.14 | 1.00 | 0.28 | 0.28 | 0.28 |
| claude-opus-5-5 | page_image | 39 | 0.74 | 0.00 | 0.26 | 0.14 | 1.00 | 0.74 | 0.74 | 0.74 |
| claude-opus-5-5 | page_text | 39 | 0.82 | 0.00 | 0.18 | 0.12 | 1.00 | 0.82 | 0.82 | 0.82 |
| claude-fable-5-1 | excerpt | 39 | 0.21 | 0.00 | 0.79 | 0.13 | 1.00 | 0.21 | 0.21 | 0.21 |
| claude-fable-5-1 | page_image | 39 | 0.92 | 0.00 | 0.08 | 0.08 | 1.00 | 0.92 | 0.92 | 0.92 |
| claude-fable-5-1 | page_text | 39 | 0.79 | 0.00 | 0.21 | 0.13 | 1.00 | 0.79 | 0.79 | 0.79 |
