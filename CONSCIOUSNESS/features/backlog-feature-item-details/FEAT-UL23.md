# FEAT-UL23: Word and Item Embeddings: word2vec and Skip-Gram with Negative Sampling Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 25 of Unsupervised Learning Part II. Delivers a word2vec lesson; the learner can learn dense representations of discrete tokens or items from co-occurrence alone. Notebooks: 25a_word_embeddings_theory.ipynb, 25b_word_embeddings_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
- [ ] **AC-1** — Theory notebook: distributional hypothesis, co-occurrence and PMI
- [ ] **AC-2** — Theory notebook: skip-gram softmax and the negative-sampling derivation
- [ ] **AC-3** — Theory notebook: SGNS-as-PMI-factorisation checked numerically
- [ ] **AC-4** — Theory notebook: from-scratch SGNS with hand-derived gradients and a neighbours/2D plot
- [ ] **AC-5** — Theory notebook: item2vec demonstration on baskets
- [ ] **AC-6** — Practical notebook: gensim Word2Vec matched against the from-scratch model
- [ ] **AC-7** — Practical notebook: analogies and most_similar with an honest small-corpus caveat
- [ ] **AC-8** — Practical notebook: embeddings clustered and visualised with earlier-lesson tools
- [ ] **AC-9** — Practical notebook: item2vec recommendations compared with lesson 8
- [ ] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors; no network downloads)
- [ ] **AC-11** — Cross-lesson link: lessons 8, 9, 10 data generators reused rather than re-invented

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL23
- Directive: DIRECT-UL22
- Tasks: TASK-UL069, TASK-UL070, TASK-UL071
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
