# TASK-UL069: Lesson 25a theory: Word and Item Embeddings: word2vec and Skip-Gram with Negative Sampling

## Context
Part II, lesson 25, theory notebook `notebooks/25a_word_embeddings_theory.ipynb`. As a learner I want a word2vec lesson so that I can learn dense representations of discrete tokens or items from co-occurrence alone. Feature card: FEAT-UL23 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. The distributional hypothesis; one-hot vs dense representations; co-occurrence matrices and PMI
2. Skip-gram: the softmax objective and why it is too expensive; negative sampling derived as a binary classification surrogate; the unigram^0.75 sampling distribution
3. SGNS as implicit matrix factorisation of shifted PMI (Levy & Goldberg) — stated and checked numerically on a small corpus
4. Gradients for the SGNS loss derived by hand; the training loop
5. From scratch: sgns_train() in NumPy on an in-notebook corpus built the way lesson 10b builds its corpus (structured generator, no download); nearest neighbours and a 2D PCA/t-SNE plot of the embeddings
6. Item2vec: the same algorithm on baskets from the lesson-9 generator — items that co-occur end up close

**From scratch:** sgns_train() with negative sampling and hand-derived gradients in NumPy
**Data:** in-notebook generated corpus and baskets — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL23 are satisfiable from this notebook's content (read the card before writing)
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
- Blocks: the 25b practical and the lesson-25 verification task
