# TASK-UL086: Fix lesson 28 capstone: honest K-selection rationale and report

## Context

TASK-UL079's independent review (REJECT verdict, agent-rejected on FEAT-UL26) found notebooks/28_capstone_pipeline.ipynb's cell 11 K-selection logic contradicts its own printed rationale: the code discards the gap statistic's K=5 pick and falls back to the stability tie's lowest member (K=3), while the print statement claims gap statistic was the deciding tool. Fix acceptance criteria are the exact unmet items from the review.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-UL25
- Story: STORY-UL26
- Features: FEAT-UL26

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
