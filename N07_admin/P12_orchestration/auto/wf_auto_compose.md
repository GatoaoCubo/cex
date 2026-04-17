---
id: p12_wf_auto_compose
kind: workflow
pillar: P12
title: "Auto-Compose — Assemble prompts for nucleus execution"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: prompt_assembly
quality: 9.0
tags: [workflow, auto, n07, compose, rag, prompt]
tldr: "Assembles the full prompt for a nucleus: builder specs + KCs + brand + memory + task + examples. RAG prompt chaining."
density_score: 0.93
---

# Auto-Compose

## Trigger
When a nucleus needs a prompt assembled before execution (after hydrate, before produce).

## Industry Pattern
RAG (Retrieval-Augmented Generation) prompt chaining. Retrieve context → compose prompt → send to LLM.

## Steps

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | Load builder specs | Read `archetypes/builders/{kind}-builder/` | Identity + instructions |
| 2 | Load kind KC | `cex_query.py --kind {kind}` | Domain knowledge |
| 3 | Load brand context | `brand_inject.py` | Brand vars for prompt |
| 4 | Load decision manifest | Read `decision_manifest.yaml` | User decisions |
| 5 | Load memory | `cex_memory_select.py` | Past learnings |
| 6 | Load examples | Scan `compiled/` for similar | Reference artifacts |
| 7 | Apply token budget | `cex_token_budget.py` | Trim to fit context window |
| 8 | Compose final prompt | `cex_crew_runner.py compose_prompt()` | Complete prompt |

## Composition Order (priority)
1. System prompt (builder identity) — never trimmed
2. Task description — never trimmed
3. Decision manifest — never trimmed
4. Brand context — trimmed last
5. Kind KC — trimmed if needed
6. Examples — trimmed first
7. Memory — trimmed second

## Failure Mode
Missing component → skip it, compose with available parts. Log what was skipped.
