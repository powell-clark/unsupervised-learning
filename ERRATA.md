# Errata and open findings

These are findings from an independent academic review on 2026-10-22, and the author works through them as he studies the lessons.

## 0a_clustering_foundations_theory.ipynb

- [fixed] P1 — cell 11, 12, 14 — Cosine distance has the wrong range and zero vectors are treated as having a direction. — State similarity in [-1, 1] and distance in [0, 2] for nonzero real vectors, label the zero-vector convention, and use nonzero example points.
- [fixed] P1 — cell 17 — The high-dimensional ball explanation places points outside the stated radius inside the ball and misstates volume growth. — Use the sum-of-squares radius constraint and ball-volume formula, distinguishing a fixed-radius ball from a cube whose corner radius grows with dimension.
- [fixed] P1 — cell 17–19, 28 — Distance concentration is presented as making all high-dimensional clustering meaningless, with an unsupported dimension cutoff and a reversed equal-distance plot label. — Restrict the demonstration to independent uniform features, explain relative concentration and the role of structure, remove the cutoff, and label equal distances as having no contrast.

## 0b_cluster_evaluation.ipynb

- [fixed] P1 — cell 10 — The silhouette calculation discards the first cluster member rather than the current observation and gives singletons the wrong score. — Exclude the current observation by index, assign singleton silhouettes zero, and reject cluster counts outside 2 through n_samples - 1.
- [open] P1 — cell 14 — The silhouette plot treats scores below the mean as evidence of incorrect assignment. — Distinguish below-average positive scores from negative scores, which indicate a smaller mean distance to another cluster.
- [open] P1 — cell 28 — The adjusted Rand index is reported as percentage agreement. — Report it as a chance-adjusted pair-counting index, with 1 for identical partitions and 0 for chance-level agreement, and compute any matched-label accuracy separately.
- [open] P1 — cell 37, 38, 47 — The gap statistic is reduced to an argmax and falsely claimed to peak at the true cluster count. — Compute uncertainty estimates and select the smallest k satisfying Gap(k) >= Gap(k+1) - s_(k+1), identifying argmax as a separate heuristic.
- [open] P3 — cell 48 — The next-lesson references swap the DBSCAN and hierarchical lesson numbers. — Identify hierarchical clustering as Lesson 2 and DBSCAN as Lesson 3.

## 1a_kmeans_theory.ipynb

- [open] P2 — cell 5 — A bounded monotone K-Means objective is treated as proof of finite algorithm termination and centroid convergence. — Add the finite-assignment argument and state tie-breaking and empty-cluster assumptions.
- [open] P2 — cell 7 — The scratch K-Means stores initial centroids in the input dtype and truncates means for integer data. — Convert input or initial centres to floating point and document the input contract.
- [open] P2 — cell 5, 12 — Foundational algorithms and historical claims lack usable primary references. — Add complete original-paper references beside the relevant method and derivation claims.
- [open] P3 — cell 1 — The contents contain duplicate numbering and do not follow the actual section order. — Renumber the entries and align them with the notebook's sections.

## 2a_hierarchical_theory.ipynb

- [open] P1 — cell 9 — The hierarchical implementation writes shrinking-list positions into the linkage matrix instead of persistent cluster identifiers. — Maintain persistent cluster identifiers and assign merge i the identifier n+i.
- [open] P1 — cell 15 — Dendrogram cluster counts are fabricated by subtracting integer merge heights. — Cut at each height with the distance criterion and count the distinct resulting cluster labels.

## 3a_dbscan_theory.ipynb

- [open] P1 — cell 15 — Ordinary DBSCAN is recommended for variable-density clusters despite its single global density scale. — Recommend comparable-density clusters, explain the parameter trade-offs, and distinguish methods that accommodate varying densities.
- [open] P1 — cell 12 — The DBSCAN validation compares only the label alphabet rather than the partitions. — Compare noise masks and label-invariant partitions while accounting for potentially ambiguous border points.
- [open] P2 — cell 0, 1, 7, 9 — DBSCAN promises density-reachability and density-connectivity without defining them. — Define direct density-reachability and its asymmetry, reachability and connectivity, then explain expansion through core points.
- [open] P2 — cell 0 — Foundational algorithms and historical claims lack usable primary references. — Add complete original-paper references beside the relevant method and derivation claims.

