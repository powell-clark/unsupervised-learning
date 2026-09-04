# TASK-UL058: Lesson 21b practical: Expectation-Maximisation and Variational Inference

## Context
Part II, lesson 21, practical notebook `notebooks/21b_em_variational_inference_practical.ipynb`. Builds on `21a_em_variational_inference_theory.ipynb` (TASK-UL057) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL19.

## Notebook plan (sections, in order)
1. sklearn.mixture.BayesianGaussianMixture: variational GMM in practice, weight_concentration_prior and covariance_prior, effective number of components vs n_components
2. Comparing K chosen by BIC (lesson 4b) against K inferred variationally on the same data
3. Convergence diagnostics: lower_bound_, n_iter_, tol, and what a flat ELBO means
4. A messy real case: variational GMM on load_wine (standardised) with interpretation of pruned components
5. When to prefer EM vs VI vs sampling: a short decision guide setting up lesson 22

**Library:** scikit-learn BayesianGaussianMixture
**Data:** sklearn load_digits, load_wine; synthetic — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL19 are satisfiable from this notebook's content
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
- Blocked by: TASK-UL057
- Blocks: the lesson-21 verification task
