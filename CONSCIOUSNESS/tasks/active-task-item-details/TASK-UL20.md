# TASK-UL20: Association Rules Practical (9b)

## Context
Second notebook of Lesson 9 (STORY-UL10, DIRECT-UL9). Applies mlxtend's Apriori and FP-Growth
to a larger, more realistic market-basket dataset, explores the minimum support/confidence
trade-off at scale, and extracts ranked, actionable business rules.

## Acceptance Criteria
- [x] Larger, realistic market-basket dataset (more items, more transactions than 9A)
- [x] mlxtend Apriori applied end to end: encoding, mining, rule extraction
- [x] FP-Growth applied to the same dataset for comparison
- [x] Apriori vs FP-Growth: runtime comparison as min_support shrinks (repeated scans vs FP-tree)
- [x] Minimum support/confidence trade-off: how threshold choice changes rule count and quality
- [x] Ranked, actionable business rules (e.g., top rules by lift with a support floor)
- [x] Visualization: rule count vs threshold, runtime comparison
- [x] Runs top-to-bottom in Google Colab

## Technical Notes
Builds on TASK-UL19's metrics and Apriori derivation. FP-Growth avoids Apriori's repeated
database scans by compressing transactions into a prefix tree (FP-tree), then mining frequent
itemsets by traversing conditional pattern bases — same frequent-itemset guarantee, different
mechanics, and it should get faster relative to Apriori as min_support drops and the naive
candidate-generation approach starts to explode.

## Dependencies
- Blocked by: TASK-UL19 (association rules theory)
- Blocks: none
- Story: STORY-UL10 (Association-rule learner story)
- Directive: DIRECT-UL9 (Association Rules & Apriori)
- Features: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy/production pairing)
