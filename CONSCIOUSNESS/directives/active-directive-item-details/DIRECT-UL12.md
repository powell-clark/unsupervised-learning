# DIRECT-UL12: Deep Unsupervised Learning (Autoencoders/VAE)

## Context

Autoencoders learn compressed latent representations through reconstruction. TASK-UL25 covers vanilla autoencoders, variational autoencoders (VAE), the ELBO loss, and the reparameterization trick. TASK-UL26 builds a convolutional denoising autoencoder in PyTorch.

## Acceptance Criteria

- [ ] TASK-UL25 (0a theory) complete — autoencoders, VAE framework, ELBO, reparameterization trick
- [ ] TASK-UL26 (0b practical) complete — PyTorch implementation, denoising AE, image generation
- [ ] Both notebooks run in Colab
- [ ] From-scratch PyTorch implementations verified
- [ ] FEAT-UL1 and FEAT-UL2 satisfied

## Technical Notes

Topics: encoder-decoder architecture, bottleneck layer, reconstruction loss, KL divergence, sampling from latent space. Application: image denoising, generation, representation learning.

## Dependencies

- Blocked by: DIRECT-UL1 (Clustering Foundations)
- Blocks: DIRECT-UL8 (Anomaly Detection — autoencoder approach)
