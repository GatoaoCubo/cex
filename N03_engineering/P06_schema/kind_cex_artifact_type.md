---
id: p06_kind_cex_artifact_type
kind: type_def
8f: F1_constrain
pillar: P06
title: "Kind: The Atomic Artifact Type in CEX"
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n03_engineering
quality: 8.7
tags: [kind, type_def, taxonomy, meta, P06, architecture, schema]
tldr: "Meta-definition of 'kind': the atomic artifact type in CEX. 293 kinds, 12 pillars, 1 builder per kind, 13 ISOs per builder."
density_score: 0.92
related:
  - bld_schema_kind
  - bld_architecture_kind
  - bld_instruction_kind
  - bld_output_template_builder
  - bld_knowledge_card_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_examples_glossary_entry
  - p03_sp_kind_builder
  - bld_config_kind
---

## Definition

A **kind** is the atomic unit of CEX's typed knowledge system. Every artifact produced by any nucleus has exactly one kind. The kind determines the artifact's schema (required frontmatter fields, body structure), its pillar assignment (P01-P12), its builder (13 ISOs that teach an LLM how to produce it), and its quality gates (HARD pass/fail checks + SOFT scoring dimensions).

A kind is to CEX what a class is to object-oriented programming: it defines structure, behavior, and constraints. An artifact is an instance of a kind. A builder is the factory that produces instances.

## The Kind Registry

Source of truth: `.cex/kinds_meta.json` (293 entries as of 2026-04-19).

Each entry in the registry contains:

| Field | Type | Description |
|-------|------|-------------|
| description | string | What this kind produces (1-2 sentences) |
| pillar | string | P01-P12 assignment |
| naming | string | File naming pattern (e.g., `p01_kc_{slug}.md`) |
| max_bytes | int | Maximum body size in bytes |
| llm_function | string | Primary 8F function: CONSTRAIN, BECOME, INJECT, REASON, CALL, PRODUCE, GOVERN, COLLABORATE |
| core | bool | Whether this kind is part of the CEX core (vs. domain-specific) |
| boundary | string | What this kind IS and IS NOT (disambiguation from similar kinds) |
| deprecated_by | string or null | If deprecated, which kind replaces it |

## Kind-Pillar Relationship

Every kind belongs to exactly one pillar. Pillars group kinds by domain:

| Pillar | Domain | Example Kinds | Kind Count |
|--------|--------|--------------|------------|
| P01 | Knowledge | knowledge_card, chunk_strategy, embedding_config, rag_source | ~25 |
| P02 | Model | agent, model_provider, boot_config, fallback_chain, personality | ~20 |
| P03 | Prompt | prompt_template, system_prompt, chain, context_file, tagline | ~25 |
| P04 | Tools | cli_tool, browser_tool, mcp_server, event_stream, webhook | ~20 |
| P05 | Output | landing_page, output_template, formatter, parser | ~15 |
| P06 | Schema | schema, type_def, input_schema, validation_schema, interface | ~20 |
| P07 | Evaluation | quality_gate, scoring_rubric, benchmark, llm_judge | ~15 |
| P08 | Architecture | agent_card, component_map, context_map, decision_record, diagram | ~25 |
| P09 | Config | env_config, rate_limit_config, secret_config, feature_flag | ~20 |
| P10 | Memory | entity_memory, knowledge_index, memory_summary, prompt_cache | ~20 |
| P11 | Feedback | constitutional_rule, guardrail, bugloop, learning_record | ~25 |
| P12 | Orchestration | workflow, crew_template, schedule, dispatch_rule, pipeline_template | ~25 |

## Kind-Builder Relationship

Every kind has exactly one builder. A builder is a directory of 13 ISOs (Isolated Specification Objects) at `archetypes/builders/{kind}-builder/`:

| ISO | File Pattern | 8F Function | Purpose |
|-----|-------------|-------------|---------|
| Manifest | bld_manifest_{kind}.md | BECOME | Builder identity, capabilities, routing |
| Schema | bld_schema_{kind}.md | CONSTRAIN | Formal schema (source of truth) |
| System Prompt | bld_system_prompt_{kind}.md | BECOME | Agent persona and rules |
| Instruction | bld_instruction_{kind}.md | REASON | Step-by-step production process |
| Output Template | bld_output_template_{kind}.md | PRODUCE | Fill-in template with {{vars}} |
| Examples | bld_examples_{kind}.md | GOVERN | Golden + anti-example for few-shot |
| Memory | bld_memory_{kind}.md | INJECT | Learned patterns and anti-patterns |
| Tools | bld_tools_{kind}.md | CALL | Available tools and data sources |
| Quality Gate | bld_quality_gate_{kind}.md | GOVERN | HARD gates + SOFT scoring |
| Knowledge Card | bld_knowledge_card_{kind}.md | INJECT | Domain knowledge and references |
| Architecture | bld_architecture_{kind}.md | GOVERN | Component map and boundaries |
| Collaboration | bld_collaboration_{kind}.md | COLLABORATE | Crew roles and handoff protocol |
| Config | bld_config_{kind}.md | CONSTRAIN | Naming, paths, size limits |

