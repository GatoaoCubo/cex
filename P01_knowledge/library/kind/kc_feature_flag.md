---
id: p01_kc_feature_flag
kind: knowledge_card
type: kind
pillar: P09
title: "Feature Flag — Deep Knowledge for feature_flag"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: feature_flag
quality: 9.1
tags: [feature_flag, P09, GOVERN, kind-kc]
tldr: "feature_flag is a lightweight on/off control artifact with gradual rollout support — enabling kill switches, incremental rollouts, and per-agent_group capability gating without redeployment."
when_to_use: "Building, reviewing, or reasoning about feature_flag artifacts"
keywords: [feature_toggle, kill_switch, gradual_rollout]
feeds_kinds: [feature_flag]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Feature Flag

## Spec
```yaml
kind: feature_flag
pillar: P09
llm_function: GOVERN
max_bytes: 1536
naming: p09_ff_{{feature}}.yaml
core: false
```

## What It Is
A feature_flag is a binary on/off control artifact with optional gradual rollout percentage — it enables instant kill switches, incremental capability rollouts, and per-agent_group feature gating without code deployment. It is NOT a permission (which controls access to resources), NOT a env_config (which is generic configuration, not capability toggling).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Env var boolean pattern | `LANGCHAIN_TRACING_V2=true` — boolean env toggle |
| LlamaIndex | N/A | No flag system; `Settings` object covers some cases |
| CrewAI | N/A | No native flag; boolean env var pattern used |
| DSPy | Module activation | Module inclusion/exclusion controlled in program flow |
| Haystack | Pipeline component inclusion | Adding/removing components acts as implicit flag |
| OpenAI | `anthropic-beta` request headers | Beta features toggled per-request via headers |
| Anthropic | `anthropic-beta` headers | Beta feature gating: `computer-use-2025-11-24` |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| feature | string | required | kebab-case identifier — descriptive = fewer misuses |
| enabled | bool | false | Default off for new features reduces blast radius |
| rollout_pct | int | 0 | 0-100 percentage; gradual = safer but slower adoption |
| owner | string | required | Agent_group/team — orphaned flags accumulate silently |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Kill switch | Instant disable without redeployment | `FIRECRAWL_ENABLED: false` in production emergency |
| Gradual rollout | 10% → 50% → 100% adoption cadence | `rollout_pct` incremented over days/weeks |
| Per-agent_group flag | Feature enabled for one agent_group only | `scope: [atlas]`, `enabled: true` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Permanent flags | Flag never removed after 100% rollout pollutes config | Lifecycle: add → ramp → cleanup; remove at 100% |
| Flag without owner | Orphaned flags accumulate — no one knows safe removal | Always assign owner agent_group/team |
| Secret as flag | Using flag to carry API key or credential | Flags are boolean logic only — credentials go to secret_config |

## Integration Graph
```
env_config, permission --> [feature_flag] --> runtime_rule, agent_card
                                  |
                             law, decision_record, rate_limit_config
```

## Decision Tree
- IF binary on/off capability control THEN feature_flag
- IF credential or key THEN secret_config
- IF generic system configuration variable THEN env_config
- DEFAULT: feature_flag for any capability needing controlled rollout or kill switch

## Quality Criteria
- GOOD: feature, enabled, owner, rollout_pct all present
- GREAT: rollout plan documented, revert procedure, telemetry hook named
- FAIL: missing owner, no rollout plan, used to store non-boolean configuration
