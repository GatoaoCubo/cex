---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agent artifact
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an agent

## Phase 1: RESEARCH
1. Identify the agent name and primary domain
2. Determine the owning satellite (STELLA, SHAKA, LILY, EDISON, PYTHA, ATLAS, YORK, or agnostic)
3. List 4-8 concrete capabilities the agent has
4. List tools the agent uses (MCP servers, scripts, APIs)
5. Identify upstream agents (who sends tasks to this agent)
6. Identify downstream agents (who receives output from this agent)
7. Search for existing agents via brain_query [IF MCP] (avoid duplicates)
8. Define domain boundary (what this agent handles vs what it routes away)
9. Collect routing keywords (4-8 terms that trigger this agent in brain search)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Generate agent_slug in snake_case (e.g., knowledge_card_builder)
4. Fill frontmatter: all required fields (quality: null, never self-score)
5. Set llm_function: BECOME (always, never override)
6. Write Overview section: 2-3 sentences on who, domain, primary function
7. Write Architecture section: capabilities list + tools table + satellite position
8. Write File Structure section: list all 10 required ISO files with correct naming
9. Write When to Use section: triggers, keywords, NOT when exclusions
10. Write Input/Output section: required inputs, optional inputs, primary output
11. Write Integration section: upstream, downstream, signal type
12. Write Quality Gates section: reference HARD and SOFT gates
13. Write Common Issues section: 3-5 failure modes with remediation
14. Write Invocation section: spawn command or invocation pattern
15. Write Related Agents section: 2-4 siblings with relationship type
16. Set capabilities_count to match actual bullets in Architecture
17. Set tools_count to match actual tools listed
18. Check body <= 5120 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 7 HARD gates pass
3. Score each SOFT gate against QUALITY_GATES.md
4. Confirm id matches p02_agent_ pattern
5. Confirm kind == agent
6. Confirm quality == null
7. Confirm iso_vectorstore lists >= 10 ISO files
8. Confirm llm_function == BECOME
9. Confirm satellite field is set (not blank)
10. If score < 8.0: revise before outputting
