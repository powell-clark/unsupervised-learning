# FEAT-UL22: Time-Series Clustering and Dynamic Time Warping Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Lesson 24 of Unsupervised Learning Part II. Delivers a time-series clustering lesson; the learner can group sequences by shape when Euclidean distance on raw samples is the wrong metric. Notebooks: 24a_time_series_clustering_theory.ipynb, 24b_time_series_clustering_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: Euclidean-vs-shape failure demonstration
- [ ] **AC-2** — Theory notebook: DTW derived and implemented with path backtracking
- [ ] **AC-3** — Theory notebook: Sakoe-Chiba constraint implemented with a runtime/quality comparison
- [ ] **AC-4** — Theory notebook: DBA explained and implemented
- [ ] **AC-5** — Theory notebook: from-scratch DTW k-medoids
- [ ] **AC-6** — Practical notebook: tslearn TimeSeriesKMeans across three metrics with barycenters
- [ ] **AC-7** — Practical notebook: ARI against known classes and DTW-silhouette K selection
- [ ] **AC-8** — Practical notebook: runtime scaling comparison
- [ ] **AC-9** — Practical notebook: feature-based clustering alternative compared
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors)
- [ ] **AC-11** — Cross-lesson link: k-medoids/K-Means (lesson 1) and silhouette (lesson 0b) reused under a new metric

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL22
- Directive: DIRECT-UL21
- Tasks: TASK-UL066, TASK-UL067, TASK-UL068
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
