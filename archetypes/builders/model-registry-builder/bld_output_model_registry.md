---
kind: output_template
id: bld_output_template_model_registry
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for model_registry production
quality: 9.1
title: "Output Template Model Registry"
version: "1.0.0"
author: wave1_builder_gen
tags: [model_registry, builder, output_template]
tldr: "Template with vars for model_registry production"
domain: "model_registry construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_instruction_model_registry
  - p11_qg_model_registry
  - bld_knowledge_card_model_registry
  - kc_model_registry
  - bld_collaboration_model_registry
  - bld_schema_model_registry
  - model-registry-builder
  - bld_examples_model_registry
  - p03_sp_model_registry_builder
  - bld_architecture_model_registry
---

```yaml
id: p10_mr_{{model_name_slug}}_{{version_slug}}
# Example: p10_mr_llama3_8b_v1_0_0
kind: model_registry
pillar: P10
title: "{{Model Display Name}} v{{version}}"
version: "{{version}}"
# SemVer string: e.g., "2.4.1" or immutable hash: "sha256:abc123..."
model_type: "{{LLM|CNN|Classifier|Embedding|Diffusion|Multimodal|Other}}"
framework: "{{PyTorch|JAX|TensorFlow|ONNX|Safetensors}}"
deployment_stage: "{{Experimental|Staging|Production|Archived}}"
quality: null
tags: []
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
tldr: "{{model_name}} v{{version}} -- {{task description, e.g., instruction-tuned LLM for Portuguese QA}} registered at {{stage}}"
```

# {{Model Display Name}} v{{version}}

## Model Metadata

| Field | Value |
| :--- | :--- |
| base_model | {{parent model: e.g., meta-llama/Llama-3-8B}} |
| training_data | {{dataset name + URI: e.g., HuggingFace datasets/dolly-15k}} |
| training_pipeline | {{pipeline name + git_sha: e.g., pipeline-nlp-v4 @ abc1234}} |
| compute_tier | {{GPU hours / instance type: e.g., 4x A100 80GB, 12h}} |
| parameter_count | {{e.g., 8B, 70B, 405B}} |

## Performance Metrics

| Metric | Value | Benchmark | Source |
| :--- | :--- | :--- | :--- |
| {{e.g., F1}} | {{e.g., 0.923}} | {{e.g., SQuAD 2.0}} | {{e.g., eval run 2024-01-15}} |
| {{e.g., latency p50}} | {{e.g., 42ms}} | {{e.g., internal load test}} | {{e.g., N05 eval report}} |

## Artifact URIs

| Type | URI |
| :--- | :--- |
| weights | {{e.g., s3://models/llama3-8b/v1.0.0/weights.safetensors}} |
| config | {{e.g., s3://models/llama3-8b/v1.0.0/config.json}} |
| tokenizer | {{e.g., s3://models/llama3-8b/v1.0.0/tokenizer.model}} |

## Lineage

| Field | Value |
| :--- | :--- |
| base_model | {{e.g., meta-llama/Llama-3-8B @ sha256:abc...}} |
| parent_version | {{e.g., p10_mr_llama3_8b_v0_9_0 -- or "none" for first version}} |
| dataset_hash | {{e.g., sha256:def456...}} |
| git_sha | {{training repo commit: e.g., abc1234}} |

## Deployment Information

| Field | Value |
| :--- | :--- |
| serving_endpoint | {{e.g., https://api.internal/models/llama3-8b/v1 -- or N/A}} |
| container_image | {{e.g., registry.internal/llama3-8b:v1.0.0 -- or N/A}} |
| inference_config | {{e.g., max_tokens=2048, temperature=0.7, quantization=int8}} |

## Lifecycle History

| Date | Stage | Approver | Notes |
| :--- | :--- | :--- | :--- |
| {{YYYY-MM-DD}} | Experimental | {{nucleus or person}} | {{e.g., initial registration}} |
| {{YYYY-MM-DD}} | Staging | {{e.g., N05 Operations}} | {{e.g., passed eval gate H09-H14}} |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_model_registry]] | upstream | 0.41 |
| [[p11_qg_model_registry]] | downstream | 0.33 |
| [[bld_knowledge_card_model_registry]] | upstream | 0.27 |
| [[kc_model_registry]] | upstream | 0.24 |
| [[bld_collaboration_model_registry]] | downstream | 0.24 |
| [[bld_schema_model_registry]] | downstream | 0.23 |
| [[model-registry-builder]] | downstream | 0.23 |
| [[bld_examples_model_registry]] | downstream | 0.20 |
| [[p03_sp_model_registry_builder]] | upstream | 0.20 |
| [[bld_architecture_model_registry]] | downstream | 0.20 |
