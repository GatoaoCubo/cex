---
id: p11_qg_permission
kind: quality_gate
pillar: P11
title: "Gate: permission"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: permission
quality: 9.0
tags: [quality-gate, permission, P11, P09, governance, access-control, security]
tldr: "Gates for permission artifacts — roles, operations, deny-by-default, audit trail, and escalation path defined."
density_score: 0.85
llm_function: GOVERN
---
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
