# TASK-UL052: Lesson 19b practical: Normalizing Flows and Modern Density Models

## Context
Part II, lesson 19, practical notebook `notebooks/19b_normalizing_flows_practical.ipynb`. Builds on `19a_normalizing_flows_theory.ipynb` (TASK-UL051) — read it first and reuse its from-scratch functions where the plan compares them with the library. Feature card: FEAT-UL17.

## Notebook plan (sections, in order)
1. RealNVP on 2D data at slightly larger scale: deeper flow, learned density contours vs the KDE from lesson 18 on the same data
2. A minimal DDPM (denoising diffusion) on the same 2D data: forward noising schedule, a small MLP noise predictor, ancestral sampling — written from scratch in PyTorch, CPU-trainable in under two minutes
3. Side-by-side: VAE (reuse the 12a architecture), flow, diffusion, and a conceptual GAN column — likelihood available?, sample quality, training stability, inference cost
4. Using the flow density as an anomaly score (link to lesson 7 and 18)
5. Practical guidance on when a flow, a VAE, or diffusion is the right tool

**Library:** PyTorch (from scratch — no diffusion/flow libraries added)
**Data:** synthetic 2D — no downloads

## Acceptance Criteria
- [ ] Every section above present with working code and at least one figure or table per section
- [ ] The production library result is compared against the lesson's from-scratch implementation at least once
- [ ] All practical-notebook criteria on FEAT-UL17 are satisfiable from this notebook's content
- [ ] `jupyter execute` passes: every code cell executed, zero errors, outputs committed
- [ ] Colab-runnable: no network downloads (a bundled/cached dataset or an in-notebook generator only)

## Build rules (house pattern — read two Part I notebooks first, e.g. 5a/5b or 12a/12b)
- Open with a story-driven motivation, then a Table of Contents with anchor links, then a Required Libraries cell.
- Derivations in markdown with LaTeX; every claim that can be checked numerically is checked in a code cell.
- From-scratch implementation first, production library second, and one cell that shows the two agree (or explains why they differ).
- No network downloads: only sklearn/networkx bundled data, in-notebook generators, or the cached MNIST under notebooks/data. If a step would download, replace it with a generator and say so in a markdown cell.
- Keep any training cell under ~3 minutes on CPU; bound epochs and sample sizes accordingly.
- Reuse earlier-lesson code patterns rather than re-inventing (reference the lesson by number in markdown).
- Finish with a Conclusion: key takeaways, practical guidance, what was NOT covered and why (honesty section), next steps.
- Execute in place before committing: `jupyter execute notebooks/<nb> --output /tmp/<nb>`, confirm every code cell ran with zero errors, copy back over the committed file. Commit with the task id in the subject.

## Execution
- Builder model: the session model (sonnet is sufficient)
- Expected duration: 2h

## Dependencies
- Blocked by: TASK-UL051
- Blocks: the lesson-19 verification task
