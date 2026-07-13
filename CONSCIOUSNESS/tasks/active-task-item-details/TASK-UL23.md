# TASK-UL23: Self-Organizing Maps Theory (11a)

## Context
First notebook of Lesson 11 (STORY-UL12, DIRECT-UL11). Introduces Self-Organizing Maps
(Kohonen, 1982) — a neural, competitive-learning algorithm that projects high-dimensional
data onto a low-dimensional (typically 2D) grid while preserving topology: points that are
close in the original space end up on nearby grid cells.

## Acceptance Criteria
- [ ] Competitive learning framing: neurons as a grid of weight vectors, winner-take-all
- [ ] Best Matching Unit (BMU): finding the winner neuron for an input
- [ ] Neighborhood function and its decay over training (Gaussian neighborhood, shrinking radius)
- [ ] Learning rate decay over training
- [ ] The SOM update rule: how the BMU and its neighbors move toward the input
- [ ] From-scratch NumPy implementation of SOM training
- [ ] Cross-check against a reference implementation
- [ ] Visualization: grid evolution over training, topology preservation on a known 2D/3D shape
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Unlike every clustering method so far, a SOM's neurons have a fixed spatial relationship to
each other (the grid topology) before training even starts — training doesn't just find
cluster centers, it arranges them so that neighboring grid cells end up representing similar
regions of the input space. This topology preservation is the SOM's defining property and
what U-Matrix visualization (Lesson 11B) exploits.

## Dependencies
- Blocked by: TASK-UL2 (foundations groundwork)
- Blocks: TASK-UL24 (Self-organizing maps practical)
- Story: STORY-UL12 (Self-organizing-map learner story)
- Directive: DIRECT-UL11 (Self-Organizing Maps)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
