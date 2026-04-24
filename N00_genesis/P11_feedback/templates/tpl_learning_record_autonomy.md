---
id: tpl_learning_record_autonomy
kind: template
8f: F6_produce
pillar: P11
title: "Learning Record — Autonomous Mission Phase"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/.cex/learning_records/emergent_autonomy_20260403/
variables: [MISSION, NUCLEUS, PHASE, FINDINGS, METRICS, RECOMMENDATIONS]
density_score: 0.95
tags: [template, learning-record, autonomy, mission-retrospective, instance-extraction]
tldr: "Learning record for autonomous mission phases — capture what worked, what failed, and what to do differently."
updated: "2026-04-13"
related:
  - mission_content_monetization
  - mission_geo_discovery
  - p12_sig_builder_nucleus
  - tpl_workflow_research_pipeline
  - bld_tools_capability_registry
  - p10_out_executive_summary
  - p12_wf_orchestration_pipeline
  - p08_pat_nucleus_fractal
  - p11_qg_skill
  - bld_instruction_playground_config
---

# Learning Record: {{MISSION}} — {{PHASE}}

## Context

| Field | Value |
|-------|-------|
| Mission | {{MISSION}} |
| Nucleus | {{NUCLEUS}} |
| Phase | {{PHASE}} |
| Date | {{DATE}} |
| Duration | {{DURATION}} |
| Status | {{STATUS | default: 'complete'}} |

---

## Objectives

{{#OBJECTIVES}}
| # | Objective | Status | Notes |
|---|-----------|:------:|-------|
{{#each}}
| {{position}} | {{description}} | {{status}} | {{notes}} |
{{/each}}
{{/OBJECTIVES}}

---

## What Worked

{{#FINDINGS.successes}}
### {{position}}. {{title}}

**Description**: {{description}}

**Evidence**: {{evidence}}

**Replicable**: {{replicable | default: 'yes'}}

{{/FINDINGS.successes}}

---

## What Failed

{{#FINDINGS.failures}}
### {{position}}. {{title}}

**Description**: {{description}}

**Root cause**: {{root_cause}}

**Impact**: {{impact}}

**Mitigation**: {{mitigation}}

{{/FINDINGS.failures}}

---

## Emergent Patterns

Unexpected behaviors, capabilities, or insights that emerged during autonomous operation:

{{#FINDINGS.emergent}}
- **{{title}}**: {{description}}
{{/FINDINGS.emergent}}

---

## Metrics

| Metric | Before | After | Delta |
|--------|:------:|:-----:|:-----:|
{{#METRICS}}
| {{name}} | {{before}} | {{after}} | {{delta}} |
{{/METRICS}}

---

## Recommendations

{{#RECOMMENDATIONS}}
### {{priority}} Priority

{{#items}}
- [ ] **{{title}}**: {{description}}
  - Nucleus: {{nucleus}}
  - Effort: {{effort}}
  - Impact: {{impact}}
{{/items}}

{{/RECOMMENDATIONS}}

---

## Pipeline Lessons (if research mission)

### Correct Pipeline (validated)

```
Phase 1: DISCOVER  → find URLs/sources (don't extract yet)
Phase 2: EXTRACT   → get structured data from sources
Phase 3: VALIDATE  → anti-fake checks, format validation
Phase 4: ENRICH    → fill gaps from secondary sources
Phase 5: CONSOLIDATE → dedup, score, final output
```

### Anti-Patterns (avoid)

| Anti-Pattern | Why It Fails | Alternative |
|-------------|--------------|-------------|
| Fabricating data | Trust = 0, all work wasted | Report zero results honestly |
| Skipping validation | Garbage in CRM | Always run Phase 3 |
| Single-source | Low coverage | Use 3+ source types |
| Manual only | Doesn't scale | Automate Phases 1-3 |

---

## Signals Emitted

{{#SIGNALS}}
| Timestamp | Nucleus | Type | Quality | Tag |
|-----------|:-------:|------|:-------:|-----|
{{#each}}
| {{timestamp}} | {{nucleus}} | {{type}} | {{quality}} | {{tag}} |
{{/each}}
{{/SIGNALS}}

---

## Archive

This record should be stored at:
```
.cex/learning_records/{{MISSION_SLUG}}/{{PHASE_SLUG}}_{{NUCLEUS}}.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[mission_content_monetization]] | downstream | 0.26 |
| [[mission_geo_discovery]] | downstream | 0.24 |
| [[p12_sig_builder_nucleus]] | downstream | 0.21 |
| [[tpl_workflow_research_pipeline]] | sibling | 0.21 |
| [[bld_tools_capability_registry]] | upstream | 0.20 |
| [[p10_out_executive_summary]] | upstream | 0.19 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.19 |
| [[p08_pat_nucleus_fractal]] | upstream | 0.18 |
| [[p11_qg_skill]] | related | 0.18 |
| [[bld_instruction_playground_config]] | upstream | 0.18 |
