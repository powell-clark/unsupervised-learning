---
id: FEAT-UL1
status: in_progress
priority: p2
kano: performance
title: Colab-runnable notebooks
description: Every lesson notebook runs end-to-end in Google Colab with one click and no local setup
acceptance_criteria:
  - Each notebook opens and runs top-to-bottom in Google Colab with no local setup
  - All dependencies install from the first cell (pip installs where needed)
  - Datasets download or generate inline; no manual file placement required
  - Plots and outputs render inline in the Colab runtime
stories: [STORY-UL1,STORY-UL2,STORY-UL3,STORY-UL4,STORY-UL5,STORY-UL6,STORY-UL7,STORY-UL8,STORY-UL9,STORY-UL10,STORY-UL11,STORY-UL12,STORY-UL13,STORY-UL14]
tasks: [TASK-UL1,TASK-UL2,TASK-UL3,TASK-UL4,TASK-UL5,TASK-UL6,TASK-UL7,TASK-UL8,TASK-UL9,TASK-UL10,TASK-UL11,TASK-UL12,TASK-UL13,TASK-UL14,TASK-UL15,TASK-UL16,TASK-UL17,TASK-UL18,TASK-UL19,TASK-UL20,TASK-UL21,TASK-UL22,TASK-UL23,TASK-UL24,TASK-UL25,TASK-UL26,TASK-UL27,TASK-UL28,TASK-UL29,TASK-UL30]
---

# FEAT-UL1: Colab-runnable notebooks

## Context
Accessibility is a core pedagogy promise: a learner should be able to open any
lesson in the browser and run it immediately, with zero environment setup. This
is a cross-cutting capability that every lesson notebook must satisfy.

## Acceptance Criteria
- [ ] Each notebook opens and runs top-to-bottom in Google Colab with no local setup
- [ ] All dependencies install from the first cell
- [ ] Datasets download or generate inline; no manual file placement
- [ ] Plots and outputs render inline in the Colab runtime

## Notes
Realised and demonstrated by the shipped Lesson 8 notebooks; maintained as a
standard across every future lesson.
