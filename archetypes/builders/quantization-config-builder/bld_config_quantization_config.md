---
kind: config
id: bld_config_quantization_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for quantization_config production
quality: 8.7
title: "Config Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, config]
tldr: "Naming, paths, limits for quantization_config production"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_transport_config
  - bld_config_ab_test_config
  - bld_config_data_residency
  - bld_config_usage_quota
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_pricing_page
  - bld_config_vad_config
---

## Domain
quantization_config artifacts define bits, precision, and quant_type parameters
for model weight compression. Pillar: P09 (Config).

## Naming Convention
Pattern: p09_qc_{{name}}.yaml
Examples:
- p09_qc_llama3.yaml
- p09_qc_mistral.yaml

## Paths
Artifacts: P09_config/quantization/

## Limits
- max_bytes: 2048
- max_turns: 10
- effort_level: medium

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_transport_config]] | sibling | 0.58 |
| [[bld_config_ab_test_config]] | sibling | 0.56 |
| [[bld_config_data_residency]] | sibling | 0.55 |
| [[bld_config_usage_quota]] | sibling | 0.55 |
| [[bld_config_diff_strategy]] | sibling | 0.54 |
| [[bld_config_agent_computer_interface]] | sibling | 0.53 |
| [[bld_config_sales_playbook]] | sibling | 0.53 |
| [[bld_config_search_strategy]] | sibling | 0.52 |
| [[bld_config_pricing_page]] | sibling | 0.52 |
| [[bld_config_vad_config]] | sibling | 0.51 |
