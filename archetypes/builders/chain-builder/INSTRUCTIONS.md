---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for chain
pattern: 3-phase pipeline (design -> compose -> validate)
---

# Instructions: How to Produce a chain

## Phase 1: DESIGN
1. Identify the pipeline purpose: what input-to-output transformation?
2. Decompose into atomic prompt steps (each step = 1 LLM call, 1 purpose)
3. Analyze existing chains via brain_query [IF MCP] (avoid duplicates)
4. Determine flow type: sequential (A->B->C), branching, parallel, or mixed
5. Define typed input/output for each step (string, list, JSON, markdown)
6. Choose error strategy: fail_fast for critical paths, skip for enrichment
7. Determine context passing: full (all prior output), filtered, or summary

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 19 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Purpose section: 2-4 sentences on what transformation this chain performs
6. Write Steps section: numbered steps with Input/Prompt/Output for each
7. Write Data Flow section: ASCII diagram showing step connections
8. Write Error Handling section: strategy, failure behavior, retry policy
9. Verify steps_count matches actual numbered steps in body
10. Check body <= 6144 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p03_ch_ pattern, kind == chain, quality == null, required fields present, body has all 4 sections, steps_count matches
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: steps have typed I/O? Data flow diagram matches steps? No runtime orchestration leaked?
5. If score < 8.0: revise in same pass before outputting
