---
id: atom_33_nucleus_model_strategy
kind: knowledge_card
pillar: P01
quality: 9.0
title: CEX Nucleus Model Deployment and Fine-Tuning Strategy
author: CEX Engineering Team
date: 2026-04-05
description: Comprehensive technical plan for deploying and fine-tuning models across CEX nuclei to achieve zero-API dependency
tags: [LLM, fine-tuning, deployment, CEX, Ollama, QLoRA]
related:
  - roadmap_cex
  - p01_ctx_cex_project
  - p01_kc_finetune_config
  - spec_vllm_lora_hotswap
  - bld_knowledge_card_model_registry
  - spec_infinite_bootstrap_loop
  - p03_sp_cex_core_identity
  - kc_model_registry
  - p01_kc_cex_project_overview
  - spec_local_model_per_nucleus
---

# CEX Nucleus Model Deployment and Fine-Tuning Strategy

## Boundary

This artifact defines the technical implementation strategy for deploying fine-tuned models across CEX nuclei. It IS a detailed roadmap for transitioning from API-dependent execution to locally hosted models. It IS NOT a product specification, user guide, or business strategy document. The focus is strictly on model selection, dataset construction, deployment architecture, and risk mitigation.

## Related Kinds

- **technical_roadmap**: Provides high-level implementation phases and timelines  
- **deployment_plan**: Focuses on hardware configuration and model serving architecture  
- **model_selection_guide**: Details criteria for choosing base models and adapters  
- **fine_tuning_pipeline**: Describes dataset construction and training workflows  
- **quality_assurance_framework**: Defines evaluation criteria and success metrics  

---

## Executive Summary

This document outlines the technical roadmap for transitioning CEX's 184 nuclei from API-dependent model execution to locally deployed, fine-tuned models. The strategy leverages Gemma 4 26B A4B as the base model for most nuclei, with Qwen3 14B used where VRAM constraints require smaller models. The plan includes dataset construction, fine-tuning pipelines, deployment architecture, and a phased implementation timeline.

---

## 1. Model Selection and Justification

### 1.1 Candidate Models Evaluation

| Model | VRAM Fit (Q4) | Base Quality | Context Window | License | Tool Use | MoE Efficiency | FT Ecosystem |
|-------|----------------|--------------|----------------|---------|----------|----------------|--------------|
| Gemma4:26b | ✅ 14GB | #3 Open | 256K | Apache 2.0 | ✅ | ✅ | HF + Unsloth |
| Qwen3:14b | ✅ 10GB | #6 Open | 128K | Apache 2.0 | ✅ | ❌ | HF + Unsloth |
| Llama4:17b | ❌ 12GB | #8 Open | 10M | Llama | ✅ | ❌ | HF + Unsloth |
| DeepSeek-R1:7b | ✅ 5GB | #12 Open | 128K | MIT | ❌ | ❌ | Limited |

**Conclusion:** Gemma4:26b is the optimal base model for most nuclei due to its balance of quality, VRAM efficiency, and Apache 2.0 license. Qwen3:14b is selected for N04 and N05 where VRAM headroom is needed.

---

## 2. Dataset Construction Pipeline

### 2.1 Available Training Data

| Source | Count | Format | Use Case |
|--------|-------|--------|----------|
| Builder ISOs | 2,400+ | MD + YAML | N03 (construction rules) |
| Knowledge Cards | 2,000+ | MD | N01, N04 (domain knowledge) |
| Quality Gates | 184 | MD | All (evaluation criteria) |
| Golden Examples | 184 | MD | All (few-shot examples) |
| Atlas Atoms | 32 | MD | N01 (research patterns) |
| Marketing Artifacts | ~100+ | MD | N02 (copy patterns) |
| Mission Plans | ~20+ | MD | N07 (orchestration) |
| Commit History | 5,000+ | Git | N05 (code patterns) |

### 2.2 Training Pipeline

```python
# Dataset Construction Workflow
for nucleus in all_nuclei:
    collect_artifacts(nucleus)
    create_instruction_response_pairs(
        instruction_template="Build a {kind} about {topic}",
        response_source="bld_examples_{kind}.md"
    )
    augment_with_quality_gates(
        positive_examples=HARD_gate_pass,
        negative_examples=HARD_gate_fail
    )
    format_for_qloRA(alpaca_format=True)
    train_model(
        base_model="gemma4:26b-a4b",
        adapter_size=r=16,
        epochs=3
    )
    evaluate_with(cex_doctor.py)
    deploy_model(ollama.create("cex-n0x"))
```

