# TASK-UL060: Lesson 22a theory: Bayesian Nonparametric Clustering: Dirichlet Process Mixtures

## Context
Part II, lesson 22, theory notebook `notebooks/22a_dirichlet_process_mixtures_theory.ipynb`. As a learner I want a Dirichlet process mixture lesson so that I can let the data decide the number of clusters instead of sweeping K. Feature card: FEAT-UL20 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. The problem with choosing K; priors over partitions
2. The Chinese restaurant process: definition, exchangeability, the rich-get-richer effect, expected number of tables ≈ α log n derived and simulated
3. Stick-breaking construction of the Dirichlet process; equivalence with the CRP stated; the concentration parameter α
4. DP mixture model: generative story; why marginalising the mixture weights gives the CRP prior over assignments
5. Collapsed Gibbs sampling for a DP-GMM with conjugate (Normal-Normal, known variance) components from scratch: predictive likelihood, the new-cluster probability, label-switching caveat
6. Posterior over the number of clusters from the sampler traces; sensitivity to α

**From scratch:** CRP simulator, stick-breaking sampler, collapsed Gibbs DP-GMM in NumPy
**Data:** synthetic 2D mixtures with unknown K — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL20 are satisfiable from this notebook's content (read the card before writing)
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
- Blocks: the 22b practical and the lesson-22 verification task
