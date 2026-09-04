# TASK-UL055: Lesson 20b practical: Matrix Factorisation Family: NMF and ICA

## Context
Part II, lesson 20, practical notebook `notebooks/20b_nmf_ica_practical.ipynb`. Builds on `20a_nmf_ica_theory.ipynb` (TASK-UL054) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL18.

## Notebook plan (sections, in order)
1. sklearn.decomposition.NMF on load_digits: parts-based components vs PCA eigen-digits (lesson 5b), reconstruction error vs n_components, init="nndsvd"
2. NMF as topic modelling on an in-notebook corpus built the same way as lesson 10b (TF-IDF + NMF), compared with the LDA topics from lesson 10 on the same corpus
3. sklearn.decomposition.FastICA: unmixing three synthetic sources (sine, square, sawtooth plus noise), recovered vs true, and the PCA failure on the same mixture
4. ICA on the digits data: independent components vs PCA components, visualised
5. Choosing between PCA / NMF / ICA: a decision table with the lesson's own evidence

**Library:** scikit-learn NMF, FastICA
**Data:** sklearn load_digits; in-notebook corpus and signals — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL18 are satisfiable from this notebook's content
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
- Blocked by: TASK-UL054
- Blocks: the lesson-20 verification task
