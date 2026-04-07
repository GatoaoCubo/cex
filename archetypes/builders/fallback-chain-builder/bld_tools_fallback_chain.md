---
kind: tools
id: bld_tools_fallback_chain
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for fallback_chain production
quality: 9.1
title: "Tools Fallback Chain"
version: "1.0.0"
author: n03_builder
tags: [fallback_chain, builder, examples]
tldr: "Golden and anti-examples for fallback chain construction, demonstrating ideal structure and common pitfalls."
domain: "fallback chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: fallback-chain-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing fallback_chains to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, step object |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_fallback_chain |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Model Cards | P02_model/examples/p02_mc_*.md | Model specs, pricing, capabilities |
| LiteLLM | docs.litellm.ai/docs/set_keys | Provider model identifiers |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == fallback_chain, quality == null,
steps_count matches chain rows, steps ordered by decreasing capability, timeout > 0.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_fallback_chain
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-fallback-chain.md
```
