# TASK-UL14: Manifold Learning Practical (6b)

## Context
Second notebook of Lesson 6 (STORY-UL7). Applies scikit-learn t-SNE and UMAP to real datasets. Demonstrates parameter tuning, perplexity effects, n_neighbors selection, and practical workflow for manifold visualization.

## Acceptance Criteria
- [ ] scikit-learn t-SNE API and parameters
- [ ] Perplexity tuning and its effect on results
- [ ] UMAP API and key hyperparameters
- [ ] n_neighbors and min_dist parameter selection
- [ ] Comparing t-SNE and UMAP on same datasets
- [ ] Digit/MNIST dataset visualization
- [ ] Swiss roll nonlinear structure preservation
- [ ] Iris dataset: checking if clusters are artifacts
- [ ] Practical workflow: when to use t-SNE vs UMAP
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Show parameter effects on actual data. Demonstrate UMAP's speed advantage over t-SNE. Include examples where manifold learning reveals true structure and examples where it creates artifacts. Emphasize the "know your data" principle.

## Dependencies
- Blocked by: TASK-UL13 (theory foundation)
- Blocks: STORY-UL7 (manifold learning story completion)
- Story: STORY-UL7 (Manifold learning learner story)
- Directive: DIRECT-UL7 (Manifold Learning)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production), FEAT-UL7 (Manifold lesson spec)