## 4a_gmm_theory.ipynb

- [open] P1 — cell 8, 10 — GMM responsibilities and likelihoods can underflow and are then changed by added epsilon terms. — Compute weighted log densities and normalise with logsumexp, handling empty components separately.
- [open] P1 — cell 11, 17 — EM is claimed to converge to a local maximum without accounting for non-maximal stationary points or covariance collapse. — State conditional convergence results, distinguish objective and parameter convergence, and discuss mixture degeneracy.
- [open] P1 — cell 16 — GMM and K-Means agreement compares arbitrary numeric labels directly. — Use a label-invariant index or optimally match labels before computing agreement.

## 5a_pca_theory.ipynb

- [open] P1 — cell 6 — The PCA example uses a matrix with negative determinant as a covariance matrix while warnings are suppressed. — Choose a positive semidefinite covariance matrix and retain relevant warnings.
- [open] P1 — cell 4 — The supposedly two-dimensional PCA dataset appends eight independent unit-variance noise coordinates that dominate the signal. — Use a rank-two embedding with small observation noise or explicitly teach the example as failure to recover lower-variance signal.

## 5b_pca_practical.ipynb

- [open] P2 — cell 8 — The eigenfaces example uses random images plus a shared gradient that centring removes. — Call it an image-matrix PCA demonstration or use actual face variation before teaching eigenfaces and recognition.

## 6a_manifold_learning_theory.ipynb

- [open] P1 — cell 6 — The t-SNE example retains self-similarities and constructs joint probabilities with the wrong normalisation. — Exclude self-pairs, symmetrise conditional probabilities with the 2n denominator, and introduce perplexity-based bandwidth selection.
- [open] P1 — cell 7, 8, 11 — The manifold comparison invents unconditional geometry, artefact, speed and stability guarantees. — Describe method objectives and limitations, distinguish implementation variants, and restrict rankings to defined measured comparisons.
- [open] P2 — cell 5, 7 — Foundational algorithms and historical claims lack usable primary references. — Add complete original-paper references beside the relevant method and derivation claims.

## 6b_manifold_learning_practical.ipynb

- [open] P1 — cell 10, 11 — The manifold comparison invents unconditional geometry, artefact, speed and stability guarantees. — Describe method objectives and limitations, distinguish implementation variants, and restrict rankings to defined measured comparisons.

## 7a_anomaly_detection_theory.ipynb

- [open] P1 — cell 0 — The One-Class SVM introduction calls the origin a normal reference point despite excluding it in the derivation. — Describe mapped training observations as lying on the learned normal side and the origin on the excluded background side.

## 7b_anomaly_detection_practical.ipynb

- [open] P1 — cell 4, 7, 9 — The anomaly lesson claims labels are used only for evaluation while using them for contamination settings and autoencoder training selection. — Disclose label-derived hyperparameters and distinguish unsupervised outlier detection from normal-labelled novelty detection.
- [open] P1 — cell 9, 11, 13 — The autoencoder comparison trains on every normal observation later evaluated while excluding anomalies using labels. — Split observations first, fit preprocessing and models on appropriate training data, and compare all methods on the same untouched mixed test set.
- [open] P1 — cell 12 — ROC-AUC is falsely said to be inflated by a large pool of true negatives. — Explain prevalence invariance for fixed class-conditional scores and how a small false-positive rate can still produce many false alarms.
- [open] P2 — cell 13 — Average precision is labelled PR-AUC without specifying the integration convention. — Name and define average precision as a recall-weighted precision sum and distinguish trapezoidal PR area.

## 8a_recommender_systems_theory.ipynb

