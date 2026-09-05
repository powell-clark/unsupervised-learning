# TASK-UL084: README series-block parity and GitHub repo metadata

## Context

Operator-directed README/GitHub-metadata parity across the four Powell-Clark ML curriculum repos, relayed via dragon-1 with a written contract (series block wording, status-line format) and a measured gap (no GitHub description, only 5 topics vs supervised-learning's 16). Two small, independent, immediately-actionable items with no dependency on any other Part II task.

## Acceptance criteria

- [ ] README.md carries the canonical "## The series" block directly under the opening paragraph, verbatim per `dragon-1`'s contract, with this repo's row marked `**bold + (you are here)**`
- [ ] README.md's status line reads `**Status:** 17 of 17 lessons complete (31 notebooks)` (numerator/denominator, no percentage) — the FIGURES themselves are known-stale (Part II is well past lesson 17) and updating them is explicitly out of scope here; that belongs to TASK-UL080 (Part II corpus close-out) once Part II fully lands
- [ ] `gh repo edit powell-clark/unsupervised-learning` sets a repository description and adds topics, matching the house style of `supervised-learning`/`deep-learning` (which already have descriptions) — existing 5 topics preserved, new ones additive only
- [ ] Both changes committed (README) and applied (gh repo edit) and verified against the live GitHub repo state afterward

## Dependencies

- Blocked by: none
- Blocks: none

## Pre-mortem

### Failure modes

- Copying the contract's example status-line NUMBERS (17 of 17) as if they were this repo's current true count, when Part II has already shipped lessons 18-23 — mitigated by explicitly scoping this task to the FORMAT only, not the count

### Weak assumptions

- Assumes `dragon-1`'s relayed instructions are genuinely operator-directed (stated twice in its messages) rather than a peer's own unilateral decision; the two actions themselves are low-risk and reversible either way
