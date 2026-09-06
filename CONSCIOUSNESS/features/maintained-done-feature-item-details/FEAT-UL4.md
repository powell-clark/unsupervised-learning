# FEAT-UL4: Density-Based Clustering Lesson (DBSCAN/HDBSCAN)

**Status:** maintained | **Kano:** performance | **Priority:** p2

## Description
Comprehensive lesson on density-based clustering: DBSCAN foundations, epsilon and min_samples selection, noise handling, and hierarchical DBSCAN. Covers theory of density-reachability alongside practical parameter optimization and HDBSCAN robustness.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: Density-reachability and core/border/noise point definitions
- [x] **AC-2** — Theory notebook: DBSCAN algorithm derivation and complexity analysis
- [x] **AC-3** — Theory notebook: Why DBSCAN handles arbitrary shapes (unlike K-Means)
- [x] **AC-4** — Practical notebook: K-distance graph method for epsilon selection
- [x] **AC-5** — Practical notebook: scikit-learn DBSCAN implementation with parameter tuning
- [x] **AC-6** — Practical notebook: Noise point analysis and outlier handling
- [x] **AC-7** — Practical notebook: HDBSCAN introduction (hierarchy, stability, adaptive)
- [x] **AC-8** — Practical notebook: Real case study with non-convex clusters
- [x] **AC-9** — Practical notebook: DBSCAN vs K-Means vs Hierarchical comparison
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab — verified via jupyter execute under TASK-UL040, 6/6 and 5/5 cells, zero errors
- [x] **AC-11** — Scalability notes (eps parameter affects complexity)
- [x] **AC-12** — Completed task pair: TASK-UL7 (theory) and TASK-UL8 (practical)

## Review (TASK-UL041)
Independent agent review against notebooks/3a_dbscan_theory.ipynb and
3b_dbscan_practical.ipynb: all 12 criteria verified via section headers
plus keyword search (noise-point handling and scalability language both
confirmed present in-text). agent-approved — stays in backlog pending
human sign-off per the FEAT-UL14 precedent (live tooling requires it).

## Linked Entities
- Story: STORY-UL4 (DBSCAN learner story)
- Directive: DIRECT-UL4 (Density-Based Clustering)
- Tasks: TASK-UL7, TASK-UL8
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)

## Human sign-off
Operator ruling in chat 2026-09-06 14:48, relayed by the kernel (MSG-EGLPK006): signed off. The FEAT-UL14 precedent (agent-approved features held pending explicit human sign-off before promotion to maintained) is lifted for this card by that ruling. Human verdict recorded in REVIEW-INDEX.md (reviewer_type=human, reviewer_id=operator, verdict=human-approved).
