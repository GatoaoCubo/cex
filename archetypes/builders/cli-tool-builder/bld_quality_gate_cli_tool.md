---
id: p11_qg_cli_tool
kind: quality_gate
pillar: P11
title: "Gate: cli_tool"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "command-line tool definition — point-in-time executables with declared commands, flags, and exit codes"
quality: 9.0
tags: [quality-gate, cli-tool, P04, command-line, exit-codes, output-format]
tldr: "Pass/fail gate for cli_tool artifacts: command completeness, exit code semantics, output format declaration, and flag documentation."
density_score: 0.90
llm_function: GOVERN
---
# Gate: cli_tool
## Definition
| Field | Value |
|---|---|
| metric | cli_tool artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: cli_tool` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_tool` but file is `other_tool.md` |
| H04 | Kind equals literal `cli_tool` | `kind: script` or `kind: skill` or any other value |
| H05 | Quality field is null | `quality: 7.5` or any non-null value |
| H06 | All required fields present | Missing `commands`, `output_format`, or `exit_codes` |
| H07 | At least one command defined | `commands: []` or commands field absent |
| H08 | Exit codes include 0 (success) and at least one error code | Only exit code 0 defined; no failure paths documented |
| H09 | Output format is one of: text, json, table, yaml | `output_format: costm` or unrecognized value |
| H10 | Tool is non-persistent | Tool runs and terminates; no daemon or background process behavior documented |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Command coverage | 1.0 | All meaningful operations exposed as named commands or subcommands |
| Flag documentation | 1.0 | Each flag has name, type, default, and description; no undocumented flags |
| Exit code semantics | 1.0 | Each exit code has specific meaning (not generic "error"); maps to failure category |
| Output format consistency | 0.5 | All commands produce the same declared output format |
| Config file documentation | 0.5 | Config file path and schema documented if tool supports config files |
| Env var overrides | 0.5 | Environment variable overrides listed for key settings |
| Help text quality | 1.0 | Usage example provided per command; help flag (--help) behavior described |
| Error message clarity | 1.0 | Error output (stderr vs stdout) distinguished; error messages are actionable |
| Idempotency declaration | 0.5 | Commands that mutate state declare whether re-run is safe |
| Boundary clarity | 1.0 | Explicitly not a daemon, skill, or plugin — one-shot execution contract stated |
| Domain specificity | 1.0 | Commands, flags, and outputs specific to the declared domain problem |
| Testability | 1.0 | Each command testsble with known input; expected output documented |
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
| conditions | Internal debug tool used only during development, never shipped to end users |
| approver | Author self-certification with comment explaining debug-only scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — debug tools must be promoted to >= 7.0 or removed from repo |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |
