---
kind: tools
id: bld_tools_streaming_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for streaming_config production
quality: 9.1
title: "Tools Streaming Config"
version: "1.0.0"
author: n03_builder
tags: [streaming_config, builder, tools, P04]
tldr: "Tools for streaming_config production: brain_query for dedup, cex_compile for validation, cex_score for gate."
domain: "streaming config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Tools: streaming-config-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing streaming_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_compile.py | Compile .md to .yaml after save | Phase 3 (post-produce) | REQUIRED |
| cex_score.py | Score artifact quality | Phase 3 (validation) | REQUIRED |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_retriever.py | Find similar streaming configs for reference | Phase 1 | AVAILABLE |

## Data Sources

| Source | Path | Data |
|--------|------|------|
| CEX Schema | P05_output/_schema.yaml | Field definitions, streaming_config kind |
| CEX Examples | P05_output/examples/ | Real streaming_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P05_streaming_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, output layer |
| Protocol docs | External reference | SSE (W3C), WS (RFC 6455), Chunked (RFC 7230) |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Compile Command

```bash
python _tools/cex_compile.py P05_output/examples/p05_sc_{name}.md
```

## Score Command

```bash
python _tools/cex_score.py --apply P05_output/examples/p05_sc_{name}.md
```

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `^p05_sc_[a-z][a-z0-9_]+$`,
protocol is valid enum, buffer_bytes positive integer, body <= 2048 bytes, quality == null.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_streaming_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_tools_streaming_config.md
```
