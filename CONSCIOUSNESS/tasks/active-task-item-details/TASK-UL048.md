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
- [x] Every section above present as a titled section with working code where the plan names an implementation — all six, plus an added Section 9 (GMM vs KDE) covering FEAT-UL16 AC-11
- [x] The from-scratch implementation is validated numerically inside the notebook — `kde_1d` agrees with sklearn `KernelDensity` to 1.28e-15 and scipy `gaussian_kde` to 3.33e-16 (gaussian), 4.44e-16 / 3.89e-16 for epanechnikov / tophat, and `kde_nd` with sklearn to 9.71e-16 on 2-D iris; the estimate integrates to 1.000000
- [x] All theory-notebook criteria on FEAT-UL16 are satisfiable from this notebook's content — AC-1 (Section 3), AC-2 (Section 6, all three rules implemented), AC-3 (Section 7), AC-4 (Section 8), AC-5 (Section 10, 1-D and 2-D), AC-11 (Section 9)
- [x] `jupyter execute` passes: 9 of 9 code cells executed with sequential counts, zero error outputs, outputs committed (run without `--allow-errors`)
- [x] Colab-runnable: synthetic generators plus `load_iris`; no network downloads, no files outside the repo

## Build notes
Two self-checks changed the content rather than the wording, both caught by reading the executed output against the prose:
- The `h ∝ n^(-1/5)` "verification" was originally a fit to `h_amise(n)`, which IS that formula — arithmetic presented as evidence. Replaced with a grid search for the ISE-minimising bandwidth at each n; the searched slope comes out -0.247 against theory -0.200, and the MISE slope -0.729 against -0.800, with the grid resolution named as the source of the gap.
- The kernel-comparison table has tophat beating the AMISE-optimal Epanechnikov at a common h. That is not an error — it is the lesson's own point about efficiency differences sitting under sampling noise — so the notebook now says so explicitly instead of leaving an apparent contradiction on the page.

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
