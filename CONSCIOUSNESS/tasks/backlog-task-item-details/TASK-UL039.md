# TASK-UL039: Active learning strategies addendum to Lesson 16

## Context
FEAT-UL13 listed "active learning strategies" (when labeled data is too expensive: which
points to label next) as part of Lesson 16, alongside label propagation, self-training, and
co-training (TASK-UL30). TASK-UL30 covers the latter three thoroughly but does not cover
active learning — a distinct topic (query strategy for choosing the next point to label,
given a labeling budget) rather than making the most of an already-fixed labeled set.
Deferred honestly rather than checked off under existing work.

## Acceptance Criteria
- [ ] Framing: active learning as budget-constrained label acquisition, distinct from semi-supervised learning
- [ ] Uncertainty sampling: query the point the current model is least confident about
- [ ] Query-by-committee: query the point where an ensemble of models disagrees most
- [ ] Empirical comparison: active learning query strategies vs random sampling, at a fixed labeling budget
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Low priority — this extends an already-complete, already-shipped Lesson 16
(notebooks/16_semi_supervised_learning.ipynb) with an adjacent topic, not a functional gap in
what shipped. `sklearn` has no built-in active learning module; `modAL` is a common
third-party library if a production-library pairing is wanted (verify Colab compatibility
before committing to it).

## Dependencies
- Blocked by: TASK-UL30 (shipped)
- Blocks: none
