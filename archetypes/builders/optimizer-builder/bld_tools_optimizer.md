---
kind: tools
id: bld_tools_optimizer
pillar: P04
llm_function: CALL
purpose: Tools available for optimizer production
quality: 9.1
title: "Tools Optimizer"
version: "1.0.0"
author: n03_builder
tags: [optimizer, builder, examples]
tldr: "Golden and anti-examples for optimizer construction, demonstrating ideal structure and common pitfalls."
domain: "optimizer construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_quality_gate
  - bld_tools_dispatch_rule
  - bld_tools_bugloop
  - bld_tools_diagram
  - bld_tools_component_map
  - bld_tools_golden_test
  - bld_tools_benchmark
  - bld_tools_mcp_server
  - bld_tools_type_def
  - bld_tools_guardrail
---

# Tools: optimizer-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing optimizers for domain | Phase 1 (check duplicates, find patterns) | CONDITIONAL |
| brain_query [MCP] | Find benchmarks for baseline values | Phase 1 (research thresholds) | CONDITIONAL |
| validate_artifact.py | Validate optimizer YAML against SCHEMA | Phase 3 | [PLANNED] |
| metric_probe.py | Measure current baseline from live system | Phase 1 (baseline capture) | [PLANNED] |
## Reference Artifacts (existing)
| Artifact | File | Domain |
|----------|------|--------|
| KC Latency Optimizer | P11_feedback/examples/p11_opt_kc_latency.md | Knowledge card generation |
| Pool Score Optimizer | P11_feedback/examples/p11_opt_pool_score.md | Pool quality |
| Embedding Cost Optimizer | P11_feedback/examples/p11_opt_embedding_cost.md | Vector store |
## Brain Query Patterns [IF MCP]
```
brain_query("optimizer {domain}")          # find existing optimizers for domain
brain_query("benchmark {metric_name}")     # find baseline values
brain_query("threshold {process_type}")    # find proven threshold ranges
```
## Tool Usage Rules
- brain_query: CONDITIONAL — only call if MCP is available in runtime
- If brain_query unavailable: use KNOWLEDGE.md threshold patterns as fallback
- validate_artifact.py: [PLANNED] — currently validate manually against QUALITY_GATES.md
- Never require tools that block production — all tools are optional accelerators

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_quality_gate]] | sibling | 0.48 |
| [[bld_tools_dispatch_rule]] | sibling | 0.46 |
| [[bld_tools_bugloop]] | sibling | 0.45 |
| [[bld_tools_diagram]] | sibling | 0.43 |
| [[bld_tools_component_map]] | sibling | 0.42 |
| [[bld_tools_golden_test]] | sibling | 0.42 |
| [[bld_tools_benchmark]] | sibling | 0.41 |
| [[bld_tools_mcp_server]] | sibling | 0.41 |
| [[bld_tools_type_def]] | sibling | 0.41 |
| [[bld_tools_guardrail]] | sibling | 0.40 |
