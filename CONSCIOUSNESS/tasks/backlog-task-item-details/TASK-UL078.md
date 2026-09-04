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
- [ ] Every section above present; the decision log and the not-done-and-why list are mandatory
- [ ] At least two candidate methods compared with evidence at each of: representation, clustering, anomaly detection
- [ ] All criteria on FEAT-UL26 satisfiable from this notebook
- [ ] `jupyter execute` passes: every code cell executed, zero errors, outputs committed
- [ ] No network downloads

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
