# TASK-UL073: Lesson 26b practical: Self-Supervised Contrastive Representation Learning

## Context
Part II, lesson 26, practical notebook `notebooks/26b_contrastive_learning_practical.ipynb`. Builds on `26a_contrastive_learning_theory.ipynb` (TASK-UL072) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL24.

## Notebook plan (sections, in order)
1. SimCLR training on an MNIST subset, CPU-bounded (few epochs, small encoder); embedding quality tracked by a linear probe on frozen features
2. The comparison that matters: linear-probe accuracy of contrastive features vs PCA (lesson 5) vs a convolutional autoencoder bottleneck (lesson 12b), same subset, same probe
3. k-NN on embeddings and a t-SNE/UMAP view (lesson 6) of the three representation types side by side
4. Ablations: temperature, batch size / number of negatives, augmentation strength — each with a plot
5. Guidance: when self-supervised pretraining pays off, compute cost, and the labelled-data-scarcity link to lesson 16

**Library:** PyTorch (from scratch), scikit-learn for probes and t-SNE
**Data:** cached MNIST — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL24 are satisfiable from this notebook's content
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
- Blocked by: TASK-UL072
- Blocks: the lesson-26 verification task
