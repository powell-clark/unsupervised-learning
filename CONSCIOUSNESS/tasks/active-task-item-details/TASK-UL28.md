# TASK-UL28: Dimensionality Reduction Pipeline (14)

## Context
Second notebook of Lesson 14 (STORY-UL14, DIRECT-UL13, FEAT-UL13). Synthesizes PCA and
manifold learning (Lessons 5-6) into pipeline design guidance: feature selection versus
feature extraction, and when to reach for PCA versus a manifold method.

## Acceptance Criteria
- [ ] Feature selection vs feature extraction: definitions and the trade-off between them
- [ ] Feature selection methods: variance threshold, univariate selection, model-based (importance) selection
- [ ] Empirical comparison: feature selection vs PCA feature extraction on the same dataset (downstream task performance, interpretability, dimensionality achieved)
- [ ] Full pipeline: raw features -> preprocessing -> reduction -> downstream use, built with sklearn Pipeline
- [ ] Decision guide: when to use PCA vs manifold learning (t-SNE/UMAP) vs feature selection, grounded in the trade-offs (interpretability, downstream task, out-of-sample projection)
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Feature selection keeps a subset of the original, interpretable features; feature extraction
(PCA) creates new features as combinations of the originals, sacrificing interpretability for
capturing more shared variance in fewer dimensions. Manifold methods (Lesson 6) are extraction
too, but nonlinear and typically without a clean out-of-sample transform (t-SNE) or with one
(UMAP) — a genuine practical distinction from PCA's linear, always-invertible transform. Build
on sklearn's Pipeline abstraction since that is the production pattern for chaining
preprocessing and reduction steps.

## Dependencies
- Blocked by: TASK-UL12, TASK-UL14 (PCA and manifold learning practicals), TASK-UL27 (comparison-lesson pattern)
- Blocks: none
- Story: STORY-UL14 (Professional-practice learner story)
- Directive: DIRECT-UL13 (Professional Practice)
- Feature: FEAT-UL13 (Professional Practice Lesson), FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
