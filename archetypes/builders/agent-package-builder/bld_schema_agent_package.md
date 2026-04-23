---
kind: schema
id: bld_schema_agent_package
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for agent_package
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Agent Package"
version: "1.0.0"
author: n03_builder
tags: [agent_package, builder, examples]
tldr: "Golden and anti-examples for agent package construction, demonstrating ideal structure and common pitfalls."
domain: "agent package construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_agent_package
  - bld_schema_kind
  - bld_config_agent_package
  - bld_schema_golden_test
  - bld_schema_scoring_rubric
  - bld_schema_unit_eval
  - bld_schema_runtime_state
  - bld_schema_agent
  - bld_schema_input_schema
  - bld_schema_handoff_protocol
---

# Schema: agent_package
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_iso_{agent_slug}) | YES | - | Namespace compliance |
| kind | literal "agent_package" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Semantic versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| agent_name | string | YES | - | Target agent this package represents |
| tier | enum [minimal, standard, complete, whitelabel] | YES | "standard" | Package completeness level |
| files_count | integer | YES | - | Actual file count in directory |
| domain | string | YES | - | Agent primary domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "agent-package" |
| tldr | string <= 160ch | YES | - | Dense one-liner |
| portable | boolean | REC | true | No hardcoded paths in any file |
| llm_function | literal "BECOME" | REC | "BECOME" | Package carries agent identity |
| lp_mapping | object | REC | - | File-to-pillar mapping |
| system_instruction_tokens | integer | REC | - | Token count of system_instruction.md |
| density_score | float 0.80-1.00 | OPT | - | Content density across all files |
## Tier System
| Tier | Min Files | Required Contents |
|------|-----------|-------------------|
| minimal | 3 | manifest.yaml, system_instruction.md, instructions.md |
| standard | 7 | minimal + architecture.md, output_template.md, examples.md, error_handling.md |
| complete | 10 | standard + quick_start.md, input_schema.yaml, upload_kit.md |
| whitelabel | 12 | complete + upload_kit_whitelabel.md, branding_config.yaml |
## LP Mapping (file to pillar)
| File | Pillar | Purpose |
|------|--------|---------|
| manifest.yaml | P02 | Package identity and inventory |
| system_instruction.md | P03 | Full system prompt for LLM injection |
| instructions.md | P03 | Step-by-step execution protocol |
| architecture.md | P08 | Boundary, position, dependency graph |
| output_template.md | P05 | Template with `{{vars}}` for agent output |
| examples.md | P07 | Golden + anti-examples (min 2) |
| error_handling.md | P11 | Failure modes and remediation |
| quick_start.md | P01 | 5-minute onboarding guide |
| input_schema.yaml | P06 | Input contract definition |
| upload_kit.md | P04 | Deployment and loading instructions |
## ID Pattern
Regex: `^p02_iso_[a-z][a-z0-9_]+$`
Rule: id MUST equal directory name with p02_iso_ prefix.
## Body Structure (required sections in manifest.yaml)
1. `## Agent Identity` — who the packaged agent is, one paragraph
2. `## File Inventory` — table of all files with pillar, tier requirement, status
3. `## Tier Compliance` — declared tier, files present vs expected, gaps
4. `## Portability Notes` — platform dependencies, no hardcoded paths check
5. `## References` — source agent definition, upstream builders
## Constraints
- max_bytes: 4096 (manifest.yaml body only)
- per_file_max: 4096 bytes (each file in the package)
- system_instruction_tokens: max 4096
- min_examples: 2 (in examples.md)
- density: >= 0.80 across all files
- no_hardcoded_paths: true (no /home/, /Users/, C:\, records/)
- id == directory name prefix
- files_count MUST match actual file count
- tier MUST match actual file count thresholds

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_agent_package]] | upstream | 0.54 |
| [[bld_schema_kind]] | sibling | 0.48 |
| [[bld_config_agent_package]] | downstream | 0.48 |
| [[bld_schema_golden_test]] | sibling | 0.47 |
| [[bld_schema_scoring_rubric]] | sibling | 0.47 |
| [[bld_schema_unit_eval]] | sibling | 0.47 |
| [[bld_schema_runtime_state]] | sibling | 0.47 |
| [[bld_schema_agent]] | sibling | 0.46 |
| [[bld_schema_input_schema]] | sibling | 0.46 |
| [[bld_schema_handoff_protocol]] | sibling | 0.46 |
