---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for learning_record
pattern: 3-phase pipeline (analyze -> compose -> validate)
---

# Instructions: How to Produce a learning_record

## Phase 1: ANALYZE
1. Identify the experience to document (success, failure, or partial)
2. Classify outcome: SUCCESS, PARTIAL, or FAILURE
3. Assign score: 0.0-10.0 based on objective impact
4. Identify patterns: what concrete steps led to this outcome
5. Identify anti-patterns: what failed or should be avoided
6. Check brain_query [IF MCP] for existing learning_records (avoid duplicates)
7. Determine reproducibility: can this outcome be reliably repeated

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 15 required + 7 extended fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Summary: dense overview in 2-3 sentences
6. Write Pattern: concrete reproducible steps that worked
7. Write Anti-Pattern: specific failures with observable symptoms
8. Write Context: environment, satellite, timing, constraints
9. Write Impact: measurable outcomes (time, errors, score deltas)
10. Write Reproducibility: conditions, confidence level, caveats

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id pattern, kind literal, quality null, required fields, outcome enum, score range
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: is pattern concrete (not vague advice)? Is anti-pattern specific?
5. If score < 8.0: revise in same pass before outputting
