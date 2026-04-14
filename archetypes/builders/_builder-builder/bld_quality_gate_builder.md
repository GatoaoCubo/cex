---
id: p11_qg_builder
kind: quality_gate
pillar: P11
title: "Gate: builder"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: type_builder
quality: 9.1
tags: [quality-gate, type-builder, builder-builder, P11, governance]
tldr: "Gates for type_builder artifacts — meta-builders that specialize in producing one kind."
density_score: 0.88
llm_function: GOVERN
---
# Gate: builder

## Definition

| Field     | Value                                      |
|-----------|--------------------------------------------|
| metric    | structural completeness + domain specificity |
| threshold | 8.0                                        |
| operator  | >=                                         |
| scope     | all type_builder artifacts                 |

## HARD Gates

All must pass. Failure on any = final score 0.

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = broken builder |
| H02 | id matches `^[a-z][a-z0-9-]+-builder$` | Namespace compliance for builders |
| H03 | id == filename stem | Discovery relies on exact match |
| H04 | kind == "type_builder" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, domain, llm_function, version, created, updated, author, tags | Completeness |
| H07 | llm_function == "BECOME" | Builders adopt identity, never CALL or GOVERN |
| H08 | domain maps to a known kind in TAXONOMY_LAYERS.yaml | Builder must target a real kind |
| H09 | MANIFEST has Identity, Capabilities, Routing, Crew Role sections | Structure compliance |
| H10 | Crew Role includes at least one "I do NOT handle" exclusion | Boundary definition required |

## SOFT Scoring

| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty, no filler | 1.0 |
| S02 | tags is list, len >= 3, includes "kind-builder" | 0.5 |
| S03 | Identity section explains what the builder produces in one tight sentence | 1.0 |
| S04 | Capabilities list has 4-6 bullets, each starts with verb | 1.0 |
| S05 | Routing keywords has >= 4 domain-specific terms | 1.0 |
| S06 | Routing triggers has >= 2 natural-language phrases | 0.5 |
| S07 | Crew Role names ROLE_CAPS (uppercase descriptor) | 0.5 |
| S08 | Crew Role answer is a single focused question | 1.0 |
| S09 | Exclusions cite specific neighboring kinds (not vague) | 1.0 |
| S10 | density_score >= 0.80 | 0.5 |
| S11 | No framework-internal jargon in user-facing fields | 1.0 |
| S12 | Capabilities reference field count or gate count from schema | 0.5 |

Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.

## Actions

| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference builder |
| >= 8.0 | PUBLISH — ready for routing index |
| >= 7.0 | REVIEW — fix weakest SOFT gates before publish |
| < 7.0  | REJECT — rework Identity + Capabilities |

## Bypass

| Field | Value |
|-------|-------|
| conditions | Emergency gap-fill when no builder exists for a critical kind |
| approver | p11-chief |
| audit_trail | Log bypass reason in records/audits/ with timestamp |
| expiry | 72h — full gate pass required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
