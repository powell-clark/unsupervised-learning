# STORY-UL22: Time-Series Clustering and Dynamic Time Warping

**Status:** fulfilled

As a learner I want a time-series clustering lesson so that I can group sequences by shape when Euclidean distance on raw samples is the wrong metric.

## Outcome
Fulfilled on FEAT-UL22 reaching `maintained` via REVIEW-UL092 (agent-approved, all 11 acceptance criteria met with cell-index evidence and an independent re-execution, 2026-09-05). Two notebooks delivered: 24a_time_series_clustering_theory.ipynb (DTW derived and validated against a true recursive path enumeration, Sakoe-Chiba band measured for both speed and quality, DBA cutting total distance 69.3%, from-scratch DTW k-medoids recovering shape classes exactly where Euclidean k-medoids fails) and 24b_time_series_clustering_practical.ipynb (tslearn cross-checked exactly against 24a's from-scratch DTW, TimeSeriesKMeans across three metrics on real labelled Trace data, DTW-silhouette K-selection, runtime scaling measured, feature-based alternative tested honestly against DTW shape-clustering). The reviewer independently re-derived all 8 quantitative claims under stricter tests than the notebooks apply to themselves (a true unmemoised path enumerator, an exhaustive medoid search, an independent DBA) and caught 14 findings — an inaccurate band-footprint claim, a mislabelled "coordinate ascent", a hardcoded speedup overclaim, and others — all fixed before the final verdict.

## Linked Entities
- Directive: DIRECT-UL21
- Feature: FEAT-UL22 (plus cross-cutting FEAT-UL1, FEAT-UL2)
- Tasks: TASK-UL066, TASK-UL067, TASK-UL068
