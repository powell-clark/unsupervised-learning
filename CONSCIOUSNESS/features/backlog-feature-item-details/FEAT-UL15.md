# FEAT-UL15: Spectral Clustering and Graph Laplacians Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Lesson 17 of Unsupervised Learning Part II. Delivers a spectral clustering lesson on similarity graphs and graph Laplacians; the learner can cluster data whose structure is connectivity, not compactness. Notebooks: 17a_spectral_clustering_theory.ipynb, 17b_spectral_clustering_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: similarity graph construction (epsilon, kNN, RBF) with a connectivity comparison
- [ ] **AC-2** — Theory notebook: the three Laplacians defined and their PSD / zero-eigenvalue properties demonstrated numerically
- [ ] **AC-3** — Theory notebook: RatioCut/NCut relaxation argument explaining why the eigenvectors are the embedding
- [ ] **AC-4** — Theory notebook: eigengap heuristic for K with a plot
- [ ] **AC-5** — Theory notebook: from-scratch NumPy spectral clustering recovering two-moons and concentric circles where K-Means fails
- [ ] **AC-6** — Practical notebook: sklearn SpectralClustering with affinity and parameter sweeps
- [ ] **AC-7** — Practical notebook: image segmentation case study compared against K-Means segmentation
- [ ] **AC-8** — Practical notebook: community detection on a graph, spectral vs Louvain, scored by modularity
- [ ] **AC-9** — Practical notebook: scalability discussion — dense vs sparse affinities with timings
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, every code cell executed, zero errors)
- [ ] **AC-11** — Cross-lesson link: explicit contrast with lesson 1 (K-Means) and lesson 3 (DBSCAN) on non-convex clusters

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL15
- Directive: DIRECT-UL14
- Tasks: TASK-UL045, TASK-UL046, TASK-UL047
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
