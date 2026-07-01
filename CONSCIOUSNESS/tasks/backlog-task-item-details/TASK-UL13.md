# TASK-UL13: Manifold Learning Theory (6a)

## Context
First notebook of Lesson 6 (STORY-UL7). Derives manifold learning from first principles: neighborhood graphs, t-SNE (SNE → symmetric SNE → t-SNE), UMAP (fuzzy topological structures). Foundation for practical visualization and manifold reduction.

## Acceptance Criteria
- [ ] Manifold hypothesis and local/global structure preservation
- [ ] Neighborhood graphs and k-NN construction
- [ ] SNE: Symmetric SNE derivation and gradient descent
- [ ] t-SNE: Student-t kernel, why it works better than Gaussian
- [ ] Perplexity parameter and its interpretation
- [ ] UMAP: Fuzzy topological spaces and graph layout
- [ ] UMAP vs t-SNE: differences in approach and results
- [ ] Caveats about visualization artifacts (clustering may be artificial)
- [ ] From-scratch NumPy implementation of simplified t-SNE
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Focus on why manifold learning works: preserve local structure and approximate global structure. Show t-SNE's non-convex optimization. Demonstrate UMAP's speed and preservation of both local and global structure. Include toy 2D data and high-dimensional examples.

## Dependencies
- Blocked by: TASK-UL2 (cluster evaluation basics - for context only)
- Blocks: TASK-UL14 (practical manifold visualization)
- Story: STORY-UL7 (Manifold learning learner story)
- Directive: DIRECT-UL7 (Manifold Learning)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production), FEAT-UL7 (Manifold lesson spec)
