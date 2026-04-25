---
id: p02_ax_builder_nucleus
kind: axiom
8f: F4_reason
pillar: P02
title: Axioms -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [axiom, builder, N03, invariants]
tldr: "10 axioms: AX01 frontmatter=identity, AX02 one-kind-one-pillar, AX03 one-kind-one-function, AX04 quality floor 8.0, AX05 compiled derives from source, AX06 8F is sequential, AX07 builders=13 ISOs complete, AX08 no proprietary refs, AX09 constructor specifies never executes, AX10 kinds_meta.json is truth."
density_score: 0.95
related:
  - p03_sp_n03_creation_nucleus
  - p03_sp_builder_nucleus
  - bld_architecture_kind
  - kind-builder
  - p03_sp_kind_builder
  - bld_instruction_kind
  - bld_schema_kind
  - bld_collaboration_kind
  - p11_qg_builder_nucleus
  - bld_knowledge_card_kind
---

# Axioms of the Builder Nucleus

Non-negotiable. No exception. No override.

## AX01: Frontmatter is Identity
Every CEX artifact has YAML frontmatter with minimum: id, kind, pillar, title, version, created, updated, author, quality, tags, tldr. Without frontmatter, it is not an artifact.

## AX02: One Kind, One Pillar
Every kind belongs to exactly 1 of 12 pillars. No kind spans pillars. If it seems to, it is two kinds.

## AX03: One Kind, One Function
Every kind exercises exactly 1 of 8 LLM functions (BECOME, INJECT, REASON, CALL, PRODUCE, CONSTRAIN, GOVERN, COLLABORATE).

## AX04: Quality Floor is 8.0
Minimum for publication is 8.0. Below = redo. Golden = 9.5. Not negotiable.

## AX05: Compiled Derives from Source
.yaml in compiled/ are derived views of .md sources. The .md is truth. Never edit compiled/ directly.

## AX06: Pipeline is Sequential
8F runs F1-F8 in order. Skip is allowed. Reorder is not. F7 GOVERN always follows F6 PRODUCE.

## AX07: Builders are Complete
Each builder = 13 ISOs. None optional: manifest, quick_start, prime, instructions, architecture, output_template, examples, error_handling, upload_kit, system_instruction, schema, knowledge_card, collaboration.

## AX08: No Proprietary References
No artifact references a specific company, product, or framework. CEX is universal. Generic terms only.

## AX09: Constructor Specifies, Never Executes
The builder defines WHAT to build and HOW to validate. Never deploys or monitors. N03 builds, N05 operates.

## AX10: kinds_meta.json is Truth
.cex/kinds_meta.json is the single source of truth for what kinds exist, their pillar, function, and constraints.

## Enforcement

| Axiom | Check | Severity |
|-------|-------|----------|
| AX01, AX02, AX03, AX07, AX10 | cex_doctor.py + Runner.F7 | HARD FAIL |
| AX04, AX05, AX06 | Runner.F7 quality gates | SOFT FAIL (retry) |
| AX08 | grep across tracked files | 0 violations required |
| AX09 | Architectural (human review) | Design constraint |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.33 |
| [[p03_sp_builder_nucleus]] | downstream | 0.32 |
| [[bld_architecture_kind]] | downstream | 0.29 |
| [[kind-builder]] | downstream | 0.28 |
| [[p03_sp_kind_builder]] | downstream | 0.27 |
| [[bld_instruction_kind]] | downstream | 0.27 |
| [[bld_schema_kind]] | downstream | 0.26 |
| [[bld_collaboration_kind]] | downstream | 0.26 |
| [[p11_qg_builder_nucleus]] | downstream | 0.26 |
| [[bld_knowledge_card_kind]] | upstream | 0.25 |
