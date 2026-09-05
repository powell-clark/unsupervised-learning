# STORY-UL20: Bayesian Nonparametric Clustering: Dirichlet Process Mixtures

**Status:** fulfilled

As a learner I want a Dirichlet process mixture lesson so that I can let the data decide the number of clusters instead of sweeping K.

## Outcome
Fulfilled on FEAT-UL20 reaching `maintained` via REVIEW-UL083 (agent-approved, all 11 acceptance criteria met with cell-index evidence and an independent re-execution, 2026-09-05). Two notebooks delivered: 22a_dirichlet_process_mixtures_theory.ipynb (CRP, stick-breaking, Blackwell-MacQueen urn, from-scratch collapsed Gibbs DP-GMM, alpha sensitivity) and 22b_dirichlet_process_mixtures_practical.ipynb (sklearn DP mixture, three-way comparison with BIC-GMM and silhouette K-Means, real digits case with ARI, three demonstrated pitfalls, decision guide). 22a additionally passed a dedicated adversarial math review that confirmed the sampler exactly targets the DP-mixture posterior (checked against exact enumeration over all 203 partitions of a toy n=6 dataset).

## Linked Entities
- Directive: DIRECT-UL19
- Feature: FEAT-UL20 (plus cross-cutting FEAT-UL1, FEAT-UL2)
- Tasks: TASK-UL060, TASK-UL061, TASK-UL062
