# Unsupervised Machine Learning

A university-grade curriculum for unsupervised machine learning — clustering, dimensionality
reduction, anomaly detection, density estimation, latent-variable models and representation
learning. Every method is derived from first principles, implemented from scratch in NumPy, then
reproduced with scikit-learn, PyTorch or a specialist library. All notebooks run in Google Colab
with no local setup.

## The series

Four repositories, one curriculum. The first three are *how* a model learns; the fourth is *what*
it is built from, and cuts across all three.

- [Supervised learning](https://github.com/powell-clark/supervised-learning) — learning from labelled examples
- **[Unsupervised learning](https://github.com/powell-clark/unsupervised-learning)** — finding structure with no labels (you are here)
- [Reinforcement learning](https://github.com/powell-clark/reinforcement-learning) — learning from reward
- [Deep learning & transformers](https://github.com/powell-clark/deep-learning) — the architecture the other three can each be built on

**Status:** 29 of 29 lessons complete (53 notebooks)

## Overview

- **From First Principles**: every algorithm derived from foundations, not quoted
- **Dual Structure**: theory (a) + practical (b) notebooks for each lesson
- **Story-Driven**: a real-world motivation before the mathematics
- **Complete Implementations**: from-scratch NumPy, then production libraries
- **Google Colab Compatible**: runs in the browser, no local setup
- **Two Parts**: Part I (Lessons 0–16) covers the core methods and professional practice;
  Part II (Lessons 17–28) extends into density estimation, inference, sequences, representation
  learning and a capstone

## Lesson catalog

#### Foundations

- **Lesson 0**: Clustering Foundations and Evaluation
  - [`0a_clustering_foundations_theory.ipynb`](notebooks/0a_clustering_foundations_theory.ipynb) — what a cluster is, distance and similarity, and how to choose the number of clusters [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/0a_clustering_foundations_theory.ipynb)
  - [`0b_cluster_evaluation.ipynb`](notebooks/0b_cluster_evaluation.ipynb) — internal and external evaluation metrics, with silhouette analysis [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/0b_cluster_evaluation.ipynb)

#### Core Clustering Algorithms

- **Lesson 1**: K-Means Clustering
  - [`1a_kmeans_theory.ipynb`](notebooks/1a_kmeans_theory.ipynb) — Lloyd's algorithm, initialisation and convergence, derived and implemented from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/1a_kmeans_theory.ipynb)
  - [`1b_kmeans_practical.ipynb`](notebooks/1b_kmeans_practical.ipynb) — RFM customer segmentation, image compression and scalability [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/1b_kmeans_practical.ipynb)
- **Lesson 2**: Hierarchical Clustering
  - [`2a_hierarchical_theory.ipynb`](notebooks/2a_hierarchical_theory.ipynb) — the agglomerative algorithm and linkage methods [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/2a_hierarchical_theory.ipynb)
  - [`2b_hierarchical_practical.ipynb`](notebooks/2b_hierarchical_practical.ipynb) — dendrogram cutting and scalability analysis [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/2b_hierarchical_practical.ipynb)
- **Lesson 3**: DBSCAN
  - [`3a_dbscan_theory.ipynb`](notebooks/3a_dbscan_theory.ipynb) — epsilon-neighbourhoods and core, border and noise points [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/3a_dbscan_theory.ipynb)
  - [`3b_dbscan_practical.ipynb`](notebooks/3b_dbscan_practical.ipynb) — k-distance graphs for choosing epsilon, and an introduction to HDBSCAN [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/3b_dbscan_practical.ipynb)
- **Lesson 4**: Gaussian Mixture Models
  - [`4a_gmm_theory.ipynb`](notebooks/4a_gmm_theory.ipynb) — the EM algorithm, responsibilities and covariance types [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/4a_gmm_theory.ipynb)
  - [`4b_gmm_practical.ipynb`](notebooks/4b_gmm_practical.ipynb) — BIC/AIC model selection and image segmentation [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/4b_gmm_practical.ipynb)

#### Dimensionality Reduction

- **Lesson 5**: Principal Component Analysis
  - [`5a_pca_theory.ipynb`](notebooks/5a_pca_theory.ipynb) — eigendecomposition, the SVD and numerical stability [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/5a_pca_theory.ipynb)
  - [`5b_pca_practical.ipynb`](notebooks/5b_pca_practical.ipynb) — eigenfaces, kernel PCA and PCA as preprocessing [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/5b_pca_practical.ipynb)
- **Lesson 6**: Manifold Learning: t-SNE and UMAP
  - [`6a_manifold_learning_theory.ipynb`](notebooks/6a_manifold_learning_theory.ipynb) — t-SNE derived, UMAP, and the artefacts both can create [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/6a_manifold_learning_theory.ipynb)
  - [`6b_manifold_learning_practical.ipynb`](notebooks/6b_manifold_learning_practical.ipynb) — perplexity and UMAP parameter tuning, and detecting artefacts [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/6b_manifold_learning_practical.ipynb)

#### Specialised Methods

- **Lesson 7**: Anomaly Detection
  - [`7a_anomaly_detection_theory.ipynb`](notebooks/7a_anomaly_detection_theory.ipynb) — isolation-based, density-based and boundary-based methods from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/7a_anomaly_detection_theory.ipynb)
  - [`7b_anomaly_detection_practical.ipynb`](notebooks/7b_anomaly_detection_practical.ipynb) — fraud-style class imbalance, a PyTorch autoencoder and a PR-AUC comparison [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/7b_anomaly_detection_practical.ipynb)
- **Lesson 8**: Matrix Factorisation and Recommender Systems
  - [`8a_recommender_systems_theory.ipynb`](notebooks/8a_recommender_systems_theory.ipynb) — collaborative filtering and matrix factorisation [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/8a_recommender_systems_theory.ipynb)
  - [`8b_recommender_systems_practical.ipynb`](notebooks/8b_recommender_systems_practical.ipynb) — Surprise, Implicit and PyTorch implementations [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/8b_recommender_systems_practical.ipynb)
- **Lesson 9**: Association Rule Learning
  - [`9a_association_rules_theory.ipynb`](notebooks/9a_association_rules_theory.ipynb) — support, confidence and lift, and Apriori from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/9a_association_rules_theory.ipynb)
  - [`9b_association_rules_practical.ipynb`](notebooks/9b_association_rules_practical.ipynb) — mlxtend Apriori against FP-Growth, threshold trade-offs and ranked rules [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/9b_association_rules_practical.ipynb)

#### Advanced Topics

- **Lesson 10**: Topic Modelling
  - [`10a_topic_modeling_theory.ipynb`](notebooks/10a_topic_modeling_theory.ipynb) — the LDA generative model and collapsed Gibbs sampling from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/10a_topic_modeling_theory.ipynb)
  - [`10b_topic_modeling_practical.ipynb`](notebooks/10b_topic_modeling_practical.ipynb) — Gensim and scikit-learn, coherence-based choice of K, and pyLDAvis [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/10b_topic_modeling_practical.ipynb)
- **Lesson 11**: Self-Organising Maps
  - [`11a_self_organizing_maps_theory.ipynb`](notebooks/11a_self_organizing_maps_theory.ipynb) — best-matching units, neighbourhood decay and grid unfolding from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/11a_self_organizing_maps_theory.ipynb)
  - [`11b_self_organizing_maps_practical.ipynb`](notebooks/11b_self_organizing_maps_practical.ipynb) — MiniSom, the U-Matrix and component planes on the Wine dataset [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/11b_self_organizing_maps_practical.ipynb)
