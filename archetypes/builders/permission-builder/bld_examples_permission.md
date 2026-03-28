---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of permission artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: permission-builder

## Golden Example

INPUT: "Cria permission para controlar acesso de agentes ao pool de knowledge cards"

OUTPUT:
```yaml
---
id: p09_perm_pool_access
kind: permission
pillar: P09
title: "Permission: Pool Access"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
scope: "knowledge card pool (P01 artifacts)"
roles: [orchestrator, researcher, builder, auditor, viewer]
read: "conditional"
write: "conditional"
execute: "deny"
quality: null
tags: [permission, pool, access-control, knowledge, roles]
tldr: "Controls read/write access to knowledge card pool by agent role with deny-overrides-allow"
domain: "knowledge management"
density_score: 0.89
inheritance: "orchestrator > researcher > builder > auditor > viewer"
escalation: "Request via signal to orchestrator with justification"
linked_artifacts:
  primary: "p11_gr_pool_integrity"
  related: [p08_law_pool_governance, p10_bi_pool_index]
---

## Scope
Controls which agent roles can read, write, or modify knowledge cards
in the CEX pool. Prevents unauthorized modifications to validated
knowledge while allowing broad read access for retrieval.

## Access Matrix
| Role | Read | Write | Execute | Conditions |
|------|------|-------|---------|------------|
| orchestrator | allow | allow | deny | Full pool access for governance |
| researcher | allow | conditional | deny | Write only to own-authored cards |
| builder | conditional | conditional | deny | Read domain-scoped; write own artifacts |
| auditor | allow | deny | deny | Read-only for compliance review |
| viewer | conditional | deny | deny | Read only published (quality >= 8.0) cards |

## Allow List
1. orchestrator: read all pool artifacts — governance oversight
2. orchestrator: write all pool artifacts — quality management
3. researcher: read all pool artifacts — research needs broad access
4. researcher: write own-authored cards — authorship ownership
5. auditor: read all pool artifacts — compliance requires visibility

## Deny List
1. viewer: write any artifact — viewers are read-only consumers
2. auditor: write any artifact — auditors must not modify what they review
3. builder: read outside own domain — prevents cross-domain contamination
4. ALL: execute on pool — pool artifacts are data, not executables

## Audit
| Event | Logged | Retention | Alert |
|-------|--------|-----------|-------|
| Write to golden card (>= 9.5) | yes | 90 days | immediate to orchestrator |
| Bulk read (> 50 cards/session) | yes | 30 days | threshold alert |
| Denied access attempt | yes | 60 days | 3+ attempts triggers escalation |
| Role escalation request | yes | 90 days | logged with justification |

## Escalation
- Request method: signal to orchestrator with scope and justification
- Approver: orchestrator (or designated deputy)
- Duration: temporary (max 24h, renewable)
- Audit: escalation logged with requester, approver, duration, and scope
```

WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p09_perm_ pattern (H02 pass)
- kind: permission (H04 pass)
- 19 frontmatter fields present (H08 pass)
- read/write/execute all valid enums (H07 pass)
- roles: 5 concrete roles with hierarchy (H09 pass)
- Access Matrix with 5 roles x 4 columns (S03 pass)
- Allow List with 5 entries and justifications (S04 pass)
- Deny List with 4 entries and reasons (S05 pass)
- Audit section with 4 events and retention (S06 pass)

## Anti-Example

INPUT: "Set up access rules"

BAD OUTPUT:
```yaml
---
id: access_rules
kind: permission
title: "Access"
quality: 7.5
roles: admin
read: yes
write: yes
---

## Rules
- Admins can do everything
- Others should ask for permission
- Be reasonable about access
```

FAILURES:
1. id: no p09_perm_ prefix -> H02 FAIL
2. pillar: missing -> H05 FAIL
3. quality: self-scored 7.5 instead of null -> H06 FAIL
4. roles: string instead of list -> H09 FAIL
5. read: "yes" not valid enum (must be allow/deny/conditional) -> H07 FAIL
6. write: "yes" not valid enum -> H07 FAIL
7. execute: missing entirely -> H07 FAIL
8. scope: missing -> H08 FAIL
9. "Admins can do everything": no granularity, no conditions -> S03 FAIL
10. "Be reasonable": subjective, not enforceable -> S03 FAIL
11. No Access Matrix section -> S03 FAIL
12. No Deny List section -> S05 FAIL
13. No Audit section -> S06 FAIL
14. No Escalation section -> S07 FAIL
