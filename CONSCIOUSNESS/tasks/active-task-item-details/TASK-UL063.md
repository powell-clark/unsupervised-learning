# TASK-UL063: Lesson 23a theory: Hidden Markov Models and Unsupervised Sequence Learning

## Context
Part II, lesson 23, theory notebook `notebooks/23a_hidden_markov_models_theory.ipynb`. As a learner I want a hidden Markov model lesson so that I can discover latent regimes in sequential data without labels. Feature card: FEAT-UL21 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. Markov chains: transition matrices, stationary distributions, a short simulation
2. The HMM generative model: hidden states, emissions, the three problems (evaluation, decoding, learning)
3. Forward-backward with scaling (why naive products underflow), derived and implemented
4. Viterbi decoding derived and implemented; posterior decoding contrasted
5. Baum-Welch as EM (lesson 21 recipe): expected counts, closed-form M-step for Gaussian emissions, implemented from scratch
6. Model selection and pitfalls: local optima, label switching, choosing the number of states

**From scratch:** forward_backward(), viterbi(), baum_welch() for a Gaussian-emission HMM in NumPy, validated on data simulated from a known HMM
**Data:** simulated HMM sequences — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL21 are satisfiable from this notebook's content (read the card before writing)
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
- Blocked by: TASK-UL044
- Blocks: the 23b practical and the lesson-23 verification task
