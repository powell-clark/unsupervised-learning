# TASK-UL085: Fix FEAT-UL23 AC-11 wording: lesson 8 generator unreusable

## Context

verify-lesson-25 (REVIEW-UL096) rejected FEAT-UL23 at 10 of 11: AC-11 as literally worded (lessons 8, 9, 10 data generators reused) cannot be satisfied for lesson 8 -- 8b's data is loaded over the network (which AC-10 forbids reusing) and 8a's own ratings are uniform random with no latent structure worth reusing; 9A and 10B are already genuinely reused (byte-identical, confirmed by the reviewer). Acceptance criteria: (1) revise FEAT-UL23's AC-11 wording to accurately scope the cross-lesson-reuse requirement to lessons 9 and 10 (documenting why lesson 8 is excluded, citing REVIEW-UL096), (2) re-run the verification procedure (dispatch a fresh independent reviewer against the revised criteria), (3) on approval, perform the close step: move FEAT-UL23 to maintained, STORY-UL23 to fulfilled, DIRECT-UL22 to done.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-UL22
- Story: STORY-UL23
- Features: FEAT-UL23

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
