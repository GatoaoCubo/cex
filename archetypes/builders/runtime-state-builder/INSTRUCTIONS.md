---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for runtime_state
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a runtime_state

## Phase 1: RESEARCH
1. Identify the agent whose runtime state needs definition
2. Find existing runtime_states for similar agents (search P10_memory/examples/)
3. Map the agent's decision points during execution
4. Identify routing rules that change during runtime
5. Check brain_query [IF MCP] for duplicate runtime_states

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 17 required + 4 recommended fields (quality: null)
4. Define routing_rules: how the agent routes tasks at runtime
5. Define decision_tree: branch conditions and outcomes
6. Define priorities: ordered list of what the agent optimizes for
7. Define heuristics: rules of thumb for ambiguous situations
8. Define domain_map: what domains this agent covers at runtime
9. Define tools_available: tools the agent can invoke
10. Define constraints: limits on agent behavior at runtime
11. Define fallback: what happens when primary path fails
12. Define update_triggers: what causes state transitions

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, agent present
3. SOFT: routing_rules concrete, decision_tree has branches, priorities ordered
4. Verify: state is RUNTIME (not design-time or ephemeral)
5. If score < 8.0: revise before outputting
