---
kind: instruction
id: bld_instruction_model_registry
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for model_registry
pattern: 3-phase pipeline (gather -> register -> validate)
quality: 9.0
title: "Instruction Model Registry"
version: "1.0.0"
author: n04_audit_hybrid_review3
tags: [model_registry, builder, instruction]
tldr: "Step-by-step instructions for producing a model_registry artifact covering provenance, versioning, lineage, and lifecycle stage."
domain: "model registry construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
---

# Instructions: How to Produce a model_registry

## Phase 1: GATHER

1. Identify the model to register: what artifact is being tracked (LLM, classifier, embedding model)?
2. Collect provenance data:
   - Base model (e.g., `llama-3-8b`, `bert-base-uncased`)
   - Training dataset URI or hash (for reproducibility)
   - Training pipeline reference (Git SHA, run ID, pipeline version)
3. Gather evaluation metrics: accuracy, F1, BLEU, ROUGE, latency p50/p99 — minimum one quantitative metric
4. Determine deployment stage: Experimental, Staging, Production, Archived (MLflow convention)
5. Locate artifact URIs: weights path, config path, tokenizer path (S3, GCS, Azure Blob, HuggingFace Hub)
6. Check for an existing registry entry for the same model — are you creating a new version or a new model?

## Phase 2: REGISTER

1. Read `bld_schema_model_registry.md` — source of truth for all frontmatter fields
2. Read `bld_output_template_model_registry.md` — fill exactly, following schema constraints
3. Fill required frontmatter:
   - `id`: unique identifier following pattern `p10_mr_{model_name}_{version}`
   - `kind`: `model_registry` (literal, no variation)
   - `pillar`: `P10`
   - `version`: SemVer string (e.g., `2.4.1`) or immutable hash
   - `quality`: `null` — never self-score
   - `model_type`: LLM | CNN | Classifier | Embedding | Diffusion | Other
   - `framework`: PyTorch | JAX | TensorFlow | ONNX | Safetensors
4. Fill body sections:
   - **Model Metadata**: base_model, training_data, training_pipeline_ref, compute_tier
   - **Performance Metrics**: at least one quantitative benchmark with source
   - **Artifact URIs**: weights, config, tokenizer — each with full URI
   - **Lineage**: parent_version, git_sha, dataset_hash
   - **Lifecycle Stage**: current stage + transition history
   - **Deployment Information**: serving endpoint, inference config, container image
5. Use tables for metrics, URIs, and lineage — prefer structured data over prose
6. Reference the base model's existing registry entry if one exists

## Phase 3: VALIDATE

1. Run `python _tools/cex_compile.py <file>` after saving
2. Run `python _tools/cex_doctor.py` to check registry integrity
3. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - `id` matches pattern `p10_mr_[a-z][a-z0-9_]+`
   - `kind == model_registry`
   - `quality == null`
   - At least one quantitative metric present (number with unit)
   - At least one artifact URI present (weights path)
   - Lineage field present (base_model or parent_version)
   - `deployment_stage` is one of: Experimental, Staging, Production, Archived
   - Body >= 200 bytes, <= 4096 bytes
4. SOFT gates:
   - `tldr` captures model identity concretely (name + version + task)
   - Training data lineage traceable (dataset URI or hash present)
   - Lifecycle transition history documented if version > 1.0.0
   - Framework and model_type filled — no generic strings
5. Boundary checks:
   - Is this a registry entry (versioned artifact)? Or a model card (qualitative spec)?
   - Is this tracking deployment provenance? Or raw training checkpoints?
   - Are metrics from actual evaluation runs, not from the base model's paper?
6. If HARD gate fails: fix immediately, recompile, re-validate
7. If score < 8.0: expand thin sections, add quantitative metrics, replace prose with tables
