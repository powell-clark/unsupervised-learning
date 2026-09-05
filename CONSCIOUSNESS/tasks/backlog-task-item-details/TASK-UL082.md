# TASK-UL082: Stream fragment files deleted from working tree while tracked

## Context

Between commits 10f1e1a and 6204fb5 something outside git removed CONSCIOUSNESS/stream/review-verdicts/ul-5521042d.main.jsonl and CONSCIOUSNESS/stream/task-events/ul-5521042d.main.jsonl from the working tree (both dirs left empty, mtime 02:21). Neither path is in .gitignore, so both were tracked, and the next 'git add -A CONSCIOUSNESS/' committed the deletion as though it were intended. No audit content was lost this time — both verdict rows were duplicated in REVIEW-INDEX.md as REVIEW-UL063 and REVIEW-UL064, and the files were restored from 10f1e1a — but the next occurrence could silently drop fragments that have no canonical counterpart. Decide which surface is authoritative in this consumer repo: either gitignore the fragment dirs (matching the data--stream_exhaust_untracked policy that e440dc7 applied to the other stream files) or stop whatever is deleting them. Also worth resolving: this repo's project-local review-gates rule mandates direct PSV appends to REVIEW-INDEX.md while the released plugin's precept mandates id-less fragments folded by a compactor that does not run here, so verdicts are currently written to both by hand.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- _(to be filled in)_

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
