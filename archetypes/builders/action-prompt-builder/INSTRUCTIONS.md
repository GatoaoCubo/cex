---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for action_prompt
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an action_prompt

## Phase 1: RESEARCH
1. Identify the action: what task needs a prompt, expressed as verb phrase
2. Define input: what data types and formats are provided
3. Define output: what the result should look like (structure, format)
4. Analyze existing action_prompts via brain_query (avoid duplicates)
5. Enumerate edge cases: at least 2 scenarios where things could go wrong
6. Determine constraints: what the prompt must NOT do
7. Identify purpose: WHY this action prompt is needed (not just WHAT it does)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 21 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Context section: 2-3 sentences on background and purpose
6. Write Input section: specific data items with types and formats
7. Write Execution section: concise steps to transform input into output
8. Write Output section: expected structure, format, and examples
9. Write Validation section: criteria to verify output correctness
10. Check body <= 3072 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p03_ap_ pattern, kind == action_prompt, quality == null, required fields present, body has all 5 sections, edge_cases >= 2
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: action is verb phrase? Input specific? No identity/persona? No detailed recipe?
5. If score < 8.0: revise in same pass before outputting
