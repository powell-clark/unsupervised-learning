# TASK-UL057: Lesson 21a theory: Expectation-Maximisation and Variational Inference

## Context
Part II, lesson 21, theory notebook `notebooks/21a_em_variational_inference_theory.ipynb`. As a learner I want a general EM and variational inference lesson so that I can derive inference for a new latent-variable model rather than only apply the GMM special case. Feature card: FEAT-UL19 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. Latent-variable models in general; the ELBO from Jensen's inequality; EM as coordinate ascent on the ELBO (E-step tightens, M-step maximises) — the general recipe stated once and reused
2. Worked example 1: mixture of Bernoullis on binarised digits (E-step responsibilities, M-step closed form), from scratch, with the learned prototypes plotted
3. Worked example 2: EM for missing-data imputation in a multivariate Gaussian (the sufficient-statistics trick), from scratch, error vs missingness rate
4. Why EM gets stuck: local optima, degenerate components, initialisation strategies
5. Mean-field variational inference: the factorised approximation, the CAVI update q_j ∝ exp E_{-j}[log p], the reverse-KL mode-seeking behaviour illustrated
6. CAVI for a Bayesian GMM with known variances from scratch in NumPy; ELBO monotonicity plot; posterior over mixing weights

**From scratch:** mixture-of-Bernoullis EM, Gaussian missing-data EM, and CAVI for a Bayesian GMM — all NumPy
**Data:** load_digits binarised, synthetic Gaussians — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL19 are satisfiable from this notebook's content (read the card before writing)
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
- Builder model: the session model. If the session model is sonnet, dispatch an opus subagent (Agent tool, model: "opus") to draft and check the derivation sections before you execute the notebook — this lesson's mathematics is where a weaker draft is most likely to be subtly wrong.
- Expected duration: 2h

## Dependencies
- Blocked by: none
- Blocks: the 21b practical and the lesson-21 verification task
