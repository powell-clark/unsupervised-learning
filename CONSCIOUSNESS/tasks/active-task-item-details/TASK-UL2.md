# TASK-UL2: Cluster evaluation (0b)

## Context
Second notebook of Lesson 0 (STORY-UL1). Teaches how to evaluate clusters when
there are no ground-truth labels — the single most important skill for trusting
unsupervised results.

## Acceptance Criteria
- [ ] Internal metrics: silhouette, Davies-Bouldin, Calinski-Harabasz (from scratch + sklearn)
- [ ] External metrics: Adjusted Rand Index, Normalized Mutual Information
- [ ] Choosing K: elbow method and gap statistic
- [ ] Visual evaluation techniques
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Builds on TASK-UL1's distance metrics. Cross-check from-scratch metric
implementations against scikit-learn.

## Dependencies
- Blocked by: TASK-UL1
- Blocks: STORY-UL2 (K-Means)
