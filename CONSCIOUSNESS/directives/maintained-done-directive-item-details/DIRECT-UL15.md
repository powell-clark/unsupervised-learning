# DIRECT-UL15: Nonparametric Density Estimation

## Context
Part II, lesson 18: Kernel Density Estimation and Nonparametric Density. Extends the Part I curriculum into territory the identity-vision-mission names but Part I only touched — density estimation, representation learning, and the graph/sequence/Bayesian methods a complete unsupervised course needs. Planned by Fable 5.1 on 2026-09-04; built and verified autonomously (see CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md).

**Status: done (actual_end 2026-09-05).**

## Acceptance Criteria
- [x] STORY-UL16 fulfilled (FEAT-UL16 maintained after an independent agent review) — REVIEW-UL067, `verify-lesson-18`, fresh context, approved all eleven criteria with cell-index evidence
- [x] Notebooks 18a_kernel_density_estimation_theory.ipynb, 18b_kernel_density_estimation_practical.ipynb committed with execution outputs, zero errors — 18a 9 of 9 code cells (counts 1..9, 8 figures), 18b 6 of 6 (counts 1..6, 5 figures), both executed without `--allow-errors` and verified against the artefacts as committed at HEAD
- [x] FEAT-UL1 and FEAT-UL2 satisfied for this lesson — Colab-runnable (only `load_digits`/`load_iris` and in-notebook generators, no downloads); from-scratch `kde_1d`/`kde_nd` validated against sklearn `KernelDensity` and scipy `gaussian_kde` to ~1e-15 or better in both notebooks

## Outcome
Lesson 18 closes the directive as planned, in three tasks: TASK-UL048 (theory), TASK-UL049 (practical), TASK-UL050 (verification). Two content decisions are worth carrying into the remaining Part II directives.

First, the from-scratch-versus-library comparison earns its place only when the parameterisations are reconciled explicitly — scipy's `bw_method` is a multiplier on the sample standard deviation, not a bandwidth, and 18b quantifies what the unconverted mistake costs (0.0088 against a density peaking at 0.0101) rather than merely warning about it.

Second, a rate "verified" by fitting a slope to the formula that defines it is not evidence. 18a originally did exactly that for $h \propto n^{-1/5}$; it now grid-searches the ISE-minimising bandwidth at each n and reports the honest gap (-0.247 against -0.200). Later lessons in this directive family should assume the same standard.

## Dependencies
- Blocked by: none hard; conceptually follows Part I lessons named in the feature card
- Blocks: DIRECT-UL25 (capstone) uses this lesson's methods
