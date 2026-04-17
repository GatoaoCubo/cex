---
id: p03_ins_spawn_config
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Spawn Config Builder Instructions
target: "spawn-config-builder agent"
phases_count: 4
prerequisites:
  - "Target director name is known and non-empty"
  - "Spawn mode is specified: solo, grid, or continuous"
  - "Director-model pairing is defined (e.g. builder_agent=opus, research_agent=sonnet)"
  - "Handoff file path or inline prompt is available"
validation_method: checklist
domain: spawn_config
quality: 9.0
tags: [instruction, spawn-config, orchestration, director, P12]
idempotent: true
atomic: false
rollback: "Delete generated spawn_config YAML file"
dependencies: []
logging: true
tldr: "Build a director spawn_config YAML with CLI flags, MCP profile, timeout policy, and prompt sizing for solo/grid/continuous modes."
density_score: 0.92
llm_function: REASON
---
## Context
The spawn-config-builder produces a `spawn_config` artifact — a structured YAML that defines exactly how a director process is launched. Downstream orchestration scripts consume this artifact to spawn terminals with the correct flags, model, MCP profile, timeout, and prompt strategy.
**Input contract**:
- `director`: string — canonical director name (e.g. `builder_agent`, `research_agent`, `marketing_agent`)
- `mode`: enum — `solo` | `grid` | `continuous`
- `model`: string — LLM model identifier (e.g. `claude-opus-4-6`, `claude-sonnet`)
- `task_description`: string — what the director must accomplish (used to size the prompt)
- `handoff_file`: string or null — relative path to handoff `.md` file if task exceeds 200 chars
- `mcp_profile`: string or null — path to `.mcp-{sat}.json` if director requires MCP tools
- `timeout_ms`: integer or null — override default timeout (default: 120000 for solo, 300000 for grid/continuous)
**Output contract**: a single `spawn_config` YAML block with 19 required fields, ready to be written to `records/spawn_configs/{director}_{mode}.yaml`.
**Variables used throughout**:
- `{{director}}` — uppercased director name
- `{{mode}}` — spawn mode
- `{{model}}` — model identifier
- `{{inline_prompt}}` — prompt string <= 200 chars
- `{{handoff_path}}` — relative path to handoff file
- `{{mcp_path}}` — path to MCP config file
## Phases
### Phase 1: Analyze Requirements
**Action**: Parse all inputs and determine prompt strategy.
```
IF len(task_description) <= 200:
    prompt_strategy = "inline"
    inline_prompt = task_description
    handoff_path = null
ELSE:
    prompt_strategy = "handoff"
    inline_prompt = "Read handoff file and execute: " + handoff_file
    handoff_path = handoff_file
    ASSERT len(inline_prompt) <= 200
```
Also determine:
- `interactive_mode`: always `true` for grid/continuous; `true` for solo unless explicitly headless
- `timeout_ms`: use provided value, else apply defaults (solo=120000, grid=300000, continuous=600000)
- `mcp_required`: `true` if `mcp_profile` is not null
Verifiable exit: prompt_strategy is set; inline_prompt length <= 200; timeout_ms is an integer.
### Phase 2: Resolve CLI Flags
**Action**: Build the ordered CLI flags list for the director launch command.
```
flags = ["--dangerously-skip-permissions", "--no-chrome"]
IF prompt_strategy == "handoff":
    flags.append("-p")   # non-interactive dispatch skips workspace trust prompt
IF mcp_required:
    flags.append("--mcp-config " + mcp_path)
    flags.append("--strict-mcp-config")
IF model is not null:
    flags.append("--model " + model)
```
Rules:
- `-p` flag is MANDATORY when using handoff files (prevents workspace trust hang)
- `--mcp-config` MUST use a relative path, never absolute (avoids PS->cmd chain hang)
- `--no-chrome` is always present; browser access requires separate boot script
Verifiable exit: flags list contains `--dangerously-skip-permissions`; `-p` present iff prompt_strategy == "handoff".
### Phase 3: Compose spawn_config YAML
**Action**: Assemble all resolved values into the 19-field YAML structure.
Required fields in order:
1. `id` — `spawn_{director}_{mode}`
2. `kind` — `spawn_config`
3. `pillar` — `P12`
4. `version` — `1.0.0`
5. `director` — `{{director}}`
6. `mode` — `{{mode}}`
7. `model` — `{{model}}`
8. `prompt_strategy` — `inline` or `handoff`
9. `inline_prompt` — `{{inline_prompt}}`
10. `handoff_path` — `{{handoff_path}}` or `null`
11. `cli_flags` — list from Phase 2
12. `mcp_profile` — `{{mcp_path}}` or `null`
13. `interactive` — boolean
14. `timeout_ms` — integer
15. `spawn_delay_ms` — `5000` (always; prevents terminal race conditions)
16. `retry_on_failure` — `true`
17. `max_retries` — `2`
18. `log_output` — `true`
19. `created` — ISO date string
Verifiable exit: YAML parses cleanly; all 19 fields present; no null for required non-nullable fields.
### Phase 4: Validate Against Quality Gates
**Action**: Run the 8 HARD gates before emitting output.
```
HARD gates (all must pass):
  H1: director name is non-empty and matches known director list
  H2: mode is one of [solo, grid, continuous]
  H3: inline_prompt length <= 200 characters
  H4: cli_flags contains "--dangerously-skip-permissions"
  H5: if prompt_strategy == "handoff", cli_flags contains "-p"
  H6: timeout_ms is a positive integer
  H7: spawn_delay_ms == 5000
  H8: all 19 YAML fields are present
SOFT gates (log warnings, do not block):
  S1: model field matches a known model identifier
  S2: handoff_path points to an existing file (if not null)
  S3: mcp_profile path ends in .json (if not null)
  S4: retry config is reasonable (max_retries <= 5)
```
If any HARD gate fails: fix the violation and re-validate. Do not emit until all HARD gates pass.
Verifiable exit: checklist shows 8/8 HARD pass.
## Output Contract
```yaml
id: spawn_`{{director}}`_`{{mode}}`
kind: spawn_config
pillar: P12
version: 1.0.0
director: `{{director}}`
mode: `{{mode}}`
model: `{{model}}`
prompt_strategy: `{{prompt_strategy}}`
inline_prompt: "`{{inline_prompt}}`"
handoff_path: `{{handoff_path}}`
cli_flags:
  - "--dangerously-skip-permissions"
  - "--no-chrome"
  # "-p" included when prompt_strategy is handoff
