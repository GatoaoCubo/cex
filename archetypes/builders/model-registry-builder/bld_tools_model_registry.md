---
kind: tools
id: bld_tools_model_registry
pillar: P04
llm_function: CALL
purpose: Tools available for model_registry production
quality: 8.8
title: "Tools Model Registry"
version: "1.0.0"
author: wave1_builder_gen
tags: [model_registry, builder, tools]
tldr: "Tools available for model_registry production"
domain: "model_registry construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_knowledge_card_model_registry
  - kc_model_registry
  - model-registry-builder
  - bld_architecture_model_registry
  - p03_sp_model_registry_builder
  - bld_instruction_model_registry
  - p10_lr_model_registry_builder
  - model-card-builder
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
---

## CEX Tools (real -- in _tools/)

| Tool | Purpose | When |
| :--- | :--- | :--- |
| cex_compile.py | Compiles artifact .md to .yaml, validates frontmatter | After saving registry entry |
| cex_score.py | Scores artifact quality (D1-D5, 5-dimension) | After compile, before publish |
| cex_retriever.py | TF-IDF similarity search across 2184+ artifacts | Find similar registry entries |
| cex_doctor.py | Health check: frontmatter, schema, pillar placement | Maintenance, CI gate |
| cex_hygiene.py | Artifact CRUD with 8 hygiene rules enforced | Cleanup, deduplication |

## External References (industry standards, not CEX tools)

| Platform | Registry Concept | Key Fields |
| :--- | :--- | :--- |
| MLflow Model Registry | registered_model, model_version, stage, alias | name, version, stage, tags |
| W&B Artifacts | artifact, type, version, aliases (latest/best) | name, type, version, metadata |
| SageMaker Model Registry | model_package, model_package_group, approval_status | ModelPackageGroupName, ModelApprovalStatus |
| Vertex AI Model Registry | model resource, version, evaluation metrics | displayName, versionId, deployedModels |
| HuggingFace Hub | model_id, safetensors, GGUF variants, model card | modelId, sha, tags, cardData |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_model_registry]] | upstream | 0.40 |
| [[kc_model_registry]] | upstream | 0.35 |
| [[model-registry-builder]] | downstream | 0.31 |
| [[bld_architecture_model_registry]] | downstream | 0.29 |
| [[p03_sp_model_registry_builder]] | upstream | 0.29 |
| [[bld_instruction_model_registry]] | upstream | 0.26 |
| [[p10_lr_model_registry_builder]] | downstream | 0.26 |
| [[model-card-builder]] | upstream | 0.24 |
| [[bld_tools_rbac_policy]] | sibling | 0.21 |
| [[bld_tools_usage_quota]] | sibling | 0.21 |
