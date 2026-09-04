# TASK-UL050: Verify lesson 18: independent review and close FEAT-UL16

## Context
Verification task for Part II lesson 18 (Kernel Density Estimation and Nonparametric Density). Notebooks: `notebooks/18a_kernel_density_estimation_theory.ipynb`, `notebooks/18b_kernel_density_estimation_practical.ipynb`. Feature card: `CONSCIOUSNESS/features/backlog-feature-item-details/FEAT-UL16.md`. Story: STORY-UL16. Directive: DIRECT-UL15. This task is the review gate: the feature is kano `performance` (agent gate, one independent review), so an approved verdict here closes the feature, story and directive with no human step.

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
- [ ] Execution evidence confirmed for every notebook of this lesson (all code cells executed, zero errors, outputs committed)
- [ ] Independent review performed by a fresh-context opus subagent against every criterion on FEAT-UL16, with per-criterion evidence recorded on the card
- [ ] Verdict fragment appended (agent-approved or agent-rejected) with the evidence summary
- [ ] On approval: FEAT-UL16 moved to maintained, STORY-UL16 to fulfilled, DIRECT-UL15 to done — indexes and cards both moved
- [ ] On rejection: one fix task filed with the exact unmet criteria; feature left in backlog with gaps documented

## Execution
- Reviewer model: opus (fresh-context subagent). Do not review your own build in the same context — the point is independence.
- Expected duration: 1h

## Dependencies
- Blocked by: TASK-UL048, TASK-UL049
- Blocks: the Part II corpus close-out task
