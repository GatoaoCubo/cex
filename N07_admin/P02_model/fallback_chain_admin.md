---
id: p02_fc_cex_model_fallback
kind: fallback_chain
8f: F8_collaborate
pillar: P02
title: Fallback Chain -- CEX Model Selection
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: orchestration
quality: 9.1
tags: [fallback-chain, multi-cli, cost, free, ollama]
tldr: Model degradation chain -- opus to sonnet to gemini-free to ollama-local. Zero-cost fallback always available.
density_score: 0.92
related:
  - kc_ollama_deployment_guide
  - n05_readme_install
  - claude_vs_free_decision_matrix
  - p12_sc_admin_orchestrator
  - spec_infinite_bootstrap_loop
  - roadmap_cex
  - bld_config_model_provider
  - bld_config_fallback_chain
  - p01_kc_fallback_chain
  - p02_fb_model_cascade
---

# Fallback Chain: CEX Model Selection

## Chain (highest capability to free fallback)

| Priority | Provider | Model | Context | Cost | When |
|----------|----------|-------|---------|------|------|
| 1 | Anthropic | claude-opus-4-6 | 200K | 1939$ | Complex construction, orchestration |
| 2 | Anthropic | claude-sonnet | 200K | $ | Creative, content, standard builds |
| 3 | Google | gemini-2.5-pro | 1M | /usr/bin/bash | Knowledge, research (subscription) |
| 4 | OpenAI | codex/GPT-5.4 | 192K | 1939 | Code review, testing |
| 5 | Ollama | qwen2.5-coder:7b | 32K | /usr/bin/bash | Local fallback, code tasks |
| 6 | Ollama | llama3.1:8b | 128K | /usr/bin/bash | Local fallback, general |
| 7 | Ollama | codexaft:v3 | 8K | /usr/bin/bash | Fine-tuned CEX model (smallest) |

## Degradation Rules

1. If API key missing for Priority 1-4: skip to next
2. If Ollama not running: error (no model available)
3. If rate-limited: auto-degrade one level
4. If context too large for current model: try next with larger context
5. Quality threshold: if output < 7.0 at priority N, retry at N-1

## Free-Only Mode

User with zero subscriptions can still use CEX:
- Install Ollama (free, local)
- Pull qwen2.5-coder:7b (4GB download)
- Boot: claude --model ollama/qwen2.5-coder:7b (requires Ollama running locally)
- All CEX tools work (motor, doctor, compile, index are Python-only)
- 8F Runner F4/F6 use local model (slower, lower quality, but functional)

## Fine-Tuned CEX Model (codexaft)

{{BRAND_DOMAIN}}/codexaft:v3 is a Qwen 3.1B fine-tuned on CEX artifacts.
Smallest usable model for CEX-specific tasks.
Ideal for: scaffold generation, frontmatter completion, template filling.
Not ideal for: complex reasoning, multi-kind crews, architecture design.

## Per-Nucleus Default

| Nucleus | Primary | Fallback 1 | Fallback 2 |
|---------|---------|------------|------------|
| N07 orch | opus-4-6 | sonnet | (none -- orchestrator needs capability) |
| N03 build | opus | sonnet | ollama/qwen2.5-coder |
| N05 ops | codex | opus | ollama/deepseek-coder |
| N04 know | gemini-2.5-pro | sonnet | ollama/llama3.1 |
| N01 res | gemini-2.5-pro | sonnet | ollama/llama3.1 |
| N02 mkt | sonnet | haiku | ollama/llama3.1 |
| N06 com | sonnet | haiku | ollama/codexaft |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_ollama_deployment_guide]] | upstream | 0.39 |
| [[n05_readme_install]] | downstream | 0.36 |
| [[claude_vs_free_decision_matrix]] | downstream | 0.36 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.31 |
| [[spec_infinite_bootstrap_loop]] | related | 0.31 |
| [[roadmap_cex]] | related | 0.29 |
| [[bld_config_model_provider]] | downstream | 0.28 |
| [[bld_config_fallback_chain]] | downstream | 0.27 |
| [[p01_kc_fallback_chain]] | related | 0.27 |
| [[p02_fb_model_cascade]] | sibling | 0.26 |
