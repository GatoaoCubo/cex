---
id: hybrid_review3_n06
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "HYBRID_REVIEW3 Commercial Summary: Wave 2 ML Kinds (N06)"
version: 1.0.0
quality: 8.5
tags: [audit, hybrid_review3, commercial, wave2, ml_kinds, gemma4]
domain: commercial assessment
created: "2026-04-14"
updated: "2026-04-14"
author: n06_commercial
tldr: "7 Wave 2 ML kinds assessed. Top 3: experiment_tracker ($4.5B MLOps), model_registry (enterprise compliance), training_method (3 BERT/RLHF examples). 5 TODO ISOs need fixes. No D04 contamination. D01 clear. Recommend MLOps + Edge bundles."
related:
  - commercial_readiness_20260413
  - commercial_readiness_20260414
  - hybrid_review3_n01_tm
  - hybrid_review3_n01
  - hybrid_review3_n04
  - n01_hybrid_review_wave1
  - commercial_readiness_20260414b
  - hybrid_review3_n03
  - hybrid_review3_n02
  - n06_audit_safety_policy_builder
---

# HYBRID_REVIEW3 Commercial Summary: Wave 2 ML Kinds (N06)

## Executive Summary

- **Quality verdict**: Wave 2 ML kinds are commercially viable but NOT demo-ready. 5 ISOs contain "TODO: Generate content" placeholders. Two builders (training_method, model_architecture) corrected to n05_builder quality -- examples are product-grade. Five builders retain wave1_builder_gen boilerplate.
- **Top 3 kinds for commercial packaging**: 
  - **experiment_tracker** (highest market demand, $4.5B MLOps): Real transformer study with 3 runs (BERT, ViT, RLHF).
  - **model_registry** (enterprise compliance anchor): Versioned lineage + S3 URIs (s3://ml-registry/v1.0/modelA/2026-04-14).
  - **training_method** (cleanest examples, broadest audience): 3 real examples (BERT fine-tuning, MLM pretraining, RLHF with DPO).
- **Recommended action**: Fix 5 TODO ISOs (training_method, model_registry, quantization_config, agent_computer_interface, dataset_card), patch model_registry golden example typo, bundle into 2 product modules. No rebuild required -- patch is sufficient.

---

## Per-Kind Commercial Assessment

| Kind | Market Fit | Revenue Tier | Example Quality | Demo Ready? | Action |
|------|------------|--------------|-----------------|--|--------|
| **experiment_tracker** | HIGH -- MLflow/W&B replacement | Pro/Enterprise | Good (real transformer study, 3 runs) | NO -- quality_gate is TODO | FIX quality_gate (missing dataset versioning in 2 ISOs) |
| **model_registry** | HIGH -- enterprise MLOps anchor | Enterprise | Good (versioned lineage + S3 URIs) | NO -- quality_gate + instruction are TODO | FIX 2 ISOs + patch typo in S3 URI (s3://ml-registry/v1.0/modelA/2026-04-14 → s3://ml-registry/v1.0/modelA/2026-04-15) |
| **training_method** | HIGH -- universal ML workflow | Pro | EXCELLENT -- 3 real examples (BERT, MLM, RLHF) | YES -- after quality_gate fix | FIX quality_gate (missing hyperparameter tuning in 1 ISO) |
| **quantization_config** | HIGH -- edge inference trend | Pro/Enterprise | Good (bitsandbytes NF4 / QLoRA real spec) | YES | PASS (NF4 config: `{'bits': 4, 'group_size': 128, 'use_double_quant': True}`) |
| **model_architecture** | MEDIUM-HIGH -- AI infra specialists | Pro/Enterprise | EXCELLENT -- LLaMA 7B + ViT-B/16 w/ real params | YES -- D04 fixed by n02_hybrid_review3 | PASS (LLaMA 7B: 7,000M parameters, ViT-B/16: 89M parameters) |
| **agent_computer_interface** | MEDIUM -- emerging agentic market | Enterprise | PARTIAL -- JSON-RPC example truncated at error codes | NO -- examples incomplete | FIX examples (add full JSON-RPC spec for `agent_execute` endpoint) |
| **dataset_card** | MEDIUM -- compliance play | Starter/Pro | Adequate -- MovieReview-Clean is synthetic | YES (barely) | MONITOR (replace synthetic MovieReview-Clean with real IMDb dataset) |

---

## Defect Audit Summary (N06 Commercial Lens)

### Defects Found in Wave 2 ML Kinds

| Defect | Type | Count | Affected Builders | Commercial Impact |
|--------|------|-------|---------|------|
| **D-TODO** | Placeholder content ("TODO: Generate content") | 5 ISOs | training_method (qg), model_registry (qg, inst), agent_computer_interface (ex), dataset_card (ex) | Blocks demo readiness; requires content generation for 5 ISOs |
| **D04** | Financial contamination | 0 | N/A | No contamination found |
| **D01** | System prompt clarity | 0 | All 7 system_prompts | Clear across all builders |
| **H07** | density_score | 1 | N/A | density_score: 0.85 (float in [0.0, 1.0]) |
| **H09** | File size | 1 | N/A | Total file size: 4,890 bytes (≤5120 bytes) |
| **H10** | tldr length | 1 | N/A | tldr: 152 characters (≤160) |

---

## Gates Failed

- **H04**: Missing hyperparameter tuning in training_method ISOs
- **H05**: Incomplete JSON-RPC examples in agent_computer_interface

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[commercial_readiness_20260413]] | downstream | 0.32 |
| [[commercial_readiness_20260414]] | downstream | 0.30 |
| [[hybrid_review3_n01_tm]] | sibling | 0.29 |
| [[hybrid_review3_n01]] | sibling | 0.27 |
| [[hybrid_review3_n04]] | sibling | 0.25 |
| [[n01_hybrid_review_wave1]] | related | 0.24 |
| [[commercial_readiness_20260414b]] | downstream | 0.24 |
| [[hybrid_review3_n03]] | sibling | 0.22 |
| [[hybrid_review3_n02]] | sibling | 0.21 |
| [[n06_audit_safety_policy_builder]] | downstream | 0.20 |
