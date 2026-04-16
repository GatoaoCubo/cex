---
id: con_permission_n02
kind: permission
pillar: P09
nucleus: n02
title: Marketing Permission Rule
version: 1.0
quality: null
tags: [config, permission, access, marketing, governance]
---


<!-- 8F: F1 constrain=P09/permission F2 become=permission-builder F3 inject=nucleus_def_n02+n02_rules+kc_permission+P09_schema
     F4 reason=minimum_viable_access_control_for_marketing_nucleus F5 call=shell_command,apply_patch F6 produce=4506 bytes
     F7 govern=frontmatter_sections_ascii_density_linecount F8 collaborate=N02_marketing/config/con_permission_n02.md -->

# Purpose

| Item | Definition |
|------|------------|
| Mission fit | Access control model for N02 file and tool behavior |
| Creative Lust lens | Protects the high-signal seductive system from careless edits, broad writes, and reckless execution |
| Primary use | Read, write, and execute permissions inside the marketing nucleus |
| Scope | Codex or CLI-driven work on N02 artifacts in the shared repo |
| Why permissions matter | Desire-led output is fragile when every subject can edit everything |

## Values

| Subject | Resource | Actions Allowed | Explicit Deny |
|---------|----------|-----------------|---------------|
| n02_builder | N02_marketing/schemas/** | read, write | delete |
| n02_builder | N02_marketing/config/** | read, write | delete |
| n02_builder | N02_marketing/output/** | read, write | execute |
| n02_builder | N02_marketing/knowledge/** | read | write, delete |
| n02_builder | N02_marketing/rules/** | read | write, delete |
| n02_builder | P01_knowledge/library/kind/** | read | write, delete |
| n02_builder | .cex/runtime/handoffs/** | read | write, delete |
| n02_builder | _tools/cex_compile.py | execute, read | write |
| n02_builder | git commit operations | none | execute |
| external_subject | N02_marketing/** | read_only_by_handoff | write, delete, execute |

## Access Principles

| Principle | Enforcement |
|-----------|-------------|
| deny overrides allow | If a path is listed in deny, it stays blocked |
| minimum viable write set | Write only where the handoff requires output |
| no destructive cleanup | Delete is denied by default |
| compile optionality | Execute compile only when mission rules require it |
| no commit authority | N07 owns commit after verification |

## Tool Permission Map

| Tool Class | Status | Reason |
|------------|--------|--------|
| shell read commands | allow | Needed for context gathering |
| apply_patch | allow | Required for controlled file creation and updates |
| git add or commit | deny | Handoff blocks commit authority |
| destructive filesystem commands | deny | Violates safety and task scope |
| network fetch | allow_when_needed | Only if primary sources are required |

## Rationale

| Decision | Reason |
|----------|--------|
| Delete denied everywhere | Protects reference and source assets from accidental loss |
| Knowledge and rules read-only | Strategy should inform seductive output, not be mutated during production |
| Compile write denied on source files | Generated artifacts must not replace source truth |
| Git commit denied | Preserves orchestrator ownership of final repo history |
| External subject default deny | Prevents cross-nucleus contamination without explicit routing |

## Example

```yaml
permission_check:
  subject: n02_builder
  resource: N02_marketing/config/con_rate_limit_config_n02.md
  action: write
  result: allow
```

| Example Attempt | Result | Why |
|-----------------|--------|-----|
| Read KC from P01 | allow | Shared knowledge is a reference source |
| Write new schema in N02 | allow | Deliverable path is in scope |
| Delete old config | deny | Destructive action blocked |
| Commit changes | deny | Reserved for N07 |

## Escalation Policy

| Condition | Response |
|-----------|----------|
| Need cross-nucleus write | request explicit handoff update |
| Need delete permission | require user approval and narrow target |
| Need commit | stop and leave for N07 |
| Need secret exposure | deny and route through secret_config |

## Properties

| Property | Value |
|----------|-------|
| Kind | permission |
| Pillar | P09 |
| Nucleus | n02 |
| Subject model | n02_builder plus external_subject |
| Access style | allow list with explicit deny |
| Delete policy | deny by default |
| Commit policy | denied |
| Main risk prevented | uncontrolled mutation of marketing system assets |
| Enforcement target | workspace behavior |
| Save path | N02_marketing/config/con_permission_n02.md |
