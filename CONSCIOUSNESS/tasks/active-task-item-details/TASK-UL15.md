# TASK-UL15: Anomaly Detection Theory (7a)

## Context
First notebook of Lesson 7 (STORY-UL8, DIRECT-UL8). Introduces anomaly detection as the
unsupervised task of flagging rare, unusual points in unlabeled data. Covers three
distinct paradigms: isolation-based (Isolation Forest), density-based (Local Outlier
Factor), and boundary-based (One-Class SVM).

## Acceptance Criteria
- [ ] Isolation Forest: random partitioning intuition, path length, anomaly score formula
- [ ] Local Outlier Factor: k-distance, reachability distance, local reachability density, LOF score
- [ ] One-Class SVM: kernel trick, separating hyperplane from the origin, nu parameter
- [ ] From-scratch NumPy implementations for all three methods
- [ ] Cross-check against scikit-learn equivalents
- [ ] Visualization: synthetic data with injected outliers, decision boundaries/scores
- [ ] Comparison table across the three paradigms (assumptions, complexity, strengths, weaknesses)
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Builds on distance metrics (Lesson 0a) and density concepts (Lesson 3, DBSCAN). Isolation
Forest needs no distance metric at all — anomalies are isolated in fewer random splits.
LOF reuses the density-reachability idea from DBSCAN but produces a continuous outlier
score rather than a binary cluster/noise label. One-Class SVM treats the origin as the
only "normal" reference point in a kernel-transformed feature space.

## Dependencies
- Blocked by: TASK-UL2 (cluster evaluation, distance/density groundwork)
- Blocks: TASK-UL16 (Anomaly detection practical), DIRECT-UL13 (Professional Practice)
