# TASK-UL26: Deep Unsupervised Learning Practical (12b)

## Context
Second notebook of Lesson 12 (STORY-UL13, DIRECT-UL12). Builds a convolutional (not
fully-connected) autoencoder better suited to image data, and extends it to denoising:
train on corrupted inputs, reconstruct the clean original.

## Acceptance Criteria
- [ ] Convolutional autoencoder architecture (Conv2d encoder, ConvTranspose2d decoder)
- [ ] Comparison against 12A's fully-connected autoencoder: parameter count, reconstruction quality
- [ ] Denoising: inject noise into inputs, train to reconstruct the clean original
- [ ] Visualization: noisy input, clean target, and denoised reconstruction side by side
- [ ] Quantitative comparison: denoising reconstruction error vs a naive (no-denoising) baseline
- [ ] Training dynamics comparison against the fully-connected models from 12A
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Builds directly on TASK-UL25's autoencoder and training loop. Convolutional layers exploit
spatial locality that a fully-connected layer discards (every pixel connects to every hidden
unit regardless of position) — expect fewer parameters and better reconstruction quality on
image data. Denoising autoencoders never optimize identity reconstruction (input equals
target); the noise-in, clean-out training signal is what prevents the trivial solution and
forces the bottleneck to learn genuinely useful structure.

## Dependencies
- Blocked by: TASK-UL25 (deep unsupervised learning theory)
- Blocks: none
- Story: STORY-UL13 (Deep-unsupervised-learning learner story)
- Directive: DIRECT-UL12 (Deep Unsupervised Learning (Autoencoders/VAE))
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
