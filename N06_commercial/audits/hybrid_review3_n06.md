---
id: hybrid_review3_n06
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Commercial Summary: Wave 2 ML Kinds (N06)"
version: 1.0.0
quality: null
tags: [audit, hybrid_review3, commercial, wave2, ml_kinds, gemma4]
domain: commercial assessment
created: "2026-04-14"
updated: "2026-04-14"
author: n06_commercial
tldr: "7 Wave 2 ML kinds assessed. Top 3 commercial picks: experiment_tracker, model_registry, training_method. 5 TODO placeholder ISOs require fix before demo-ready. No D04 financial contamination found. D01 clear across all 7 system_prompts. Recommended bundles: MLOps Pipeline Pack + Edge Inference Pack."
---

# HYBRID_REVIEW3 Commercial Summary: Wave 2 ML Kinds (N06)

## Executive Summary

- **Quality verdict**: Wave 2 ML kinds are commercially viable but NOT demo-ready. 5 ISOs contain "TODO: Generate content" placeholders. Two builders (training_method, model_architecture) corrected to n05_builder quality -- examples are product-grade. Five builders retain wave1_builder_gen boilerplate.
- **Top 3 kinds for commercial packaging**: experiment_tracker (highest market demand, $4.5B MLOps), model_registry (enterprise compliance anchor), training_method (cleanest examples, broadest audience).
- **Recommended action**: Fix 5 TODO ISOs, patch model_registry golden example typo, bundle into 2 product modules. No rebuild required -- patch is sufficient.

---

## Per-Kind Commercial Assessment

| Kind | Market Fit | Revenue Tier | Example Quality | Demo Ready? | Action |
|------|------------|--------------|-----------------|-------------|--------|
| experiment_tracker | HIGH -- MLflow/W&B replacement | Pro/Enterprise | Good (real transformer study, 3 runs) | NO -- quality_gate is TODO | FIX quality_gate |
| model_registry | HIGH -- enterprise MLOps anchor | Enterprise | Good (versioned lineage + S3 URIs) | NO -- quality_gate + instruction are TODO | FIX 2 ISOs + patch typo |
| training_method | HIGH -- universal ML workflow | Pro | EXCELLENT -- 3 real examples (BERT, MLM, RLHF) | YES -- after quality_gate fix | FIX quality_gate |
| quantization_config | HIGH -- edge inference trend | Pro/Enterprise | Good (bitsandbytes NF4 / QLoRA real spec) | YES | PASS |
| model_architecture | MEDIUM-HIGH -- AI infra specialists | Pro/Enterprise | EXCELLENT -- LLaMA 7B + ViT-B/16 w/ real params | YES -- D04 fixed by n02_hybrid_review3 | PASS |
| agent_computer_interface | MEDIUM -- emerging agentic market | Enterprise | PARTIAL -- JSON-RPC example truncated at error codes | NO -- examples incomplete | FIX examples |
| dataset_card | MEDIUM -- compliance play | Starter/Pro | Adequate -- MovieReview-Clean is synthetic | YES (barely) | MONITOR |

---

## Defect Audit Summary (N06 Commercial Lens)

### Defects Found in Wave 2 ML Kinds

| Defect | Type | Count | Affected Builders | Commercial Impact |
|--------|------|-------|-------------------|-------------------|
| D-TODO | Placeholder content ("TODO: Generate content") | 5 ISOs | training_method (qg), dataset_card (instruction), model_registry (instruction + qg), experiment_tracker (qg) | HIGH -- quality_gate TODO = no scoring possible = demo blocker |
| D-TYPO | model_registry golden example has `202    3-10-12` (space in date) | 1 ISO | model_registry | LOW -- cosmetic but visible in demos |
| D-TRUNC | agent_computer_interface example truncated at error code `-3` | 1 ISO | agent_computer_interface | MEDIUM -- incomplete golden example fails trust test |
| D01 | system_prompt llm_function=INJECT | 0 | -- | CLEAR -- all 7 builders use BECOME |
| D04 | Domain contamination (financial/trading) | 0 active | model_architecture qg was contaminated, FIXED by n02_hybrid_review3 | RESOLVED |
| D05 | density_score hardcoded 0.85 | 5 of 7 | aci, experiment_tracker, quantization_config, model_registry, dataset_card | LOW -- cosmetic, training_method=0.86 and model_architecture=0.88 are measured |

