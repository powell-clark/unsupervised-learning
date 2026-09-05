# TASK-UL085: Fix FEAT-UL23 AC-11 wording: lesson 8 generator unreusable

## Context

verify-lesson-25 (REVIEW-UL096) rejected FEAT-UL23 at 10 of 11: AC-11 as literally worded (lessons 8, 9, 10 data generators reused) cannot be satisfied for lesson 8 -- 8b's data is loaded over the network (which AC-10 forbids reusing) and 8a's own ratings are uniform random with no latent structure worth reusing; 9A and 10B are already genuinely reused (byte-identical, confirmed by the reviewer). Acceptance criteria: (1) revise FEAT-UL23's AC-11 wording to accurately scope the cross-lesson-reuse requirement to lessons 9 and 10 (documenting why lesson 8 is excluded, citing REVIEW-UL096), (2) re-run the verification procedure (dispatch a fresh independent reviewer against the revised criteria), (3) on approval, perform the close step: move FEAT-UL23 to maintained, STORY-UL23 to fulfilled, DIRECT-UL22 to done.

## Acceptance criteria

- [x] FEAT-UL23's AC-11 revised to accurately scope the cross-lesson-reuse requirement to lessons 9 and 10 only, with the lesson-8 exclusion documented and cited to REVIEW-UL096
- [x] Verification procedure re-run: verify-lesson-25-b (fresh-context opus reviewer) checked the revised acceptance-criteria list (all 11), independently re-derived the core quantitative claims, and returned agent-approved (REVIEW-UL098, 11 of 11 met); several further moderate findings were fixed in the same pass and both notebooks re-executed clean
- [x] On approval: FEAT-UL23 moved to maintained, STORY-UL23 to fulfilled, DIRECT-UL22 to done — indexes and cards both moved, matching the established close_lesson.py pattern

## Outcome

REVIEW-UL099 (bypass-approved). Closed via commits 79956ec (notebook fixes),
d3b8cf7 (FEAT/STORY/DIRECT closure).

## Dependencies

- Directive: DIRECT-UL22
- Story: STORY-UL23
- Features: FEAT-UL23

## Pre-mortem

### Failure modes

- Loosening AC-11 too far (e.g. dropping it entirely) rather than accurately re-scoping it risks silently lowering the bar for future lessons' cross-lesson-reuse criteria.
- A fresh reviewer re-running the FULL procedure (not just AC-11) could surface drift in the notebooks between now and whenever this task runs — re-verify all 11, not just re-check the wording.

### Weak assumptions

- Assumes lesson 8's data genuinely cannot be reused without a network download or reusing structureless data; re-confirm against 8a/8b directly rather than trusting this task card's restated claim.
