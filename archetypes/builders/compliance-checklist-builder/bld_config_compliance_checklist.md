---
kind: config
id: bld_config_compliance_checklist
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for compliance_checklist production
quality: 8.6
title: "Config Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, config]
tldr: "Naming, paths, limits for compliance_checklist production"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p11_cc_{{name}}.md`
Examples:
- `p11_cc_example.md`
- `p11_cc_compliance.md`

## Paths
- `/artifacts/compliance_checklists/p11_cc_{{name}}.md`
- `/reports/p11_cc_{{name}}_report.json`

## Limits
- max_bytes: 6144
- max_turns: 10
- effort_level: medium

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
