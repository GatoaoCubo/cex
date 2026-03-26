---
lp: P03
llm_function: REASON
purpose: Step-by-step production process for model_card
---

# Instructions: How to Produce a model_card

## Phase 1: RESEARCH (INJECT)
1. Identify the model: name, provider, version
2. Find official docs: pricing page, API docs, model page
3. Extract: context_window, max_output, pricing, capabilities, knowledge_cutoff
4. Verify each data point against official source (URL required)
5. If data unavailable: mark field as null, add comment

## Phase 2: COMPOSE (PRODUCE)
1. Read OUTPUT_TEMPLATE.md — follow exactly
2. Fill frontmatter: all 26 fields (null OK for optional)
3. Write Boundary section (copy from ARCHITECTURE.md, adapt)
4. Write Specifications table (every row needs Source column)
5. Write Capabilities table (booleans only, no prose)
6. Write When to Use table (>= 3 scenarios with alternatives)
7. Write References (>= 1 official URL)

## Phase 3: VALIDATE (GOVERN)
1. Run QUALITY_GATES.md checks mentally
2. Verify: id == filename stem, type == model_card, lp == P02
3. Verify: quality == null (never self-score)
4. Verify: pricing has concrete numbers (no "varies")
5. Verify: context_window is exact integer (no "up to")
6. Verify: all capabilities are boolean (no prose)
7. If score < 8.0: loop back to Phase 2

## Variants
- **spec_card**: single model documentation (default)
- **comparison_card**: 2+ models compared side-by-side
  For comparison: use EXAMPLES.md comparison variant
