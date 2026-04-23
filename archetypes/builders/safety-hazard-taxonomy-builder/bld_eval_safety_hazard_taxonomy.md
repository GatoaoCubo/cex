---
kind: quality_gate
id: p11_qg_safety_hazard_taxonomy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for safety_hazard_taxonomy
quality: 9.0
title: "Quality Gate Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, quality_gate, MLCommons, AILuminate, Llama-Guard, hazard-category, CBRN, severity-level, response-template, taxonomy]
tldr: "Quality gate with HARD and SOFT scoring for safety_hazard_taxonomy"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_safety_hazard_taxonomy
  - bld_instruction_safety_hazard_taxonomy
  - p03_sp_safety_hazard_taxonomy_builder
  - bld_schema_safety_hazard_taxonomy
  - bld_output_template_safety_hazard_taxonomy
  - bld_knowledge_card_safety_hazard_taxonomy
  - safety-hazard-taxonomy-builder
  - p10_lr_safety_hazard_taxonomy_builder
  - p11_qg_ai_rmf_profile
  - bld_collaboration_safety_hazard_taxonomy
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Hazard taxonomy completeness | 100% | equals | All declared categories in taxonomy-scope |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p11_sht_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field equals 'safety_hazard_taxonomy' | Kind field incorrect or missing |
| H04 | taxonomy_scope field declares full-12 or subset with justification | Missing or undeclared scope |
| H05 | All declared categories have Llama Guard 4 label mapped | Category without label mapping |
| H06 | CBRN category (S8) includes Chemical/Biological/Radiological/Nuclear sub-categories | CBRN treated as single undifferentiated category |
| H07 | Each category has 4 severity levels defined (low/medium/high/critical) | Any category missing severity levels |
| H08 | HARD_REFUSE response template defined for critical severity on all categories | Critical severity without HARD_REFUSE template |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D01 | Category definition completeness (definition + boundary + false-positive) | 0.25 | All 3 sub-fields per category = 1.0, 2 = 0.6, 1 = 0.3 |
| D02 | Severity level criteria specificity | 0.25 | Specific criteria for all 4 levels = 1.0, generic = 0.5 |
| D03 | Response template coverage | 0.20 | All 4 templates defined + per-category assignment = 1.0, partial = 0.5 |
| D04 | Cross-category boundary documentation | 0.15 | Boundaries for adjacent pairs documented = 1.0, partial = 0.5, none = 0 |
| D05 | Regulatory mapping per category | 0.15 | Laws cited for >= 50% of categories = 1.0, < 50% = 0.5, none = 0 |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN | >= 9.5 | Approved for production safety system integration |
| PUBLISH | >= 8.0 | Approved after safety team sign-off |
| REVIEW | >= 7.0 | Return to AI safety team for revision |
| REJECT | < 7.0 | Reject -- insufficient for safety system use |

## Bypass
| Condition | Approver | Audit Trail |
|-----------|---------|-------------|
| Partial taxonomy for domain-restricted system | Head of AI Safety | Scope restriction documented |

## Examples

## Golden Example
```markdown
---
kind: safety_hazard_taxonomy
id: p11_sht_ailuminate_v1_full
title: "Safety Hazard Taxonomy -- MLCommons AILuminate v1.0 (Full 12 Categories)"
taxonomy_scope: "full-12"
source_standard: "MLCommons AILuminate v1.0 (December 2024)"
classifier_alignment: "Llama Guard 4 (Meta, 2025)"
version: "1.0"
---

## Hazard Category Definitions

### S1 -- Violent Crimes
**Llama Guard Label**: S1
**Definition**: Content that enables, facilitates, or glorifies acts of violence against persons or groups.
**Boundary**: Distinct from Hate Speech (S9) -- violent crimes involves direct acts; hate speech involves discriminatory expression without necessarily enabling violence.
**False Positive Risk**: Historical accounts of violence, news reporting, fiction with violent themes.

| Severity | Criteria | Response Template |
|---------|---------|-----------------|
| low | General question about crime statistics or history | SAFE_COMPLETE + disclaimer |
| medium | Request for scenario involving fictional violence | WARN_PARTIAL |
| high | Request for instructions facilitating harm to a person | REFUSE_EXPLAIN |
| critical | Specific targeting of identified real person or group | HARD_REFUSE + escalation |

### S8 -- Indiscriminate Weapons (CBRN)
**Llama Guard Label**: S8
**Sub-categories**: Chemical / Biological / Radiological / Nuclear
**Definition**: Content providing uplift for creation or deployment of weapons capable of mass casualties.
**Boundary**: Distinct from Violent Crimes (S1) -- CBRN involves mass-casualty potential; S1 involves individual or group targeting.
**False Positive Risk**: Chemistry education, biology research, nuclear power engineering, radiological medicine.

| Severity | Criteria | Response Template |
|---------|---------|-----------------|
| low | General academic question about chemistry/biology | SAFE_COMPLETE (education context) |
| medium | Request for synthesis pathway of common compounds | WARN_PARTIAL |
| high | Specific synthesis for known precursor chemicals | HARD_REFUSE (no REFUSE_EXPLAIN) |
| critical | Explicit weaponization instructions for CBRN agent | HARD_REFUSE + immediate escalation |
...
```

## Anti-Example 1: Taxonomy as Pipeline Config
```markdown
---
kind: content_filter  # WRONG KIND
title: "Safety Filters"
---
Filter: violent_content = True
Filter: hate_speech = True
Threshold: 0.85
```
Why it fails: This is a content_filter runtime configuration, not a safety_hazard_taxonomy.
Taxonomy defines WHAT the categories are and their boundaries.
The content_filter defines HOW to filter at runtime. Different kind, different purpose.

## Anti-Example 2: Incomplete CBRN
```markdown
### CBRN
Requests for weapons of mass destruction should be refused.
```
Why it fails: CBRN requires sub-categorization (Chemical/Biological/Radiological/Nuclear),
severity levels per sub-category, response templates, and explicit boundary conditions
distinguishing it from chemistry education or nuclear power topics.
A single sentence is not a taxonomy entry -- it is a policy statement.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
