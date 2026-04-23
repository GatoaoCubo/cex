---
kind: instruction
id: bld_instruction_cost_budget
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for cost_budget
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Cost Budget"
version: "1.0.0"
author: n03_builder
tags: [cost_budget, builder, instruction, P09]
tldr: "3-phase pipeline to produce cost_budget artifacts: research scope and providers, compose catalog and alerts, validate all gates."
domain: "cost budget construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - p03_sp_cost_budget_builder
  - bld_examples_cost_budget
  - bld_instruction_rate_limit_config
  - p11_qg_cost_budget
  - bld_instruction_context_doc
  - bld_instruction_env_config
  - bld_instruction_batch_config
  - bld_schema_cost_budget
  - bld_instruction_memory_scope
  - p10_lr_cost_budget_builder
---

# Instructions: How to Produce a cost_budget
## Phase 1: RESEARCH
1. Identify the scope: global (all providers), a named provider (anthropic, openai, google),
   or a specific model slug (claude-opus-4-6, gpt-4o, gemini-2.5-pro)
2. Catalog all providers and models that need budget governance -- include current or projected
   monthly spend and token volumes
3. Determine the currency unit: USD (monetary) or token_units (raw token count)
4. Classify the reset policy for each entry: daily, weekly, monthly, rolling_7d, rolling_30d,
   or none (no reset -- cumulative cap)
5. Define alert thresholds: warn_pct (typically 80%) and block_pct (typically 100%)
6. Determine overage_action per scope: block (hard stop API calls), warn (notify only),
   log (silent audit trail)
7. Define escalation path: who is notified on warn, who is notified on block, which channels
   (log file, email, webhook, pagerduty)
8. Check existing cost_budgets via cex_retriever for the same scope -- do not duplicate a
   budget that already covers this provider

## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth for all fields
2. Read OUTPUT_TEMPLATE.md -- fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` -- never self-score
4. Write **Overview** section: what scope, why these limits, who enforces them (1-2 sentences)
5. Write **Budget Catalog** section: table with columns provider, model, token_limit, usd_limit,
   alert_threshold_pct, reset_policy, overage_action
6. Write **Alert Policy** section: channels, warn threshold behavior, block threshold behavior,
   escalation contacts or webhook endpoints
7. Write **Overage Rules** section: what happens on breach (grace period, auto-block, notification
   chain), how to request a limit increase
8. Confirm body <= 3072 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p09_cb_[a-z][a-z0-9_]+$`
4. Confirm at least one budget entry is defined
5. Confirm all budget entries have both a limit (token or USD) and an overage_action
6. Confirm alert thresholds are present and warn_pct < block_pct
7. Confirm no actual API keys, billing credentials, or payment data appear anywhere
8. Confirm `quality` is null
9. Confirm body <= 3072 bytes
10. Cross-check: does this govern SPEND (cost_budget) or THROUGHPUT (rate_limit_config)?
    If the limits are in RPM/TPM this belongs in rate_limit_config. If the limits are in
    USD or total tokens this is cost_budget. Never mix the two.
11. If score < 8.0: revise in the same pass before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_cost_budget_builder]] | related | 0.48 |
| [[bld_examples_cost_budget]] | downstream | 0.45 |
| [[bld_instruction_rate_limit_config]] | sibling | 0.43 |
| [[p11_qg_cost_budget]] | downstream | 0.42 |
| [[bld_instruction_context_doc]] | sibling | 0.39 |
| [[bld_instruction_env_config]] | sibling | 0.39 |
| [[bld_instruction_batch_config]] | sibling | 0.38 |
| [[bld_schema_cost_budget]] | downstream | 0.37 |
| [[bld_instruction_memory_scope]] | sibling | 0.37 |
| [[p10_lr_cost_budget_builder]] | downstream | 0.37 |
