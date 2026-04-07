---
kind: examples
id: bld_examples_multi_modal_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of multi_modal_config artifacts
pattern: few-shot learning — LLM reads these before producing
updated: "2026-04-07"
domain: "examples artifact construction"
title: "Examples Multi Modal Config"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.94
tldr: "Defines the examples specification for examples multi modal config, with structural rules, validation gates, and integration points."
---

# Examples: multi-modal-config-builder
## Golden Example
INPUT: "Create multi-modal config for document analysis with Claude"
OUTPUT:
```yaml
---
id: p04_mmc_document_analysis
kind: multi_modal_config
pillar: P04
title: "Document Analysis Multi-Modal Config"

version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "multi-modal-config-builder"
supported_modalities: [image, document, text]

image_max_resolution: "2048x2048"
image_format: [png, jpg, webp, gif]
preprocessing: [resize, compress]
routing_model:
  image: claude-sonnet-4-20250514

  document: claude-sonnet-4-20250514
  text: claude-sonnet-4-20250514
token_cost_estimate:
  image_1024: 750
  image_2048: 1500

  document_page: 1200
domain: document_processing
quality: 9.0
tags: [multi_modal_config, document, image, analysis]
tldr: "Document analysis: image+PDF via Claude Sonnet, max 2048px, ~1500 tokens/image, resize preprocessing"
---
```
WHY THIS IS GOLDEN:
1. quality: null
2. supported_modalities explicit
3. Resolution limits set
4. Routing map present
5. Token costs estimated
6. Preprocessing defined

## Anti-Example
BAD OUTPUT:
```yaml
id: modal_cfg
supported_modalities: all
image_max_resolution: unlimited
quality: 8.0
```
FAILURES:
1. id: no p04_mmc_ prefix
2. supported_modalities: "all" not valid — must be explicit list
3. Resolution: "unlimited" burns budget

4. quality: not null
5. No routing, no preprocessing, no token costs

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | examples artifact construction |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |
