---
kind: schema
id: bld_schema_boot_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for boot_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Boot Config"
version: "1.0.0"
author: n03_builder
tags: [boot_config, builder, examples]
tldr: "Golden and anti-examples for boot config construction, demonstrating ideal structure and common pitfalls."
domain: "boot config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_agent_card
  - bld_schema_constraint_spec
  - bld_schema_input_schema
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_spawn_config
  - bld_schema_output_validator
  - bld_schema_unit_eval
  - bld_schema_memory_scope
  - bld_schema_smoke_eval
---

# Schema: boot_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_boot_{provider_slug}) | YES | - | Namespace compliance |
| kind | literal "boot_config" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Semantic versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| provider | string | YES | - | Target provider runtime |
| identity | object | YES | - | Agent identity block (name, role, agent_group) |
| constraints | object | YES | - | Operational limits (tokens, timeout, retries) |
| tools | list[string] | YES | - | Available tools/MCPs for this provider |
| domain | string | YES | - | Config scope domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "boot-config" |
| tldr | string <= 160ch | YES | - | Dense one-liner |
| model | string | REC | - | Default LLM model identifier |
| temperature | float 0.0-2.0 | REC | - | Default temperature setting |
| flags | list[string] | REC | - | CLI/runtime flags |
| mcp_config | object | REC | - | MCP server references |
| permissions | object | REC | - | Read/write/execute permissions |
| system_prompt_ref | string | REC | - | Reference to system_prompt artifact |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## Identity Object
```yaml
identity:
  name: string        # Agent display name
  role: string        # Primary role description
  agent_group: string   # Owning agent_group or "agnostic"
```
## Constraints Object
```yaml
constraints:
  max_tokens: integer       # Output token limit
  context_window: integer   # Available context window
  timeout_seconds: integer  # Max execution time
  max_retries: integer      # Retry count on failure
  temperature: float        # Override if set
```
## ID Pattern
Regex: `^p02_boot_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Provider Overview` — which provider, runtime environment, version
2. `## Identity Block` — agent name, role, agent_group assignment
3. `## Constraints` — table of operational limits
4. `## Tools Configuration` — MCP servers, CLI tools, available APIs
5. `## Flags` — CLI/runtime flags with purpose
6. `## References` — provider docs, related boot_configs
## Constraints
- max_bytes: 2048 (body only)
- naming: p02_boot_{provider_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- provider: required, descriptive (not abbreviated)
- llm_function: GOVERN (boot_config governs initialization)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_agent_card]] | sibling | 0.66 |
| [[bld_schema_constraint_spec]] | sibling | 0.61 |
| [[bld_schema_input_schema]] | sibling | 0.61 |
| [[bld_schema_retriever_config]] | sibling | 0.61 |
| [[bld_schema_handoff_protocol]] | sibling | 0.60 |
| [[bld_schema_spawn_config]] | sibling | 0.60 |
| [[bld_schema_output_validator]] | sibling | 0.60 |
| [[bld_schema_unit_eval]] | sibling | 0.60 |
| [[bld_schema_memory_scope]] | sibling | 0.60 |
| [[bld_schema_smoke_eval]] | sibling | 0.60 |
