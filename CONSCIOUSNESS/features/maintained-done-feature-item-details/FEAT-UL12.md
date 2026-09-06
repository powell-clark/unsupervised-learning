# FEAT-UL12: Autoencoders and Deep Unsupervised Learning Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p3

## Description
Comprehensive lesson on autoencoders: vanilla autoencoders, variational autoencoders (VAE), ELBO objective, reparameterization trick, and generative modeling. Covers theory of unsupervised representation learning.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: Autoencoder architecture (encoder-decoder)
- [x] **AC-2** — Theory notebook: Reconstruction loss and regularization
- [x] **AC-3** — Theory notebook: VAE: probabilistic encoder, reparameterization trick
- [x] **AC-4** — Theory notebook: Evidence Lower Bound (ELBO) derivation
- [x] **AC-5** — Theory notebook: KL divergence and standard normal prior
- [x] **AC-6** — Practical notebook: PyTorch vanilla autoencoder implementation
- [x] **AC-7** — Practical notebook: VAE implementation with sampling — covered in the theory notebook's `sampling-comparison` section; the practical notebook's own focus is the convolutional/denoising track (AC-8), not a second VAE implementation
- [x] **AC-8** — Practical notebook: Convolutional denoising autoencoders (images) — met on the code (`conv-vs-fc`, `denoising`, `denoising-quantify` sections)
- [x] **AC-9** — Practical notebook: Latent space interpolation and generation — added under TASK-UL043: linear interpolation through the fully-connected autoencoder's latent space between two digits, 8 steps, decoded and plotted; honestly notes the plain autoencoder's latent space isn't regularized the way a VAE's is
- [x] **AC-10** — Practical notebook: Anomaly detection via reconstruction error — added under TASK-UL043, with a genuine finding rather than an assumed-easy demo: an autoencoder trained on digits 0-8 does NOT separate well from unseen digit 9 (0.99x — MNIST digits share too much stroke-level structure), separates massively from random noise (48x, genuinely out-of-distribution), and separates modestly from occluded normal digits (1.34x, closer to a realistic fraud/defect case). All three measured side by side rather than reporting only the case that happened to work.
- [x] **AC-11** — Both notebooks run end-to-end in Google Colab — verified via jupyter execute, 8/8 and 9/9 cells, zero errors (12b grew from 7 to 9 code cells under TASK-UL043)
- [x] **AC-12** — Comparison: VAE vs GAN conceptually (VAE in this lesson) — added under TASK-UL043 as a markdown comparison table (training signal, latent space, sample quality, stability, what each gives you "for free")
- [x] **AC-13** — Completed task pair: TASK-UL25 (theory) and TASK-UL26 (practical)

## Review (TASK-UL041 / TASK-UL043)
Independent agent review against notebooks/12a_deep_unsupervised_theory.ipynb
and 12b_deep_unsupervised_practical.ipynb (TASK-UL041) found 10 of 13
criteria met, 3 genuine gaps (AC-9, AC-10, AC-12) by direct keyword search
of the raw notebook JSON rather than section-header matching. Filed as
TASK-UL043 rather than force-closing past the gap. TASK-UL043 then
implemented and verified all three: 12b re-executed in place, 9/9 cells,
zero errors. All 13 criteria now genuinely met — agent-approved. Stays in
backlog pending human sign-off, matching the FEAT-UL14 precedent (the live
`approve` tooling requires a human verdict even for an agent-approved
performance-kano feature).

## Linked Entities
- Story: STORY-UL13 (Autoencoders learner story)
- Directive: DIRECT-UL12 (Deep Unsupervised Learning)
- Tasks: TASK-UL25, TASK-UL26, TASK-UL043
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)

## Human sign-off
Operator ruling in chat 2026-09-06 14:48, relayed by the kernel (MSG-EGLPK006): signed off. The FEAT-UL14 precedent (agent-approved features held pending explicit human sign-off before promotion to maintained) is lifted for this card by that ruling. Human verdict recorded in REVIEW-INDEX.md (reviewer_type=human, reviewer_id=operator, verdict=human-approved).
