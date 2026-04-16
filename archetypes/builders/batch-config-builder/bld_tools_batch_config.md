---
kind: tools
id: bld_tools_batch_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for batch_config production
quality: 9.1
title: "Tools Batch Config"
version: "1.0.0"
author: n03_builder
tags: [batch_config, builder, tools, P09]
tldr: "Tools for batch_config production: data sources, validation tools, provider API references."
domain: "batch config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

# Tools: batch-config-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing batch_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_compile.py | Compile .md artifact to .yaml | Phase 3 (after write) | REQUIRED |
| cex_score.py | Score artifact quality | Phase 3 (after compile) | REQUIRED |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, batch_config kind |
| CEX kinds_meta | .cex/kinds_meta.json | Boundary, max_bytes, naming for batch_config |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09_batch_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| OpenAI Batch API docs | platform.openai.com/docs/guides/batch | Provider-specific params, limits |
| Anthropic Message Batches docs | docs.anthropic.com/en/docs/build-with-claude/message-batches | Provider-specific params, limits |

## Provider API Reference

| Provider | Batch Submit Endpoint | Max Requests | Max File Size | SLA | Discount |
|----------|----------------------|--------------|---------------|-----|---------|
| OpenAI | POST /v1/batches | 50,000 | 200 MB | 24h | ~50% |
| Anthropic | POST /v1/messages/batches | 10,000 | N/A | Best-effort | ~50% |
| Azure OpenAI | POST /openai/... | Provider-specific | Provider-specific | 24h | ~50% |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate.
Key checks: YAML parses, id pattern `^p09_bc_[a-z][a-z0-9_]+$`, provider valid enum,
completion_window >= 1h, cost_cap_usd present, body <= 2048 bytes, quality == null,
no actual API keys in artifact.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_batch_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-batch-config.md
```
