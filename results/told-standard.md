# same_person: the standard told against untold

Same items, same models, same page evidence. UNTOLD is the headline run: the model is not given the archive's same-person standard. TOLD appends the standard to the system prompt (`-T standard=told`): SAME only when the pages tie the two names, DIFFERENT when the pages show two people, CANNOT TELL when the only tie is the name. Shares are of all n items and sum to one; `ci95` is 1.96 x the binomial standard error on correct; `precision` = correct / (correct + wrong). A flip is an item whose verdict changed when told: `toward` gold when the outcome improved (wrong -> abstained -> correct), `away` when it worsened, `lateral` when the verdict changed and the outcome did not.


## gold

| model | condition | standard | n | correct | wrong | abstained | ci95 | precision | coverage | net |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | crops | untold | 90 | 0.63 | 0.04 | 0.32 | 0.10 | 0.93 | 0.62 | 0.59 |
| claude-haiku-5-5 | crops | told | 90 | 0.44 | 0.02 | 0.53 | 0.10 | 0.95 | 0.38 | 0.42 |
| claude-haiku-5-5 | text | untold | 90 | 0.47 | 0.02 | 0.51 | 0.10 | 0.95 | 0.40 | 0.44 |
| claude-haiku-5-5 | text | told | 90 | 0.36 | 0.04 | 0.60 | 0.10 | 0.89 | 0.30 | 0.31 |
| claude-sonnet-5-5 | crops | untold | 90 | 0.63 | 0.06 | 0.31 | 0.10 | 0.92 | 0.64 | 0.58 |
| claude-sonnet-5-5 | crops | told | 90 | 0.46 | 0.01 | 0.53 | 0.10 | 0.98 | 0.38 | 0.44 |
| claude-sonnet-5-5 | text | untold | 90 | 0.54 | 0.03 | 0.42 | 0.10 | 0.94 | 0.51 | 0.51 |
| claude-sonnet-5-5 | text | told | 90 | 0.38 | 0.01 | 0.61 | 0.10 | 0.97 | 0.29 | 0.37 |
| claude-opus-5-5 | crops | untold | 90 | 0.76 | 0.06 | 0.19 | 0.09 | 0.93 | 0.78 | 0.70 |
| claude-opus-5-5 | crops | told | 90 | 0.53 | 0.03 | 0.43 | 0.10 | 0.94 | 0.49 | 0.50 |
| claude-opus-5-5 | text | untold | 90 | 0.59 | 0.02 | 0.39 | 0.10 | 0.96 | 0.55 | 0.57 |
| claude-opus-5-5 | text | told | 90 | 0.43 | 0.06 | 0.51 | 0.10 | 0.89 | 0.40 | 0.38 |
| claude-fable-5-1 | crops | untold | 90 | 0.77 | 0.11 | 0.12 | 0.09 | 0.87 | 0.86 | 0.66 |
| claude-fable-5-1 | crops | told | 90 | 0.62 | 0.02 | 0.36 | 0.10 | 0.97 | 0.58 | 0.60 |
| claude-fable-5-1 | text | untold | 90 | 0.61 | 0.07 | 0.32 | 0.10 | 0.90 | 0.62 | 0.54 |
| claude-fable-5-1 | text | told | 90 | 0.48 | 0.02 | 0.50 | 0.10 | 0.96 | 0.42 | 0.46 |

| model | condition | n | flips | toward gold | away | lateral | transitions (untold -> told) |
|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | crops | 90 | 42 | 13 | 28 | 1 | SAME -> CANNOT_TELL 25, CANNOT_TELL -> DIFFERENT 10, DIFFERENT -> CANNOT_TELL 5, SAME -> DIFFERENT 1, CANNOT_TELL -> SAME 1 |
| claude-haiku-5-5 | text | 90 | 31 | 10 | 21 | 0 | SAME -> CANNOT_TELL 17, CANNOT_TELL -> DIFFERENT 12, DIFFERENT -> CANNOT_TELL 2 |
| claude-sonnet-5-5 | crops | 90 | 37 | 11 | 26 | 0 | SAME -> CANNOT_TELL 23, DIFFERENT -> CANNOT_TELL 7, CANNOT_TELL -> DIFFERENT 7 |
| claude-sonnet-5-5 | text | 90 | 32 | 9 | 23 | 0 | SAME -> CANNOT_TELL 21, CANNOT_TELL -> DIFFERENT 7, DIFFERENT -> CANNOT_TELL 4 |
| claude-opus-5-5 | crops | 90 | 28 | 4 | 24 | 0 | SAME -> CANNOT_TELL 22, DIFFERENT -> CANNOT_TELL 4, CANNOT_TELL -> DIFFERENT 2 |
| claude-opus-5-5 | text | 90 | 35 | 10 | 25 | 0 | SAME -> CANNOT_TELL 19, CANNOT_TELL -> DIFFERENT 12, DIFFERENT -> CANNOT_TELL 3, SAME -> DIFFERENT 1 |
| claude-fable-5-1 | crops | 90 | 29 | 9 | 20 | 0 | SAME -> CANNOT_TELL 19, DIFFERENT -> CANNOT_TELL 9, CANNOT_TELL -> DIFFERENT 1 |
| claude-fable-5-1 | text | 90 | 26 | 8 | 18 | 0 | SAME -> CANNOT_TELL 17, DIFFERENT -> CANNOT_TELL 5, CANNOT_TELL -> DIFFERENT 4 |

