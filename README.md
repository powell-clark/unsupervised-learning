# Unsupervised Machine Learning

A comprehensive, hands-on curriculum for learning unsupervised machine learning from first principles using Python. This repository teaches clustering, dimensionality reduction, anomaly detection, and advanced unsupervised methods through theory and practical implementation.

## Overview

This curriculum follows a rigorous pedagogical approach:
- **From First Principles**: Mathematical derivations from foundational concepts
- **Dual Structure**: Theory (a) + Practical (b) notebooks for each lesson
- **Story-Driven**: Real-world motivations before diving into mathematics
- **Complete Implementations**: From-scratch NumPy code + production Scikit-learn/PyTorch
- **Google Colab Compatible**: Run everything in your browser, no setup required

## Curriculum Progress

**Status**: 76% complete (13 of 17 lessons, 26 notebooks)

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

### Planned Lessons (4 remaining)

#### Professional Practice
- **Lesson 13**: Clustering Comparison Framework
- **Lesson 14**: Dimensionality Reduction Pipeline
- **Lesson 15**: Unsupervised Preprocessing (scaling, encoding, metrics)
- **Lesson 16**: Semi-Supervised Learning (label propagation, co-training)

## Technical Stack

- **Core**: NumPy, Pandas, Scikit-learn
- **Deep Learning**: PyTorch
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Specialized**:
  - Gensim (topic modeling)
  - mlxtend (association rules)
  - MiniSom (self-organizing maps)
  - UMAP-learn (dimensionality reduction)
  - pyLDAvis (topic model visualization)

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
6. **Apply Professional Skills** (Lessons 13-16): Production-ready pipelines and practical frameworks

## Architecture

This curriculum uses the consciousness system for task management and feature-driven development:
- **PGPS**: Roadmap tracking with feature cards and task specifications
- **Review System**: Verdicts recorded for all completed work
- **Autonomous Loop**: Continuous work cycle with status tracking

## Related Repositories

This is part of a comprehensive machine learning curriculum:
- **[supervised-learning](https://github.com/powell-clark/supervised-learning)** — Foundational supervised methods (reference)
- **unsupervised-learning** — This repository (76% complete)
- **[reinforcement-learning](https://github.com/powell-clark/reinforcement-learning)** — Sequential decision-making (planned)

## License

Apache License 2.0 — See LICENSE.md file for details

## Contributing

Contributions welcome! Please read CONTRIBUTING.md for guidelines.

## Contact

Questions or suggestions? Open an issue on GitHub or reach out!

---

**Status**: 76% complete (13 of 17 lessons, 26 notebooks)
**Last Updated**: 2026-07-13
**Author**: Powell-Clark Limited
