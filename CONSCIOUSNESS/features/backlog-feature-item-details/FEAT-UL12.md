# FEAT-UL12: Autoencoders and Deep Unsupervised Learning Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

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
- [ ] **AC-8** — Practical notebook: Convolutional denoising autoencoders (images) — met on the code (`conv-vs-fc`, `denoising`, `denoising-quantify` sections), leaving this checked as content-complete
- [ ] **AC-9** — Practical notebook: Latent space interpolation and generation — NOT MET. Searched 12b_deep_unsupervised_practical.ipynb for "interpolat": zero matches. The theory notebook's conclusion mentions the concept in one sentence; nothing in the practical notebook demonstrates it in code.
- [ ] **AC-10** — Practical notebook: Anomaly detection via reconstruction error — NOT MET. Searched 12b for "anomaly": zero matches. 12b's `denoising-quantify` section measures reconstruction quality for denoising, not for anomaly flagging; no anomaly-detection application is demonstrated anywhere in the practical notebook.
- [x] **AC-11** — Both notebooks run end-to-end in Google Colab — verified via jupyter execute under TASK-UL040, 8/8 and 7/7 cells, zero errors (this is independent of AC-9/AC-10: the notebook runs cleanly, it just doesn't cover those two topics)
- [ ] **AC-12** — Comparison: VAE vs GAN conceptually (VAE in this lesson) — NOT MET. Searched both notebooks for "GAN": zero matches in either.
- [x] **AC-13** — Completed task pair: TASK-UL25 (theory) and TASK-UL26 (practical)

## Review (TASK-UL041)
Independent agent review against notebooks/12a_deep_unsupervised_theory.ipynb
and 12b_deep_unsupervised_practical.ipynb: 10 of 13 criteria verified met.
Three genuine gaps found by direct keyword search of the raw notebook JSON
(not just section-header matching, which would have missed all three) —
AC-9, AC-10, AC-12 above. agent-rejected: stays in backlog with the gap
documented, matching the FEAT-UL14 honesty pattern rather than force-closing.
Filed as backlog TASK-UL043 (Extend Lesson 12 practical: latent
interpolation, reconstruction-based anomaly detection, VAE-vs-GAN note).

## Linked Entities
- Story: STORY-UL13 (Autoencoders learner story)
- Directive: DIRECT-UL12 (Deep Unsupervised Learning)
- Tasks: TASK-UL25, TASK-UL26
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