## gold:blind-page

| model | condition | standard | n | correct | wrong | abstained | ci95 | precision | coverage | net |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | crops | untold | 34 | 0.44 | 0.09 | 0.47 | 0.17 | 0.83 | 0.30 | 0.35 |
| claude-haiku-5-5 | crops | told | 34 | 0.62 | 0.06 | 0.32 | 0.16 | 0.91 | 0.52 | 0.56 |
| claude-haiku-5-5 | text | untold | 34 | 0.44 | 0.06 | 0.50 | 0.17 | 0.88 | 0.26 | 0.38 |
| claude-haiku-5-5 | text | told | 34 | 0.53 | 0.09 | 0.38 | 0.17 | 0.86 | 0.43 | 0.44 |
| claude-sonnet-5-5 | crops | untold | 34 | 0.44 | 0.15 | 0.41 | 0.17 | 0.75 | 0.39 | 0.29 |
| claude-sonnet-5-5 | crops | told | 34 | 0.62 | 0.03 | 0.35 | 0.16 | 0.95 | 0.48 | 0.59 |
| claude-sonnet-5-5 | text | untold | 34 | 0.50 | 0.06 | 0.44 | 0.17 | 0.89 | 0.35 | 0.44 |
| claude-sonnet-5-5 | text | told | 34 | 0.56 | 0.03 | 0.41 | 0.17 | 0.95 | 0.39 | 0.53 |
| claude-opus-5-5 | crops | untold | 34 | 0.68 | 0.15 | 0.18 | 0.16 | 0.82 | 0.74 | 0.53 |
| claude-opus-5-5 | crops | told | 34 | 0.68 | 0.09 | 0.24 | 0.16 | 0.88 | 0.65 | 0.59 |
| claude-opus-5-5 | text | untold | 34 | 0.47 | 0.06 | 0.47 | 0.17 | 0.89 | 0.30 | 0.41 |
| claude-opus-5-5 | text | told | 34 | 0.62 | 0.09 | 0.29 | 0.16 | 0.88 | 0.57 | 0.53 |
| claude-fable-5-1 | crops | untold | 34 | 0.62 | 0.24 | 0.15 | 0.16 | 0.72 | 0.78 | 0.38 |
| claude-fable-5-1 | crops | told | 34 | 0.65 | 0.06 | 0.29 | 0.16 | 0.92 | 0.57 | 0.59 |
| claude-fable-5-1 | text | untold | 34 | 0.44 | 0.18 | 0.38 | 0.17 | 0.71 | 0.43 | 0.26 |
| claude-fable-5-1 | text | told | 34 | 0.53 | 0.06 | 0.41 | 0.17 | 0.90 | 0.39 | 0.47 |

| model | condition | n | flips | toward gold | away | lateral | transitions (untold -> told) |
|---|---|---|---|---|---|---|---|
| claude-haiku-5-5 | crops | 34 | 10 | 8 | 1 | 1 | CANNOT_TELL -> DIFFERENT 7, DIFFERENT -> CANNOT_TELL 2, SAME -> DIFFERENT 1 |
| claude-haiku-5-5 | text | 34 | 11 | 7 | 4 | 0 | CANNOT_TELL -> DIFFERENT 8, DIFFERENT -> CANNOT_TELL 2, SAME -> CANNOT_TELL 1 |
| claude-sonnet-5-5 | crops | 34 | 13 | 10 | 3 | 0 | CANNOT_TELL -> DIFFERENT 6, DIFFERENT -> CANNOT_TELL 5, SAME -> CANNOT_TELL 2 |
| claude-sonnet-5-5 | text | 34 | 10 | 6 | 4 | 0 | CANNOT_TELL -> DIFFERENT 5, DIFFERENT -> CANNOT_TELL 4, SAME -> CANNOT_TELL 1 |
| claude-opus-5-5 | crops | 34 | 6 | 3 | 3 | 0 | DIFFERENT -> CANNOT_TELL 3, SAME -> CANNOT_TELL 2, CANNOT_TELL -> DIFFERENT 1 |
| claude-opus-5-5 | text | 34 | 11 | 8 | 3 | 0 | CANNOT_TELL -> DIFFERENT 9, DIFFERENT -> CANNOT_TELL 2 |
| claude-fable-5-1 | crops | 34 | 10 | 6 | 4 | 0 | DIFFERENT -> CANNOT_TELL 6, SAME -> CANNOT_TELL 4 |
| claude-fable-5-1 | text | 34 | 9 | 7 | 2 | 0 | DIFFERENT -> CANNOT_TELL 4, CANNOT_TELL -> DIFFERENT 3, SAME -> CANNOT_TELL 2 |
