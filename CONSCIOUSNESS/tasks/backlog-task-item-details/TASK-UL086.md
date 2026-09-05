# TASK-UL086: Fix lesson 28 capstone: honest K-selection rationale and report

## Context

TASK-UL079's independent review (REJECT verdict, agent-rejected on FEAT-UL26) found notebooks/28_capstone_pipeline.ipynb's cell 11 K-selection logic contradicts its own printed rationale: the code discards the gap statistic's K=5 pick and falls back to the stability tie's lowest member (K=3), while the print statement claims gap statistic was the deciding tool. Fix acceptance criteria are the exact unmet items from the review.

## Acceptance criteria

- [ ] **D1 (HIGH)** — cell 11: make the code and the printed rationale agree. Either make `K_CHOSEN` always follow `gap_k` (matching the existing text "gap statistic used as the deciding tool"), or change the text to honestly state that the stability tie's lowest member was taken instead, and say why (tie-break rule, D7)
- [ ] **D2 (MEDIUM)** — cell 16: restrict the "the same near-empty anomaly-isolating cluster showed up at every K tested, on every representation compared" claim — cell 9's own guarded output shows this is true for every K (2-6) only on the autoencoder representation; raw and PCA only show it from K=3 upward, not at K=2
- [ ] **D3 (MEDIUM)** — cell 11/15: disclose that the delivered K-selection (gap+stability, unguarded) can still land on a K whose smallest cluster falls below the same MIN_CLUSTER_FRAC floor applied in cell 9 to representation choice (the delivered K=3 partition's smallest cluster is 14 of 600, below the 30-point/5% floor) — the guard does not currently extend past representation choice
- [ ] **D4 (MEDIUM)** — cell 11: correct the `gap_statistic`/`stability_curve` docstrings — they claim "Reused from 27A" but the code is actually adapted with reduced budgets (e.g. `B`, `n_init`, `n_resamples`); state the actual parameter differences honestly, matching the standard 27B set
- [ ] **D5 (MEDIUM)** — cell 13/15: drop or qualify the "never used to tune the thresholds above" claim — `IsolationForest(contamination=0.03)` and the KDE 0.03 density quantile are both set to match the known synthetic anomaly rate exactly, so the reported recall numbers are partly circular; state this honestly
- [ ] **D6 (MEDIUM)** — cell 15: report the delivered K_CHOSEN partition's own silhouette (computed directly from `km_final`), not `rep_results[best_rep][0]` (which is the representation-choice stage's own guarded-K silhouette, from a different K)
- [ ] **D7 (MEDIUM)** — cell 11: document the tie-break rationale when the stability curve reports multiple tied K's (why the lowest tied K is taken)
- [ ] **D8 (LOW)** — cell 9: the naive and guarded searches can report the same rounded silhouette at two different K's when the true values are nearly tied (observed: PCA naive K=3 0.425639 vs guarded K=2 0.425574, differ by 6.5e-5, both display as 0.4256); apply a stated tie tolerance or note the near-tie explicitly
- [ ] Re-run TASK-UL079's verification procedure (fresh-context opus subagent, independent) and, on approval, perform FEAT-UL26's close step (feature to maintained, story to fulfilled, directive to done)

## Optional polish (not blocking approval, address if convenient)

- D9 (LOW) cell 15: the alt-representations comparison prints a raw Python list-of-tuples repr into stakeholder-facing report text; render it as prose instead
- D10 (LOW) cell 13: report per-method anomaly precision (measured: both 100.0%, either 81.8%) alongside recall, since the flagged counts (18/18) are largely restating the input contamination/quantile parameters rather than a finding
- D11/D12 (LOW) cell 7: `idx_holdout` is assigned but never evaluated against anything; either use it for a genuine holdout check or soften the "fit/holdout split" framing so it does not imply a validation role that does not exist
- D13 (LOW) cell 9: `min_cluster_frac=0.0` is treated as "no guard" via Python falsiness rather than an explicit `is None` check — harmless today, a trap on future edits

## Dependencies

- Directive: DIRECT-UL25
- Story: STORY-UL26
- Features: FEAT-UL26

## Pre-mortem

### Failure modes

- Fixing D1 by forcing `K_CHOSEN = gap_k` changes the final K from 3 to 5 and every downstream number in cells 11/15/16 that cites K=3, sizes, or ARI-vs-true — re-execute the whole notebook after the fix and re-check every printed number for staleness, the same class of bug (D6) that caused this rejection
- D2's wording fix must be re-verified against cell 9's actual per-K output for all three representations, not assumed from memory

### Weak assumptions

- Assuming the "gap statistic as deciding tool" design intent (per the ORIGINAL print text) is the correct one to restore, rather than "stability tie as decider" — re-read cell 10's markdown framing before choosing which side of D1 to fix; do not pick the side that is merely less code to change
