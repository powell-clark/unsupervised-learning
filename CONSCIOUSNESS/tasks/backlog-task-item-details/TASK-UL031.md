# TASK-UL031: Consciousness loop re-activation stall after STATUS: complete

> **Needs review:** the agent created this task during real-time validation and is uncertain about scope or priority. Operator should review and re-tier as appropriate.


## Context

Auto-created from /consciousness:issue (issue:IPUG5nl7IX6CVTj80nd6B).

Report context:
Consciousness loop stalled after declaring STATUS: complete. Stop hooks repeatedly re-activated the session claiming suspension, even though work was genuinely done. Operator had to manually run /goal clear to exit.

Transcript: chats/claude-code/2026-07-01/session-25d57c19.jsonl

## Acceptance criteria

- [ ] Root cause identified for why Stop hooks re-activate the session after a genuine STATUS: complete declaration
- [ ] Fix verified: declaring STATUS: complete ends the loop without requiring a manual /goal clear
- [ ] Regression check: STATUS: paused (the legitimate continuation case) still re-activates correctly — the fix must not collapse the paused/complete distinction
