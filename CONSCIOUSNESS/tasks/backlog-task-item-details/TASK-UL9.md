# TASK-UL9: GMM Theory (4a)

## Context
First notebook of Lesson 4 (STORY-UL5). Derives Gaussian Mixture Models from first principles: probabilistic clustering, EM algorithm, covariance structures. Provides mathematical foundation for practical GMM implementation in TASK-UL10.

## Acceptance Criteria
- [ ] Gaussian distribution review and mixture model concept
- [ ] EM algorithm derivation (E-step: responsibilities, M-step: parameter updates)
- [ ] Convergence proof and log-likelihood as objective
- [ ] Covariance types: full, tied, diag, spherical (trade-offs)
- [ ] Numerical stability considerations and regularization
- [ ] From-scratch NumPy implementation of EM
- [ ] Comparison: GMM vs K-Means (probabilistic vs hard assignment)
- [ ] Runs top-to-bottom in Google Colab
- [ ] Clear derivations with mathematical notation
- [ ] Reproducible synthetic data examples

## Technical Notes
Foundation for practical implementation. Focus on math clarity over production optimization. Include numpy arrays for demonstrations. Note convergence challenges and regularization strategies.

## Dependencies
- Blocked by: TASK-UL2 (cluster evaluation basics)
- Blocks: TASK-UL10 (practical GMM implementation)
- Story: STORY-UL5 (GMM learner story)
- Directive: DIRECT-UL5 (Gaussian Mixture Models)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production), FEAT-UL5 (GMM lesson spec)
