---
id: p01_kc_ollama_deployment_patterns
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Ollama Deployment Patterns for Custom Local Models"
version: 2.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: execution
quality: 9.1
tags: [ollama, deployment, gguf, lora, modelfile, local-llm]
tldr: "Ollama deploy depends on matching base and adapter, preserving template, and choosing quantization between memory and quality."
when_to_use: "Package fine-tuned model for Ollama or diagnose bad output in local deploy"
keywords: [ollama_deployment, modelfile, gguf_import, lora_adapter, quantization]
long_tails:
  - "How to deploy custom model on Ollama without degrading output"
  - "When to use single GGUF vs base plus adapter on Ollama"
axioms:
  - "ALWAYS use the same base model from training when applying adapter"
  - "NEVER swap chat template between training and inference"
linked_artifacts:
  primary: null
  related: [p01_kc_zero_touch_execution, p01_kc_cicd_pipeline_architecture]
density_score: 1.0
data_source: "https://docs.ollama.com/modelfile"
related:
  - kc_ollama_deployment_guide
  - p02_fc_cex_model_fallback
  - p03_sp_finetune_config_builder
  - n05_readme_install
  - p01_kc_finetune_config
  - bld_collaboration_finetune_config
  - claude_vs_free_decision_matrix
  - bld_tools_model_provider
  - bld_instruction_finetune_config
  - n05_output_monetization_infra
---

## Quick Reference

topic: local LLM deployment | scope: Ollama + GGUF/adapter | criticality: high
pipeline: export -> convert -> Modelfile -> ollama create -> validate

## Key Concepts

- Mismatch between base and adapter generates erratic output
- Chat template must match the one from training
- Single GGUF simplifies; base+adapter facilitates swap
- Q4_K_M balances memory, speed and quality

## Comparison

| Pattern | Structure | Advantage | Disadvantage |
|---------|-----------|-----------|-------------|
| Single GGUF | `FROM ./model.gguf` | Simple build | Adapter not swappable |
| Base+adapter | `FROM base` + `ADAPTER` | Fast swap | Base must match |
| HF Registry | `ollama run hf.co/...` | Minimal setup | Network dependent |

| Quantization | Reduction | Loss | Use case |
|-------------|-----------|------|----------|
| Q8_0 | ~50% | Minimal | Quality-first |
| Q5_K_M | ~62% | Low | Balanced plus |
| Q4_K_M | ~75% | Low | Recommended default |
| Q4_0 | ~75% | Moderate | Speed-first |
| Q2_K | ~87% | High | Extreme hardware |

| Symptom | Probable cause | Fix |
|---------|----------------|-----|
| Erratic output | Base different from training | Use exact base |
| Wrong format | Incorrect template | Set TEMPLATE |
| Slowness | CPU fallback | Check ollama ps |
| OOM | Context too large | Reduce num_ctx |
| Adapter ignored | Relative path | Use absolute path |

| Scenario | Ideal pattern | Quantization |
|----------|-------------|-------------|
| Quick prototype | HF Registry | Q4_K_M |
| Internal production | Single GGUF | Q4_K_M or Q8_0 |
| Multi-adapter dev | Base+adapter | Q4_K_M |
| Edge device | Single GGUF | Q2_K |
| High fidelity | Single GGUF | Q8_0 |

## Golden Rules

- ALWAYS validate FROM against the exact fine-tune base
- ALWAYS fix num_ctx and SYSTEM in the production Modelfile
- NEVER assume adapter compensates for incorrect template
- ALWAYS test latency and sanity before exposing API

## Code

<!-- lang: dockerfile | purpose: stable Ollama packaging -->
```dockerfile
FROM llama3.2:8b-instruct-q4_K_M
ADAPTER ./sales-assistant.gguf
PARAMETER num_ctx 4096
PARAMETER temperature 0.2
SYSTEM You answer as a concise e-commerce assistant.
```

<!-- lang: bash | purpose: build and smoke-test -->
```bash
ollama create organization-sales -f Modelfile
ollama run organization-sales "Resuma riscos de margem em 3 linhas."
ollama ps
```

## References

- external: https://docs.ollama.com/modelfile
- external: https://docs.ollama.com/import
- external: https://docs.ollama.com/cli
- deepens: p01_kc_zero_touch_execution
- deepens: p01_kc_cicd_pipeline_architecture


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_ollama_deployment_guide]] | sibling | 0.35 |
| [[p02_fc_cex_model_fallback]] | downstream | 0.24 |
| [[p03_sp_finetune_config_builder]] | downstream | 0.21 |
| [[n05_readme_install]] | downstream | 0.21 |
| [[p01_kc_finetune_config]] | sibling | 0.20 |
| [[bld_collaboration_finetune_config]] | downstream | 0.19 |
| [[claude_vs_free_decision_matrix]] | downstream | 0.19 |
| [[bld_tools_model_provider]] | downstream | 0.18 |
| [[bld_instruction_finetune_config]] | downstream | 0.18 |
| [[n05_output_monetization_infra]] | downstream | 0.18 |
