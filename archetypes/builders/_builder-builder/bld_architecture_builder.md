---
kind: architecture
id: bld_architecture_builder
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of builder — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_builder
  - _builder-builder
  - bld_knowledge_card_builder
  - bld_architecture_kind
  - bld_config_builder
  - bld_output_template_builder
  - kind-builder
  - p03_sp__builder_builder
  - bld_examples_builder
  - bld_instruction_builder
---

# Architecture: builder in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| META_MANIFEST.md | Meta-template that generates MANIFEST.md for any builder | _builder-builder | active |
| META_ARCHITECTURE.md | Meta-template that generates ARCHITECTURE.md for any builder | _builder-builder | active |
| META_INSTRUCTIONS.md | Meta-template that generates INSTRUCTIONS.md for any builder | _builder-builder | active |
| META_EXAMPLES.md | Meta-template that generates EXAMPLES.md for any builder | _builder-builder | active |
| _schema.yaml | JSON schema for the target type (input to builder generation) | target domain | required input |
| TAXONOMY_LAYERS.yaml | Pillar definitions, overlaps, and routing rules | system | required input |
| SEED_BANK.yaml | Keyword seeds for routing and discovery | system | required input |
| Generated MANIFEST.md | Builder identity, capabilities, routing (output artifact) | _builder-builder | output |
| Generated ARCHITECTURE.md | Component map, dependencies, boundary table (output artifact) | _builder-builder | output |

## Dependency Graph

```
TAXONOMY_LAYERS.yaml  --produces-->  _builder-builder  --produces-->  MANIFEST.md
_schema.yaml          --produces-->  _builder-builder  --produces-->  ARCHITECTURE.md
SEED_BANK.yaml        --produces-->  _builder-builder  --produces-->  INSTRUCTIONS.md
META_MANIFEST.md      --produces-->  _builder-builder  --produces-->  EXAMPLES.md
META_ARCHITECTURE.md  --depends-->   _builder-builder
META_INSTRUCTIONS.md  --depends-->   _builder-builder
Generated MANIFEST.md --signals-->   target builder (becomes operational)
```

| From | To | Type | Data |
|------|----|------|------|
| _schema.yaml | _builder-builder | data_flow | type field definitions, required fields, validation rules |
| TAXONOMY_LAYERS.yaml | _builder-builder | data_flow | pillar assignment, overlaps, routing keywords |
| SEED_BANK.yaml | _builder-builder | data_flow | trigger phrases, keyword seeds |
| META_MANIFEST.md | _builder-builder | depends | template structure for MANIFEST generation |
| META_ARCHITECTURE.md | _builder-builder | depends | template structure for ARCHITECTURE generation |
| _builder-builder | MANIFEST.md | produces | fully hydrated builder identity file |
| _builder-builder | ARCHITECTURE.md | produces | boundary + dependency map for target type |
| _builder-builder | INSTRUCTIONS.md | produces | step-by-step build protocol |
| MANIFEST.md | target builder | signals | builder becomes discoverable and routable |

## Boundary Table

| builder IS | builder IS NOT |
|------------|----------------|
| A meta-artifact that generates other builders | A builder that produces domain artifacts directly |
| Template engine for MANIFEST, ARCHITECTURE, INSTRUCTIONS, EXAMPLES | Content about a specific domain (agent, axiom, signal, etc.) |
| The factory for the factory layer | A runtime executor or skill |
| Parameterized by _schema.yaml and TAXONOMY_LAYERS.yaml | Self-contained without external inputs |
| Responsible for structural consistency across all builders | Responsible for domain correctness of generated content |
| The entry point for adding new types to the system | A validator, quality gate, or governance artifact |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Input | _schema.yaml, TAXONOMY_LAYERS.yaml, SEED_BANK.yaml | Provide type definition, pillar position, and routing seeds |
| Meta-Templates | META_MANIFEST.md, META_ARCHITECTURE.md, META_INSTRUCTIONS.md, META_EXAMPLES.md | Structural skeletons with {{placeholders}} for all builder files |
| Generation | _builder-builder (LLM execution) | Hydrate templates with domain-specific content for the target type |
| Output | Generated MANIFEST.md, ARCHITECTURE.md, INSTRUCTIONS.md, EXAMPLES.md | Complete builder package ready to become a type_builder agent |
| Activation | Target builder routing registration | New builder becomes discoverable via brain_query and keyword routing |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_builder]] | downstream | 0.56 |
| [[_builder-builder]] | upstream | 0.47 |
| [[bld_knowledge_card_builder]] | upstream | 0.45 |
| [[bld_architecture_kind]] | sibling | 0.44 |
| [[bld_config_builder]] | downstream | 0.44 |
| [[bld_output_template_builder]] | upstream | 0.39 |
| [[kind-builder]] | related | 0.38 |
| [[p03_sp__builder_builder]] | upstream | 0.38 |
| [[bld_examples_builder]] | upstream | 0.35 |
| [[bld_instruction_builder]] | upstream | 0.32 |
