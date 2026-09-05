# Unsupervised Machine Learning

A comprehensive, hands-on curriculum for learning unsupervised machine learning from first principles using Python. This repository teaches clustering, dimensionality reduction, anomaly detection, and advanced unsupervised methods through theory and practical implementation.

## The series

Four repositories, one curriculum. The first three are *how* a model learns; the fourth is *what*
it is built from, and cuts across all three.

- [Supervised learning](https://github.com/powell-clark/supervised-learning) — learning from labelled examples
- **[Unsupervised learning](https://github.com/powell-clark/unsupervised-learning) — finding structure with no labels (you are here)**
- [Reinforcement learning](https://github.com/powell-clark/reinforcement-learning) — learning from reward
- [Deep learning & transformers](https://github.com/powell-clark/deep-learning) — the architecture the other three can each be built on

## Overview

This curriculum follows a rigorous pedagogical approach:
- **From First Principles**: Mathematical derivations from foundational concepts
- **Dual Structure**: Theory (a) + Practical (b) notebooks for each lesson
- **Story-Driven**: Real-world motivations before diving into mathematics
- **Complete Implementations**: From-scratch NumPy code + production Scikit-learn/PyTorch
- **Google Colab Compatible**: Run everything in your browser, no setup required

## Curriculum Progress

**Status:** 17 of 17 lessons complete (31 notebooks)

### Completed Lessons

#### Foundation
- **Lesson 0**: Clustering Introduction & Evaluation
  - `0a_clustering_foundations.ipynb` — Cluster structure, k selection basics
  - `0b_cluster_evaluation.ipynb` — Internal/external metrics, silhouette analysis

#### Core Algorithms
- **Lesson 1**: K-Means Clustering
  - `1a_kmeans_theory.ipynb` — Lloyd's algorithm, initialization, convergence
  - `1b_kmeans_practical.ipynb` — RFM segmentation, image compression, scalability
  
- **Lesson 2**: Hierarchical Clustering
  - `2a_hierarchical_theory.ipynb` — Agglomerative algorithm, linkage methods
  - `2b_hierarchical_practical.ipynb` — Dendrogram cutting, scalability analysis
  
- **Lesson 3**: DBSCAN (Density-Based Clustering)
  - `3a_dbscan_theory.ipynb` — Epsilon-neighborhoods, core/border/noise classification
  - `3b_dbscan_practical.ipynb` — K-distance graphs, HDBSCAN introduction
  
- **Lesson 4**: Gaussian Mixture Models (GMM)
  - `4a_gmm_theory.ipynb` — EM algorithm, responsibilities, covariance types
  - `4b_gmm_practical.ipynb` — BIC/AIC selection, image segmentation

#### Dimensionality Reduction
- **Lesson 5**: Principal Component Analysis (PCA)
  - `5a_pca_theory.ipynb` — Eigendecomposition, SVD, numerical stability
  - `5b_pca_practical.ipynb` — Eigenfaces, kernel PCA, preprocessing benefits
  
- **Lesson 6**: Manifold Learning (t-SNE, UMAP)
  - `6a_manifold_learning_theory.ipynb` — t-SNE derivation, UMAP, visualization artifacts
  - `6b_manifold_learning_practical.ipynb` — Perplexity tuning, UMAP parameters, artifact detection

#### Specialized Methods
- **Lesson 7**: Anomaly Detection (Isolation Forest, LOF, one-class SVM)
  - `7a_anomaly_detection_theory.ipynb` — Isolation-based, density-based, and boundary-based paradigms from scratch
  - `7b_anomaly_detection_practical.ipynb` — Fraud-style imbalance, PyTorch autoencoder, PR-AUC comparison

- **Lesson 8**: Matrix Factorization & Recommender Systems
  - `8a_recommender_systems_theory.ipynb` — Collaborative filtering and matrix factorization
  - `8b_recommender_systems_practical.ipynb` — Surprise, Implicit, and PyTorch implementations

- **Lesson 9**: Association Rule Learning (Apriori, market-basket mining)
  - `9a_association_rules_theory.ipynb` — Support/confidence/lift, Apriori downward closure, from-scratch mining
  - `9b_association_rules_practical.ipynb` — mlxtend Apriori vs FP-Growth, threshold trade-offs, ranked rules

#### Advanced Topics
- **Lesson 10**: Topic Modeling (LDA, Gibbs sampling)
  - `10a_topic_modeling_theory.ipynb` — LDA generative model, collapsed Gibbs sampling from scratch
  - `10b_topic_modeling_practical.ipynb` — Gensim, scikit-learn, coherence-based K selection, pyLDAvis

- **Lesson 11**: Self-Organizing Maps (competitive learning)
  - `11a_self_organizing_maps_theory.ipynb` — BMU, neighborhood decay, grid unfolding from scratch
  - `11b_self_organizing_maps_practical.ipynb` — MiniSom, U-Matrix, component planes on the Wine dataset

- **Lesson 12**: Deep Unsupervised Learning (Autoencoders, VAE)
  - `12a_deep_unsupervised_theory.ipynb` — Autoencoder-PCA connection, VAE, ELBO, reparameterization trick
  - `12b_deep_unsupervised_practical.ipynb` — Convolutional and denoising autoencoders in PyTorch

#### Professional Practice
- **Lesson 13**: Clustering Comparison Framework
  - `13_clustering_comparison.ipynb` — Runtime/quality benchmarks across K-Means, Hierarchical, DBSCAN, GMM; K/eps sensitivity sweeps
- **Lesson 14**: Dimensionality Reduction Pipeline
  - `14_dimensionality_reduction_pipeline.ipynb` — Feature selection vs PCA extraction, leakage-safe pipelines
- **Lesson 15**: Unsupervised Preprocessing (scaling, encoding, metrics)
  - `15_unsupervised_preprocessing.ipynb` — Scaling, categorical encoding, distance metrics, imputation, each measured by downstream clustering quality
- **Lesson 16**: Semi-Supervised Learning (label propagation, co-training)
  - `16_semi_supervised_learning.ipynb` — Label spreading, self-training, from-scratch co-training with the naive-collapse vs balanced-fix contrast

## Part II — Advanced Topics

**Status:** 12 of 12 lessons complete (23 notebooks)

Lessons 17-28 extend the course into density estimation, flows, matrix factorization, general EM and variational inference, Dirichlet-process clustering, HMMs, time-series clustering, embeddings, contrastive learning, clustering stability, and a capstone. Built and independently reviewed autonomously (fresh-context opus review per lesson, agent-approved before closing) — see `CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md` for the per-lesson plan and review history.

#### Density Estimation and Modern Generative Models
- **Lesson 17**: Spectral Clustering and Graph Laplacians
  - `17a_spectral_clustering_theory.ipynb` — Graph Laplacians, eigengap heuristic, normalized cuts from scratch
  - `17b_spectral_clustering_practical.ipynb` — Non-convex cluster shapes, affinity construction, scalability

- **Lesson 18**: Kernel Density Estimation and Nonparametric Density
  - `18a_kernel_density_estimation_theory.ipynb` — KDE derivation, bandwidth selection, curse of dimensionality
  - `18b_kernel_density_estimation_practical.ipynb` — Bandwidth cross-validation, multivariate KDE, anomaly scoring

- **Lesson 19**: Normalizing Flows and Modern Density Models
  - `19a_normalizing_flows_theory.ipynb` — Change-of-variables, coupling layers, exact-likelihood flows from scratch
  - `19b_normalizing_flows_practical.ipynb` — Flow-based density estimation trained and evaluated on real data

#### Factorization and Inference
- **Lesson 20**: Matrix Factorisation Family: NMF and ICA
  - `20a_nmf_ica_theory.ipynb` — Non-negative matrix factorization and independent component analysis derivations
  - `20b_nmf_ica_practical.ipynb` — Topic extraction via NMF, blind source separation via ICA

- **Lesson 21**: Expectation-Maximisation and Variational Inference
  - `21a_em_variational_inference_theory.ipynb` — General EM derivation, ELBO, mean-field variational inference
  - `21b_em_variational_inference_practical.ipynb` — EM for mixture models and variational inference in practice

- **Lesson 22**: Bayesian Nonparametric Clustering: Dirichlet Process Mixtures
  - `22a_dirichlet_process_mixtures_theory.ipynb` — Stick-breaking construction, Chinese restaurant process, infinite mixtures from scratch
  - `22b_dirichlet_process_mixtures_practical.ipynb` — DP-mixture clustering without choosing K in advance

#### Sequences and Representations
- **Lesson 23**: Hidden Markov Models and Unsupervised Sequence Learning
  - `23a_hidden_markov_models_theory.ipynb` — Forward-backward, Viterbi, Baum-Welch EM from scratch
  - `23b_hidden_markov_models_practical.ipynb` — hmmlearn regime detection on simulated sequences

- **Lesson 24**: Time-Series Clustering and Dynamic Time Warping
  - `24a_time_series_clustering_theory.ipynb` — DTW derivation, time-series K-means from scratch
  - `24b_time_series_clustering_practical.ipynb` — tslearn DTW-based clustering on real time-series data

- **Lesson 25**: Word and Item Embeddings: word2vec and Skip-Gram with Negative Sampling
  - `25a_word_embeddings_theory.ipynb` — Skip-gram objective and negative-sampling derivation from scratch
  - `25b_word_embeddings_practical.ipynb` — gensim word2vec, embedding-space analogies and similarity

- **Lesson 26**: Self-Supervised Contrastive Representation Learning
  - `26a_contrastive_learning_theory.ipynb` — InfoNCE/NT-Xent derivation, collapse and its avoidance from scratch
  - `26b_contrastive_learning_practical.ipynb` — SimCLR-style contrastive pretraining measured against PCA/autoencoder features with a linear probe

#### Validation and Synthesis
- **Lesson 27**: Clustering Stability, Consensus and Choosing K Honestly
  - `27a_clustering_stability_theory.ipynb` — Gap statistic, resampling stability, prediction strength, consensus clustering
  - `27b_clustering_stability_practical.ipynb` — Multi-algorithm consensus ensembles with per-point uncertainty flagging

- **Lesson 28**: Capstone: An End-to-End Unsupervised Analysis
  - `28_capstone_pipeline.ipynb` — A complete pipeline: leakage-safe preprocessing, evidence-based representation choice, honest gap-statistic/stability K-selection, dual anomaly detection, and a written stakeholder report

## Technical Stack

- **Core**: NumPy, Pandas, Scikit-learn
- **Deep Learning**: PyTorch
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Specialized**:
  - Gensim (topic modeling, word2vec)
  - mlxtend (association rules)
  - MiniSom (self-organizing maps)
  - UMAP-learn (dimensionality reduction)
  - pyLDAvis (topic model visualization)
  - hmmlearn (hidden Markov models)
  - tslearn (time-series clustering, dynamic time warping)

## Datasets

Datasets included and used:
- Iris (unlabeled for clustering examples)
- Synthetic data (demonstrations)
- Customer segmentation (RFM analysis)
- MNIST samples (dimensionality reduction)
- Face images (eigenfaces)
- Gene expression data (advanced examples)

Additional datasets will be integrated for later lessons.

## Getting Started

### Prerequisites
No formal prerequisites, but familiarity with Python, NumPy, and basic machine learning concepts is helpful.

### Installation

```bash
git clone https://github.com/powell-clark/unsupervised-learning.git
cd unsupervised-learning
pip install -r requirements.txt
```

### Running Notebooks

All notebooks are Google Colab compatible. Click the "Open in Colab" badge in any notebook to run it immediately in your browser (no local setup required).

## Learning Path

1. **Start with Foundation** (Lesson 0): Core clustering concepts and evaluation
2. **Master Core Algorithms** (Lessons 1-4): Essential clustering methods (K-Means, Hierarchical, DBSCAN, GMM)
3. **Learn Dimensionality Reduction** (Lessons 5-6): PCA and manifold learning for high-dimensional data
4. **Explore Specialized Methods** (Lessons 7-9): Anomaly detection, matrix factorization, association rules
5. **Advance to Modern Techniques** (Lessons 10-12): Topic modeling, self-organizing maps, deep unsupervised learning
6. **Apply Professional Skills** (Lessons 13-16): Production-ready pipelines and practical frameworks, synthesizing every prior lesson into decision frameworks for real projects
7. **Extend into Part II** (Lessons 17-28): Density estimation and modern generative models, the factorization/inference family beyond PCA and GMM, sequences and representation learning, and a capstone that combines every tool from both parts on one end-to-end analysis

## Architecture

This curriculum uses the consciousness system for task management and feature-driven development:
- **PGPS**: Roadmap tracking with feature cards and task specifications
- **Review System**: Verdicts recorded for all completed work
- **Autonomous Loop**: Continuous work cycle with status tracking

## Related Repositories

This is part of a comprehensive machine learning curriculum:
- **[supervised-learning](https://github.com/powell-clark/supervised-learning)** — Foundational supervised methods (reference)
- **unsupervised-learning** — This repository (100% complete, Parts I and II)
- **[reinforcement-learning](https://github.com/powell-clark/reinforcement-learning)** — Sequential decision-making (planned)

## License

Apache License 2.0 — See LICENSE.md file for details

## Contributing

Contributions welcome! Please read CONTRIBUTING.md for guidelines.

## Contact

Questions or suggestions? Open an issue on GitHub or reach out!

---

**Status:** 29 of 29 lessons complete (54 notebooks)
**Last Updated**: 2026-09-05
**Author**: Powell-Clark Limited
