# STORY-UL28: Currency Refresh Cadence

As a maintainer I want a bounded, recurring refresh cadence for the corpus so that library
versions, datasets, and notebook execution stay current without the corpus silently rotting
between the operator's visits.

## Acceptance Criteria

- [ ] A refresh cadence is defined and stated on this card (e.g. quarterly, or triggered by
      a named library's major-version bump) — bounded, not "whenever", so it does not
      become an excuse to run the full sweep every session
- [ ] Each refresh checks: `pip install -r requirements.txt` for version drift, a full
      `jupyter nbconvert --execute` sweep across every notebook (the TASK-UL040/TASK-UL080
      pattern), and whether any bundled dataset (sklearn, gensim, tslearn) has changed
      shape upstream
- [ ] A refresh that finds drift files exactly the fix tasks needed, scoped to what
      actually broke — never a blanket "re-verify everything" task
- [ ] The cadence and its last-run date are recorded somewhere durable (this card, or a
      dedicated `CONSCIOUSNESS/artifacts/currency-log.md`) so the NEXT session can tell at
      a glance whether a refresh is due

## Linked Entities

- Directive: DIRECT-UL26 (Maintain the curriculum as a living Feynman-style corpus)
- Tasks: none filed yet — the first refresh task is filed when the cadence next falls due
