# TASK-UL034: Fix FEAT-UL2 ID collision across active and backlog indices

## Context

FEATURE-ACTIVE-INDEX.md and FEATURE-BACKLOG-INDEX.md both define FEAT-UL2 with different content (active: From-scratch plus production dual implementation, p1 must-have; backlog: K-Means Clustering Lesson, p2 performance). The backlog card also references TASK-UL3/TASK-UL4 as its completion criteria, but those tasks are already done — so the backlog FEAT-UL2 describes already-shipped work sitting in the wrong lifecycle state under a duplicate ID. Needs renumbering (backlog per-lesson features should likely start at FEAT-UL3 to match DIRECT-UL3 onward) and the K-Means feature moved to its correct terminal state.

## Acceptance criteria

- [ ] _(to be filled in)_
