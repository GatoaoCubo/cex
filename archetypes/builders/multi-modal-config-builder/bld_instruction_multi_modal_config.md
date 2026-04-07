---
kind: instruction
id: bld_instruction_multi_modal_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for multi_modal_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Multi Modal Config"
version: "1.0.0"
author: n03_builder
tags: [multi_modal_config, builder, examples]
tldr: "Golden and anti-examples for multi modal config construction, demonstrating ideal structure and common pitfalls."
domain: "multi modal config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a multi_modal_config
## Phase 1: RESEARCH
1. Identify target use case: what non-text inputs need processing?
2. Determine supported modalities: image, audio, video, document?
3. Survey target model capabilities: which models handle which modalities natively?
4. Assess volume/cost: how many images per request? Audio duration?
5. Check existing configs to avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template
3. Define supported_modalities list
4. Set per-modality constraints: image resolution, audio duration, video duration
5. Define preprocessing pipeline per modality (resize, compress, transcribe)
6. Create routing_model map: modality → best model
7. Estimate token costs per modality
8. Define fallback chain for unsupported modalities
9. Set quality: null
10. Keep file under 2048 bytes
## Phase 3: VALIDATE
1. Verify supported_modalities contains valid enum values
2. Check format constraints present for each modality
3. Verify routing_model maps to real models
4. Check token_cost_estimate is populated
5. Verify id matches `p04_mmc_[a-z][a-z0-9_]+`
6. Check total file under 2048 bytes
7. If any gate fails: fix and re-validate

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify multi
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | multi modal config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
