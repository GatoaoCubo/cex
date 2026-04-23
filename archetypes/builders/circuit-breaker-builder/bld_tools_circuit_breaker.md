---
quality: 8.7
quality: 8.1
kind: tools
id: bld_tools_circuit_breaker
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for circuit_breaker production
title: "Tools Circuit Breaker"
version: "1.0.0"
author: n03_builder
tags: [circuit_breaker, builder, tools]
tldr: "Tools: cex_compile, cex_doctor, cex_score. Data sources: P09 schema, Resilience4j docs, P09 examples."
domain: "circuit breaker construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_tools_path_config
  - bld_tools_runtime_rule
  - bld_tools_retriever_config
  - bld_tools_feature_flag
  - bld_tools_cli_tool
  - bld_tools_golden_test
  - bld_tools_unit_eval
  - bld_tools_memory_scope
  - bld_tools_validation_schema
  - bld_tools_function_def
---

# Tools: circuit-breaker-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile .md to .yaml | Phase 3 (after produce) | ACTIVE |
| cex_score.py | Quality scoring | Phase 3 (validate) | ACTIVE |
| cex_doctor.py | Builder health check | Phase 3 (post-build) | ACTIVE |
| brain_query [MCP] | Search existing circuit_breaker artifacts | Phase 1 (check duplicates) | CONDITIONAL |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, circuit_breaker kind |
| CEX Examples | P09_config/examples/ | Real circuit_breaker artifacts |
| Resilience4j Docs | resilience4j.readme.io | Reference threshold and window configs |
| Hystrix Config | github.com/Netflix/Hystrix/wiki/Configuration | Legacy reference for threshold semantics |
| CEX Builder | archetypes/builders/circuit-breaker-builder/ | This builder's 13 ISOs |

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Validation Checklist
Manually verify against QUALITY_GATES.md:
1. YAML frontmatter parses cleanly
2. id matches `^p09_cb_[a-z][a-z0-9_]+$`
3. failure_rate_threshold: integer in [1, 100]
4. cooldown_duration: positive integer
5. probe_count: positive integer
6. All 4 body sections present
7. quality == null
8. tags includes "circuit_breaker"
9. body <= 3072 bytes
10. NOT conflated with rate_limit_config, fallback_chain, runtime_rule

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_path_config]] | sibling | 0.45 |
| [[bld_tools_runtime_rule]] | sibling | 0.45 |
| [[bld_tools_retriever_config]] | sibling | 0.44 |
| [[bld_tools_feature_flag]] | sibling | 0.44 |
| [[bld_tools_cli_tool]] | sibling | 0.43 |
| [[bld_tools_golden_test]] | sibling | 0.43 |
| [[bld_tools_unit_eval]] | sibling | 0.43 |
| [[bld_tools_memory_scope]] | sibling | 0.43 |
| [[bld_tools_validation_schema]] | sibling | 0.43 |
| [[bld_tools_function_def]] | sibling | 0.42 |
