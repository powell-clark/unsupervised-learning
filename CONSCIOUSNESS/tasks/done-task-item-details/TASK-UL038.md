# TASK-UL038: Extend Lesson 15 preprocessing depth

## Context
TASK-UL29 (Lesson 15: Unsupervised Preprocessing) deliberately narrowed scope relative to its
original acceptance criteria: it covers StandardScaler (not min-max/robust), one-hot vs ordinal
encoding (not target/frequency), and Euclidean vs cosine distance (not Manhattan/Gower). The
core pedagogical points are all soundly demonstrated; this task tracks the deferred depth as
optional follow-up enhancement, not a gap in the shipped lesson.

## Acceptance Criteria
- [x] Add min-max and robust scaling to the scaling comparison, with a case where one clearly outperforms StandardScaler (e.g. outlier-heavy data for RobustScaler) — added, with a genuine surprise: on outlier-contaminated data, RobustScaler actually scores WORST (ARI -0.00) and MinMaxScaler best (ARI 0.99), both for accidental reasons unrelated to "robustness" in the usual sense (RobustScaler leaves the outliers looking extreme, so K-Means spends 2 of 3 clusters isolating them; MinMaxScaler's range-stretch accidentally deletes income's contribution to distance, leaving K-Means to cluster on the untouched, cleanly-separated age feature). Caught my own first-draft wrong prediction before shipping it — see Pre-mortem note below
- [x] Add target/frequency encoding to the categorical encoding comparison — added a 20-category (Zipf-frequency) example; target-mean encoding clearly BEATS one-hot here (0.983 vs 0.215), not merely matches it as first drafted, because one-hot dilutes the real signal across 20 sparse columns while target-mean concentrates it into one; frequency encoding (uninformative by construction) scores worst (0.135), the intended contrast
- [x] Add Manhattan distance (contrast with Euclidean on high-dimensional/sparse data) and Gower distance (mixed categorical+numeric) to the distance metric section — added a distance-concentration sweep (dimensions 2-512) confirming Euclidean's max/min ratio collapses toward 1 faster than Manhattan's at every tested dimension, and a from-scratch Gower distance (no new dependency) clustered via `AgglomerativeClustering(metric='precomputed')` on mixed numeric+categorical data (ARI 1.000) vs a naive un-normalised Euclidean baseline (ARI 0.983)
- [x] 15 re-executed in place, zero errors, outputs committed
- [x] Commit and push

## Technical Notes
Low priority — this extends an already-complete, already-shipped lesson (notebooks/15_unsupervised_preprocessing.ipynb) rather than filling a functional gap. Only pick this up if there's
a clear appetite for deepening Lesson 15 specifically.

## Dependencies
- Blocked by: TASK-UL29 (shipped)
- Blocks: none

## Pre-mortem note (resolved before shipping)
The first draft of both the scaling and encoding additions wrote a plausible-sounding "Insight" print BEFORE checking the actual executed numbers, and both were wrong: the scaling draft claimed RobustScaler would be safest and MinMaxScaler most fragile under outlier contamination (backwards — RobustScaler scored worst, ARI -0.00); the encoding draft claimed target-mean encoding would merely "match" one-hot's ARI at lower dimensionality (it actually beat one-hot by a wide margin, 0.983 vs 0.215). Both were caught by re-reading the notebook's own re-executed output against the prose before committing, investigating the actual mechanism with a standalone script, and rewriting the explanation to match the measured result — the same discipline this course applies to itself throughout Part I and Part II.
