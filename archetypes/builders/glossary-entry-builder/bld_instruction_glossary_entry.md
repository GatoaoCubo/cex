---
kind: instruction
id: bld_instruction_glossary_entry
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for glossary_entry
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a glossary_entry

## Phase 1: CLASSIFY

1. Identify the term to define — what single word or phrase needs a precise definition?
2. Determine domain context — in which domain or system does this term carry its specific meaning?
3. Check for existing definitions of the same term — avoid duplicating or contradicting an existing entry
4. List synonyms and abbreviations — what other names or short forms does this term go by?
5. Identify potential confusion with similar terms — which nearby terms could be mistaken for this one?
6. Find canonical usage examples — where in the codebase, documentation, or domain is this term used correctly?

## Phase 2: COMPOSE

1. Read SCHEMA.md — source of truth for all 15+ required fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: all 15+ fields, null is acceptable for optional fields, quality: null (never self-score)
4. Write Term section: the exact term being defined, including casing and any abbreviation form
5. Write Definition section: maximum 3 lines, precise and unambiguous, no filler or aspirational language
6. Write Synonyms section: alternative names and abbreviations, even if only one exists
7. Write Context section: the domain where this definition applies and any scope restrictions
8. Write Related Terms section: linked terms for navigation to nearby concepts
9. Write Usage Example section: one sentence showing correct usage of the term in context
10. Check body size — must stay at or below 1024 bytes

## Phase 3: VALIDATE

1. Check QUALITY_GATES.md — run all HARD gates manually
2. HARD gates:
   - [ ] id matches `p01_ge_[a-z][a-z0-9_]+`
   - [ ] kind == `glossary_entry`
   - [ ] quality == null
   - [ ] definition is 3 lines or fewer
   - [ ] term is a single concept (not a phrase defining a whole domain)
   - [ ] at least 1 synonym or abbreviation listed
   - [ ] body <= 1024 bytes
3. SOFT gates: tldr <= 160 chars, tags >= 3, usage example present, related terms linked
4. Cross-check: single term not deep knowledge (that is knowledge_card)? Not domain overview (that is context_doc)? Not an embedding configuration? Definition is precise not aspirational?
5. If score < 8.0: revise in the same pass before outputting
