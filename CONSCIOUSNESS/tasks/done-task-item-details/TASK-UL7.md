# TASK-UL7: DBSCAN Theory (3a)

## Context
First notebook of Lesson 3 (STORY-UL4). Introduces density-based clustering as alternative to distance-based (K-Means) and hierarchical. DBSCAN finds arbitrary cluster shapes, handles noise, and requires no K specification upfront.

## Acceptance Criteria
- [ ] Core vs border vs noise points: epsilon and minpts definitions
- [ ] Density-reachability and density-connectivity
- [ ] From-scratch DBSCAN implementation
- [ ] Cross-check against scikit-learn
- [ ] Epsilon and minpts parameter effects
- [ ] Visualization: clusters, noise, core/border points
- [ ] Comparison with K-Means and Hierarchical on non-convex data
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Builds on distance metrics (Lesson 0A). Show how DBSCAN discovers arbitrary shapes K-Means/Hierarchical miss. Introduce epsilon-neighborhood concept. Discuss parameter selection challenges.

## Dependencies
- Blocked by: TASK-UL2
- Blocks: TASK-UL8 (DBSCAN practical), STORY-UL4
