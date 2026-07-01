---
id: FEAT-UL2
status: in_progress
priority: p1
kano: must-have
title: From-scratch plus production dual implementation
description: Each lesson pairs a from-scratch NumPy derivation with a production Scikit-learn or PyTorch implementation
acceptance_criteria:
  - Each lesson has a theory notebook implementing the algorithm from scratch in NumPy
  - Each lesson has a practical notebook using production Scikit-learn or PyTorch
  - The from-scratch results are cross-checked against the production library
  - Mathematical derivation precedes code in the theory notebook
stories: [STORY-UL1,STORY-UL2,STORY-UL3,STORY-UL4,STORY-UL5,STORY-UL6,STORY-UL7,STORY-UL8,STORY-UL9,STORY-UL10,STORY-UL11,STORY-UL12,STORY-UL13,STORY-UL14]
tasks: [TASK-UL1,TASK-UL2,TASK-UL3,TASK-UL4,TASK-UL5,TASK-UL6,TASK-UL7,TASK-UL8,TASK-UL9,TASK-UL10,TASK-UL11,TASK-UL12,TASK-UL13,TASK-UL14,TASK-UL15,TASK-UL16,TASK-UL17,TASK-UL18,TASK-UL19,TASK-UL20,TASK-UL21,TASK-UL22,TASK-UL23,TASK-UL24,TASK-UL25,TASK-UL26,TASK-UL27,TASK-UL28,TASK-UL29,TASK-UL30]
---

# FEAT-UL2: From-scratch plus production dual implementation

## Context
The defining pedagogical pattern of the curriculum: derive the mathematics, then
implement the algorithm from scratch in NumPy to build intuition, then apply the
production library (Scikit-learn or PyTorch) that practitioners actually use.
Every lesson carries both halves.

## Acceptance Criteria
- [ ] Each lesson has a theory notebook implementing the algorithm from scratch in NumPy
- [ ] Each lesson has a practical notebook using production Scikit-learn or PyTorch
- [ ] From-scratch results are cross-checked against the production library
- [ ] Mathematical derivation precedes code in the theory notebook

## Notes
Realised and demonstrated by the shipped Lesson 8 notebooks (8a from-scratch
matrix factorization; 8b Surprise/Implicit/PyTorch); maintained across every
future lesson.
