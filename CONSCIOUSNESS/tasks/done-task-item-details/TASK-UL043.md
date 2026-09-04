# TASK-UL043: Extend Lesson 12 practical: latent interpolation, reconstruction-based anomaly detection, VAE-vs-GAN note

## Context

Discovered during TASK-UL041's independent review of FEAT-UL12 (Autoencoders
and Deep Unsupervised Learning). notebooks/12b_deep_unsupervised_practical.ipynb
covers the convolutional/denoising autoencoder track well, but three of
FEAT-UL12's acceptance criteria are genuinely unmet — confirmed by direct
keyword search of the raw notebook JSON, not just section-header matching:

- AC-9: Latent space interpolation and generation — zero mentions of
  "interpolat" anywhere in 12b; the theory notebook (12a) only name-drops
  the idea in its conclusion, no worked demonstration in either notebook.
- AC-10: Anomaly detection via reconstruction error — zero mentions of
  "anomaly" in 12b; the notebook's reconstruction-error work
  (`denoising-quantify`) measures denoising quality, not anomaly flagging.
- AC-12: VAE vs GAN conceptual comparison — zero mentions of "GAN" in
  either notebook.

This is the same pattern as FEAT-UL14's original gaps (TASK-UL034/UL040):
a feature's tasks were marked done, but independent review against the
actual notebook content found real, specific holes.

## Acceptance Criteria

- [x] Add a latent-space interpolation demo to 12b (walk between two
      encoded points in the trained autoencoder/VAE's latent space, decode
      intermediate points, show the generated images) — done using the
      fully-connected autoencoder's 32-dim latent space, 8-step linear
      interpolation between two digits, honest note about the plain
      autoencoder's latent space lacking a VAE's regularization
- [x] Add a reconstruction-error-based anomaly detection demo to 12b (train
      on normal data, show reconstruction error separates normal from
      anomalous inputs — e.g. one MNIST digit class held out as "anomalous") —
      done, with a genuine finding along the way: the naive "hold out digit 9"
      approach does NOT separate (0.99x, digits share too much structure);
      random noise separates massively (48x); occluded normal digits separate
      modestly (1.34x). Measured all three rather than reporting only the
      case that happened to work.
- [x] Add a short VAE-vs-GAN conceptual comparison (a markdown cell is
      sufficient — this course teaches VAEs, not GANs, so a brief
      contrast rather than a GAN implementation satisfies the criterion) —
      done as a comparison table (training signal, latent space, sample
      quality, stability, what you get "for free")
- [x] Re-execute 12b in place after the additions, verify zero errors —
      9/9 cells (grew from 7), zero errors
- [x] Update FEAT-UL12's AC-9/AC-10/AC-12 to [x] once demonstrated, citing
      the specific cells — done, all 13 criteria now met

## Dependencies

- Blocked by: none
- Blocks: none
- Discovered via: TASK-UL041, independent review of FEAT-UL12
