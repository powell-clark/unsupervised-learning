# DIRECT-UL3: Hierarchical Clustering

## Context

Hierarchical clustering reveals nested structure in data without fixing the cluster count upfront. TASK-UL5 covers linkage methods (single, complete, average, Ward) and dendrogram interpretation. TASK-UL6 applies scikit-learn and explores cutting strategies.

## Acceptance Criteria

- [ ] TASK-UL5 (0a theory) complete — linkage methods, dendrogram construction
- [ ] TASK-UL6 (0b practical) complete — scikit-learn, cutting dendrograms, comparison of linkages
- [ ] Both notebooks run in Colab
- [ ] From-scratch agglomerative clustering implementation verified
- [ ] FEAT-UL1 and FEAT-UL2 satisfied

## Technical Notes

Topics: agglomerative vs divisive, linkage criteria, distance matrices, dendrograms, cutting strategies. Implementation: numpy distance matrix + greedy merging, then scikit-learn.

## Dependencies

- Blocked by: DIRECT-UL1 (Clustering Foundations)
- Blocks: DIRECT-UL13 (Professional Practice)
