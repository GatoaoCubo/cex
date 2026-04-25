---
id: kc_8f_stress_tests
kind: knowledge_card
8f: F3_inject
type: meta
pillar: P01
title: "8F Stress Tests — Vague Input → Production Artifact"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n01_intelligence
domain: meta
quality: 9.2
tags: [8f, stress-test, e2e, benchmark, regression]
tldr: "3 scenarios proving 8F amplifies 5-word vague input into validated artifacts + competitive benchmark vs raw LLM, Cursor, Custom GPTs"
when_to_use: "Validating 8F resilience; regression testing; demonstrating CEX value"
keywords: [stress-test, vague-input, amplification, e2e, regression]
linked_artifacts:
  - P01_knowledge/library/domain/meta/kc_8f_pipeline.md
  - _tools/cex_8f_runner.py
  - .claude/rules/8f-reasoning.md
density_score: null
related:
  - n06_report_intent_resolution_moat
  - bld_tools_reasoning_trace
  - p01_kc_8f_pipeline
  - p01_kc_cex_as_digital_asset
  - p12_wf_auto_ship
  - p07_regression_check
  - p01_kc_iterative_refinement_skill
  - p03_sp_n03_creation_nucleus
  - report_intent_resolution_value_prop
  - n06_intent_resolution_depth_spec
---

# 8F Stress Tests

## Executive Summary

3 stress scenarios use deliberately vague pt-BR input to test every 8F stage. Each defines: input, expected trace, outputs, pass/fail, regression markers. Competitive analysis benchmarks 8F vs 3 alternatives across 9 dimensions.

## S1: "faz um CRM pra pet shop"

**Ambiguity**: pet shop = grooming? vet? retail? CRM scope?

**Expected trace**: F1 fan-out → 3 kinds (landing_page, content_monetization, agent). F3 injects pet shop domain + brand. F4 disambiguates scope + GDP gate. F7 gates each >= 8.0.

**Outputs**: `landing_page_petshop_crm.md` (P05) + `content_monetization_petshop.md` (P11) + `agent_petshop_crm.md` (P02). All must compile.

**Pass**: 3 files exist + compile + quality >= 8.0 + F4 shows disambiguation.
**Regression**: F1 returns single kind | F4 skips ambiguity | score drops > 1.0.

## S2: "preciso de conteudo pro instagram"

**Ambiguity**: format (reels/stories/carousel)? audience? niche?

**Expected trace**: F1 → prompt_template + schedule. F3 injects brand_config + Instagram constraints (2200 chars, 30 hashtags). F4 plans format mix + CTAs + GDP gate. F6 produces variants + calendar.

**Outputs**: `prompt_template_instagram.md` (P03) + `schedule_instagram.md` (P08). Brand voice must match config.

**Pass**: Brand voice consistent + CTAs present + char limits respected.
**Regression**: F3 misses brand_config | F6 ignores platform limits | < 2 variants.

## S3: "documenta esse projeto"

**Ambiguity**: which project? depth? audience (dev/user)?

**Expected trace**: F1 → knowledge_card + context_doc. F3 **must scan actual repo** (git log, ls) — NOT hallucinate. F4 plans from real codebase. F5 finds existing docs, dedup. F7 validates all cited paths exist.

**Outputs**: `kc_project_overview.md` (P01) + updated `README.md`. No phantom file references.

**Pass**: Every documented path/function exists in codebase.
**Regression**: F3 skips repo scan | F6 hallucinated modules | F5 overwrites existing.

## Test Harness

```
SETUP    git stash; clean state
INPUT    cex_8f_runner.py --intent "<input>" --execute
CAPTURE  Parse 8F trace → F1-F8 fields
VERIFY   Files exist? Compile? Quality >= 8.0?
REGRESS  Compare trace vs baseline
CLEANUP  git stash pop
```

**Universal regression markers**: F1 kind changes for same input | F3 source count drops | F4 omits ambiguity | F7 score drops > 1.0 | F8 compile fails.

## Competitive Analysis

| Dim | 8F | Raw Claude | Cursor | Custom GPTs |
|-----|-----|-----------|--------|-------------|
| Ambiguity | F4 reasons + GDP | Guesses | Asks/guesses | Guesses |
| Knowledge | F3: 9 sources | Training only | File context | Uploads only |
| Quality gate | F7: 7H+6S+retry | None | Linter | None |
| Structure | Schema frontmatter | Freeform | Code files | Freeform |
| Versioning | F8 auto-commit | Manual | User git | None |
| Routing | 8 nuclei × 300 kinds | 1 model | 1 model | 1 GPT |
| Reuse | F5 dedup + retriever | None | Grep | None |
| Retry | F7→F6 auto (2x) | User re-prompts | User | User |
| Reproducible | Same trace | Temperature-var | Session-var | Temperature-var |

### 8F Wins

1. **Structured amplification**: 5 words → 8 stages → validated artifact (vs 1-pass)
2. **Constraint propagation**: schema rules F1→F8 (vs LLM invents format)
3. **Knowledge compounding**: F3 accumulated domain (vs zero-context start)
4. **Auto quality enforcement**: F7 catches before commit (vs manual review)
5. **Multi-artifact fan-out**: 1 intent → N typed artifacts (vs 1 blob)

### 8F Loses

1. **Latency**: 8 stages = ~3-5× slower for simple tasks
2. **Setup cost**: 13 ISOs × 300 kinds = 1495 files to maintain
3. **Rigidity**: assumes artifact output — poor for open conversation
4. **Learning curve**: 150 tools vs "just type"

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_report_intent_resolution_moat]] | downstream | 0.22 |
| [[bld_tools_reasoning_trace]] | downstream | 0.21 |
| [[p01_kc_8f_pipeline]] | sibling | 0.20 |
| [[p01_kc_cex_as_digital_asset]] | sibling | 0.20 |
| [[p12_wf_auto_ship]] | downstream | 0.20 |
| [[p07_regression_check]] | downstream | 0.19 |
| [[p01_kc_iterative_refinement_skill]] | sibling | 0.19 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.19 |
| [[report_intent_resolution_value_prop]] | related | 0.19 |
| [[n06_intent_resolution_depth_spec]] | downstream | 0.19 |
