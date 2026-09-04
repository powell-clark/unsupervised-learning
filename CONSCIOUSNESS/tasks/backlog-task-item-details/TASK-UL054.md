# TASK-UL054: Lesson 20a theory: Matrix Factorisation Family: NMF and ICA

## Context
Part II, lesson 20, theory notebook `notebooks/20a_nmf_ica_theory.ipynb`. As a learner I want an NMF and ICA lesson so that I can extract parts-based and statistically independent components where PCA's orthogonal components are the wrong inductive bias. Feature card: FEAT-UL18 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. The factorisation family: PCA (lesson 5), NMF, ICA and the constraints that distinguish them (orthogonality, non-negativity, independence)
2. NMF: objective (Frobenius and KL), the multiplicative update rules derived from the gradient with the Lee-Seung step-size trick, monotone decrease demonstrated numerically, non-uniqueness
3. ICA: the cocktail-party model, why Gaussian sources are unidentifiable (rotation invariance), non-Gaussianity via kurtosis and negentropy, whitening as preprocessing
4. FastICA fixed-point derivation (the logcosh contrast), one-unit and symmetric decorrelation
5. From scratch: nmf() with multiplicative updates and fastica() in NumPy, each validated against a synthetic ground truth

**From scratch:** nmf() multiplicative updates and fastica() fixed-point iteration in NumPy
**Data:** synthetic mixed signals; load_digits for parts-based NMF — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL18 are satisfiable from this notebook's content (read the card before writing)
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
- Blocks: the 20b practical and the lesson-20 verification task
