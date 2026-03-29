---
kind: instruction
id: bld_instruction_chunk_strategy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for chunk_strategy
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a chunk_strategy
## Phase 1: RESEARCH
1. Identify the use case and target system
2. Determine which pattern fits (Fixed-size, Recursive character, Semantic, Document-structure)
3. List required parameters with concrete values
4. Check for existing chunk_strategy artifacts to avoid duplicates
5. Confirm slug for id: snake_case, lowercase, no hyphens
6. Review KNOWLEDGE.md for domain patterns and anti-patterns
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (id, kind, pillar, version, created, updated, author, name, method, chunk_size, chunk_overlap, separators, quality, tags, tldr), quality: null
4. Write Overview section: what it does, who uses it
5. Write Method section: core definition with concrete values
6. Write Parameters section: parameter table with value and rationale columns
7. Write Integration section: upstream/downstream connections
8. Verify body <= 2048 bytes
9. Verify id matches `^p01_chunk_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p01_chunk_`
4. Confirm kind == chunk_strategy
5. Confirm all required body sections present: Overview, Method, Parameters, Integration
6. HARD gates: frontmatter valid, id pattern matches, kind correct, required fields present
7. SOFT gates: score against QUALITY_GATES.md dimensions
8. Cross-check boundary: is this truly a chunk_strategy and not embedding_config (vector model params)?
9. Revise if score < 8.0 before outputting
