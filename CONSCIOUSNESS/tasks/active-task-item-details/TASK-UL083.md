# TASK-UL083: Soften two unmeasured claims in lesson 18b

## Context

Two soft flags from REVIEW-UL067 (verify-lesson-18, fresh context), raised as non-blocking alongside an APPROVE verdict on all eleven FEAT-UL16 criteria. Both are in notebooks/18b_kernel_density_estimation_practical.ipynb and both are cases of prose outrunning the statistic beside it — the same class of defect this lesson's own build caught three times, so worth fixing rather than filing and forgetting. (1) The sampling cell prints 'Generated samples sit FARTHER from the training set' in capitals for what is a 16 percent median-distance gap (18.68 against 16.12). The min-distance pair (12.36 against 5.29) supports the claim far more strongly than the median does, so either lead with the min or drop the emphasis. (2) The anomaly cell explains Isolation Forest's below-chance PR-AUC by asserting digit 9 'sits INSIDE the cloud among 4s, 7s and 8s'. That is domain-plausible and consistent with the overlapping score distributions plotted next to it, but nothing in the notebook measures it. Either compute a per-class statistic — mean distance from each digit-9 test point to its nearest 4, 7 or 8 against its nearest same-class neighbour would do it — or mark the sentence as an interpretation rather than a finding. Acceptance: both claims either measured or hedged, 18b re-executed clean with outputs committed, and the notebook's numbers re-checked against its prose afterwards.

## Acceptance criteria

- [x] Sampling-distance claim (1): dropped the all-caps "FARTHER" emphasis; cell 7 now states the actual percentage gap plainly (16%, 18.68 vs 16.12) and additionally cites the min-distance pair as the stronger corroborating evidence (12.36 vs 5.29, a 2.3x gap), computed dynamically from the notebook's own variables rather than hardcoded
- [x] Anomaly-explanation claim (2): computed the per-class nearest-neighbour statistic directly (`nn_ratio` helper) — digit 9's nearest same-class median is 17.5 vs nearest-4/7/8 median 30.6 (1.74x gap), contrasted against digit 0 (a visually distinctive digit): 14.2 vs 35.9 (2.52x gap) — digit 9 is measurably closer to its confusable neighbours, relative to its own within-class scatter, than a well-separated digit is; the sentence now states this measured comparison and explicitly flags the interior-region explanation as "consistent with, though not direct proof of" rather than an assumed fact
- [x] 18b re-executed in place (`jupyter nbconvert --execute`), zero errors, outputs committed — 6/6 code cells, zero errors, zero execution_count nulls, zero numpy-repr leaks
- [x] Every number in the notebook's prose re-checked against its own printed/computed output after the edit — verified by direct inspection of the re-executed cell outputs (18.68/16.12/12.36/5.29 for claim 1; 17.5/30.6/1.74x and 14.2/35.9/2.52x for claim 2), and independently cross-checked against a standalone script computing the same nearest-neighbour statistics from scratch before writing the fix (results matched to within rounding)
- [x] Commit and push

## Dependencies

- Directive: DIRECT-UL15
- Story: STORY-UL16
- Features: FEAT-UL1,FEAT-UL2,FEAT-UL16

## Pre-mortem

### Failure modes

- Computing the per-class nearest-neighbour statistic for claim (2) could contradict the notebook's existing narrative (e.g. digit 9 might not actually sit closer to 4/7/8 than to other 9s) — if so, rewrite the explanation to match the measured result rather than keeping the plausible-but-unverified original framing
- Fixing claim (1)'s emphasis without re-deriving the actual printed distances first risks introducing a second unmeasured claim in the same cell

### Weak assumptions

- Assumes REVIEW-UL067's quoted numbers (18.68/16.12 median, 12.36/5.29 min) are still exactly what the committed notebook prints — re-derive from the notebook's own output rather than trusting the review card's transcription
