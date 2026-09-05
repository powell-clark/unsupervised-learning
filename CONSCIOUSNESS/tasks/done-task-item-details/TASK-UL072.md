# TASK-UL072: Lesson 26a theory: Self-Supervised Contrastive Representation Learning

## Context
Part II, lesson 26, theory notebook `notebooks/26a_contrastive_learning_theory.ipynb`. As a learner I want a contrastive learning lesson so that I can learn representations from unlabelled images that transfer to downstream tasks better than reconstruction-based features. Feature card: FEAT-UL24 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. Pretext tasks and the idea of invariance; why reconstruction (lesson 12) is not the only route to representations
2. Noise-contrastive estimation → InfoNCE: derivation, the mutual-information lower bound, the role of temperature and the number of negatives
3. SimCLR: two augmented views, encoder + projection head, the NT-Xent loss written out and implemented from scratch in PyTorch
4. Why representations collapse without negatives; BYOL / VICReg as non-contrastive answers (conceptual only)
5. Augmentations as the specification of invariance: what crops, flips and noise say about the data
6. A tiny end-to-end run on an MNIST subset (the repo's cached MNIST, no download): the loss curve and a t-SNE of embeddings coloured by the held-out labels

**From scratch:** NT-Xent / InfoNCE loss and a small CNN encoder written by hand in PyTorch
**Data:** cached MNIST under notebooks/data — no downloads

## Acceptance Criteria
- [x] Every section above present as a titled section with working code where the plan names an implementation — 28 cells (12 code, 16 markdown), all six planned sections present
- [x] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library) — NT-Xent implemented three independent ways (plain Python, hand-written log-sum-exp tensors, `F.cross_entropy`), agreeing to float32 round-off (worst spread 1.01e-6) and matching a hand-derived closed form ($\log(1+2/e)$) to 6.42e-8; InfoNCE's MI lower bound checked against a closed-form joint distribution across M=2..1024 with standard errors quoted throughout
- [x] All theory-notebook criteria on FEAT-UL24 are satisfiable from this notebook's content — AC-1 through AC-5 covered with cell-level evidence; AC-11's cross-lesson references (5, 6, 12, 25) integrated substantively, not as footnotes
- [x] `jupyter execute` passes: every code cell executed, zero errors, outputs committed — 12/12 code cells, zero errors
- [x] Colab-runnable: no local files outside the repo, no network downloads — MNIST loaded from the repo's cached `notebooks/data/MNIST`, confirmed no network calls

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
- Blocks: the 26b practical and the lesson-26 verification task
