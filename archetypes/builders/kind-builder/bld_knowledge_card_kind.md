---
kind: knowledge_card
id: bld_knowledge_card_kind
pillar: P01
llm_function: INJECT
purpose: Domain knowledge about the CEX builder architecture -- the 13-ISO pattern
sources: CEX architecture, convention-over-configuration (Rails), archetype pattern (GoF)
quality: 9.2
title: "Knowledge Card Kind Builder"
version: "1.0.0"
author: n03_builder
tags: [kind_builder, builder, knowledge_card, meta-builder, architecture]
tldr: "CEX builder architecture: 13 ISOs per kind, pillar mapping, 8F integration, loader discovery."
domain: "kind builder construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Domain Knowledge: kind_builder

## Executive Summary

The CEX builder architecture uses a convention-over-configuration pattern where every
kind has a dedicated builder directory containing exactly 13 Isolated Specification
Objects (ISOs). Each ISO serves a specific function in the 8F pipeline. At runtime,
cex_skill_loader.py discovers builders by directory name, loads all 13 ISOs, and
injects them into the LLM prompt. The kind-builder is the meta-builder that creates
these builder packages.

## Spec Table

| Property | Value |
|----------|-------|
| Builder location | archetypes/builders/{kind}-builder/ |
| ISO count | 13 per builder |
| Sub-agent location | .claude/agents/{kind}-builder.md |
| Loader | cex_skill_loader.py |
| Discovery | Directory name pattern: {kind}-builder/ |
| Pipeline integration | Each ISO maps to one 8F function |
| Kind registry | .cex/kinds_meta.json (130+ kinds) |
| Total builders | 126 (as of 2026-04-13) |

## The 13-ISO Pattern

Each ISO serves a specific role in the builder's lifecycle:

| ISO | 8F Function | Role in Pipeline |
|-----|-------------|-----------------|
| manifest | F1 CONSTRAIN | Identity: what this builder is, capabilities, routing |
| schema | F1 CONSTRAIN | Structure: required fields, body sections, constraints |
| system_prompt | F2 BECOME | Persona: rules, tone, knowledge boundary |
| instruction | F4 REASON | Process: step-by-step production phases |
| output_template | F6 PRODUCE | Template: `{{vars}}` filled during generation |
| examples | F3 INJECT | Calibration: golden + anti examples for few-shot |
| memory | F3 INJECT | Learning: patterns observed, evidence, confidence |
| tools | F5 CALL | Tooling: available tools, data sources, permissions |
| quality_gate | F7 GOVERN | Validation: HARD gates + SOFT scoring dimensions |
| knowledge_card | F3 INJECT | Domain: industry patterns, references, boundaries |
| architecture | F7 GOVERN | Structure: components, dependencies, boundary table |
| collaboration | F8 COLLABORATE | Teamwork: crews, handoffs, builder dependencies |
| config | F1 CONSTRAIN | Limits: naming, paths, sizes, runtime constraints |

## Pillar Mapping

Each ISO has its OWN pillar assignment (not the target kind's pillar):

| ISO kind | ISO pillar | Rationale |
|----------|-----------|-----------|
| type_builder (manifest) | P08 Architecture | Builder identity is architectural |
| schema | P06 Schema | Schema lives in schema pillar |
| system_prompt | P03 Prompt | Prompts live in prompt pillar |
| instruction | P03 Prompt | Process instructions are prompts |
| output_template | P05 Output | Templates live in output pillar |
| examples | P07 Evaluation | Examples are evaluation artifacts |
| learning_record (memory) | P10 Memory | Memory lives in memory pillar |
| tools | P04 Tools | Tools live in tools pillar |
| quality_gate | P11 Feedback | Gates live in feedback pillar |
| knowledge_card | P01 Knowledge | Knowledge lives in knowledge pillar |
| architecture | P08 Architecture | Architecture lives in architecture pillar |
| collaboration | P12 Orchestration | Collaboration is orchestration |
| config | P09 Config | Config lives in config pillar |

## Loader Discovery

cex_skill_loader.py discovers builders by:

1. Scanning `archetypes/builders/` for directories matching `{kind}-builder/`
2. Loading all 13 `bld_*.md` files from the directory
3. Parsing YAML frontmatter from each file
4. Assembling the complete builder context for prompt injection
5. Falling back to `_shared/` ISOs if a kind-specific ISO is missing

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Fewer than 13 ISOs | Loader fails or injects incomplete context |
| Generic placeholder content | Wastes tokens, LLM produces generic output |
| Missing boundary sections | Builder accepts out-of-scope requests |
| Schema/gate mismatch | Artifacts pass gates but violate schema (or vice versa) |
| Wrong ISO pillar assignment | Compilation routes ISO to wrong directory |
| Hardcoded quality score | Violates quality: null rule, biases peer review |
| No golden example | LLM has no calibration target, output varies wildly |

## References

- Convention over Configuration: Ruby on Rails (DHH, 2004) -- same directory = same behavior
- Archetype pattern: Gang of Four -- template class with specialized instances
- 8F pipeline: CEX spec (.claude/rules/8f-reasoning.md)
- Builder registry: .cex/kinds_meta.json
- Loader source: cex_sdk/cex_skill_loader.py
