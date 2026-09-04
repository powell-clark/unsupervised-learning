# FEAT-UL16: Kernel Density Estimation and Nonparametric Density Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Lesson 18 of Unsupervised Learning Part II. Delivers a kernel density estimation lesson; the learner can estimate a probability density without assuming a parametric family and use it for scoring and sampling. Notebooks: 18a_kernel_density_estimation_theory.ipynb, 18b_kernel_density_estimation_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: histogram-to-KDE motivation and kernel definition
- [ ] **AC-2** — Theory notebook: bandwidth selection — Scott, Silverman and leave-one-out CV derived and implemented
- [ ] **AC-3** — Theory notebook: bias-variance / over-vs-undersmoothing demonstration
- [ ] **AC-4** — Theory notebook: curse of dimensionality for KDE shown empirically
- [ ] **AC-5** — Theory notebook: from-scratch vectorised 1D and 2D KDE
- [ ] **AC-6** — Practical notebook: sklearn KernelDensity with cross-validated bandwidth and a scipy gaussian_kde comparison
- [ ] **AC-7** — Practical notebook: generative sampling case study (PCA + KDE on digits)
- [ ] **AC-8** — Practical notebook: density-based anomaly scoring compared with lesson 7 methods
- [ ] **AC-9** — Practical notebook: a documented failure case in high dimensions
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors)
- [ ] **AC-11** — Cross-lesson link: GMM (lesson 4) as parametric density vs KDE as nonparametric, stated with a side-by-side fit

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL16
- Directive: DIRECT-UL15
- Tasks: TASK-UL048, TASK-UL049, TASK-UL050
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
