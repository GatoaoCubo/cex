---
kind: quality_gate
id: p11_qg_safety_policy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for safety_policy
quality: 9.1
title: "Quality Gate Safety Policy"
version: "1.0.0"
author: wave1_builder_gen
tags: [safety_policy, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for safety_policy"
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_safety_policy
  - safety-policy-builder
  - kc_safety_policy
  - bld_collaboration_safety_policy
  - p03_sp_safety_policy_builder
  - p07_qg_benchmark_suite
  - p03_qg_planning_strategy
  - bld_instruction_safety_policy
  - p11_qg_audit_log
  - p03_qg_prompt_technique
---

## Quality Gate

## Definition
| metric       | threshold | operator | scope                          |
|--------------|-----------|----------|--------------------------------|
| safety_policy | P11       | matches  | all AI safety governance rules |

## HARD Gates
| ID   | Check                  | Fail Condition                                      |
|------|------------------------|-----------------------------------------------------|
| H01  | YAML valid             | Invalid YAML syntax                                 |
| H02  | ID matches pattern     | ID does not match `P[0-9]{2}-[A-Z]{3}-[0-9]{4}`    |
| H03  | kind matches           | kind is not `safety_policy`                       |
| H04  | Policy version exists  | Missing version field                             |
| H05  | Signed by CTO          | No CTO signature                                  |
| H06  | Risk assessment included | Missing risk assessment section               |
| H07  | Approval date present  | No approval date                                  |

## SOFT Scoring
| Dim | Dimension            | Weight | Scoring Guide                                      |
|-----|----------------------|--------|----------------------------------------------------|
| D1  | Completeness         | 0.15   | 100% complete = 1.0; missing sections = 0.5        |
| D2  | Clarity              | 0.15   | Unambiguous language = 1.0; ambiguous = 0.5        |
| D3  | Alignment with P11   | 0.10   | Fully aligned = 1.0; partial = 0.5                 |
| D4  | Risk coverage        | 0.15   | Comprehensive risks = 1.0; incomplete = 0.5        |
| D5  | Stakeholder input    | 0.10   | Includes all required stakeholders = 1.0; missing = 0.5 |
| D6  | Update frequency     | 0.10   | Updated annually = 1.0; outdated = 0.5             |
| D7  | Enforcement          | 0.10   | Clear enforcement rules = 1.0; vague = 0.5         |
| D8  | Audit trail          | 0.15   | Full audit logs = 1.0; partial = 0.5               |

## Actions
| Score     | Action                                      |
|-----------|---------------------------------------------|
| GOLDEN    | >=9.5: Auto-approve, no further review      |
| PUBLISH   | >=8.0: Publish with CTO approval            |
| REVIEW    | >=7.0: Require stakeholder review           |
| REJECT    | <7.0: Reject, mandatory rewrite required    |

## Bypass
| conditions                          | approver | audit trail                          |
|------------------------------------|----------|--------------------------------------|
| Emergency, CTO override            | CTO      | Document reason, approval timestamp |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
