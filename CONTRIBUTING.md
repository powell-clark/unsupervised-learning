# Contributing to Unsupervised Machine Learning

Thank you for your interest in contributing to this educational repository! This guide will help you contribute effectively.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Notebook Structure](#notebook-structure)
- [Code Style](#code-style)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project follows a code of conduct that promotes a welcoming and inclusive environment:

- Be respectful and considerate in all interactions
- Focus on what is best for the community and learners
- Show empathy toward other community members
- Accept constructive criticism gracefully

## How to Contribute

### Types of Contributions

We welcome several types of contributions:

1. **New Lesson Implementations** - Implementing planned but incomplete lessons
2. **Bug Fixes** - Fixing errors in existing notebooks or code
3. **Documentation Improvements** - Clarifying explanations or fixing typos
4. **Dataset Scripts** - Adding data download and preprocessing scripts
5. **Testing** - Adding tests for implementations
6. **Visualizations** - Improving or adding new visualizations
7. **Examples** - Adding real-world application examples

### Before You Start

- Check existing issues and pull requests to avoid duplication
- For major changes, open an issue first to discuss your approach
- Read the [CURRICULUM_PLAN.md](./CURRICULUM_PLAN.md) to understand the overall structure

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Installation

```bash
# Clone the repository
git clone https://github.com/powell-clark/unsupervised-machine-learning.git
cd unsupervised-machine-learning

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy jupyter
```

### Verify Installation

```bash
# Run existing notebooks
jupyter notebook notebooks/

# Run tests (when available)
pytest tests/
```

## Notebook Structure

All lessons follow a consistent structure with two notebooks:

### Theory Notebook (Xa_topic_theory.ipynb)

1. **Introduction** - Real-world motivation and story
2. **Mathematical Foundations** - Derivations from first principles
3. **Algorithm Explanation** - Step-by-step algorithm breakdown
4. **From-Scratch Implementation** - NumPy implementation with type hints
5. **Simple Examples** - Synthetic data demonstrating concepts
6. **Visualizations** - Plots showing algorithm behavior
7. **Mathematical Analysis** - Convergence, complexity, limitations
8. **Conclusion** - Summary and when to use

### Practical Notebook (Xb_topic_practical.ipynb)

1. **Introduction** - Brief recap and goals
2. **Real Dataset** - Loading and exploring real-world data
3. **Production Library Implementation** - Using scikit-learn/PyTorch/etc.
4. **Algorithm Comparison** - Comparing multiple approaches
5. **Hyperparameter Tuning** - Systematic parameter optimization
6. **Evaluation** - Comprehensive metrics and analysis
7. **Production Considerations** - Deployment, monitoring, ethics
8. **Conclusion** - Summary and next steps

### Cell Organization

```python
# 1. Library imports (first cell)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# ... other imports

# Set random seed for reproducibility
np.random.seed(42)

# 2. Markdown cells with LaTeX for theory
## Cost Function
The cost function is:
$$J(\theta) = \frac{1}{2m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2$$

# 3. Implementation cells with docstrings and type hints
def gradient_descent(X: NDArray, y: NDArray, learning_rate: float = 0.01) -> NDArray:
    """
    Perform gradient descent optimization.

    Args:
        X: Feature matrix of shape (n_samples, n_features)
        y: Target vector of shape (n_samples,)
        learning_rate: Learning rate for gradient descent

    Returns:
        Optimized parameters of shape (n_features,)
    """
    # Implementation here
    pass

# 4. Visualization cells
plt.figure(figsize=(10, 6))
plt.plot(X, y, 'o', label='Data')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.show()
```

## Code Style

### Python Code

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable names (no single letters except in mathematical context)
- Maximum line length: 100 characters
- Use type hints for function signatures
- Write comprehensive docstrings for all functions and classes

Example:
```python
from typing import Tuple
from numpy.typing import NDArray

def kmeans_clustering(
    X: NDArray,
    n_clusters: int = 3,
    max_iters: int = 100,
    random_state: int = 42
) -> Tuple[NDArray, NDArray]:
    """
    Perform K-Means clustering from scratch.

    Args:
        X: Data matrix of shape (n_samples, n_features)
        n_clusters: Number of clusters to form
        max_iters: Maximum number of iterations
        random_state: Random seed for reproducibility

    Returns:
        centroids: Cluster centers of shape (n_clusters, n_features)
        labels: Cluster assignment for each sample of shape (n_samples,)

    Raises:
        ValueError: If n_clusters > n_samples
    """
    # Implementation
    pass
```

### Notebook Best Practices

1. **One logical operation per cell** - Don't combine unrelated operations
2. **Clear section headers** - Use Markdown headers to organize content
3. **Reproducible** - Set random seeds, document versions
4. **No hidden state** - Cells should be runnable in order without dependencies
5. **Informative outputs** - Add print statements showing progress/results
6. **Clean up** - Remove debugging code and unused cells

### Mathematical Notation

Use consistent LaTeX notation:

- Vectors: lowercase bold $\mathbf{x}$ or $\vec{x}$
- Matrices: uppercase bold $\mathbf{X}$ or $X$
- Scalars: regular $x$, $y$, $\theta$
- Sets: $\mathcal{X}$, $\mathcal{Y}$
- Indices: $i$, $j$, $k$
- Summations: $\sum_{i=1}^n$
- Expectations: $\mathbb{E}[\cdot]$

## Testing

### Test Coverage Required

All from-scratch implementations should have tests:

```python
# tests/test_clustering.py
import numpy as np
import pytest
from your_module import kmeans_clustering

def test_kmeans_basic():
    """Test K-means on simple 2D data."""
    X = np.array([[1, 1], [1, 2], [10, 10], [10, 11]])
    centroids, labels = kmeans_clustering(X, n_clusters=2)

    # Check shapes
    assert centroids.shape == (2, 2)
    assert labels.shape == (4,)

    # Check that points are correctly clustered
    assert labels[0] == labels[1]
    assert labels[2] == labels[3]
    assert labels[0] != labels[2]

def test_kmeans_convergence():
    """Test that K-means converges."""
    X = np.random.randn(100, 2)
    centroids, labels = kmeans_clustering(X, n_clusters=3)

    # Should not raise any errors and should converge
    assert len(np.unique(labels)) <= 3
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_clustering.py

# Run with coverage
pytest --cov=src tests/
```

## Pull Request Process

### 1. Fork and Branch

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR-USERNAME/unsupervised-machine-learning.git
cd unsupervised-machine-learning

# Create a feature branch
git checkout -b feature/add-kmeans-lesson
```

### 2. Make Changes

- Implement your changes following the style guide
- Add or update tests
- Update documentation if needed
- Ensure notebooks run without errors

### 3. Test Your Changes

```bash
# Run tests
pytest tests/

# Check code style
black --check .
flake8 .

# Test notebooks run without errors
jupyter nbconvert --to notebook --execute notebooks/your_notebook.ipynb
```

### 4. Commit and Push

```bash
# Stage your changes
git add .

# Commit with a clear message
git commit -m "feat: Add Lesson 1 K-Means theory notebook

- Implement Lloyd's algorithm from scratch
- Add mathematical derivations for cost function
- Include convergence analysis
- Add visualizations of clustering process"

# Push to your fork
git push origin feature/add-kmeans-lesson
```

### 5. Create Pull Request

- Go to the original repository on GitHub
- Click "New Pull Request"
- Select your fork and branch
- Fill out the PR template:
  - **Title**: Clear, concise description
  - **Description**: What changes, why, how to test
  - **Related Issues**: Link any relevant issues
  - **Checklist**: Confirm you've completed all steps

### PR Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] New lesson implementation
- [ ] Bug fix
- [ ] Documentation update
- [ ] Test addition
- [ ] Other (specify)

## Related Issues
Fixes #123

## Testing
Describe how you tested your changes:
- [ ] Ran all notebooks without errors
- [ ] Added/updated tests
- [ ] Tested on Google Colab

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Commented complex sections
- [ ] Updated documentation
- [ ] Added tests
- [ ] All tests pass
- [ ] No new warnings
```

### 6. Review Process

- Maintainers will review your PR
- Address any requested changes
- Once approved, your PR will be merged

## Lesson Implementation Guidelines

When implementing a new lesson, follow these steps:

### 1. Research Phase

- Read multiple sources (textbooks, papers, existing implementations)
- Understand the mathematical foundations
- Identify key algorithms and variants
- Find appropriate datasets

### 2. Theory Notebook

- Start with a compelling real-world story
- Derive algorithms from first principles
- Implement from scratch in NumPy
- Add comprehensive visualizations
- Include complexity analysis

### 3. Practical Notebook

- Use real-world datasets
- Implement with production libraries
- Compare multiple approaches
- Tune hyperparameters systematically
- Discuss deployment considerations

### 4. Review

- Ensure notebooks run top-to-bottom without errors
- Check all equations render correctly
- Verify code produces expected outputs
- Test on Google Colab
- Get feedback from peers

## Resources

### Learning Materials

- [CURRICULUM_PLAN.md](./CURRICULUM_PLAN.md) - Full curriculum specification
- [README.md](./README.md) - Project overview

### Style Guides

- [PEP 8](https://pep8.org/) - Python style guide
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [NumPy Docstring Standard](https://numpydoc.readthedocs.io/)

### Tools

- [Black](https://black.readthedocs.io/) - Code formatter
- [Flake8](https://flake8.pycqa.org/) - Linter
- [MyPy](http://mypy-lang.org/) - Type checker
- [Pytest](https://pytest.org/) - Testing framework

## Questions?

If you have questions:

1. Check existing issues and discussions
2. Read the documentation
3. Open a new issue with the "question" label
4. Reach out to maintainers

Thank you for contributing to making machine learning education accessible to everyone!
