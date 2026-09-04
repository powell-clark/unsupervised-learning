# FEAT-UL7: Manifold Learning Lesson (t-SNE and UMAP)

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Comprehensive lesson on manifold learning: t-SNE and UMAP for visualization, preserving local and global structure, and hyperparameter tuning. Covers theory of neighborhood graphs and embedding algorithms.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: Manifold hypothesis and local/global structure
- [x] **AC-2** — Theory notebook: t-SNE: SNE to symmetric SNE to t-SNE derivation
- [x] **AC-3** — Theory notebook: UMAP: fuzzy topological structures and optimization
- [x] **AC-4** — Theory notebook: Differences between t-SNE and UMAP
- [x] **AC-5** — Practical notebook: scikit-learn TSNE implementation
- [x] **AC-6** — Practical notebook: UMAP library usage (installation, parameters)
- [x] **AC-7** — Practical notebook: Hyperparameter tuning (perplexity, n_neighbors, min_dist)
- [x] **AC-8** — Practical notebook: Interpreting 2D embeddings (clusters vs artifacts)
- [x] **AC-9** — Practical notebook: High-dimensional data visualization case study
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab — verified directly this session while fixing a real API-deprecation bug (scikit-learn 1.9.0 removed TSNE's `n_iter` in favour of `max_iter`, 4 occurrences across both notebooks), 5/5 and 5/5 cells, zero errors
- [x] **AC-11** — Caveats about visualization artifacts (clustering may be artificial)
- [x] **AC-12** — Completed task pair: TASK-UL13 (theory) and TASK-UL14 (practical)

## Review (TASK-UL041)
Independent agent review against notebooks/6a_manifold_learning_theory.ipynb
and 6b_manifold_learning_practical.ipynb: all 12 criteria verified directly
(this session fixed real execution bugs in both notebooks under TASK-UL040).
agent-approved. STORY-UL7's promotion out of backlog was explicitly
deferred under TASK-UL035 pending this review — now that FEAT-UL7 is
agent-approved, the story still cannot fulfil until a human approves this
feature (per the FEAT-UL14 precedent: live tooling requires it), so both
stay in backlog for now.

## Linked Entities
- Story: STORY-UL7 (Manifold learner story)
- Directive: DIRECT-UL7 (Manifold Learning)
- Tasks: TASK-UL13, TASK-UL14
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
