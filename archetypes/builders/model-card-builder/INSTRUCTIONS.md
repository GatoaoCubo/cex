---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for model_card
pattern: 3-phase pipeline (research → compose → validate)
---

# Instructions: How to Produce a model_card

## Phase 1: RESEARCH
1. Identify the model: name, provider, version
2. Find official docs: provider model page, pricing page, API reference
3. Extract all SCHEMA.md fields from official sources
4. Every data point needs a source URL — no exceptions
5. If data unavailable from official source: mark field null
6. Check multiple sources if one page is incomplete (model page + pricing page + changelog)

## Phase 2: COMPOSE
1. Read SCHEMA.md — this is the source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill frontmatter: all 26 fields (null OK for optional)
4. Write Boundary section (adapt from ARCHITECTURE.md)
5. Write Specifications table — every row has Source URL column (never `-`)
6. Write Capabilities table — 8 rows matching features object, booleans only
7. Write When to Use table — >= 5 scenarios with concrete alternatives
8. Write References — >= 1 official URL
9. Pricing: use BASE TIER. Document higher tiers in Specifications table.

## Phase 3: VALIDATE
1. Run validate_artifact.py if available [PLANNED], else validate manually against QUALITY_GATES.md
2. HARD gates (all must pass): id format, type, lp, quality==null, integers, provider enum
3. SOFT gates: check each against QUALITY_GATES.md table
4. Cross-check: every SCHEMA field populated? Every Spec row has URL?
5. Body under 4096 bytes?
6. If score < 8.0: revise in same pass before outputting
