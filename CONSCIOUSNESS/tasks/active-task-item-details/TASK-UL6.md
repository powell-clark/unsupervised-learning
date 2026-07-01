# TASK-UL6: Hierarchical Clustering Practical (2b)

## Context
Second notebook of Lesson 2 (STORY-UL3). Applies hierarchical clustering to real data: gene expression clustering, document similarity, and customer segmentation. Demonstrates cutting dendrograms at different heights to obtain K clusters, comparing results across linkage methods, and interpreting cluster trees.

## Acceptance Criteria
- [x] Full scikit-learn AgglomerativeClustering usage (linkage, distance metric, n_clusters)
- [x] Real case study: clustering real dataset (iris, real gene expression, or similar)
- [x] Cutting dendrograms programmatically at different heights
- [x] Dendrogram visualization and interpretation
- [x] Comparing dendrograms: single vs. complete vs. average vs. ward linkage
- [x] Silhouette and Davies-Bouldin evaluation of hierarchical results
- [x] Pros/cons of hierarchical vs. K-Means in practice
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
Builds on TASK-UL5 theory. Show scipy.cluster.hierarchy.fcluster for cutting. Benchmark scalability (hierarchical is slower than K-Means). Compare cluster interpretability: dendrograms vs. centroids.

## Dependencies
- Blocked by: TASK-UL5
- Blocks: STORY-UL3 (Hierarchical Clustering completion)
