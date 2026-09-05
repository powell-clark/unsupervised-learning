# FEAT-UL23: Word and Item Embeddings: word2vec and Skip-Gram with Negative Sampling Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 25 of Unsupervised Learning Part II. Delivers a word2vec lesson; the learner can learn dense representations of discrete tokens or items from co-occurrence alone. Notebooks: 25a_word_embeddings_theory.ipynb, 25b_word_embeddings_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
Ten of eleven verified by REVIEW-UL096 — an independent fresh-context opus review that read every code cell's source and printed output from the raw `.ipynb` JSON, independently re-executed both notebooks from clean copies (jupyter execute --inplace, exit 0 each), and independently re-derived several quantitative claims under different implementations than the notebooks use on themselves (its own SGNS trainer, its own PMI computation, complex-step gradient verification, a direct PYTHONHASHSEED test).

- [x] **AC-1** — Theory notebook: distributional hypothesis, co-occurrence and PMI — 25a c5-c6, one-hot orthogonality demo plus a two-topic toy corpus's PMI table (PMI('cat','dog')=0.875, PMI('cat','truck')=-inf, PMI('car','truck')=1.043); the raw-count-vs-PMI point uses the actual highest-count partner of 'cat' ('a', 82), not a hardcoded claim
- [x] **AC-2** — Theory notebook: skip-gram softmax and the negative-sampling derivation — 25a c7-c8, softmax-cost timing measured across |V| (843x time growth for a 500x vocab growth, described honestly as non-linear at this scale rather than claimed as clean linear scaling) and unigram^0.75 reweighting measured on real word frequencies
- [x] **AC-3** — Theory notebook: SGNS-as-PMI-factorisation checked numerically — 25a c9-c10, Levy-Goldberg derivation (algebra corrected: the local objective's negative-term coefficient no longer carries a stray factor of N) checked via correlation 0.82 over 168 pairs between a genuinely trained low-rank model and PMI-log(k)
- [x] **AC-4** — Theory notebook: from-scratch SGNS with hand-derived gradients and a neighbours/2D plot — 25a c11-c12 (gradients verified against finite-difference to 1e-10) + c14-c15 (5-topic corpus, 50 of 50 words recover a same-topic nearest neighbour, 2D PCA plot); sgns_train's negative-sampling update now snapshots each unique negative row once and accumulates correctly under duplicate draws within one pair
- [x] **AC-5** — Theory notebook: item2vec demonstration on baskets — 25a c16-c17, adapted lesson-9A rules (one association per basket, no injected noise — both measured adaptations, including a real 8-of-8 vs 4-of-8 partial-recovery comparison against noise re-added), 8 of 8 engineered partners recovered
- [x] **AC-6** — Practical notebook: gensim Word2Vec matched against the from-scratch model — 25b c5, both recover 50 of 50 same-topic neighbours on the identical corpus; one known difference (gensim's default frequent-word subsampling) stated honestly rather than folded into an "exactly the algorithm" overclaim
- [x] **AC-7** — Practical notebook: analogies and most_similar with an honest small-corpus caveat — 25b c7, a cross-topic analogy stress-tested by swapping the specific word (answer barely moves, "chef" regardless) demonstrating topic-membership voting rather than genuine relational structure
- [x] **AC-8** — Practical notebook: embeddings clustered and visualised with earlier-lesson tools — 25b c9-c10, K-Means and sklearn's built-in HDBSCAN both recover ARI=1.0 on the embeddings; t-SNE/UMAP 2D projection visually confirms the same 5 clusters
- [x] **AC-9** — Practical notebook: item2vec recommendations compared with lesson 8 — 25b c12, from-scratch item2vec (8/8) vs. gensim item2vec (6/8, dynamically-worded verdict) vs. item-item collaborative filtering in the spirit of lesson 8 (8/8, no embedding needed) — a genuine, unforced three-way comparison
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors; no network downloads) — 25a 9/9, 25b 7/7 code cells, zero errors, re-executed byte-identical (only wall-clock timings moved) by the independent reviewer
- [ ] **AC-11** — Cross-lesson link: lessons 9 and 10 data generators reused rather than re-invented; lesson 8's collaborative-filtering approach compared conceptually (its own generator is a network-downloaded or structureless ratings matrix, neither reusable within AC-10's no-downloads constraint, per REVIEW-UL096 — TASK-UL085) — re-scoped from the original "lessons 8, 9, 10 data generators reused" wording, which was unsatisfiable for lesson 8 specifically. Awaiting re-verification against this revised wording (TASK-UL085).

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Linked Entities
- Story: STORY-UL23
- Directive: DIRECT-UL22
- Tasks: TASK-UL069, TASK-UL070, TASK-UL071
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
