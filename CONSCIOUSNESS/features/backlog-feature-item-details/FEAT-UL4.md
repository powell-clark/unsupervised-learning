# FEAT-UL4: Density-Based Clustering Lesson (DBSCAN/HDBSCAN)

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Comprehensive lesson on density-based clustering: DBSCAN foundations, epsilon and min_samples selection, noise handling, and hierarchical DBSCAN. Covers theory of density-reachability alongside practical parameter optimization and HDBSCAN robustness.

## Acceptance Criteria
- [ ] Theory notebook: Density-reachability and core/border/noise point definitions
- [ ] Theory notebook: DBSCAN algorithm derivation and complexity analysis
- [ ] Theory notebook: Why DBSCAN handles arbitrary shapes (unlike K-Means)
- [ ] Practical notebook: K-distance graph method for epsilon selection
- [ ] Practical notebook: scikit-learn DBSCAN implementation with parameter tuning
- [ ] Practical notebook: Noise point analysis and outlier handling
- [ ] Practical notebook: HDBSCAN introduction (hierarchy, stability, adaptive)
- [ ] Practical notebook: Real case study with non-convex clusters
- [ ] Practical notebook: DBSCAN vs K-Means vs Hierarchical comparison
- [ ] Both notebooks run end-to-end in Google Colab
- [ ] Scalability notes (eps parameter affects complexity)
- [ ] Completed task pair: TASK-UL7 (theory) and TASK-UL8 (practical)

## Linked Entities
- Story: STORY-UL4 (DBSCAN learner story)
- Directive: DIRECT-UL4 (Density-Based Clustering)
- Tasks: TASK-UL7, TASK-UL8
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
