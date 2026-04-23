---
kind: quality_gate
id: p11_qg_model_registry
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for model_registry
quality: 9.1
title: "Quality Gate: Model Registry"
version: "1.0.0"
author: n04_audit_hybrid_review3
tags: [model_registry, builder, quality_gate, governance, mlops]
tldr: "Gates ensuring model_registry artifacts contain quantitative metrics, artifact URIs, lineage refs, and deployment stage per MLflow/W&B standards."
domain: "model registry quality assurance"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_instruction_model_registry
  - p11_qg_agent_computer_interface
  - p11_qg_knowledge_card
  - p02_qg_training_method
  - p11_qg_handoff
  - p11_qg_input_schema
  - p11_qg_quality_gate
  - p11_qg_creation_artifacts
  - p11_qg_model_architecture
  - p11_qg_agent_package
---

## Quality Gate

# Gate: Model Registry

## Definition

| Field | Value |
|-------|-------|
| metric | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.0 for reference |
| operator | AND (all hard) + weighted average (soft) |
| scope | any artifact with `kind: model_registry` |

## HARD Gates

All must pass. Any failure = immediate reject.

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | `id` matches `^p10_mr_[a-z][a-z0-9_]+$` | Wrong prefix, uppercase, or non-alphanumeric |
| H03 | `id` equals filename stem | Mismatch between id field and file name |
| H04 | `kind == model_registry` | Any other kind value |
| H05 | `quality == null` | Any non-null value (self-scoring violation) |
| H06 | `pillar == P10` | Wrong pillar assignment |
| H07 | `model_type` is one of: LLM, CNN, Classifier, Embedding, Diffusion, Multimodal, Other | Missing or unrecognized type |
| H08 | `framework` is non-empty | Missing framework (PyTorch, JAX, ONNX, etc.) |
| H09 | At least one quantitative eval metric present (number + unit in body) | Metrics section absent or purely qualitative |
| H10 | At least one artifact URI present (weights, config, or tokenizer path) | No artifact storage reference |
| H11 | `deployment_stage` is one of: Experimental, Staging, Production, Archived | Missing or non-standard stage |
| H12 | Lineage field present: `base_model` or `parent_version` | No provenance anchor |
| H13 | File size <= 4096 bytes | Exceeds max_bytes limit |
| H14 | File size >= 200 bytes | Stub entry -- insufficient content |

## SOFT Scoring

Total weights sum to 100%.

| ID | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|----|-----------|--------|--------|-------|-------|
| S01 | Metric concreteness | 1.5 | >= 2 quantitative metrics with benchmark source named | 1 metric, no source | Metrics absent or purely qualitative |
| S02 | Lineage completeness | 1.5 | base_model + training_dataset + git_sha all present | 2 of 3 present | Only 1 or none |
| S03 | Artifact URI completeness | 1.0 | Weights + config + tokenizer URIs all present | 2 of 3 present | Only 1 or none |
| S04 | Lifecycle history | 1.0 | Transition history documented (date + stage + approver) | Stage present but no history | Stage absent |
| S05 | Deployment information | 1.0 | Serving endpoint + inference config + container image | Endpoint only | No deployment info |
| S06 | Domain accuracy | 1.0 | ML model registry (LLM/CV/NLP) -- not financial or generic catalog | Minor scope ambiguity | Financial model or wrong domain |
| S07 | Structured format | 0.5 | >= 3 tables in body (metrics, URIs, lineage) | 1-2 tables | Prose-only body |
| S08 | tldr precision | 0.5 | tldr names model + version + task concretely | Vague description | Absent or generic |

**Score = sum(pts x weight) / sum(max_pts x weight) x 10**

## Actions

| Score | Tier | Action |
|-------|------|--------|
| >= 9.0 | Reference | Publish as authoritative registry entry |
| >= 8.0 | Skilled | Publish + log versioning pattern |
| >= 7.0 | Learning | Publish but flag for metric/lineage enrichment |
| < 7.0 | Rejected | Return with gate report: list failed gates |

## Common Failure Modes

| Defect | Gate | Fix |
|--------|------|-----|
| Financial portfolio models contaminating ML registry | S06 | Replace with LLM/CV/NLP examples |
| Metrics section qualitative only ("performs well") | H09, S01 | Add F1/accuracy/latency with benchmark source |
| Missing artifact URIs | H10, S03 | Add S3/GCS/HuggingFace Hub paths |
| Deployment stage absent | H11 | Set to Experimental/Staging/Production/Archived |
| No base_model reference | H12, S02 | Add lineage anchor (parent model name + version) |

## Bypass

| Field | Value |
|-------|-------|
| Conditions | Proprietary model where artifact URIs cannot be disclosed (security requirement) |
| Approver | N05 Operations nucleus + N07 orchestrator sign-off |
| Required | Redact URIs with placeholder pattern: `[REDACTED:s3://internal/...]` |

## Examples

## Golden Example
---
kind: model_registry
id: transformer-encoder-xl
version: "2.4.0"
status: production
lifecycle:
  stage: active
  deprecated: false
  last_updated: 2023-10-12
lineage:
  base_model: "transformer-base-v1"
  parent_version: "2.3.9"
  training_pipeline: "pipeline-nlp-v4"
artifacts:
  - type: weights
    uri: "s3://models/transformer-xl/v2.4.0/weights.bin"
  - type: configuration
    uri: "s3://models/transformer-xl/v2.4.0/config.json"
  - type: tokenizer
    uri: "s3://models/transformer-xl/v2.4.0/tokenizer.model"
tags:
  - architecture: transformer
  - task: sequence-classification
  - compute_tier: high
---
Registry entry for the production-grade XL encoder. This version includes updated attention heads for long-context support.

## Anti-Example 1: Confusion with Model Card
---
kind: model_card
id: transformer-encoder-xl
description: A large scale transformer model for text classification.
intended_use: Natural language understanding tasks.
limitations: High memory footprint; not suitable for edge devices.
accuracy_metrics:
  f1_score: 0.92
  precision: 0.91
---
Detailed documentation regarding the model's capabilities and ethical considerations.

## Why it fails
This is a **model_card**, not a **model_registry**. It focuses on the qualitative specification, usage instructions, and performance metrics of a single model instance rather than the versioned artifact tracking, lineage, and URI pointers required for a registry.

## Anti-2: Confusion with Checkpoint
---
kind: checkpoint
id: transformer-encoder-xl-run-882
epoch: 45
loss: 0.0234
learning_rate: 0.00005
optimizer: AdamW
batch_size: 32
gradients: "s3://training-logs/run-882/grads.pt"
---
A snapshot of the model weights at the end of epoch 45 during the training process.

## Why it fails
This is a **checkpoint**, not a **model_registry**. It describes a specific point-in-time training state (hyperparameters, loss, and epoch) rather than a managed, versioned asset intended for deployment and lineage tracking in a production environment.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
