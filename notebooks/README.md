# Notebooks

This directory contains all Jupyter notebooks for the unsupervised machine learning curriculum.

## 📚 Available Notebooks

### Legend
- ✅ **Complete** - Fully implemented and tested
- 🚧 **In Progress** - Currently being developed
- ⬜ **Planned** - Not yet started

---

## Foundation (0 of 2 complete)

### Lesson 0: Clustering Introduction
⬜ **0a_clustering_introduction_theory.ipynb**
- What is unsupervised learning?
- Distance metrics (Euclidean, Manhattan, Cosine)
- Curse of dimensionality

⬜ **0b_clustering_evaluation.ipynb**
- Internal metrics (Silhouette, Davies-Bouldin)
- External metrics (Adjusted Rand Index)
- Elbow method, Gap statistic

---

## Core Algorithms (0 of 8 complete)

### Lesson 1: K-Means Clustering
⬜ **1a_kmeans_theory.ipynb**
- Lloyd's algorithm derivation
- K-Means++ initialization
- From-scratch NumPy implementation

⬜ **1b_kmeans_practical.ipynb**
- Scikit-learn implementation
- Mini-batch K-Means
- Market segmentation application

### Lesson 2: Hierarchical Clustering
⬜ **2a_hierarchical_theory.ipynb**
- Agglomerative vs divisive
- Linkage methods (single, complete, average, Ward)
- Dendrogram construction

⬜ **2b_hierarchical_practical.ipynb**
- Scikit-learn implementation
- Real-world applications

### Lesson 3: DBSCAN
⬜ **3a_dbscan_theory.ipynb**
- Density-based clustering concepts
- Core points, border points, noise
- From-scratch implementation

⬜ **3b_dbscan_practical.ipynb**
- Scikit-learn and HDBSCAN
- Geographic data clustering

### Lesson 4: Gaussian Mixture Models
⬜ **4a_gmm_theory.ipynb**
- EM algorithm derivation
- E-step and M-step mathematics
- From-scratch implementation

⬜ **4b_gmm_practical.ipynb**
- Scikit-learn GMM
- Model selection (BIC, AIC)
- Image segmentation

---

## Dimensionality Reduction (0 of 4 complete)

### Lesson 5: Principal Component Analysis
⬜ **5a_pca_theory.ipynb**
- Eigenvalue decomposition
- SVD approach to PCA
- From-scratch implementation

⬜ **5b_pca_practical.ipynb**
- Scikit-learn PCA
- Kernel PCA
- Eigenfaces application

### Lesson 6: Manifold Learning
⬜ **6a_manifold_learning_theory.ipynb**
- t-SNE mathematics
- UMAP foundations
- Comparison of methods

⬜ **6b_manifold_learning_practical.ipynb**
- Scikit-learn t-SNE and UMAP
- Interactive visualizations
- Single-cell RNA-seq visualization

---

## Specialized Methods (2 of 6 complete)

### Lesson 7: Anomaly Detection
⬜ **7a_anomaly_detection_theory.ipynb**
- Statistical methods
- Isolation Forest
- Local Outlier Factor
- Autoencoder-based detection

⬜ **7b_anomaly_detection_practical.ipynb**
- Scikit-learn implementations
- Fraud detection application

### Lesson 8: Recommender Systems ✅
✅ **8a_recommender_systems_theory.ipynb**
- Collaborative filtering mathematics
- Matrix factorization
- Gradient descent derivation
- From-scratch implementation

✅ **8b_recommender_systems_practical.ipynb**
- Surprise library (SVD, SVD++, NMF)
- Implicit library (ALS)
- Neural Collaborative Filtering with PyTorch
- MovieLens dataset

### Lesson 9: Association Rules
⬜ **9a_association_rules_theory.ipynb**
- Apriori algorithm
- FP-Growth
- Support, confidence, lift

⬜ **9b_association_rules_practical.ipynb**
- mlxtend library
- Market basket analysis

---

## Advanced Topics (0 of 16 complete)

### Lesson 10: Topic Modeling
⬜ **10a_topic_modeling_theory.ipynb**
- Latent Dirichlet Allocation (LDA)
- Dirichlet distributions
- Gibbs sampling

⬜ **10b_topic_modeling_practical.ipynb**
- Gensim and scikit-learn
- pyLDAvis visualization
- 20 Newsgroups dataset

### Lesson 11: Self-Organizing Maps
⬜ **11a_som_theory.ipynb**
- Competitive learning
- Topology preservation
- From-scratch implementation

⬜ **11b_som_practical.ipynb**
- MiniSom library
- U-Matrix visualization

### Lesson 12: Deep Unsupervised Learning
⬜ **12a_autoencoders_theory.ipynb**
- Vanilla autoencoders
- Variational Autoencoders (VAE)
- ELBO derivation
- Reparameterization trick

⬜ **12b_autoencoders_practical.ipynb**
- PyTorch implementations
- Convolutional autoencoders
- Image denoising

⬜ **12c_gans_theory.ipynb** *(2025-2026 addition)*
- GAN fundamentals
- Minimax game formulation
- Training stability
- Wasserstein GAN

⬜ **12d_gans_practical.ipynb** *(2025-2026 addition)*
- DCGAN, StyleGAN basics
- Conditional GANs
- CycleGAN
- Evaluation metrics (FID, IS)

### Lesson 13: Diffusion Models *(2025-2026 addition)*
⬜ **13a_diffusion_theory.ipynb**
- Forward and reverse diffusion
- Denoising Diffusion Probabilistic Models (DDPM)
- Score-based generative models
- From-scratch PyTorch implementation

