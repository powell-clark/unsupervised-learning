# TASK-UL064: Lesson 23b practical: Hidden Markov Models and Unsupervised Sequence Learning

## Context
Part II, lesson 23, practical notebook `notebooks/23b_hidden_markov_models_practical.ipynb`. Builds on `23a_hidden_markov_models_theory.ipynb` (TASK-UL063) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL21.

## Notebook plan (sections, in order)
1. hmmlearn.hmm.GaussianHMM: fitting, decoding, scoring; comparison with the from-scratch implementation on the same simulated data
2. Regime detection on a synthetic returns-like series with volatility regimes built in-notebook; decoded regimes plotted against the truth
3. Choosing n_components by held-out log-likelihood and BIC; the effect of n_iter and multiple restarts
4. A multivariate case (2-3 correlated signals) and covariance_type choices
5. What HMMs get wrong: duration modelling, non-stationarity; pointers to HSMMs

**Library:** hmmlearn (added to requirements by the environment task)
**Data:** in-notebook simulations — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL21 are satisfiable from this notebook's content
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
- Blocked by: TASK-UL063
- Blocks: the lesson-23 verification task
