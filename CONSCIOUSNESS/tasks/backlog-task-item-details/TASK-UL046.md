# TASK-UL046: Lesson 17b practical: Spectral Clustering and Graph Laplacians

## Context
Part II, lesson 17, practical notebook `notebooks/17b_spectral_clustering_practical.ipynb`. Builds on `17a_spectral_clustering_theory.ipynb` (TASK-UL045) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL15.

## Notebook plan (sections, in order)
1. sklearn.cluster.SpectralClustering: affinity="nearest_neighbors" vs "rbf", gamma/n_neighbors sweeps, assign_labels="kmeans" vs "discretize"
2. The eigengap plot from the affinity matrix (sklearn.metrics.pairwise + np.linalg.eigh) used to pick K on a real dataset (load_digits or load_wine)
3. Image segmentation: sklearn.datasets.load_sample_image("china.jpg") downsampled, spectral clustering on pixel colour+position features, compared with K-Means segmentation from lesson 1b
4. Community detection on networkx.karate_club_graph(): spectral partition vs networkx.community.louvain_communities, both scored with modularity
5. Scalability: timing vs n for the dense RBF affinity, and why nearest-neighbour affinities (sparse) matter

**Library:** scikit-learn SpectralClustering, networkx (already in requirements)
**Data:** sklearn bundled datasets and sample image; networkx bundled karate club graph — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL15 are satisfiable from this notebook's content
- [ ] `jupyter execute` passes: every code cell executed, zero errors, outputs committed
- [ ] Colab-runnable: no network downloads (a bundled/cached dataset or an in-notebook generator only)

## Build rules (house pattern — read two Part I notebooks first, e.g. 5a/5b or 12a/12b)
- Open with a story-driven motivation, then a Table of Contents with anchor links, then a Required Libraries cell.
- Derivations in markdown with LaTeX; every claim that can be checked numerically is checked in a code cell.
- From-scratch implementation first, production library second, and one cell that shows the two agree (or explains why they differ).
- No network downloads: only sklearn/networkx bundled data, in-notebook generators, or the cached MNIST under notebooks/data. If a step would download, replace it with a generator and say so in a markdown cell.
- Keep any training cell under ~3 minutes on CPU; bound epochs and sample sizes accordingly.
- Reuse earlier-lesson code patterns rather than re-inventing (reference the lesson by number in markdown).
- Finish with a Conclusion: key takeaways, practical guidance, what was NOT covered and why (honesty section), next steps.
- Execute in place before committing: `jupyter execute notebooks/<nb> --output /tmp/<nb>`, confirm every code cell ran with zero errors, copy back over the committed file. Commit with the task id in the subject.

## Execution
- Builder model: the session model (sonnet is sufficient)
- Expected duration: 2h

## Dependencies
- Blocked by: TASK-UL045
- Blocks: the lesson-17 verification task
