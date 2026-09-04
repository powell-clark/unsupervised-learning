# TASK-UL5: Hierarchical Clustering Theory (2a)

## Context
First notebook of Lesson 2 (STORY-UL3). Introduces hierarchical agglomerative clustering, linkage methods, and dendrograms. Unlike K-Means (which requires K upfront), hierarchical clustering reveals nested cluster structure without fixing the number of clusters in advance.

## Acceptance Criteria
- [x] Agglomerative vs. divisive clustering paradigms
- [x] Distance metrics between clusters: single, complete, average, ward linkage
- [x] Dendrogram interpretation and visualization
- [x] From-scratch hierarchical clustering (linkage matrix computation)
- [x] Cross-check against scikit-learn AgglomerativeClustering
- [x] Dendrograms with real data (Iris, synthetic blobs)
- [x] Comparing dendrograms from different linkage methods
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
Builds on TASK-UL2's distance metrics. Show how dendrograms reveal structure differently than K-Means. Introduce scipy.cluster.hierarchy for dendrogram computation and visualization.

## Dependencies
- Blocked by: TASK-UL2
- Blocks: TASK-UL6 (Hierarchical practical), STORY-UL3 (Hierarchical Clustering)
