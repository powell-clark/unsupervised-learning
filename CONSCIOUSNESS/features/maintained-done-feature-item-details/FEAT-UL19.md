# FEAT-UL19: Expectation-Maximisation and Variational Inference Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p2

## Description
Lesson 21 of Unsupervised Learning Part II. Delivers a general EM and variational inference lesson; the learner can derive inference for a new latent-variable model rather than only apply the GMM special case. Notebooks: 21a_em_variational_inference_theory.ipynb, 21b_em_variational_inference_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
All eleven verified by REVIEW-UL079 — an independent fresh-context opus review that read every code cell's source and printed output from the raw `.ipynb` JSON, plus an independent re-execution of both notebooks. 21a additionally passed a separate, dedicated adversarial math review (REVIEW-UL077's builder note) before this feature-level review.

- [x] **AC-1** — Theory notebook: ELBO derivation via Jensen and EM as coordinate ascent stated generally — 21a c4 derives the Jensen bound and exact KL-gap identity; c5 verifies numerically (arbitrary q -17.385 vs exact -7.948; posterior-q gap 8.88e-16; KL direct == via-identity at 9.437118)
- [x] **AC-2** — Theory notebook: mixture-of-Bernoullis EM from scratch with learned prototypes — 21a c6-7, ground-truth recovery 0.0261, digit prototype grid plotted
- [x] **AC-3** — Theory notebook: missing-data Gaussian EM from scratch with an imputation-error curve — 21a c8-9, error-vs-missingness curve, C_i ablation isolating 2.17x (correction) from a further 1.37x (marginal vs conditional imputation)
- [x] **AC-4** — Theory notebook: mean-field VI and the CAVI update derived — 21a c12-13, $q_j^\star \propto \exp\mathbb{E}_{-j}[\log p]$ derived and the reverse/forward-KL mode-seeking contrast demonstrated
- [x] **AC-5** — Theory notebook: from-scratch CAVI for a Bayesian GMM with an ELBO monotonicity plot — 21a c14-15, min step-to-step ELBO change -9.095e-13 (none), pruning to 3 effective components matching K_true
- [x] **AC-6** — Practical notebook: sklearn BayesianGaussianMixture with prior sweeps and effective-components analysis — 21b c5,c7,c13, cross-checked against 21A's from-scratch CAVI (both prune to 4 effective components on identical data)
- [x] **AC-7** — Practical notebook: BIC vs variational K selection compared on the same data — 21b c9, BIC argmin K=4 matches variational effective K=4, reviewer independently reproduced the BIC values exactly
- [x] **AC-8** — Practical notebook: convergence diagnostics explained — 21b c10-11, converged_/n_iter_/lower_bound_ demonstrated with a deliberately starved fit, plus a genuine local-optima demonstration (masked by sklearn's default k-means++ init, restored with init_params='random') independently reproduced by the reviewer
- [x] **AC-9** — Practical notebook: real-data case (wine) with interpretation — 21b c12-13, standardised load_wine, prior-strength sweep showing NO pruning occurs on this data, per-cluster purity reported with its full spread (mean 87.8%, worst cluster 55%) after the reviewer found the initial "each cluster is clean" framing masked that spread
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors) — 21a 7/7, 21b 7/7 code cells, independently re-executed by the reviewer with exit 0 and a clean git diff
- [x] **AC-11** — Cross-lesson link: lesson 4 (GMM EM) is the special case; lesson 12a (ELBO) is the same bound — verified accurate against both notebooks' actual content, not just presence: 12a's ELBO decomposition matches 21a's claimed identity exactly

## Review history
1. **REVIEW-UL079** (agent, `verify-lesson-21`, opus, fresh context, 2026-09-05) — **agent-approved**. All 11 criteria met with cell-index evidence and an independent re-execution. Flagged one finding: the wine section's mean per-cluster purity (87.8%) masked a real spread (2 of 8 clusters at only ~55% purity), fixed before this verdict was recorded.
2. 21a separately passed a dedicated adversarial math review (`mathcheck-21a`, opus, fresh context) before this feature-level review — 7 issues found and fixed (an overclaim, an M-step formula-vs-code mismatch, an over-attribution, a noisy single-draw measurement, a substantive ELBO computation bug, a follow-up robustness overclaim caught by the reviewer's own re-verification, and a mis-attributed prior).

## Linked Entities
- Story: STORY-UL19
- Directive: DIRECT-UL18
- Tasks: TASK-UL057, TASK-UL058, TASK-UL059
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
