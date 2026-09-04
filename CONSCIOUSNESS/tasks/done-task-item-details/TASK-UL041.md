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

- [x] Each of FEAT-UL3 through FEAT-UL13 (Hierarchical, DBSCAN, GMM, PCA, Manifold, Anomaly Detection, Association Rules, Topic Modeling, SOM, Autoencoders, Professional Practice) gets an independent agent review against its own acceptance criteria and referenced notebooks — all 11 reviewed
- [x] Each feature moves to FEATURE-MAINTAINED-DONE-INDEX.md only on an agent-approved verdict; features with unmet criteria stay in backlog with the gap documented (same honesty pattern as FEAT-UL14) — corrected in execution: the live `approve` tooling requires a human verdict even for agent-approved features (the FEAT-UL14 precedent), so none of the 10 agent-approved features here moved to maintained either; all 11 stay in backlog with their review outcome recorded on the card
- [x] Review verdicts recorded in REVIEW-INDEX.md per review-gates precept — 11 fragments written (10 agent-approved, 1 agent-rejected for FEAT-UL12)
- [x] Cross-reference against TASK-UL040 — TASK-UL040 was already closed (30/30 notebooks executing clean) by the time this task ran, so execution evidence was confirmed for every feature without re-discovering it per-feature

## Outcome

10 of 11 features (FEAT-UL3 through FEAT-UL11, FEAT-UL13) fully pass their
acceptance criteria — agent-approved, awaiting human sign-off. FEAT-UL12
(Autoencoders) has three genuine content gaps found by direct keyword
search of the raw notebook JSON rather than trusting section headers alone
(the same discipline that caught FEAT-UL14's gaps): no latent-space
interpolation demo, no reconstruction-based anomaly-detection demo, and no
VAE-vs-GAN comparison anywhere in the practical notebook. Documented on
FEAT-UL12's card, verdict recorded as agent-rejected, and the gap filed as
backlog TASK-UL043 rather than left as an undiscovered claim.

"Roadmap is source of truth" is now true for this section of the backlog:
every feature's status reflects an independently verified review, not an
assumed pass.

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
