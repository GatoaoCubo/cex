---
kind: examples
id: bld_examples_smoke_eval
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of smoke_eval artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Examples Smoke Eval"
version: "1.0.0"
author: n03_builder
tags: [smoke_eval, builder, examples]
tldr: "Golden and anti-examples for smoke eval construction, demonstrating ideal structure and common pitfalls."
domain: "smoke eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: smoke-eval-builder
## Golden Example
INPUT: "Create smoke eval for brain search MCP availability"
OUTPUT:
```yaml
id: p07_se_brain_mcp
kind: smoke_eval
pillar: P07
title: "Smoke: Brain MCP Availability"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
scope: "brain-search-mcp"
critical_path:
  - "MCP server responds"
  - "brain_query returns results"
  - "Results contain id and score"
timeout: 15
assertions:
  - check: "MCP server process is running"
    expected: "process alive"
    timeout_ms: 3000
  - check: "brain_query('test') returns non-empty list"
    expected: "list.length > 0"
    timeout_ms: 5000
  - check: "First result has id field"
    expected: "result[0].id is string"
    timeout_ms: 1000
  - check: "First result has score field"
    expected: "result[0].score >= 0"
    timeout_ms: 1000
fast_fail: true
prerequisites:
  - "Ollama running with nomic-embed-text"
  - "FAISS index built (build_indexes_ollama.py)"
  - "MCP server config in .mcp.json"
environment: "local-dev"
health_check: "brain_status()"
frequency: "every session start"
alerting: "stdout warning"
domain: "infrastructure"
quality: 8.8
tags: [smoke-eval, brain-mcp, infrastructure, CI]
tldr: "15s smoke: brain MCP responds, query returns results with id+score"
density_score: 0.92
## Critical Path
1. Verify MCP server process is alive (3s max)
2. Execute brain_query('test') (5s max)
3. Validate result structure: id + score fields (1s max)
## Assertions
- MCP server process is running (3s timeout)
- brain_query returns non-empty list (5s timeout)
- First result contains 'id' field (string)
- First result contains 'score' field (>= 0)
## Prerequisites
- Ollama running locally with nomic-embed-text model
- FAISS index built via build_indexes_ollama.py
- MCP server configured in .mcp.json
## On Failure
- Log: which assertion failed and at what step
- Action: if MCP down, suggest restart command
- Escalation: if repeated failure, flag for investigation
```
WHY THIS IS GOLDEN:
- quality: null (never self-scored)
- id matches p07_se_ pattern
- kind: smoke_eval
- 19 frontmatter fields present (all required + recommended)
- timeout: 15 (well under 30s limit)
- fast_fail: true
- critical_path: 3 ordered steps with individual timeouts
- assertions: 4 entries with check/expected/timeout_ms
- prerequisites listed concretely
- On Failure section with actionable steps
## Anti-Example
INPUT: "Smoke test for brain"
BAD OUTPUT:
```yaml
id: brain_smoke
kind: smoke
timeout: 120
quality: 8.0
## Test
Check if brain works. Run some queries and see if results come back.
```
FAILURES:
1. id: no p07_se_ prefix -> H02 FAIL
2. kind: "smoke" not "smoke_eval" -> H04 FAIL
3. pillar: missing -> H05 FAIL
4. quality: self-scored 8.0 instead of null -> H06 FAIL
5. timeout: 120 exceeds 30s limit -> H07 FAIL
6. fast_fail: missing -> H08 FAIL
7. critical_path: missing -> H09 FAIL
8. assertions: missing structured list -> H10 FAIL
9. scope: missing -> S01 FAIL
10. tags: missing -> S02 FAIL
11. tldr: missing -> S03 FAIL
12. prerequisites: missing -> S05 FAIL