- [open] P1 — cell 5–7 — The recommender reverses the stated user and movie matrix axes and reuses the rating symbol as a mask. — Define a movie-by-user rating matrix and a separate observation mask with consistent indices before deriving the objective.
- [open] P1 — cell 10, 16 — The recommender ranks already-rated items as new recommendations. — Retain the observation mask and rank eligible unseen items, distinguishing rating prediction from recommendation generation.
- [open] P1 — cell 19, 21 — Item-mean centring is claimed to remove user rating bias. — Distinguish item centring from user bias and add explicit user and item bias terms or narrow the claim.

## 8b_recommender_systems_practical.ipynb

- [open] P1 — cell 21 — The ALS summary claims an explicit-ratings-only limitation while teaching implicit-feedback ALS. — Describe the implicit model's confidence and preference assumptions and its cold-start limitations.

## 9a_association_rules_theory.ipynb

- [open] P1 — cell 6, 18 — Sample lift above one is treated as proof of a genuine population association. — Describe positive empirical association and discuss support, sampling uncertainty, multiple comparisons and validation on new transactions.
- [open] P1 — cell 12 — The compound-lift explanation mistakes independence between source patterns for independence of compound events. — Explain that within-pattern dependence can create real dependence between compound antecedents and consequents.

## 9b_association_rules_practical.ipynb

- [open] P1 — cell 15 — Sample lift above one is treated as proof of a genuine population association. — Describe positive empirical association and discuss support, sampling uncertainty, multiple comparisons and validation on new transactions.
- [open] P1 — cell 8 — The compound-lift explanation mistakes independence between source patterns for independence of compound events. — Explain that within-pattern dependence can create real dependence between compound antecedents and consequents.

## 10a_topic_modeling_theory.ipynb

- [open] P2 — cell 8 — The central LDA conditional equation retains a placeholder denominator. — Omit the topic-independent denominator under proportionality or write it fully and explain why it cancels.
- [open] P2 — cell 10 — The Gibbs sampler's terminal-state estimate is presented without posterior averaging or mixing assessment. — Label it as conditional on the final assignment or average suitable post-burn-in summaries with label alignment where needed.

## 10b_topic_modeling_practical.ipynb

- [open] P1 — cell 12 — Topic coherence is falsely claimed to improve monotonically when topics are split. — Explain that coherence can favour overly fine or redundant solutions without asserting monotonicity.

## 11a_self_organizing_maps_theory.ipynb

- [open] P1 — cell 16, 18 — SOM topology preservation is presented as a proven guarantee based on a smooth grid and low topographic error. — Say the algorithm encourages local organisation, define the diagnostic's limited scope, and discuss folds and distortions.
- [open] P2 — cell 6, 11 — The SOM radius-decay schedule fails at an initial radius of one and grows for radii below one. — Require an initial radius above one or parameterise decay between valid initial and final radii.

## 11b_self_organizing_maps_practical.ipynb

- [open] P1 — cell 14, 15 — SOM topology preservation is presented as a proven guarantee based on a smooth grid and low topographic error. — Say the algorithm encourages local organisation, define the diagnostic's limited scope, and discuss folds and distortions.

## 12a_deep_unsupervised_theory.ipynb

- [open] P2 — cell 13, 18 — VAE regularisation is oversold as guaranteeing Gaussian encoded means and meaningful interpolations. — Distinguish conditional posteriors, their aggregate and plotted means, describing regularisation as pressure rather than a guarantee.

## 12b_deep_unsupervised_practical.ipynb

- [open] P1 — cell 6, 7 — The autoencoder comparison calls latent dimensionalities comparable despite using 1568 convolutional values versus 32 fully connected values. — Match the bottlenecks or disclose the factor-of-49 capacity difference and the convolutional representation's size relative to the input.
- [open] P1 — cell 14, 18 — Autoencoder training images are called held-out test observations after new corruption is added. — Reserve disjoint clean images before training and use an actual test set or documented validation split.
- [open] P1 — cell 19 — The GAN comparison denies its explicit latent prior and attributes a vanilla-autoencoder interpolation to a VAE. — Distinguish the generator-input prior from VAE posterior regularisation and identify the model actually used.

## 14_dimensionality_reduction_pipeline.ipynb