### Author Quality Correlation

| Author | Count | Quality Signal | Examples Quality |
|--------|-------|----------------|-----------------|
| n05_builder | 2 (training_method, model_architecture) | Highest -- deliberate correction | Product-grade (real HW specs, real algo params) |
| n02_hybrid_review3 | 1 (model_architecture qg fixed) | High -- peer review correction | Proper HARD/SOFT gate structure |
| wave1_builder_gen | 5 remaining builders | Baseline -- unreviewed | Mixed -- golden examples adequate, supporting ISOs weak |

---

## Prioritization Matrix

| Priority | Kind | Market Demand | CEX Advantage | Time to Polish | Customer Segment |
|----------|------|---------------|---------------|----------------|-----------------|
| P1 | experiment_tracker | HIGHEST -- MLflow dominates, but CEX YAML structure beats MLflow JSON blobs | Structured multi-run comparison vs. MLflow's messy UI | 1 day (fix quality_gate TODO) | ML engineers, data scientists |
| P2 | model_registry | HIGH -- enterprise MLOps mandatory, compliance driver | Lineage + version tracking in single YAML artifact | 2 days (fix 2 TODOs + typo) | MLOps teams, enterprise AI |
| P3 | training_method | HIGH -- universal, broadest audience | 3 paradigms (supervised/self-supervised/RL) with real HW specs | 0 days (fix quality_gate TODO only) | Any ML practitioner |
| P4 | quantization_config | HIGH -- every LLM deployment needs quantization decision | bitsandbytes NF4/QLoRA is the real spec, not generic | 0 days (pass) | LLM deployment engineers |
| P5 | model_architecture | MEDIUM-HIGH -- foundational for AI infra teams | LLaMA + ViT examples with real GQA/SwiGLU specs | 0 days (pass) | AI researchers, infra teams |
| P6 | agent_computer_interface | MEDIUM -- emerging, MCP protocol adoption accelerating | ACI spec is a CEX-native kind (no MLflow/W&B equivalent) | 1 day (fix truncated examples) | Agent platform engineers |
| P7 | dataset_card | MEDIUM -- HuggingFace dominates, compliance niche remains | Structured YAML vs HuggingFace prose cards | 0 days (pass) | Data teams, compliance officers |

---

## Packaging Opportunities

### Bundle 1: "MLOps Pipeline Pack" (Pro tier, $149/mo)

**Kinds**: training_method + experiment_tracker + model_registry

**Rationale**: Sequential MLOps workflow -- define how to train (training_method), track experiment runs (experiment_tracker), register production artifacts (model_registry). This mirrors the exact MLflow + W&B workflow that $4.5B MLOps market pays for. CEX advantage: single YAML-first format across all 3 vs. MLflow (Python-centric API) and W&B (dashboard-centric).

| Stage | Kind | Output |
|-------|------|--------|
| 1. Training design | training_method | BERT fine-tune spec with HW profile |
| 2. Experiment tracking | experiment_tracker | 3 runs: perplexity, loss, throughput comparison |
| 3. Production registration | model_registry | Versioned artifact with S3 URIs + lineage |

**Upsell path**: MLOps Pipeline Pack -> quantization_config (deploy to edge) -> agent_computer_interface (build agents on top).

### Bundle 2: "Edge Inference Pack" (Pro/Enterprise, $199/mo)

**Kinds**: quantization_config + model_architecture

**Rationale**: Every team deploying LLMs to production faces the same two decisions: (1) what architecture are we deploying? (2) how do we compress it for inference cost? CEX bundles both into a single configuration workflow. Competitors (MLflow, W&B) have NO equivalent -- this is a CEX-native product advantage.

| Stage | Kind | Output |
|-------|------|--------|
| 1. Define architecture | model_architecture | LLaMA 7B spec with parameter distribution |
| 2. Configure compression | quantization_config | NF4 4-bit config with bfloat16 compute dtype |

**Upsell path**: Edge Inference Pack -> model_registry (register quantized artifacts) -> experiment_tracker (benchmark full vs. quantized).

