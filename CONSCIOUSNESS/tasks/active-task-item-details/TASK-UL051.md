# TASK-UL051: Lesson 19a theory: Normalizing Flows and Modern Density Models

## Context
Part II, lesson 19, theory notebook `notebooks/19a_normalizing_flows_theory.ipynb`. As a learner I want a normalizing-flows lesson so that I can build a generative model with an exact likelihood and understand how it differs from VAEs, GANs and diffusion models. Feature card: FEAT-UL17 (its acceptance criteria are the contract; the verification task will check each one against the raw notebook).

## Notebook plan (sections, in order)
1. Change of variables for densities: the Jacobian determinant, why invertibility matters, one worked 1D and one 2D example by hand
2. Composing simple invertible maps into a flow; log-likelihood as a sum of log|det J| terms
3. Affine coupling layers (RealNVP): the construction, why the Jacobian is triangular, alternating masks; planar flows mentioned as the historical precursor
4. Exact likelihood vs the VAE ELBO (lesson 12a): what is gained, what is paid (architectural constraints)
5. Training: maximum likelihood = minimising forward KL; how sampling works by inverting the flow
6. From scratch (PyTorch, the same from-scratch bar lesson 12a uses): AffineCoupling module with explicit log-det, a 4-layer flow, training loop on 2D moons, density contour plot and samples

**From scratch:** AffineCoupling and Flow modules written by hand in PyTorch with an explicit log|det J| term — no external flow library
**Data:** make_moons, make_circles, a 2D spiral generated in-notebook — no downloads

## Acceptance Criteria
- [ ] Every section above present as a titled section with working code where the plan names an implementation
- [ ] The from-scratch implementation is validated numerically inside the notebook (against ground truth or the production library)
- [ ] All theory-notebook criteria on FEAT-UL17 are satisfiable from this notebook's content (read the card before writing)
- [ ] `jupyter execute` passes: every code cell executed, zero errors, outputs committed
- [ ] Colab-runnable: no local files outside the repo, no network downloads

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
- Builder model: the session model. If the session model is sonnet, dispatch an opus subagent (Agent tool, model: "opus") to draft and check the derivation sections before you execute the notebook — this lesson's mathematics is where a weaker draft is most likely to be subtly wrong.
- Expected duration: 2h

## Dependencies
- Blocked by: none
- Blocks: the 19b practical and the lesson-19 verification task
