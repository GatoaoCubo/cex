---
id: p10_out_finetune_dataset
kind: output
pillar: P10
title: "Output: Fine-Tune Dataset"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 8.6
tags: [output, n04, fine-tuning, jsonl, ml, dataset, training]
tldr: "JSONL export for LLM fine-tuning: instruction/input/output triples from KCs."
density_score: 0.92
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

## Metadata Header
```json
{"_meta": {"source": "CEX P01_knowledge", "kc_count": 243, "generated": "2026-03-31", "avg_quality": 8.9}}
```
