# TASK-UL032: Goal hook re-activation stall on consciousness session end

> **Needs review:** the agent created this task during real-time validation and is uncertain about scope or priority. Operator should review and re-tier as appropriate.


## Context

Auto-created from /consciousness:issue (issue:n9ryUScLVbJuvwe6kGllD).

Report context:
Goal hook repeatedly re-activates consciousness session after STATUS: complete instead of respecting the end state and exiting cleanly. Stop hook reports 'consciousness:suspended' and advises /goal clear, but goal keeps firing on subsequent turns.

Transcript: chats/claude-code/2026-07-01/session-25d57c19.jsonl

## Acceptance criteria

- [ ] Root cause identified for why the goal hook keeps firing after a session reports 'consciousness:suspended'
- [ ] Fix verified: the goal hook respects the suspended/complete end state and does not re-fire on subsequent turns
- [ ] Regression check: legitimate goal re-activation cases (e.g. a new directive arriving) still fire correctly
