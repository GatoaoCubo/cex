---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for permission
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a permission

## Phase 1: RESEARCH
1. Identify the scope: what resource, agent, or artifact needs access control
2. Find existing permissions for the same scope (search P09_config/examples/)
3. Determine the roles involved: who needs read, write, execute access
4. Research access patterns for the domain (RBAC, ABAC, ACL)
5. Check brain_query [IF MCP] for duplicate permissions

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 17 required + 4 recommended fields (quality: null)
4. Set scope to the resource or artifact being protected
5. Define read rules: who can view and under what conditions
6. Define write rules: who can modify and under what conditions
7. Define execute rules: who can run and under what conditions
8. Define roles with inheritance hierarchy
9. Write allow_list: explicitly permitted role-action pairs
10. Write deny_list: explicitly forbidden role-action pairs (deny overrides allow)
11. Write audit section: what gets logged and when
12. Write escalation section: how to request elevated access

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, scope present
3. SOFT: read/write/execute defined, roles concrete, audit specified
4. Verify: deny_list overrides allow_list (precedence correct)
5. If score < 8.0: revise before outputting
