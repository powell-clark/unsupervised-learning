# TASK-UL20: Association Rules Practical (9b)

## Context
Second notebook of Lesson 9 (STORY-UL10, DIRECT-UL9). Applies mlxtend's Apriori and FP-Growth
to a larger, more realistic market-basket dataset, explores the minimum support/confidence
trade-off at scale, and extracts ranked, actionable business rules.

## Acceptance Criteria
- [ ] Larger, realistic market-basket dataset (more items, more transactions than 9A)
- [ ] mlxtend Apriori applied end to end: encoding, mining, rule extraction
- [ ] FP-Growth applied to the same dataset for comparison
- [ ] Apriori vs FP-Growth: runtime comparison as min_support shrinks (repeated scans vs FP-tree)
- [ ] Minimum support/confidence trade-off: how threshold choice changes rule count and quality
- [ ] Ranked, actionable business rules (e.g., top rules by lift with a support floor)
- [ ] Visualization: rule count vs threshold, runtime comparison
- [ ] Runs top-to-bottom in Google Colab

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
