# TASK-UL16: Anomaly Detection Practical (7b)

## Context
Second notebook of Lesson 7 (STORY-UL8, DIRECT-UL8). Applies the Isolation Forest, LOF, and
One-Class SVM from Lesson 7A to a fraud-detection-style dataset, then introduces a fourth,
reconstruction-based paradigm: a PyTorch autoencoder trained only on normal transactions,
flagged by reconstruction error.

## Acceptance Criteria
- [x] Fraud-style dataset: realistic class imbalance (rare positive class)
- [x] Apply Isolation Forest, LOF, and One-Class SVM from 7A to the dataset
- [x] PyTorch autoencoder: architecture, training on normal-only data
- [x] Reconstruction error as the anomaly score
- [x] Precision/recall/PR-AUC comparison across all four methods
- [x] Threshold selection without a labeled validation set
- [x] Visualization: reconstruction error distribution, precision-recall curves
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
Builds directly on TASK-UL15's three methods and dataset framing. The autoencoder is trained
exclusively on normal-labeled data (or assumed-normal if unlabeled), so a held-out anomaly
inflates reconstruction error at inference time. Emphasize that PR-AUC (not ROC-AUC) is the
right metric under severe class imbalance, and that threshold choice is a business decision,
not a purely statistical one, when no labeled validation set exists.

## Dependencies
- Blocked by: TASK-UL15 (anomaly detection theory)
- Blocks: DIRECT-UL13 (Professional Practice)
- Story: STORY-UL8 (Anomaly-detection learner story)
- Directive: DIRECT-UL8 (Anomaly Detection)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
