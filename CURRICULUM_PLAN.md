# 📊 Unsupervised Machine Learning - Curriculum Plan

## Overview
This document outlines the comprehensive curriculum for the **unsupervised-machine-learning** repository, which will complement the supervised learning series. The repository will teach unsupervised learning from first principles using Python, following the same pedagogical approach: story-driven introductions, mathematical derivations, from-scratch implementations, and production code.

**2025-2026 Update**: Curriculum expanded to include modern topics emphasized in elite university programs:
- **Lesson 12c-d**: GANs (still relevant alongside diffusion models)
- **Lesson 13**: Diffusion Models (covered in 80% of advanced ML courses)
- **Lesson 14**: Self-Supervised & Contrastive Learning (SimCLR, MoCo, CLIP)

This brings total curriculum to **40 notebooks** (up from 32), aligning with cutting-edge unsupervised learning research and industry practices.

## Teaching Philosophy
- **From First Principles**: Every algorithm derived mathematically from foundational concepts
- **Dual Approach**: Each lesson has theory (a) and practical (b) notebooks
- **Story-Driven**: Real-world motivations and intuitive explanations before mathematics
- **Complete Implementations**: From-scratch NumPy implementations + production Scikit-learn/PyTorch code
- **Google Colab Compatible**: All notebooks runnable in browser with one click

## Curriculum Structure

### Foundation
**Lesson 0: Clustering Foundations** - Introduction to unsupervised learning
- **0a_clustering_introduction_theory.ipynb**
  - What is unsupervised learning? How does it differ from supervised?
  - Distance metrics: Euclidean, Manhattan, Cosine similarity
  - Similarity vs. dissimilarity measures
  - Curse of dimensionality in clustering
  - Dataset: Iris (without labels) for visualization

- **0b_clustering_evaluation.ipynb**
  - Evaluating clusters without ground truth
  - Internal metrics: Silhouette score, Davies-Bouldin, Calinski-Harabasz
  - External metrics: Adjusted Rand Index, Normalized Mutual Information
  - Choosing optimal number of clusters: Elbow method, Gap statistic
  - Visual evaluation techniques

### Core Algorithms

**Lesson 1: K-Means Clustering** - The foundation of clustering
- **1a_kmeans_theory.ipynb**
  - Mathematical formulation: minimizing within-cluster sum of squares
  - Lloyd's algorithm derivation
  - Convergence guarantees and initialization methods (random, K-Means++)
  - Time complexity analysis
  - From-scratch implementation
  - Dataset: Customer segmentation data

- **1b_kmeans_practical.ipynb**
  - Scikit-learn implementation
  - Mini-batch K-Means for large datasets
  - Handling categorical features
  - Real-world application: Market segmentation
  - Visualization techniques for high-dimensional clusters

**Lesson 2: Hierarchical Clustering** - Tree-based clustering
- **2a_hierarchical_theory.ipynb**
  - Agglomerative vs. Divisive approaches
  - Linkage methods: Single, complete, average, Ward
  - Dendrogram construction and interpretation
  - Mathematical formulation of linkage criteria
  - From-scratch implementation with dendrogram visualization
  - Dataset: Gene expression data

- **2b_hierarchical_practical.ipynb**
  - Scikit-learn implementation
  - Cutting dendrograms to extract clusters
  - Comparing linkage methods
  - Real-world application: Taxonomy construction, document clustering

**Lesson 3: DBSCAN** - Density-based clustering
- **3a_dbscan_theory.ipynb**
  - Core points, border points, noise points
  - ε (epsilon) and MinPts parameters
  - Mathematical formulation of density-reachability
  - Advantages over K-Means: arbitrary shapes, noise handling
  - From-scratch implementation
  - Dataset: Spatial data with non-convex clusters

- **3b_dbscan_practical.ipynb**
  - Scikit-learn implementation
  - Parameter selection techniques
  - Handling varying densities with HDBSCAN
  - Real-world application: Anomaly detection in geographic data

**Lesson 4: Gaussian Mixture Models** - Probabilistic clustering
- **4a_gmm_theory.ipynb**
  - Mixture of Gaussians: mathematical formulation
  - Expectation-Maximization (EM) algorithm derivation
  - E-step: Computing responsibilities
  - M-step: Updating parameters
  - Connection to K-Means
  - Covariance types: spherical, diagonal, tied, full
  - From-scratch implementation
  - Dataset: Synthetic multi-modal data

