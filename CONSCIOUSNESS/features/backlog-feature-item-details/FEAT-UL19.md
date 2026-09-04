# FEAT-UL19: Expectation-Maximisation and Variational Inference Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Lesson 21 of Unsupervised Learning Part II. Delivers a general EM and variational inference lesson; the learner can derive inference for a new latent-variable model rather than only apply the GMM special case. Notebooks: 21a_em_variational_inference_theory.ipynb, 21b_em_variational_inference_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: ELBO derivation via Jensen and EM as coordinate ascent stated generally
- [ ] **AC-2** — Theory notebook: mixture-of-Bernoullis EM from scratch with learned prototypes
- [ ] **AC-3** — Theory notebook: missing-data Gaussian EM from scratch with an imputation-error curve
- [ ] **AC-4** — Theory notebook: mean-field VI and the CAVI update derived
- [ ] **AC-5** — Theory notebook: from-scratch CAVI for a Bayesian GMM with an ELBO monotonicity plot
- [ ] **AC-6** — Practical notebook: sklearn BayesianGaussianMixture with prior sweeps and effective-components analysis
- [ ] **AC-7** — Practical notebook: BIC vs variational K selection compared on the same data
- [ ] **AC-8** — Practical notebook: convergence diagnostics explained
- [ ] **AC-9** — Practical notebook: real-data case (wine) with interpretation
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors)
- [ ] **AC-11** — Cross-lesson link: lesson 4 (GMM EM) is the special case; lesson 12a (ELBO) is the same bound

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL19
- Directive: DIRECT-UL18
- Tasks: TASK-UL057, TASK-UL058, TASK-UL059
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
