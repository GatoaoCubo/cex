---
id: p08_ac_verification
kind: agent_card
pillar: P08
title: "Agent Card: Verification Agent"
version: 1.0.0
quality: 8.9
tags: [agent_card, verification, govern, quality-assurance]
tldr: "Agent card for the verification agent used in F7 GOVERN. Defines capabilities, tools, input/output contracts, and deployment constraints."
domain: "architecture"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.91
---

# Verification Agent

## Purpose
Validates artifacts produced during F6 PRODUCE against structural,
rubric, and semantic quality gates. Acts as the quality firewall
before F8 COLLABORATE (save/compile/commit).

## Capabilities

| Capability | Description |
|-----------|-------------|
| Structural validation | Frontmatter, naming, size, schema compliance |
| Rubric scoring | 5-dimension scoring (D1-D5) against kind-specific rubric |
| Semantic review | Content quality, density, domain accuracy |
| Gate enforcement | Hard/soft fail classification with retry routing |
| Fix suggestions | Actionable remediation for each failure |

## Tools Available

- `cex_compile.py` -- compile artifact and validate output
- `cex_doctor.py` -- run health checks
- `cex_score.py` -- automated scoring (structural + rubric layers)
- `cex_hooks.py` -- pre-commit validation

## Input Contract

Receives: artifact path, kind, pillar, quality target
Expects: file exists, frontmatter is parseable, kind is registered

## Output Contract

Returns: PASS/FAIL verdict, numeric score, gate results, fix list
Format: structured text with clear pass/fail for automated parsing

## Deployment

- Activated during F7 GOVERN stage of 8F pipeline
- Runs in same context as the builder (no separate process)
- Max 2 retries on soft failures before escalating
- Hard failures block F8 immediately
