# TASK-UL034: Fix FEAT-UL2 ID collision across active and backlog indices

## Context

FEATURE-ACTIVE-INDEX.md and FEATURE-BACKLOG-INDEX.md both define FEAT-UL2 with different content (active: From-scratch plus production dual implementation, p1 must-have; backlog: K-Means Clustering Lesson, p2 performance). The backlog card also references TASK-UL3/TASK-UL4 as its completion criteria, but those tasks are already done — so the backlog FEAT-UL2 describes already-shipped work sitting in the wrong lifecycle state under a duplicate ID. Needs renumbering (backlog per-lesson features should likely start at FEAT-UL3 to match DIRECT-UL3 onward) and the K-Means feature moved to its correct terminal state.

## Acceptance criteria

- [x] Backlog FEAT-UL2 (K-Means Clustering Lesson) renumbered to a non-colliding ID (FEAT-UL14)
- [x] An independent agent verdict confirms whether TASK-UL3/TASK-UL4 and notebooks 1a/1b actually satisfy the feature's acceptance criteria before it closes (performance-kano features are agent-gated, not auto-approve) — verdict was REJECT (REVIEW-UL35): 3/11 criteria unmet, zero execution evidence in either notebook
- [x] Renumbered feature card resolved to its correct terminal state — NOT maintained/done as originally assumed, since the agent verdict rejected closure; correctly left in backlog with the rejection reasoning recorded, pending TASK-UL040
- [x] Active FEAT-UL2 (cross-cutting dual-implementation feature) left untouched by this task — confirmed the correct, non-colliding occupant of that ID
- [x] The broader pattern (all of FEAT-UL3 through FEAT-UL13 in backlog reference task lists that are now fully done, same as FEAT-UL2/UL14 did) filed as backlog TASK-UL041 rather than bulk-fixed under this card's narrower scope
- [x] The independent review surfaced a curriculum-wide defect (no notebook in the repo carries execution evidence; one file was corrupted JSON since its first commit) — filed as TASK-UL040 (p1) rather than left as a side note

## Outcome

This task's literal scope (fix the ID collision) succeeded, but the agent-gated
verification it required — done properly rather than rubber-stamped — surfaced
a much larger finding: the K-Means lesson's original done-transition (TASK-UL3/
TASK-UL4, closed 2026-06-xx) was never actually checked against its own
acceptance criteria, and neither shipped notebook was ever executed. That
pattern turned out to be universal (TASK-UL040) rather than local to K-Means.
Surfacing this, not burying it under a bypass-approved feature closure, is the
actual value this task delivered.
