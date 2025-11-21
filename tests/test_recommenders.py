"""
Tests for recommender systems (Lesson 8).

Tests cover:
- Collaborative filtering
- Matrix factorization
- Recommender evaluation metrics
"""

import numpy as np
import pytest


class TestCollaborativeFiltering:
    """Tests for collaborative filtering implementation."""

    def test_cf_basic(self):
        """Test basic collaborative filtering on toy data."""
        # Create simple rating matrix
        R = np.array([[1, 0, 0, 1],
                      [0, 1, 1, 0],
                      [1, 0, 0, 1],
                      [0, 1, 1, 0]])
        Y = np.array([[5, 0, 0, 4],
                      [0, 4, 5, 0],
                      [5, 0, 0, 4],
                      [0, 4, 5, 0]])

        # TODO: Test CollaborativeFiltering class from Lesson 8a
        # This is a placeholder - update when importing from notebooks
        pytest.skip("Need to refactor CollaborativeFiltering class from notebook into module")

    def test_cf_predictions(self):
        """Test prediction accuracy."""
        pytest.skip("Need to refactor code from notebooks")

    def test_similar_items(self):
        """Test finding similar items."""
        pytest.skip("Need to refactor code from notebooks")


class TestMatrixFactorization:
    """Tests for matrix factorization approaches."""

    def test_gradient_descent_convergence(self):
        """Test gradient descent converges."""
        pytest.skip("Need to refactor code from notebooks")

    def test_regularization(self):
        """Test regularization prevents overfitting."""
        pytest.skip("Need to refactor code from notebooks")


# Note: Lesson 8 is implemented but code is in notebooks.
# To enable these tests, refactor implementations into src/recommenders.py
