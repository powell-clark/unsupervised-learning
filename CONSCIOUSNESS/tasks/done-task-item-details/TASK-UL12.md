# TASK-UL12: PCA Practical (5b)

## Context
Second notebook of Lesson 5 (STORY-UL6). Applies scikit-learn PCA and kernel PCA to real data. Demonstrates Eigenfaces (face recognition with PCA), preprocessing benefits, and practical component selection workflows.

## Acceptance Criteria
- [ ] scikit-learn PCA usage and fit/transform API
- [ ] Extracting components and explained variance ratios
- [ ] Scree plot visualization for K selection
- [ ] Data standardization (when and why to scale)
- [ ] Kernel PCA for nonlinear dimensionality reduction
- [ ] Eigenfaces: PCA applied to face images
- [ ] Face recognition accuracy with varying number of components
- [ ] PCA as preprocessing: impact on downstream tasks
- [ ] Reconstruction error vs number of components
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Use a face dataset (LFW, Yale Faces, or synthetic). Compare linear PCA to kernel PCA on the same data. Show reconstruction quality improving with components. Demonstrate that PCA can serve as a feature extractor for classification.

## Dependencies
- Blocked by: TASK-UL11 (theory foundation)
- Blocks: STORY-UL6 (PCA story completion)
- Story: STORY-UL6 (PCA learner story)
- Directive: DIRECT-UL6 (Dimensionality Reduction - PCA)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production), FEAT-UL6 (PCA lesson spec)
