# TASK-UL067: Lesson 24b practical: Time-Series Clustering and Dynamic Time Warping

## Context
Part II, lesson 24, practical notebook `notebooks/24b_time_series_clustering_practical.ipynb`. Builds on `24a_time_series_clustering_theory.ipynb` (TASK-UL066) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL22.

## Notebook plan (sections, in order)
1. tslearn: TimeSeriesScalerMeanVariance, TimeSeriesKMeans with metric euclidean / dtw / softdtw on the bundled CachedDatasets "Trace" set — TASK-UL044 confirmed this loads offline, shape (100, 275, 1), 4 classes, so use it directly; no fallback branch needed
2. Cluster barycenters plotted per metric; ARI against the known Trace classes
3. Silhouette with a DTW distance matrix (tslearn.metrics.cdist_dtw) to choose K
4. Runtime comparison: unconstrained DTW vs Sakoe-Chiba vs Euclidean as series length grows
5. Feature-based alternative: summary statistics + K-Means from lesson 1, compared honestly

**Library:** tslearn (added to requirements by the environment task)
**Data:** tslearn CachedDatasets "Trace" (ships inside the tslearn wheel; verified offline by TASK-UL044) — no network

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL22 are satisfiable from this notebook's content
- [ ] `jupyter execute` passes: every code cell executed, zero errors, outputs committed
- [ ] Colab-runnable: no network downloads (a bundled/cached dataset or an in-notebook generator only)

## Build rules (house pattern — read two Part I notebooks first, e.g. 5a/5b or 12a/12b)
- Open with a story-driven motivation, then a Table of Contents with anchor links, then a Required Libraries cell.
- Derivations in markdown with LaTeX; every claim that can be checked numerically is checked in a code cell.
- From-scratch implementation first, production library second, and one cell that shows the two agree (or explains why they differ).
- No network downloads: only sklearn/networkx bundled data, in-notebook generators, or the cached MNIST under notebooks/data. If a step would download, replace it with a generator and say so in a markdown cell.
- Keep any training cell under ~3 minutes on CPU; bound epochs and sample sizes accordingly.
- Reuse earlier-lesson code patterns rather than re-inventing (reference the lesson by number in markdown).
- Finish with a Conclusion: key takeaways, practical guidance, what was NOT covered and why (honesty section), next steps.
- Execute in place before committing: `jupyter execute notebooks/<nb> --output /tmp/<nb>`, confirm every code cell ran with zero errors, copy back over the committed file. Commit with the task id in the subject.

## Execution
- Builder model: the session model (sonnet is sufficient)
- Expected duration: 2h

## Dependencies
- Blocked by: TASK-UL066
- Blocks: the lesson-24 verification task
