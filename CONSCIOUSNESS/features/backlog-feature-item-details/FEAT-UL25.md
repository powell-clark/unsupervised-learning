# FEAT-UL25: Clustering Stability, Consensus and Choosing K Honestly Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 27 of Unsupervised Learning Part II. Delivers a clustering-stability lesson; the learner can report how confident a clustering is instead of a single K chosen by one heuristic. Notebooks: 27a_clustering_stability_theory.ipynb, 27b_clustering_stability_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: why indices disagree, recapped with evidence from earlier lessons
- [ ] **AC-2** — Theory notebook: gap statistic derived and implemented with the one-SE rule
- [ ] **AC-3** — Theory notebook: resampling stability curve from scratch
- [ ] **AC-4** — Theory notebook: prediction strength implemented
- [ ] **AC-5** — Theory notebook: consensus matrices and consensus CDF from scratch
- [ ] **AC-6** — Practical notebook: multi-algorithm consensus ensemble with co-association heatmaps
- [ ] **AC-7** — Practical notebook: K chosen by four criteria on one figure per dataset
- [ ] **AC-8** — Practical notebook: per-point uncertainty flagged and inspected
- [ ] **AC-9** — Practical notebook: a reporting template and resample-budget analysis
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors)
- [ ] **AC-11** — Cross-lesson link: reuses lesson 0b metrics, lesson 1b elbow, lesson 4b BIC, lesson 17 spectral

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL25
- Directive: DIRECT-UL24
- Tasks: TASK-UL075, TASK-UL076, TASK-UL077
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
