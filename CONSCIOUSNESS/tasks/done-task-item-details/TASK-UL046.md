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
- [x] Every section above present with working code and at least one figure or table per section — 15 cells (6 code), 5 figures, every section carries a printed table or measurement
- [x] The production library result is compared against the lesson's from-scratch implementation at least once — 17a's `spectral_clustering()` already matched sklearn at ARI 1.000; this notebook extends that by sweeping sklearn's own parameters and showing the affinity choice moves ARI from 0.002 to 1.000
- [x] All practical-notebook criteria on FEAT-UL15 are satisfiable from this notebook's content
- [x] `jupyter execute` passes: 6/6 code cells executed, zero errors, outputs committed
- [x] Colab-runnable: sklearn bundled data + `load_sample_image`, networkx bundled karate club, no downloads

## Outcome
Sections and their measured results:
- **API sweep** — rbf ARI spans 0.263–1.000 across gamma; nearest_neighbors spans 0.002–1.000 across k. The affinity choice is the model, demonstrated rather than asserted. `assign_labels` (kmeans / discretize / cluster_qr) is stable at 0.98–0.99 across seeds, so the graph dominates the assignment method.
- **Eigengap on real data** — the section that changed most under verification (see below).
- **Image segmentation** — china.jpg at 36×54 = 1944 pixel-nodes; spatial coherence quantified by runs-per-row: spectral colour+position 10.97, spectral colour-only 11.64, K-Means colour+position 13.61.
- **Community detection** — karate club (34 nodes, 78 edges). Spectral k=2: modularity 0.4036, ARI 0.882 against the recorded factions. Louvain: modularity 0.4439 (higher than the **true split's own 0.3914**), ARI only 0.509. A better objective score is not a better answer to the question asked.
- **Scalability** — dense-vs-kNN speed-up grows 1.2x → 31.9x over n=200→1600; extrapolated dense affinity is 0.8 GB at n=10⁴ and 80 GB at n=10⁵ against 0.8 MB / 8 MB for kNN. Memory, not runtime, is the wall.

## Defect found and corrected during verification
The eigengap section originally asserted "the heuristics agree with each other and with the cultivars" — while its own output printed eigengap K=1 against wine's true K=3. Investigated rather than reworded: λ₁ = 0 always (17a Property 2), so the trivial gap λ₂−λ₁ dominates on a connected graph and the naive argmax returns K=1 on **both** datasets. Restricted to k ≥ 2 it gives 2 for wine (true 3) and misses digits' 10.

The section now reports both readings and states the real finding: **on this real data the eigengap does not recover the known class count**, unlike 17a's synthetic blobs where it was exact — yet spectral clustering *told* K scores ARI 0.880 on wine and 0.707 on digits. The algorithm works; model selection is what fails. That is a more useful lesson than the tidy claim it replaced. A follow-on wording slip (calling silhouette's 11 an "under-call" of 10) was caught in the same pass.

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