- [open] P1 — cell 6–8 — The feature-selection comparison fits supervised selectors on all labels and preprocessing on all observations before cross-validation. — Cross-validate a complete preprocessing, selection and classification pipeline separately for every candidate.

## 15_unsupervised_preprocessing.ipynb

- [open] P2 — cell 10 — KNN imputation is incorrectly described as requiring completely observed neighbours. — Describe feature-specific donors with the required target feature, distances over jointly observed features, and fallback cases.

## 16_semi_supervised_learning.ipynb

- [open] P1 — cell 6 — The semi-supervised benchmark fits its scaler before separating the test observations. — Split raw observations first and fit preprocessing on training data, or explicitly define a transductive evaluation protocol.

## 17a_spectral_clustering_theory.ipynb

- [open] P2 — cell 11, 20 — The spectral summary confuses the scaled quadratic objective's bound with the unscaled RatioCut bound. — Name the scaled objective explicitly or state the unscaled lower bound as the second-smallest eigenvalue.

## 17b_spectral_clustering_practical.ipynb

- [open] P1 — cell 1, 6, 7 — The symmetric normalised Laplacian is incorrectly said to have the constant vector as its zero eigenvector. — Use the degree-square-root-weighted constant vector for the symmetric normalised Laplacian and state the conventions for the other Laplacians.
- [open] P3 — cell 1, 6 — The eigengap section is duplicated verbatim. — Remove the duplicate and restore a contents cell if intended.

## 18a_kernel_density_estimation_theory.ipynb

- [open] P1 — cell 14 — The multivariate KDE formula calls a radial expression a product kernel and omits the required dimensional normalisation. — Write the product over coordinate-wise kernels with the n times h-to-the-d denominator or define a normalised multivariate radial kernel.
- [open] P1 — cell 15 — An integrated-squared-error sample-size rate is applied to mean absolute relative error. — Measure replicated integrated squared error for the stated rate or estimate sample requirements empirically for the actual loss.

## 18b_kernel_density_estimation_practical.ipynb

- [open] P1 — cell 8 — ROC-AUC is falsely said to be inflated by a large pool of true negatives. — Explain prevalence invariance for fixed class-conditional scores and how a small false-positive rate can still produce many false alarms.
- [open] P1 — cell 7 — The memorisation verdict accepts exact training copies and misinterprets large generated-to-training distances. — Remove the verdict and report distances descriptively against held-out real samples, explaining that KDE samples are training-centred kernel noise.

## 19a_normalizing_flows_theory.ipynb

- [open] P1 — cell 4 — The flow lesson reverses the density effect of expansion under the data-to-base map. — Describe compression under the generative map or reverse the stated intuition for the data-to-base map.
- [open] P1 — cell 0, 6, 9 — Triangular Jacobians are presented as a requirement for every normalizing flow. — Require an invertible transformation with tractable density calculation and describe triangular coupling layers as one architecture.

## 19b_normalizing_flows_practical.ipynb

- [open] P1 — cell 8 — The memorisation verdict accepts exact training copies and misinterprets large generated-to-training distances. — Remove the verdict and report distances descriptively against held-out real samples, explaining that KDE samples are training-centred kernel noise.

## 20a_nmf_ica_theory.ipynb

- [open] P1 — cell 12 — FastICA is falsely described as an exact Newton step. — Call it an approximate Newton or fixed-point update and show the Hessian approximation used in the derivation.

## 20b_nmf_ica_practical.ipynb

- [open] P1 — cell 9 — Low pairwise correlation is used to certify independence of non-Gaussian sources. — Describe the check only as a correlation diagnostic and generate sources independently or explain the deterministic example's limitations.

## 21a_em_variational_inference_theory.ipynb

- [open] P2 — cell 14 — A small Dirichlet concentration is misleadingly called a weak prior. — Describe its preference for sparse boundary-near weights and distinguish concentration, effective sample size and distribution shape.

## 22a_dirichlet_process_mixtures_theory.ipynb

- [open] P2 — cell 0, 9, 15 — The Dirichlet-process lesson implies reliable recovery of the generating component count and calls finite-chain inference exact. — Distinguish density estimation, sample partitions and generating components, discuss count inconsistency, and qualify finite-chain inference.

