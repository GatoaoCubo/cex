---
kind: collaboration
id: bld_collaboration_rate_limit_config
pillar: P12
llm_function: COLLABORATE
purpose: How rate-limit-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - rate-limit-config-builder
  - bld_collaboration_model_provider
  - bld_knowledge_card_rate_limit_config
  - bld_examples_rate_limit_config
  - p03_sp_rate_limit_config_builder
  - bld_collaboration_runtime_rule
  - bld_tools_rate_limit_config
  - bld_collaboration_cost_budget
  - bld_instruction_rate_limit_config
  - bld_config_rate_limit_config
---

# Collaboration: rate-limit-config-builder

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the RPM, TPM, budget, and tier limits for this provider and tier?"
I do not define retry logic. I do not define API credentials. I do not define execution timeouts.
I declare the numeric quota boundaries so callers know exactly what they can consume.
## Crew Compositions
### Crew: "Provider Integration"
```
  1. rate-limit-config-builder -> "quota declaration (RPM, TPM, budget, tier)"
  2. runtime-rule-builder       -> "retry/backoff policy for 429 handling"
  3. env-config-builder         -> "API key, base URL, model selection"
```
### Crew: "Multi-Provider Setup"
```
  1. rate-limit-config-builder (anthropic) -> "Anthropic Build tier limits"
  2. rate-limit-config-builder (openai)    -> "OpenAI Tier 2 limits"
  3. rate-limit-config-builder (litellm)   -> "LiteLLM proxy unified limits"
  4. client-builder                        -> "client that reads all three configs"
```
### Crew: "Cost-Controlled Production"
```
  1. rate-limit-config-builder -> "quota + budget_usd + alert_threshold"
  2. guardrail-builder         -> "execution constraints, circuit breaker policy"
  3. monitor-builder           -> "observability for 429 rate and budget burn"
```
## Handoff Protocol
### I Receive
- seeds: provider name, tier, monthly budget target
- optional: model list (for model_overrides), concurrent target, retry_after preference
### I Produce
- rate_limit_config artifact (.md with YAML frontmatter)
- committed to: `cex/P09_config/examples/p09_ratelimit_{provider}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures listed
## Builders I Depend On
None — independent builder (layer 0). Rate limit configs can be defined standalone
once provider and tier are known.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| runtime-rule-builder | Needs retry_after and quota values to size backoff windows |
| client-builder | Reads RPM/TPM to implement throttling and request queuing |
| guardrail-builder | References budget_usd and alert_threshold for cost circuit breakers |
| monitor-builder | Uses RPM/TPM as baselines for 429-rate alerting thresholds |
| agent-builder | Agents enforce rate limits during parallel task execution |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[rate-limit-config-builder]] | upstream | 0.55 |
| [[bld_collaboration_model_provider]] | sibling | 0.46 |
| [[bld_knowledge_card_rate_limit_config]] | upstream | 0.45 |
| [[bld_examples_rate_limit_config]] | upstream | 0.43 |
| [[p03_sp_rate_limit_config_builder]] | upstream | 0.43 |
| [[bld_collaboration_runtime_rule]] | sibling | 0.42 |
| [[bld_tools_rate_limit_config]] | upstream | 0.42 |
| [[bld_collaboration_cost_budget]] | sibling | 0.41 |
| [[bld_instruction_rate_limit_config]] | upstream | 0.39 |
| [[bld_config_rate_limit_config]] | upstream | 0.38 |
