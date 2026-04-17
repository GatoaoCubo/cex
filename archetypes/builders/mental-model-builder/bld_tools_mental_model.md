---
kind: tools
id: bld_tools_mental_model
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for mental_model (P02) production
quality: 9.1
title: "Tools Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: mental-model-builder

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing mental_models to avoid duplicates | Phase 1 (analyze) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | mental_model field definitions |
| MM Examples | P02_model/examples/ | Existing mental_model artifacts |
| framework MMs | records/agent_groups/*/mental_model.yaml | 7 agent_group mental models |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_mental_model |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | P02/P10 overlap, layer position |
| agent-builder | archetypes/builders/agent-builder/ | Agent identity reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == mental_model, pillar == P02 (not P10),
quality == null, routing_rules >= 3, decision_tree >= 2, keywords are specific.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_mental_model
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-mental-model.md
```
