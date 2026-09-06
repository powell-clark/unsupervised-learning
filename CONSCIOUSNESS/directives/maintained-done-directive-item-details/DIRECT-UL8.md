# DIRECT-UL8: Anomaly Detection

## Context

Anomaly detection identifies rare, unusual data points in unlabeled datasets. TASK-UL15 covers Isolation Forest, Local Outlier Factor (LOF), and one-class SVM. TASK-UL16 builds a PyTorch autoencoder for fraud detection on real transaction data.

## Acceptance Criteria

- [ ] TASK-UL15 (0a theory) complete — Isolation Forest, LOF, one-class SVM principles
- [ ] TASK-UL16 (0b practical) complete — scikit-learn methods, PyTorch autoencoder, fraud detection
- [ ] Both notebooks run in Colab
- [ ] From-scratch implementations verified
- [ ] FEAT-UL1 and FEAT-UL2 satisfied

## Technical Notes

Topics: isolation (random forest idea), local density, support vectors, neural networks, reconstruction error. Application: credit card fraud detection using real/synthetic transaction data.

## Dependencies

- Blocked by: DIRECT-UL1 (Clustering Foundations), potentially DIRECT-UL12 (Autoencoders) for advanced approach
- Blocks: DIRECT-UL13 (Professional Practice)
