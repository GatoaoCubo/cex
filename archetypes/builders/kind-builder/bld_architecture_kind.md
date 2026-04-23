---
kind: architecture
id: bld_architecture_kind
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of kind-builder -- how builders fit in the CEX architecture
quality: 9.1
title: "Architecture Kind Builder"
version: "1.0.0"
author: n03_builder
tags: [kind_builder, builder, architecture, meta-builder]
tldr: "Builder architecture: directory structure, loader discovery, nucleus routing, 13-ISO component map."
domain: "kind builder construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - kind-builder
  - bld_collaboration_kind
  - bld_instruction_kind
  - bld_schema_kind
  - p03_sp_kind_builder
  - bld_tools_kind
  - bld_knowledge_card_kind
  - bld_config_kind
  - bld_output_template_builder
  - p10_lr_kind_builder
---
# Architecture: kind-builder

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| kinds_meta.json | Kind registry -- pillar, naming, max_bytes, llm_function per kind | .cex/ | required |
| builder directory | 13-ISO package at archetypes/builders/{kind}-builder/ | archetypes/ | required |
| manifest ISO | Builder identity, capabilities, routing keywords | kind-builder | required |
| schema ISO | Formal schema: fields, body sections, constraints | kind-builder | required |
| system_prompt ISO | Persona, rules, knowledge boundary | kind-builder | required |
| instruction ISO | Step-by-step production process | kind-builder | required |
| output_template ISO | Template with `{{vars}}` for artifact generation | kind-builder | required |
| examples ISO | Golden + anti examples for calibration | kind-builder | required |
| memory ISO | Patterns learned, anti-patterns, evidence | kind-builder | required |
| tools ISO | Available tools and data sources | kind-builder | required |
| quality_gate ISO | HARD gates + SOFT scoring dimensions | kind-builder | required |
| knowledge_card ISO | Domain knowledge, industry patterns | kind-builder | required |
| architecture ISO | Components, dependencies, boundaries | kind-builder | required |
| collaboration ISO | Crews, handoffs, builder dependencies | kind-builder | required |
| config ISO | Naming, paths, size limits | kind-builder | required |
| sub-agent file | .claude/agents/{kind}-builder.md dispatch definition | kind-builder | required |
| _shared ISOs | Cross-builder shared skills (GDP, 8F, etc.) | archetypes/builders/_shared/ | optional |

## Dependency Graph

```
kinds_meta.json --feeds--> kind-builder (reads target kind metadata)
pillar_schema --feeds--> kind-builder (reads P{xx}/_schema.yaml for field defs)
kc_{kind}.md --feeds--> kind-builder (reads domain knowledge if available)
reference_builder --feeds--> kind-builder (structural template from existing builder)

kind-builder --produces--> {kind}-builder/ (13 ISOs)
kind-builder --produces--> .claude/agents/{kind}-builder.md (sub-agent)

{kind}-builder/ --loaded_by--> cex_skill_loader.py (at prompt composition time)
{kind}-builder/ --validated_by--> cex_doctor.py (health checks)
{kind}-builder/ --scored_by--> cex_score.py (quality assessment)
{kind}-builder/ --compiled_by--> cex_compile.py (structural validation)

.claude/agents/{kind}-builder.md --used_by--> N07 dispatch (nucleus routing)
.claude/P02_model/{kind}-builder.md --used_by--> _spawn/dispatch.sh (process spawning)
```

| From | To | Type | Data |
|------|----|------|------|
| kinds_meta.json | kind-builder | feeds | pillar, naming, max_bytes, llm_function, boundary |
| pillar schema | kind-builder | feeds | field definitions, sibling kinds |
| kc_{kind}.md | kind-builder | feeds | domain knowledge, industry patterns |
| reference builder | kind-builder | feeds | structural template (13 ISO format) |
| kind-builder | {kind}-builder/ | produces | 13 ISO files with kind-specific content |
| kind-builder | .claude/agents/ | produces | sub-agent definition for dispatch |
| {kind}-builder/ | cex_skill_loader | consumed_by | prompt composition at F3 |
| {kind}-builder/ | cex_doctor | validated_by | health check at F7 |

## Boundary Table

| kind-builder IS | kind-builder IS NOT |
|----------------|---------------------|
| A meta-builder that scaffolds builder directories | A builder that produces artifacts of any specific kind |
| Produces 13 ISO files + 1 sub-agent file per run | A registry editor (does not modify kinds_meta.json) |
| Reads kinds_meta.json for metadata input | A deployment tool (does not deploy or activate builders) |
| Uses an existing builder as structural reference | An artifact validator (cex_doctor handles validation) |
| Fills ISOs with kind-specific domain knowledge | A generic template stamper (content must be domain-specific) |
| Creates the .claude/agents/ sub-agent definition | A nucleus (kind-builder is a builder, not a nucleus) |
| Validates its own output (13-file completeness check) | A quality scorer (cex_score handles scoring) |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Registry | kinds_meta.json | Kind metadata source of truth |
| Archetype | archetypes/builders/ | Builder package storage |
| Discovery | cex_skill_loader.py | Runtime builder loading |
| Dispatch | .claude/agents/ | Sub-agent routing |
| Validation | cex_doctor.py, cex_score.py | Health and quality checks |
| Compilation | cex_compile.py | Structural validation |

## Directory Structure

```
archetypes/
  builders/
    _shared/                    # Cross-builder shared ISOs
      skill_guided_decisions.md
      skill_8f_pipeline.md
      ...
    env-config-builder/         # Example: 13 ISOs for env_config
      bld_manifest_env_config.md
      bld_schema_env_config.md
      ...
    kind-builder/               # THIS builder (meta)
      bld_manifest_kind.md
      bld_schema_kind.md
      ...
    {new-kind}-builder/         # Output of kind-builder
      bld_manifest_{kind}.md
      bld_schema_{kind}.md
      ... (13 files total)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kind-builder]] | related | 0.57 |
| [[bld_collaboration_kind]] | downstream | 0.48 |
| [[bld_instruction_kind]] | upstream | 0.43 |
| [[bld_schema_kind]] | upstream | 0.38 |
| [[p03_sp_kind_builder]] | upstream | 0.36 |
| [[bld_tools_kind]] | upstream | 0.36 |
| [[bld_knowledge_card_kind]] | upstream | 0.36 |
| [[bld_config_kind]] | downstream | 0.35 |
| [[bld_output_template_builder]] | upstream | 0.32 |
| [[p10_lr_kind_builder]] | downstream | 0.32 |
