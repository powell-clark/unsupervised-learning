# DIRECT-UL2: K-Means Clustering

## Context

K-Means is the most widely used clustering algorithm in practice. TASK-UL3 derives Lloyd's algorithm and K-Means++ initialization from first principles. TASK-UL4 applies scikit-learn and explores mini-batch K-Means for large datasets.

## Acceptance Criteria

- [ ] TASK-UL3 (0a theory) complete — Lloyd's algorithm derivation, K-Means++ initialization
- [ ] TASK-UL4 (0b practical) complete — scikit-learn, mini-batch variants, real-world datasets
- [ ] Both notebooks run in Colab
- [ ] From-scratch implementations verified against scikit-learn
- [ ] FEAT-UL1 and FEAT-UL2 satisfied

## Technical Notes

Topics: centroid updates, convergence, complexity, initialization strategies (Lloyd's, K-Means++), extensions (mini-batch, fuzzy K-Means). Implementation: numpy derivation, then scikit-learn production version.

## Dependencies

- Blocked by: DIRECT-UL1 (Clustering Foundations)
- Blocks: DIRECT-UL13 (Professional Practice — clustering comparison)