### Bundle 3: "Agentic Infrastructure Pack" (Enterprise, $399/mo)

**Kinds**: agent_computer_interface + model_architecture + model_registry

**Rationale**: Enterprises building AI agents need three things: the model spec (what runs), the registry (where it lives), and the ACI contract (how agents call it). No incumbent covers all three as a unified spec format. MCP adoption is accelerating (Anthropic protocol), and CEX's ACI builder is the first structured YAML spec for agent-computer interfaces.

**Status**: PENDING -- agent_computer_interface examples need fix before this bundle is demo-ready.

---

## Quality Audit Aggregate (Wave 2 ML Kinds)

> Note: N01-N05 HYBRID_REVIEW3 audit reports not yet committed at time of this assessment.
> This section uses direct builder inspection + master_systemic_defects.md for baseline.

| Dimension | Score | Evidence |
|-----------|-------|---------|
| D01 (system_prompt BECOME) | PASS 7/7 | All 7 system_prompts use llm_function: BECOME |
| D04 (domain contamination) | PASS 7/7 | model_architecture qg fixed by n02_hybrid_review3 |
| D05 (density_score measured) | PARTIAL 2/7 | training_method=0.86, model_architecture=0.88 measured; 5 others hardcoded 0.85 |
| TODO placeholders | FAIL 5 ISOs | quality_gate (3x), instruction (2x) -- blocks quality scoring |
| Example quality | PASS 7/7 | All golden examples are domain-correct (no synthetic ACME/John Smith) |
| Example completeness | PARTIAL 6/7 | agent_computer_interface truncated at error code -3 |
| Real tool coverage | PASS 7/7 | bitsandbytes NF4, BERT, A100, GQA, MCP, JSON-RPC all real |
| Financial contamination | PASS 7/7 | No FIFO, Pro-Rata, backtest, CCXT found |

**Aggregate defect count**: 6 ISOs require fixes (5 TODO + 1 truncated). 0 require rebuild.

---

## Recommended Next Wave (Maximum Commercial ROI)

After fixing Wave 2 ML kinds, the highest commercial value gap in CEX is:

| Kind | Gap | Market | CEX Fit | Priority |
|------|-----|--------|---------|----------|
| finetune_config | Missing -- LoRA/QLoRA parameters not in CEX | LoRA is the dominant fine-tuning paradigm (PEFT library, 50K+ HuggingFace models) | P02, natural complement to training_method | CRITICAL |
| inference_config | Missing -- KV cache, speculative decoding, batching strategy | Every LLM deployment team needs this; vLLM/TGI configs are complex | P09, natural pair to quantization_config | HIGH |
| model_card | Missing -- ethical/capability documentation (distinct from model_registry) | EU AI Act requires model cards for high-risk AI | P08, dataset_card companion | HIGH |
| data_pipeline | Missing -- ETL from raw data to training-ready format | Every training_method needs a data pipeline upstream | P01, MLOps Pack extension | MEDIUM |

**Rationale**: finetune_config is the single highest-ROI kind to build next. The fine-tuning market (LoRA/QLoRA) is at peak adoption. CEX has training_method + experiment_tracker + model_registry but no LoRA parameters kind -- a gap that breaks the MLOps Pipeline Pack's completeness story.

---

## Competitive Benchmarking

| Incumbent | Strength | CEX Advantage |
|-----------|----------|--------------|
| MLflow | Experiment tracking, model registry | CEX: YAML-first single format; MLflow is Python API + UI heavy |
| Weights & Biases | Experiment visualization, team collaboration | CEX: structured artifact output vs W&B's visual dashboards (no export schema) |
| HuggingFace Hub | Dataset cards, model cards | CEX: machine-readable YAML schema vs HuggingFace's prose markdown |
| Hugging Face PEFT | LoRA/QLoRA training | CEX: finetune_config kind (MISSING -- see next wave) |
| BitsAndBytes | Quantization library | CEX: quantization_config wraps the decision layer (which method, which bits) not the library |

**Market opportunity**: $4.5B MLOps market (2024), CAGR 36%. CEX targets the spec/configuration layer above tools, not the tools themselves. This is a 10x less competitive position than building another MLflow.
