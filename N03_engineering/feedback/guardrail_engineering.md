---
id: p11_gr_builder_nucleus
kind: guardrail
pillar: P11
title: Guardrails -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [guardrail, builder, N03, safety]
tldr: Protection rules preventing destructive operations -- never overwrite without backup, never delete kinds.
density_score: 0.90
---

# Guardrails: Builder Nucleus

## G01: Never Overwrite Without Backup
Before overwriting any existing artifact, the previous version must be readable.
The compile step preserves .md source. Git history is the backup.
If git is unavailable, refuse to overwrite.

## G02: Never Delete a Kind
kinds_meta.json only grows. Kinds can be deprecated (add deprecated: true) but never removed.
Removing a kind breaks every artifact that references it.

## G03: Never Skip Frontmatter Validation
Even in dry-run mode, F7 validates frontmatter structure.
An artifact without valid frontmatter is not an artifact (AX01).

## G04: Never Publish Below 8.0
Quality floor is absolute. If F7 returns < 8.0 after 2 retries, the artifact is NOT saved.
It is logged as failed with the quality score and issues.

## G05: Never Modify Builder ISOs Automatically
The 13 ISOs per builder are hand-crafted. No automated process may modify them.
Feedback on builders goes through cex_feedback.py for human review.

## G06: Never Build Without Schema Check
Before F6 PRODUCE, F1 MUST have loaded the schema constraints.
Building without knowing max_bytes leads to oversized artifacts.

## G07: Proprietary Contamination Block
If any output contains proprietary names, product references, or company-specific terms,
F7 rejects with AX08 violation. The builder re-generates with generic terms.

## Enforcement

| Guardrail | Enforced By | Severity |
|-----------|-------------|----------|
| G01 | Git check before write | BLOCK |
| G02 | cex_kind_register.py (no --delete flag) | DESIGN |
| G03 | Runner.F7 always runs | HARD |
| G04 | Runner.F7 threshold check | HARD |
| G05 | File permissions on builders/ | DESIGN |
| G06 | Runner.F1 is mandatory step | PIPELINE |
| G07 | grep + F7 check | HARD |