---
kind: instruction
id: bld_instruction_schedule
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for schedule
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Schedule"
version: "1.0.0"
author: n03_builder
tags: [schedule, builder, examples]
tldr: "Golden and anti-examples for schedule construction, demonstrating ideal structure and common pitfalls."
domain: "schedule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a schedule
## Phase 1: RESEARCH
1. Identify the workflow to trigger — confirm workflow_ref id exists in the cex corpus
2. Determine trigger_type: cron (fixed clock), interval (every N), event, manual, or one_shot
3. Write the cron expression; annotate it in plain English immediately
4. Confirm the IANA timezone relevant to the business domain (never assume UTC)
5. Decide catch_up: will missed runs need backfill on restart? Default false unless justified
6. Determine max_concurrent: is the workflow idempotent? If not, cap at 1
7. Assess jitter need: does this schedule share infrastructure with other schedules?
8. Define on-failure behavior: retry, alert, or skip — with rationale
9. Check for existing schedule artifacts to avoid duplicate scheduling of same workflow
10. Confirm schedule slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write ## Overview: what triggers, how often, why it exists
5. Write ## Trigger: cron expression + plain-English explanation + timezone + enabled status
6. Write ## Workflow: workflow_ref, expected duration, upstream dependencies
7. Write ## Policy: catch_up, max_concurrent, jitter, on-failure — each with rationale
8. Verify body <= 1024 bytes
9. Verify id matches `^p12_sc_[a-z][a-z0-9_]+$`
10. Verify file is named `p12_sched_{slug}.md`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `^p12_sc_` prefix and equals filename stem
4. Confirm kind == schedule
5. Confirm cron is a valid 5-field or 6-field expression
6. Confirm workflow_ref is non-empty and references a known workflow
7. Confirm trigger_type is one of: cron, interval, event, manual, one_shot
8. SOFT gates: score against QUALITY_GATES.md
9. Cross-check: does the body contain ONLY timing/policy logic (no workflow steps)?
10. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify schedule
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | schedule construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
