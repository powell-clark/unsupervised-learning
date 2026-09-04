# TASK-UL30: Semi-Supervised Learning (16)

## Context
Single-notebook Lesson 16 (STORY-UL14, DIRECT-UL13, FEAT-UL13) — the final lesson of the
curriculum. Bridges unsupervised and supervised learning: label propagation, self-training,
and co-training, for the common real-world case where a little labeled data exists alongside
a lot of unlabeled data.

## Acceptance Criteria
- [x] Framing: why semi-supervised learning exists (labeling cost vs abundant unlabeled data)
- [x] Label propagation: graph-based spread of labels through unlabeled data via similarity
- [x] Self-training: train on labeled data, iteratively add confidently-predicted unlabeled points
- [x] Empirical comparison: supervised-only (few labels) vs label propagation vs self-training, at varying labeled-fraction levels
- [x] Co-training: two views/feature-subsets teaching each other, with the assumption it requires (conditionally independent, sufficient views) — implemented from scratch (no production library), including the naive version's class-imbalance collapse and the balanced fix
- [x] Decision guide: when semi-supervised methods help vs when they don't (or actively hurt)
- [x] Runs top-to-bottom in Google Colab

Note: FEAT-UL13 also listed "active learning strategies" (choosing which points to label
next) under this lesson — a distinct topic from what's covered here (working with a fixed,
already-drawn labeled set). Deferred honestly as backlog TASK-UL039 rather than folded in
under a checked box for work not done.

## Technical Notes
The central risk this lesson must show honestly: semi-supervised methods can hurt as well as
help — self-training on confidently-wrong predictions reinforces its own errors, and label
propagation assumes the similarity graph actually reflects true class structure. Sweep the
labeled-data fraction to show where each method beats or loses to a supervised-only baseline
rather than asserting semi-supervised learning is unconditionally better.

## Dependencies
- Blocked by: TASK-UL2 (foundations groundwork)
- Blocks: none — closes DIRECT-UL13 and the curriculum
- Story: STORY-UL14 (Professional-practice learner story)
- Directive: DIRECT-UL13 (Professional Practice)
- Feature: FEAT-UL13 (Professional Practice Lesson), FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
