# DIRECT-UL17: Non-negative and Independent Component Factorisation

**Status:** done (actual_end 2026-09-05)

## Context
Part II, lesson 20: Matrix Factorisation Family: NMF and ICA. Extends the Part I curriculum into territory the identity-vision-mission names but Part I only touched — density estimation, representation learning, and the graph/sequence/Bayesian methods a complete unsupervised course needs. Planned by Fable 5.1 on 2026-09-04; built and verified autonomously (see CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md).

## Acceptance Criteria
- [x] STORY-UL18 fulfilled (FEAT-UL18 maintained after an independent agent review) — REVIEW-UL075, agent-approved, 11 of 11 criteria met
- [x] Notebooks 20a_nmf_ica_theory.ipynb, 20b_nmf_ica_practical.ipynb committed with execution outputs, zero errors — 20a 5/5 code cells, 20b 6/6, independently re-executed by the reviewer with byte-identical outputs
- [x] FEAT-UL1 and FEAT-UL2 satisfied for this lesson (Colab-runnable; from-scratch plus production implementation) — 20a compares against sklearn NMF/FastICA; 20b compares against sklearn NMF/FastICA/LDA throughout

## Outcome
Lesson 20 (Matrix Factorisation Family: NMF and ICA) shipped and closed on an approved independent review (REVIEW-UL075). Two defects found and fixed during the build were independently re-verified by the reviewer as genuine fixes rather than unverified claims: a correlated-synthetic-source bug in the FastICA demonstration, and an honestly-reported near-null result in an ICA-vs-PCA sparsity comparison.

## Dependencies
- Blocked by: none hard; conceptually follows Part I lessons named in the feature card
- Blocks: DIRECT-UL25 (capstone) uses this lesson's methods
