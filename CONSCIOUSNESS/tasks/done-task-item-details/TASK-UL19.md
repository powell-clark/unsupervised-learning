# TASK-UL19: Association Rules Theory (9a)

## Context
First notebook of Lesson 9 (STORY-UL10, DIRECT-UL9) — Lesson 8 is Recommender Systems
(STORY-UL9), so Association Rules takes the next slot per README's lesson numbering.
Introduces association rule mining —
discovering frequent itemsets and "if you bought X, you're likely to buy Y" relationships in
unlabeled transaction data. Derives the Apriori algorithm and its supporting metrics.

## Acceptance Criteria
- [x] Itemsets, transactions, and the frequent-itemset framing
- [x] Support, confidence, and lift: definitions and interpretation
- [x] The Apriori principle (downward closure) and why it makes enumeration tractable
- [x] Apriori algorithm: candidate generation, pruning, frequent itemset mining
- [x] Rule generation from frequent itemsets
- [x] From-scratch NumPy/Python implementation of Apriori
- [x] Cross-check against a reference implementation
- [x] Visualization: support/confidence/lift for generated rules
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
Unlike every other lesson so far, association rules operate on categorical/binary
transaction data (items present or absent), not continuous feature vectors — no distance
metric involved. The Apriori principle (every subset of a frequent itemset is frequent) is
the key pruning insight that makes itemset enumeration tractable despite the combinatorial
explosion of possible itemsets.

## Dependencies
- Blocked by: TASK-UL2 (foundations groundwork)
- Blocks: TASK-UL20 (Association rules practical)
- Story: STORY-UL10 (Association-rule learner story)
- Directive: DIRECT-UL9 (Association Rules & Apriori)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
