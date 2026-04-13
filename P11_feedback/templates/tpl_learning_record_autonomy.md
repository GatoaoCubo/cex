---
id: tpl_learning_record_autonomy
kind: template
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