---

## 3. Deployment Architecture (Phase 3)

### 3.1 Hardware Configuration

**RTX 5070 Ti (16GB VRAM)**  
- Ollama serving ONE model at a time  
- Sequential dispatch (1 nucleus at a time)  
- Future scalability: 2x 5070 Ti = 32GB VRAM (support 2 nuclei parallel)

### 3.2 Model Deployment

```
[RTX 5070 Ti]
  |
  +-- Ollama Server
       |
       +-- cex-n07 (Gemma4:26b + N07 QLoRA) - orchestration
       +-- cex-n03 (Gemma4:26b + N03 QLoRA) - building
       +-- cex-n01 (Gemma4:26b + N01 QLoRA) - research
       +-- cex-n02 (Gemma4:26b + N02 QLoRA) - marketing
       +-- cex-n04 (Qwen3:14b + N04 QLoRA) - knowledge
       +-- cex-n05 (Qwen3:14b + N05 QLoRA) - operations
       +-- cex-n06 (Gemma4:e4b + N06 FT) - commercial
       +-- cex-pf  (Gemma4:e4b + preflight FT) - context compression
```

### 3.3 Ollama Modelfile Example

```yaml
# cex-n03 Modelfile
FROM gemma4:26b-a4b
ADAPTER ./adapters/cex-n03-qlora/
PARAMETER temperature 0.3
PARAMETER num_ctx 65536
SYSTEM "You are N03 Builder, the artifact construction nucleus of CEX..."
```

---

## 4. Implementation Roadmap

| Phase | Timeline | Milestone | Cost Reduction |
|-------|----------|-----------|----------------|
| 0 | Immediate | 184 kinds + builders registered | API-dependent |
| 1 | Week 1 | Gemma4:26b as local fallback | 50% API reduction |
| 2 | Week 2-3 | Dataset construction pipeline | 30% API reduction |
| 3 | Week 4-6 | QLoRA adapter deployment | 15% API reduction |
| 4 | Week 7-8 | Full model deployment | Zero API dependency |

---

## 5. Risk Management

| Risk Category | Mitigation Strategy | Owner |
|---------------|---------------------|-------|
| VRAM Limitations | Prioritize Qwen3:14b for N04/N05 | Hardware Team |
| Data Quality | Implement cex_doctor.py validation | QA Team |
| Model Drift | Weekly retraining cycles | ML Team |
| Deployment Failures | Rolling deployment strategy | DevOps Team |
| License Compliance | Legal review of Apache 2.0 terms | Legal Team |

---

## 6. Success Metrics

| Metric | Target | Measurement |
|-------|--------|-------------|
| API Dependency | 0% | System logs analysis |
| Model Accuracy | >92% | QA test suite |
| Deployment Time | <2 hours | DevOps monitoring |
| Training Cost | $5000/month | Cloud billing reports |
| User Satisfaction | 4.5/5 | Internal surveys |

---

## 7. References

| Source | URL | Access |
|-------|-----|--------|
| CEX Quality Gates | Internal Doc #CEX-QG-2026 | Restricted |
| Gemma 4 Model | https://gemma.ai | Public |
| Qwen3 Model | https://qwen.ai | Public |
| Llama License | https://llama.ai | Public |
| DeepSeek-R1 | https://deepseek.com | Public |
| Ollama Docs | https://ollama.ai | Public |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[roadmap_cex]] | related | 0.29 |
| [[p01_ctx_cex_project]] | related | 0.25 |
| [[p01_kc_finetune_config]] | sibling | 0.25 |
| [[spec_vllm_lora_hotswap]] | downstream | 0.25 |
| [[bld_knowledge_card_model_registry]] | sibling | 0.25 |
| [[spec_infinite_bootstrap_loop]] | related | 0.24 |
| [[p03_sp_cex_core_identity]] | downstream | 0.22 |
| [[kc_model_registry]] | sibling | 0.22 |
| [[p01_kc_cex_project_overview]] | sibling | 0.22 |
| [[spec_local_model_per_nucleus]] | downstream | 0.22 |
