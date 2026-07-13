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
- [ ] All remaining 29 notebooks re-executed in place (`jupyter execute --output <scratch>`, verify zero errors, copy back over the committed file) and committed with real outputs
- [ ] Each notebook's execution log checked for real errors/warnings (not just "did it finish") before considering it done
- [ ] The 3 acceptance-criteria gaps found in FEAT-UL14 (soft K-Means/probabilistic section, elbow-method plot, initialization contrast in 1b) either fixed or explicitly re-scoped and disclosed, matching this project's honesty pattern for narrowed scope
- [ ] A spot-check across a few other pre-existing (non-this-session) notebooks for similar undiscovered corruption or content gaps, given 0b was corrupted from its first commit and nobody noticed for months

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
