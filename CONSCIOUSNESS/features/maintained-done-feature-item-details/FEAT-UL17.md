# FEAT-UL17: Normalizing Flows and Modern Density Models Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p2

## Description
Lesson 19 of Unsupervised Learning Part II. Delivers a normalizing-flows lesson; the learner can build a generative model with an exact likelihood and understand how it differs from VAEs, GANs and diffusion models. Notebooks: 19a_normalizing_flows_theory.ipynb, 19b_normalizing_flows_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then a production-library comparison (scipy in 19a, sklearn KDE/IsolationForest/LOF in 19b), all Colab-runnable with committed execution outputs.

## Acceptance Criteria
All ten verified by REVIEW-UL071 — an independent fresh-context opus review that read every code cell's source and printed output from the raw `.ipynb` JSON, plus a fresh re-execution at OMP_NUM_THREADS=2 to approximate a 2-core Colab CPU.

- [x] **AC-1** — Theory notebook: change-of-variables derivation with worked examples — 19a c4 derives $p_x(x)=p_z(f(x))|\det J_f(x)|$; c5 checks the 1-D example to 2.220e-16 against scipy lognorm and the 2-D linear-map example to 1.776e-15 against the exact Gaussian, plus a deliberate no-Jacobian counterexample that fails to integrate to 1
- [x] **AC-2** — Theory notebook: affine coupling layer construction with the triangular-Jacobian argument — 19a c7 derives the block-triangular Jacobian and $\log|\det J|=\sum_i s_i(x_A)$; c8 verifies invertibility to 6.661e-16, log-det agreement (analytic vs autograd slogdet) to 6.661e-16, and triangularity exactly 0, plus an O(D) vs O(D³) cost table
- [x] **AC-3** — Theory notebook: exact likelihood vs ELBO comparison — 19a c9 states the ELBO, identifies the gap as the uncomputable $D_{KL}(q(z|x)\|p(z|x))$, and gives a 7-row comparison table
- [x] **AC-4** — Theory notebook: from-scratch PyTorch flow trained on 2D data with density contours and samples — 19a c12 trains a 4-coupling flow on `make_moons` (NLL 2.8379 → 1.5946), round trip 1.110e-15, density integrates to 0.9968, contour + sample figure
- [x] **AC-5** — Practical notebook: deeper RealNVP compared against KDE on the same data — 19b c5 (6 layers, hidden 128, 3000 points): NLL 2.8306 → 1.6409, round trip 2.22e-15; held-out log-likelihood on 600 unseen points — flow -1.7565 vs CV-tuned KDE -1.6745 — reported honestly as the flow losing to KDE
- [x] **AC-6** — Practical notebook: minimal from-scratch DDPM on 2D data with forward process, noise predictor and sampling — 19b c6-7 verifies the noise schedule numerically before training (`alpha_bar_T = 0.000004`, closed-form-vs-simulated max diffs 0.0336/0.0213); c8 trains a `NoisePredictor` MLP (MSE 0.4561 → 0.2441) and ancestral-samples over T=40, with a memorisation check (ratio 2.15)
- [x] **AC-7** — Practical notebook: VAE / flow / diffusion / GAN comparison table grounded in the lesson's own models — 19b c12 reads live variables from the trained VAE/flow/diffusion (not hardcoded), GAN row explicitly marked not implemented rather than fabricated
- [x] **AC-8** — Practical notebook: flow log-density used as an anomaly score — 19b c14 scores `flow.log_prob` by `average_precision_score` against KDE (Lesson 18), Isolation Forest and LOF (Lesson 7), and a 60-draw random baseline
- [x] **AC-9** — Both notebooks run end-to-end in Google Colab on CPU — every code cell non-null `execution_count` (19a 5/5, 19b 7/7), zero error outputs, zero stderr, zero network/file-IO/`.cuda()` calls; reviewer's independent re-execution: 19a 41.41s, 19b 107.53s, both exit 0, fresh outputs byte-identical to committed
- [x] **AC-10** — Cross-lesson link: builds explicitly on lesson 12a (VAE/ELBO) and lesson 18 (KDE) — checked for accuracy, not just presence: 19b's citation of 18b's Isolation Forest result is exact (0.0367 vs 0.0606 random baseline), its citation of 18b's KDE collapse correctly names the controlled Experiment 2 rather than the confounded Experiment 1, and 19b's VAE section reuses lesson 12a's architecture with the correct latent dimension (2, corrected from an initial factual error — see Review history)

## Review history
1. **REVIEW-UL071** (agent, `verify-lesson-19`, opus, fresh context, 2026-09-05) — **agent-approved**. All 10 criteria met with cell-index evidence, including an independent re-execution of both notebooks confirming byte-identical outputs. Raised three findings, all fixed before this verdict was recorded (commit bc3bef4): a factual error repeated in both notebooks (Lesson 12A's VAE latent dimension misstated as 20, actually 2), an anomaly-detection framing overclaim in 19b now replaced with a measured overlap percentage, and a cosmetic table-formatting collision.

## Linked Entities
- Story: STORY-UL17
- Directive: DIRECT-UL16
- Tasks: TASK-UL051, TASK-UL052, TASK-UL053
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
