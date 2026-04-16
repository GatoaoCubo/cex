---
kind: output_template
id: bld_output_template_ai_rmf_profile
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for ai_rmf_profile production
quality: 9.1
title: "Output Template AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, output_template, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE, GenAI-profile, 600-1, action-ID, risk-category]
tldr: "Template with vars for ai_rmf_profile production"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
---
id: p11_rmf_{{profile_slug}}.md
kind: ai_rmf_profile
pillar: P11
title: "AI RMF GenAI Profile -- {{system_name}} (v{{version}})"
profile_scope: "{{system_name}}, {{deployment_context}}, {{user_population}}"
review_date: "{{review_date}}"
profiler: "{{profiler_team}}"
version: "{{version}}"
nist_version: "AI-RMF 1.0 + AI 600-1 (July 2024)"
domain: "{{domain}}"
quality: null
tags: [ai_rmf_profile, NIST, AI-RMF, 600-1, GenAI-profile]
tldr: "AI RMF GenAI Profile for {{system_name}} -- {{profile_scope_short}}"
created: "{{created_date}}"
updated: "{{updated_date}}"
author: "{{author}}"
---

## Function Coverage

| Function | Action-IDs | Implementation Status |
|----------|-----------|----------------------|
| GOVERN | {{govern_action_ids}} | {{govern_status}} |
| MAP | {{map_action_ids}} | {{map_status}} |
| MEASURE | {{measure_action_ids}} | {{measure_status}} |
| MANAGE | {{manage_action_ids}} | {{manage_status}} |

## Risk Category Severity Matrix (AI 600-1)

| # | Category | Severity | Controlling Action-IDs | Response |
|---|---------|---------|----------------------|---------|
| 1 | CBRN Information | {{cbrn_severity}} | {{cbrn_action_ids}} | {{cbrn_response}} |
| 2 | Confabulation | {{confab_severity}} | {{confab_action_ids}} | {{confab_response}} |
| 3 | Data Privacy | {{privacy_severity}} | {{privacy_action_ids}} | {{privacy_response}} |
| 4 | Environmental | {{env_severity}} | {{env_action_ids}} | {{env_response}} |
| 5 | Harmful Bias / Homogenization | {{bias_severity}} | {{bias_action_ids}} | {{bias_response}} |
| 6 | Human-AI Configuration | {{human_ai_severity}} | {{human_ai_action_ids}} | {{human_ai_response}} |
| 7 | Information Integrity | {{info_int_severity}} | {{info_int_action_ids}} | {{info_int_response}} |
| 8 | Information Security | {{info_sec_severity}} | {{info_sec_action_ids}} | {{info_sec_response}} |
| 9 | Intellectual Property | {{ip_severity}} | {{ip_action_ids}} | {{ip_response}} |
| 10 | Obscene / Degrading Content | {{obscene_severity}} | {{obscene_action_ids}} | {{obscene_response}} |
| 11 | Value Chain / Component Integration | {{value_chain_severity}} | {{value_chain_action_ids}} | {{value_chain_response}} |
| 12 | Workforce / Labor | {{workforce_severity}} | {{workforce_action_ids}} | {{workforce_response}} |

## Crosswalk Table

| AI-RMF Action-ID | Description | ISO 42001 Control | EU AI Act Ref |
|-----------------|-------------|------------------|--------------|
| {{action_id_1}} | {{desc_1}} | {{iso_1}} | {{eu_1}} |

## Gap Analysis
| Action-ID | Gap Description | Remediation Plan | Target Date |
|-----------|----------------|-----------------|------------|
| {{gap_action_id}} | {{gap_desc}} | {{remediation}} | {{target_date}} |

## Evidence Pointers
| Action-ID | Evidence Type | Reference | Date |
|-----------|--------------|-----------|------|
| {{action_id}} | {{evidence_type}} | {{reference}} | {{date}} |
```
