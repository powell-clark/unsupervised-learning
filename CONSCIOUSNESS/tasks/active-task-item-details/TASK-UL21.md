# TASK-UL21: Topic Modeling Theory (10a)

## Context
First notebook of Lesson 10 (STORY-UL11, DIRECT-UL10). Introduces Latent Dirichlet Allocation
(LDA) — discovering latent themes across a document corpus without any topic labels. Derives
the generative model and the Gibbs sampling inference procedure used to fit it.

## Acceptance Criteria
- [x] Bag-of-words framing and the document-term matrix
- [x] LDA's generative story: document-topic and topic-word Dirichlet priors
- [x] Why exact inference is intractable and approximate inference is required
- [x] Collapsed Gibbs sampling: derivation and update equation
- [x] From-scratch NumPy implementation of collapsed Gibbs sampling for LDA
- [x] Cross-check against a reference implementation
- [x] Visualization: topic-word distributions, document-topic assignments
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
LDA models each document as a mixture of topics and each topic as a distribution over words,
with Dirichlet priors over both mixtures. Unlike every clustering method so far, a document
isn't assigned to one cluster — it has a distribution over topics. Collapsed Gibbs sampling
integrates out the topic-mixture parameters analytically and samples only the per-word topic
assignments, which is what makes a from-scratch implementation tractable to derive and code.

## Dependencies
- Blocked by: TASK-UL2 (foundations groundwork)
- Blocks: TASK-UL22 (Topic modeling practical)
- Story: STORY-UL11 (Topic-modeling learner story)
- Directive: DIRECT-UL10 (Topic Modeling (LDA))
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
