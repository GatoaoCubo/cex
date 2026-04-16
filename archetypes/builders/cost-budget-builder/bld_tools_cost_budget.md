---
kind: tools
id: bld_tools_cost_budget
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for cost_budget production
quality: 9.1
title: "Tools Cost Budget"
version: "1.0.0"
author: n03_builder
tags: [cost_budget, builder, tools, P09]
tldr: "Tools for cost_budget production: retriever for duplicate check, compile for validation, token budget SDK for enforcement."
domain: "cost budget construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Tools: cost-budget-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_retriever.py | Search existing cost_budget artifacts for duplicates | Phase 1 (check overlap) | ACTIVE |
| cex_token_budget.py | SDK runtime that enforces cost_budget limits at call time | Phase 3 (verify enforceability) | ACTIVE |
| brain_query [MCP] | Search artifact pool for same provider/scope | Phase 1 (alternative) | CONDITIONAL |
| cex_compile.py | Compile .md to .yaml after authoring | F8 COLLABORATE | ACTIVE |
| cex_score.py | Peer-review scoring after authoring | F7 GOVERN | ACTIVE |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, cost_budget kind |
| CEX Examples | P09_config/examples/ | Real cost_budget artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09_cost_budget |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, config layer |
| Token Budget SDK | _tools/cex_token_budget.py | Runtime enforcement reference |
| Kinds Meta | .cex/kinds_meta.json | cost_budget kind definition |

## Runtime Integration
| SDK Method | Description | Budget Field Read |
|------------|-------------|-------------------|
| `check_budget(provider, model, tokens)` | Pre-call check: would this call exceed limit? | token_limit, usd_limit |
| `record_spend(provider, model, tokens, cost_usd)` | Post-call: record actual spend | reset_policy |
| `get_utilization(scope)` | Return current spend vs limit | total_budget, providers |
| `trigger_alert(level, provider, pct)` | Fire configured alert channel | alert_enabled, overage_action |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, providers list matches catalog,
body <= 3072 bytes, quality == null, no actual API keys or billing credentials in artifact.

## Pipeline Integration
1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_cost_budget
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_tools_cost_budget.md
```
