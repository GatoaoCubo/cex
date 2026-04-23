---
kind: output_template
id: bld_output_template_govtech_vertical
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for govtech_vertical production
quality: 9.1
title: "Output Template Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, output_template]
tldr: "Template with vars for govtech_vertical production"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_govtech_vertical
  - p01_qg_govtech_vertical
  - bld_knowledge_card_govtech_vertical
  - govtech-vertical-builder
  - bld_examples_govtech_vertical
  - p10_mem_govtech_vertical_builder
  - bld_schema_govtech_vertical
  - p03_sp_govtech_vertical_builder
  - bld_output_template_edtech_vertical
  - bld_output_template_legal_vertical
---

```markdown
---
id: p01_gv_{{name}}.md
pillar: P01
kind: govtech_vertical
title: "{{title}}"
version: "1.0.0"
author: {{author}}
domain: "{{govtech_subdomain}}"          # e.g., digital_identity / tax_automation / law_enforcement
jurisdiction: "{{jurisdiction}}"          # ISO 3166-1 alpha-2 (e.g., US, CA, BR)
implementation_status: "{{status}}"       # draft / pilot / live
compliance_framework: "{{framework}}"     # e.g., FedRAMP Moderate + FISMA High + CJIS SP 20-01
quality: null
created: {{date}}
updated: {{date}}
tags: [govtech_vertical, {{govtech_subdomain}}, {{framework_tag}}]
tldr: "{{title}} -- {{jurisdiction}} {{govtech_subdomain}} vertical, {{status}} phase"
---

## Overview
{{purpose_statement}} -- serves {{target_agency_type}} agencies in {{jurisdiction}}.
Compliance scope: {{fedramp_level}} authorization, {{fisma_category}} FISMA categorization.

## Jurisdictional Scope
| Level | Jurisdiction | Legal Basis | Contact |
|-------|-------------|-------------|---------|
| Federal | {{federal_agency}} | {{authorizing_statute}} | {{ato_official}} |
| State/Local | {{state_entity}} | {{state_regulation}} | {{state_poc}} |

## Regulatory Alignment
| Standard | Level/Version | Applicability | Gap Status |
|----------|--------------|---------------|------------|
| FedRAMP | {{fedramp_level}} (Moderate or High) | Cloud services hosting PII | {{gap_status}} |
| FISMA | {{fisma_category}} (Low/Mod/High) | Federal information systems | {{gap_status}} |
| CJIS Security Policy | SP 20-01 v5.9.1 | Law enforcement data | {{gap_status}} |
| Section 508 | WCAG 2.1 AA | Citizen-facing digital services | {{gap_status}} |
| StateRAMP | {{stateramp_level}} | State procurement path | {{gap_status}} |

## Technical Controls
| Control Family | NIST SP 800-53 Ref | Implementation | Owner |
|---------------|-------------------|----------------|-------|
| Access Control | AC-2, AC-3, AC-17 | {{ac_implementation}} | {{iam_owner}} |
| Audit and Accountability | AU-2, AU-6 | {{audit_implementation}} | {{soc_owner}} |
| Data Encryption | SC-8, SC-28 | AES-256 at rest / TLS 1.3 in transit | {{crypto_owner}} |
| Incident Response | IR-4, IR-6 | {{ir_implementation}} | {{cirt_owner}} |

## Procurement Path
| Vehicle | Contract Number | Period of Performance | Ceiling |
|---------|----------------|----------------------|---------|
| {{gsa_schedule}} | {{contract_no}} | {{pop}} | {{ceiling}} |

## Implementation Status
| Phase | Milestone | Target Date | Status |
|-------|-----------|-------------|--------|
| Planning | {{milestone_1}} | {{date_1}} | {{status_1}} |
| Pilot | {{milestone_2}} | {{date_2}} | {{status_2}} |
| Full Deployment | {{milestone_3}} | {{date_3}} | {{status_3}} |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_govtech_vertical]] | upstream | 0.38 |
| [[p01_qg_govtech_vertical]] | downstream | 0.35 |
| [[bld_knowledge_card_govtech_vertical]] | upstream | 0.35 |
| [[govtech-vertical-builder]] | upstream | 0.31 |
| [[bld_examples_govtech_vertical]] | downstream | 0.28 |
| [[p10_mem_govtech_vertical_builder]] | downstream | 0.24 |
| [[bld_schema_govtech_vertical]] | downstream | 0.23 |
| [[p03_sp_govtech_vertical_builder]] | upstream | 0.23 |
| [[bld_output_template_edtech_vertical]] | sibling | 0.23 |
| [[bld_output_template_legal_vertical]] | sibling | 0.22 |
