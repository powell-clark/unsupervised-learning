# TASK-UL081: Re-verify FEAT-UL15 AC-11 and close lesson 17

## Context

Filed by TASK-UL047's rejection branch. The independent review of lesson 17 (Spectral Clustering and Graph Laplacians) passed AC-1..AC-10 with cited cell evidence and **rejected on AC-11**, which requires an explicit contrast with both lesson 1 (K-Means) and lesson 3 (DBSCAN) on non-convex clusters — DBSCAN appeared nowhere in either notebook.

The gap was closed in commit `fbee6c5`: `notebooks/17a_spectral_clustering_theory.ipynb` gained a "The Other Non-Convex Method: Spectral vs DBSCAN" section (comparison table plus a three-dataset, three-algorithm cell), and 17a re-executed at 9/9 cells, zero errors, 7 figures.

**Why this task exists rather than a straight close:** that fix was authored by the same session that built the notebooks, so it is unverified. Self-approval is exactly the failure the review gate exists to prevent — the first review found a real gap precisely because it was independent.

## Acceptance Criteria

- [ ] Independent re-review of AC-11 by a fresh-context subagent, judging the raw `.ipynb` JSON rather than section headings: DBSCAN is genuinely imported and run (not merely described), the non-convex contrast is explicit, and the K-Means contrast is still present
- [ ] The new section's prose and print statements are checked against the cell's own stored output — the section claims DBSCAN and spectral both reach ARI 1.000 on moons and circles, and that on an unequal-density pair DBSCAN falls to ~0.889 with ~16% of points marked noise while spectral holds 1.000. Both previous reviews of this lesson found a prose-versus-output contradiction, so this check is load-bearing
- [ ] Confirm the inserted section did not disturb AC-5 (from-scratch implementation validated numerically) or AC-10 (both notebooks execute clean)
- [ ] Verdict fragment appended to `CONSCIOUSNESS/stream/review-verdicts/<session>.main.jsonl` with `target_type: feature`, `target_id: FEAT-UL15`
- [ ] On approval: FEAT-UL15 → `maintained` (row to FEATURE-MAINTAINED-DONE-INDEX.md, card to maintained-done-feature-item-details/), STORY-UL15 → `fulfilled` (row to STORY-FULFILLED-REJECTED-INDEX.md), DIRECT-UL14 → `done` with `actual_end` set, row to DIRECT-MAINTAINED-DONE-INDEX.md, card moved
- [ ] On rejection: document the remaining gap on FEAT-UL15 and file one further fix task

## Note on an in-flight review

A re-review subagent (`reverify-lesson-17`, Sonnet) was dispatched at 2026-09-05 00:30 bst against exactly this scope but had not reported when the session ran out of context. If its verdict surfaces, it satisfies the first three criteria above — otherwise simply dispatch a fresh one; the review is cheap and repeatable.

## Dependencies

- Blocked by: none
- Blocks: TASK-UL080 (Part II corpus close-out)
- Filed by: TASK-UL047
