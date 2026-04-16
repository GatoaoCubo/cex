---
kind: collaboration
id: bld_collaboration_cost_budget
pillar: P12
llm_function: COLLABORATE
purpose: How cost-budget-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Cost Budget"
version: "1.0.0"
author: n03_builder
tags: [cost_budget, builder, collaboration, P12]
tldr: "cost-budget-builder crew roles: receives provider list and spend targets, produces budget catalog with alert policy."
domain: "cost budget construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Collaboration: cost-budget-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what budget limits and alert thresholds does
this scope need, with what reset policy and overage behavior?"
I do not configure request throughput (rate_limit_config). I do not define feature toggles.
I govern spend so LLM deployments stay within financial boundaries without surprise billing.

## Crew Compositions
### Crew: "Provider Deployment Configuration"
```
  1. boot-config-builder     -> "provider startup configuration"
  2. rate-limit-config-builder -> "request throughput limits (RPM/TPM)"
  3. cost-budget-builder      -> "spend limits per provider/model (USD/tokens)"
  4. env-config-builder       -> "environment variables for provider auth"
```

### Crew: "Multi-Provider Cost Governance"
```
  1. agent-builder            -> "agent definition and model selection"
  2. cost-budget-builder      -> "budget per provider used by agent"
  3. fallback-chain-builder   -> "degradation if budget exhausted"
  4. trace-config-builder     -> "spend observability and alert channels"
```

### Crew: "FinOps Setup"
```
  1. cost-budget-builder      -> "budget limits and alert thresholds"
  2. rate-limit-config-builder -> "throughput caps"
  3. guardrail-builder        -> "safety rules including spend guardrails"
  4. workflow-builder         -> "workflow gates on budget availability"
```

## Handoff Protocol
### I Receive
- seeds: scope (global, provider name, model slug), provider list
- optional: spend targets (USD/month), token volume estimates, alert channels, escalation contacts
### I Produce
- cost_budget artifact (.md + compiled .yaml)
- committed to: `P09_config/examples/p09_cb_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
| Builder | Why |
|---------|-----|
| boot-config-builder | Reveals which providers are active in the deployment |
| trace-config-builder | Provides alert channel definitions (webhook URLs, log paths) |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| fallback-chain-builder | Fallback chain may trigger when cost_budget is exhausted |
| workflow-builder | Workflow steps gate on budget availability before calling LLM |
| agent-builder | Agent card references cost_budget for its provider spend governance |
| guardrail-builder | Spend guardrails reference cost_budget thresholds for enforcement |
