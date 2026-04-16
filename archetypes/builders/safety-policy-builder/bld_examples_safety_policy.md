---
kind: examples
id: bld_examples_safety_policy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of safety_policy artifacts
quality: 9.0
title: "Examples Safety Policy"
version: "1.0.0"
author: wave1_builder_gen
tags: [safety_policy, builder, examples]
tldr: "Golden and anti-examples of safety_policy artifacts"
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
title: AI Safety Governance Policy
kind: safety_policy
version: 1.0
author: AI Ethics Committee
date: 2023-10-01
---

**Purpose**
Establish organizational rules for AI system development, deployment, and monitoring to prevent harm and ensure alignment with ethical principles.

**Scope**
Applies to all AI projects, teams, and stakeholders within the organization.

**Key Policies**
1. **Risk Assessment**: Mandatory pre-deployment safety reviews for all AI systems.
2. **Human Oversight**: Critical decisions must involve human-in-the-loop validation.
3. **Transparency**: Public documentation of AI capabilities, limitations, and safety measures.
4. **Accountability**: Clear ownership of safety outcomes for all AI initiatives.

**Procedures**
- Quarterly safety audits by the AI Ethics Committee.
- Incident reporting and escalation protocols for safety violations.
- Training programs for staff on safety governance principles.

**Review**
Policy reviewed annually by the Board of Directors and updated as needed.
```

## Anti-Example 1: Vagueness
```markdown
---
title: AI Safety Rules
kind: safety_policy
version: 0.1
author: Engineering Team
date: 2023-09-15
---

We should make sure AI systems are safe. Everyone must follow safety rules. Safety is important.
```
## Why it fails
Lacks specificity, actionable steps, and accountability. No defined procedures or metrics for evaluating safety, making enforcement impossible.

## Anti-Example 2: Overly Narrow Focus
```markdown
---
title: Data Privacy Safety Policy
kind: safety_policy
version: 1.0
author: Legal Department
date: 2023-08-20
---

**Purpose**
Ensure compliance with data protection laws in AI systems.

**Scope**
Applies only to data handling in AI projects.

**Policies**
- Encrypt all data at rest and in transit.
- Limit data access to authorized personnel.
```
## Why it fails
Focuses solely on data privacy (a compliance concern) rather than broader safety governance. Ignores risks like algorithmic bias, system failures, or ethical misuse.
