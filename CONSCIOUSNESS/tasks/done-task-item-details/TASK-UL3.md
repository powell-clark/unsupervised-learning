# TASK-UL3: K-Means Theory (1a)

## Context
First notebook of Lesson 1 (STORY-UL2). Derives K-Means from first principles, building Lloyd's algorithm step-by-step from the distance minimization problem, then introduces K-Means++ initialization to avoid poor local optima.

## Acceptance Criteria
- [x] Lloyd's algorithm derivation: objective function, EM-style convergence
- [x] From-scratch K-Means implementation (using only NumPy)
- [x] Cross-check against scikit-learn implementation
- [x] K-Means++ initialization algorithm and motivation
- [x] Seed-based comparison: random vs. K-Means++ on test data
- [x] Visual demonstration: cluster assignments, centroids, convergence history
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
Builds on TASK-UL2's distance metrics and cluster evaluation. Introduce convergence criterion (inertia plateau) and discuss local optima sensitivity. Show how K-Means++ reduces chance of poor initialization.

## Dependencies
- Blocked by: TASK-UL2
- Blocks: TASK-UL4 (K-Means practical), STORY-UL2 (K-Means Clustering)