- **4b_gmm_practical.ipynb**
  - Scikit-learn implementation
  - Model selection: BIC and AIC
  - Soft clustering vs. hard clustering
  - Real-world application: Image segmentation, speaker identification

**Lesson 5: Dimensionality Reduction - PCA** - Principal Component Analysis
- **5a_pca_theory.ipynb**
  - The curse of dimensionality
  - Linear algebra foundations: eigenvectors and eigenvalues
  - Maximizing variance formulation
  - Covariance matrix derivation
  - SVD approach to PCA
  - Choosing number of components: explained variance
  - From-scratch implementation using eigendecomposition and SVD
  - Dataset: High-dimensional gene expression or image data

- **5b_pca_practical.ipynb**
  - Scikit-learn implementation
  - Kernel PCA for non-linear dimensionality reduction
  - Whitening and centering
  - Real-world application: Face recognition (Eigenfaces), data visualization

**Lesson 6: Advanced Dimensionality Reduction** - Non-linear methods
- **6a_manifold_learning_theory.ipynb**
  - Manifold hypothesis
  - t-SNE: t-distributed Stochastic Neighbor Embedding
    - SNE formulation with KL divergence
    - t-distribution for heavy tails
    - Perplexity parameter
  - UMAP: Uniform Manifold Approximation and Projection
    - Topological data analysis foundations
    - Fuzzy simplicial sets
  - Comparison: PCA vs. t-SNE vs. UMAP
  - Dataset: MNIST for visualization

- **6b_manifold_learning_practical.ipynb**
  - Scikit-learn t-SNE and UMAP implementations
  - Parameter tuning for visualization
  - Interactive visualizations with Plotly
  - Real-world application: Single-cell RNA-seq visualization, embeddings visualization

**Lesson 7: Anomaly Detection** - Finding outliers (unsupervised approaches)
- **7a_anomaly_detection_theory.ipynb**
  - Statistical methods: Z-score, IQR, Grubbs' test
  - Isolation Forest: path length in random trees
  - Local Outlier Factor (LOF): local density deviation
  - One-Class SVM for novelty detection
  - Autoencoders for anomaly detection
  - From-scratch implementations
  - Dataset: Credit card transactions

- **7b_anomaly_detection_practical.ipynb**
  - Scikit-learn implementations (Isolation Forest, LOF, One-Class SVM)
  - PyTorch Autoencoder for anomaly detection
  - Threshold selection techniques
  - Real-world application: Fraud detection, system monitoring

**Lesson 8: Recommender Systems** - Collaborative and content-based filtering
- **8a_recommender_systems_theory.ipynb**
  - Collaborative filtering: user-based and item-based
  - Matrix factorization for recommendations
  - Cost function derivation
  - Gradient descent for collaborative filtering
  - Alternating Least Squares (ALS)
  - Content-based filtering vs collaborative filtering
  - Hybrid approaches
  - Cold start problem
  - From-scratch implementation
  - Dataset: MovieLens ratings matrix

- **8b_recommender_systems_practical.ipynb**
  - Surprise library for collaborative filtering
  - Matrix factorization with SVD, SVD++, NMF
  - Implicit library for implicit feedback
  - TensorFlow/PyTorch implementation
  - Mean normalization for bias handling
  - Binary labels (likes/clicks)
  - Evaluation metrics: RMSE, MAE, Precision@K, Recall@K
  - Finding related items
  - Real-world application: Movie recommendations, e-commerce

**Lesson 9: Association Rule Learning** - Market basket analysis
- **9a_association_rules_theory.ipynb**
  - Support, confidence, lift metrics
  - Apriori algorithm
  - FP-Growth algorithm
  - From-scratch implementation
  - Dataset: Retail transaction data

- **9b_association_rules_practical.ipynb**
  - mlxtend library implementation
  - Mining frequent itemsets
  - Generating association rules
  - Real-world application: Market basket analysis, web usage mining

### Advanced Topics

**Lesson 10: Topic Modeling** - Discovering latent topics
- **10a_topic_modeling_theory.ipynb**
  - Latent Dirichlet Allocation (LDA)
  - Plate notation and generative process
  - Dirichlet distributions
  - Gibbs sampling for inference
  - Connection to NMF
  - From-scratch simplified implementation
  - Dataset: 20 Newsgroups or Wikipedia articles

