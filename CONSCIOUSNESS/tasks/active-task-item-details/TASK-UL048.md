# TASK-UL048: Lesson 18a theory: Kernel Density Estimation and Nonparametric Density

## Context
Part II, lesson 18, theory notebook `notebooks/18a_kernel_density_estimation_theory.ipynb`. As a learner I want a kernel density estimation lesson so that I can estimate a probability density without assuming a parametric family and use it for scoring and sampling. Feature card: FEAT-UL16 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. From histograms to KDE: bin-width sensitivity, the Parzen window, kernel definition and the properties a kernel needs
2. Kernels (Gaussian, Epanechnikov, tophat, triangular) and why the kernel matters less than the bandwidth
3. Bandwidth selection: Scott and Silverman rules derived from the AMISE argument for Gaussian data, leave-one-out cross-validated log-likelihood implemented from scratch
4. Bias-variance of KDE: oversmoothing vs undersmoothing shown on a bimodal target, MISE convergence rate stated
5. Multivariate KDE and the curse of dimensionality: how sample requirements grow with d, demonstrated by error vs d on a known density
6. From scratch: a vectorised NumPy kde(x_query, X, h, kernel) for 1D and 2D, plus loo_cv_bandwidth()

**From scratch:** kde() and loo_cv_bandwidth() in NumPy; Scott/Silverman rules implemented and compared to LOO-CV
**Data:** synthetic bimodal mixtures, load_iris / load_digits features — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL16 are satisfiable from this notebook's content (read the card before writing)
- [ ] `jupyter execute` passes: every code cell executed, zero errors, outputs committed
- [ ] Colab-runnable: no local files outside the repo, no network downloads

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
- Blocks: the 18b practical and the lesson-18 verification task
