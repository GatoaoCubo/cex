---
id: p02_ax_builder_nucleus
kind: axiom
pillar: P02
title: Axioms -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [axiom, builder, N03, invariants]
tldr: 10 immutable truths governing all artifact construction. Violations are hard failures.
density_score: 0.95
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
