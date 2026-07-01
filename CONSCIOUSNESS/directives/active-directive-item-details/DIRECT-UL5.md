# DIRECT-UL5: Gaussian Mixture Models

## Context

GMMs provide a probabilistic framework for clustering with soft assignments. TASK-UL9 derives the EM algorithm and explores covariance types (full, tied, diagonal, spherical). TASK-UL10 applies scikit-learn GMM with BIC/AIC model selection and image segmentation.

## Acceptance Criteria

- [ ] TASK-UL9 (0a theory) complete — EM algorithm derivation, covariance structures, BIC/AIC
- [ ] TASK-UL10 (0b practical) complete — GMM fitting, model selection, soft assignments
- [ ] Both notebooks run in Colab
- [ ] From-scratch EM implementation verified
- [ ] FEAT-UL1 and FEAT-UL2 satisfied

## Technical Notes

Topics: Gaussian components, posterior probabilities, EM iterations (E-step, M-step), convergence criteria, model selection, soft vs hard assignments. Application: image segmentation using GMM.

## Dependencies

- Blocked by: DIRECT-UL1 (Clustering Foundations)
- Blocks: DIRECT-UL13 (Professional Practice)
