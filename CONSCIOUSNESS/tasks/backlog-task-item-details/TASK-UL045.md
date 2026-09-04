# TASK-UL045: Lesson 17a theory: Spectral Clustering and Graph Laplacians

## Context
Part II, lesson 17, theory notebook `notebooks/17a_spectral_clustering_theory.ipynb`. As a learner I want a spectral clustering lesson on similarity graphs and graph Laplacians so that I can cluster data whose structure is connectivity, not compactness. Feature card: FEAT-UL15 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. Similarity graphs: epsilon-neighbourhood, k-nearest-neighbour (mutual and not), fully connected RBF; how each choice changes connectivity
2. Graph Laplacians: unnormalised L = D - W, symmetric L_sym, random-walk L_rw; properties (PSD, zero eigenvalue per connected component) proved in the notebook
3. Why the eigenvectors: RatioCut and NCut as relaxed graph-partition problems, the Rayleigh quotient argument, and why K-Means on the spectral embedding recovers the partition
4. The eigengap heuristic for choosing K, with a worked plot
5. From scratch: build W, D, L_sym in NumPy, take the K smallest eigenvectors with np.linalg.eigh, row-normalise, K-Means (reuse the lesson-1 implementation pattern) — a spectral_clustering(X, k, affinity) function
6. Failure modes: disconnected graphs, bad sigma, the two-moons/concentric-circles contrast with K-Means from lesson 1

**From scratch:** spectral_clustering() in NumPy: affinity matrix, normalised Laplacian, eigendecomposition, K-Means on the embedding
**Data:** make_moons, make_circles, make_blobs (sklearn.datasets) — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL15 are satisfiable from this notebook's content (read the card before writing)
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
- Blocked by: none
- Blocks: the 17b practical and the lesson-17 verification task
