---
kind: tools
id: bld_tools_finetune_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for finetune_config production
quality: 9.2
title: "Tools Finetune Config"
version: "1.0.0"
author: n03_builder
tags: [finetune_config, builder, tools, P02]
tldr: "Tools for finetune_config production: schema refs, framework docs, VRAM calculator, duplicate check."
domain: "finetune_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_tools_memory_scope
  - bld_tools_retriever_config
  - bld_tools_handoff_protocol
  - bld_tools_cli_tool
  - bld_tools_path_config
  - bld_tools_prompt_version
  - bld_tools_chunk_strategy
  - bld_tools_runtime_rule
  - bld_tools_output_validator
  - bld_tools_constraint_spec
---

# Tools: finetune-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing finetune_config artifacts for duplicates | Phase 1 (check duplicates) | CONDITIONAL |
| cex_retriever.py | TF-IDF similarity search over compiled artifacts | Phase 1 (find similar configs) | AVAILABLE |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | PLANNED |
| cex_compile.py | Compile .md to .yaml | Phase 3 (F8) | AVAILABLE |
| cex_score.py | Score artifact quality | Phase 3 (F7) | AVAILABLE |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | Field definitions, finetune_config kind |
| CEX Examples | P02_model/examples/ | Real finetune_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_finetune_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position |
| HuggingFace Hub | huggingface.co/models | Base model metadata, parameter counts, licenses |
| TRL Docs | huggingface.co/docs/trl | SFTTrainer, DPOTrainer default hyperparameters |
| Axolotl Docs | github.com/axolotl-ai-cloud/axolotl | YAML config schema reference |
| Unsloth Docs | github.com/unslothai/unsloth | QLoRA notebook baselines |

## VRAM Estimation Guide
| Scenario | Model | Quantization | VRAM |
|----------|-------|-------------|------|
| QLoRA 4-bit | 7B | NF4 | ~8-10 GB |
| QLoRA 4-bit | 13B | NF4 | ~14-16 GB |
| QLoRA 4-bit | 70B | NF4 | ~48-56 GB |
| LoRA bf16 | 7B | none | ~28-32 GB |
| Full fine-tune | 7B | none | ~56-80 GB |
Note: values are training-time estimates with gradient checkpointing enabled.

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, adapter_type from enum,
all required hyperparameters have values, body <= 4096 bytes, quality == null.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_finetune_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_tools_finetune_config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_scope]] | sibling | 0.59 |
| [[bld_tools_retriever_config]] | sibling | 0.58 |
| [[bld_tools_handoff_protocol]] | sibling | 0.57 |
| [[bld_tools_cli_tool]] | sibling | 0.56 |
| [[bld_tools_path_config]] | sibling | 0.56 |
| [[bld_tools_prompt_version]] | sibling | 0.56 |
| [[bld_tools_chunk_strategy]] | sibling | 0.54 |
| [[bld_tools_runtime_rule]] | sibling | 0.54 |
| [[bld_tools_output_validator]] | sibling | 0.54 |
| [[bld_tools_constraint_spec]] | sibling | 0.54 |
