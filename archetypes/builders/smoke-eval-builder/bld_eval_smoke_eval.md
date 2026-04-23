---
kind: quality_gate
id: p11_qg_smoke-eval
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of smoke_eval artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Smoke Eval'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: Gates ensuring smoke eval files define a critical path, binary pass/fail assertions,
  a timeout under 30s, and no deep correctness testing.
domain: smoke_eval
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - bld_collaboration_smoke_eval
  - bld_examples_smoke_eval
  - bld_knowledge_card_smoke_eval
  - bld_memory_smoke_eval
  - p03_sp_smoke_eval_builder
  - smoke-eval-builder
  - p11_qg_unit_eval
  - bld_config_smoke_eval
  - p03_ins_smoke_eval_builder
  - bld_output_template_smoke_eval
---

## Quality Gate

## Definition
A smoke eval is a fast sanity check (under 30 seconds) that confirms the most critical path of a system is alive and reachable. It does not verify correctness, edge cases, or performance — those belong to deeper eval types. A smoke eval passes this gate when every assertion is binary (pass or fail, no partial credit), the critical path covers the highest-impact flow, and the eval fails fast on the first hard error rather than accumulating multiple failures.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`smoke-eval-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `smoke_eval` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Critical path** definition (the single most important user or system flow being verified) | Without a named critical path, the eval may check low-value flows while missing failures in high-value ones |
| H08 | Spec contains an **Assertions list** (each assertion is a named binary check: pass or fail, no partial states) | Non-binary assertions introduce ambiguity into CI pass/fail decisions |
| H09 | Spec contains a **Timeout** value that is <= 30 seconds | Evals exceeding 30s are no longer smoke evals; they block CI pipelines and defeat the purpose |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Assertions are binary pass/fail (no graded or scored assertions) | 1.0 | Assertions use scores or ranges | Mixed binary and graded | Every assertion is strictly pass or fail with no ambiguous middle state |
| 3 | Critical path covers the most important flow (not a secondary or convenience flow) | 1.0 | Covers peripheral feature | Covers important but not highest-impact flow | Covers the flow whose failure would cause the most user or system impact |
| 4 | Fast-fail on first hard error (eval halts and reports on first assertion failure) | 1.0 | Runs all assertions regardless | Partial fast-fail | Explicitly configured to halt on first failure with clear fail message |
| 5 | Health check components listed (services, endpoints, or dependencies checked before assertions begin) | 1.0 | No health checks | One component listed | All external dependencies checked before assertions begin |
| 6 | Tags include `smoke-eval` | 0.5 | Missing | Present but misspelled | Exactly `smoke-eval` in tags list |
| 7 | CI integration notes (invocation command, required env vars, expected output on pass) | 1.0 | No CI notes | Invocation command only | Invocation command + required env vars + expected output on pass |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
