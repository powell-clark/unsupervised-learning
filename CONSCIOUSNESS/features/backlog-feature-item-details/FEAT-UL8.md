# FEAT-UL8: Anomaly Detection Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Comprehensive lesson on anomaly detection: Isolation Forest, Local Outlier Factor (LOF), One-Class SVM, and autoencoder-based detection. Covers isolation principle, density-based anomalies, and reconstruction-based approaches.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: Anomaly vs outlier definitions
- [x] **AC-2** — Theory notebook: Isolation Forest: recursive partitioning and anomaly score
- [x] **AC-3** — Theory notebook: LOF: k-distance, reachability distance, local density
- [x] **AC-4** — Theory notebook: One-Class SVM: support vector representation
- [x] **AC-5** — Practical notebook: scikit-learn Isolation Forest implementation
- [x] **AC-6** — Practical notebook: Local Outlier Factor with parameter selection
- [x] **AC-7** — Practical notebook: One-Class SVM for anomaly detection
- [x] **AC-8** — Practical notebook: PyTorch autoencoder for fraud/outlier detection
- [x] **AC-9** — Practical notebook: Fraud detection case study (credit card, banking) — notebook title itself is "Fraud Detection with Isolation Forest, LOF, One-Class SVM"
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab — verified via jupyter execute under TASK-UL040, 8/8 and 8/8 cells, zero errors
- [x] **AC-11** — Reconstruction error as anomaly signal (autoencoders)
- [x] **AC-12** — Completed task pair: TASK-UL15 (theory) and TASK-UL16 (practical)

## Review (TASK-UL041)
Independent agent review against notebooks/7a_anomaly_detection_theory.ipynb
and 7b_anomaly_detection_practical.ipynb: all 12 criteria verified via
section headers, each mapping directly to a named table-of-contents entry
(iforest/lof/ocsvm theory+scratch+sklearn, autoencoder, reconstruction-error,
pr-auc). agent-approved — stays in backlog pending human sign-off per the
FEAT-UL14 precedent.

## Linked Entities
- Story: STORY-UL8 (Anomaly detection learner story)
- Directive: DIRECT-UL8 (Anomaly Detection)
- Tasks: TASK-UL15, TASK-UL16
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
