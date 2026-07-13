# TASK-UL29: Unsupervised Preprocessing (15)

## Context
Single-notebook Lesson 15 (STORY-UL14, DIRECT-UL13, FEAT-UL13). Synthesizes the preprocessing
decisions that silently shape every unsupervised method covered so far: scaling, categorical
encoding, distance metric choice, and missing-data handling.

## Acceptance Criteria
- [ ] Scaling: standardization vs min-max vs robust scaling, and why unscaled features distort distance-based methods
- [ ] Empirical demonstration: same clustering algorithm, same data, with and without scaling — quantified quality difference
- [ ] Categorical encoding for distance-based methods: one-hot vs ordinal vs target/frequency encoding, and the distance-metric implications of each
- [ ] Distance metric choice: Euclidean vs Manhattan vs cosine vs Gower (mixed types), and when each is appropriate
- [ ] Missing data: at least one imputation strategy demonstrated with its effect on downstream clustering quality
- [ ] Runs top-to-bottom in Google Colab

## Technical Notes
Every distance-based method in this course (K-Means, Hierarchical, DBSCAN, SOM) is silently
sensitive to feature scale — a feature measured in the thousands will dominate Euclidean
distance over one measured in single digits, regardless of which is actually more informative.
One-hot encoding preserves Euclidean-distance validity for categorical features (each category
becomes an orthogonal dimension) but expands dimensionality; ordinal encoding is compact but
imposes a false distance ordering on unordered categories. This lesson should measure these
effects on a real mixed-type dataset, not just assert them.

## Dependencies
- Blocked by: TASK-UL2, TASK-UL27 (foundations, comparison-lesson pattern)
- Blocks: none
- Story: STORY-UL14 (Professional-practice learner story)
- Directive: DIRECT-UL13 (Professional Practice)
- Feature: FEAT-UL13 (Professional Practice Lesson), FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
