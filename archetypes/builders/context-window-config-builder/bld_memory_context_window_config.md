---
id: p10_lr_context_window_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n04_knowledge
observation: "Context window configs that fail most often are missing output_reserve (model truncates mid-response) or have budgets exceeding total_tokens. Equal allocation across sections wastes capacity — RAG-heavy needs 50%+ for context."
pattern: "Always reserve output_reserve >= 2000 tokens. Budget proportionally to workload. Priority: system > query > context > examples. Validate sum <= total. quality:null always."
evidence: "Initial pattern from KC analysis — no production log yet."
confidence: 0.70
outcome: PENDING
domain: context_window_config
tags: [context-window, token-budget, overflow, priority, allocation]
tldr: "Reserve output >= 2000. Budget proportionally. Validate sum <= total. quality:null always."
impact_score: 7.0
decay_rate: 0.05
agent_group: n04_knowledge
keywords: [context_window, token_budget, output_reserve, overflow, priority_tiers]
memory_scope: project
observation_types: [user, feedback, project, reference]
llm_function: INJECT
quality: 8.8
title: Memory ISO - context_window_config
density_score: 1.0
related:
  - bld_knowledge_card_context_window_config
  - p01_kc_context_window_config
  - p03_sp_context_window_config_builder
  - p01_kc_token_budgeting
  - bld_collaboration_context_window_config
  - bld_output_template_context_window_config
  - bld_instruction_context_window_config
  - context-window-config-builder
  - bld_examples_context_window_config
  - p11_qg_context_window_config
---
## Summary
Context window configs allocate a model's finite context among prompt sections. The primary failure is insufficient output reserve leading to truncated responses.
## Pattern
1. **Reserve output first** — minimum 2000 tokens, typically 15-30% of total
2. **Budget proportionally** — match workload (RAG-heavy → 50% context)
3. **Priority tiers** — system prompt always protected first
4. **Validate arithmetic** — sum(budgets) + reserve <= total_tokens
## Anti-Pattern
- No output reserve: model truncates response
- Equal budgets: wastes capacity on low-priority sections
- Budget > total: impossible to assemble prompt
- Static budget for dynamic content: fixed 8K for variable RAG results

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_context_window_config]] | upstream | 0.49 |
| [[p01_kc_context_window_config]] | upstream | 0.47 |
| [[p03_sp_context_window_config_builder]] | upstream | 0.36 |
| [[p01_kc_token_budgeting]] | upstream | 0.30 |
| [[bld_collaboration_context_window_config]] | downstream | 0.30 |
| [[bld_output_template_context_window_config]] | upstream | 0.28 |
| [[bld_instruction_context_window_config]] | upstream | 0.28 |
| [[context-window-config-builder]] | upstream | 0.24 |
| [[bld_examples_context_window_config]] | upstream | 0.23 |
| [[p11_qg_context_window_config]] | downstream | 0.22 |
