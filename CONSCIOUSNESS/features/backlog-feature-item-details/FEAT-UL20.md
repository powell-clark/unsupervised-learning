# FEAT-UL20: Bayesian Nonparametric Clustering: Dirichlet Process Mixtures Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Lesson 22 of Unsupervised Learning Part II. Delivers a Dirichlet process mixture lesson; the learner can let the data decide the number of clusters instead of sweeping K. Notebooks: 22a_dirichlet_process_mixtures_theory.ipynb, 22b_dirichlet_process_mixtures_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: CRP defined, simulated, and the α log n growth verified
- [ ] **AC-2** — Theory notebook: stick-breaking construction and its relation to the CRP
- [ ] **AC-3** — Theory notebook: DP mixture generative model stated
- [ ] **AC-4** — Theory notebook: from-scratch collapsed Gibbs sampler for a DP-GMM with posterior over K
- [ ] **AC-5** — Theory notebook: sensitivity to the concentration parameter shown
- [ ] **AC-6** — Practical notebook: sklearn DP mixture with truncation and prior sweeps
- [ ] **AC-7** — Practical notebook: three-way comparison with BIC-GMM and silhouette K-Means
- [ ] **AC-8** — Practical notebook: real-data case with ARI against known classes
- [ ] **AC-9** — Practical notebook: pitfalls and decision guide
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors; the Gibbs sampler bounded to a couple of minutes)
- [ ] **AC-11** — Cross-lesson link: lesson 21 (VI) provides the inference used by sklearn; lesson 4 the finite special case

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL20
- Directive: DIRECT-UL19
- Tasks: TASK-UL060, TASK-UL061, TASK-UL062
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
