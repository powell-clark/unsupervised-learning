# FEAT-UL25: Clustering Stability, Consensus and Choosing K Honestly Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 27 of Unsupervised Learning Part II. Delivers a clustering-stability lesson; the learner can report how confident a clustering is instead of a single K chosen by one heuristic. Notebooks: 27a_clustering_stability_theory.ipynb, 27b_clustering_stability_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
All eleven verified by REVIEW-UL106 -- an independent fresh-context opus review that read raw `.ipynb` JSON cell-by-cell for both notebooks, independently re-executed both from clean copies, and independently re-derived every mathematically load-bearing claim (the gap one-SE rule, the consensus-CDF area via a closed-form check, the prediction-strength train/test logic, the `pick_key`/tie-selection logic by hand). It found 18 findings (2 HIGH must-fix, 7 medium, 9 low) -- all fixed and re-verified before this closure, including a geometrically false stability-tie explanation and a singleton-cluster logic inversion in the per-point uncertainty flag.

- [x] **AC-1** — Theory notebook: why indices disagree, recapped with evidence from earlier lessons -- 27a cell 4 names Lessons 0B (silhouette/DB/CH), 1B (elbow) and 4B (BIC); cell 5 measures all three on two synthetic datasets and derives agreement/disagreement dynamically (well-separated: all three agree at K=4; overlapping: BIC picks 2, the others pick 4)
- [x] **AC-2** — Theory notebook: gap statistic derived and implemented with the one-SE rule -- 27a cell 7, PCA-aligned uniform reference, validated against a known true K=4; the one-SE rule is genuinely load-bearing (differs from bare argmax)
- [x] **AC-3** — Theory notebook: resampling stability curve from scratch -- 27a cell 9, mean pairwise ARI on shared points across subsample pairs, with an explicit tie check (TOL_STAB=0.02); independently confirmed and corrected during review that K=2's apparent perfect stability on well-separated blobs is a subsample-overlap artefact (falls from 1.000 to 0.476 as overlap drops 80%->20%), not a genuine structural coarsening -- the notebook now demonstrates and explains this directly
- [x] **AC-4** — Theory notebook: prediction strength implemented -- 27a cell 11, train/test split, nearest-training-centroid assignment, minimum co-assignment fraction over test clusters (Tibshirani & Walther 2005); recovers true K=4 on both synthetic datasets, and independently confirms the K=2 stability artefact above (strength near 0.5 at K=2, a coin flip)
- [x] **AC-5** — Theory notebook: consensus matrices and consensus CDF from scratch -- 27a cell 13, co-association matrix + consensus-CDF area; independently re-derived via the closed form (area = 1 - mean(M) for a [0,1]-supported variable), matching to 4 decimal places at every K (2: 0.5017 ... 6: 0.8143), flattening detection picks K=4
- [x] **AC-6** — Practical notebook: multi-algorithm consensus ensemble with co-association heatmaps -- 27b cell 5, K-Means/GMM/Spectral(Lesson 17)/HDBSCAN rotated across resamples on Wine and a Digits subsample; HDBSCAN's noise label correctly excluded from both numerator and denominator (independently verified), and its noise fraction now disclosed explicitly (Wine 38.5%, Digits 62.6%)
- [x] **AC-7** — Practical notebook: K chosen by four criteria on one figure per dataset -- 27b cell 7, silhouette/BIC/gap/stability on one 4-panel figure per dataset; picks now tie-aware (e.g. Wine silhouette correctly reports a [2,3] tie rather than a flat, overconfident single K)
- [x] **AC-8** — Practical notebook: per-point uncertainty flagged and inspected -- 27b cell 9, own-cluster co-association confidence flagged and plotted on both real datasets; a singleton-cluster logic inversion (max confidence for the least-confident points) found and fixed during review
- [x] **AC-9** — Practical notebook: a reporting template and resample-budget analysis -- 27b cells 11/13; the reporting template ties every number to one write-up (Wine worked example), and the resample-budget sweep finds its convergence point dynamically with an honest knife-edge-margin caveat added during review
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors) -- 27a 7/7, 27b 6/6 code cells, zero errors, independently re-executed by the reviewer and by this session from clean copies; no network calls (verified by grep of every cell)
- [x] **AC-11** — Cross-lesson link: reuses lesson 0b metrics, lesson 1b elbow, lesson 4b BIC, lesson 17 spectral -- independently verified against the actual earlier notebooks: 4B's `GaussianMixture.bic()` is the same sklearn tool (not a look-alike; an inline comment records a hand-rolled attempt that was tried and rejected); 17B's exact `SpectralClustering(affinity='nearest_neighbors', n_neighbors=10)` parameterisation is a genuine rotating ensemble member; 0B's silhouette/ARI are used directly; 1B's elbow-on-inertia pattern is reused in 27a's own disagreement demo

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Review history
- REVIEW-UL106 -- agent-approved, iteration 1 (11 of 11 AC met; 18 findings, 2 HIGH, all fixed and re-verified before closure)

## Linked Entities
- Story: STORY-UL25
- Directive: DIRECT-UL24
- Tasks: TASK-UL075, TASK-UL076, TASK-UL077
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
