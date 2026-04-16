---
kind: config
id: bld_config_kubernetes_ai_requirement
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for kubernetes_ai_requirement production
quality: 8.6
title: "Config Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, config]
tldr: "Naming, paths, limits for kubernetes_ai_requirement production"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p09_kar_{{name}}.md`
Examples: `p09_kar_llama3_70b_pretrain.md`, `p09_kar_vllm_disagg_inference.md`

## Paths
Artifacts stored in: `/artifacts/p09/kubernetes_ai_requirements/{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 6
effort_level: 4

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
