# FEAT-UL26: Capstone: An End-to-End Unsupervised Analysis Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 28 of Unsupervised Learning Part II. Delivers a capstone that runs a complete unsupervised analysis end to end; the learner can see every tool from both parts of the course chosen, combined and reported on one problem. Notebooks: 28_capstone_pipeline.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [x] **AC-1** — Single notebook: problem framing and a decision log — cells 0/4 (framing), cell 7 (decision_log table)
- [x] **AC-2** — Leakage-safe preprocessing pipeline reused from lesson 15 — cell 7, 80/20 fit/holdout split, every statistic fit on idx_fit only
- [x] **AC-3** — Representation choice made with evidence from at least two candidates — cell 9, raw/PCA/autoencoder compared naive and guarded
- [ ] **AC-4** — Clustering with stability/consensus-based K selection and confidence reporting — mechanism present in cell 11 (gap+one-SE+stability+GMM cross-check+ARI sanity) but BLOCKED: see REJECTION GAPS below (D1)
- [x] **AC-5** — Anomaly analysis with at least two density/isolation methods compared — cell 13, Isolation Forest vs KDE
- [x] **AC-6** — A written report section including an explicit not-done-and-why list — cell 15 section 4
- [x] **AC-7** — Notebook runs end-to-end in Google Colab (jupyter execute, zero errors) — independently re-executed by the reviewer, EXIT=0, 7/7 code cells, zero error outputs, every number reproduces exactly from seed 42
- [x] **AC-8** — Cross-lesson link: cites the specific earlier notebooks whose methods it reuses — lessons 5, 12, 15, 18, 26, 27/27A cited by number

## Rejection gaps (REVIEW-INDEX agent-rejected verdict, TASK-UL079, 2026-09-05)
Independent fresh-context opus review found a HIGH-severity defect blocking AC-4: cell 11's printed rationale claims the gap statistic decided the final K, but the code actually discards the gap statistic's K=5 pick and falls back to the resampling-stability tie's lowest member (K=3) — the executed choice contradicts its own stated justification. Additional MEDIUM-severity honesty defects found (D2-D7) and LOW polish items (D8-D13); full list and fix acceptance criteria filed as TASK-UL086 (Fix lesson 28 capstone: honest K-selection rationale and report). This card stays in backlog with AC-4 unticked until TASK-UL086 lands and TASK-UL079's verification procedure is re-run for approval.

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL26
- Directive: DIRECT-UL25
- Tasks: TASK-UL078, TASK-UL079, TASK-UL086
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
