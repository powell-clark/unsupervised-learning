# TASK-UL049: Lesson 18b practical: Kernel Density Estimation and Nonparametric Density

## Context
Part II, lesson 18, practical notebook `notebooks/18b_kernel_density_estimation_practical.ipynb`. Builds on `18a_kernel_density_estimation_theory.ipynb` (TASK-UL048) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL16.

## Notebook plan (sections, in order)
1. sklearn.neighbors.KernelDensity: kernels, bandwidth chosen by GridSearchCV on score(), comparison with scipy.stats.gaussian_kde
2. Sampling from a fitted KDE with KernelDensity.sample(): PCA(15 components) on load_digits then KDE then inverse_transform to generate new digit images (the classic sklearn example, reproduced and explained)
3. Density-based anomaly scoring: log-density threshold on a held-out set, contrasted with Isolation Forest / LOF from lesson 7 on the same data, PR-AUC compared
4. KDE for visualisation: 2D contour plots of clusters found in earlier lessons
5. When KDE breaks: a high-dimensional example where the scores stop discriminating

**Library:** scikit-learn KernelDensity, scipy.stats.gaussian_kde
**Data:** sklearn load_digits, load_iris; synthetic — no downloads

## Acceptance Criteria
- [x] Every section above present with working code and at least one figure or table per section — all five, each with a figure and a printed table
- [x] The production library result is compared against the lesson's from-scratch implementation at least once — Section 3 compares 18A's `kde_scratch` with `KernelDensity` (6.23e-16) and `gaussian_kde` (4.86e-17), and additionally shows what the unconverted `bw_method` mistake costs (0.0088 against a density peaking at 0.0101)
- [x] All practical-notebook criteria on FEAT-UL16 are satisfiable from this notebook's content — AC-6 (Section 3), AC-7 (Section 4), AC-8 (Section 5), AC-9 (Section 7, Experiment 2), AC-10 (clean execution)
- [x] `jupyter execute` passes: 6 of 6 code cells with sequential execution counts, zero error outputs, run without `--allow-errors`, outputs committed
- [x] Colab-runnable: `load_digits` and `load_iris` only; no downloads, no files outside the repo

## Build notes
Three results contradicted what I had written before running, and each was fixed by changing the experiment or the claim rather than the wording:

1. **The dimension sweep showed the opposite of the curse.** Sweeping PCA components, KDE PR-AUC *rose* from 0.039 (d=2) to 0.222 (d=30) — because each added component brings dimension *and* information, and information won at n≈1,400. The section now reports that failed experiment explicitly, names the confound, and adds a controlled Experiment 2 (10 informative components fixed, pure noise appended) which produces the failure cleanly: KDE 0.1251 → 0.0403, at or below chance, LOF likewise, with the cross-validated bandwidth more than doubling as the mechanism.
2. **Isolation Forest scored below a random baseline** (0.0367 vs 0.0606). Verified this is not a sign error — `score_samples` is higher-is-normal for both KDE and IF, and both are negated identically for `average_precision_score`. It is a genuine mismatch: IF finds points that are easy to isolate, i.e. edge points, while digit 9 sits inside the cloud. Written up as the lesson's point about matching the scoring rule to the anomaly's shape.
3. **The random baseline was a single noisy draw** that outscored Isolation Forest by luck. Now averaged over 60 draws, and the prose corrected — a random ranker's average precision has expectation slightly *above* prevalence when positives are few (measured 0.0606 vs prevalence 0.0503), so the measured baseline is the honest bar.

Also replaced a 1797×1797×64 pairwise distance tensor (~1.6 GB, against 6 GB free) with `NearestNeighbors` before first execution.

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
- Blocked by: TASK-UL048
- Blocks: the lesson-18 verification task
