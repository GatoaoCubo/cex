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
capability_summary: >
  L1: Meta-builder that cria outros builders — gera 13 builder specs complete for qualquer kind.
  L2: Usa meta-templates for produzir manifest, instruction, config, memory, tools, etc.
  L3: Quando precisa criar um builder novo for um kind that ainda not tem builder.
quality: 9.0
title: "Manifest Builder"
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
density_score: 0.90
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
1. "cria builder", "scaffold builder", "novo kind precisa builder"
2. "gera 13 builder specs", "meta-builder"
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
