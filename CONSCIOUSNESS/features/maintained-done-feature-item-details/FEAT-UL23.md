# FEAT-UL23: Word and Item Embeddings: word2vec and Skip-Gram with Negative Sampling Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 25 of Unsupervised Learning Part II. Delivers a word2vec lesson; the learner can learn dense representations of discrete tokens or items from co-occurrence alone. Notebooks: 25a_word_embeddings_theory.ipynb, 25b_word_embeddings_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
All eleven verified. REVIEW-UL096 (an independent fresh-context opus review) found 10 of 11 met, with AC-11 unmet as originally worded (lesson 8's generator is genuinely unreusable within AC-10's no-downloads constraint). AC-11 was re-scoped (TASK-UL085) to state that constraint explicitly rather than assume an unsatisfiable reuse. REVIEW-UL098 (a second independent fresh-context reviewer) re-verified all 11 criteria against the revised wording and current notebook content, independently re-executed both notebooks from clean copies, and independently re-derived the core quantitative claims under different implementations (its own SGNS trainer, its own dict-based PMI computation, a symbolic Levy-Goldberg check, complex-step gradient verification). It surfaced further moderate findings (stale conclusion wording, a markdown/code contradiction, a mischaracterised baseline, an undercounted implementation difference, an np.str_ output-formatting leak) — all fixed and both notebooks re-executed clean before this closure.

- [x] **AC-1** — Theory notebook: distributional hypothesis, co-occurrence and PMI — 25a c5-c6, one-hot orthogonality demo plus a two-topic toy corpus's PMI table (PMI('cat','dog')=0.875, PMI('cat','truck')=-inf, PMI('car','truck')=1.043); the raw-count-vs-PMI point dynamically detects and describes ties rather than asserting a single winner ('a' and 'is' are currently tied at 82 for 'cat''s highest raw-count partner; 'the' scores 77, rank 3, PMI=-0.071)
- [x] **AC-2** — Theory notebook: skip-gram softmax and the negative-sampling derivation — 25a c7-c8, softmax-cost timing measured across |V| with a robust (warm-up + min-of-5-repeats) timer, described honestly as growing with |V| but not perfectly linearly at this scale, with a measured (not asserted) per-element-cost explanation; unigram^0.75 reweighting measured on real word frequencies
- [x] **AC-3** — Theory notebook: SGNS-as-PMI-factorisation checked numerically — 25a c9-c10, Levy-Goldberg derivation (algebra corrected: no stray factor of N in the local objective) checked via correlation 0.8199 over 168 pairs between a genuinely trained low-rank model and PMI-log(k)
- [x] **AC-4** — Theory notebook: from-scratch SGNS with hand-derived gradients and a neighbours/2D plot — 25a c11-c12 (gradients verified against finite-difference to ~1.9e-10) + c14-c15 (5-topic corpus, 50 of 50 words recover a same-topic nearest neighbour, 2D PCA plot); sgns_train's negative-sampling update snapshots each unique negative row once and accumulates correctly under duplicate draws within one pair
- [x] **AC-5** — Theory notebook: item2vec demonstration on baskets — 25a c16-c17, isolates the real cause of item2vec's degradation on lesson-9A's original generator (multiple rules firing in the same basket, not injected noise — noise alone measured harmless, 8/8, once isolated), 8 of 8 engineered partners recovered on the clean single-rule-per-basket data
- [x] **AC-6** — Practical notebook: gensim Word2Vec matched against the from-scratch model — 25b c5, both recover 50 of 50 same-topic neighbours on the identical corpus; two differences left at gensim's defaults are stated honestly (frequent-word subsampling, and the learning-rate schedule: gensim's alpha=0.025->min_alpha=0.0001 vs the from-scratch trainer's lr_start=0.05->lr_end=1e-4), rather than an "exactly the algorithm" overclaim
- [x] **AC-7** — Practical notebook: analogies and most_similar with an honest small-corpus caveat — 25b c7, a cross-topic analogy stress-tested by swapping the specific word (answer barely moves) demonstrating topic-membership voting rather than genuine relational structure
- [x] **AC-8** — Practical notebook: embeddings clustered and visualised with earlier-lesson tools — 25b c9-c10, K-Means and sklearn's built-in HDBSCAN both recover ARI=1.0 on the embeddings; t-SNE/UMAP 2D projection visually confirms the same 5 clusters
- [x] **AC-9** — Practical notebook: item2vec recommendations compared with lesson 8 — 25b c12, from-scratch item2vec (8/8) vs. gensim item2vec (6/8, dynamically-worded verdict) vs. a classic item-item collaborative-filtering baseline (8/8, no embedding, no ratings, no training loop) explicitly distinguished from -- not attributed to -- Lesson 8's own latent-factor approach
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors; no network downloads confirmed by scanning every cell for URLs/downloads/fetches) — 25a 9/9, 25b 7/7 code cells, zero errors
- [x] **AC-11** — Cross-lesson link: lessons 9 and 10 data generators reused rather than re-invented; lesson 8's collaborative-filtering approach compared conceptually (its own generator is a network-downloaded MovieLens set in 8b, or a genuinely structureless uniform-random ratings matrix in 8a -- neither reusable within AC-10's no-downloads constraint, independently confirmed by REVIEW-UL098) — 25a's topic_vocab is byte-identical to 10B's own; 9A's exact rules and milk-conditional probability are carried through unchanged

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Review history
- REVIEW-UL096 — agent-rejected, iteration 1 (10 of 11 AC met; AC-11 unmet as worded)
- REVIEW-UL098 — agent-approved, iteration 2 (11 of 11 AC met, after AC-11 re-scoping via TASK-UL085)

## Linked Entities
- Story: STORY-UL23
- Directive: DIRECT-UL22
- Tasks: TASK-UL069, TASK-UL070, TASK-UL071, TASK-UL085
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
