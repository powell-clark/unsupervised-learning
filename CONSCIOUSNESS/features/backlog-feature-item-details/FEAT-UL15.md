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

## Review (TASK-UL047, 2026-09-05)

Independent agent review (Sonnet, fresh context, judging raw notebook JSON cell-by-cell
rather than section headers) returned **agent-rejected**: 10 of 11 criteria met with cited
cell evidence, **AC-11 NOT MET** — it requires an explicit contrast with both lesson 1
(K-Means) and lesson 3 (DBSCAN) on non-convex clusters, and a grep for "dbscan" / "lesson 3"
returned zero hits in either notebook. K-Means was contrasted throughout; DBSCAN was absent.

The reviewer additionally cleared two things on independent scrutiny: the sigma=0.02 /
13-components case in 17a is correctly explained rather than self-contradictory, and the
RatioCut relaxation derivation matches von Luxburg's standard argument with no maths errors.

**Gap closed, awaiting re-review.** 17a now carries a dedicated "The Other Non-Convex Method:
Spectral vs DBSCAN" section — a comparison table (what a cluster is, what you must supply,
noise labelling, behaviour under unequal density, cost) plus a three-dataset three-algorithm
cell. Measured: moons and circles give DBSCAN and spectral ARI 1.000 each against K-Means
0.247 / -0.003, so non-convexity alone does not choose between them; a purpose-built
unequal-density pair drops DBSCAN to 0.889 with 16.0% of points marked noise while spectral
holds 1.000. That is the discriminating case, and it makes the choice rule concrete: supply k
(spectral) or a single density scale (DBSCAN), and note only DBSCAN labels outliers.

17a re-executed: 9/9 code cells, zero errors, 7 figures.

**This feature is NOT closed.** The fix was authored by the same session that built the
notebooks, so it has not been independently verified. TASK-UL047 remains open for a fresh
reviewer to re-run the procedure against AC-11 and close on approval.
