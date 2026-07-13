# FEAT-UL14: K-Means Clustering Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Comprehensive lesson on K-Means clustering: Lloyd's algorithm from first principles, K-Means++ initialization, elbow method, and silhouette analysis. Covers theory notebook deriving the algorithm alongside practical scikit-learn implementation with real data segmentation.

Renumbered from FEAT-UL2 (TASK-UL034) to resolve an ID collision with the
active cross-cutting FEAT-UL2 (dual NumPy/production implementation). An
independent agent review commissioned by TASK-UL034 found this feature's
original closure claim (TASK-UL3, TASK-UL4) did not hold: 3 of 11 criteria
were unmet in the shipped notebooks, and neither notebook carried any
execution evidence (`execution_count: null` on every cell) — see TASK-UL040
for the curriculum-wide finding. All three content gaps and the execution
gap have since been fixed directly under TASK-UL040 (soft K-Means section
added to 1a, elbow-method plot and an honest random-vs-k-means++ contrast
added to 1b, both notebooks executed in place with real outputs). Two
further real bugs were caught only because these notebooks had never
actually been run before: a matplotlib `boxplot(labels=...)` API removal in
1a, and an `x`/`y` scatter length mismatch discovered in the sibling 0a
notebook via the same process.

## Acceptance Criteria
- [x] Theory notebook: Lloyd's algorithm derivation (vector form, convergence proof)
- [x] Theory notebook: K-Means++ initialization (why it matters, implementation)
- [x] Theory notebook: soft K-Means and probabilistic interpretation — added: softmax responsibilities over negative squared distances, hard-K-means limit as β→∞, explicit connection to GMM's E-step
- [x] Practical notebook: scikit-learn KMeans usage and fit patterns
- [x] Practical notebook: Elbow method for choosing K — added: inertia-vs-K plot with automatic second-derivative elbow detection, contrasted against silhouette's choice (elbow=3 vs silhouette=2 on the RFM data — an honest disagreement, not hidden)
- [x] Practical notebook: Silhouette analysis for cluster validation
- [x] Practical notebook: Real data segmentation case study (e.g., customer clustering)
- [x] Both notebooks run end-to-end in Google Colab without local setup — verified via jupyter execute, 10/10 and 13/13 cells, zero errors, outputs committed in place
- [x] Theory notebook includes NumPy-only derivation
- [x] Practical notebook contrasts multiple initializations and their impact — added: random vs k-means++ on a 6-cluster dataset engineered to actually show the effect (random spread=248.1 vs k-means++ spread=3.0 across 50 seeds, 82.9x tighter)
- [x] Completed task pair: TASK-UL3 (theory) and TASK-UL4 (practical) — closure now genuinely verified against every criterion above, not assumed

## Status: agent-approved, awaiting human verdict (TASK-UL040)

All 11 criteria are now genuinely met, confirmed by a second independent
agent review (REVIEW-CCC067, machine-approved). The actual `approve` CLI's
resolved gate for this entity requires a human verdict to transition to
maintained/done — not the agent-only gate this card originally assumed from
reading the review-gates precept in isolation. Left in backlog pending
`approve FEAT-UL14 --as-human`, rather than force-closing past what the
live tooling actually enforces.

## Linked Entities
- Story: STORY-UL2 (K-Means learner story)
- Directive: DIRECT-UL2 (K-Means Clustering)
- Tasks: TASK-UL3, TASK-UL4
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
