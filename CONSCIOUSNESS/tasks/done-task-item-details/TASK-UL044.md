# TASK-UL044: Install and smoke-test Part II dependencies (hmmlearn, tslearn)

## Context
Lessons 23 (HMMs) and 24 (time-series clustering) need `hmmlearn` and `tslearn`, neither of which Part I used. Both have wheels for this Python (verified 2026-09-04: hmmlearn 0.3.3 cp312 manylinux, tslearn 0.9.0 py3-none-any). `requirements.txt` already lists them (added with the syllabus); this task makes the environment match and proves the imports work before any lesson depends on them.

## Acceptance Criteria
- [x] `pip install -r requirements.txt` completes without error in the executing environment — exit 0, hmmlearn 0.3.3 and tslearn 0.9.0 installed from prebuilt wheels (no compiler needed)
- [x] The bundled-dataset check prints a shape — `CachedDatasets().load_dataset('Trace')` returns (100, 275, 1) with 4 classes, **offline**. The dataset ships inside the tslearn wheel, so lesson 24b uses it directly; the synthetic fallback named on TASK-UL067's card is unnecessary (leave the generator in as a teaching aid if useful, but it is not a dependency)
- [x] Installed versions appended to the `## Environment` section of CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md

## Outcome
Both libraries import and run end to end, not merely import:
- `GaussianHMM(n_components=2, n_iter=20).fit()` on a simulated two-regime series recovers means [-0.02, 4.87] against a true [0, 5] and decodes both states — the lesson-23 machinery works.
- `TimeSeriesKMeans(n_clusters=2, metric='dtw').fit()` on synthetic sine/square shapes converges (inertia 0.093) — the lesson-24 machinery works, DTW backend included.

Smoke test kept at `/tmp` scratch only; the durable evidence is this card plus the syllabus Environment table.

## Execution
- Builder model: this session (opus). Expected duration 30m; actual ~4m.

## Dependencies
- Blocked by: none
- Blocks: the lesson 23 and 24 build tasks