- **Lesson 12**: Deep Unsupervised Learning
  - [`12a_deep_unsupervised_theory.ipynb`](notebooks/12a_deep_unsupervised_theory.ipynb) — the autoencoder-PCA connection, the VAE, the ELBO and the reparameterisation trick [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/12a_deep_unsupervised_theory.ipynb)
  - [`12b_deep_unsupervised_practical.ipynb`](notebooks/12b_deep_unsupervised_practical.ipynb) — convolutional and denoising autoencoders in PyTorch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/12b_deep_unsupervised_practical.ipynb)

#### Professional Practice

- **Lesson 13**: Clustering Comparison Framework
  - [`13_clustering_comparison.ipynb`](notebooks/13_clustering_comparison.ipynb) — runtime and quality benchmarks across K-Means, hierarchical, DBSCAN and GMM, with sensitivity sweeps [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/13_clustering_comparison.ipynb)
- **Lesson 14**: Dimensionality Reduction Pipeline
  - [`14_dimensionality_reduction_pipeline.ipynb`](notebooks/14_dimensionality_reduction_pipeline.ipynb) — feature selection against PCA extraction, in leakage-safe pipelines [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/14_dimensionality_reduction_pipeline.ipynb)
- **Lesson 15**: Unsupervised Preprocessing
  - [`15_unsupervised_preprocessing.ipynb`](notebooks/15_unsupervised_preprocessing.ipynb) — scaling, encoding, distance metrics and imputation, each measured by downstream clustering quality [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/15_unsupervised_preprocessing.ipynb)
