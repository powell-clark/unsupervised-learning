# FEAT-UL24: Self-Supervised Contrastive Representation Learning Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 26 of Unsupervised Learning Part II. Delivers a contrastive learning lesson; the learner can measure with a linear probe whether self-supervised image features beat PCA and autoencoder features on the same unlabelled data. Notebooks: 26a_contrastive_learning_theory.ipynb, 26b_contrastive_learning_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: pretext tasks and invariance framing
- [ ] **AC-2** — Theory notebook: InfoNCE derived with the mutual-information bound and temperature discussion
- [ ] **AC-3** — Theory notebook: NT-Xent implemented from scratch in PyTorch
- [ ] **AC-4** — Theory notebook: collapse and non-contrastive alternatives explained
- [ ] **AC-5** — Theory notebook: tiny end-to-end MNIST run with loss curve and embedding plot
- [ ] **AC-6** — Practical notebook: SimCLR with a linear-probe evaluation
- [ ] **AC-7** — Practical notebook: contrastive vs PCA vs autoencoder features under the same probe
- [ ] **AC-8** — Practical notebook: k-NN and 2D visualisation of the three representations
- [ ] **AC-9** — Practical notebook: temperature / negatives / augmentation ablations
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab on CPU (jupyter execute, zero errors; training bounded to a few minutes)
- [ ] **AC-11** — Cross-lesson link: lessons 5, 6, 12 and 16 referenced concretely

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL24
- Directive: DIRECT-UL23
- Tasks: TASK-UL072, TASK-UL073, TASK-UL074
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
