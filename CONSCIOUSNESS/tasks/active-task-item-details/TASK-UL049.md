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
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL16 are satisfiable from this notebook's content
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
- Blocked by: TASK-UL048
- Blocks: the lesson-18 verification task