- **Lesson 16**: Semi-Supervised Learning
  - [`16_semi_supervised_learning.ipynb`](notebooks/16_semi_supervised_learning.ipynb) — label spreading, self-training and co-training from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/16_semi_supervised_learning.ipynb)

#### Part II: Density Estimation and Generative Models

- **Lesson 17**: Spectral Clustering and Graph Laplacians
  - [`17a_spectral_clustering_theory.ipynb`](notebooks/17a_spectral_clustering_theory.ipynb) — graph Laplacians, the eigengap heuristic and normalised cuts from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/17a_spectral_clustering_theory.ipynb)
  - [`17b_spectral_clustering_practical.ipynb`](notebooks/17b_spectral_clustering_practical.ipynb) — non-convex cluster shapes, affinity construction and scalability [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/17b_spectral_clustering_practical.ipynb)
- **Lesson 18**: Kernel Density Estimation
  - [`18a_kernel_density_estimation_theory.ipynb`](notebooks/18a_kernel_density_estimation_theory.ipynb) — KDE derived, bandwidth selection and the curse of dimensionality [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/18a_kernel_density_estimation_theory.ipynb)
  - [`18b_kernel_density_estimation_practical.ipynb`](notebooks/18b_kernel_density_estimation_practical.ipynb) — bandwidth cross-validation, multivariate KDE and anomaly scoring [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/18b_kernel_density_estimation_practical.ipynb)
- **Lesson 19**: Normalising Flows
  - [`19a_normalizing_flows_theory.ipynb`](notebooks/19a_normalizing_flows_theory.ipynb) — the change of variables, coupling layers and exact-likelihood flows from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/19a_normalizing_flows_theory.ipynb)
  - [`19b_normalizing_flows_practical.ipynb`](notebooks/19b_normalizing_flows_practical.ipynb) — flow-based density estimation trained and evaluated on real data [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/19b_normalizing_flows_practical.ipynb)

#### Part II: Factorisation and Inference

- **Lesson 20**: Matrix Factorisation: NMF and ICA
  - [`20a_nmf_ica_theory.ipynb`](notebooks/20a_nmf_ica_theory.ipynb) — non-negative matrix factorisation and independent component analysis, derived [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/20a_nmf_ica_theory.ipynb)
  - [`20b_nmf_ica_practical.ipynb`](notebooks/20b_nmf_ica_practical.ipynb) — topic extraction with NMF and blind source separation with ICA [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/20b_nmf_ica_practical.ipynb)
- **Lesson 21**: Expectation-Maximisation and Variational Inference
  - [`21a_em_variational_inference_theory.ipynb`](notebooks/21a_em_variational_inference_theory.ipynb) — general EM, the ELBO and mean-field variational inference [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/21a_em_variational_inference_theory.ipynb)
  - [`21b_em_variational_inference_practical.ipynb`](notebooks/21b_em_variational_inference_practical.ipynb) — EM for mixture models and variational inference in practice [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/21b_em_variational_inference_practical.ipynb)
- **Lesson 22**: Dirichlet Process Mixtures
  - [`22a_dirichlet_process_mixtures_theory.ipynb`](notebooks/22a_dirichlet_process_mixtures_theory.ipynb) — stick-breaking, the Chinese restaurant process and infinite mixtures from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/22a_dirichlet_process_mixtures_theory.ipynb)
  - [`22b_dirichlet_process_mixtures_practical.ipynb`](notebooks/22b_dirichlet_process_mixtures_practical.ipynb) — clustering without choosing K in advance [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/22b_dirichlet_process_mixtures_practical.ipynb)

