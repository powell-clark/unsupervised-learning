# FEAT-UL26: Capstone: An End-to-End Unsupervised Analysis Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p3

## Description
Lesson 28 of Unsupervised Learning Part II. Delivers a capstone that runs a complete unsupervised analysis end to end; the learner can see every tool from both parts of the course chosen, combined and reported on one problem. Notebooks: 28_capstone_pipeline.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [x] **AC-1** — Single notebook: problem framing and a decision log — cells 0/4 (framing), cell 7 (decision_log table)
- [x] **AC-2** — Leakage-safe preprocessing pipeline reused from lesson 15 — cell 7, 80/20 fit/holdout split, every statistic fit on idx_fit only
- [x] **AC-3** — Representation choice made with evidence from at least two candidates — cell 9, raw/PCA/autoencoder compared naive and guarded
- [x] **AC-4** — Clustering with stability/consensus-based K selection and confidence reporting — cell 11: gap+one-SE+stability+GMM cross-check+ARI sanity; K_CHOSEN now unconditionally follows gap_k (TASK-UL086 fix), matching its own printed rationale; round-2 independent review branch-tested this across 8 synthetic scenarios with 0 mismatches
- [x] **AC-5** — Anomaly analysis with at least two density/isolation methods compared — cell 13, Isolation Forest vs KDE
- [x] **AC-6** — A written report section including an explicit not-done-and-why list — cell 15 section 4
- [x] **AC-7** — Notebook runs end-to-end in Google Colab (jupyter execute, zero errors) — independently re-executed by the reviewer, EXIT=0, 7/7 code cells, zero error outputs, every number reproduces exactly from seed 42
- [x] **AC-8** — Cross-lesson link: cites the specific earlier notebooks whose methods it reuses — lessons 5, 12, 15, 18, 26, 27/27A cited by number

## Review history
- **Round 1 (TASK-UL079, 2026-09-05): agent-rejected.** HIGH-severity defect blocking AC-4: cell 11's printed rationale claimed the gap statistic decided the final K, but the code discarded the gap statistic's K=5 pick and fell back to the resampling-stability tie's lowest member (K=3) — the executed choice contradicted its own stated justification. D2-D7 (MEDIUM) and D8-D13 (LOW) also filed as fix criteria on TASK-UL086.
- **Round 2 (TASK-UL086, 2026-09-05): agent-approved.** All D1-D13 fixes independently re-verified (exhaustive branch-testing of the K_CHOSEN logic across 8 synthetic gap/stability scenarios, 0 mismatches; every key number independently re-derived: K_CHOSEN=5, ARI-vs-true 0.226->0.311, km_final_silhouette=0.3832). Reviewer additionally found four non-blocking items (N1 MEDIUM self-introduced regression, N2 MEDIUM pre-existing representation-space artifact where raw and PCA's guarded K=2 winners turned out to be the identical partition, N3/N4 LOW wording) — all fixed in the same pass rather than deferred.

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL26
- Directive: DIRECT-UL25
- Tasks: TASK-UL078, TASK-UL079, TASK-UL086
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
