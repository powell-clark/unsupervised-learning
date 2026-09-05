# TASK-UL078: Lesson 28 capstone notebook: Capstone: An End-to-End Unsupervised Analysis

## Context
Part II, lesson 28, single notebook `notebooks/28_capstone_pipeline.ipynb`. The capstone reuses methods from both parts of the course on one problem, with a decision log and a written report. Feature card: FEAT-UL26. Build it last: it should cite the Part II notebooks that exist by then (the verification tasks leave the corpus in a consistent state; if a lesson is still open, use the Part I method instead and say so).

## Notebook plan (sections, in order)
1. Problem framing on one offline dataset (sklearn load_wine or a realistic customer dataset generated in-notebook with documented structure): questions before methods
2. Preprocessing with a leakage-safe pipeline (lesson 15) and a decision log recording each choice
3. Representation: PCA (5) vs contrastive/autoencoder features where applicable (12, 26) vs raw; chosen with evidence
4. Structure: K-Means / GMM / spectral / DP-mixture (1, 4, 17, 22) with stability and consensus (27) deciding K and confidence
5. Density and anomalies: KDE / flow / Isolation Forest (18, 19, 7) agreeing or disagreeing on outliers
6. Interpretation and a written report section: what was found, how confident, what was not done and why — the honesty section is mandatory

**Data:** sklearn bundled or in-notebook generated — no downloads

## Acceptance Criteria
- [x] Every section above present; the decision log and the not-done-and-why list are mandatory — cells 0-16 (17 cells): Intro (0), TOC (1), Required Libraries (2-3), Problem Framing (4-5), Preprocessing with decision_log (6-7), Representation (8-9), Structure (10-11), Anomalies (12-13), Written Report incl. not-done-and-why section 4 (14-15), Conclusion (16)
- [x] At least two candidate methods compared with evidence at each of: representation, clustering, anomaly detection — representation: raw/PCA/autoencoder compared cell 9 (with a min-cluster-size guard added on pre-commit review, see below); clustering: K-Means vs GMM cross-check cell 11 (ARI=0.650 at K=3); anomaly detection: Isolation Forest vs KDE cell 13
- [x] All criteria on FEAT-UL26 satisfiable from this notebook — verified against FEAT-UL26.md; the independent agent review in TASK-UL079 ticks and closes that card
- [x] `jupyter execute` passes: every code cell executed, zero errors, outputs committed — commit a85ea8c, 7/7 code cells executed with zero errors (verified via cell-output error scan)
- [x] No network downloads — cell 5 generates the synthetic customer dataset in-notebook; no external fetches anywhere in the notebook

## Pre-commit review finding (self-caught, fixed before shipping)
The first execution picked "autoencoder (3-d)" as the winning representation on a bare highest-silhouette-at-any-K search (silhouette 0.8213 at K=2). Independent verification (four standalone scripts re-deriving the clustering from scratch) showed this K=2 split was [586, 14] with the 14-point cluster drawing almost evenly from all four true segments (ARI vs true ≈ -0.0001) — a degenerate split isolating the injected extreme-spend anomalies, not real segment structure. The same ~14-point degenerate cluster recurred at every K tested for all three representations (raw, PCA, autoencoder), confirming K-Means' well-known outlier sensitivity was distorting the representation-choice metric universally. Fixed by adding a `min_cluster_frac=0.05` guard to `silhouette_at_best_k` (cell 9), reporting both the naive and guarded search honestly; the guarded search excludes the autoencoder entirely (no non-degenerate K in range(2,7)) and picks PCA (silhouette 0.4256). Downstream K-selection (gap+stability, cell 11, unchanged reused logic from 27A) then lands on K=3 for PCA (ARI-vs-true=0.226, sanity check only). Conclusion (cell 16) and report (cell 15) updated to state this honestly, including a dynamic small-cluster flag tying forward to Section 6's anomaly detection.

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
- Expected duration: 3h

## Dependencies
- Blocked by: none hard (see Context on ordering)
- Blocks: the lesson-28 verification task
