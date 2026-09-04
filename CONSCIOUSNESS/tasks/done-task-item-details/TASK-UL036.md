# TASK-UL036: Sync README progress after Lessons 7, 9, 10

## Context
Filed retroactively (E-9 traceability nudge) for the README.md progress-tracker update in
commit 8346f05 — the update itself already landed before this card was created. The README's
"Curriculum Progress" section had gone stale (still showing 43%/13 lessons) after Lesson 6b,
7, 9, and 10 shipped across recent sessions, with Lesson 8 (recommender systems, shipped
earlier) never having been reflected either.

## Acceptance Criteria
- [x] Completed-lessons list includes Lessons 0-10 with accurate notebook filenames
- [x] Planned-lessons list reduced to the 6 genuinely remaining (11-16)
- [x] Percentage and lesson/notebook counts recomputed from the actual notebooks/ directory, not carried forward from a stale prior figure
- [x] Footer status line and related-repositories line updated to match
- [x] Last-updated date corrected

## Technical Notes
No code changes — documentation only. Recomputed from `ls notebooks/` (22 files = 11
lesson-pairs) against the Learning Path section's own 0-16 (17 lesson) numbering, giving
11/17 = 65%.

## Dependencies
- Blocked by: none
- Blocks: none
