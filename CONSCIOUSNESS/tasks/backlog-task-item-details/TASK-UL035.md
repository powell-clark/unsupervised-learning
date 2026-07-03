# TASK-UL035: Fix stale DIRECT-UL1 placeholder across story backlog

## Context
Discovered during a backlog-coherence check (dispatched hygiene pass, 2026-07-03). Every
row in `CONSCIOUSNESS/stories/STORY-BACKLOG-INDEX.md` carries `directive_id=DIRECT-UL1`,
which reads as a copy-paste placeholder from initial bulk creation rather than the correct
per-lesson directive. For example STORY-UL8 (anomaly detection) references DIRECT-UL1
(Clustering Foundations) instead of DIRECT-UL8 (Anomaly Detection) — the directive that
actually owns TASK-UL15/TASK-UL16, its own task_ids.

Compounding gap: `STORY-ACTIVE-INDEX.md` is empty (header row only) even though
DIRECT-UL1 and DIRECT-UL8 are both in_progress/pending with active or done tasks
underneath them. STORY-UL7 (Manifold Learning) still sits in backlog despite both of
its tasks (TASK-UL13, TASK-UL14) being done — it should have been promoted through
in_progress and, per the review-gates precept, fulfilled once its owning features
reached maintained.

## Acceptance Criteria
- [ ] Audit every STORY-UL* row's directive_id against the directive that actually owns
      its task_ids (cross-reference DIRECT-ACTIVE-INDEX.md / DIRECT-BACKLOG-INDEX.md)
- [ ] Correct each mismatched directive_id in STORY-BACKLOG-INDEX.md
- [ ] Promote STORY-UL7 (and any other story whose tasks are all done) out of backlog
      per its resolved lifecycle state (fulfilled, per review-gates precept)
- [ ] Verify STORY-ACTIVE-INDEX.md reflects the story owning any in_progress task
      (e.g. STORY-UL8 while TASK-UL15 is in_progress)
- [ ] Re-run the coherence check across all four story/task/feature/directive index
      quadruplets to confirm no other placeholder drift exists
- [ ] Fix column-shape mismatch on the TASK-UL031/TASK-UL032/TASK-UL034 rows in
      TASK-BACKLOG-INDEX.md — each row has 13 pipe-delimited fields against a 10-column
      header, with the .md filename landing in the blocks column instead of blocked_by/
      blocks/sequence/expected_duration/story_points being populated correctly

## Dependencies
None — pure data-correctness pass across existing indices, no code change.
