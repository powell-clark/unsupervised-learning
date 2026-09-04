# FEAT-UL17: Normalizing Flows and Modern Density Models Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Lesson 19 of Unsupervised Learning Part II. Delivers a normalizing-flows lesson; the learner can build a generative model with an exact likelihood and understand how it differs from VAEs, GANs and diffusion models. Notebooks: 19a_normalizing_flows_theory.ipynb, 19b_normalizing_flows_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: change-of-variables derivation with worked examples
- [ ] **AC-2** — Theory notebook: affine coupling layer construction with the triangular-Jacobian argument
- [ ] **AC-3** — Theory notebook: exact likelihood vs ELBO comparison
- [ ] **AC-4** — Theory notebook: from-scratch PyTorch flow trained on 2D data with density contours and samples
- [ ] **AC-5** — Practical notebook: deeper RealNVP compared against KDE on the same data
- [ ] **AC-6** — Practical notebook: minimal from-scratch DDPM on 2D data with forward process, noise predictor and sampling
- [ ] **AC-7** — Practical notebook: VAE / flow / diffusion / GAN comparison table grounded in the lesson's own models
- [ ] **AC-8** — Practical notebook: flow log-density used as an anomaly score
- [ ] **AC-9** — Both notebooks run end-to-end in Google Colab on CPU (jupyter execute, zero errors; training cells bounded to a few minutes)
- [ ] **AC-10** — Cross-lesson link: builds explicitly on lesson 12a (VAE/ELBO) and lesson 18 (KDE)

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL17
- Directive: DIRECT-UL16
- Tasks: TASK-UL051, TASK-UL052, TASK-UL053
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
