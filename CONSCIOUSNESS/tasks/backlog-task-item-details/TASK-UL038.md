# TASK-UL038: Extend Lesson 15 preprocessing depth

## Context
TASK-UL29 (Lesson 15: Unsupervised Preprocessing) deliberately narrowed scope relative to its
original acceptance criteria: it covers StandardScaler (not min-max/robust), one-hot vs ordinal
encoding (not target/frequency), and Euclidean vs cosine distance (not Manhattan/Gower). The
core pedagogical points are all soundly demonstrated; this task tracks the deferred depth as
optional follow-up enhancement, not a gap in the shipped lesson.

## Acceptance Criteria
- [ ] Add min-max and robust scaling to the scaling comparison, with a case where one clearly outperforms StandardScaler (e.g. outlier-heavy data for RobustScaler)
- [ ] Add target/frequency encoding to the categorical encoding comparison
- [ ] Add Manhattan distance (contrast with Euclidean on high-dimensional/sparse data) and Gower distance (mixed categorical+numeric) to the distance metric section

## Technical Notes
Low priority — this extends an already-complete, already-shipped lesson (notebooks/15_unsupervised_preprocessing.ipynb) rather than filling a functional gap. Only pick this up if there's
a clear appetite for deepening Lesson 15 specifically.

## Dependencies
- Blocked by: TASK-UL29 (shipped)
- Blocks: none