- **10b_topic_modeling_practical.ipynb**
  - Gensim and Scikit-learn implementations
  - Preprocessing text for topic modeling
  - Choosing number of topics
  - Visualization with pyLDAvis
  - Real-world application: Document organization, content recommendation

**Lesson 11: Self-Organizing Maps** - Neural network clustering
- **11a_som_theory.ipynb**
  - Competitive learning
  - Neighborhood functions
  - Learning rate schedules
  - Topology preservation
  - From-scratch implementation
  - Dataset: Color clustering

- **11b_som_practical.ipynb**
  - MiniSom library implementation
  - U-Matrix visualization
  - Real-world application: Data visualization, feature extraction

**Lesson 12: Deep Unsupervised Learning** - Modern neural approaches
- **12a_autoencoders_theory.ipynb**
  - Vanilla autoencoders
  - Variational Autoencoders (VAE)
    - ELBO derivation
    - Reparameterization trick
  - Sparse autoencoders
  - Denoising autoencoders
  - From-scratch PyTorch implementation
  - Dataset: MNIST

- **12b_autoencoders_practical.ipynb**
  - Production PyTorch implementations
  - Convolutional autoencoders
  - Applications: Denoising, compression, generation
  - Latent space visualization
  - Real-world application: Image denoising, feature learning

- **12c_gans_theory.ipynb**
  - Generative Adversarial Networks fundamentals
  - Generator and Discriminator architecture
  - Minimax game formulation
  - Training dynamics and stability
  - Mode collapse problem
  - Wasserstein GAN and gradient penalty
  - From-scratch PyTorch implementation
  - Dataset: MNIST, CelebA

- **12d_gans_practical.ipynb**
  - Production GAN implementations
  - Deep Convolutional GANs (DCGAN)
  - StyleGAN basics
  - Conditional GANs (cGAN)
  - CycleGAN for unpaired translation
  - Evaluation metrics: Inception Score, FID
  - Real-world application: Image synthesis, data augmentation

**Lesson 13: Diffusion Models** - State-of-the-art generative modeling (2025-2026)
- **13a_diffusion_theory.ipynb**
  - Forward diffusion process
  - Reverse diffusion process
  - Denoising Diffusion Probabilistic Models (DDPM)
  - Score-based generative models
  - Noise schedules (linear, cosine)
  - Connection to VAEs and energy-based models
  - From-scratch PyTorch implementation
  - Dataset: MNIST, CIFAR-10

- **13b_diffusion_practical.ipynb**
  - Production diffusion model implementations
  - Classifier-free guidance
  - DDIM for faster sampling
  - Conditional generation
  - Latent diffusion models basics
  - Stable Diffusion components overview
  - Real-world application: Image generation, inpainting

**Lesson 14: Self-Supervised & Contrastive Learning** - Modern unsupervised representation learning
- **14a_self_supervised_theory.ipynb**
  - Self-supervised learning paradigm
  - Pretext tasks (rotation, jigsaw, colorization)
  - Contrastive learning principles
  - SimCLR: Simple framework for contrastive learning
    - NT-Xent loss derivation
    - Data augmentation strategies
  - MoCo: Momentum Contrast
    - Queue-based approach
    - Momentum encoder
  - Alignment and uniformity principles
  - From-scratch PyTorch implementation
  - Dataset: CIFAR-10, STL-10

- **14b_self_supervised_practical.ipynb**
  - Production SimCLR and MoCo implementations
  - CLIP: Contrastive Language-Image Pre-training
  - Vision-language models basics
  - DINO: Self-distillation with no labels
  - Transfer learning with self-supervised features
  - Fine-tuning on downstream tasks
  - Real-world application: Pre-training for limited labeled data, zero-shot classification

### Professional Practice (X-Series)

**X1_clustering_comparison.ipynb**
- Systematic comparison of all clustering algorithms
- When to use each method
- Computational complexity comparison
- Handling different data types
- Practical decision framework

**X2_dimensionality_reduction_pipeline.ipynb**
- Building end-to-end dimensionality reduction pipelines
- Feature selection vs. feature extraction
- Combining methods (e.g., PCA → t-SNE)
- Preservation of information metrics
- Practical guidelines

**X3_unsupervised_preprocessing.ipynb**
- Data preprocessing for unsupervised learning
- Scaling and normalization impact
- Handling missing data
- Categorical encoding for clustering
- Distance metric selection

