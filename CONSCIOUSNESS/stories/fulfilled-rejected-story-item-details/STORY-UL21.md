# STORY-UL21: Hidden Markov Models and Unsupervised Sequence Learning

**Status:** fulfilled

As a learner I want a hidden Markov model lesson so that I can discover latent regimes in sequential data without labels.

## Outcome
Fulfilled on FEAT-UL21 reaching `maintained` via REVIEW-UL087 (agent-approved, all 11 acceptance criteria met with cell-index evidence and an independent re-execution, 2026-09-05). Two notebooks delivered: 23a_hidden_markov_models_theory.ipynb (Markov chains, scaled forward-backward validated against a 729-path brute-force enumeration, Viterbi, Baum-Welch as EM, model-selection pitfalls) and 23b_hidden_markov_models_practical.ipynb (hmmlearn cross-checked to floating-point precision against 23a's from-scratch code, volatility-regime detection at 97.8% accuracy, held-out/BIC model selection, multivariate covariance comparison, duration/non-stationarity mismatches measured quantitatively). The reviewer independently re-derived every scrutinised numeric claim under its own log-space implementation and caught a genuine Colab-compatibility gap (a missing `hmmlearn` install guard) plus nine smaller findings, all fixed before the final verdict.

## Linked Entities
- Directive: DIRECT-UL20
- Feature: FEAT-UL21 (plus cross-cutting FEAT-UL1, FEAT-UL2)
- Tasks: TASK-UL063, TASK-UL064, TASK-UL065
