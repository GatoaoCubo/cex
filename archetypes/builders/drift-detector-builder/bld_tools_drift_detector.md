---
quality: 8.6
quality: 8.0
kind: tools
id: bld_tools_drift_detector
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for drift_detector production
title: "Tools Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, tools]
tldr: "Tools for drift_detector production: statistical testing, existing detector discovery, compilation."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_tools_function_def
  - bld_tools_hitl_config
  - bld_tools_response_format
  - bld_tools_search_tool
  - bld_tools_validation_schema
  - bld_tools_quality_gate
  - bld_tools_streaming_config
  - bld_tools_cli_tool
  - bld_tools_citation
  - bld_tools_retriever_config
---

# Tools: drift-detector-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Find existing drift_detector artifacts | Phase 1 (dedup) | CONDITIONAL |
| cex_retriever.py | Semantic search for similar detectors | Phase 1 (research) | AVAILABLE |
| cex_score.py | Score artifact quality | Phase 3 (validate) | AVAILABLE |
| cex_compile.py | Compile .md to .yaml | Phase 3 (F8) | AVAILABLE |
| Evidently AI [external] | Open-source drift reports + monitoring | Phase 2 (reference) | EXTERNAL |
| Arize Phoenix [external] | LLM/embedding drift monitoring | Phase 2 (reference) | EXTERNAL |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P11_feedback/_schema.yaml | Field definitions |
| Evidently docs | docs.evidentlyai.com | PSI/KS implementation reference |
| Arize Phoenix | docs.arize.com/phoenix | LLM drift patterns |
| Whylogs | whylogs.readthedocs.io | Statistical profile comparison |

## PSI Calculation Reference
```
PSI = sum((actual_% - expected_%) * ln(actual_% / expected_%))
Bucket into 10-20 bins; handle zero-frequency bins with epsilon = 0.0001
```

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Validation
Key checks: YAML parses, id `^p11_dd_`, detection_method in enum,
threshold is numeric (not string), features_monitored is a list with named elements,
alert_rule has destination and frequency, quality == null, body <= 3072 bytes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_function_def]] | sibling | 0.42 |
| [[bld_tools_hitl_config]] | sibling | 0.41 |
| [[bld_tools_response_format]] | sibling | 0.41 |
| [[bld_tools_search_tool]] | sibling | 0.41 |
| [[bld_tools_validation_schema]] | sibling | 0.40 |
| [[bld_tools_quality_gate]] | sibling | 0.39 |
| [[bld_tools_streaming_config]] | sibling | 0.39 |
| [[bld_tools_cli_tool]] | sibling | 0.39 |
| [[bld_tools_citation]] | sibling | 0.39 |
| [[bld_tools_retriever_config]] | sibling | 0.39 |
