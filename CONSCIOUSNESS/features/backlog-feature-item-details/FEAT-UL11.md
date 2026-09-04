# FEAT-UL11: Self-Organizing Maps Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p4

## Description
Comprehensive lesson on Self-Organizing Maps (SOMs): competitive learning, neighborhood functions, topological ordering, and U-Matrix visualization. Covers biological inspiration alongside practical grid-based neural networks.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: Kohonen networks and competitive learning principle
- [x] **AC-2** — Theory notebook: Neighborhood functions (Gaussian, bubble, triangle)
- [x] **AC-3** — Theory notebook: Topological ordering and organization properties
- [x] **AC-4** — Theory notebook: Weight update rule and convergence
- [x] **AC-5** — Practical notebook: MiniSom library implementation
- [x] **AC-6** — Practical notebook: SOM training workflow (initialization, learning schedule)
- [x] **AC-7** — Practical notebook: U-Matrix visualization for cluster boundaries
- [x] **AC-8** — Practical notebook: Hit maps and component planes
- [x] **AC-9** — Practical notebook: Data clustering and visualization case study
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab — verified via jupyter execute under TASK-UL040, 6/6 and 7/7 cells, zero errors
- [x] **AC-11** — Biological SOM motivation and emergent properties — confirmed via keyword search (Kohonen, neuron terminology present)
- [x] **AC-12** — Completed task pair: TASK-UL23 (theory) and TASK-UL24 (practical)

## Review (TASK-UL041)
Independent agent review against notebooks/11a_self_organizing_maps_theory.ipynb
and 11b_self_organizing_maps_practical.ipynb: all 12 criteria verified via
section headers (u-matrix, component-planes, competitive-learning all named
directly) plus keyword search for biological-motivation coverage.
agent-approved — stays in backlog pending human sign-off per the
FEAT-UL14 precedent.

## Linked Entities
- Story: STORY-UL12 (SOM learner story)
- Directive: DIRECT-UL11 (Self-Organizing Maps)
- Tasks: TASK-UL23, TASK-UL24
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
