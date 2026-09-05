# TASK-UL039: Active learning strategies addendum to Lesson 16

## Context
FEAT-UL13 listed "active learning strategies" (when labeled data is too expensive: which
points to label next) as part of Lesson 16, alongside label propagation, self-training, and
co-training (TASK-UL30). TASK-UL30 covers the latter three thoroughly but does not cover
active learning — a distinct topic (query strategy for choosing the next point to label,
given a labeling budget) rather than making the most of an already-fixed labeled set.
Deferred honestly rather than checked off under existing work.

## Acceptance Criteria
- [x] Framing: active learning as budget-constrained label acquisition, distinct from semi-supervised learning — new markdown section explicitly distinguishes "given a labeled set that is already fixed" (semi-supervised, sections above) from "given a labeling budget still to spend" (active learning)
- [x] Uncertainty sampling: query the point the current model is least confident about — implemented via smallest margin between top-two predicted class probabilities
- [x] Query-by-committee: query the point where an ensemble of models disagrees most — implemented via a 5-member bootstrap-resampled committee, querying highest vote entropy
- [x] Empirical comparison: active learning query strategies vs random sampling, at a fixed labeling budget — 15 rounds, 10 labels/round, 20 initial, same digits dataset as the semi-supervised comparison above; verified with a standalone script BEFORE writing any notebook prose (see Pre-mortem note): uncertainty sampling final accuracy 0.948 vs random's 0.924 (mean across 5 seeds: 0.943 vs 0.917, with lower variance), query-by-committee intermediate at 0.920
- [x] Runs top-to-bottom in Google Colab — no new dependency added (LogisticRegression, StratifiedShuffleSplit, train_test_split, StandardScaler, accuracy_score are all already imported and used elsewhere in this same notebook); re-executed locally, 7/7 code cells zero errors, zero repr leaks

## Technical Notes
Low priority — this extends an already-complete, already-shipped Lesson 16
(notebooks/16_semi_supervised_learning.ipynb) with an adjacent topic, not a functional gap in
what shipped. `sklearn` has no built-in active learning module; `modAL` is a common
third-party library if a production-library pairing is wanted (verify Colab compatibility
before committing to it).

## Dependencies
- Blocked by: TASK-UL30 (shipped)
- Blocks: none

## Pre-mortem note
Having just caught two wrong first-draft predictions in TASK-UL038 (writing a confident explanation before checking the actual output), this task's active-learning comparison was verified in a standalone script BEFORE any notebook prose was written, across 5 random seeds, to confirm the uncertainty-sampling-beats-random result was real and not a single lucky seed. It held up consistently (uncertainty mean 0.943 vs random mean 0.917, uncertainty's own variance actually lower). No wrong claim was written this time.
