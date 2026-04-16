---
kind: tools
id: bld_tools_dataset_card
pillar: P04
llm_function: CALL
purpose: Real CEX tools available for dataset_card production
quality: 9.0
title: "Tools Dataset Card"
version: "1.1.0"
author: n03_hybrid_review3
tags: [dataset_card, builder, tools]
tldr: "Real CEX tools (verified in _tools/) + industry-standard external references"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
---

## Production Tools (real, present in `_tools/`)
| Tool | Purpose | When |
| :--- | :--- | :--- |
| cex_compile.py | Compile .md -> .yaml artifact | After F6 save |
| cex_score.py | Peer-review scoring (5D) | F7 GOVERN |
| cex_retriever.py | TF-IDF similarity over 2184 artifacts | F3 INJECT (find similar dataset_cards) |
| cex_doctor.py | Builder health check (118 PASS) | Pre-dispatch sanity |
| cex_hooks.py | Pre/post validation + git hook | F8 before commit |
| cex_sanitize.py | ASCII enforcement | F7 pre-commit |
| cex_feedback.py | Quality tracking + archive | Post-F8 metrics |
| signal_writer.py | Inter-nucleus signals | F8 on complete |

## Validation Tools
| Tool | Purpose | When |
| :--- | :--- | :--- |
| cex_hooks.py pre-commit | Reject non-ASCII in code | Git stage |
| cex_doctor.py | Builder ISO integrity | After any ISO edit |
| cex_quality_monitor.py | Regression detection | Weekly |

## External References (industry standards, not executable tools)
- **HuggingFace** Dataset Cards spec: `huggingface.co/docs/datasets/dataset_card`
- **ML Commons Croissant**: `mlcommons.org/working-groups/data/croissant/`
- **Google Data Cards Playbook**: `research.google/pubs/data-cards-playbook/`
- **Datasheets for Datasets** (Gebru et al., 2021): `arxiv.org/abs/1803.09010`
- **GDPR Article 30** (records of processing)
- **W3C DCAT-3** (data catalog vocabulary)

## Anti-Patterns
- Do NOT invent tool names (e.g., `schema_validator.py`, `lint_card.py`, `integrity_check.py`, `cex_formatter.py` — none exist in this repo).
- Do NOT reference tools from `N04_knowledge/` internals; use only public `_tools/*.py`.
