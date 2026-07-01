# TASK-UL10: GMM Practical (4b)

## Context
Second notebook of Lesson 4 (STORY-UL5). Applies scikit-learn's GaussianMixture to real data with focus on model selection (BIC/AIC), hyperparameter tuning, and soft cluster interpretation. Image segmentation case study.

## Acceptance Criteria
- [ ] scikit-learn GaussianMixture usage and parameters
- [ ] Fitting GMM and extracting learned parameters
- [ ] Responsibilities (soft assignments) extraction and interpretation
- [ ] BIC and AIC model selection criteria
- [ ] Choosing optimal number of clusters K
- [ ] Visualizing uncertainty: soft vs hard assignments
- [ ] Image segmentation case study (RGB or grayscale)
- [ ] Comparison: full vs diagonal vs spherical covariances
- [ ] Performance metrics: silhouette score, likelihood per sample
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Focus on practical workflow: fit, evaluate, tune K, interpret assignments. Show how soft assignments differ from K-Means hard assignments. Use real data (not just toy 2D).

## Dependencies
- Blocked by: TASK-UL9 (theory foundation)
- Blocks: STORY-UL5 (GMM story completion)
- Story: STORY-UL5 (GMM learner story)
- Directive: DIRECT-UL5 (Gaussian Mixture Models)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production), FEAT-UL5 (GMM lesson spec)
