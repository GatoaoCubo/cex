---
lp: P03
llm_function: REASON
purpose: Step-by-step production process for knowledge_card
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a knowledge_card

## Phase 1: RESEARCH
1. Identify the topic: what atomic fact needs capturing
2. Check for existing KCs: brain_query("{topic}") to avoid duplicates
3. Gather source material: official docs, code analysis, expert input
4. Determine body structure: domain_kc (subject) or meta_kc (system/spec)
5. Extract 3-5 key concepts and 3+ golden rules
6. Identify keywords (BM25), long_tails (semantic), axioms (actionable)
7. If topic too broad: split into 2+ cards (atomicity principle)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: 13 required fields + 6 CEX extensions
4. quality: null (ALWAYS — never self-score)
5. Write body using chosen structure (domain_kc or meta_kc)
6. Every bullet max 80 chars
7. Include at least 1 code block or table (density + visual)
8. Include at least 1 linked_artifact if related CEX artifacts exist
9. Ensure tldr < 160 chars, standalone, no self-reference
10. Check total size < 5120 bytes

## Phase 3: VALIDATE
1. Run: `python _tools/validate_kc.py <file>` (ACTIVE tool)
2. All 10 HARD gates must pass (H01-H10)
3. Check SOFT gates against QUALITY_GATES.md
4. Cross-check: frontmatter fields match body content
5. Verify no filler phrases (S09) and no self-references (S02)
6. Verify no duplicate sentences (S19, Jaccard >= 0.85)
7. If HARD fail: fix immediately, re-validate
8. If score < 8.0: revise in same pass before outputting
