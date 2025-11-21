"""
Tests for clustering algorithms (Lessons 0-4).

Tests cover:
- K-Means clustering
- Hierarchical clustering
- DBSCAN
- Gaussian Mixture Models
"""

import numpy as np
import pytest
from sklearn.datasets import make_blobs


class TestKMeans:
    """Tests for K-Means clustering implementation."""

    def test_kmeans_basic(self):
        """Test K-means on simple 2D data."""
        # TODO: Implement when Lesson 1 is complete
        pytest.skip("Lesson 1 (K-Means) not yet implemented")

    def test_kmeans_convergence(self):
        """Test that K-means converges."""
        pytest.skip("Lesson 1 (K-Means) not yet implemented")

    def test_kmeans_initialization(self):
        """Test K-means++ initialization."""
        pytest.skip("Lesson 1 (K-Means) not yet implemented")


class TestHierarchical:
    """Tests for Hierarchical clustering implementation."""

    def test_hierarchical_linkage(self):
        """Test different linkage methods."""
        pytest.skip("Lesson 2 (Hierarchical) not yet implemented")

    def test_dendrogram_construction(self):
        """Test dendrogram construction."""
        pytest.skip("Lesson 2 (Hierarchical) not yet implemented")


class TestDBSCAN:
    """Tests for DBSCAN implementation."""

    def test_dbscan_basic(self):
        """Test DBSCAN on non-convex clusters."""
        pytest.skip("Lesson 3 (DBSCAN) not yet implemented")

    def test_dbscan_noise_detection(self):
        """Test noise point identification."""
        pytest.skip("Lesson 3 (DBSCAN) not yet implemented")


class TestGMM:
    """Tests for Gaussian Mixture Models implementation."""

    def test_gmm_em_algorithm(self):
        """Test EM algorithm convergence."""
        pytest.skip("Lesson 4 (GMM) not yet implemented")

    def test_gmm_covariance_types(self):
        """Test different covariance matrix types."""
        pytest.skip("Lesson 4 (GMM) not yet implemented")


# Add more tests as lessons are implemented
