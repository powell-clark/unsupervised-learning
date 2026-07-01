# STORY-UL1: Clustering Foundations (Lesson 0)

*As a learner I want a foundations lesson on unsupervised learning, distance
metrics, and cluster evaluation so that I can judge cluster quality without
ground-truth labels.*

## Context
Lesson 0 is the true entry point to the curriculum — the conceptual and
evaluative groundwork every later clustering lesson depends on. It introduces
what unsupervised learning is, how distance/similarity is measured, the curse of
dimensionality, and — critically — how to evaluate clusters without labels.

## Acceptance Criteria
- [x] 0a: unsupervised vs supervised framing; Euclidean/Manhattan/Cosine metrics; curse of dimensionality; Iris (unlabelled) visualisation
- [x] 0b: internal metrics (silhouette, Davies-Bouldin, Calinski-Harabasz); external metrics (ARI, NMI); elbow and gap statistic for choosing K
- [x] Both notebooks run in Colab (FEAT-UL1)
- [x] From-scratch metric implementations plus scikit-learn cross-check (FEAT-UL2)

## Tasks
- TASK-UL1 — 0a clustering foundations theory
- TASK-UL2 — 0b cluster evaluation

## Dependencies
- Blocked by: none — this is the starting point
- Blocks: STORY-UL2 (K-Means) and all downstream clustering lessons
