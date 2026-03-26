---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for knowledge_card
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a knowledge_card

## Phase 1: RESEARCH
1. Identify the topic: what atomic fact needs capturing?
2. Determine KC kind: domain_kc (external) or meta_kc (CEX-internal)
3. Gather sources: official docs, APIs, code, established references
4. Extract key concepts, patterns, rules, comparisons
5. Check brain_query [IF MCP] for existing KCs on same topic (avoid duplicates)
6. Every data point needs a source — URLs for external, artifact refs for internal

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: 13 required + 6 CEX fields (null OK for optional)
4. Set quality: null (NEVER self-score — validator H05 enforces this)
5. Write body using correct structure:
   - domain_kc: Quick Reference, Key Concepts, Strategy Phases, Golden Rules, Flow, Comparativo, References
   - meta_kc: Executive Summary, Spec Table, Patterns, Anti-Patterns, Application, References
6. Ensure >= 4 sections with >= 3 non-empty lines each (validator S06, S08)
7. Keep bullets <= 80 chars (validator S10)
8. Include >= 1 external URL in body (validator S13)
9. Include axioms in frontmatter — actionable rules (validator S18)
10. Total body: 200-5120 bytes (validator H08)

## Phase 3: VALIDATE
1. Run: `python _tools/validate_kc.py <file>` (ACTIVE tool — use it!)
2. HARD gates (all 10 must pass): YAML, id, format, kind, quality, fields, tags, size, paths, author
3. SOFT gates (20 checks): see QUALITY_GATES.md
4. Cross-check: density >= 0.80? No filler? No self-refs in tldr?
5. If HARD fails: fix immediately, re-run validator
6. If score < 8.0: expand thin sections, add tables/code, remove filler
7. Target: PUBLISH (>= 8.0) minimum, GOLDEN (>= 9.5) ideal
