---
id: p11_qg_code_executor
kind: quality_gate
pillar: P11
title: "Gate: code_executor"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "Sandboxed code execution environments with isolation, language support, resource limits, and timeout policies"
quality: 9.0
tags: [quality-gate, code-executor, P04, sandbox, isolation, timeout]
tldr: "Pass/fail gate for code_executor artifacts: sandbox isolation, timeout policy, language listing, resource limits, and network access declaration."
density_score: 0.90
llm_function: GOVERN
---
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