#### Part II: Sequences and Representations

- **Lesson 23**: Hidden Markov Models
  - [`23a_hidden_markov_models_theory.ipynb`](notebooks/23a_hidden_markov_models_theory.ipynb) — forward-backward, Viterbi and Baum-Welch from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/23a_hidden_markov_models_theory.ipynb)
  - [`23b_hidden_markov_models_practical.ipynb`](notebooks/23b_hidden_markov_models_practical.ipynb) — regime detection with hmmlearn [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/23b_hidden_markov_models_practical.ipynb)
- **Lesson 24**: Time-Series Clustering and Dynamic Time Warping
  - [`24a_time_series_clustering_theory.ipynb`](notebooks/24a_time_series_clustering_theory.ipynb) — DTW derived, and time-series K-means from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/24a_time_series_clustering_theory.ipynb)
  - [`24b_time_series_clustering_practical.ipynb`](notebooks/24b_time_series_clustering_practical.ipynb) — DTW-based clustering with tslearn on real time series [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/24b_time_series_clustering_practical.ipynb)
- **Lesson 25**: Word Embeddings
  - [`25a_word_embeddings_theory.ipynb`](notebooks/25a_word_embeddings_theory.ipynb) — the skip-gram objective and negative sampling, derived from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/25a_word_embeddings_theory.ipynb)
  - [`25b_word_embeddings_practical.ipynb`](notebooks/25b_word_embeddings_practical.ipynb) — gensim word2vec, analogies and similarity in embedding space [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/25b_word_embeddings_practical.ipynb)
- **Lesson 26**: Contrastive Representation Learning
  - [`26a_contrastive_learning_theory.ipynb`](notebooks/26a_contrastive_learning_theory.ipynb) — InfoNCE / NT-Xent derived, and representational collapse [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/26a_contrastive_learning_theory.ipynb)
  - [`26b_contrastive_learning_practical.ipynb`](notebooks/26b_contrastive_learning_practical.ipynb) — SimCLR-style pretraining against PCA and autoencoder features, with a linear probe [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/26b_contrastive_learning_practical.ipynb)

#### Part II: Validation and Synthesis

- **Lesson 27**: Clustering Stability and Choosing K
  - [`27a_clustering_stability_theory.ipynb`](notebooks/27a_clustering_stability_theory.ipynb) — the gap statistic, resampling stability, prediction strength and consensus clustering [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/27a_clustering_stability_theory.ipynb)
  - [`27b_clustering_stability_practical.ipynb`](notebooks/27b_clustering_stability_practical.ipynb) — multi-algorithm consensus with per-point uncertainty [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/27b_clustering_stability_practical.ipynb)
- **Lesson 28**: Capstone: An End-to-End Unsupervised Analysis
  - [`28_capstone_pipeline.ipynb`](notebooks/28_capstone_pipeline.ipynb) — preprocessing, representation choice, K selection, anomaly detection and a written report, end to end [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-learning/blob/main/notebooks/28_capstone_pipeline.ipynb)

## Technical stack

- **Core**: NumPy, pandas, scikit-learn
- **Deep learning**: PyTorch
- **Visualisation**: Matplotlib, Seaborn, Plotly
- **Specialist libraries**: Gensim, mlxtend, MiniSom, UMAP, pyLDAvis, hmmlearn, tslearn

## Local use

```bash
git clone https://github.com/powell-clark/unsupervised-learning.git
cd unsupervised-learning
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/jupyter notebook notebooks/
```

## How this repository is built

The curriculum was developed with Claude Code: lessons were drafted by autonomous sessions against
a written syllabus, executed top to bottom and reviewed before they were accepted. The agents'
working state is kept out of this repository.

## Contributing

Spotted a typo, an unclear explanation or a bug? Open an issue or a pull request.

## Licence

Licensed under the Apache License, Version 2.0; see [LICENSE.md](LICENSE.md).
