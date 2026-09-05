# STORY-UL19: Expectation-Maximisation and Variational Inference

**Status:** fulfilled

As a learner I want a general EM and variational inference lesson so that I can derive inference for a new latent-variable model rather than only apply the GMM special case.

## Outcome
Fulfilled on FEAT-UL19 reaching `maintained` via REVIEW-UL079 (agent-approved, all 11 acceptance criteria met with cell-index evidence and an independent re-execution, 2026-09-05). Two notebooks delivered: 21a_em_variational_inference_theory.ipynb (general EM via Jensen/ELBO, mixture-of-Bernoullis EM, missing-data Gaussian EM, mean-field CAVI, from-scratch Bayesian GMM) and 21b_em_variational_inference_practical.ipynb (BayesianGaussianMixture practice, BIC-vs-variational K, convergence diagnostics, a real load_wine case, a decision guide). 21a additionally passed a dedicated adversarial math review that found and fixed 7 issues before the feature-level review ran.

## Linked Entities
- Directive: DIRECT-UL18
- Feature: FEAT-UL19 (plus cross-cutting FEAT-UL1, FEAT-UL2)
- Tasks: TASK-UL057, TASK-UL058, TASK-UL059
