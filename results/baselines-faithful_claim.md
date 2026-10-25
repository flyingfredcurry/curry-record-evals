# faithful_claim: no-model baselines

Scored with the task's own rules (curry_record_evals/scoring.py). `all` counts every item once. Held items are reported apart and never counted in gold. july_verifier exists only on ring-audit items (gold and held).

gold-blind-page are the 70 items Mike Curry ruled at the blind sitting of 2026-10-21 and ruled again the same evening at its whole-page pass, the whole page in view, no earlier call shown (the first sheet had shown a crop around the cited text, which on a column-head cite hid the name): the 30 July rulings the page text contradicted on its face, held out of gold until then, and 40 items that were silver before it. Two of the 70 he had been told about before the first sheet; the item says so.

| split | baseline | n | correct | wrong | abstained | ci95 | precision | coverage | net | net_p3 |
|---|---|---|---|---|---|---|---|---|---|---|
| gold | always_supported | 300 | 0.613 | 0.387 | 0.0 | 0.055 | 0.613 | 1.0 | 0.227 | -0.547 |
| gold | always_cannot | 300 | 0.04 | 0.0 | 0.96 | 0.022 | 1.0 | 0.0 | 0.04 | 0.04 |
| gold | name_present | 300 | 0.583 | 0.037 | 0.38 | 0.056 | 0.941 | 0.604 | 0.547 | 0.473 |
| gold | faithful_cite_t1 | 300 | 0.517 | 0.033 | 0.45 | 0.057 | 0.939 | 0.531 | 0.483 | 0.417 |
| gold | july_verifier | 260 | 0.419 | 0.127 | 0.454 | 0.06 | 0.768 | 0.526 | 0.292 | 0.038 |
| gold-blind-page | always_supported | 70 | 0.5 | 0.5 | 0.0 | 0.117 | 0.5 | 1.0 | 0.0 | -1.0 |
| gold-blind-page | always_cannot | 70 | 0.157 | 0.0 | 0.843 | 0.085 | 1.0 | 0.0 | 0.157 | 0.157 |
| gold-blind-page | name_present | 70 | 0.571 | 0.143 | 0.286 | 0.116 | 0.8 | 0.661 | 0.429 | 0.143 |
| gold-blind-page | faithful_cite_t1 | 70 | 0.286 | 0.129 | 0.586 | 0.106 | 0.69 | 0.305 | 0.157 | -0.1 |
| gold-blind-page | july_verifier | 30 | 0.2 | 0.333 | 0.467 | 0.143 | 0.375 | 0.3 | -0.133 | -0.8 |
| gold-deliberate | always_supported | 23 | 0.391 | 0.609 | 0.0 | 0.199 | 0.391 | 1.0 | -0.217 | -1.435 |
| gold-deliberate | always_cannot | 23 | 0.043 | 0.0 | 0.957 | 0.083 | 1.0 | 0.0 | 0.043 | 0.043 |
| gold-deliberate | name_present | 23 | 0.304 | 0.043 | 0.652 | 0.188 | 0.875 | 0.318 | 0.261 | 0.174 |
| gold-deliberate | faithful_cite_t1 | 23 | 0.304 | 0.043 | 0.652 | 0.188 | 0.875 | 0.318 | 0.261 | 0.174 |
| gold-deliberate | july_verifier | 23 | 0.261 | 0.043 | 0.696 | 0.179 | 0.857 | 0.273 | 0.217 | 0.13 |
| gold-group | always_supported | 168 | 0.792 | 0.208 | 0.0 | 0.061 | 0.792 | 1.0 | 0.583 | 0.167 |
| gold-group | always_cannot | 168 | 0.0 | 0.0 | 1.0 | 0.0 | None | 0.0 | 0.0 | 0.0 |
| gold-group | name_present | 168 | 0.732 | 0.0 | 0.268 | 0.067 | 1.0 | 0.732 | 0.732 | 0.732 |
| gold-group | faithful_cite_t1 | 168 | 0.732 | 0.0 | 0.268 | 0.067 | 1.0 | 0.732 | 0.732 | 0.732 |
| gold-group | july_verifier | 168 | 0.44 | 0.131 | 0.429 | 0.075 | 0.771 | 0.571 | 0.31 | 0.048 |
| gold-rapid | always_supported | 39 | 0.179 | 0.821 | 0.0 | 0.12 | 0.179 | 1.0 | -0.641 | -2.282 |
| gold-rapid | always_cannot | 39 | 0.0 | 0.0 | 1.0 | 0.0 | None | 0.0 | 0.0 | 0.0 |
| gold-rapid | name_present | 39 | 0.128 | 0.0 | 0.872 | 0.105 | 1.0 | 0.128 | 0.128 | 0.128 |
| gold-rapid | faithful_cite_t1 | 39 | 0.128 | 0.0 | 0.872 | 0.105 | 1.0 | 0.128 | 0.128 | 0.128 |
| gold-rapid | july_verifier | 39 | 0.59 | 0.0 | 0.41 | 0.154 | 1.0 | 0.59 | 0.59 | 0.59 |
| silver | always_supported | 236 | 0.873 | 0.127 | 0.0 | 0.042 | 0.873 | 1.0 | 0.746 | 0.492 |
| silver | always_cannot | 236 | 0.0 | 0.0 | 1.0 | 0.0 | None | 0.0 | 0.0 | 0.0 |
| silver | name_present | 236 | 0.873 | 0.03 | 0.097 | 0.042 | 0.967 | 0.903 | 0.843 | 0.784 |
| silver | faithful_cite_t1 | 236 | 0.0 | 0.025 | 0.975 | 0.0 | 0.0 | 0.025 | -0.025 | -0.076 |
| all | always_supported | 536 | 0.728 | 0.272 | 0.0 | 0.038 | 0.728 | 1.0 | 0.455 | -0.09 |
| all | always_cannot | 536 | 0.022 | 0.0 | 0.978 | 0.013 | 1.0 | 0.0 | 0.022 | 0.022 |
| all | name_present | 536 | 0.711 | 0.034 | 0.256 | 0.038 | 0.955 | 0.739 | 0.677 | 0.61 |
| all | faithful_cite_t1 | 536 | 0.289 | 0.03 | 0.681 | 0.038 | 0.906 | 0.303 | 0.259 | 0.2 |
| all | july_verifier | 260 | 0.419 | 0.127 | 0.454 | 0.06 | 0.768 | 0.526 | 0.292 | 0.038 |
