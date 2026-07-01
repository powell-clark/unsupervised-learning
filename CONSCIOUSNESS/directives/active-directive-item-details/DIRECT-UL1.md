# DIRECT-UL1: Clustering Foundations

## Context

Lesson 0 is the entry point to unsupervised learning. It establishes the mathematical and conceptual groundwork every clustering algorithm depends on: what is unsupervised learning, how do we measure distance between points, why does distance become meaningless in high dimensions, and how can we evaluate clusters without ground-truth labels?

TASK-UL1 covers theory (unsupervised vs supervised, distance metrics, curse of dimensionality, Iris visualization). TASK-UL2 covers evaluation (silhouette, Davies-Bouldin, Calinski-Harabasz, elbow method, gap statistic).

## Acceptance Criteria

- [x] TASK-UL1 (0a theory) complete — notebook shipped and runs in Colab
- [ ] TASK-UL2 (0b evaluation) complete — notebook shipped and runs in Colab
- [ ] Both use from-scratch NumPy implementations verified against scikit-learn
- [ ] FEAT-UL1 (Colab compatibility) satisfied
- [ ] FEAT-UL2 (dual implementation) satisfied
- [ ] DIRECT-UL2 (K-Means Clustering) unblocked

## Technical Notes

Dataset: Iris (unlabeled). Libraries: NumPy, Matplotlib, Pandas, SciPy, scikit-learn. Story-driven pedagogy: introduce the problem, derive the solution, implement from scratch, validate with production libraries.

## Dependencies

- Blocked by: none
- Blocks: DIRECT-UL2 (K-Means), DIRECT-UL3 (Hierarchical), DIRECT-UL4 (DBSCAN), all downstream clustering directives
