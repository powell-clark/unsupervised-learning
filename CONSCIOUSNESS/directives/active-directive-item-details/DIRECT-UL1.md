# DIRECT-UL1: Ship complete unsupervised learning curriculum

## Context
The unsupervised-learning repository is the natural companion to the supervised
series. Its mission is to teach clustering, dimensionality reduction, density
estimation, and representation learning from first principles — deriving the
mathematics, implementing from scratch in NumPy, then applying production
Scikit-learn/PyTorch. CURRICULUM_PLAN.md lays out 13 lessons (0–12) plus an
X-series of professional-practice notebooks. Lesson 8 (Recommender Systems) is
already built; the rest are planned.

## Acceptance Criteria
- [x] Curriculum carded into PGPS as stories and tasks (STORY-UL1–UL14, TASK-UL1–UL30)
- [x] Lesson 8 (Recommender Systems) shipped — 8a theory + 8b practical
- [ ] Lesson 0 (Clustering Foundations) shipped as the true starting point
- [ ] Lessons 1–7, 9–12 shipped in curriculum sequence
- [ ] X-series (X1–X4) professional-practice notebooks shipped
- [ ] Every notebook runs in Google Colab (FEAT-UL1) with dual implementation (FEAT-UL2)

## Technical Notes
Each lesson is one story; each notebook is one task (a = theory, b = practical).
Execution follows curriculum order: Lesson 0 first, then Core Algorithms
(1–5), Dimensionality Reduction (6), Specialized Methods (7, 9), Advanced
Topics (10–12), and the X-series last. Lesson 8 shipped out of order.

## Dependencies
- Blocked by: none
- Blocks: none
