# TASK-UL24: Self-Organizing Maps Practical (11b)

## Context
Second notebook of Lesson 11 (STORY-UL12, DIRECT-UL11). Applies MiniSom to a real dataset,
builds U-Matrix visualizations for finding cluster boundaries on the trained grid, and uses
component planes to inspect individual feature contributions across the map.

## Acceptance Criteria
- [ ] MiniSom applied end to end on a real (non-toy-synthetic) dataset
- [ ] U-Matrix construction and interpretation: average distance to grid-neighbors per neuron
- [ ] U-Matrix visualization revealing cluster boundaries as high-distance "walls"
- [ ] Component planes: per-feature heatmaps across the trained grid
- [ ] Comparing SOM-derived clusters against a known clustering method (e.g. K-Means) on the same data
- [ ] Topology preservation check: quantifying how well grid distance correlates with input-space distance
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Builds directly on TASK-UL23's SOM derivation. The U-Matrix (unified distance matrix) computes,
for every neuron, the average distance to its immediate grid-neighbors' weight vectors — high
values mark a boundary between dissimilar regions of the map, low values mark the interior of
a homogeneous cluster. Component planes make individual features interpretable in a way that a
single 2D projection (t-SNE/UMAP) cannot, since each plane shows one feature's value across the
same fixed grid.

## Dependencies
- Blocked by: TASK-UL23 (self-organizing maps theory)
- Blocks: none
- Story: STORY-UL12 (Self-organizing-map learner story)
- Directive: DIRECT-UL11 (Self-Organizing Maps)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
