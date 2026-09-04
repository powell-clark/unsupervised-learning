# FEAT-UL6: PCA Dimensionality Reduction Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Comprehensive lesson on Principal Component Analysis: eigendecomposition, SVD, variance explained, and applications. Covers theory deriving PCA from covariance decomposition alongside practical dimensionality reduction and face recognition.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: Covariance matrix and variance maximization objective
- [x] **AC-2** — Theory notebook: Eigendecomposition of covariance matrix
- [x] **AC-3** — Theory notebook: Singular Value Decomposition (SVD) connection
- [x] **AC-4** — Theory notebook: Choosing number of components (variance explained ratio)
- [x] **AC-5** — Practical notebook: scikit-learn PCA implementation
- [x] **AC-6** — Practical notebook: Explained variance visualization
- [x] **AC-7** — Practical notebook: Kernel PCA for nonlinear dimensionality reduction
- [x] **AC-8** — Practical notebook: Eigenfaces (PCA on face images) classification
- [x] **AC-9** — Practical notebook: Performance: PCA as preprocessing for downstream tasks
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab — verified directly this session while fixing two real bugs (a positional-unpacking mistake in 5a, an undersized axes grid in 5b), 8/8 and 7/7 cells, zero errors
- [x] **AC-11** — Theory includes numerical stability (SVD vs eigendecomposition)
- [x] **AC-12** — Completed task pair: TASK-UL11 (theory) and TASK-UL12 (practical)

## Review (TASK-UL041)
Independent agent review against notebooks/5a_pca_theory.ipynb and
5b_pca_practical.ipynb: all 12 criteria verified directly (this session
worked through both notebooks' code line-by-line while fixing execution
bugs under TASK-UL040 — highest-confidence review in this batch).
agent-approved — stays in backlog pending human sign-off per the
FEAT-UL14 precedent.

## Linked Entities
- Story: STORY-UL6 (PCA learner story)
- Directive: DIRECT-UL6 (Dimensionality Reduction - PCA)
- Tasks: TASK-UL11, TASK-UL12
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
