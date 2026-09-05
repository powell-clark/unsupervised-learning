# TASK-UL075: Lesson 27a theory: Clustering Stability, Consensus and Choosing K Honestly

## Context
Part II, lesson 27, theory notebook `notebooks/27a_clustering_stability_theory.ipynb`. As a learner I want a clustering-stability lesson so that I can report how confident a clustering is instead of a single K chosen by one heuristic. Feature card: FEAT-UL25 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. Why internal indices disagree (silhouette vs elbow vs BIC recap from lessons 0b/1b/4b) and what a stable clustering means
2. The gap statistic derived (reference distribution from a uniform box or PCA-aligned box), implemented from scratch with the one-standard-error rule
3. Stability by resampling: subsample, cluster, compare with ARI/NMI; the stability curve over K, implemented from scratch
4. Prediction strength: definition and implementation
5. Consensus clustering: co-association matrices from many runs, hierarchical clustering of the consensus matrix, the consensus-CDF and its area
6. Honest reporting: confidence in K and in individual assignments (per-point consensus)

**From scratch:** gap_statistic(), stability_curve(), prediction_strength(), consensus_matrix() in NumPy
**Data:** make_blobs with varying separation, load_iris, load_wine — no downloads

## Acceptance Criteria
- [x] Every section above present as a titled section with working code where the plan names an implementation — 17 cells (7 code, 10 markdown), all six planned sections present
- [x] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library) — gap statistic, stability curve, prediction strength and consensus-CDF area all validated against a known true K=4 on synthetic blobs; BIC uses sklearn's `GaussianMixture.bic()` directly (Lesson 4B's own tool) after a hand-rolled approximation gave an uninformative monotone curve
- [x] All theory-notebook criteria on FEAT-UL25 are satisfiable from this notebook's content — AC-1 through AC-5 covered with cell-level evidence
- [x] `jupyter execute` passes: every code cell executed, zero errors, outputs committed — 7/7 code cells, zero errors
- [x] Colab-runnable: no local files outside the repo, no network downloads — make_blobs and in-notebook uniform noise only; `load_iris`/`load_wine` deliberately deferred to 27B's real-data application (disclosed in this notebook's own Next Steps), since 27A's job is validating each method against a KNOWN synthetic true K first

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
- Builder model: the session model (sonnet is sufficient).
- Expected duration: 2h

## Dependencies
- Blocked by: none
- Blocks: the 27b practical and the lesson-27 verification task
