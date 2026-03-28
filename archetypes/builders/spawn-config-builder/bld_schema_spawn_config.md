---
kind: schema
id: bld_schema_spawn_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for spawn_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: spawn_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p12_spawn_{mode_slug}) | YES | - | Namespace compliance |
| kind | literal "spawn_config" | YES | - | Type integrity |
| pillar | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable config name |
| mode | enum: solo, grid, continuous | YES | - | Spawn mode |
| satellite | string or list[string] | YES | - | Target satellite(s) |
| model | string | YES | - | LLM model (opus, sonnet, haiku) |
| flags | list[string] | YES | - | CLI flags for claude command |
| mcp_config | string | REC | - | Path to .mcp-{sat}.json |
| timeout | integer | YES | - | Timeout in seconds |
| interactive | boolean | REC | true | Whether terminal stays open |
| prompt_strategy | enum: inline, handoff | REC | "handoff" | How task is passed |
| domain | string | YES | - | Domain this config serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "spawn_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
## ID Pattern
Regex: `^p12_spawn_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Spawn Command` — the actual PowerShell/CLI command to execute
2. `## Parameters` — detailed parameter descriptions and rationale
3. `## Constraints` — limitations, requirements, and safety notes
## Constraints
- max_bytes: 3072 (body only)
- naming: p12_spawn_{mode_slug}.yaml
- machine_format: yaml
- id == filename stem
- mode MUST be one of: solo, grid, continuous
- flags SHOULD include runtime-required permission and safety flags
- prompt_strategy: use "handoff" when task description > 200 chars
- quality: null always
