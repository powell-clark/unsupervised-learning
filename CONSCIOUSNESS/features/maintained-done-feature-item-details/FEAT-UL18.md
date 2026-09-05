# FEAT-UL18: Matrix Factorisation Family: NMF and ICA Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p2

## Description
Lesson 20 of Unsupervised Learning Part II. Delivers an NMF and ICA lesson; the learner can extract parts-based and statistically independent components where PCA's orthogonal components are the wrong inductive bias. Notebooks: 20a_nmf_ica_theory.ipynb, 20b_nmf_ica_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
All eleven verified by REVIEW-UL075 — an independent fresh-context opus review that read every code cell's source and printed output from the raw `.ipynb` JSON, plus an independent re-execution confirming byte-identical outputs.

- [x] **AC-1** — Theory notebook: the factorisation family compared by constraint — 20a c4 gives a constraint table (PCA orthonormal, NMF non-negative, ICA independent); c5 measures it (47.3% of PCA's leading components' weights negative vs 0.0% for NMF)
- [x] **AC-2** — Theory notebook: NMF multiplicative updates derived and shown to decrease the objective monotonically — 20a c6 derives the Lee-Seung update from $\nabla_H J = W^TWH - W^TX$; c7 verifies max step-to-step increase across 300 iterations is -2.699e-05 (i.e. none), objective 178.5949 → 0.0028
- [x] **AC-3** — Theory notebook: ICA identifiability argument (Gaussian sources fail) and non-Gaussianity measures — 20a c8 derives $x=As=(AQ^T)(Qs)$ for any orthogonal $Q$; c9 measures kurtosis-vs-rotation-angle as flat for Gaussian sources ([-0.117,+0.005]) vs clearly peaked for uniform sources ([-1.174,-0.569])
- [x] **AC-4** — Theory notebook: FastICA fixed-point derivation — 20a c10 derives $w^+=\mathbb{E}[zg(w^Tz)]-\mathbb{E}[g'(w^Tz)]w$ from $G(u)=\log\cosh u$ as a Newton step; c11 implements it exactly, including symmetric decorrelation
- [x] **AC-5** — Theory notebook: from-scratch NMF and FastICA validated against synthetic ground truth — 20a c7 (NMF, 0.0007 rel. error vs sklearn's 0.0023 on a known rank-4 matrix) and c11 (FastICA, 0.998+ correlation recovering three known sources)
- [x] **AC-6** — Practical notebook: sklearn NMF parts-based decomposition on digits vs PCA — 20b c5 sweeps ranks 5-40, reporting NMF's reconstruction-error penalty (0.0203-0.0397) against PCA's Eckart-Young-optimal baseline, with a component image grid
- [x] **AC-7** — Practical notebook: NMF topic modelling compared with LDA on the same corpus — 20b c7 reproduces Lesson 10B's corpus generator exactly (independently confirmed byte-identical by the reviewer, including RNG draw order), scoring NMF (TF-IDF) and LDA (raw counts, Lesson 10B's recipe) both at 1.000 topic-overlap against the true generating vocabulary
- [x] **AC-8** — Practical notebook: FastICA source separation with the PCA failure contrast — 20b c9: sklearn and from-scratch (20A) agree exactly at [0.998, 0.988, 0.986] separation correlation; PCA on the identical mixture fails at [0.79, 0.65, 0.68]
- [x] **AC-9** — Practical notebook: PCA / NMF / ICA decision table — 20b c13, built from this lesson's own measured numbers rather than reputation
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab (jupyter execute, zero errors) — 20a 5/5, 20b 6/6 code cells, zero error outputs; independently re-executed by the reviewer with byte-identical results and zero network/file-IO calls found by pattern scan
- [x] **AC-11** — Cross-lesson link: explicit references to lesson 5 (PCA) and lesson 10 (LDA) — verified accurate, not just present: the reviewer independently reconstructed Lesson 10B's corpus generator and confirmed 20b's reproduction is byte-identical (same 500 docs, same vocabulary, same RNG draw order); PCA whitening in 20a explicitly reuses Lesson 5A's eigendecomposition machinery

## Review history
1. **REVIEW-UL075** (agent, `verify-lesson-20`, opus, fresh context, 2026-09-05) — **agent-approved**. All 11 criteria met with cell-index evidence and an independent re-execution. The reviewer went further than presence-checking on two self-reported findings from the build: independently reconstructed the discarded, buggy version of the FastICA source generator and reproduced its -0.606 correlation defect exactly, confirming the shipped fix genuinely resolves a real bug rather than describing an unverified one; and independently reproduced the ICA-vs-PCA Gini sparsity null result (0.581 vs 0.578), finding it real and "if anything understated in the notebook's favour."

## Linked Entities
- Story: STORY-UL18
- Directive: DIRECT-UL17
- Tasks: TASK-UL054, TASK-UL055, TASK-UL056
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
