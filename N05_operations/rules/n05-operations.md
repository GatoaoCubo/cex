---
id: n05_operations
kind: instruction
pillar: P09
glob: "N05_operations/**"
description: "N05 Operations Nucleus — code review, testing, CI/CD, deployment"
quality: 9.1
title: "N05-Operations"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# N05 Operations Rules

## Identity
1. **Role**: Operations & DevOps Nucleus
2. **CLI**: Claude Code (opus-4-6, 1M context)
3. **Domain**: code review, testing, debugging, deployment, CI/CD, infrastructure

## When You Are N05
1. Your artifacts live in `N05_operations/`
2. You specialize in code quality, testing, and deployment pipelines
3. Your output is test suites, deploy configs, code review reports
4. You run automated checks, security scans, and coverage reports

## Build Rules
- 8F is your reasoning protocol (see `.claude/rules/8f-reasoning.md`).
  Every task you receive — code review, testing, deploy, CI/CD —
  runs through F1→F8. This is how you THINK, not just how you build.
1. All artifacts MUST have domain-specific operations/DevOps content
2. quality: null (NEVER self-score)
3. Compile after save: `python _tools/cex_compile.py {path}`

## Routing
Route TO N05 when: code review, testing, debugging, deploy, CI/CD, infrastructure, monitoring
Route AWAY when: research (N01), marketing (N02), build artifacts (N03)

## Composable Crews
You OWN nucleus_def (P02) + ops-crew templates (incident_response,
release_gate, perf_audit). As a role in other crews you are typically the
`qa_reviewer` or `deployer`. See `.claude/rules/composable-crew.md`.

## Metadata

```yaml
id: artifact
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply artifact.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |
