# TASK-UL041: Resolve stale per-lesson features sitting in backlog

## Context

Discovered while fixing TASK-UL034's FEAT-UL2/FEAT-UL2 ID collision:
FEATURE-BACKLOG-INDEX.md holds twelve per-lesson features (FEAT-UL2 through
FEAT-UL13, now FEAT-UL14 through FEAT-UL13 after the UL034 renumbering) that
each reference a task pair or set that is fully done in TASK-DONE-INDEX.md.
None have been moved to FEATURE-MAINTAINED-DONE-INDEX.md. This is the same
pattern TASK-UL034 found for the K-Means feature (FEAT-UL14), applied across
the whole backlog.

These features are `kano: performance`, which per the review-gates precept
resolves to an agent-tier gate (not auto-approve) — closing each one properly
requires an independent agent verdict against its actual acceptance criteria,
not a bulk status flip. TASK-UL034's review of FEAT-UL14 found real gaps (3 of
11 criteria unmet, no execution evidence) despite the underlying tasks being
marked done — so these closures cannot be assumed clean; each needs the same
scrutiny.

## Acceptance Criteria

- [ ] Each of FEAT-UL3 through FEAT-UL13 (Hierarchical, DBSCAN, GMM, PCA, Manifold, Anomaly Detection, Association Rules, Topic Modeling, SOM, Autoencoders, Professional Practice) gets an independent agent review against its own acceptance criteria and referenced notebooks
- [ ] Each feature moves to FEATURE-MAINTAINED-DONE-INDEX.md only on an agent-approved verdict; features with unmet criteria stay in backlog with the gap documented (same honesty pattern as FEAT-UL14)
- [ ] Review verdicts recorded in REVIEW-INDEX.md per review-gates precept
- [ ] Cross-reference against TASK-UL040 — if that task is still open when this one is picked up, the "no execution evidence" finding will likely recur across most of these; don't re-discover it per-feature, just note it once and point to TASK-UL040

## Technical Notes

Twelve features, agent-gated — expect this to surface several more
FEAT-UL14-shaped gaps between claimed-done and actually-verified. Not urgent
(p4) since it's PGPS bookkeeping accuracy rather than a content defect, but
real: "Roadmap is source of truth" is not true right now for this section of
the backlog.

## Dependencies

- Blocked by: none (can run independently of TASK-UL040, though findings will overlap)
- Blocks: none
- Discovered via: TASK-UL034, REVIEW-UL35
