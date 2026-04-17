---
id: p02_ap_nucleus_boot_package
kind: agent_package
pillar: P02
title: Nucleus Boot Package -- Composition Pattern
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [agent-package, boot, composition, nucleus]
tldr: How 8 CEX kinds compose into a complete bootable nucleus.
density_score: 0.90
---

# Nucleus Boot Package

## The Problem

Legacy: 6-8 scattered files per agent (boot + MCP + identity + mental model + settings + dispatch + model card + fallback).
Each different format, different location, different update cycle.

## The CEX Solution

Each fragment is a proper CEX kind. A nucleus COMPOSES them:

| Fragment | CEX Kind | Pillar |
|----------|----------|--------|
| Boot script (CLI, env, model) | boot_config | P09 |
| Identity (who am I) | system_prompt | P03 |
| Decision logic | mental_model | P02 |
| Tool access | mcp_server | P04 |
| Permissions/plugins | env_config | P09 |
| Task routing | dispatch_rule | P12 |
| LLM selection | model_card | P02 |
| Degradation | fallback_chain | P02 |

## Boot Sequence

1. boot_config: set env vars, working dir, select CLI
2. model_card + fallback_chain: resolve which LLM
3. system_prompt: inject identity into LLM session
4. mental_model: load decision tree
5. mcp_server + env_config: configure tools
6. dispatch_rule: ready to receive tasks

## Key Insight

A bootable nucleus is a COMPOSITION of typed artifacts.
Each independently buildable, validatable, replaceable.
The boot_config is just the entry point.