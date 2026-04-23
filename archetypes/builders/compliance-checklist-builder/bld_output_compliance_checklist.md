---
kind: output_template
id: bld_output_template_compliance_checklist
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for compliance_checklist production
quality: 8.8
title: "Output Template Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, output_template]
tldr: "Template with vars for compliance_checklist production"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_compliance_checklist
  - bld_output_template_data_residency
  - bld_schema_compliance_checklist
  - p03_sp_verification_agent
  - bld_architecture_compliance_checklist
  - bld_examples_compliance_checklist
  - p09_kc_data_residency
  - bld_config_compliance_framework
  - bld_collaboration_compliance_checklist
  - bld_output_template_course_module
---

```yaml
---
id: p11_cc_{{name}}.md
name: {{compliance_checklist_name}}
pillar: P11
quality: null
description: {{checklist_description}}
sections:
  - title: {{section_title}}
    items:
      - {{item_1}}
      - {{item_2}}
---
```

<!-- id: Unique identifier following pattern ^p11_cc_[a-z][a-z0-9_]+.md$ -->
<!-- name: Name of compliance checklist -->
<!-- pillar: Always "P11" -->
<!-- quality: Must be null -->
<!-- description: Brief overview of checklist purpose -->
<!-- section_title: Title of checklist section -->
<!-- item_1: First compliance item -->
<!-- item_2: Second compliance item -->

**Example Table:**
| Requirement         | Status | Notes         |
|---------------------|--------|---------------|
| KYC Verification    | PASS   | <!-- Pass/fail indicator --> |
| Transaction Limits  | FAIL   | <!-- Compliance status --> |

**Example Code Block:**
```python
# Data Encryption Standards
def encrypt_data(data):
    # Implement AES-256 encryption
    <!-- Add encryption logic here -->
    return encrypted_data
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_compliance_checklist]] | downstream | 0.27 |
| [[bld_output_template_data_residency]] | sibling | 0.23 |
| [[bld_schema_compliance_checklist]] | downstream | 0.19 |
| [[p03_sp_verification_agent]] | upstream | 0.18 |
| [[bld_architecture_compliance_checklist]] | downstream | 0.18 |
| [[bld_examples_compliance_checklist]] | downstream | 0.18 |
| [[p09_kc_data_residency]] | downstream | 0.18 |
| [[bld_config_compliance_framework]] | downstream | 0.17 |
| [[bld_collaboration_compliance_checklist]] | downstream | 0.17 |
| [[bld_output_template_course_module]] | sibling | 0.17 |
