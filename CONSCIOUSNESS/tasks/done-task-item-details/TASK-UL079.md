# TASK-UL079: Verify lesson 28: independent review and close FEAT-UL26

## Context
Verification task for Part II lesson 28 (Capstone: An End-to-End Unsupervised Analysis). Notebooks: `notebooks/28_capstone_pipeline.ipynb`. Feature card: `CONSCIOUSNESS/features/backlog-feature-item-details/FEAT-UL26.md`. Story: STORY-UL26. Directive: DIRECT-UL25. This task is the review gate: the feature is kano `performance` (agent gate, one independent review), so an approved verdict here closes the feature, story and directive with no human step.

## Verification procedure (identical for every Part II lesson)

1. **Execution evidence.** From the repo root run, for each notebook of this lesson:
   `jupyter execute notebooks/<nb> --output /tmp/<nb>` then check the scratch copy with
   the repo's sweep script pattern: every code cell has a non-null `execution_count` and no
   output carries `output_type == "error"`. If the committed notebook lacks outputs, copy the
   executed scratch copy back over it and commit — the shipped artefact must carry outputs
   (this is the TASK-UL040 standard).
2. **Independent review, different model, fresh context.** Dispatch ONE subagent with the
   Agent tool, `model: "opus"`, `subagent_type: "general-purpose"`, and a self-contained
   prompt containing: the feature card's full acceptance-criteria list, the notebook paths,
   and the instruction to open the raw `.ipynb` JSON and decide each criterion from actual
   cell content (code and markdown), citing the cell index that satisfies it or stating
   plainly that nothing does. Section headers alone are not evidence — FEAT-UL12's review
   found three missing criteria that header-matching would have passed. The subagent
   returns a per-criterion table (met / not met / evidence).
3. **Record.** Update the feature card: tick every met criterion with the evidence cited;
   leave unmet ones unticked with the reviewer's finding written under them. Append a
   verdict fragment to `CONSCIOUSNESS/stream/review-verdicts/<session>.main.jsonl`
   (`target_type: feature`, verdict `agent-approved` if every criterion is met, else
   `agent-rejected`, note summarising the evidence). Features here are kano `performance`,
   which resolves to an agent gate with one required review — no human verdict is needed.
4. **Close or bounce.**
   - Approved: move the feature row from FEATURE-BACKLOG-INDEX.md to
     FEATURE-MAINTAINED-DONE-INDEX.md with status `maintained` (match that file's header),
     move its card to maintained-done-feature-item-details/, move the story row from
     STORY-BACKLOG-INDEX.md to STORY-FULFILLED-REJECTED-INDEX.md with status `fulfilled`
     (match its header), and set the directive's status to `done` with `actual_end` today in
     DIRECT-ACTIVE-INDEX.md, then move that row to DIRECT-MAINTAINED-DONE-INDEX.md (match
     its header) and its card to maintained-done-directive-item-details/.
   - Rejected: file ONE fix task with `append-task-cli` (`--target backlog`, `--directive`,
     `--story`, `--features` set to this lesson's ids, priority p2) whose acceptance
     criteria are exactly the unmet items plus "re-run this verification procedure and,
     on approval, perform the close step". Leave the feature in backlog with the gaps
     documented. Do not close this verification task as done until the verdict is recorded.
5. Commit and push with the task id in the subject. Then auto-close this task per the
   review-gates auto-close path (tasks are auto-approve).

## Acceptance Criteria
- [x] Execution evidence confirmed for every notebook of this lesson (all code cells executed, zero errors, outputs committed) — reviewer independently re-ran `jupyter nbconvert --execute` on a fresh copy, EXIT=0, 6/7 cells byte-identical to committed outputs (7th differs only in a CPU-timing string)
- [x] Independent review performed by a fresh-context opus subagent against every criterion on FEAT-UL26, with per-criterion evidence recorded on the card — dispatched via Agent tool (subagent_type general-purpose, model opus), full per-criterion table returned, 7/8 criteria MET, AC-4 MET-IN-MECHANISM-BLOCKED
- [x] Verdict fragment appended (agent-approved or agent-rejected) with the evidence summary — agent-rejected recorded for FEAT-UL26, reviewer-id verify-lesson-28-opus
- [ ] On approval: FEAT-UL26 moved to maintained, STORY-UL26 to fulfilled, DIRECT-UL25 to done — indexes and cards both moved — N/A this round, verdict was REJECT
- [x] On rejection: one fix task filed with the exact unmet criteria; feature left in backlog with gaps documented — TASK-UL086 filed (D1-D8 as ACs plus a re-verification AC), FEAT-UL26.md updated with a Rejection Gaps section and 7/8 ACs ticked with cell-level evidence, AC-4 left unticked

## Review outcome
REJECT. Independent fresh-context opus review found every number in the notebook reproduces exactly from seed 42 (no fabrication, no stale numbers, no numpy-scalar repr leaks) and 7 of 8 criteria are cleanly met, but AC-4 is blocked by a HIGH-severity defect (D1): cell 11 prints that the gap statistic decided the final K, while the code actually discards the gap statistic's K=5 pick and falls back to the resampling-stability tie's lowest member (K=3) — a direct contradiction between the notebook's stated methodology and its executed one, in a capstone whose own thesis is "a sequence of justified choices, not default choices". Six further MEDIUM-severity honesty defects (D2-D7) and several LOW polish items (D8-D13) were also found and filed as TASK-UL086's acceptance criteria.

## Execution
- Reviewer model: opus (fresh-context subagent). Do not review your own build in the same context — the point is independence.
- Expected duration: 1h

## Dependencies
- Blocked by: TASK-UL078
- Blocks: the Part II corpus close-out task
