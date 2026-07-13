# TASK-UL25: Deep Unsupervised Learning Theory (12a)

## Context
First notebook of Lesson 12 (STORY-UL13, DIRECT-UL12). Introduces autoencoders as a neural
generalization of PCA — a learned, nonlinear compression instead of a linear projection — then
extends to Variational Autoencoders (VAE), deriving the ELBO objective and the reparameterization
trick that makes it trainable by backpropagation.

## Acceptance Criteria
- [ ] Vanilla autoencoder: encoder-decoder architecture, bottleneck, reconstruction loss
- [ ] Connection to PCA: linear autoencoder recovers the PCA subspace
- [ ] Why a vanilla autoencoder's latent space isn't generative (no way to sample new, valid points)
- [ ] VAE generative story: latent prior, encoder outputs a distribution not a point
- [ ] ELBO derivation: reconstruction term plus KL-divergence regularization term
- [ ] The reparameterization trick: why direct sampling blocks backpropagation, and how it's fixed
- [ ] From-scratch PyTorch implementation of both a vanilla AE and a VAE
- [ ] Visualization: latent space structure, reconstruction quality, sampling from the VAE prior
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
A linear autoencoder (no nonlinearities, squared error loss) provably recovers the same subspace
as PCA (Lesson 5) — this is the natural bridge from a method already covered to a genuinely new
one. The VAE's key move is probabilistic: instead of encoding a point to one latent vector, it
encodes to a distribution (mean and variance), regularized toward a standard normal prior via
KL divergence, which is what makes the latent space fillable — you can sample a random prior
point and decode it into something plausible, unlike a vanilla AE's arbitrary, ungoverned latent
space.

## Dependencies
- Blocked by: TASK-UL2 (foundations groundwork)
- Blocks: TASK-UL26 (Autoencoders practical)
- Story: STORY-UL13 (Deep-unsupervised-learning learner story)
- Directive: DIRECT-UL12 (Deep Unsupervised Learning (Autoencoders/VAE))
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
