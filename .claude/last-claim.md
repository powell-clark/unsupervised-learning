# Just claimed: TASK-UL1

Claim time: 2026-07-01T10:31:02.990Z

---

## Task card

# TASK-UL1: Clustering foundations theory (0a)

## Context
First notebook of Lesson 0 (STORY-UL1). Establishes what unsupervised learning
is and how to measure distance/similarity — the foundation for every clustering
algorithm that follows.

## Acceptance Criteria
- [ ] Explain unsupervised vs supervised learning with intuition and examples
- [ ] Derive/compare Euclidean, Manhattan, and Cosine similarity
- [ ] Demonstrate the curse of dimensionality in clustering
- [ ] Visualise the Iris dataset without labels
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Dataset: Iris (unlabelled). Libraries: NumPy, Matplotlib, scikit-learn (for
loading only). Story-driven intro before mathematics, per house pedagogy.

## Dependencies
- Blocked by: none
- Blocks: TASK-UL2


---

## Parent story card

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
- [ ] 0a: unsupervised vs supervised framing; Euclidean/Manhattan/Cosine metrics; curse of dimensionality; Iris (unlabelled) visualisation
- [ ] 0b: internal metrics (silhouette, Davies-Bouldin, Calinski-Harabasz); external metrics (ARI, NMI); elbow and gap statistic for choosing K
- [ ] Both notebooks run in Colab (FEAT-UL1)
- [ ] From-scratch metric implementations plus scikit-learn cross-check (FEAT-UL2)

## Tasks
- TASK-UL1 — 0a clustering foundations theory
- TASK-UL2 — 0b cluster evaluation

## Dependencies
- Blocked by: none — this is the starting point
- Blocks: STORY-UL2 (K-Means) and all downstream clustering lessons
