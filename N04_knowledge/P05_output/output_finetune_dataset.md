---
id: p10_out_finetune_dataset
kind: output
8f: F6_produce
pillar: P10
title: "Output: Fine-Tune Dataset"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [output, n04, fine-tuning, jsonl, ml, dataset, training]
tldr: "JSONL export for LLM fine-tuning: instruction/input/output triples from KCs."
density_score: 0.92
related:
  - p06_schema_export_format
  - n04_agent_knowledge
  - p01_kc_fine_tuning_dataset_preparation
  - p01_kc_instruction
  - p01_kc_few_shot_example
  - bld_knowledge_card_instruction
  - p01_kc_prompt_engineering_best_practices
  - instruction-builder
  - p01_fse_{{TOPIC_SLUG}}
  - tpl_instruction
---

# Output: Fine-Tune Dataset

## Format: JSONL
```json
{"instruction": "Explain chain-of-thought prompting for LLM agents", "input": "", "output": "Chain-of-Thought (CoT) elicits intermediate reasoning steps from LLMs..."}
{"instruction": "What is the self-healing pattern in agent systems?", "input": "", "output": "Self-healing: generate → validate → [fail] → diagnose → fix → retry..."}
{"instruction": "When should you use RAG vs fine-tuning?", "input": "I have 200 domain-specific documents", "output": "RAG for dynamic data that changes. Fine-tuning for stable patterns..."}
```

## Generation Rules
- instruction: derived from KC `tldr` or `when_to_use`, phrased as question
- input: optional context from `keywords`
- output: compressed body (max 500 tokens)
- Filter: only KCs with density >= 0.85 and quality >= 8.0
- Dedup: no two entries with >80% output overlap

## Usage Guidelines

| When to use | When NOT to use |
|-------------|-----------------|
| Stable domain knowledge (patterns don't change) | Dynamic/frequently updated information |
| Need consistent formatting/style across responses | Small datasets (<100 examples) |
| Target model will be used repeatedly | One-off tasks |
| Have 500+ high-quality KC examples | Factual Q&A (use RAG instead) |

**Anti-patterns:**
- Including low-quality KCs (quality <8.0) dilutes training signal
- Duplicate instructions with minor variations (confuses model)
- Overly long outputs (>500 tokens) → truncation issues
- Missing instruction diversity → overfitting to question patterns

## Metadata Header
```json
{"_meta": {"source": "CEX P01_knowledge", "kc_count": 243, "generated": "2026-03-31", "avg_quality": 8.9}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_export_format]] | upstream | 0.23 |
| [[n04_agent_knowledge]] | upstream | 0.21 |
| [[p01_kc_fine_tuning_dataset_preparation]] | upstream | 0.20 |
| [[p01_kc_instruction]] | upstream | 0.20 |
| [[p01_kc_few_shot_example]] | upstream | 0.20 |
| [[bld_knowledge_card_instruction]] | upstream | 0.20 |
| [[p01_kc_prompt_engineering_best_practices]] | upstream | 0.19 |
| [[instruction-builder]] | upstream | 0.19 |
| [[p01_fse_{{TOPIC_SLUG}}]] | upstream | 0.19 |
| [[tpl_instruction]] | upstream | 0.19 |
