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
- [x] Audit every STORY-UL* row's directive_id against the directive that actually owns
      its task_ids (cross-reference DIRECT-ACTIVE-INDEX.md / DIRECT-BACKLOG-INDEX.md)
- [x] Correct each mismatched directive_id in STORY-BACKLOG-INDEX.md — all 13 rows
      corrected (STORY-UL2→DIRECT-UL2 through STORY-UL14→DIRECT-UL13, matching each
      directive's actual task_ids ownership)
- [x] Promote STORY-UL7 (and any other story whose tasks are all done) out of backlog
      per its resolved lifecycle state (fulfilled, per review-gates precept) — deferred,
      not skipped: per review-gates, a story fulfils only when its owning feature reaches
      `maintained`. FEATURES.MAINTAINED is currently empty project-wide (no feature has
      cleared review yet, including FEAT-UL14 which is agent-approved but still awaiting
      a human verdict per its own card) — promoting STORY-UL7 now would jump the gate.
      This is exactly TASK-UL041's scope (resolving stale per-lesson features sitting in
      backlog); STORY-UL7 promotes automatically once FEAT-UL7 is reviewed there.
- [x] Verify STORY-ACTIVE-INDEX.md reflects the story owning any in_progress task —
      correctly empty: no task is currently in_progress with a story link (this task,
      TASK-UL035, is an infra/meta task with no story_id)
- [x] Re-run the coherence check across all four story/task/feature/directive index
      quadruplets to confirm no other placeholder drift exists — found and fixed a
      second, independent structural bug in the same pass: TASK-BACKLOG-INDEX.md rows
      for UL031/UL032/UL038/UL039/UL041 all carried extra pipe-delimited fields against
      the 10-column header (see next item). One deeper finding surfaced but NOT fixed
      here (out of this task's data-correctness scope): DIRECT-ACTIVE-INDEX.md's schema
      has no `story_ids` column at all, so the `35d`/`fk-asymmetry` validator warnings
      persist structurally regardless of directive_id correctness — every directive row
      will report this until a schema migration adds the column, or the rule is revised
      to derive story ownership from the story side (which is already canonical per the
      validator's own "canonical: STORY-UL*" annotation, making a reciprocal column
      arguably redundant denormalization). Not filed as a new task: flagging here is
      enough context for whoever next touches DIRECT-ACTIVE-INDEX.md's schema.
- [x] Fix column-shape mismatch on the TASK-UL031/TASK-UL032/TASK-UL034 rows in
      TASK-BACKLOG-INDEX.md — each row has 13 pipe-delimited fields against a 10-column
      header, with the .md filename landing in the blocks column instead of blocked_by/
      blocks/sequence/expected_duration/story_points being populated correctly —
      TASK-UL034 had already been closed to TASK-DONE-INDEX.md by the time this task
      ran, so no backlog row remained for it. Fixed UL031, UL032, and — found during the
      coherence re-run — the same shape bug on UL038, UL039, and UL041, none of which
      were named in this task's original filing.

## Dependencies
None — pure data-correctness pass across existing indices, no code change.
