# TASK-UL076: Lesson 27b practical: Clustering Stability, Consensus and Choosing K Honestly

## Context
Part II, lesson 27, practical notebook `notebooks/27b_clustering_stability_practical.ipynb`. Builds on `27a_clustering_stability_theory.ipynb` (TASK-UL075) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL25.

## Notebook plan (sections, in order)
1. A consensus ensemble over K-Means, GMM, spectral (lesson 17) and HDBSCAN (lesson 3) on load_wine and load_digits; co-association heatmaps
2. Choosing K across methods: gap, stability, silhouette and BIC on one figure per dataset; where they agree and where they do not
3. Per-point uncertainty: points with low consensus flagged and inspected
4. A reporting template: what a defensible clustering write-up contains
5. Runtime budgets: how many resamples are enough (convergence of the stability estimate)

**Library:** scikit-learn, scipy; HDBSCAN via sklearn.cluster.HDBSCAN (sklearn ≥1.3) or the lesson-3 approach
**Data:** sklearn bundled datasets — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL25 are satisfiable from this notebook's content
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
- Blocked by: TASK-UL075
- Blocks: the lesson-27 verification task
