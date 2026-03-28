---
kind: knowledge_card
id: bld_knowledge_card_spawn_config
pillar: P12
llm_function: INJECT
purpose: Domain knowledge for spawn_config production — atomic searchable facts
sources: spawn-config-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: spawn_config

## Executive Summary

Spawn configs are YAML artifacts that define exactly how a satellite agent is launched — CLI flags, model, timeout, MCP profile, and prompt delivery strategy. They encode the spawn contract so the same satellite can be reliably re-launched without manual CLI assembly. Unlike signals (runtime status) or dispatch_rules (routing policy), spawn configs are static pre-launch recipes that exist before the satellite process starts.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P12 (orchestration) |
| Format | YAML |
| Naming | `p12_spawn_{mode_slug}.yaml` |
| ID regex | `^p12_spawn_[a-z][a-z0-9_]+$` |
| Max body bytes | 3072 |
| Required frontmatter fields | 19 |
| Recommended frontmatter fields | 4: mcp_config, interactive, prompt_strategy, domain |
| mode enum | `solo` / `grid` / `continuous` |
| model values | `opus`, `sonnet`, `haiku` |
| prompt_strategy enum | `inline` (< 200 chars) / `handoff` (longer tasks) |
| quality field | null always — invariant |
| tldr max | 160 characters |

## Patterns

| Pattern | Rule |
|---------|------|
| Mode selection | solo = 1 satellite 1 task; grid = parallel fixed set; continuous = queue-refill loop |
| prompt_strategy | Use `handoff` when task > 200 chars; `inline` only for short commands |
| flags list | Include all runtime-required permission and safety flags |
| mcp_config | Reference `.mcp-{sat}.json`; omit only for satellites with no MCP tools |
| Model pairing | Match satellite to correct model: opus = build/execute, sonnet = research/marketing |
| interactive | `true` = terminal stays open for monitoring; `false` = fire-and-forget |
| id == filename stem | `p12_spawn_solo_edison.yaml` → `id: p12_spawn_solo_edison` |
| Timeout budgeting | research ~30 min, build ~45 min, deploy ~15 min |

- **Body sections**: Spawn Command → Parameters → Constraints
- **Spawn Command**: exact PowerShell/CLI command — not pseudocode
- **Grid max**: 3 satellites concurrent to prevent system instability

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Inline prompt > 200 chars with `-p` flag | Long inline prompts hang non-interactive spawn |
| Missing required permission flags | Satellite blocked by permission prompts mid-execution |
| Wrong model for satellite domain | Performance mismatch; sonnet for build tasks under-delivers |
| Omitting `timeout` | Runaway satellite consumes resources indefinitely |
| `mode: continuous` without queue refill logic | Slots go idle after first wave |
| Hardcoded absolute paths in mcp_config | Breaks portability across machines |
| Complex task with `prompt_strategy: inline` | Satellite receives insufficient context |

## Application

1. Choose mode: `solo` (one satellite), `grid` (parallel fixed), or `continuous` (queue-driven)
2. Identify target satellite and its correct model pairing
3. Determine `prompt_strategy`: if task > 200 chars, write handoff file first and set `handoff`
4. Assemble `flags` list with all required CLI flags
5. Set `mcp_config` path if satellite uses MCP tools
6. Set `timeout` based on expected task duration
7. Write body: Spawn Command (exact CLI) → Parameters → Constraints
8. Set `quality: null`, verify body ≤ 3072 bytes

## References

- Schema: spawn_config SCHEMA.md (P06)
- Pillar: P12 (orchestration)
- Boundary: signal (runtime status), dispatch_rule (routing policy), handoff (task instructions)
