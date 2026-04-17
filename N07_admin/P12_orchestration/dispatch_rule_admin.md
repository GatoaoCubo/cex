---
id: p12_dr_admin_orchestration
title: "Dispatch Rule Admin"
kind: dispatch_rule
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: orchestration
quality: 9.1
tags: [dispatch-rule, orchestration, N07, routing, multi-cli]
tldr: "Routes tasks to 6 nuclei by domain keywords — build to N03, research to N01, marketing to N02, knowledge to N04, ops to N05, commercial to N06."
scope: admin_orchestration
keywords: [build, research, marketing, knowledge, operations, commercial, scaffold, analyze, write, deploy, index, price]
agent_group: orchestrator
model: opus
priority: 9
confidence_threshold: 0.70
fallback: n03
conditions:
  quality_min: 8.0
  signal_required: true
routing_strategy: keyword_match
density_score: 1.0
---

# Admin Orchestration Dispatch Rules

## Purpose

Master routing rules for N07 Orchestrator. Maps incoming task intent to the correct
specialist nucleus based on domain keywords. Each nucleus has a dedicated CLI and
LLM model optimized for its domain. N07 evaluates intent, matches keywords, and
dispatches via `bash _spawn/dispatch.sh`.

## Routing Rules

### Rule 1: Build / Scaffold → N03

| Property | Value |
|----------|-------|
| Keywords | build, create, construct, scaffold, generate, forge, artifact, kind, 8F, construir |
| Target | N03 (Builder) |
| CLI | claude opus |
| Priority | 9 |
| Mode | solo (default) or grid (if > 3 artifacts) |

### Rule 2: Research / Analysis → N01

| Property | Value |
|----------|-------|
| Keywords | research, analyze, paper, market, competitor, benchmark, survey, pesquisar |
| Target | N01 (Research) |
| CLI | gemini 2.5-pro |
| Priority | 8 |
| Mode | solo |

### Rule 3: Marketing / Copy → N02

| Property | Value |
|----------|-------|
| Keywords | marketing, copy, ad, campaign, brand, creative, slogan, social, redacao |
| Target | N02 (Marketing) |
| CLI | claude sonnet |
| Priority | 7 |
| Mode | solo |

### Rule 4: Knowledge / Docs → N04

| Property | Value |
|----------|-------|
| Keywords | knowledge, document, index, rag, kc, glossary, context, embed, conhecimento |
| Target | N04 (Knowledge) |
| CLI | gemini 2.5-pro |
| Priority | 8 |
| Mode | solo |

### Rule 5: Code / Test / Deploy → N05

| Property | Value |
|----------|-------|
| Keywords | code, test, debug, deploy, ci, cd, review, fix, refactor, ops, codigo |
| Target | N05 (Operations) |
| CLI | codex GPT-5.4 |
| Priority | 8 |
| Mode | solo |

### Rule 6: Sales / Pricing → N06

| Property | Value |
|----------|-------|
| Keywords | sales, pricing, course, monetize, commercial, revenue, conversion, venda |
| Target | N06 (Commercial) |
| CLI | claude sonnet |
| Priority | 7 |
| Mode | solo |

## Keyword Rationale

Keywords are domain-specific action verbs and nouns covering PT and EN variants.
Each rule covers a distinct domain with no keyword overlap. Priority breaks ties
when a task touches multiple domains. Stemming is applied for bilingual matching.

## Confidence Threshold

- **Threshold**: 0.70 (keyword match score)
- **Match strategy**: keyword_match with stemming (PT+EN)
- **Below threshold**: ask human for clarification

## Fallback Logic

- If no rule matches above 0.70 confidence: ask human for clarification
- If multiple rules match: highest priority wins
- If equal priority: prefer the rule with more keyword hits
- If N07 cannot classify: log to `.cex/runtime/signals/` as `dispatch_ambiguous` and wait

## References

- Workflow: N07_admin/P12_orchestration/workflow_admin.md
- Spawn config: N07_admin/P12_orchestration/spawn_config_admin.md
- Grid ops (fallbacks, recovery): N07_admin/P10_memory/grid_orchestration_mastery.md
