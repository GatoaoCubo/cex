---
kind: tools
id: bld_tools_circuit_breaker
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for circuit_breaker production
quality: 8.3
title: "Tools Circuit Breaker"
version: "1.0.0"
author: n03_builder
tags: [circuit_breaker, builder, tools]
tldr: "Tools: cex_compile, cex_doctor, cex_score. Data sources: P09 schema, Resilience4j docs, P09 examples."
domain: "circuit breaker construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
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
