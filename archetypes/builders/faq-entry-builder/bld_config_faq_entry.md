---
kind: config
id: bld_config_faq_entry
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for faq_entry production
quality: 8.6
title: "Config Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, config]
tldr: "Naming, paths, limits for faq_entry production"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: p01_faq_<topic>_<identifier>.md
Examples:
- p01_faq_trading_limits.md
- p01_faq_support_contact.md

## Paths
/opt/cex/faq/entries/P01/

## Limits
max_bytes: 3072
max_turns: 5
effort level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
