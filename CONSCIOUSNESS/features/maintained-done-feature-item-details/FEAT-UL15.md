# FEAT-UL15: Spectral Clustering and Graph Laplacians Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p2

## Description
Lesson 17 of Unsupervised Learning Part II. Delivers a spectral clustering lesson on similarity graphs and graph Laplacians; the learner can cluster data whose structure is connectivity, not compactness. Notebooks: 17a_spectral_clustering_theory.ipynb, 17b_spectral_clustering_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: similarity graph construction (epsilon, kNN, RBF) with a connectivity comparison (REVIEW-UL061)
- [x] **AC-2** — Theory notebook: the three Laplacians defined and their PSD / zero-eigenvalue properties demonstrated numerically (REVIEW-UL061)
- [x] **AC-3** — Theory notebook: RatioCut/NCut relaxation argument explaining why the eigenvectors are the embedding (REVIEW-UL061; RatioCut derivation independently checked against von Luxburg's tutorial)
- [x] **AC-4** — Theory notebook: eigengap heuristic for K with a plot (REVIEW-UL061)
- [x] **AC-5** — Theory notebook: from-scratch NumPy spectral clustering recovering two-moons and concentric circles where K-Means fails (REVIEW-UL061; re-confirmed intact after the AC-11 insertion by REVIEW-UL063 — cell 15, scratch-vs-sklearn ARI 1.000 on moons/circles/blobs)
- [x] **AC-6** — Practical notebook: sklearn SpectralClustering with affinity and parameter sweeps (REVIEW-UL061)
- [x] **AC-7** — Practical notebook: image segmentation case study compared against K-Means segmentation (REVIEW-UL061)
- [x] **AC-8** — Practical notebook: community detection on a graph, spectral vs Louvain, scored by modularity (REVIEW-UL061)
- [x] **AC-9** — Practical notebook: scalability discussion — dense vs sparse affinities with timings (REVIEW-UL061)
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, every code cell executed, zero errors) (REVIEW-UL061; re-confirmed after the AC-11 insertion by REVIEW-UL063 — 17a 9/9 cells sequential execution counts zero errors, 17b untouched and still 6/6 clean)
- [x] **AC-11** — Cross-lesson link: explicit contrast with lesson 1 (K-Means) and lesson 3 (DBSCAN) on non-convex clusters (REVIEW-UL063 — cell 16 markdown frames the K-Means/DBSCAN contrast, cell 17 code exec_count=8 imports and runs sklearn DBSCAN on moons/circles/an unequal-density pair; printed ARI 0.247/1.000/1.000, -0.003/1.000/1.000, 0.960/0.889/1.000 with 16.0% DBSCAN noise, matching the prose exactly)

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL15
- Directive: DIRECT-UL14
- Tasks: TASK-UL045, TASK-UL046, TASK-UL047, TASK-UL081
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md

## Review history

- **REVIEW-UL061** (TASK-UL047, 2026-09-05, agent-rejected): independent Sonnet review, judging
  raw notebook JSON cell-by-cell rather than section headers, returned 10 of 11 criteria met
  with cited cell evidence; **AC-11 NOT MET** — it requires an explicit contrast with both
  lesson 1 (K-Means) and lesson 3 (DBSCAN) on non-convex clusters, and DBSCAN appeared nowhere
  in either notebook. The reviewer also independently cleared the sigma=0.02/13-components
  case in 17a as correctly explained, and checked the RatioCut relaxation against von
  Luxburg's standard derivation with no maths errors found.
- **Fix (commit fbee6c5):** 17a gained "The Other Non-Convex Method: Spectral vs DBSCAN" — a
  comparison table plus a three-dataset three-algorithm cell measuring K-Means/DBSCAN/spectral
  against each other. Not self-approved, since the session that authored the fix also
  authored the notebooks — TASK-UL081 was filed to carry an independent re-review.
- **REVIEW-UL063** (TASK-UL081, 2026-09-05, agent-approved): independent fresh-context
  re-review confirmed AC-11 met — DBSCAN is genuinely imported and run (not merely described),
  the printed numbers match the prose exactly with no overstatement (both prior reviews of
  this lesson had found a prose-versus-output contradiction elsewhere in the corpus, so this
  check was load-bearing) — and confirmed the insertion broke nothing: AC-5 and AC-10 both
  re-verified intact.

**Maintained 2026-09-05.**