⬜ **13b_diffusion_practical.ipynb**
- Production diffusion implementations
- Classifier-free guidance
- DDIM sampling
- Stable Diffusion overview

### Lesson 14: Self-Supervised Learning *(2025-2026 addition)*
⬜ **14a_self_supervised_theory.ipynb**
- Contrastive learning principles
- SimCLR framework
- MoCo (Momentum Contrast)
- Alignment and uniformity

⬜ **14b_self_supervised_practical.ipynb**
- SimCLR and MoCo implementations
- CLIP for vision-language
- DINO (self-distillation)
- Transfer learning applications

---

## Professional Practice (0 of 4 complete)

⬜ **X1_clustering_comparison.ipynb**
- Systematic comparison of all clustering algorithms
- When to use each method
- Computational complexity

⬜ **X2_dimensionality_reduction_pipeline.ipynb**
- End-to-end pipelines
- Feature selection vs extraction
- Combining methods (PCA → t-SNE)

⬜ **X3_unsupervised_preprocessing.ipynb**
- Scaling and normalization
- Missing data handling
- Distance metric selection

⬜ **X4_semi_supervised_learning.ipynb**
- Label propagation
- Self-training
- Co-training

---

## Running Notebooks

### Locally

```bash
# Navigate to notebooks directory
cd notebooks/

# Start Jupyter
jupyter notebook

# Or use JupyterLab
jupyter lab
```

### Google Colab

All notebooks are Google Colab compatible. Each notebook includes a Colab badge at the top:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/unsupervised-machine-learning/blob/main/notebooks/8a_recommender_systems_theory.ipynb)

Click the badge to open directly in Colab.

---

## Notebook Structure

Each theory notebook (Xa) follows this structure:

1. **Introduction** - Real-world story and motivation
2. **Mathematical Foundations** - Derivations from first principles
3. **Algorithm Explanation** - Step-by-step breakdown
4. **From-Scratch Implementation** - NumPy with type hints
5. **Simple Examples** - Synthetic data demonstrations
6. **Visualizations** - Algorithm behavior plots
7. **Analysis** - Convergence, complexity, limitations
8. **Conclusion** - Summary and when to use

Each practical notebook (Xb) follows this structure:

1. **Introduction** - Brief recap and goals
2. **Real Dataset** - Loading and exploration
3. **Production Implementation** - Using libraries (scikit-learn, PyTorch, etc.)
4. **Algorithm Comparison** - Multiple approaches
5. **Hyperparameter Tuning** - Systematic optimization
6. **Evaluation** - Comprehensive metrics
7. **Production Considerations** - Deployment, monitoring, ethics
8. **Conclusion** - Summary and next steps

---

## Learning Path

### Beginner Path (Start Here)
1. Lesson 0: Clustering Introduction
2. Lesson 1: K-Means
3. Lesson 5: PCA
4. Lesson 8: Recommender Systems ✅

### Intermediate Path
5. Lesson 2: Hierarchical Clustering
6. Lesson 3: DBSCAN
7. Lesson 4: GMM
8. Lesson 6: t-SNE and UMAP
9. Lesson 7: Anomaly Detection

### Advanced Path
10. Lesson 10: Topic Modeling
11. Lesson 11: Self-Organizing Maps
12. Lesson 12: Autoencoders & VAE
13. Lesson 12c-d: GANs
14. Lesson 13: Diffusion Models
15. Lesson 14: Self-Supervised Learning

### Professional Path
16. X1: Clustering Comparison
17. X2: Dimensionality Reduction Pipeline
18. X3: Unsupervised Preprocessing
19. X4: Semi-Supervised Learning

---

## Prerequisites

Before starting:

1. **Complete supervised learning** - See [supervised-machine-learning](https://github.com/powell-clark/supervised-machine-learning) repository
2. **Mathematics**:
   - Linear algebra (vectors, matrices, eigenvalues)
   - Calculus (derivatives, gradients)
   - Probability (distributions, expectations)
3. **Python**:
   - NumPy basics
   - Matplotlib for visualization
   - Basic PyTorch/TensorFlow (for deep learning lessons)

---

## Tips for Learning

### Work Through in Order
Follow the numbered sequence - each lesson builds on previous ones.

### Run Every Cell
Don't just read - execute all code cells to see results.

### Experiment
Modify parameters, try different datasets, break things and fix them.

### Take Notes
Add your own markdown cells with observations and insights.

### Do the Math
Work through mathematical derivations with pen and paper.

### Implement Extensions
Try implementing variations mentioned in notebooks.

---

## Troubleshooting

### Kernel Crashes
- Restart kernel: `Kernel → Restart`
- Clear outputs: `Cell → All Output → Clear`
- Check memory usage (especially with large datasets)

### Missing Dependencies
```bash
pip install -r requirements.txt
```

### Cannot Find Module
```bash
# Add repo to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Colab Issues
- Check internet connection
- Clear runtime: `Runtime → Restart runtime`
- Datasets re-download when runtime resets

---

## Contributing

Want to implement a missing lesson? See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

Priority implementations:
1. **Lesson 0** - Clustering foundations (CRITICAL)
2. **Lesson 1** - K-Means (CRITICAL)
3. **Lesson 5** - PCA (CRITICAL)

---

## Questions?

- Check [CURRICULUM_PLAN.md](../CURRICULUM_PLAN.md) for detailed lesson specifications
- Review completed Lesson 8 notebooks as examples
- Open an issue on GitHub

---

**Progress**: 2/40 notebooks complete (5%)
**Next Priority**: Lessons 0, 1, 5
**Last Updated**: 2025
