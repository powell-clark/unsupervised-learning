# Datasets

This directory contains datasets used throughout the unsupervised machine learning curriculum. Datasets are **not included** in the repository due to size and licensing considerations.

## Quick Start

All notebooks include code to automatically download required datasets. Simply run the notebooks, and datasets will be downloaded to this directory when needed.

Alternatively, you can pre-download all datasets by running:

```bash
python scripts/download_datasets.py --all
```

## Dataset Overview

### Foundation & Core Algorithms

#### Iris Dataset (Lesson 0)
- **Source**: Scikit-learn built-in
- **Size**: 150 samples × 4 features
- **Usage**: Clustering introduction and visualization
- **Download**: Automatic via `sklearn.datasets.load_iris()`

```python
from sklearn.datasets import load_iris
iris = load_iris()
```

#### Customer Segmentation (Lesson 1)
- **Source**: [UCI ML Repository - Online Retail](https://archive.ics.uci.edu/ml/datasets/online+retail)
- **Size**: ~500K transactions
- **Usage**: K-Means clustering for market segmentation
- **Download**: Automatic in notebook or manual from UCI

```python
# Automatic download in notebook
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
df = pd.read_excel(url)
```

#### Gene Expression Data (Lessons 2, 5)
- **Source**: [GEO Database](https://www.ncbi.nlm.nih.gov/geo/) or synthetic
- **Size**: Varies (typically 100-1000 samples × 1000-20000 genes)
- **Usage**: Hierarchical clustering, PCA
- **Download**: Automatic synthetic data generation in notebooks

#### Spatial Clustering Data (Lesson 3)
- **Source**: Synthetic with scikit-learn
- **Size**: Custom generated
- **Usage**: DBSCAN for non-convex clusters
- **Download**: Generated in notebook

```python
from sklearn.datasets import make_moons, make_circles
X, _ = make_moons(n_samples=200, noise=0.05, random_state=42)
```

### Dimensionality Reduction

#### MNIST Handwritten Digits (Lessons 6, 12, 13)
- **Source**: [MNIST Database](http://yann.lecun.com/exdb/mnist/)
- **Size**: 70,000 images (28×28 pixels)
- **Usage**: Manifold learning (t-SNE, UMAP), autoencoders, diffusion models
- **Download**: Automatic via PyTorch/TensorFlow

```python
from torchvision import datasets, transforms
mnist = datasets.MNIST('./data', train=True, download=True)
```

### Specialized Methods

#### Credit Card Fraud (Lesson 7)
- **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Size**: 284,807 transactions × 30 features
- **Usage**: Anomaly detection
- **Download**: Requires Kaggle account
- **Note**: Due to privacy, uses anonymized PCA-transformed features

**Manual Download**:
1. Create Kaggle account at https://www.kaggle.com
2. Download from: https://www.kaggle.com/mlg-ulb/creditcardfraud
3. Place `creditcard.csv` in `data/` directory

#### MovieLens (Lesson 8)
- **Source**: [MovieLens](https://grouplens.org/datasets/movielens/)
- **Versions**: 100K (small), 1M, 20M, 25M (large)
- **Size**: 100K ratings from 943 users on 1,682 movies
- **Usage**: Recommender systems
- **Download**: Automatic via Surprise library

```python
from surprise import Dataset
data = Dataset.load_builtin('ml-100k')
```

#### Retail Transactions (Lesson 9)
- **Source**: [UCI ML Repository - Online Retail](https://archive.ics.uci.edu/ml/datasets/online+retail)
- **Size**: ~25K transactions
- **Usage**: Association rule mining
- **Download**: Automatic in notebook

### Advanced Topics

#### 20 Newsgroups (Lesson 10)
- **Source**: Scikit-learn built-in
- **Size**: ~18K documents, 20 categories
- **Usage**: Topic modeling (LDA)
- **Download**: Automatic via scikit-learn

```python
from sklearn.datasets import fetch_20newsgroups
newsgroups = fetch_20newsgroups(subset='all')
```

#### CelebA (Lesson 12 - GANs)
- **Source**: [CelebFaces Attributes Dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
- **Size**: 202,599 celebrity face images
- **Usage**: GAN training
- **Download**: Automatic via PyTorch

```python
from torchvision import datasets
celeba = datasets.CelebA('./data', split='train', download=True)
```

#### CIFAR-10/100 (Lessons 13, 14)
- **Source**: [CIFAR Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- **Size**: 60,000 32×32 color images (10 or 100 classes)
- **Usage**: Diffusion models, self-supervised learning
- **Download**: Automatic via PyTorch/TensorFlow

```python
from torchvision import datasets
cifar10 = datasets.CIFAR10('./data', train=True, download=True)
```

#### STL-10 (Lesson 14)
- **Source**: [STL-10 Dataset](https://cs.stanford.edu/~acoates/stl10/)
- **Size**: 13,000 labeled + 100,000 unlabeled images
- **Usage**: Self-supervised and contrastive learning
- **Download**: Automatic via PyTorch

```python
from torchvision import datasets
stl10 = datasets.STL10('./data', split='unlabeled', download=True)
```

## Directory Structure

After downloading datasets, your directory should look like:

```
data/
├── README.md (this file)
├── iris/                 # Automatically created
├── mnist/                # Downloaded by PyTorch/TF
├── cifar-10-batches-py/  # Downloaded by PyTorch/TF
├── celeba/               # Downloaded by PyTorch
├── stl10_binary/         # Downloaded by PyTorch
├── creditcard.csv        # Manual download from Kaggle
├── online_retail.xlsx    # Auto-downloaded
└── 20newsgroups/         # Auto-downloaded
```

## Storage Requirements

| Dataset | Size | Required For |
|---------|------|-------------|
| Iris | <1 MB | Lesson 0 |
| Customer Data | ~50 MB | Lesson 1 |
| Synthetic Data | <1 MB | Lessons 3, 4 |
| MNIST | ~50 MB | Lessons 6, 12, 13 |
| Credit Card | ~150 MB | Lesson 7 |
| MovieLens 100K | ~5 MB | Lesson 8 |
| MovieLens 1M | ~24 MB | Lesson 8 (optional) |
| 20 Newsgroups | ~20 MB | Lesson 10 |
| CelebA | ~1.4 GB | Lesson 12 |
| CIFAR-10 | ~170 MB | Lessons 13, 14 |
| STL-10 | ~2.6 GB | Lesson 14 |

**Total**: ~5 GB (all datasets)
**Minimum**: ~500 MB (essential datasets only)

## Download Script

Create `scripts/download_datasets.py` to batch download:

```python
"""
Download all datasets for the unsupervised ML curriculum.

Usage:
    python scripts/download_datasets.py --all
    python scripts/download_datasets.py --lesson 0 1 5
"""

import argparse
from pathlib import Path

# Implementation in scripts/ directory
```

## Data Preprocessing

Some datasets require preprocessing before use:

### Credit Card Fraud
```python
import pandas as pd
df = pd.read_csv('data/creditcard.csv')
# Already normalized via PCA, no additional preprocessing needed
```

### Online Retail (Customer Segmentation)
```python
df = pd.read_excel('data/online_retail.xlsx')
# Remove missing customer IDs
df = df.dropna(subset=['CustomerID'])
# Create RFM features for clustering
# (Recency, Frequency, Monetary)
```

## Google Colab Users

All notebooks are designed to work in Google Colab. Datasets will download automatically to Colab's temporary storage. Note:

- Colab storage is **temporary** (resets on disconnect)
- Re-run download cells when reconnecting
- For large datasets, consider mounting Google Drive

```python
# Mount Google Drive in Colab
from google.colab import drive
drive.mount('/content/drive')

# Download to persistent Drive location
data_path = '/content/drive/MyDrive/ml_datasets/'
```

## Licensing

All datasets used in this curriculum are:
- Publicly available for educational use
- From reputable sources (UCI, Kaggle, academic institutions)
- Properly attributed in notebooks

Please review individual dataset licenses before commercial use:
- **MNIST**: Public domain
- **CIFAR-10/100**: MIT License
- **CelebA**: Non-commercial research only
- **MovieLens**: For non-commercial use
- **Credit Card Fraud**: Database Contents License (DbCL) v1.0
- **20 Newsgroups**: Public domain

## Troubleshooting

### Download Fails

If automatic downloads fail:

1. **Check internet connection**
2. **Manual download**: Follow links above and place in `data/`
3. **Firewall/proxy**: Configure Python requests library

### Kaggle Datasets

For Kaggle datasets (e.g., Credit Card Fraud):

1. Create account at https://www.kaggle.com
2. Go to Account → API → Create New API Token
3. Place `kaggle.json` in `~/.kaggle/`
4. Use Kaggle CLI: `kaggle datasets download -d mlg-ulb/creditcardfraud`

### Storage Issues

If running out of disk space:

- Download only required lesson datasets
- Use smaller dataset versions (e.g., MNIST subset)
- Clean up after completing lessons: `rm -rf data/cifar-10-*`

### Google Colab Storage

Colab provides ~100 GB temporary storage:

```python
# Check available space
!df -h
```

## Contributing

To add a new dataset:

1. Update this README with dataset information
2. Add automatic download code to relevant notebook
3. Include licensing information
4. Test download on fresh environment

## Questions?

If you have issues with datasets:

1. Check notebook code comments
2. Review this README
3. Open an issue on GitHub with:
   - Dataset name
   - Error message
   - Environment (local/Colab)

---

**Last Updated**: 2025
**Maintained by**: Powell-Clark Limited
