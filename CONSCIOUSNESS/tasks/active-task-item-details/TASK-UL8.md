# TASK-UL8: DBSCAN Practical (3b)

## Context
Second notebook of Lesson 3 (STORY-UL4). Applies DBSCAN to real data with focus on parameter selection. Introduces HDBSCAN (hierarchical DBSCAN) as parameter-robust alternative. Benchmarks against K-Means and Hierarchical.

## Acceptance Criteria
- [ ] Full scikit-learn DBSCAN usage (eps, min_samples)
- [ ] K-distance graphs for epsilon selection
- [ ] Real case study: clustering real dataset
- [ ] Outlier handling and noise point analysis
- [ ] HDBSCAN introduction: adaptive clustering
- [ ] DBSCAN vs K-Means vs Hierarchical comparison
- [ ] Scalability and computational complexity
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Builds on TASK-UL7. Show k-distance plot method for choosing ε. Demonstrate HDBSCAN's robustness to parameter choices. Compare results and performance on real data.

## Dependencies
- Blocked by: TASK-UL7
- Blocks: STORY-UL4 (DBSCAN completion)
