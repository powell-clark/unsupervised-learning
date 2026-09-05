# DIRECT-UL20: Hidden Markov Models

**Status:** done (actual_end 2026-09-05)

## Context
Part II, lesson 23: Hidden Markov Models and Unsupervised Sequence Learning. Extends the Part I curriculum into territory the identity-vision-mission names but Part I only touched — density estimation, representation learning, and the graph/sequence/Bayesian methods a complete unsupervised course needs. Planned by Fable 5.1 on 2026-09-04; built and verified autonomously (see CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md).

## Acceptance Criteria
- [x] STORY-UL21 fulfilled (FEAT-UL21 maintained after an independent agent review) — REVIEW-UL087, agent-approved, 11 of 11 criteria met
- [x] Notebooks 23a_hidden_markov_models_theory.ipynb, 23b_hidden_markov_models_practical.ipynb committed with execution outputs, zero errors — 23a 9/9, 23b 6/6 code cells, independently re-executed by the reviewer with a byte-identical output diff
- [x] FEAT-UL1 and FEAT-UL2 satisfied for this lesson (Colab-runnable; from-scratch plus production implementation) — 23a's from-scratch forward-backward/Viterbi/Baum-Welch checked against brute-force enumeration and a known generating model; 23b compares against hmmlearn's GaussianHMM throughout, matched to floating-point precision

## Outcome
Lesson 23 (Hidden Markov Models and Unsupervised Sequence Learning) shipped and closed on an approved independent review (REVIEW-UL087). The reviewer independently re-implemented the inference under a different algorithm (log-space `logsumexp` rather than the notebooks' scale-factor recursion) and reproduced every scrutinised numeric claim exactly, catching one genuine Colab-compatibility gap (23b's `hmmlearn` import lacked an install guard, the only Part II notebook with this issue) plus nine smaller findings (an overclaim about a "byte-for-byte" reproduction, a label-switching presentation defect that made an excellent fit look broken, and cosmetic issues) — all fixed and re-verified before the verdict upgraded to 11 of 11.

## Dependencies
- Blocked by: none hard; conceptually follows Part I lessons named in the feature card
- Blocks: DIRECT-UL25 (capstone) uses this lesson's methods
