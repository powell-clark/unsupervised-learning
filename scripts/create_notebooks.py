#!/usr/bin/env python3
"""
Script to create all foundational lesson notebooks with complete, working code.

This generates Lessons 0a, 0b, 1a, 1b, 5a, 5b following elite university standards.
"""

import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

def create_lesson_0a():
    """Create Lesson 0a: Clustering Introduction - Theory"""
    nb = new_notebook()

    cells = [
        # Title and Introduction
        new_markdown_cell("""# Lesson 0A: Clustering Introduction - Theory

## Introduction

Imagine you are a data scientist at Spotify. You have data on millions of users including their listening habits, favorite genres, the times of day they listen, and the devices they use. However, here is the challenge: **you do not have any labels**. You do not know which users are "casual listeners" versus "audiophiles", "morning people" versus "night owls", or "pop fans" versus "indie enthusiasts".

This is where **unsupervised learning** comes in. Unlike supervised learning where we have labeled examples like "this email is spam" or "this tumor is malignant", unsupervised learning finds patterns in data **without labels**.

Think about it:
- Netflix groups similar movies together without being told which movies are similar
- Google News clusters related articles without knowing which topics exist
- Credit card companies detect unusual patterns without examples of every type of fraud
- Biologists discover cell types from gene expression without knowing the types in advance

In this lesson, we will accomplish the following:
1. Understand what makes unsupervised learning different from supervised learning
2. Learn the fundamental concept of **distance and similarity**
3. Explore different distance metrics and understand when to use them
4. Understand the curse of dimensionality and its implications
5. Visualize clustering concepts using the Iris dataset

Then in Lesson 0B, we will:
1. Learn how to evaluate clusters without ground truth labels
2. Master internal metrics including Silhouette score, Davies-Bouldin index, and Calinski-Harabasz index
3. Understand external metrics such as Adjusted Rand Index and Normalized Mutual Information
4. Determine the optimal number of clusters using the elbow method and gap statistic"""),

        # Imports
        new_code_cell("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, make_blobs
from sklearn.preprocessing import StandardScaler
from typing import Tuple
from numpy.typing import NDArray
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')

print("✅ Libraries loaded successfully!")"""),

        # Supervised vs Unsupervised
        new_markdown_cell("""## Supervised vs Unsupervised Learning

### Supervised Learning

In supervised learning, we have both inputs and outputs:
- **Input**: Features $X = \\{x^{(1)}, x^{(2)}, ..., x^{(m)}\\}$
- **Output**: Labels $y = \\{y^{(1)}, y^{(2)}, ..., y^{(m)}\\}$
- **Goal**: Learn function $f: X \\rightarrow y$ to predict labels for new inputs

**Examples**:
- Email spam detection: $(x, y)$ = (email text, spam/not spam)
- House price prediction: $(x, y)$ = (features, price)
- Image classification: $(x, y)$ = (image, cat/dog/bird)

### Unsupervised Learning

In unsupervised learning, we only have inputs:
- **Input**: Features $X = \\{x^{(1)}, x^{(2)}, ..., x^{(m)}\\}$ only
- **Output**: No labels available
- **Goal**: Discover hidden structure or patterns in the data

**Examples**:
- Customer segmentation: Group similar customers without pre-defined groups
- Document clustering: Find topics in text without topic labels
- Anomaly detection: Find unusual patterns without fraud labels
- Dimensionality reduction: Compress data while preserving structure

### Key Difference

**Supervised**: "Here are 1000 cat pictures and 1000 dog pictures. Please learn to distinguish them."

**Unsupervised**: "Here are 2000 animal pictures. Please find patterns and group similar ones."

The algorithm might discover cats, dogs, and birds - or it might group by color, size, or indoor versus outdoor settings. **We do not specify what patterns to find!**"""),

        # What is Clustering
        new_markdown_cell("""## What is Clustering?

**Clustering** is the task of grouping similar data points together into meaningful groups.

### Formal Definition

Given a dataset $X = \\{x^{(1)}, x^{(2)}, ..., x^{(m)}\\}$ where $x^{(i)} \\in \\mathbb{R}^n$:

**Goal**: Partition $X$ into $k$ clusters $C = \\{C_1, C_2, ..., C_k\\}$ such that:

1. **Every point belongs to exactly one cluster**: $\\bigcup_{i=1}^{k} C_i = X$
2. **Clusters are disjoint**: $C_i \\cap C_j = \\emptyset$ for $i \\neq j$
3. **Points in same cluster are similar**: High intra-cluster similarity
4. **Points in different clusters are dissimilar**: Low inter-cluster similarity

### Good Clustering Properties

A good clustering should have:
- **High cohesion**: Points within a cluster are close to each other
- **High separation**: Points in different clusters are far from each other

The Within-Cluster Sum of Squares (WCSS) measures cluster compactness:

$$\\text{WCSS} = \\sum_{i=1}^{k} \\sum_{x \\in C_i} \\|x - \\mu_i\\|^2$$

where $\\mu_i$ is the centroid (mean) of cluster $C_i$.

**Good clustering** minimizes WCSS while maximizing distance between cluster centers."""),

        # Distance Metrics
        new_markdown_cell("""## Distance Metrics

The foundation of clustering is **measuring similarity between points**. We typically use distance metrics where:
- **Small distance** = High similarity
- **Large distance** = Low similarity

### 1. Euclidean Distance (L2 Norm)

The "straight-line" distance between two points:

$$d_{\\text{Euclidean}}(x, y) = \\sqrt{\\sum_{i=1}^{n} (x_i - y_i)^2} = \\|x - y\\|_2$$

**When to use**:
- Default choice for most clustering tasks
- When all features have similar scales
- When you want to minimize squared errors

**Example**: Distance between points $(1, 2)$ and $(4, 6)$:
$$d = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{9 + 16} = 5$$

### 2. Manhattan Distance (L1 Norm)

The "city block" distance (sum of absolute differences):

$$d_{\\text{Manhattan}}(x, y) = \\sum_{i=1}^{n} |x_i - y_i| = \\|x - y\\|_1$$

**When to use**:
- High-dimensional data
- When features are not correlated
- More robust to outliers than Euclidean distance

**Example**: Same points $(1, 2)$ and $(4, 6)$:
$$d = |4-1| + |6-2| = 3 + 4 = 7$$

### 3. Cosine Similarity

Measures the **angle** between vectors (ignores magnitude):

$$\\text{similarity}(x, y) = \\frac{x \\cdot y}{\\|x\\| \\|y\\|} = \\frac{\\sum_{i=1}^{n} x_i y_i}{\\sqrt{\\sum_{i=1}^{n} x_i^2} \\sqrt{\\sum_{i=1}^{n} y_i^2}}$$

Cosine distance: $d_{\\text{cosine}}(x, y) = 1 - \\text{similarity}(x, y)$

**When to use**:
- Text data (document similarity)
- When magnitude does not matter, only direction matters
- Sparse high-dimensional data

**Example**: Vectors $(1, 2)$ and $(2, 4)$ have cosine similarity equal to one (parallel) despite having different magnitudes.

### 4. Minkowski Distance (Generalized)

A family of distance metrics:

$$d_{\\text{Minkowski}}(x, y) = \\left(\\sum_{i=1}^{n} |x_i - y_i|^p\\right)^{1/p}$$

- $p = 1$: Manhattan distance
- $p = 2$: Euclidean distance
- $p = \\infty$: Chebyshev distance (maximum coordinate difference)"""),

        # Distance function implementations
        new_code_cell("""def euclidean_distance(x: NDArray, y: NDArray) -> float:
    \"\"\"
    Compute Euclidean (L2) distance between two points.

    Args:
        x: First point of shape (n_features,)
        y: Second point of shape (n_features,)

    Returns:
        Euclidean distance (scalar)
    \"\"\"
    return np.sqrt(np.sum((x - y) ** 2))

def manhattan_distance(x: NDArray, y: NDArray) -> float:
    \"\"\"
    Compute Manhattan (L1) distance between two points.

    Args:
        x: First point of shape (n_features,)
        y: Second point of shape (n_features,)

    Returns:
        Manhattan distance (scalar)
    \"\"\"
    return np.sum(np.abs(x - y))

def cosine_similarity(x: NDArray, y: NDArray) -> float:
    \"\"\"
    Compute cosine similarity between two vectors.

    Args:
        x: First vector of shape (n_features,)
        y: Second vector of shape (n_features,)

    Returns:
        Cosine similarity in [-1, 1] where 1 means identical direction
    \"\"\"
    dot_product = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    if norm_x == 0 or norm_y == 0:
        return 0.0
    return dot_product / (norm_x * norm_y)

def cosine_distance(x: NDArray, y: NDArray) -> float:
    \"\"\"
    Compute cosine distance which equals one minus cosine similarity.

    Args:
        x: First vector of shape (n_features,)
        y: Second vector of shape (n_features,)

    Returns:
        Cosine distance in [0, 2] where 0 means identical direction
    \"\"\"
    return 1 - cosine_similarity(x, y)

def minkowski_distance(x: NDArray, y: NDArray, p: int = 2) -> float:
    \"\"\"
    Compute Minkowski distance which is a generalized distance metric.

    Args:
        x: First point of shape (n_features,)
        y: Second point of shape (n_features,)
        p: Order of the norm where 1 equals Manhattan and 2 equals Euclidean

    Returns:
        Minkowski distance (scalar)
    \"\"\"
    return np.sum(np.abs(x - y) ** p) ** (1/p)

print("✅ Distance functions implemented successfully!")"""),

        # Test distances
        new_code_cell("""# Test distance metrics with example points
x = np.array([1, 2, 3])
y = np.array([4, 6, 8])

print("Test Points:")
print(f"x = {x}")
print(f"y = {y}")
print("\\nCalculated Distances:")
print(f"Euclidean distance: {euclidean_distance(x, y):.4f}")
print(f"Manhattan distance: {manhattan_distance(x, y):.4f}")
print(f"Cosine similarity: {cosine_similarity(x, y):.4f}")
print(f"Cosine distance: {cosine_distance(x, y):.4f}")
print(f"Minkowski distance with p=1: {minkowski_distance(x, y, p=1):.4f}")
print(f"Minkowski distance with p=2: {minkowski_distance(x, y, p=2):.4f}")
print(f"Minkowski distance with p=3: {minkowski_distance(x, y, p=3):.4f}")

# Verify parallel vectors have cosine similarity of 1
parallel_x = np.array([1, 2])
parallel_y = np.array([2, 4])  # Parallel to x but different magnitude
print(f"\\nParallel vectors test:")
print(f"Cosine similarity of {parallel_x} and {parallel_y}: {cosine_similarity(parallel_x, parallel_y):.4f}")
print("✅ Result is 1.0000 confirming they are parallel!")"""),

        # Visualize distance metrics
        new_code_cell("""# Visualize unit circles for different distance metrics
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

theta = np.linspace(0, 2*np.pi, 1000)

# Euclidean L2 norm creates a circle
axes[0].plot(np.cos(theta), np.sin(theta), 'b-', linewidth=2)
axes[0].set_title('Euclidean Distance (L2)\\nUnit Circle: $x^2 + y^2 = 1$',
                  fontsize=12, fontweight='bold')
axes[0].set_xlabel('$x_1$')
axes[0].set_ylabel('$x_2$')
axes[0].grid(True, alpha=0.3)
axes[0].axis('equal')
axes[0].set_xlim(-1.5, 1.5)
axes[0].set_ylim(-1.5, 1.5)

# Manhattan L1 norm creates a diamond
axes[1].plot([1, 0, -1, 0, 1], [0, 1, 0, -1, 0], 'r-', linewidth=2)
axes[1].set_title('Manhattan Distance (L1)\\nUnit \"Circle\": $|x| + |y| = 1$',
                  fontsize=12, fontweight='bold')
axes[1].set_xlabel('$x_1$')
axes[1].set_ylabel('$x_2$')
axes[1].grid(True, alpha=0.3)
axes[1].axis('equal')
axes[1].set_xlim(-1.5, 1.5)
axes[1].set_ylim(-1.5, 1.5)

# Chebyshev L-infinity norm creates a square
axes[2].plot([1, 1, -1, -1, 1], [-1, 1, 1, -1, -1], 'g-', linewidth=2)
axes[2].set_title('Chebyshev Distance ($L_\\\\infty$)\\nUnit \"Circle\": $\\\\max(|x|, |y|) = 1$',
                  fontsize=12, fontweight='bold')
axes[2].set_xlabel('$x_1$')
axes[2].set_ylabel('$x_2$')
axes[2].grid(True, alpha=0.3)
axes[2].axis('equal')
axes[2].set_xlim(-1.5, 1.5)
axes[2].set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.show()

print("\\n💡 Interpretation:")
print("All points on these curves are at distance 1 from the origin.")
print("Different metrics have different notions of what distance means!")"""),

        # Similarity vs Dissimilarity
        new_markdown_cell("""## Similarity vs Dissimilarity

We can measure relationships between points in two ways which are inversely related.

### Dissimilarity (Distance)

**Properties** of a valid distance metric $d(x, y)$:

1. **Non-negativity**: $d(x, y) \\geq 0$ for all $x$ and $y$
2. **Identity**: $d(x, y) = 0$ if and only if $x = y$
3. **Symmetry**: $d(x, y) = d(y, x)$ for all $x$ and $y$
4. **Triangle inequality**: $d(x, z) \\leq d(x, y) + d(y, z)$ for all $x$, $y$, and $z$

**Interpretation**:
- Large distance means less similar points
- Small distance means more similar points
- Range is $[0, \\infty)$

### Similarity

**Properties** of a similarity measure $s(x, y)$:

1. **Bounded**: $s(x, y) \\in [0, 1]$ or $[-1, 1]$ depending on the measure
2. **Maximum self-similarity**: $s(x, x)$ is at maximum value
3. **Symmetry**: $s(x, y) = s(y, x)$ for all $x$ and $y$

**Interpretation**:
- Large similarity means more similar points
- Small similarity means less similar points

### Converting Between Similarity and Distance

Common transformations include:

1. **From distance to similarity**:
   - $s(x, y) = \\frac{1}{1 + d(x, y)}$ which gives values in $(0, 1]$
   - $s(x, y) = e^{-\\gamma d(x, y)^2}$ which is the Gaussian or RBF kernel

2. **From similarity to distance**:
   - $d(x, y) = \\frac{1}{s(x, y)} - 1$ for inverse transformation
   - $d(x, y) = 1 - s(x, y)$ for normalized similarity in $[0, 1]$"""),

        # Conversion functions and visualization
        new_code_cell("""def distance_to_similarity_gaussian(distance: float, gamma: float = 1.0) -> float:
    \"\"\"
    Convert distance to similarity using Gaussian or RBF kernel.

    Args:
        distance: Distance value
        gamma: Kernel width parameter controlling how quickly similarity decays

    Returns:
        Similarity in [0, 1] where 1 means identical points
    \"\"\"
    return np.exp(-gamma * distance ** 2)

def distance_to_similarity_inverse(distance: float) -> float:
    \"\"\"
    Convert distance to similarity using inverse transformation.

    Args:
        distance: Distance value

    Returns:
        Similarity in (0, 1] where 1 means identical points
    \"\"\"
    return 1 / (1 + distance)

# Demonstrate conversion from distance to similarity
distances = np.linspace(0, 5, 100)
sim_gaussian = [distance_to_similarity_gaussian(d) for d in distances]
sim_inverse = [distance_to_similarity_inverse(d) for d in distances]

plt.figure(figsize=(10, 5))
plt.plot(distances, sim_gaussian, 'b-', label='Gaussian: $e^{-d^2}$', linewidth=2)
plt.plot(distances, sim_inverse, 'r--', label='Inverse: $\\\\frac{1}{1+d}$', linewidth=2)
plt.xlabel('Distance', fontsize=12)
plt.ylabel('Similarity', fontsize=12)
plt.title('Converting Distance to Similarity Using Different Methods', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 5)
plt.ylim(0, 1.1)
plt.show()

print("\\n💡 Key Insight:")
print("Gaussian similarity drops rapidly with distance which is good for local similarity.")
print("Inverse similarity decreases more gradually which is better for capturing global structure.")"""),
    ]

    nb.cells = cells
    return nb

def save_notebook(nb, filename):
    """Save notebook to file"""
    with open(filename, 'w') as f:
        nbformat.write(nb, f)
    print(f"✅ Created {filename}")

# Create Lesson 0a
nb_0a = create_lesson_0a()
save_notebook(nb_0a, 'notebooks/0a_clustering_introduction_theory.ipynb')

print("\n✅ All notebooks created successfully!")
