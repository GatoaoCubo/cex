---
id: p10_lr_content-monetization-builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
observation: "Content monetization configs that hardcode pricing in application code become unmaintainable when A/B testing tiers, changing providers, or expanding to new markets. Extracting all monetization parameters into config YAML reduced pricing change cycle from 2-3 dev hours to 5 minutes."
pattern: "Externalize ALL monetization parameters: tiers, prices, credit costs, provider config, email triggers, ad budgets. Config-driven monetization enables non-dev pricing changes, A/B testing, and multi-market expansion without code changes."
evidence: "3 content businesses analyzed: (1) CODEXA AI tools — credit system with 4 pipeline ops, hybrid pricing, 35% margin. (2) PetVida courses — Hotmart checkout, drip content, 70% margin. (3) DigitalPro infoproduct — Kiwify + Meta Ads funnel, 60% margin. All shared the same problem: pricing locked in code, provider switching required rewrite, no margin tracking."
confidence: 0.85
outcome: SUCCESS
domain: content_monetization
tags: [monetization, pricing, config-driven, credits, checkout, margin-tracking]
tldr: "Config-driven monetization: 2-3 dev hours → 5 min for pricing changes. Margin tracking prevents silent profit erosion."
impact_score: 8.5
decay_rate: 0.03
keywords: [monetization, pricing, credits, checkout, config, margin, webhook, courses]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Content Monetization"
density_score: 0.90
llm_function: INJECT
related:
  - bld_manifest_memory_type
  - p03_sp_content_monetization_builder
  - bld_tools_memory_type
  - bld_config_tagline
  - bld_config_memory_type
  - bld_tools_agent
  - bld_output_template_builder
  - bld_collaboration_content_monetization
  - p10_lr_e2e_eval_builder
  - content-monetization-builder
---
## Summary
Content monetization has two orthogonal concerns: business logic (what to charge, how
credits work, what triggers an email) and technical integration (which payment API, which
email provider, which ad platform). These evolve at wildly different rates — business
changes weekly (A/B test a price), integration changes quarterly (switch from Stripe to
Hotmart for BR market).

The 9-stage pipeline enforces this separation. PARSE through VALIDATE are business logic
stages that operate on config values. CHECKOUT, ADS, and EMAILS are integration stages
that operate on provider-specific APIs via ENV_VAR references.

## Key Insights

### Margin Tracking is Non-Negotiable
Without explicit floor_margin_pct per tier, pipeline costs (LLM tokens, API calls)
silently erode profit. A "Pro" tier at R$99.90/month with 1000 credits costs ~R$50 in
pipeline operations — margin is 50%. But if credit costs increase (model price hike,
new expensive operation), margin drops without anyone noticing. floor_margin_pct >= 0.30
with automated checking catches this before it becomes a P&L problem.

### Credit Systems Need Overdraft Policy
Undefined overdraft behavior causes three problems: (1) negative balances create
billing disputes, (2) users who hit zero mid-operation get broken results, (3) support
teams have no policy to reference. Explicit overdraft_policy (block, notify_then_block,
allow_negative) eliminates ambiguity.

### Mock Mode Prevents Costly Mistakes
Every checkout integration must default to mock_mode: true. Live payment APIs in
development environments cause: real charges (chargebacks), webhook floods (production
data corruption), and API key exposure in logs. Mock-first development catches
integration bugs before real money moves.

## Anti-Pattern: Monolithic Checkout
Embedding Stripe-specific logic throughout the application makes switching to Hotmart
(for BR infoproducts) a rewrite. Config-driven checkout (provider + webhook_url +
webhook_secret_env) allows provider swap with zero code changes — only config update.

## Builder Context

This ISO operates within the `content-monetization-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_content-monetization-builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_content-monetization-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | content_monetization |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_memory_type]] | upstream | 0.39 |
| [[p03_sp_content_monetization_builder]] | upstream | 0.37 |
| [[bld_tools_memory_type]] | upstream | 0.35 |
| [[bld_config_tagline]] | upstream | 0.34 |
| [[bld_config_memory_type]] | upstream | 0.33 |
| [[bld_tools_agent]] | upstream | 0.31 |
| [[bld_output_template_builder]] | upstream | 0.31 |
| [[bld_collaboration_content_monetization]] | downstream | 0.31 |
| [[p10_lr_e2e_eval_builder]] | sibling | 0.30 |
| [[content-monetization-builder]] | downstream | 0.30 |
