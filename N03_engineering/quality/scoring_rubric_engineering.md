---
id: p07_sr_builder_nucleus
kind: scoring_rubric
pillar: P07
title: Scoring Rubric -- Builder Nucleus
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
framework: builder_quality
target_kinds: [all_99_kinds]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: semi-automated
domain: meta-construction
quality: 9.1
tags: [scoring-rubric, builder, N03, quality]
tldr: 5-dimension rubric for scoring any CEX artifact -- correctness, completeness, density, usefulness, integration.
density_score: 0.90
---

# Scoring Rubric: Builder Nucleus

## Purpose
Scores ANY artifact produced by the 8F pipeline. Applies universally
to all 99 kinds. Each dimension has clear 10/5/1 anchors.

## Dimensions

### D1: Correctness (30%)
Does the artifact conform to its kind specification?

| Score | Anchor |
|-------|--------|
| 10 | Frontmatter valid, all schema fields correct, kind matches, pillar correct |
| 5 | Minor field issues (typo in id, missing optional field) |
| 1 | Wrong kind in frontmatter, missing required fields, invalid YAML |

**Automation**: cex_doctor.py checks frontmatter + schema. Fully automatable.

### D2: Completeness (25%)
Are all sections from the builder template filled?

| Score | Anchor |
|-------|--------|
| 10 | Every section from bld_output_template has substantive content |
| 5 | >70% of sections filled, remainder has placeholder markers |
| 1 | <50% of sections filled, major gaps |

**Automation**: Compare sections against bld_output_template_{{kind}}.md. Semi-automatable.

### D3: Density (20%)
Is every line carrying signal? No filler, no fluff?

| Score | Anchor |
|-------|--------|
| 10 | 0.90+ signal ratio, zero filler sentences, every line teaches or specifies |
| 5 | 0.80 density, some transitional sentences but no lorem/placeholder |
| 1 | Below 0.70, has filler text, lorem ipsum, or empty sections |

**Automation**: Line analysis (content_lines / total_lines). Fully automatable.

### D4: Usefulness (15%)
Can a consumer use this artifact immediately without editing?

| Score | Anchor |
|-------|--------|
| 10 | Drop-in usable. An LLM can BECOME/INJECT/CALL this directly. |
| 5 | Needs minor edits (fill a {{variable}}, adjust a threshold) |
| 1 | Needs major rewrite to be usable |

**Automation**: Manual review. Not automatable (requires domain judgment).

### D5: Integration (10%)
Does it compile, index, and reference correctly?

| Score | Anchor |
|-------|--------|
| 10 | Compiles to valid YAML, indexes clean, all refs resolve, no warnings |
| 5 | Compiles but some references broken or warnings from doctor |
| 1 | Does not compile, index fails, orphaned references |

**Automation**: cex_compile.py + cex_index.py + cex_doctor.py. Fully automatable.

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Archive as reference example in P{{NN}}/examples/ |
| PUBLISH | >= 8.0 | Standard publication to nucleus or pillar |
| REVIEW | >= 7.0 | Return with specific feedback per dimension |
| REJECT | < 7.0 | Redo from scratch with different approach |

## Calibration

| Score | Example |
|-------|---------|
| 9.7 | kc_agent.md -- complete spec, every section filled, compiles clean, immediately usable |
| 8.3 | ex_workflow_brand_propagation.md -- good structure, minor density issues |
| 7.1 | Generic placeholder nucleus artifact -- structure OK, content thin |
| 5.5 | Auto-generated with wrong kind, missing sections |
