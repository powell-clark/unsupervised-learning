# DIRECT-UL16: Flow-Based and Diffusion Density Models

**Status:** done (actual_end 2026-09-05)

## Context
Part II, lesson 19: Normalizing Flows and Modern Density Models. Extends the Part I curriculum into territory the identity-vision-mission names but Part I only touched — density estimation, representation learning, and the graph/sequence/Bayesian methods a complete unsupervised course needs. Planned by Fable 5.1 on 2026-09-04; built and verified autonomously (see CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md).

## Acceptance Criteria
- [x] STORY-UL17 fulfilled (FEAT-UL17 maintained after an independent agent review) — REVIEW-UL071, agent-approved, 10 of 10 criteria met
- [x] Notebooks 19a_normalizing_flows_theory.ipynb, 19b_normalizing_flows_practical.ipynb committed with execution outputs, zero errors — 19a 5/5 code cells, 19b 7/7, independently re-executed by the reviewer with byte-identical outputs
- [x] FEAT-UL1 and FEAT-UL2 satisfied for this lesson (Colab-runnable; from-scratch plus production implementation) — 19a compares against scipy, 19b against sklearn KernelDensity/IsolationForest/LOF

## Outcome
Lesson 19 (Normalizing Flows and Modern Density Models) shipped and closed on an approved independent review (REVIEW-UL071). Three findings from that review (a factual error about lesson 12a's VAE latent dimension, an anomaly-detection framing overclaim, a cosmetic table-formatting collision) were fixed before the verdict was recorded, not deferred.

## Dependencies
- Blocked by: none hard; conceptually follows Part I lessons named in the feature card
- Blocks: DIRECT-UL25 (capstone) uses this lesson's methods
