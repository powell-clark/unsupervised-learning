# TASK-UL080: Part II corpus close-out: README, full sweep, syllabus status

## Context
Runs after every Part II lesson has been built and independently verified. Makes the corpus readable as one course and proves the whole thing executes.

## Acceptance Criteria
- [ ] README.md gains a "Part II — Advanced Topics" section listing lessons 17-28 with one line per notebook, in the same style as the Part I entries, and the status line updated (lesson and notebook counts)
- [ ] README "Technical Stack" lists hmmlearn and tslearn; "Learning Path" gains a Part II step
- [ ] Full sweep: the execution-evidence script (the one in TASK-UL040's card) reports every notebook in notebooks/ executed with zero errors — all Part I and Part II files
- [ ] `pip install -r requirements.txt` then an import smoke test of every library the notebooks use passes
- [ ] CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md status table updated to done per lesson, with the verification task ids
- [ ] Every Part II directive is in DIRECT-MAINTAINED-DONE-INDEX.md and every Part II story in STORY-FULFILLED-REJECTED-INDEX.md (fix any the verification tasks missed, citing the verdict)
- [ ] Commit and push

## Execution
- Builder model: the session model (sonnet is sufficient)
- Expected duration: 2h

## Dependencies
- Blocked by: TASK-UL047, TASK-UL050, TASK-UL053, TASK-UL056, TASK-UL059, TASK-UL062, TASK-UL065, TASK-UL068, TASK-UL071, TASK-UL074, TASK-UL077, TASK-UL079
- Blocks: none