The builder-kind relationship is 1:1. No builder produces multiple kinds. No kind is produced by multiple builders.

## Kind Lifecycle

```
1. DEFINE    kinds_meta.json entry (pillar, boundary, naming, max_bytes)
2. BUILD     13 ISOs at archetypes/builders/{kind}-builder/
3. REGISTER  .claude/agents/{kind}-builder.md (sub-agent for dispatch)
4. DOCUMENT  N00_genesis/P01_knowledge/library/kind/kc_{kind}.md
5. PRODUCE   Nucleus uses builder to create artifact instances
6. COMPILE   cex_compile.py converts .md to .yaml
7. INDEX     cex_retriever.py indexes for TF-IDF search
8. DEPRECATE kinds_meta.json deprecated_by field (never delete)
```

## Kind Properties (Invariants)

| Property | Invariant | Enforcement |
|----------|-----------|-------------|
| Unique ID | No two kinds share the same name in kinds_meta.json | cex_doctor.py |
| Single pillar | Each kind belongs to exactly one pillar | kinds_meta.json schema |
| Single builder | Each kind has exactly one builder directory | Builder naming convention |
| Frontmatter contract | Every instance must have: id, kind, pillar, version, quality, tags | Pre-commit hook |
| Naming pattern | Artifact filename matches the kind's naming field | cex_hooks.py |
| Size limit | Artifact body does not exceed max_bytes | Quality gate check |
| Boundary clarity | boundary field distinguishes from similar kinds | Builder manifest |

## Kind vs. Adjacent Concepts

| Concept | What It Is | Relationship to Kind |
|---------|-----------|---------------------|
| Pillar | Domain grouping (P01-P12) | A kind belongs to one pillar |
| Builder | 13-ISO factory for a kind | A kind has one builder |
| Artifact | Instance of a kind | An artifact IS-A kind |
| Schema | Formal field specification | A kind's schema defines its structure |
| Sub-agent | LLM agent configured with builder ISOs | A sub-agent produces instances of one kind |
| KC (Knowledge Card) | Domain knowledge document | Each kind has a KC documenting its use |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|-------------|-----------------|
| Creating artifact without a kind | Untyped output has no schema, no quality gate, no builder | Register the kind in kinds_meta.json first |
| One kind for multiple purposes | Violates boundary clarity; quality gates cannot be specific | Split into distinct kinds with clear boundaries |
| Compound kind names | "agent_workflow_config" conflates agent + workflow + config | Use the most specific single kind |
| Skipping the KC | Builder exists but no knowledge card; LLM lacks domain context | Write kc_{kind}.md before first production use |
| Deprecating by deletion | Breaks references in existing artifacts | Set deprecated_by in kinds_meta.json |
| Reusing another kind's builder | Produces artifacts that don't match the builder's quality gates | Create a new builder for the new kind |

## The 293-Kind Taxonomy (Summary Statistics)

| Metric | Value |
|--------|-------|
| Total kinds | 293 |
| Total builders | 295 (includes meta-builders) |
| Total ISOs | 3,835 (295 builders x 13 ISOs) |
| Core kinds | ~85 (core: true in kinds_meta.json) |
| Domain-specific kinds | ~208 |
| Deprecated kinds | 0 (no deprecations yet) |
| Pillars | 12 (P01-P12) |
| Avg kinds per pillar | ~24.4 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_kind]] | related | 0.49 |
| [[bld_architecture_kind]] | downstream | 0.49 |
| [[bld_instruction_kind]] | upstream | 0.45 |
| [[bld_output_template_builder]] | upstream | 0.37 |
| [[bld_knowledge_card_kind]] | upstream | 0.37 |
| [[kind-builder]] | downstream | 0.37 |
| [[bld_collaboration_kind]] | downstream | 0.33 |
| [[bld_examples_glossary_entry]] | downstream | 0.31 |
| [[p03_sp_kind_builder]] | upstream | 0.30 |
| [[bld_config_kind]] | downstream | 0.29 |
