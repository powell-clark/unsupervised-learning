# TASK-UL087: Style rubric and first Feynman-conformance audit pass

## Context

First audit task under STORY-UL27 (Style Conformance Audit). Read supervised-learning's 1A, 1B, 2A, 2B, 2C notebooks (and 3 onward, scope to be confirmed against that repo's own numbering) and distill a short, checkable style rubric: Feynman voice, first-principles derivation order, assumed-maths ceiling (good A-level, not further maths), story-driven motivation before mathematics, runnable-end-to-end-without-edits bar. Apply the rubric to Part I's Foundation and Core Algorithms lessons (0, 1, 2, 3, 4) as the first audit batch -- not all 29 lessons at once. File one named refinement task per lesson that falls short, citing the specific gap. Per STORY-UL30: record Consciousness loop: on/off on this task's own Execution section when claimed.

## Acceptance criteria

- [ ] Read supervised-learning's 1A, 1B, 2A, 2B, 2C notebooks directly (raw notebook content, not just titles) and confirm the actual numbering scheme continues in a way that identifies what "3 onward" means concretely
- [ ] Distil a short (roughly one page), checkable style rubric with named, testable criteria: Feynman voice (concrete analogy before formalism), first-principles derivation order (motivation -> derivation -> from-scratch implementation -> production library -> agreement check, matching this repo's own established house pattern), assumed-maths ceiling (good A-level, explicitly NOT further maths -- name which techniques that excludes, e.g. no measure theory, no formal real analysis), story-driven motivation before any mathematics, and a runnable-end-to-end-without-edits bar
- [ ] Apply the rubric to Part I's Foundation and Core Algorithms lessons only (Lesson 0, 1, 2, 3, 4 -- 9 notebooks) as the first audit batch, reading each notebook's raw content against the rubric rather than assuming conformance from having built them
- [ ] For every lesson that falls short on any rubric criterion, file one named refinement task to backlog citing the specific gap and the specific criterion it fails -- never a blanket "needs polish"
- [ ] For every lesson that conforms, say so explicitly with the evidence (which cells/sections were checked), matching this repo's own review discipline (headers are not evidence)
- [ ] Record `Consciousness loop: on | off` in this task's own `## Execution` section at claim time, per STORY-UL30
- [ ] Commit and push

## Dependencies

- Directive: DIRECT-UL26
- Story: STORY-UL27
- Features: FEAT-UL1,FEAT-UL2

## Pre-mortem

### Failure modes

- Treating "Feynman voice" as a vibe rather than a checkable criterion — pin it to something falsifiable (e.g. "opens with a concrete story/analogy before any equation", checkable by reading the first markdown cell) rather than a subjective impression
- Auditing notebooks this session already built without the same scepticism applied to lessons built earlier in the curriculum's history — the rubric must be applied uniformly, not read charitably for recent work

### Weak assumptions

- Assumes supervised-learning's lesson numbering (1A, 1B, 2A, 2B, 2C, 3 onward) maps cleanly onto a house style already worth imitating — read those notebooks directly rather than assuming the operator's naming implies a finished, polished reference; if they too have gaps, say so rather than treating them as ground truth by default
