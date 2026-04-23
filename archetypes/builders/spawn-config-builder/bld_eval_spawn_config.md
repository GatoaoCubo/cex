---
kind: quality_gate
id: p11_qg_spawn_config
pillar: P12
llm_function: GOVERN
purpose: Golden and anti-examples of spawn_config artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Spawn Config'
version: 1.0.0
author: builder
tags:
- eval
- P12
- quality_gate
- examples
tldr: Validates agent_group spawn configurations for mode, CLI flags, model pairing,
  and runtime safety.
domain: spawn_config
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - p01_kc_spawn_config
  - spawn-config-builder
  - bld_collaboration_spawn_config
  - bld_knowledge_card_spawn_config
  - bld_memory_spawn_config
  - bld_examples_spawn_config
  - bld_output_template_spawn_config
  - bld_architecture_spawn_config
  - p03_sp_spawn-config-builder
  - p11_qg_system_prompt
---

## Quality Gate

## Definition
A spawn config defines how a agent_group process is launched: execution mode (solo, grid, or continuous), CLI flags passed to the runtime, the model driving the agent_group, and how prompts and recovery are handled. This gate ensures every spawn config is safe to execute without human intervention and unambiguous to the launch runtime.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p12_sc_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `spawn_config` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `mode`, `agent_group`, `model`, `cli_flags`, `prompt` all defined and non-empty |
| H07 | Mode is valid enum | `mode` is one of: `solo`, `grid`, `continuous` |
| H08 | CLI flags defined | `cli_flags` is a non-empty list with at least one entry |
| H09 | Agent_group-model pairing | `agent_group` and `model` are both non-empty strings |
| H10 | Prompt size within limits | Inline `prompt` is <= 200 characters; longer prompts reference a handoff file path |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | Config is concise; no redundant or placeholder fields |
| Timeout policies per mode | 1.0 | Each mode defines a `timeout_ms` or `timeout_per_step_ms` |
| MCP config path validated | 1.0 | If `mcp_config` is set, path follows `.mcp-{sat}.json` pattern |
| Interactive mode documented | 0.5 | `interactive` flag is explicit (true/false, not omitted) |
| Tags include spawn-config | 0.5 | `tags` list contains `"spawn-config"` |
| Handoff file reference | 0.5 | If task is complex, `handoff_file` field points to an existing `.md` path |
| Resource limits defined | 1.0 | `max_terminals` or equivalent concurrency cap is present |
| Error recovery documented | 1.0 | `on_failure` field describes retry or skip behavior |
| Wave ordering for grid mode | 1.0 | Grid and continuous configs include `wave_order` or explicit dependency list |
| Spawn delay documented | 0.5 | `spawn_delay_ms` is defined when mode is `grid` or `continuous` |
| No task instructions in body | 1.0 | Config contains parameters only; no prose task instructions |
Sum of weights: 9.0. `soft_score = sum(weight * gate_score) / 9.0 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference spawn config |
| >= 8.0 | PUBLISH — safe for production agent_group dispatch |
| >= 7.0 | REVIEW — usable but missing safety or recovery detail |
| < 7.0 | REJECT — do not execute; incomplete or unsafe config |
## Bypass
| Field | Value |
|-------|-------|
| condition | Emergency agent_group launch during active incident where config cannot be revised before deploy |
| approver | Lead engineer on duty (human, not automated) |
| audit_log | Entry required in `.claude/bypasses/spawn_config_{date}.md` with written justification |
| expiry | 24 hours; config must reach PUBLISH score before next planned launch |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.

## Examples

# Examples: spawn-config-builder
## Golden Example
INPUT: "Create spawn config for research_agent solo research task"
OUTPUT:
```yaml
id: p12_spawn_shaka_solo_research
kind: spawn_config
pillar: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
title: "research_agent Solo Research Spawn"
mode: solo
director: "shaka"
model: "sonnet"
flags:
  - "--dangerously-skip-permissions"
  - "--no-chrome"
  - "-p"
mcp_config: ".mcp-shaka.json"
timeout: 1800
interactive: true
prompt_strategy: handoff
domain: "research"
quality: 8.8
tags: [spawn_config, shaka, solo, research]
tldr: "Solo spawn for research_agent research with sonnet, 30min timeout, handoff-based prompt"
```
## Spawn Command
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File records/framework/powershell/spawn_solo.ps1 -sat shaka -task "Leia .claude/handoffs/RESEARCH_shaka.md e execute. Commit ANTES de parar." -interactive
```
## Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| mode | solo | Single director, single task |
| director | shaka | Research domain director |
| model | sonnet | research_agent uses sonnet per routing table |
| timeout | 1800s | 30min sufficient for research tasks |
| interactive | true | Terminal stays open for monitoring |
## Constraints
- Handoff file must exist before spawn
- Max inline prompt: 200 chars (use handoff for longer tasks)
- research_agent requires firecrawl + brain MCP servers
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p12_spawn_ pattern (H02 pass)
- kind: spawn_config (H04 pass)
- 19 required fields present (H06 pass)
- body has Spawn Command + Parameters + Constraints (H07 pass)
- mode: solo is valid enum (H08 pass)
- flags include baseline set (S03 pass)
- timeout is reasonable for task type (S05 pass)
- No task instructions in config (S07 pass)
- No filler phrases (S08 pass)
## Anti-Example
INPUT: "Create spawn config for a director"
BAD OUTPUT:
```yaml
id: spawn_config
kind: config
director: research_agent
quality: 8.0
```
Spawn the research_agent director to do research. It should use the sonnet model and
have access to firecrawl. Make sure it commits before stopping.
FAILURES:
1. id: no `p12_spawn_` prefix -> H02 FAIL
2. kind: "config" not "spawn_config" -> H04 FAIL
3. pillar: missing -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, mode, model, flags, timeout, domain, tags, tldr -> H06 FAIL
6. No ## Spawn Command section -> H07 FAIL
7. Body contains task instructions ("do research") -> S07 FAIL
8. No flags listed -> S03 FAIL
9. director uppercase "research_agent" (should be lowercase) -> S04 FAIL
10. Body is prose, not structured sections -> S08 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
