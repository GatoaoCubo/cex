---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for glossary_entry
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a glossary_entry

## Phase 1: DISCOVER
1. Identify the term: what word/phrase needs defining?
2. Check brain_query for existing glossary entries (avoid duplicates)
3. Determine domain context: where is this term used in CEX?
4. List synonyms and abbreviations
5. Check if disambiguation is needed (similar terms exist?)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 15+ fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write definition: max 3 lines, concrete, no filler
6. Write Usage section: where/how the term appears
7. Write Disambiguation section: how this differs from similar terms (if needed)

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p01_gl_ pattern, kind == glossary_entry, definition <= 3 lines, quality == null
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: still a definition? Not drifting into knowledge_card depth? Not drifting into context_doc scope?
5. If score < 8.0: revise in same pass before outputting
