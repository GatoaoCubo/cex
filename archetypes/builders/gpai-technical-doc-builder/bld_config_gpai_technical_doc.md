---
kind: config
id: bld_config_gpai_technical_doc
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for gpai_technical_doc production
quality: 8.6
title: "Config GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, config, GPAI, EU-AI-Act, Annex-IV]
tldr: "Naming, paths, limits for gpai_technical_doc production"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p11_gpai_{{model}}.md`
Examples: `p11_gpai_acmellm_v2_1.md`, `p11_gpai_company_foundation_model_v1.md`

## Paths
Artifacts stored in: `P11_governance/gpai_technical_docs/`

## Limits
max_bytes: 5120
max_turns: 8
effort_level: 5

## Hooks
pre_build: validate_annex_iv_fields
post_build: compile + signal_n07
on_error: null
on_quality_fail: retry_with_field_checklist
