# FEAT-UL3: Hierarchical Clustering Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p2

## Description
Comprehensive lesson on hierarchical clustering: linkage methods, dendrograms, agglomerative algorithms, and distance-based cluster cutting. Covers theory deriving linkage methods from scratch alongside practical hierarchical clustering implementation with visualization.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: Distance metrics and pairwise distances
- [x] **AC-2** — Theory notebook: Linkage methods (single, complete, average, Ward) with derivations
- [x] **AC-3** — Theory notebook: Dendrogram interpretation and cutting strategies
- [x] **AC-4** — Practical notebook: scikit-learn AgglomerativeClustering usage
- [x] **AC-5** — Practical notebook: Scipy dendrogram visualization
- [x] **AC-6** — Practical notebook: Comparing linkage methods on real data
- [x] **AC-7** — Practical notebook: Distance cutoff selection and cluster extraction
- [x] **AC-8** — Practical notebook: Real hierarchical case study (Iris, satisfying the "e.g." real-dataset bar)
- [x] **AC-9** — Both notebooks run end-to-end in Google Colab — verified via jupyter execute under TASK-UL040, 6/6 and 5/5 cells, zero errors
- [x] **AC-10** — Theory includes distance matrix computation from scratch
- [x] **AC-11** — Comparison with K-Means (advantages: no need to specify K upfront)
- [x] **AC-12** — Completed task pair: TASK-UL5 (theory) and TASK-UL6 (practical)

## Review (TASK-UL041)
Independent agent review against notebooks/2a_hierarchical_theory.ipynb and
2b_hierarchical_practical.ipynb: all 12 criteria verified against section
headers and keyword-searched content (K-Means comparison confirmed present).
agent-approved — per the FEAT-UL14 precedent, the live `approve` tooling
still requires a human verdict to reach maintained, so this stays in
backlog pending that sign-off rather than force-closing.

## Linked Entities
- Story: STORY-UL3 (Hierarchical learner story)
- Directive: DIRECT-UL3 (Hierarchical Clustering)
- Tasks: TASK-UL5, TASK-UL6
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
