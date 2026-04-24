---
kind: schema
id: bld_schema_kind
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for a builder package (13 ISOs)
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Kind Builder"
version: "1.0.0"
author: n03_builder
tags: [kind_builder, builder, schema, iso, architecture]
tldr: "Schema for builder packages: 13 ISO files per kind, naming patterns, required frontmatter, directory structure."
domain: "kind builder construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_architecture_kind
  - bld_instruction_kind
  - bld_config_kind
  - kind-builder
  - bld_schema_reranker_config
  - bld_schema_thinking_config
  - bld_schema_search_strategy
  - bld_schema_prompt_compiler
  - bld_schema_pitch_deck
  - bld_schema_usage_report
---

# Schema: kind_builder

## Builder Package Structure

A complete builder package is a directory at `archetypes/builders/{kind}-builder/`
containing exactly 13 files. Each file is one ISO (Isolated Specification Object).

## The 13 ISO Files

| # | File Pattern | Kind | Pillar | llm_function | Purpose |
|---|-------------|------|--------|--------------|---------|
| 1 | bld_manifest_{kind}.md | type_builder | P08 | PRODUCE | Identity, capabilities, routing, crew role |
| 2 | bld_schema_{kind}.md | schema | P06 | CONSTRAIN | Formal schema: frontmatter fields, body sections, constraints |
| 3 | bld_system_prompt_{kind}.md | system_prompt | P03 | PRODUCE | Persona, rules, behavioral constraints for the builder agent |
| 4 | bld_instruction_{kind}.md | instruction | P03 | REASON | Step-by-step production process (research, compose, validate) |
| 5 | bld_output_template_{kind}.md | output_template | P05 | PRODUCE | Template with `{{vars}}` the LLM fills to produce the artifact |
| 6 | bld_examples_{kind}.md | examples | P07 | GOVERN | Golden example + anti-example for few-shot learning |
| 7 | bld_memory_{kind}.md | learning_record | P10 | INJECT | Patterns learned, anti-patterns observed, confidence scores |
| 8 | bld_tools_{kind}.md | tools | P04 | CALL | Tools and data sources available during production |
| 9 | bld_quality_gate_{kind}.md | quality_gate | P11 | GOVERN | HARD gates (pass/fail) + SOFT scoring dimensions |
| 10 | bld_knowledge_card_{kind}.md | knowledge_card | P01 | INJECT | Domain knowledge, industry patterns, references |
| 11 | bld_architecture_{kind}.md | architecture | P08 | GOVERN | Component map, dependency graph, boundary table |
| 12 | bld_collaboration_{kind}.md | collaboration | P12 | COLLABORATE | Crew compositions, handoff protocol, builder dependencies |
| 13 | bld_config_{kind}.md | config | P09 | CONSTRAIN | Naming conventions, file paths, size limits, runtime config |

## Required Frontmatter (all 13 ISOs)

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string | YES | Unique identifier for this ISO |
| kind | string | YES | The ISO's own kind (schema, instruction, etc.) |
| 8f | string | REC | 8F pipeline stage from kind_8f_mapping.yaml (e.g. F3_inject) |
| pillar | string | YES | The ISO's own pillar assignment |
| llm_function | string | YES | Which 8F function this ISO serves |
| version | semver | YES | Always starts at 1.0.0 |
| created | date | YES | YYYY-MM-DD |
| updated | date | YES | YYYY-MM-DD |
| author | string | YES | Producer identity |
| quality | null | YES | NEVER self-score |
| title | string | YES | Human-readable title |
| tags | list | YES | Minimum 3 tags, must include target kind name |
| tldr | string | YES | Dense summary, max 160 characters |
| domain | string | YES | Target kind's domain |
| density_score | float | REC | Target >= 0.85 |

## Sub-Agent File

In addition to the 13 ISOs, a builder package requires:
- `.claude/agents/{kind}-builder.md` -- sub-agent definition for dispatch

## Constraints

- Directory name: `{kind}-builder/` (kebab-case, kind uses underscores replaced by hyphens)
- File names: `bld_{iso_type}_{kind}.md` (snake_case throughout)
- All files: Markdown with YAML frontmatter
- quality: null in ALL files (never self-score)
- Body content: kind-specific, not generic filler
- ASCII-only in all files (no emoji, no smart quotes, no accented characters)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.52 |
| [[bld_instruction_kind]] | upstream | 0.49 |
| [[bld_config_kind]] | downstream | 0.43 |
| [[kind-builder]] | downstream | 0.41 |
| [[bld_schema_reranker_config]] | sibling | 0.40 |
| [[bld_schema_thinking_config]] | sibling | 0.40 |
| [[bld_schema_search_strategy]] | sibling | 0.39 |
| [[bld_schema_prompt_compiler]] | sibling | 0.39 |
| [[bld_schema_pitch_deck]] | sibling | 0.39 |
| [[bld_schema_usage_report]] | sibling | 0.39 |
