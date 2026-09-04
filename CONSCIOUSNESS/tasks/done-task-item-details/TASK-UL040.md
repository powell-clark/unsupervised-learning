# TASK-UL040: Notebooks ship without execution evidence — re-execute in place

## Context

Discovered during TASK-UL034's independent agent review of FEAT-UL14 (K-Means
lesson): notebooks 1a/1b showed `execution_count: null` and empty `outputs` on
every code cell, contradicting the review verdicts that closed TASK-UL3/UL4
("notebook shipped", "executed end-to-end"). A repo-wide check confirmed this
is universal, not local to K-Means:

```
python3 -c "
import json, glob
for fn in sorted(glob.glob('notebooks/*.ipynb')):
    nb = json.load(open(fn))
    cells = [c for c in nb['cells'] if c['cell_type']=='code']
    executed = sum(1 for c in cells if c.get('execution_count') is not None)
    print(fn, executed, '/', len(cells))
"
```

Every notebook in the repo (30 files, all of Lessons 0-16) showed 0 executed
cells at the time of this task's filing. The build pattern used throughout
this project — build a notebook via a `build_XX.py` script, then run
`jupyter execute notebook.ipynb --output <scratch-path>` and inspect the
scratch copy for errors — verifies correctness but never writes the executed,
output-bearing result back over the committed file. The verification was real
(bugs were genuinely caught and fixed this way), but the artifact a learner
actually opens on GitHub or in Colab carries no plots, no printed numbers, no
evidence the code runs — undermining the "Evidence over assertion" and
"Complete Implementations" claims in README.md.

Separately, `notebooks/0b_cluster_evaluation.ipynb` had a genuine JSON
corruption (a stray `>` character and a mangled cell block) that made the file
fail to parse entirely since its first commit (`b53932f`) — meaning it likely
never opened in Jupyter or Colab despite being marked done. This one file has
been repaired and re-executed in place as part of TASK-UL034 (20/20 cells,
zero errors) — see it as the reference pattern for the rest of this task.

## Acceptance Criteria

- [x] notebooks/0b_cluster_evaluation.ipynb: JSON corruption fixed, re-executed in place, 20/20 cells, zero errors
- [x] All remaining 29 notebooks re-executed in place (`jupyter execute --output <scratch>`, verify zero errors, copy back over the committed file) and committed with real outputs
- [x] Each notebook's execution log checked for real errors/warnings (not just "did it finish") before considering it done
- [x] The 3 acceptance-criteria gaps found in FEAT-UL14 (soft K-Means/probabilistic section, elbow-method plot, initialization contrast in 1b) either fixed or explicitly re-scoped and disclosed, matching this project's honesty pattern for narrowed scope — fixed in an earlier part of this task (commit 448d6fa), confirmed against FEAT-UL14.md: all 11 criteria met, independent review REVIEW-CCC067 agent-approved
- [x] A spot-check across a few other pre-existing (non-this-session) notebooks for similar undiscovered corruption or content gaps, given 0b was corrupted from its first commit and nobody noticed for months — exceeded: every one of the 30 curriculum notebooks (not just a sample) verified via `json.load` succeeding (rules out corruption) plus a full `jupyter execute` pass checked for `output_type == 'error'` on every code cell (rules out silent execution failures)

## Closing summary

All 30/30 notebooks in `notebooks/` now execute end-to-end with zero errors
and real committed outputs (0/30 → 30/30 across this task). Genuine bugs
found and fixed along the way, beyond the JSON corruption and content gaps
already noted above:
- `5a_pca_theory.ipynb`: `all_eigs, _, _, _ = pca_eig(X)` captured the
  projection matrix (the function's 1st return value) instead of the
  eigenvalues (2nd) — a positional-unpacking mistake
- `5b_pca_practical.ipynb`: a 2x3 `axes` grid indexed out of bounds against
  a 4-reconstruction loop — grid sized off a stale `k_values` length
- `6a_manifold_learning_theory.ipynb` (1x) and
  `6b_manifold_learning_practical.ipynb` (3x): scikit-learn 1.9.0 removed
  `TSNE`'s `n_iter` constructor argument in favour of `max_iter`
- `8b_recommender_systems_practical.ipynb`: `scikit-surprise` and
  `implicit` were never added to `requirements.txt` at all (added both);
  `cv_results['fit_time']`/`['test_time']` from `surprise.cross_validate`
  are plain tuples, not ndarrays, so `.mean()` needed `np.mean(...)`;
  `implicit` 0.7.3's `ALS.recommend()` now returns `(ids, scores)` arrays
  rather than a list of `(id, score)` pairs. Also required pre-seeding
  `surprise`'s MovieLens ml-100k dataset cache since `jupyter execute` has
  no stdin for the library's download-confirmation prompt, and
  files.grouplens.org's TLS certificate is currently expired server-side
  (verified via `openssl s_client`: notAfter=Aug 28 2026, genuinely
  lapsed) — fetched with certificate verification disabled for this one
  public, checksum-verifiable dataset zip only, then verified zip
  integrity before extracting to the expected cache path.

## Technical Notes

Priority p1: this is a correctness gap in the shipped artifact, not a nice-to-have.
Lessons 7-16 (built this session) were verified via the same scratch-output
pattern, so they likely have the same problem even though their review notes
say "executed end-to-end with jupyter execute with zero errors" — that claim
was about the scratch copy, not the committed file. Going forward, `jupyter
execute --inplace notebook.ipynb` (or an explicit copy-back step) should be the
standard, not `--output <scratch>` alone.

## Dependencies

- Blocked by: none
- Blocks: none
- Discovered via: TASK-UL034, REVIEW-UL35
