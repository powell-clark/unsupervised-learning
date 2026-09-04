# FEAT-UL26: Capstone: An End-to-End Unsupervised Analysis Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 28 of Unsupervised Learning Part II. Delivers a capstone that runs a complete unsupervised analysis end to end; the learner can see every tool from both parts of the course chosen, combined and reported on one problem. Notebooks: 28_capstone_pipeline.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Single notebook: problem framing and a decision log
- [ ] **AC-2** — Leakage-safe preprocessing pipeline reused from lesson 15
- [ ] **AC-3** — Representation choice made with evidence from at least two candidates
- [ ] **AC-4** — Clustering with stability/consensus-based K selection and confidence reporting
- [ ] **AC-5** — Anomaly analysis with at least two density/isolation methods compared
- [ ] **AC-6** — A written report section including an explicit not-done-and-why list
- [ ] **AC-7** — Notebook runs end-to-end in Google Colab (jupyter execute, zero errors)
- [ ] **AC-8** — Cross-lesson link: cites the specific earlier notebooks whose methods it reuses

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL26
- Directive: DIRECT-UL25
- Tasks: TASK-UL078, TASK-UL079
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
