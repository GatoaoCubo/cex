---
id: n00_quantization_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Quantization Config -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, quantization_config, p09, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A quantization_config defines model quantization and compression settings for local model inference: bit depth, quantization method, layer-specific overrides, and quality/speed trade-off targets. It enables CEX's local model grid (Ollama, llama.cpp) to run efficiently on available GPU/CPU hardware while maintaining acceptable output quality.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `quantization_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| model | string | yes | Base model identifier (e.g. llama3.1:8b) |
| method | enum | yes | gguf \| awq \| gptq \| bnb \| ollama_default |
| bits | integer | yes | Quantization bit depth (4, 5, 6, 8, 16) |
| gpu_layers | integer | no | Number of layers to offload to GPU (0=CPU only) |
| context_size | integer | no | Context window size for this quantized model |
| threads | integer | no | CPU threads for inference |
| quality_benchmark | float | no | Expected quality score relative to FP16 (0-1) |

## When to use
- Configuring Ollama model settings for the free local grid
- Optimizing model memory usage on the RTX 5070 Ti GPU
- Documenting the quantization trade-offs for a given model in the benchmark log

## Builder
`archetypes/builders/quantization_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind quantization_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: quant_qwen3_14b_q4
kind: quantization_config
pillar: P09
nucleus: n05
title: "qwen3:14b Q4_K_M Config"
version: 1.0
quality: null
---
model: qwen3:14b
method: gguf
bits: 4
gpu_layers: 35
context_size: 32768
threads: 8
quality_benchmark: 0.92
```

## Related kinds
- `kubernetes_ai_requirement` (P09) -- K8s GPU requirements align with quantization memory needs
- `effort_profile` (P09) -- effort profiles select between quantized (fast) and full (thorough) models
- `env_config` (P09) -- Ollama environment variables control quantization loading
