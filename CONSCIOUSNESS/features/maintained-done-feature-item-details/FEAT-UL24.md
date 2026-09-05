# FEAT-UL24: Self-Supervised Contrastive Representation Learning Lesson

**Status:** backlog | **Kano:** performance | **Priority:** p3

## Description
Lesson 26 of Unsupervised Learning Part II. Delivers a contrastive learning lesson; the learner can measure with a linear probe whether self-supervised image features beat PCA and autoencoder features on the same unlabelled data. Notebooks: 26a_contrastive_learning_theory.ipynb, 26b_contrastive_learning_practical.ipynb. Same house pattern as Part I: derivation first, from-scratch implementation, then the production library, all Colab-runnable with committed execution outputs.

## Acceptance Criteria
All eleven verified by REVIEW-UL102 -- an independent fresh-context opus review that read raw `.ipynb` JSON cell-by-cell for both notebooks (28+16 cells), independently re-derived the InfoNCE mutual-information bound in closed form rather than trusting the notebook's own Monte Carlo estimate, independently re-executed both notebooks from output-cleared copies (jupyter execute, exit 0 each), and independently reimplemented 26b's linear-probe path to cross-check its printed numbers. It found four "correct measurement, wrong explanation" defects plus minor findings; all were fixed and re-verified (including two indexing bugs caught while fixing the first two) before this closure.

- [x] **AC-1** — Theory notebook: pretext tasks and invariance framing -- 26a cell 4 (pretext-task catalogue) + cell 5 (measured: a 2-pixel shift of an MNIST image is farther in pixel space than a different image of the same digit for 80.4% of probes, and even farther than a different digit for 55.0%)
- [x] **AC-2** — Theory notebook: InfoNCE derived with the mutual-information bound and temperature discussion -- 26a cells 7-12; the Bayes-optimal-classifier derivation checked exactly (cell 8, max abs diff 0.00e+00), the MI bound verified against a closed-form joint (cell 10, bound rises 0.2671->0.7506 nats over M=2..1024 without ever exceeding the true 0.7509 nats, quoted against Monte-Carlo standard error rather than a bare inequality), temperature's effect on entropy and gradient measured directly (cell 12)
- [x] **AC-3** — Theory notebook: NT-Xent implemented from scratch in PyTorch -- 26a cells 13-14, three independent implementations (plain Python, hand-written log-sum-exp tensors, `F.cross_entropy`) agreeing to float32 round-off (worst spread 1.01e-6) and matching a hand-derived closed form log(1+2/e) to 6.42e-8
- [x] **AC-4** — Theory notebook: collapse and non-contrastive alternatives explained -- 26a cells 17-20; attract-only collapse demonstrated (reaches the theoretical floor -1, effective rank <2 of 8), NT-Xent's ceiling at collapse verified exact (log(2N-1) to <=1.9e-7 across batch sizes and temperatures), BYOL/SimSiam/VICReg covered conceptually with a genuine, independently-verified finding that VICReg's own raw-embedding terms are scale-confounded when read off a cosine-trained encoder (a matched-scale rescale demonstration shows the apparent correct-direction separation reverses once scale is controlled for)
- [x] **AC-5** — Theory notebook: tiny end-to-end MNIST run with loss curve and embedding plot -- 26a cells 23-26, 60 epochs on 6,000 unlabelled images, loss curve plotted against the log(2N-1) chance level, t-SNE of the trained representation coloured by held-out labels, honest comparison against raw pixels and an untrained control (ties pixels on 5-NN, triples silhouette at 1/12th the dimensionality)
- [x] **AC-6** — Practical notebook: SimCLR with a linear-probe evaluation -- 26b cell 5, the encoder/loss/augmentations reused unchanged from 26A, a `LogisticRegression` probe trained on 150 of 300 labelled images (a genuinely scarce subset) and tested on the other 150, reaching 92.7% accuracy
- [x] **AC-7** — Practical notebook: contrastive vs PCA vs autoencoder features under the same probe -- 26b cell 7, the identical probe protocol (same 300-image labelled subset, same 50/50 split, same classifier, same seed) applied to SimCLR (64-d, 92.7%), PCA (64-d, 78.0%) and Lesson 12B's `ConvAutoencoder` bottleneck (1,568-d, 83.3%, reused unchanged)
- [x] **AC-8** — Practical notebook: k-NN and 2D visualisation of the three representations -- 26b cell 9, 5-NN cross-validated accuracy on all 6,000 labels for all three feature sets, t-SNE (and UMAP where available) side by side, carrying forward Lesson 6A's cluster-artefact caveat explicitly
- [x] **AC-9** — Practical notebook: temperature / negatives / augmentation ablations -- 26b cells 11-13, three sweeps (temperature, batch size/negatives, augmentation strength) each at a reduced 5-epoch budget with its own plot; the batch-size sweep is honestly flagged as confounded with total gradient-step count, and the "which lever matters most" summary now tie-checks its own claim (temperature and augmentation strength are in fact statistically tied here) rather than asserting an unjustified single winner
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab on CPU (jupyter execute, zero errors; training bounded to a few minutes) -- 26a 12/12, 26b 7/7 code cells, zero errors, independently re-executed by the reviewer and by this session from output-cleared copies; MNIST loaded from the repo's cached `notebooks/data/MNIST`, no network calls
- [x] **AC-11** — Cross-lesson link: lessons 5, 6, 12 and 16 referenced concretely -- Lesson 5 (PCA) and Lesson 12 (autoencoder) both named as pixel-space-criterion baselines and directly compared under one probe in 26b; Lesson 6A's t-SNE-artefact caveat carried forward explicitly in both notebooks; Lesson 16's label-scarcity framing tied directly to the linear-probe's 300-label regime (26b's Guidance section)

## Review gate
Kano `performance` resolves to an agent gate with one independent review (DEFAULT_GATES; confirmed against dist/packages/core/review/review-gates-config.js on 2026-09-04). No human verdict is required. The lesson's verification task performs that review with a fresh-context opus subagent and closes this card on approval.

## Review history
- REVIEW-UL102 -- agent-approved, iteration 1 (11 of 11 AC met; 4 substantive defects found and fixed in the same task before closure)

## Linked Entities
- Story: STORY-UL24
- Directive: DIRECT-UL23
- Tasks: TASK-UL072, TASK-UL073, TASK-UL074
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)
- Syllabus: CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md
