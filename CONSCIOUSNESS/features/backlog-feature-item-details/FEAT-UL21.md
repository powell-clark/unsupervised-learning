# FEAT-UL21: Hidden Markov Models and Unsupervised Sequence Learning Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Lesson 23 of Unsupervised Learning Part II. Delivers a hidden Markov model lesson; the learner can discover latent regimes in sequential data without labels. Notebooks: 23a_hidden_markov_models_theory.ipynb, 23b_hidden_markov_models_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: Markov chains and the HMM generative model
- [ ] **AC-2** — Theory notebook: scaled forward-backward derived and implemented
- [ ] **AC-3** — Theory notebook: Viterbi derived and implemented
- [ ] **AC-4** — Theory notebook: Baum-Welch from scratch recovering parameters of a simulated HMM
- [ ] **AC-5** — Theory notebook: model selection and pitfalls discussed
- [ ] **AC-6** — Practical notebook: hmmlearn GaussianHMM matched against the from-scratch implementation
- [ ] **AC-7** — Practical notebook: regime detection case study with decoded regimes vs truth
- [ ] **AC-8** — Practical notebook: n_components selection by held-out likelihood / BIC with restarts
- [ ] **AC-9** — Practical notebook: multivariate case with covariance_type comparison
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors)
- [ ] **AC-11** — Cross-lesson link: Baum-Welch framed as the lesson-21 EM recipe

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL21
- Directive: DIRECT-UL20
- Tasks: TASK-UL063, TASK-UL064, TASK-UL065
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
