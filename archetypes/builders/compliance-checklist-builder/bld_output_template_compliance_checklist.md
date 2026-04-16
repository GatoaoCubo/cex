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
