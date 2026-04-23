---
kind: quality_gate
id: p11_qg_permission
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of permission artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: permission"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, permission, P11, P09, governance, access-control, security]
tldr: "Gates for permission artifacts — roles, operations, deny-by-default, audit trail, and escalation path defined."
domain: permission
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - bld_knowledge_card_permission
  - bld_examples_permission
  - permission-builder
  - bld_memory_permission
  - p03_sp_permission_builder
  - bld_schema_permission
  - bld_architecture_permission
  - p03_ins_permission
  - bld_output_template_permission
  - bld_collaboration_permission
---

## Quality Gate

# Gate: permission
## Definition
| Field     | Value                                              |
|-----------|----------------------------------------------------|
| metric    | role coverage completeness + deny-by-default enforcement |
| threshold | 8.0                                                |
| operator  | >=                                                 |
| scope     | all permission artifacts (P09)                     |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = permission silently open |
| H02 | id matches `^p09_perm_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "permission" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | scope field is non-empty string naming the resource or resource class being governed | Permission without scope = permission on everything |
| H08 | roles list has >= 1 entry | At least one role must exist to enforce anything |
| H09 | operations block declares read, write, and execute for each role (allow, deny, or conditional) | Missing operations imply allow — a dangerous default |
| H10 | default_access field is "deny" or explicitly justified if "allow" | Deny-by-default is the only safe baseline |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "permission" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | role_hierarchy block documents which roles inherit from which | 1.0 |
| S05 | allow_deny_precedence field states whether deny overrides allow or vice versa | 1.0 |
| S06 | inheritance_rules block explains how child resources derive permissions from parent | 0.5 |
| S07 | audit_trail block defines logged events and retention period | 1.0 |
| S08 | escalation_path block names approver role and max duration for temporary elevation | 1.0 |
| S09 | time_restrictions block documents any time-window or expiry constraints (null is acceptable if none) | 0.5 |
| S10 | access_matrix table covers all roles x operations combinations | 1.0 |
| S11 | examples block shows at least one allow and one deny scenario per role | 0.5 |
| S12 | No filler phrases ("this permission", "designed to control", "various roles") | 0.5 |
Weights sum: 9.0. Normalize: divide each by 9.0 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as referencand access control spec for this resource class |
| >= 8.0 | PUBLISH — enforce in runtime and register in security index |
| >= 7.0 | REVIEW — complete audit trail, escalation path, or role hierarchy |
| < 7.0  | REJECT — rework default_access and operations contract |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Incident response requiring emergency access grant with no time for full review |
| approver | p09-chief |
| audit_trail | Log in records/audits/ with grantee, resource, duration, and incident reference |
| expiry | 24h — emergency grant expires automatically; permanent change requires full gate pass |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

# Examples: permission-builder
## Golden Example
INPUT: "Create permission para controlar access de agents ao pool de knowledge cards"
OUTPUT:
```yaml
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
quality: 8.9
tags: [permission, pool, access-control, knowledge, roles]
tldr: "Controls read/write access to knowledge card pool by agent role with deny-overrides-allow"
domain: "knowledge management"
density_score: 0.89
inheritance: "orchestrator > researcher > builder > auditor > viewer"
escalation: "Request via signal to orchestrator with justification"
linked_artifacts:
  primary: "p11_gr_pool_integrity"
  related: [p08_law_pool_governance, p10_bi_pool_index]
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
id: access_rules
kind: permission
title: "Access"
quality: 7.5
roles: admin
read: yes
write: yes
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
