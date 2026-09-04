# TASK-UL22: Topic Modeling Practical (10b)

## Context
Second notebook of Lesson 10 (STORY-UL11, DIRECT-UL10). Applies Gensim's `LdaModel` and
scikit-learn's `LatentDirichletAllocation` to a larger, richer synthetic corpus, uses topic
coherence to choose the number of topics without ground truth, and visualizes the fitted
model interactively with pyLDAvis.

## Acceptance Criteria
- [x] Larger, richer corpus (more topics, more documents than 10A)
- [x] Gensim LdaModel workflow: Dictionary, doc2bow, fit, inspect topics
- [x] scikit-learn LatentDirichletAllocation workflow on the same corpus
- [x] Topic coherence (c_v) computed across a range of candidate K values
- [x] Coherence-vs-K plot with the selected K identified
- [x] pyLDAvis interactive visualization of the fitted model
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
Builds directly on TASK-UL21's generative model and inference derivation. Topic coherence
(c_v) scores how often a topic's top words co-occur across sliding windows of the corpus —
a label-free proxy for "does this topic make semantic sense," used in practice to choose K
since there's no elbow-on-inertia equivalent for topic models. pyLDAvis's default classical-MDS
topic-distance projection can break on current NumPy/SciPy (complex-valued intermediate
results); use mds='mmds' for a stable equivalent.

## Dependencies
- Blocked by: TASK-UL21 (topic modeling theory)
- Blocks: none
- Story: STORY-UL11 (Topic-modeling learner story)
- Directive: DIRECT-UL10 (Topic Modeling (LDA))
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
