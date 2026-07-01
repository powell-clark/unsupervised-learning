# TASK-UL11: PCA Theory (5a)

## Context
First notebook of Lesson 5 (STORY-UL6). Derives Principal Component Analysis from first principles: covariance matrices, eigendecomposition, Singular Value Decomposition (SVD), variance explained. Foundation for practical dimensionality reduction.

## Acceptance Criteria
- [ ] Covariance matrix review and variance maximization objective
- [ ] Eigendecomposition of covariance matrix (eigenvectors as principal components)
- [ ] Singular Value Decomposition (SVD) connection to PCA
- [ ] Deriving principal components from scratch using NumPy
- [ ] Computing explained variance ratio and cumulative variance
- [ ] Choosing number of components (variance threshold)
- [ ] Numerical stability: centering and scaling data
- [ ] From-scratch NumPy implementation (no sklearn)
- [ ] Comparison: eigendecomposition vs SVD numerically
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Focus on mathematical foundations: covariance, eigenvalues as variances, eigenvectors as directions. Show SVD as numerically stable alternative. Include toy 2D and real high-dimensional examples.

## Dependencies
- Blocked by: TASK-UL2 (cluster evaluation basics - for context only)
- Blocks: TASK-UL12 (practical PCA applications)
- Story: STORY-UL6 (PCA learner story)
- Directive: DIRECT-UL6 (Dimensionality Reduction - PCA)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production), FEAT-UL6 (PCA lesson spec)
