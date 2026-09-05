# FEAT-UL16: Kernel Density Estimation and Nonparametric Density Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p2

## Description
Lesson 18 of Unsupervised Learning Part II. Delivers a kernel density estimation lesson; the learner can estimate a probability density without assuming a parametric family and use it for scoring and sampling. Notebooks: 18a_kernel_density_estimation_theory.ipynb, 18b_kernel_density_estimation_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
All eleven verified by REVIEW-UL067 — an independent fresh-context review that read every code cell's source and outputs from the raw `.ipynb` JSON, citing cell indices rather than matching section headers.

- [x] **AC-1** — Theory notebook: histogram-to-KDE motivation and kernel definition — 18a md-4 derives both histogram defects and the kernel-sum formula; code-5 measures the bin-origin artefact (mean |diff| 0.0546, max 0.1583, against a true peak of 0.3989); md-6 gives the four-property definition and four kernel formulas
- [x] **AC-2** — Theory notebook: bandwidth selection — Scott, Silverman and leave-one-out CV derived and implemented — 18a md-10 derives all three, including why LOO-CV must drop the diagonal or degenerate to h=0; code-11 implements `scott_bandwidth`, `silverman_bandwidth`, `loo_cv_bandwidth` and runs them (0.72 / 0.65 / 0.32 against a theoretical 0.29)
- [x] **AC-3** — Theory notebook: bias-variance / over-vs-undersmoothing demonstration — 18a md-8 carries the full Taylor-expansion derivation to AMISE(h); code-13 sweeps h over two orders of magnitude and shows the U-shaped ISE curve with undersmoothed, near-optimal and oversmoothed panels
- [x] **AC-4** — Theory notebook: curse of dimensionality for KDE shown empirically — 18a code-15 measures relative error against d=1..10 (11.0% → 95.8%) and the implied sample-size cost to hold accuracy (500 → 9.9e5, a factor of ~1,980)
- [x] **AC-5** — Theory notebook: from-scratch vectorised 1D and 2D KDE — 18a code-7 (`kde_1d`) and code-15 (`kde_nd`, arbitrary d), both broadcasting-based with no per-point Python loops; code-19 exercises 2-D on iris rather than leaving it theoretically generic
- [x] **AC-6** — Practical notebook: sklearn KernelDensity with cross-validated bandwidth and a scipy gaussian_kde comparison — 18b code-5 selects h=8.821 by `GridSearchCV`, agrees with `gaussian_kde` to ~1e-16 after explicit `bw_method` conversion, and quantifies the unconverted-parameter trap at 0.0088 against a density peaking at 0.0101
- [x] **AC-7** — Practical notebook: generative sampling case study (PCA + KDE on digits) — 18b code-7 does PCA 64→15 (83.5% variance) then `KernelDensity.sample()`, with a nearest-neighbour check against memorisation (generated median 18.68 / min 12.36 against real 16.12 / 5.29)
- [x] **AC-8** — Practical notebook: density-based anomaly scoring compared with lesson 7 methods — 18b code-9 scores KDE log-density against Isolation Forest and LOF(novelty=True) by PR-AUC with a 60-draw-averaged random baseline (KDE 0.1251 = 2.06x baseline, Isolation Forest 0.0367 = 0.61x, LOF 0.0862 = 1.42x)
- [x] **AC-9** — Practical notebook: a documented failure case in high dimensions — 18b code-13 Experiment 2 holds ten informative components fixed and appends up to 120 pure-noise dimensions: KDE PR-AUC falls 0.1251 → 0.0403, at or below chance (0.0503). Reported alongside Experiment 1, the confounded sweep that failed to show the effect
- [x] **AC-10** — Both notebooks run end-to-end — 18a 9 of 9 code cells, execution counts 1..9, zero error outputs; 18b 6 of 6, counts 1..6, zero errors. Confirmed independently by the reviewer via `json.load` over every cell's `outputs` list, and separately by this session against the artefacts as committed at HEAD
- [x] **AC-11** — Cross-lesson link: GMM (lesson 4) as parametric density vs KDE as nonparametric, stated with a side-by-side fit — 18a code-17 fits both (GMM's k by BIC, KDE's h by LOO-CV) on a Gaussian mixture and a Laplace mixture, with one figure and one printed ISE table covering both estimators on both targets

## Review history
1. **REVIEW-UL067** (agent, `verify-lesson-18`, sonnet, fresh context, 2026-09-05) — **agent-approved**. All 11 criteria met with cell-index evidence. Checked every quantitative claim in both notebooks against the printed table it references and found **zero prose-versus-output contradictions**, explicitly noting that the notebooks hedge where the evidence is weak (the AMISE slope stated as 24% and 9% off theory rather than "matching") instead of overclaiming.

## Reviewer observations recorded but not blocking
The reviewer raised two soft flags, neither undermining a criterion, both accepted as fair:
1. 18b code-7 prints "FARTHER" in capitals for a 16% median-distance gap. The accompanying min-distance figures (12.36 against 5.29) support the claim far more strongly than the median does, so the emphasis outruns the statistic it sits next to.
2. 18b code-9 explains Isolation Forest's below-chance score by asserting digit 9 "sits INSIDE the cloud among 4s, 7s and 8s". Domain-plausible, and consistent with the overlapping score distributions plotted beside it, but not itself measured — no per-class overlap statistic is computed.

Tracked forward as TASK-UL083 rather than left as a comment. Both are prose-and-measurement refinements to an approved notebook, not defects in it.

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required, and one was obtained: REVIEW-UL067 approves. This card closed to `maintained` on that verdict.

## Linked Entities
- Story: STORY-UL16
- Directive: DIRECT-UL15
- Tasks: TASK-UL048, TASK-UL049, TASK-UL050
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