**X4_semi_supervised_learning.ipynb**
- Label propagation
- Self-training
- Co-training
- Combining supervised and unsupervised approaches
- Real-world application: Limited labeled data scenarios

## Datasets

### Iris Dataset (unlabeled)
- 150 samples × 4 features
- Classic clustering visualization
- Used in: Lesson 0

### Customer Segmentation Dataset
- E-commerce customer behavior data
- Used in: Lesson 1 (K-Means)

### Gene Expression Data
- High-dimensional biological data
- Used in: Lesson 2 (Hierarchical), Lesson 5 (PCA)

### Spatial Data with Non-Convex Clusters
- Geographic or synthetic data with complex shapes
- Used in: Lesson 3 (DBSCAN)

### Synthetic Multi-Modal Data
- Gaussian mixture datasets
- Used in: Lesson 4 (GMM)

### MNIST Handwritten Digits
- 70,000 samples × 784 features
- Used in: Lesson 6 (Manifold Learning), Lesson 12 (Autoencoders), Lesson 13 (Diffusion)

### Credit Card Transactions
- Fraud detection dataset
- Used in: Lesson 7 (Anomaly Detection)

### MovieLens Dataset
- Movie ratings matrix
- Used in: Lesson 8 (Matrix Factorization)

### Retail Transaction Data
- Market basket data
- Used in: Lesson 9 (Association Rules)

### 20 Newsgroups / Wikipedia Articles
- Text corpus for topic modeling
- Used in: Lesson 10 (Topic Modeling)

### CelebA (Celebrities Faces)
- 200K+ celebrity images
- Used in: Lesson 12 (GANs)

### CIFAR-10/100
- 60,000 32x32 color images in 10/100 classes
- Used in: Lesson 13 (Diffusion Models), Lesson 14 (Self-Supervised Learning)

### STL-10
- 10 classes with limited labeled data (designed for unsupervised learning)
- Used in: Lesson 14 (Self-Supervised & Contrastive Learning)

### ImageNet Subset
- Subset of ImageNet for pre-training experiments
- Used in: Lesson 14 (Self-Supervised Learning)

## Technical Stack
- **Core Libraries**: NumPy, Pandas, Scikit-learn
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Deep Learning**: PyTorch
- **Specialized**:
  - Gensim (topic modeling)
  - mlxtend (association rules)
  - MiniSom (self-organizing maps)
  - Surprise, Implicit (recommender systems)
  - UMAP-learn (dimensionality reduction)
  - pyLDAvis (topic model visualization)

## Implementation Timeline
**Phase 1: Foundation & Core** (Lessons 0-4)
- Clustering fundamentals
- K-Means, Hierarchical, DBSCAN, GMM

**Phase 2: Dimensionality Reduction** (Lessons 5-6)
- PCA and manifold learning methods

**Phase 3: Specialized Methods** (Lessons 7-9)
- Anomaly detection, matrix factorization, association rules

**Phase 4: Advanced Topics** (Lessons 10-12)
- Topic modeling, SOMs, deep unsupervised learning

**Phase 5: Professional Practice** (X-Series)
- Cross-cutting skills and best practices

## Repository Structure
```
unsupervised-machine-learning/
├── notebooks/
│   ├── 0a_clustering_introduction_theory.ipynb
│   ├── 0b_clustering_evaluation.ipynb
│   ├── 1a_kmeans_theory.ipynb
│   ├── 1b_kmeans_practical.ipynb
│   ├── ... (all lessons)
│   ├── X1_clustering_comparison.ipynb
│   └── X4_semi_supervised_learning.ipynb
├── data/
│   └── (datasets or download scripts)
├── requirements.txt
├── README.md
└── LICENSE
```

## Success Metrics
- **Comprehensiveness**: Cover 100% of standard unsupervised ML curriculum
- **Accessibility**: Explain from first principles, no PhD required
- **Practicality**: Every algorithm has production-ready code
- **Modern**: Include latest methods (UMAP, VAE) alongside classics
- **Runnable**: All notebooks work in Google Colab immediately

## Relationship to Other Repositories
- **Supervised ML**: Foundation → this repo builds on those concepts
- **Reinforcement Learning**: Separate paradigm, covered in dedicated repo
- **Computer Vision**: May use unsupervised methods (autoencoders) but focuses on vision tasks
- **NLP**: May use unsupervised methods (topic modeling) but focuses on language tasks

---

**Status**: Planning document for future implementation
**Created**: 2025
**Author**: Powell-Clark Limited
