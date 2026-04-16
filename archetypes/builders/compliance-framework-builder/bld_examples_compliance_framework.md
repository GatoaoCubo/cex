---
kind: examples
id: bld_examples_compliance_framework
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of compliance_framework artifacts
quality: 8.9
title: "Examples Compliance Framework"
version: "1.0.0"
author: wave1_builder_gen
tags: [compliance_framework, builder, examples]
tldr: "Golden and anti-examples of compliance_framework artifacts"
domain: "compliance_framework construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
title: AI Compliance Framework for EU AI Act & GDPR
version: 1.0
author: Compliance Team
date: 2023-10-01
regulatory_scope: [EU AI Act, GDPR, CCPA]
---

### Regulatory Mapping
- **EU AI Act (Art. 13):** High-risk AI systems require transparency in data processing.
  → Mapped to: Data logging module (v1.2), user consent dashboard.
- **GDPR (Art. 22):** Right to object to automated decision-making.
  → Mapped to: Manual override switch in scoring algorithms.
- **CCPA (§ 999.313):** Consumer right to access data used for AI training.
  → Mapped to: Data export API endpoint (v2.1).

### Attestation
> This system complies with mapped regulations as of 2023-10-01.
> Signed by: [Compliance Officer Name], [Date]
```

## Anti-Example 1: Missing Regulatory Scope
```markdown
---
title: AI Compliance Framework
version: 0.5
author: Dev Team
date: 2023-09-15
---

### Regulatory Mapping
- "Data must be encrypted": Implemented via AES-256.
- "User consent required": Handled by checkbox on signup.
```
## Why it fails
No explicit regulatory scope (e.g., GDPR, EU AI Act) is defined. The framework lacks traceability to specific laws, making it impossible to verify compliance or update with new regulations.

## Anti-Example 2: Conflating with Safety Policies
```markdown
---
title: AI Safety & Compliance Framework
version: 1.0
author: Ops Team
date: 2023-10-05
regulatory_scope: [Internal Safety Policy]
---

### Regulatory Mapping
- "No unattended AI deployment": Requires 24/7 monitoring.
- "Annual risk assessment": Conducted by Q4 each year.
```
## Why it fails
The framework conflates regulatory compliance with internal safety policies (not laws). It violates the boundary by focusing on organizational rules rather than external regulatory requirements.
