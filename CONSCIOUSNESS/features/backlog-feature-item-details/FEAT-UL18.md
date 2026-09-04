# FEAT-UL18: Matrix Factorisation Family: NMF and ICA Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Lesson 20 of Unsupervised Learning Part II. Delivers an NMF and ICA lesson; the learner can extract parts-based and statistically independent components where PCA's orthogonal components are the wrong inductive bias. Notebooks: 20a_nmf_ica_theory.ipynb, 20b_nmf_ica_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: the factorisation family compared by constraint
- [ ] **AC-2** — Theory notebook: NMF multiplicative updates derived and shown to decrease the objective monotonically
- [ ] **AC-3** — Theory notebook: ICA identifiability argument (Gaussian sources fail) and non-Gaussianity measures
- [ ] **AC-4** — Theory notebook: FastICA fixed-point derivation
- [ ] **AC-5** — Theory notebook: from-scratch NMF and FastICA validated against synthetic ground truth
- [ ] **AC-6** — Practical notebook: sklearn NMF parts-based decomposition on digits vs PCA
- [ ] **AC-7** — Practical notebook: NMF topic modelling compared with LDA on the same corpus
- [ ] **AC-8** — Practical notebook: FastICA source separation with the PCA failure contrast
- [ ] **AC-9** — Practical notebook: PCA / NMF / ICA decision table
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors)
- [ ] **AC-11** — Cross-lesson link: explicit references to lesson 5 (PCA) and lesson 10 (LDA)

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL18
- Directive: DIRECT-UL17
- Tasks: TASK-UL054, TASK-UL055, TASK-UL056
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
