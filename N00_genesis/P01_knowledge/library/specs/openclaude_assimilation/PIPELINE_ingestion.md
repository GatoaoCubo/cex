---
id: spec_oc_ingestion_pipeline
kind: context_doc
pillar: P01
version: 1.0.0
created: 2026-04-05
author: n07-orchestrator
title: "OpenClaude to CEX Ingestion Pipeline"
quality: 9.0
tags: [pipeline, ingestion, openclaude, taxonomy, universal]
tldr: "How OpenClaude battle-tested prompts become universal CEX artifacts"
related:
  - spec_cex_system_map
  - skill
  - p03_sp_cex_core_identity
  - bld_instruction_kind
  - bld_knowledge_card_kind
  - p03_sp_n03_creation_nucleus
  - ctx_cex_new_dev_guide
  - p01_kc_universal_llm
  - spec_context_assembly
  - bld_output_template_builder
---

# OpenClaude to CEX Ingestion Pipeline

## Core Principle

OpenClaude is NOT a codebase to port. It is a corpus of battle-tested LLM knowledge
that CEX's taxonomy can classify, refine, and redeploy to ANY provider.

Each OpenClaude prompt is an instance of a CEX kind. The pipeline:
CLASSIFIES each asset into a CEX kind, BUILDS a proper artifact through the
existing builder pipeline, STORES in the correct pillar, COMPOSES at runtime.

## Asset-to-Kind Map (created)

### P03 System Prompts (identity)
- p03_sp_verification_agent -- adversarial verifier identity
- p03_sp_cex_core_identity -- universal base prompt for all nuclei

### P03 Instructions (behavioral)
- p03_ins_doing_tasks -- universal task execution rules
- p03_ins_action_protocol -- reversibility and blast radius

### P04 Skills (capabilities)
- p04_skill_verify -- adversarial verification protocol
- p04_skill_simplify -- 3-parallel-agent review (reuse/quality/efficiency)
- p04_skill_compact -- 9-section context compaction
- p04_skill_memory_extract -- background memory extraction

### P08 Agent Cards (deployment)
- p08_ac_verification -- read-only adversarial verifier
- p08_ac_explore -- fast read-only codebase explorer
- p08_ac_plan -- read-only planning architect

### P08 Patterns (architecture)
- p08_pat_context_compaction -- structured compaction pattern

### P11 Guardrails (safety)
- p11_gr_cyber_risk -- security boundary for tool access
- p11_gr_action_reversibility -- blast radius enforcement

## Pipeline: INGEST to DEPLOY

Phase 1 CLASSIFY: Map OpenClaude source to CEX kind
Phase 2 REFINE: Extract prompt text, adapt to CEX conventions, keep substance
Phase 3 BUILD: Run through builder pipeline (8F), generate proper artifact
Phase 4 STORE: Write to correct pillar compiled/ directory
Phase 5 COMPOSE: cex_crew_runner.py loads artifacts by kind at runtime

## Reverse Path: CEX to Any CLI

CEX artifact library (universal)
  |
  v COMPILE: collect by kind (system_prompt + skill + guardrail + instruction)
  |
  v RENDER: target-specific format
    - Claude Code CLI: monolithic system prompt
    - OpenAI Custom GPT: instructions + actions JSON
    - Gemini: system instruction + function declarations
    - Cursor: .cursorrules file
    - CLAUDE.md: project instructions
    - MCP server: tool definitions
  |
  v DEPLOY: any provider, any format

CEX is the compiler. The target LLM is the architecture.

## How to Run CEX with New Knowledge

After ingestion, the artifacts are LIVE. No wiring needed for:
- cex_crew_runner.py: already scans compiled/ dirs for artifacts by kind
- cex_skill_loader.py: discovers all skills in P04_tools/compiled/
- cex_8f_motor.py: F7 GOVERN now has p03_sp_verification_agent available

Wiring needed (next steps):
1. cex_crew_runner.py: inject p03_sp_cex_core_identity as base system prompt
2. cex_crew_runner.py: inject p03_ins_doing_tasks after identity
3. F7 GOVERN gate: load p04_skill_verify for non-trivial artifacts
4. /validate command: load p04_skill_simplify for deep review
5. Context management: trigger p04_skill_compact on budget pressure
6. Memory loop: trigger p04_skill_memory_extract every N turns
7. All nuclei: load p11_gr_* guardrails before tool execution

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_cex_system_map]] | sibling | 0.29 |
| [[skill]] | downstream | 0.29 |
| [[p03_sp_cex_core_identity]] | downstream | 0.28 |
| [[bld_instruction_kind]] | downstream | 0.25 |
| [[bld_knowledge_card_kind]] | related | 0.25 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.24 |
| [[ctx_cex_new_dev_guide]] | sibling | 0.23 |
| [[p01_kc_universal_llm]] | related | 0.23 |
| [[spec_context_assembly]] | sibling | 0.22 |
| [[bld_output_template_builder]] | downstream | 0.22 |
