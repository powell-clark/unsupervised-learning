# TASK-UL070: Lesson 25b practical: Word and Item Embeddings: word2vec and Skip-Gram with Negative Sampling

## Context
Part II, lesson 25, practical notebook `notebooks/25b_word_embeddings_practical.ipynb`. Builds on `25a_word_embeddings_theory.ipynb` (TASK-UL069) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL23.

## Notebook plan (sections, in order)
1. gensim.models.Word2Vec: sg=1, negative sampling, vector_size / window / min_count / epochs; training on the same in-notebook corpus and comparing neighbours to the from-scratch model
2. Analogy arithmetic and most_similar; where analogies work and where they are noise on a small corpus (honest)
3. Embeddings as features: K-Means (lesson 1) and HDBSCAN (lesson 3) over the learned vectors; t-SNE/UMAP (lesson 6) visualisation
4. Item2vec with gensim on basket sessions from the lesson-9 generator; recommendations by nearest neighbour compared with the lesson-8 collaborative-filtering approach
5. Practical guidance: corpus size, window semantics, evaluating without labels

**Library:** gensim Word2Vec (already in requirements)
**Data:** in-notebook generated corpus and baskets — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL23 are satisfiable from this notebook's content
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
- Blocked by: TASK-UL069
- Blocks: the lesson-25 verification task
