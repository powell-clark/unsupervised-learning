# TASK-UL083: Soften two unmeasured claims in lesson 18b

## Context

Two soft flags from REVIEW-UL067 (verify-lesson-18, fresh context), raised as non-blocking alongside an APPROVE verdict on all eleven FEAT-UL16 criteria. Both are in notebooks/18b_kernel_density_estimation_practical.ipynb and both are cases of prose outrunning the statistic beside it — the same class of defect this lesson's own build caught three times, so worth fixing rather than filing and forgetting. (1) The sampling cell prints 'Generated samples sit FARTHER from the training set' in capitals for what is a 16 percent median-distance gap (18.68 against 16.12). The min-distance pair (12.36 against 5.29) supports the claim far more strongly than the median does, so either lead with the min or drop the emphasis. (2) The anomaly cell explains Isolation Forest's below-chance PR-AUC by asserting digit 9 'sits INSIDE the cloud among 4s, 7s and 8s'. That is domain-plausible and consistent with the overlapping score distributions plotted next to it, but nothing in the notebook measures it. Either compute a per-class statistic — mean distance from each digit-9 test point to its nearest 4, 7 or 8 against its nearest same-class neighbour would do it — or mark the sentence as an interpretation rather than a finding. Acceptance: both claims either measured or hedged, 18b re-executed clean with outputs committed, and the notebook's numbers re-checked against its prose afterwards.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-UL15
- Story: STORY-UL16
- Features: FEAT-UL1,FEAT-UL2,FEAT-UL16

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
