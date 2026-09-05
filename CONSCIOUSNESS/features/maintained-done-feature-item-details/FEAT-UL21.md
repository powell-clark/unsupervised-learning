# FEAT-UL21: Hidden Markov Models and Unsupervised Sequence Learning Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p2

## Description
Lesson 23 of Unsupervised Learning Part II. Delivers a hidden Markov model lesson; the learner can discover latent regimes in sequential data without labels. Notebooks: 23a_hidden_markov_models_theory.ipynb, 23b_hidden_markov_models_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
All eleven verified by REVIEW-UL087 — an independent fresh-context opus review that read every code cell's source and printed output from the raw `.ipynb` JSON, independently re-executed both notebooks from clean copies with a byte-identical output diff (0 of 15 code cells differed), and independently re-derived every scrutinised numeric claim under a DIFFERENT algorithm (its own `scipy.special.logsumexp` log-space implementation, not the notebooks' Rabiner scale-factor recursion) rather than merely re-running the notebooks' own code.

- [x] **AC-1** — Theory notebook: Markov chains and the HMM generative model — 23a c4-c5, stationary distribution checked two ways (empirical `[0.4113, 0.3175, 0.2712]` from a 200,000-step simulation vs eigenvector `[0.4091, 0.3182, 0.2727]`); c6-c7, full generative model and Rabiner's three canonical problems
- [x] **AC-2** — Theory notebook: scaled forward-backward derived and implemented — 23a c8 derivation, c9 measures genuine underflow (naive alpha hits exactly 0.0 by T=250; reviewer independently found the first exact zero at T=238), c10 validated against a 729-path brute-force enumeration (`abs diff: 0.00e+00`)
- [x] **AC-3** — Theory notebook: Viterbi derived and implemented — 23a c11-c12, validated against brute force (`match: True, logprob diff: 0.00e+00`); c13 contrasts against posterior decoding
- [x] **AC-4** — Theory notebook: Baum-Welch from scratch recovering parameters of a simulated HMM — 23a c14-c15, means `[24.671, 14.837, 8.494]` vs true `[25.0, 15.0, 8.0]`; log-likelihood monotone non-decreasing across all 50 iterations (reviewer measured the minimum increment as `+2.244e-01`, zero decreasing steps)
- [x] **AC-5** — Theory notebook: model selection and pitfalls discussed — 23a c16-c17, local optima (6-restart spread of 32.776 log-lik units), label switching (two runs recovering identical regimes under permuted indices), training-likelihood non-decreasing in K past true K=3 (best-of-4-restarts, `-1719.681 → -1491.869`)
- [x] **AC-6** — Practical notebook: hmmlearn GaussianHMM matched against the from-scratch implementation — 23b c5, best-of-8-restarts matches 23a's from-scratch forward-backward to floating-point precision (`abs diff: 3.18e-12`) and Viterbi decoding identically; a single default fit (`random_state=0`) is shown collapsing to a degenerate solution first
- [x] **AC-7** — Practical notebook: regime detection case study with decoded regimes vs truth — 23b c7, volatility-clustering regimes (variance-only, not mean-shift), decoded accuracy `0.9783` via confusion-matrix-optimal label matching
- [x] **AC-8** — Practical notebook: n_components selection by held-out log-likelihood / BIC with restarts — 23b c9, best-of-4-restarts per K; BIC picks true K=3 exactly, held-out likelihood (genuinely, not cherry-picked — reviewer confirmed the K=4-over-K=3 margin is only 0.566) picks K=4; also caught and reported that `hmmlearn`'s `monitor_.converged` is `True` even at `n_iter=1` (verified against the installed library's own source)
- [x] **AC-9** — Practical notebook: multivariate case with covariance_type comparison — 23b c11, correlated 2-D emissions (true ρ=-0.7, measured empirical -0.650); `covariance_type='full'` beats `'diag'` by a BIC-confirmed margin (244.059)
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors; the Gibbs sampler bounded to a couple of minutes) — 23a 9/9, 23b 6/6 code cells, zero errors, byte-identical to the reviewer's independent re-execution. Initially NOT MET: 23b imported `hmmlearn` with no install guard, which would fail on a fresh Colab runtime (the only Part II notebook with this gap) — fixed with a `try`/`except ImportError` + `%pip install -q hmmlearn` fallback matching this repo's 6b precedent, and the fix was independently re-verified by the same reviewer (exit 0, output diff 0 of 6 cells) before this criterion was marked met
- [x] **AC-11** — Cross-lesson link: Baum-Welch framed as the lesson-21 EM recipe — 23a c14 states it explicitly and ties the M-step to lesson 4's GMM M-step and monotonicity to lesson 21's proof; verified accurate against the actual referenced notebooks

## Review history
1. **REVIEW-UL087** (agent, `verify-lesson-23`, opus, fresh context, 2026-09-05) — **agent-approved**. Initial verdict 10 of 11 MET (AC-10 not met: missing Colab install guard for `hmmlearn` in 23b). Also surfaced 10 secondary findings (F2-F11): an overclaim about a "byte-for-byte" reproduction of a function that was actually trimmed, a label-switching presentation defect that made an excellent 97.8%-accuracy fit look broken when printed in unpermuted order, and eight cosmetic issues (an imprecise float64 constant, three dead assignments, a latent off-by-one-prone filter, a prose/printed-number mismatch, a pre-existing repo-wide README claim out of scope for this lesson, and a figure-density observation). All nine actionable findings (F1-F3, F5-F9) fixed and re-verified — the reviewer independently re-executed the fixed 23b from a clean copy (exit 0, output diff 0 of 6 cells) before upgrading the verdict to ALL CRITERIA MET (11 of 11).

## Linked Entities
- Story: STORY-UL21
- Directive: DIRECT-UL20
- Tasks: TASK-UL063, TASK-UL064, TASK-UL065
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
