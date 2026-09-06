# FEAT-UL9: Association Rules Lesson

**Status:** maintained | **Kano:** performance | **Priority:** p3

## Description
Comprehensive lesson on association rule mining: support, confidence, lift metrics, Apriori algorithm, and frequent itemset mining. Covers basket analysis from first principles alongside FP-Growth and practical market-basket applications.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook: Frequent itemsets and itemset mining problem
- [x] **AC-2** — Theory notebook: Support, confidence, lift metric definitions
- [x] **AC-3** — Theory notebook: Apriori algorithm with candidate generation and pruning
- [x] **AC-4** — Theory notebook: A priori principle and monotonicity property
- [x] **AC-5** — Practical notebook: mlxtend Apriori implementation
- [x] **AC-6** — Practical notebook: FP-Growth for frequent patterns
- [x] **AC-7** — Practical notebook: Association rule generation (confidence, lift filtering)
- [x] **AC-8** — Practical notebook: Market-basket analysis case study (retail transactions)
- [x] **AC-9** — Practical notebook: Interpreting rules for business decisions
- [x] **AC-10** — Both notebooks run end-to-end in Google Colab — verified via jupyter execute under TASK-UL040, 7/7 and 7/7 cells, zero errors
- [x] **AC-11** — Handling sparse transaction data efficiently — demonstrated via one-hot transaction encoding plus a dedicated Apriori-vs-FP-Growth runtime-scaling comparison as min_support shrinks, rather than the literal word "sparse"
- [x] **AC-12** — Completed task pair: TASK-UL19 (theory) and TASK-UL20 (practical)

## Review (TASK-UL041)
Independent agent review against notebooks/9a_association_rules_theory.ipynb
and 9b_association_rules_practical.ipynb: all 12 criteria verified via
section headers plus direct content read of the runtime-comparison cell for
AC-11 (the one criterion not literally keyword-matched on first pass).
agent-approved — stays in backlog pending human sign-off per the
FEAT-UL14 precedent.

## Linked Entities
- Story: STORY-UL10 (Association rules learner story)
- Directive: DIRECT-UL9 (Association Rules & Apriori)
- Tasks: TASK-UL19, TASK-UL20
- Feature set: FEAT-UL1 (Colab-runnable), FEAT-UL2 (NumPy-production)

## Human sign-off
Operator ruling in chat 2026-09-06 14:48, relayed by the kernel (MSG-EGLPK006): signed off. The FEAT-UL14 precedent (agent-approved features held pending explicit human sign-off before promotion to maintained) is lifted for this card by that ruling. Human verdict recorded in REVIEW-INDEX.md (reviewer_type=human, reviewer_id=operator, verdict=human-approved).
