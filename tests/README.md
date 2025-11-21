# Tests

This directory contains tests for all unsupervised machine learning implementations.

## Running Tests

### Run All Tests

```bash
pytest tests/
```

### Run Specific Test Files

```bash
# Test clustering algorithms
pytest tests/test_clustering.py

# Test dimensionality reduction
pytest tests/test_dimensionality.py

# Test recommender systems
pytest tests/test_recommenders.py

# Test generative models
pytest tests/test_generative.py
```

### Run Tests by Category

```bash
# Run only clustering tests
pytest -m clustering

# Run only unit tests (not slow integration tests)
pytest -m "not slow"
```

### Run with Coverage

```bash
# Generate coverage report
pytest --cov=src --cov-report=html tests/

# View report
open htmlcov/index.html
```

## Test Structure

```
tests/
├── __init__.py
├── README.md (this file)
├── test_clustering.py       # Lessons 0-4: Clustering algorithms
├── test_dimensionality.py   # Lessons 5-6: PCA, t-SNE, UMAP
├── test_recommenders.py     # Lesson 8: Recommender systems
├── test_generative.py       # Lessons 12-14: Autoencoders, GANs, Diffusion
└── conftest.py              # Shared pytest fixtures (to be added)
```

## Writing Tests

### Test Naming Convention

- Test files: `test_<topic>.py`
- Test classes: `Test<Algorithm>`
- Test functions: `test_<specific_behavior>`

Example:
```python
class TestKMeans:
    def test_kmeans_convergence(self):
        """Test that K-means converges."""
        # Test implementation
```

### Test Categories

Use pytest markers to categorize tests:

```python
import pytest

@pytest.mark.slow
def test_large_dataset():
    """Test that takes >1 second."""
    pass

@pytest.mark.clustering
def test_kmeans_basic():
    """Test K-means clustering."""
    pass
```

### Fixtures

Add shared test fixtures in `conftest.py`:

```python
import pytest
import numpy as np

@pytest.fixture
def simple_clusters():
    """Generate simple 2D clustered data."""
    from sklearn.datasets import make_blobs
    X, y = make_blobs(n_samples=300, centers=3, random_state=42)
    return X, y
```

## Test Implementation Status

### ✅ Implemented
- None yet (tests created, waiting for implementations)

### 🚧 In Progress
- `test_recommenders.py` - Lesson 8 complete, need to refactor code from notebooks

### ⬜ Planned
- `test_clustering.py` - Waiting for Lessons 0-4
- `test_dimensionality.py` - Waiting for Lessons 5-6
- `test_generative.py` - Waiting for Lessons 12-14

## Testing Strategy

### Unit Tests
Test individual functions and classes:
- Algorithm correctness
- Edge cases
- Error handling
- Input validation

### Integration Tests
Test complete workflows:
- End-to-end pipelines
- Multiple algorithms combined
- Real dataset processing

### Comparison Tests
Compare custom implementations against scikit-learn:
- Results should match (within numerical tolerance)
- Performance benchmarks
- API compatibility

## Continuous Integration

Tests run automatically on:
- Pull requests
- Merges to main branch
- Nightly builds (once implemented)

See `.github/workflows/tests.yml` for CI configuration (to be added).

## Code Coverage Goals

Target coverage by component:
- Core algorithms: >90%
- Utility functions: >80%
- Visualization code: >60%
- Notebooks: N/A (tested manually)

Current coverage: To be determined

## Contributing Tests

When implementing a new lesson:

1. Write tests **before** implementation (TDD)
2. Test both from-scratch and library implementations
3. Include edge cases and error conditions
4. Add docstrings explaining what's tested
5. Mark slow tests with `@pytest.mark.slow`
6. Update this README

See [CONTRIBUTING.md](../CONTRIBUTING.md) for full guidelines.

## Troubleshooting

### Tests Not Found

```bash
# Ensure pytest can find the tests
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pytest tests/
```

### Import Errors

```bash
# Install in development mode
pip install -e .
```

### Skipped Tests

Many tests are currently skipped with `pytest.skip()` because lessons aren't implemented yet. This is expected - tests will activate as implementations are added.

To see skip reasons:
```bash
pytest -v tests/
```

## Questions?

- Review [pytest documentation](https://docs.pytest.org/)
- Check [CONTRIBUTING.md](../CONTRIBUTING.md)
- Open an issue on GitHub

---

**Last Updated**: 2025
