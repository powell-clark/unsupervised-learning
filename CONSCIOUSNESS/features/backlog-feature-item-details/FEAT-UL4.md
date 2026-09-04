# FEAT-UL4: Density-Based Clustering Lesson (DBSCAN/HDBSCAN)

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Comprehensive lesson on density-based clustering: DBSCAN foundations, epsilon and min_samples selection, noise handling, and hierarchical DBSCAN. Covers theory of density-reachability alongside practical parameter optimization and HDBSCAN robustness.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: Density-reachability and core/border/noise point definitions
- [ ] **AC-2** — Theory notebook: DBSCAN algorithm derivation and complexity analysis
- [ ] **AC-3** — Theory notebook: Why DBSCAN handles arbitrary shapes (unlike K-Means)
- [ ] **AC-4** — Practical notebook: K-distance graph method for epsilon selection
- [ ] **AC-5** — Practical notebook: scikit-learn DBSCAN implementation with parameter tuning
- [ ] **AC-6** — Practical notebook: Noise point analysis and outlier handling
- [ ] **AC-7** — Practical notebook: HDBSCAN introduction (hierarchy, stability, adaptive)
- [ ] **AC-8** — Practical notebook: Real case study with non-convex clusters
- [ ] **AC-9** — Practical notebook: DBSCAN vs K-Means vs Hierarchical comparison
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab
- [ ] **AC-11** — Scalability notes (eps parameter affects complexity)
- [ ] **AC-12** — Completed task pair: TASK-UL7 (theory) and TASK-UL8 (practical)

## Linked Entities
- Story: STORY-UL4 (DBSCAN learner story)
- Directive: DIRECT-UL4 (Density-Based Clustering)
- Tasks: TASK-UL7, TASK-UL8
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
