---
kind: quality_gate
id: p11_qg_code_executor
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of code_executor artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: code_executor"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, code-executor, P04, sandbox, isolation, timeout]
tldr: "Pass/fail gate for code_executor artifacts: sandbox isolation, timeout policy, language listing, resource limits, and network access declaration."
domain: "Sandboxed code execution environments with isolation, language support, resource limits, and timeout policies"
created: "2026-03-28"
updated: "2026-03-28"
density_score: 0.90
related:
  - bld_examples_code_executor
  - bld_instruction_code_executor
  - p03_sp_code_executor_builder
  - bld_output_template_code_executor
  - code-executor-builder
  - p10_lr_code_executor_builder
  - bld_architecture_code_executor
  - bld_schema_code_executor
  - bld_knowledge_card_code_executor
  - p04_exec_python_sandbox
---

## Quality Gate

# Gate: code_executor
## Definition
| Field | Value |
|---|---|
| metric | code_executor artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: code_executor` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_exec_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or no p04_exec_ prefix |
| H03 | ID equals filename stem | `id: p04_exec_python` but file is `other_exec.md` |
| H04 | Kind equals literal `code_executor` | `kind: runtime` or `kind: sandbox` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `runtime`, `sandbox_type`, `languages`, or `timeout` |
| H07 | Languages list is non-empty | `languages: []` or languages field absent |
| H08 | Timeout is integer > 0 | `timeout: 0` or `timeout: -1` or absent |
| H09 | Sandbox type is valid enum | `sandbox_type: bare_metal` or unrecognized value |
| H10 | Body has required sections | Missing Overview, Sandbox, Languages, or Limits section |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Isolation documentation | 1.5 | Sandbox mechanism described with escape prevention details |
| Language versioning | 1.0 | Each language has version constraint, not just name |
| Resource limits detail | 1.0 | CPU, memory, disk limits specified with units |
| Network policy clarity | 1.0 | network_access explicitly stated with rationale |
| Timeout apownteness | 0.5 | Timeout reasonable for declared use case |
| File I/O policy | 0.5 | file_io explicitly stated with scope |
| Session model | 0.5 | persistent_session declared with cleanup policy if true |
| Pre-installed libraries | 0.5 | Libraries listed for each language |
| Boundary clarity | 1.0 | Explicitly not a cli_tool, daemon, or mcp_server |
| Security posture | 1.0 | No bare-metal, no unrestricted network, no unlimited resources |
| Domain specificity | 1.0 | Executor optimized for declared use case |
| Use case documentation | 0.5 | Primary use case and target user clearly stated |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Development-only executor for local testing |
| approver | Author self-certification with dev-only scope comment |
| audit_trail | Bypass note in frontmatter with expiry date |
| expiry | 14d — dev executors must be promoted or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored gates), H08 (no timeout = security risk) |

## Examples

# Examples: code-executor-builder
## Golden Example
INPUT: "Create code executor for Python data analysis in Docker sandbox"
OUTPUT:
```yaml
id: p04_exec_python_docker
kind: code_executor
pillar: P04
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
name: "Python Docker Executor"
runtime: python
sandbox_type: docker
languages:
  - "python 3.11+"
timeout: 60
resource_limits:
  cpu: "1 core"
  memory: "512MB"
  disk: "100MB"
network_access: false
file_io: true
persistent_session: false
quality: null
tags: [code_executor, python, docker, sandbox, data-analysis]
tldr: "Docker-sandboxed Python executor: 60s timeout, 512MB RAM, no network, file I/O enabled"
description: "Isolated Python 3.11+ executor in ephemeral Docker container for data analysis and computation"
```
## Overview
Executes Python code in an ephemeral Docker container for data analysis and computation.
Used by agents that need to run LLM-generated Python code safely — data processing, calculations, file transformations.
## Sandbox
Isolation: docker — each execution runs in a fresh container image, destroyed after completion.
Escape prevention: no host filesystem mount, no privileged mode, seccomp profile applied.
Session: ephemeral — no state carries between invocations.
## Languages
### Python
Version: 3.11+
Libraries: pandas, numpy, matplotlib, scipy (pre-installed in image)
## Limits
- Timeout: 60s per invocation
- CPU: 1 core (cgroup limit)
- Memory: 512MB (OOM-killed if exceeded)
- Disk: 100MB (tmpfs, wiped after execution)
- Network: blocked — no outbound connections
- File I/O: read-write within /workspace only
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_exec_ pattern (H02 pass)
- kind: code_executor (H04 pass)
- sandbox_type: docker (valid enum, H06 pass)
- languages: ["python 3.11+"] with version (H07 pass)
- timeout: 60 > 0 (H08 pass)
- Body has all 4 sections: Overview, Sandbox, Languages, Limits (H10 pass)
- resource_limits specified (S03 pass)
- network_access: false explicitly stated (S04 pass)
## Anti-Example
INPUT: "Create code executor"
BAD OUTPUT:
```yaml
id: executor
kind: runtime
name: Code Runner
languages: [any]
quality: 9.0
```
Runs code.
FAILURES:
1. id: "executor" has no `p04_exec_` prefix -> H02 FAIL
2. kind: "runtime" not "code_executor" -> H04 FAIL
3. quality: 9.0 (not null) -> H05 FAIL
4. Missing fields: sandbox_type, timeout, runtime -> H06 FAIL
5. languages: ["any"] — must be explicit language list -> H07 FAIL
6. No timeout defined — security risk -> H08 FAIL
7. No sandbox_type — bare metal execution implied -> H06 FAIL
8. Body missing Sandbox, Languages, Limits sections -> H10 FAIL
9. No resource limits — DoS risk -> S03 FAIL
10. No network policy stated -> S04 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
