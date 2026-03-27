---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for smoke_eval
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a smoke_eval

## Phase 1: RESEARCH
1. Identify the scope to smoke test (agent, service, pipeline)
2. Find existing smoke_evals for the same scope (search P07_evals/)
3. Identify the critical path (minimum viable checks)
4. List prerequisites that must exist before test runs
5. Check brain_query [IF MCP] for duplicate smoke_evals

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all required + recommended fields (quality: null)
4. Set timeout to maximum 30 seconds
5. Define critical_path: the shortest check sequence
6. Write Assertions section: fast, binary checks (pass/fail)
7. Set fast_fail: true (abort on first failure)
8. List prerequisites: environment, services, configs needed
9. Define frequency: how often this smoke should run

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, timeout <= 30
3. SOFT: critical_path defined, fast_fail true, prerequisites listed
4. Verify: total estimated runtime < 30 seconds
5. If score < 8.0: revise before outputting
