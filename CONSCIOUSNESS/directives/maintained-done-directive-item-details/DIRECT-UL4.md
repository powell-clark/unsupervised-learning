# DIRECT-UL4: Density-Based Clustering (DBSCAN/HDBSCAN)

## Context

DBSCAN finds arbitrarily shaped clusters and identifies noise points, unlike K-Means which assumes spherical clusters. TASK-UL7 derives the density-reachability concept and core/border/noise point classification. TASK-UL8 applies scikit-learn DBSCAN and the more robust HDBSCAN variant.

## Acceptance Criteria

- [ ] TASK-UL7 (0a theory) complete — density reachability, core points, border points, noise points
- [ ] TASK-UL8 (0b practical) complete — DBSCAN, HDBSCAN, parameter selection (eps, min_samples)
- [ ] Both notebooks run in Colab
- [ ] From-scratch DBSCAN implementation verified
- [ ] FEAT-UL1 and FEAT-UL2 satisfied

## Technical Notes

Topics: epsilon-neighborhoods, core points, density-connected clusters, parameter sensitivity, handling noise. Extensions: HDBSCAN for adaptive clustering. Implementation: KD-tree neighbor search, greedy cluster expansion.

## Dependencies

- Blocked by: DIRECT-UL1 (Clustering Foundations)
- Blocks: DIRECT-UL13 (Professional Practice)
