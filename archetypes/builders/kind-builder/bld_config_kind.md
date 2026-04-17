---
kind: config
id: bld_config_kind
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for builder packages
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 40
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: "python _tools/cex_doctor.py --scope archetypes/builders/{kind}-builder/"
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Kind Builder"
version: "1.0.0"
author: n03_builder
tags: [kind_builder, builder, config, meta-builder]
tldr: "Builder package config: naming patterns, file paths, size limits, model defaults, quality targets."
domain: "kind builder construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Config: kind_builder Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Builder directory | {kind}-builder/ (kebab-case) | env-config-builder/, kind-builder/ |
| ISO files | bld_{iso_type}_{kind}.md (snake_case) | bld_manifest_env_config.md |
| Sub-agent file | {kind}-builder.md (kebab-case) | env-config-builder.md |
| Frontmatter id (manifest) | {kind}-builder | env-config-builder |
| Frontmatter id (other ISOs) | bld_{iso_type}_{kind} | bld_schema_env_config |

Rule: hyphens in directory/sub-agent names, underscores in file names and frontmatter ids.

## File Paths

| Output | Path |
|--------|------|
| Builder ISOs | archetypes/builders/{kind}-builder/bld_*.md |
| Sub-agent definition | .claude/agents/{kind}-builder.md |
| Compiled output | (ISOs are not compiled to a separate location) |

## Size Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Single ISO body | max 5120 bytes | Keeps prompt injection under budget |
| Total package (13 ISOs) | max 66560 bytes (13 x 5120) | Practical upper bound |
| Manifest body | max 3072 bytes | Identity should be concise |
| Schema body | max 4096 bytes | Field tables can be dense |
| System prompt body | max 4096 bytes | Rules need room |
| Examples body | max 5120 bytes | Golden + anti need full space |
| Density floor | >= 0.85 | No filler content |

## Model Defaults

| Setting | Value | Notes |
|---------|-------|-------|
| Default model for sub-agents | sonnet | Cost-efficient for artifact production |
| Quality target | 9.0 | Floor for all ISOs and produced artifacts |
| Max retries on quality failure | 2 | Return to F6, retry F7 |
| quality field | null always | Never self-score in any ISO |

## ISO Type Registry

The 13 ISO types are fixed. kind-builder must produce exactly these:

| ISO type | Frontmatter kind | Frontmatter pillar |
|----------|------------------|-------------------|
| manifest | type_builder | P08 |
| schema | schema | P06 |
| system_prompt | system_prompt | P03 |
| instruction | instruction | P03 |
| output_template | output_template | P05 |
| examples | examples | P07 |
| memory | learning_record | P10 |
| tools | tools | P04 |
| quality_gate | quality_gate | P11 |
| knowledge_card | knowledge_card | P01 |
| architecture | architecture | P08 |
| collaboration | collaboration | P12 |
| config | config | P09 |

## Runtime Constraints

| Constraint | Value |
|------------|-------|
| Parallel ISO production | Allowed (ISOs are independent files) |
| Reference builder required | YES (at least one existing builder must be read) |
| kinds_meta.json required | YES (target kind must exist in registry) |
| ASCII-only enforcement | YES (all ISOs, no emoji, no smart quotes) |
| Overwrite protection | Do not overwrite existing ISOs without explicit request |

## Metadata

```yaml
id: bld_config_kind
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_config_kind.md
```
