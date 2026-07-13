# TASK-UL27: Clustering Comparison Framework (13)

## Context
First notebook of Lesson 13 (STORY-UL14, DIRECT-UL13, FEAT-UL13). Synthesizes K-Means,
Hierarchical, DBSCAN, and GMM (Lessons 1-4) into a practical decision framework: speed,
scalability, assumptions, hyperparameter sensitivity, and a decision guide for which
algorithm fits which problem shape.

## Acceptance Criteria
- [x] Comparison matrix: K-Means, Hierarchical, DBSCAN, GMM across assumptions, scalability, hyperparameter sensitivity, cluster shape handling
- [x] Empirical speed/scalability benchmark across dataset sizes for all four algorithms
- [x] Empirical comparison on multiple synthetic dataset shapes (blobs, moons, circles, varying density) with quality metrics — circles substituted for elongated clusters, an equally standard centroid-defeating shape
- [x] Decision guide: which algorithm to reach for given problem characteristics (shape, noise, K known/unknown, scale)
- [x] Hyperparameter sensitivity demonstration for at least two algorithms
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
Not a new algorithm — a synthesis lesson bringing together Lessons 1-4. Benchmarks should be
genuinely run (not asserted from memory) since the whole point is evidence-based selection
guidance. Use the same evaluation metrics from Lesson 0b (silhouette, ARI where ground truth
exists) to make comparisons concrete rather than qualitative-only.

## Dependencies
- Blocked by: TASK-UL2, TASK-UL4, TASK-UL6, TASK-UL8, TASK-UL10 (clustering algorithms and evaluation)
- Blocks: none
- Story: STORY-UL14 (Professional-practice learner story)
- Directive: DIRECT-UL13 (Professional Practice)
- Feature: FEAT-UL13 (Professional Practice Lesson), FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
