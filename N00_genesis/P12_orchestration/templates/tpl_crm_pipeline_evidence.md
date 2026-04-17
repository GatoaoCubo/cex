---
id: tpl_crm_pipeline_evidence
kind: template
pillar: P12
title: "CRM Pipeline Evidence — Mission Report Template"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/N07_admin/P05_output/output_crm_pipeline_evidence.md
variables: [BRAND_NAME, PIPELINE_NAME, BATCHES, FINAL_STATS, CITIES, TARGET_COUNT]
density_score: 0.95
tags: [template, pipeline-evidence, mission-report, crm, consolidation, instance-extraction]
tldr: "Mission completion evidence report — batch status, final stats, distribution, pipeline architecture lessons."
updated: "2026-04-13"
---

# {{PIPELINE_NAME}} — Pipeline Evidence

## 1. Mission Status

```
FINAL: {{FINAL_STATS.total}} contacts | 0 fakes
Target: {{TARGET_COUNT}}+ contacts {{FINAL_STATS.target_met | default: '✅'}}
```

| Wave | Batch | Status | +New | Sources | Output |
|:----:|:-----:|:------:|:----:|---------|--------|
{{#BATCHES}}
| {{wave}} | **{{letter}}** {{name}} | {{status}} | +{{new_count}} | {{sources}} | `{{output_file}}` |
{{/BATCHES}}

---

## 2. Final CRM Stats

```
Total:          {{FINAL_STATS.total}}
With phone:     {{FINAL_STATS.phone_count}} ({{FINAL_STATS.phone_pct}}%)
With address:   {{FINAL_STATS.address_count}} ({{FINAL_STATS.address_pct}}%)
With web/social:{{FINAL_STATS.web_count}} ({{FINAL_STATS.web_pct}}%)
With tax ID:    {{FINAL_STATS.taxid_count}} ({{FINAL_STATS.taxid_pct}}%)
Fakes:          0
```

### Distribution by City

{{#CITIES}}
| City | Count | Target | Status |
|------|:-----:|:------:|:------:|
{{#each}}
| {{name}} | {{count}} | {{target}} | {{status}} |
{{/each}}
{{/CITIES}}

### Distribution by Segment

{{#SEGMENTS}}
| Segment | Count | % |
|---------|:-----:|:-:|
{{#each}}
| {{name}} | {{count}} | {{pct}}% |
{{/each}}
{{/SEGMENTS}}

---

## 3. Pipeline Architecture (Lessons)

### Correct Pipeline (5 Phases)

```
DISCOVER → EXTRACT → VALIDATE → ENRICH → CONSOLIDATE
   │          │          │          │          │
   URLs    Structured   Anti-fake  Fill gaps  Dedup + score
           data         checks     2nd pass   Final output
```

### What Worked

{{#LESSONS.worked}}
- **{{title}}**: {{description}}
{{/LESSONS.worked}}

### What Didn't Work

{{#LESSONS.failed}}
- **{{title}}**: {{description}} → **Fix**: {{fix}}
{{/LESSONS.failed}}

---

## 4. Quality Metrics

| Metric | Value | Target | Status |
|--------|:-----:|:------:|:------:|
| Total contacts | {{FINAL_STATS.total}} | {{TARGET_COUNT}}+ | {{FINAL_STATS.target_met}} |
| Phone coverage | {{FINAL_STATS.phone_pct}}% | 60% | {{FINAL_STATS.phone_target_met}} |
| Address coverage | {{FINAL_STATS.address_pct}}% | 85% | {{FINAL_STATS.address_target_met}} |
| Web presence | {{FINAL_STATS.web_pct}}% | 65% | {{FINAL_STATS.web_target_met}} |
| Tax ID coverage | {{FINAL_STATS.taxid_pct}}% | 40% | {{FINAL_STATS.taxid_target_met}} |
| Fake rate | 0% | 0% | ✅ |
| Source diversity | {{FINAL_STATS.avg_sources}} | 3+ | {{FINAL_STATS.source_target_met}} |

---

## 5. Next Steps

{{#NEXT_STEPS}}
| Priority | Action | Nucleus | Effort |
|:--------:|--------|:-------:|:------:|
{{#each}}
| {{priority}} | {{description}} | {{nucleus}} | {{effort}} |
{{/each}}
{{/NEXT_STEPS}}

---

## 6. Artifacts Generated

| Artifact | Path | Size |
|----------|------|:----:|
{{#ARTIFACTS}}
| {{name}} | `{{path}}` | {{size}} |
{{/ARTIFACTS}}
