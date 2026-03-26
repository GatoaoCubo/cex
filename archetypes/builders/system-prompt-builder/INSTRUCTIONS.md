---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for system_prompt
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a system_prompt

## Phase 1: RESEARCH
1. Identify the target agent: name, domain, primary function
2. Gather domain knowledge: what expertise does the agent need?
3. Analyze existing system_prompts via brain_query (avoid duplicates)
4. Identify knowledge boundaries: what the agent KNOWS vs does NOT know
5. Determine tone: formal/technical/conversational/authoritative
6. List tools the agent has access to (if any)
7. Identify safety constraints and boundary types to exclude

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 19 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Identity section: 2-4 sentences defining persona, domain expertise, voice
6. Write Rules section: 7-12 numbered ALWAYS/NEVER rules with justification
7. Write Output Format section: response structure, format type, constraints
8. Write Constraints section: knowledge boundary, safety level, boundary statement
9. Verify rules_count matches actual numbered rules in body
10. Check body <= 4096 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p03_sp_ pattern, kind == system_prompt, quality == null, required fields present, body has all 4 sections, rules_count matches
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: rules use ALWAYS/NEVER? Identity defines expertise? No task instructions leaked?
5. If score < 8.0: revise in same pass before outputting
