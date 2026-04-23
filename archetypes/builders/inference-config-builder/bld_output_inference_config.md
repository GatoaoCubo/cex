---
kind: output_template
id: bld_output_inference_config
pillar: P05
llm_function: PRODUCE
purpose: Template for producing an inference_config artifact
quality: null
title: "Inference Config Builder - Output ISO"
version: "1.0.0"
author: n03_builder
tags: [inference_config, builder, output]
tldr: "Output template for inference config artifacts."
domain: "model inference"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_inference_config
---

# Output Template: inference_config

```yaml
id: p09_ic_{{config_slug}}
kind: inference_config
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
model_id: "{{model_identifier}}"
framework: "{{vllm_or_tgi_or_ollama_or_tensorrt}}"
quantization: "{{fp16_or_int8_or_int4_or_gguf}}"
batch_strategy: "{{continuous_or_static_or_dynamic}}"
max_concurrent: {{integer}}
vram_budget_gb: {{float}}
domain: "{{domain_value}}"
quality: null
tags: [inference, {{framework_tag}}, {{model_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Framework
`{{serving_framework_version_config}}`

## Quantization
`{{quantization_level_format_quality_impact}}`

## Batching
`{{strategy_concurrency_queue_depth}}`

## Hardware
`{{gpu_model_vram_cpu_ram_fallback}}`

## Performance Targets
`{{ttft_tokens_sec_p99_latency}}`
