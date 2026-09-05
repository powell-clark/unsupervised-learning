# STORY-UL16: Kernel Density Estimation and Nonparametric Density

As a learner I want a kernel density estimation lesson so that I can estimate a probability density without assuming a parametric family and use it for scoring and sampling.

## Fulfilment
Fulfilled when FEAT-UL16 reaches `maintained` (review-gates: a story fulfils through its owning feature's gate, not a separate step). The verification task for lesson 18 performs that move.

**Status: fulfilled (2026-09-05).** FEAT-UL16 reached `maintained` on REVIEW-UL067, an independent fresh-context review that approved all eleven acceptance criteria from raw notebook JSON.

## Outcome
The learner can now estimate a density without assuming a family, and — the part that makes the story worth having — knows when not to. 18a derives the estimator from the histogram's arbitrary-origin defect, works the AMISE argument through to $h \propto n^{-1/5}$, measures that rate by search rather than asserting it, and puts KDE head to head with Lesson 4's GMM on one target where the Gaussian family is right and one where it is wrong. 18b spends the density on four jobs — cross-validated fitting, generative sampling of digits via PCA, anomaly scoring against Lesson 7's Isolation Forest and LOF, and contour-auditing a K-Means partition — then measures where it stops working.

Both notebooks keep an experiment that failed. 18a's kernel table has the AMISE-optimal Epanechnikov losing to tophat on a single sample; 18b's first curse-of-dimensionality sweep showed KDE *improving* with dimension because the design confounded dimension with information. Neither was quietly replaced. The reviewer specifically noted this as a strength: the notebooks hedge where the evidence is weak rather than overclaiming.

## Linked Entities
- Directive: DIRECT-UL15
- Feature: FEAT-UL16 (plus cross-cutting FEAT-UL1, FEAT-UL2)
- Tasks: TASK-UL048, TASK-UL049, TASK-UL050
