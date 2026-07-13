# FEAT-UL14: K-Means Clustering Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Comprehensive lesson on K-Means clustering: Lloyd's algorithm from first principles, K-Means++ initialization, elbow method, and silhouette analysis. Covers theory notebook deriving the algorithm alongside practical scikit-learn implementation with real data segmentation.

Renumbered from FEAT-UL2 (TASK-UL034) to resolve an ID collision with the
active cross-cutting FEAT-UL2 (dual NumPy/production implementation). An
independent agent review commissioned by TASK-UL034 found this feature's
closure claim (TASK-UL3, TASK-UL4) does not hold: 3 of 11 criteria are
unmet in the shipped notebooks, and neither notebook carries any execution
evidence (`execution_count: null` on every cell) — see TASK-UL040 for the
curriculum-wide finding and fix. Left in backlog, not moved to maintained,
pending that fix.

## Acceptance Criteria
- [x] Theory notebook: Lloyd's algorithm derivation (vector form, convergence proof)
- [x] Theory notebook: K-Means++ initialization (why it matters, implementation)
- [ ] Theory notebook: soft K-Means and probabilistic interpretation — absent; only a forward-pointer to the future GMM lesson
- [x] Practical notebook: scikit-learn KMeans usage and fit patterns
- [ ] Practical notebook: Elbow method for choosing K — 1b covers silhouette/Davies-Bouldin/Calinski-Harabasz vs K, never an inertia/WCSS elbow plot; "elbow" appears only in prose
- [x] Practical notebook: Silhouette analysis for cluster validation
- [x] Practical notebook: Real data segmentation case study (e.g., customer clustering)
- [ ] Both notebooks run end-to-end in Google Colab without local setup — unverified; zero execution evidence in either committed file, tracked as TASK-UL040
- [x] Theory notebook includes NumPy-only derivation
- [ ] Practical notebook contrasts multiple initializations and their impact — that comparison exists in the theory notebook (1a), not the practical one this criterion names
- [x] Completed task pair: TASK-UL3 (theory) and TASK-UL4 (practical) — both closed in TASK-DONE-INDEX, but see above: closure was not itself verified against these criteria at the time

## Linked Entities
- Story: STORY-UL2 (K-Means learner story)
- Directive: DIRECT-UL2 (K-Means Clustering)
- Tasks: TASK-UL3, TASK-UL4
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
