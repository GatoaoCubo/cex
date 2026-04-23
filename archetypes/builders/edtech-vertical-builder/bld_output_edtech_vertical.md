---
kind: output_template
id: bld_output_template_edtech_vertical
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for edtech_vertical production
quality: 9.1
title: "Output Template Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, output_template]
tldr: "Template with vars for edtech_vertical production"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_edtech_vertical
  - bld_knowledge_card_edtech_vertical
  - p01_qg_edtech_vertical
  - bld_examples_edtech_vertical
  - bld_tools_edtech_vertical
  - p10_mem_edtech_vertical_builder
  - edtech-vertical-builder
  - p03_sp_edtech_vertical_builder
  - hybrid_review7_n06
  - bld_architecture_edtech_vertical
---

```markdown
---
id: p01_etv_{{name}}.md
pillar: P01
kind: edtech_vertical
title: "{{title}}"
version: "1.0.0"
author: {{author}}
domain: "edtech"
focus_area: "{{focus_area}}"             # K-12 / Higher Ed / Vocational / Corporate L&D
target_demographic: "{{demographic}}"    # students / instructors / administrators
quality: null
created: {{date}}
updated: {{date}}
tags: [edtech_vertical, {{focus_area_tag}}, {{regulatory_tag}}]
tldr: "{{title}} -- {{focus_area}} EdTech vertical, {{regulatory_summary}}"
---

## Overview
{{purpose_statement}} -- targets {{demographic}} in {{focus_area}} contexts.
Regulatory scope: FERPA (student records), {{coppa_scope}} COPPA, LTI 1.3 integration.

## Regulatory Compliance
| Regulation | Applicability | Key Requirement | Status |
|-----------|--------------|-----------------|--------|
| FERPA | {{ferpa_scope}} | Parental consent for records disclosure; data minimization | {{status}} |
| COPPA | Users under 13 | Verifiable parental consent before PII collection | {{status}} |
| CIPA | K-12 schools receiving E-rate | Internet filtering for minors | {{status}} |
| State EdTech Laws | {{state_jurisdiction}} | {{state_specific_requirement}} | {{status}} |

## LTI 1.3 Integration
| LMS Platform | Integration Type | Tool Launch URL | Auth Method |
|-------------|-----------------|-----------------|-------------|
| Canvas | LTI 1.3 External Tool | {{canvas_launch_url}} | OAuth 2.0 + IMS Security Framework v1.0 |
| Moodle | LTI 1.3 External Tool | {{moodle_launch_url}} | OAuth 2.0 + IMS Security Framework v1.0 |
| Blackboard | LTI 1.3 External Tool | {{bb_launch_url}} | OAuth 2.0 + IMS Security Framework v1.0 |

## Student Data Privacy
| Data Type | Collection Basis | Retention | Deletion |
|-----------|-----------------|-----------|---------|
| {{data_type_1}} | {{basis_1}} | {{retention_1}} | On student/parent request |
| {{data_type_2}} | {{basis_2}} | {{retention_2}} | At end of school year |

## Learning Analytics
| Standard | Implementation | Tracking Scope |
|----------|---------------|----------------|
| xAPI (Experience API) | {{xapi_lrs_endpoint}} | {{xapi_statements_tracked}} |
| IMS Caliper 1.2 | {{caliper_sensor_url}} | {{caliper_events}} |

## Procurement Path
| Channel | Requirement | Approval Body |
|---------|------------|---------------|
| State ed-tech approval list | {{state_approval_requirement}} | {{state_doe}} |
| District direct procurement | {{district_requirement}} | {{district_tech_director}} |
| ISTE Certification | {{iste_badge}} | ISTE Product Certification |

## Implementation Status
| Phase | Milestone | Target Date | Status |
|-------|-----------|-------------|--------|
| Design | {{milestone_1}} | {{date_1}} | {{status_1}} |
| Pilot (1 district) | {{milestone_2}} | {{date_2}} | {{status_2}} |
| Full Rollout | {{milestone_3}} | {{date_3}} | {{status_3}} |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_edtech_vertical]] | upstream | 0.52 |
| [[bld_knowledge_card_edtech_vertical]] | upstream | 0.49 |
| [[p01_qg_edtech_vertical]] | downstream | 0.44 |
| [[bld_examples_edtech_vertical]] | downstream | 0.40 |
| [[bld_tools_edtech_vertical]] | upstream | 0.36 |
| [[p10_mem_edtech_vertical_builder]] | downstream | 0.36 |
| [[edtech-vertical-builder]] | upstream | 0.34 |
| [[p03_sp_edtech_vertical_builder]] | upstream | 0.34 |
| [[hybrid_review7_n06]] | upstream | 0.30 |
| [[bld_architecture_edtech_vertical]] | downstream | 0.25 |
