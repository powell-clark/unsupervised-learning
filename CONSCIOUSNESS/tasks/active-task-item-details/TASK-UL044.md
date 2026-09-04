# TASK-UL044: Install and smoke-test Part II dependencies (hmmlearn, tslearn)

## Context
Lessons 23 (HMMs) and 24 (time-series clustering) need `hmmlearn` and `tslearn`, neither of which Part I used. Both have wheels for this Python (verified 2026-09-04: hmmlearn 0.3.3 cp312 manylinux, tslearn 0.9.0 py3-none-any). `requirements.txt` already lists them (added with the syllabus); this task makes the environment match and proves the imports work before any lesson depends on them.

## Acceptance Criteria
- [ ] `pip install -r requirements.txt` completes without error in the executing environment
- [ ] `python3 -c "import hmmlearn, tslearn; from hmmlearn.hmm import GaussianHMM; from tslearn.clustering import TimeSeriesKMeans; from tslearn.datasets import CachedDatasets; print(CachedDatasets().load_dataset('Trace')[0].shape)"` prints a shape (confirms the bundled dataset ships with the package — if it does not, note it on this card so lesson 24b uses its synthetic fallback)
- [ ] Installed versions appended to the `## Environment` section of CONSCIOUSNESS/artifacts/ul-part-ii-syllabus.md

## Execution
- Builder model: the session model (sonnet is sufficient)
- Expected duration: 30m

## Dependencies
- Blocked by: none
- Blocks: the lesson 23 and 24 build tasks
