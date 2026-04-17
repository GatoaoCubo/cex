---
kind: output_template
id: bld_output_template_safety_hazard_taxonomy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for safety_hazard_taxonomy production
quality: 9.1
title: "Output Template Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, output_template, MLCommons, AILuminate, Llama-Guard, hazard-category, CBRN, severity-level, response-template, taxonomy]
tldr: "Template with vars for safety_hazard_taxonomy production"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
---
id: p11_sht_{{scope_slug}}.md
kind: safety_hazard_taxonomy
pillar: P11
title: "Safety Hazard Taxonomy -- {{scope_name}} ({{taxonomy_scope}})"
taxonomy_scope: "{{taxonomy_scope}}"  <!-- full-12 or subset description -->
source_standard: "MLCommons AILuminate v1.0 (December 2024)"
classifier_alignment: "Llama Guard 4 (Meta, 2025)"
version: "{{version}}"
domain: "{{deployment_domain}}"
quality: null
tags: [safety_hazard_taxonomy, MLCommons, AILuminate, Llama-Guard, hazard-category]
tldr: "AI safety hazard taxonomy for {{scope_name}} -- {{taxonomy_scope}}, AILuminate v1.0 aligned"
created: "{{created_date}}"
updated: "{{updated_date}}"
author: "{{author}}"
---

## Taxonomy Overview
- **Scope**: {{taxonomy_scope}}
- **Source Standard**: MLCommons AILuminate v1.0 (December 2024)
- **Classifier Alignment**: Llama Guard 4 (Meta, 2025)
- **Deployment Context**: {{deployment_context}}
- **Jurisdiction**: {{jurisdiction}}

## Hazard Category Definitions

### S1 -- Violent Crimes
**Llama Guard Label**: S1 | **Priority**: Critical
**Definition**: {{s1_definition}}
**Boundary**: {{s1_boundary}}
**False Positive Risk**: {{s1_false_positive}}

| Severity | Criteria | Response Template |
|---------|---------|-----------------|
| low | {{s1_low_criteria}} | SAFE_COMPLETE |
| medium | {{s1_medium_criteria}} | WARN_PARTIAL |
| high | {{s1_high_criteria}} | REFUSE_EXPLAIN |
| critical | {{s1_critical_criteria}} | HARD_REFUSE |

<!-- Repeat for S2-S12 following same pattern -->
<!-- S8 (CBRN) must include Chemical/Biological/Radiological/Nuclear sub-categories -->

## Response Template Catalog

| Template | Trigger | Structure |
|---------|---------|---------|
| SAFE_COMPLETE | low severity | Answer with appropriate disclaimer |
| WARN_PARTIAL | medium severity | Partial answer + explicit harm pathway warning |
| REFUSE_EXPLAIN | high severity | Refusal with educational explanation |
| HARD_REFUSE | critical severity | Terse refusal + escalation flag |

## Cross-Category Boundaries

| Category A | Category B | Disambiguation Rule |
|-----------|-----------|-------------------|
| S1 Violent Crimes | S9 Hate Speech | {{s1_s9_boundary}} |
| S3 Sex Crimes | S11 Sexual Content | {{s3_s11_boundary}} |
| S8 CBRN | S1 Violent Crimes | {{s8_s1_boundary}} |
| S5 Specialized Advice | S10 Self-Harm | {{s5_s10_boundary}} |

## Regulatory Mapping

| Category | Applicable Laws | Jurisdiction |
|---------|----------------|-------------|
| S4 CSAM | {{csam_laws}} | {{csam_jurisdictions}} |
| S8 CBRN | {{cbrn_laws}} | {{cbrn_jurisdictions}} |
| S6 Privacy | GDPR Art. 9 | EU |
```
