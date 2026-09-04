# Unsupervised Learning — Part II: Advanced Topics

Planned by Fable 5.1 on 2026-09-04. Built and verified autonomously by a consciousness session; no human gates.

## Why these twelve
The identity-vision-mission promises clustering, dimensionality reduction, **density estimation** and **representation learning** from first principles. Part I covered the first two thoroughly and only the GMM and autoencoder corners of the last two. Part II fills that: nonparametric density (18), exact-likelihood and diffusion models (19), the factorisation family beyond PCA (20), the general inference machinery behind every mixture model (21, 22), sequences (23, 24), representations from co-occurrence and from invariance (25, 26), the validation discipline a practitioner needs (27), and a capstone (28). Lesson 17 (spectral) closes the one clustering paradigm Part I skipped.

## Lessons

| # | Lesson | Notebooks | Directive / Story / Feature | Tasks (a, b, verify) | Status |
|---|---|---|---|---|---|
| 17 | Spectral Clustering and Graph Laplacians | 17a_spectral_clustering_theory.ipynb, 17b_spectral_clustering_practical.ipynb | DIRECT-UL14 / STORY-UL15 / FEAT-UL15 | TASK-UL045, TASK-UL046, TASK-UL047 | planned |
| 18 | Kernel Density Estimation and Nonparametric Density | 18a_kernel_density_estimation_theory.ipynb, 18b_kernel_density_estimation_practical.ipynb | DIRECT-UL15 / STORY-UL16 / FEAT-UL16 | TASK-UL048, TASK-UL049, TASK-UL050 | planned |
| 19 | Normalizing Flows and Modern Density Models | 19a_normalizing_flows_theory.ipynb, 19b_normalizing_flows_practical.ipynb | DIRECT-UL16 / STORY-UL17 / FEAT-UL17 | TASK-UL051, TASK-UL052, TASK-UL053 | planned |
| 20 | Matrix Factorisation Family: NMF and ICA | 20a_nmf_ica_theory.ipynb, 20b_nmf_ica_practical.ipynb | DIRECT-UL17 / STORY-UL18 / FEAT-UL18 | TASK-UL054, TASK-UL055, TASK-UL056 | planned |
| 21 | Expectation-Maximisation and Variational Inference | 21a_em_variational_inference_theory.ipynb, 21b_em_variational_inference_practical.ipynb | DIRECT-UL18 / STORY-UL19 / FEAT-UL19 | TASK-UL057, TASK-UL058, TASK-UL059 | planned |
| 22 | Bayesian Nonparametric Clustering: Dirichlet Process Mixtures | 22a_dirichlet_process_mixtures_theory.ipynb, 22b_dirichlet_process_mixtures_practical.ipynb | DIRECT-UL19 / STORY-UL20 / FEAT-UL20 | TASK-UL060, TASK-UL061, TASK-UL062 | planned |
| 23 | Hidden Markov Models and Unsupervised Sequence Learning | 23a_hidden_markov_models_theory.ipynb, 23b_hidden_markov_models_practical.ipynb | DIRECT-UL20 / STORY-UL21 / FEAT-UL21 | TASK-UL063, TASK-UL064, TASK-UL065 | planned |
| 24 | Time-Series Clustering and Dynamic Time Warping | 24a_time_series_clustering_theory.ipynb, 24b_time_series_clustering_practical.ipynb | DIRECT-UL21 / STORY-UL22 / FEAT-UL22 | TASK-UL066, TASK-UL067, TASK-UL068 | planned |
| 25 | Word and Item Embeddings: word2vec and Skip-Gram with Negative Sampling | 25a_word_embeddings_theory.ipynb, 25b_word_embeddings_practical.ipynb | DIRECT-UL22 / STORY-UL23 / FEAT-UL23 | TASK-UL069, TASK-UL070, TASK-UL071 | planned |
| 26 | Self-Supervised Contrastive Representation Learning | 26a_contrastive_learning_theory.ipynb, 26b_contrastive_learning_practical.ipynb | DIRECT-UL23 / STORY-UL24 / FEAT-UL24 | TASK-UL072, TASK-UL073, TASK-UL074 | planned |
| 27 | Clustering Stability, Consensus and Choosing K Honestly | 27a_clustering_stability_theory.ipynb, 27b_clustering_stability_practical.ipynb | DIRECT-UL24 / STORY-UL25 / FEAT-UL25 | TASK-UL075, TASK-UL076, TASK-UL077 | planned |
| 28 | Capstone: An End-to-End Unsupervised Analysis | 28_capstone_pipeline.ipynb | DIRECT-UL25 / STORY-UL26 / FEAT-UL26 | TASK-UL078, TASK-UL079 | planned |

Environment task: TASK-UL044. Corpus close-out (after all verifications): TASK-UL080.

## How it runs
- Every lesson is three tasks: build theory (a), build practical (b, blocked by a), verify (blocked by both). Lesson 28 is one build plus verify.
- Build tasks carry the full notebook plan on their cards. The house pattern is Part I's: derivation → from-scratch NumPy/PyTorch → production library → agreement check → honest conclusion. No network downloads anywhere.
- Verification tasks execute the notebooks, then dispatch a **fresh-context opus subagent** to judge every acceptance criterion from the raw notebook JSON (the FEAT-UL12 lesson: headers are not evidence). Approval closes feature → story → directive. Rejection files one fix task with the exact gaps and leaves the feature open.
- Review gate: features are kano `performance` → agent gate, one review, no human verdict (`review_gates.entity_overrides` in config.json makes this explicit).
- Models: the executing session builds (sonnet recommended: cheaper, and the four hardest theory notebooks — 19a, 21a, 22a, 26a — instruct the builder to draft their derivations through an opus subagent); opus reviews. Builder and reviewer are always different models.

## Launch (one command, from the repo root)
```
claude --bg --model sonnet --permission-mode bypassPermissions "/consciousness:on"
```
Then `claude agents` to watch, `claude logs <id>` to read, `claude stop <id>` to halt. The loop pauses itself (`STATUS: paused`) when nothing claimable remains; `cat .claude/loop-exit.*.json` says why.

## Environment

Verified by TASK-UL044 on 2026-09-04 (Python 3.12.8):

| Package | Version | Note |
|---|---|---|
| hmmlearn | 0.3.3 | `GaussianHMM(n_components=2).fit()` on simulated 2-regime data recovers means [-0.02, 4.87] and uses both states — lesson 23 is unblocked |
| tslearn | 0.9.0 | `TimeSeriesKMeans(metric="dtw")` fits; `CachedDatasets().load_dataset("Trace")` returns (100, 275, 1) with 4 classes **offline** — the dataset ships inside the package, so lesson 24b uses it directly and the synthetic fallback named on its card is not needed |

Everything else Part II needs (numpy, scipy, scikit-learn 1.9.0, torch 2.13.0, gensim 4.4.0, networkx 3.6.1, matplotlib, seaborn) was already installed for Part I. No lesson requires a network download at runtime.
