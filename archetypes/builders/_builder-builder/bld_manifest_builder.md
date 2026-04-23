---
id: _builder-builder
kind: type_builder
pillar: P02
parent: null
domain: type_builder
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-31
author: builder_agent
tags: [meta-builder, kind-builder, P02, iso-generation, builder-creation]
keywords: [builder, meta-builder, iso, kind, scaffold, archetype, type_builder, generate]
triggers: ["create new builder", "scaffold builder for kind", "generate 13 builder specs for builder"]
capabilities: >
  L1: Meta-builder that creates other builders -- generates 13 builder specs for any kind.
  L2: Uses meta-templates to produce manifest, instruction, config, memory, tools, etc.
  L3: When you need to create a new builder for a kind that does not have one yet.
quality: 9.0
title: "Manifest Builder"
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
density_score: 0.90
related:
  - kind-builder
  - bld_architecture_kind
  - bld_collaboration_builder
  - bld_config_builder
  - bld_collaboration_kind
  - bld_examples_builder
  - bld_knowledge_card_builder
  - bld_architecture_builder
  - bld_collaboration_retriever
  - bld_output_template_builder
---
# _builder-builder
## Identity
Meta-builder that gera builders complete (13 builder specs) for qualquer kind no CEX. Masters
meta-template rendering, ISO structure, quality gate enforcement, and universal pattern hydration.
## Capabilities
1. Generate 13 builder specs for qualquer kind usando meta-templates
2. Apply universal patterns (keywords, memory_scope, effort, hooks, permissions)
3. Validate builder gerado contra doctor + norms (23 rules)
4. Respeitar non-default overrides table
## Routing
### Triggers
1. "create builder", "scaffold builder", "new kind needs builder"
2. "generate 13 builder specs", "meta-builder"
### Anti-triggers
- "cria agent" (→ agent-builder), "cria workflow" (→ workflow-builder)

## Metadata

```yaml
id: _builder-builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply -builder-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `type_builder` |
| Pillar | P02 |
| Domain | type_builder |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kind-builder]] | sibling | 0.54 |
| [[bld_architecture_kind]] | downstream | 0.51 |
| [[bld_collaboration_builder]] | downstream | 0.47 |
| [[bld_config_builder]] | downstream | 0.41 |
| [[bld_collaboration_kind]] | downstream | 0.37 |
| [[bld_examples_builder]] | downstream | 0.36 |
| [[bld_knowledge_card_builder]] | upstream | 0.33 |
| [[bld_architecture_builder]] | downstream | 0.32 |
| [[bld_collaboration_retriever]] | downstream | 0.32 |
| [[bld_output_template_builder]] | downstream | 0.30 |