## 22b_dirichlet_process_mixtures_practical.ipynb

- [open] P2 — cell 9, 16 — The Dirichlet-process practical calls a thresholded weight count a posterior over cluster counts. — Report an actual posterior count distribution or narrow the claim and show sensitivity to the weight threshold.

## 23a_hidden_markov_models_theory.ipynb

- [open] P2 — cell 8 — HMM scaling notation confuses cumulative joint-message normalisers with incremental recursion normalisers. — Define a separate unnormalised intermediate message based on the previous normalised message and specify backward scaling indices.

## 24a_time_series_clustering_theory.ipynb

- [open] P1 — cell 7, 8 — The banded DTW implementation claims reduced memory and total runtime while allocating and initialising the full table. — Distinguish banded recurrence work from quadratic allocation and initialisation or store only the band with suitable backtracking data.

## 25a_word_embeddings_theory.ipynb

- [open] P1 — cell 13, 19 — The word-vector lesson rejects the standard input-vector-only similarity convention. — Present input vectors and summed input-plus-context vectors as alternative conventions and evaluate the choice.
- [open] P1 — cell 9, 10 — The SGNS experiment claims an exact match to its derivation despite changing the negative distribution and pair-count definitions. — Match noise sampling and training-pair counts to the derivation or derive the modified objective rather than relying on correlation.

## 26a_contrastive_learning_theory.ipynb

- [open] P1 — cell 7 — Word2vec negative sampling is incorrectly equated with noise-contrastive estimation. — Describe it as a related contrastive binary objective and explain the noise-correction and normalisation differences.
- [open] P1 — cell 9 — The InfoNCE proof replaces a random sum inside a logarithm by its expectation without preserving the claimed inequality. — Supply a valid finite-sample mutual-information lower-bound proof with its sampling assumptions.
- [open] P1 — cell 15, 16, 27 — The collapsed NT-Xent batch is falsely described as the maximum possible loss. — Call collapse a chance-level configuration and remove assertions that its loss is a ceiling or worst case.

## 26b_contrastive_learning_practical.ipynb

- [open] P1 — cell 7, 13 — Arbitrary score tolerances are presented as evidence of a statistical tie. — Call them practical tolerances or use paired uncertainty estimates and repeated runs with a stated inferential procedure.
- [open] P2 — cell 5, 7, 11–13 — The linear-probe protocol calls pretraining images held out and repeatedly inspects the same labelled test split. — Distinguish held-out labels from unseen images, disclose transductive evaluation, and reserve validation data for tuning before a final test.

## 27a_clustering_stability_theory.ipynb

- [open] P1 — cell 12, 13 — The consensus-CDF calculation omits parts of the integration interval and linearly joins an empirical step function. — Compute the full empirical CDF integral as one minus the mean off-diagonal consensus and explain that area alone does not measure ambiguity.

## 28_capstone_pipeline.ipynb

- [open] P2 — cell 6, 7, 16 — The capstone requires splitting without evaluating the holdout and then fits downstream models to the full dataset. — Distinguish descriptive fixed-data clustering from inductive generalisation and either evaluate a holdout or justify a full-data descriptive fit.
- [open] P2 — cell 15 — The capstone promises actionable segmentation but reports no original-unit segment profiles or concrete customer and review memberships. — Provide interpretable feature summaries, membership and review outputs, and the business meaning of proposed segments.

## CURRICULUM_PLAN.md and UNSUPERVISED_ML_PLAN.md

- [open] P3 — CURRICULUM_PLAN.md: lines 206–230, 339–354; UNSUPERVISED_ML_PLAN.md: lines 148–161, 330–345 — Competing planning documents retain obsolete notebook names and scope. — Identify one canonical plan and mark historical plans as archived with links to the current repository catalogue.

## README.md

- [open] P3 — line 129 — The catalogue advertises time-series K-Means although the theory notebook implements DTW k-medoids. — Name DTW k-medoids in the catalogue.
