# TASK-UL061: Lesson 22b practical: Bayesian Nonparametric Clustering: Dirichlet Process Mixtures

## Context
Part II, lesson 22, practical notebook `notebooks/22b_dirichlet_process_mixtures_practical.ipynb`. Builds on `22a_dirichlet_process_mixtures_theory.ipynb` (TASK-UL060) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL20.

## Notebook plan (sections, in order)
1. sklearn BayesianGaussianMixture with weight_concentration_prior_type="dirichlet_process": truncation level, weight_concentration_prior sweep, effective components
2. The same data through BIC-selected GMM (lesson 4b), silhouette-selected K-Means (lesson 0b), and the DP model — where they agree and disagree
3. Real data: load_digits after PCA, DP mixture vs the known 10 classes (ARI), and what over/under-clustering looks like
4. Practical pitfalls: truncation too low, prior too strong, non-Gaussian clusters
5. A decision guide: when nonparametric is worth it

**Library:** scikit-learn BayesianGaussianMixture (dirichlet_process prior)
**Data:** sklearn load_digits; synthetic — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL20 are satisfiable from this notebook's content
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
- Blocked by: TASK-UL060
- Blocks: the lesson-22 verification task
