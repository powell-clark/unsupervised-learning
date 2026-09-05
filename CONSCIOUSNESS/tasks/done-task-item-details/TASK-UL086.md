# TASK-UL086: Fix lesson 28 capstone: honest K-selection rationale and report

## Context

TASK-UL079's independent review (REJECT verdict, agent-rejected on FEAT-UL26) found notebooks/28_capstone_pipeline.ipynb's cell 11 K-selection logic contradicts its own printed rationale: the code discards the gap statistic's K=5 pick and falls back to the stability tie's lowest member (K=3), while the print statement claims gap statistic was the deciding tool. Fix acceptance criteria are the exact unmet items from the review.

## Acceptance criteria

- [x] **D1 (HIGH)** — cell 11: `K_CHOSEN = gap_k` now unconditional (removed the fallback to `stab_pick[0]`), matching the existing rationale text exactly; disagreement between gap and stability is now reported as a LOWER-CONFIDENCE caveat rather than a silent override. Result: K_CHOSEN is now 5 (was 3), ARI-vs-true improved 0.226 -> 0.311 as a direct consequence
- [x] **D2 (MEDIUM)** — cell 16 Key Takeaway 6 restricted: "every K tested on the autoencoder representation, and from K=3 upward on raw and PCA", re-verified against cell 9's actual per-K guarded output (raw/PCA both non-degenerate at K=2, degenerate from K=3; autoencoder degenerate at every K 2-6)
- [x] **D3 (MEDIUM)** — cell 11: added a CAVEAT print after `km_final` computing the delivered partition's own smallest-cluster size against `MIN_CLUSTER_FRAC`; confirmed it fires (delivered K=5 partition's smallest cluster is 14 of 600, below the 30-point floor) and explains why the Section-4 guard doesn't extend to gap/stability K-selection
- [x] **D4 (MEDIUM)** — cell 11: `gap_statistic`/`stability_curve` docstrings rewritten to state the actual lineage: gap_statistic matches 27B's B/n_init reduction from 27A's originals (20->15, 10/5->5/3); stability_curve keeps 27A's n_resamples=15 but adopts 27B's n_init=3 and mean-only return
- [x] **D5 (MEDIUM)** — cell 13: dropped "never used to tune the thresholds above"; now states plainly that contamination=0.03 and the KDE quantile were both set to match the known synthetic injection rate, and that this is a demonstration simplification not available in real deployment (cross-referenced to the report's own not-done list)
- [x] **D6 (MEDIUM)** — cell 11 now computes `km_final_silhouette = silhouette_score(X_chosen, km_final.labels_)` directly; cell 15's report cites this (0.3832) for "the delivered partition's own silhouette", separately from the representation-choice-stage silhouette (0.426, a different K) which is now clearly labelled as such
- [x] **D7 (MEDIUM)** — resolved as a consequence of D1: since `K_CHOSEN` no longer ever falls back to a stability tie-break, there is no undocumented tie-break left to document; the code path D7 was about no longer exists
- [x] **D8 (LOW)** — cell 9: fixed a loop bug that skipped `best_rep` (exactly the case with the near-tie) when checking naive-vs-guarded silhouette near-ties; now prints "'PCA (3-d)' naive K=3 and guarded K=2 silhouettes differ by only 6.5e-05 ... no stated tie tolerance was applied here since it does not change which REPRESENTATION wins"
- [x] Re-executed via `jupyter nbconvert --execute`: 7/7 code cells, zero errors, zero null execution_count, zero `np.int64`/`np.float64`/`np.str_` repr leaks anywhere in the notebook; grepped the whole notebook for stale `K=3`/`K=4` references and fixed one found in cell 16 (a leftover "Section 5's K=3 pick" reference, corrected to K=5)
- [x] Re-run TASK-UL079's verification procedure (fresh-context opus subagent, independent): dispatched, verdict APPROVE. All 8 ACs confirmed met including AC-4 (round 1's blocker); D1-D13 all independently re-verified, including exhaustive branch-testing of the D1 fix logic across 8 synthetic gap/stability scenarios (0 mismatches) and independent re-derivation of every key number (K_CHOSEN=5, ARI-vs-true=0.311, km_final_silhouette=0.3832, D3's caveat arithmetic, D4's 27A/27B provenance)

## Round-2 review's own findings (N1-N4), fixed in the same pass before close
- [x] **N1 (MEDIUM, a regression I introduced in the D11/D12 fix)** — cell 7's added clause "its only role is keeping idx_fit disjoint from the points those statistics are later applied to" was FALSE (the transform is applied to all 600 rows, idx_fit included, so idx_fit is a subset of the transform targets, not disjoint from them) and contradicted cell 6's own correct markdown. Fixed: rationale now states plainly that fitting never sees idx_holdout, while the fitted transform is still applied to the full dataset including idx_holdout, since there is no separate validation evaluation step
- [x] **N2 (MEDIUM, pre-existing from round 1, caught live in round 2)** — the representation-choice winner (PCA over raw) was decided by a silhouette comparison across DIFFERENT metric spaces; independently confirmed `adjusted_rand_score(raw K=2 labels, PCA K=2 labels) = 1.000000` — the two representations' guarded winners are the IDENTICAL partition, scored differently only because silhouette depends on the space it's measured in. Fixed: cell 9 now computes this ARI directly and prints a CAVEAT when two viable representations share an identical winning partition; cell 16 Key Takeaway 2 rewritten to state this honestly rather than claim representation choice "measurably changed downstream clustering quality" (also caught and fixed my own bug in the first pass at this caveat: printed dimensionality as "3-d vs 3-d" instead of "3-d vs 7-d")
- [x] **N3 (LOW, pre-existing)** — cell 15's "Section 6 checks this directly below" was directionally backwards (Section 6/Anomalies precedes the report section); fixed to "Section 6 above checks this directly"
- [x] **N4 (LOW, pre-existing)** — cell 11's LOWER-CONFIDENCE framing and the delivered-partition floor violation weren't carried into cell 15's own Confidence line; fixed to state both explicitly there, not only via the softer "anomaly-driven artifact" flag

Re-executed after N1-N4: 7/7 code cells, zero errors, zero repr leaks, zero null execution_count.

## Optional polish (addressed in the same pass)

- [x] D9 (LOW) cell 15: alt-representations comparison now renders as prose ("raw 0.324; autoencoder (3-d) excluded (no non-degenerate K)") instead of a raw Python list-of-tuples repr
- [x] D10 (LOW) cell 13/15: precision now reported alongside recall (100.0% both-flagged, 81.8% either-flagged) in both cells
- [x] D11/D12 (LOW) cell 7: decision-log choice text changed from "80/20 internal fit/holdout split" to "80/20 internal fit/transform split", rationale now states plainly that `idx_holdout` is never separately evaluated against
- [x] D13 (LOW) cell 9: `min_cluster_frac=0.0` falsiness trap fixed — `if min_cluster_frac else 0` -> `if min_cluster_frac is not None else 0`

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
