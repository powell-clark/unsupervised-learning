# DIRECT-UL6: Dimensionality Reduction (PCA)

## Context

PCA is the foundational dimensionality reduction technique. TASK-UL11 derives eigendecomposition and SVD from scratch, explaining variance maximization. TASK-UL12 applies kernel PCA and explores applications like Eigenfaces for face recognition.

## Acceptance Criteria

- [ ] TASK-UL11 (0a theory) complete — eigendecomposition, SVD, variance explained, scree plots
- [ ] TASK-UL12 (0b practical) complete — scikit-learn PCA, kernel PCA, Eigenfaces application
- [ ] Both notebooks run in Colab
- [ ] From-scratch PCA via SVD verified against scikit-learn
- [ ] FEAT-UL1 and FEAT-UL2 satisfied

## Technical Notes

Topics: covariance matrix, eigenvalues/eigenvectors, explained variance, dimensionality selection, kernel methods. Application: face recognition using Eigenfaces.

## Dependencies

- Blocked by: DIRECT-UL1 (Clustering Foundations)
- Blocks: DIRECT-UL13 (Professional Practice — preprocessing pipeline)
