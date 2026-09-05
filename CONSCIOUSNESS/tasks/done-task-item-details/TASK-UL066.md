# TASK-UL066: Lesson 24a theory: Time-Series Clustering and Dynamic Time Warping

## Context
Part II, lesson 24, theory notebook `notebooks/24a_time_series_clustering_theory.ipynb`. As a learner I want a time-series clustering lesson so that I can group sequences by shape when Euclidean distance on raw samples is the wrong metric. Feature card: FEAT-UL22 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. Why Euclidean fails on shifted/warped series (a two-series demonstration)
2. Dynamic time warping: the alignment problem, the cumulative-cost recurrence, the DP table, backtracking the path — derived and implemented from scratch
3. Constraints: Sakoe-Chiba band and why it is both faster and often better; complexity
4. Averaging under DTW: DBA (DTW barycenter averaging) explained and implemented for small series
5. k-medoids with a DTW distance matrix from scratch; why k-means needs DBA
6. Representations: z-normalisation, PAA and SAX sketches, when to cluster features instead of shapes

**From scratch:** dtw() with optional band, dba(), and dtw_kmedoids() in NumPy
**Data:** synthetic shapes (shifted sines, ramps, steps) — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL22 are satisfiable from this notebook's content (read the card before writing)
- [ ] `jupyter execute` passes: every code cell executed, zero errors, outputs committed
- [ ] Colab-runnable: no local files outside the repo, no network downloads

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
- Builder model: the session model (sonnet is sufficient).
- Expected duration: 2h

## Dependencies
- Blocked by: TASK-UL044
- Blocks: the 24b practical and the lesson-24 verification task
