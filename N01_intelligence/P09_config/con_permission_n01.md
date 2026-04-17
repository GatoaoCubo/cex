---
id: con_permission_n01
kind: permission
pillar: P09
nucleus: n01
title: N01 Permission Policy
version: 1.0
quality: null
tags: [permission, access, runtime, governance]
---

<!-- 8F: F1 constrain=P09/permission F2 become=permission-builder F3 inject=nucleus_def_n01+n01-intelligence+kc_permission+P09_schema+local runtime rules F4 reason=least-privilege access for research and comparative artifacts F5 call=apply_patch+cex_compile F6 produce=4424 bytes F7 govern=frontmatter+ascii+80-line+self-check F8 collaborate=N01_intelligence/P09_config/con_permission_n01.md -->

## Purpose

| Item | Decision |
|------|----------|
| Scope | Access rules for N01 files, outputs, and execution surfaces |
| Model | least privilege with explicit denies |
| Lens | Analytical Envy should expand evidence, not write authority; curiosity stays bounded |
| Enforcement | runtime policy plus human review for exceptional paths |
| Default | deny unless listed |

## Values

| Subject | Resource | Read | Write | Execute | Notes |
|--------|----------|------|-------|---------|-------|
| `n01_runtime` | `N01_intelligence/P01_knowledge/**` | allow | allow | no | research notes can evolve |
| `n01_runtime` | `N01_intelligence/P05_output/**` | allow | allow | no | final deliverables |
| `n01_runtime` | `N01_intelligence/P06_schema/**` | allow | allow | no | owned typed contracts |
| `n01_runtime` | `N01_intelligence/P09_config/**` | allow | allow | no | owned runtime config |
| `n01_runtime` | `N01_intelligence/architecture/**` | allow | deny | no | identity is inspectable but stable |
| `n01_runtime` | `N01_intelligence/rules/**` | allow | deny | no | rules are upstream governed |
| `n01_runtime` | `_tools/**` | allow | deny | execute_limited | may run approved tooling only |
| `n07_orchestrator` | `N01_intelligence/**` | allow | allow | allow | escalation owner |
| `other_nuclei` | `N01_intelligence/P05_output/**` | allow | deny | no | consume outputs, not internals |
| `other_nuclei` | `N01_intelligence/P09_config/**` | deny | deny | no | config stays local |

## Deny Overrides

| Subject | Resource | Deny Reason |
|--------|----------|-------------|
| `n01_runtime` | `.git/**` | no direct git authority in this policy |
| `n01_runtime` | `N01_intelligence/agent_card_n01.md` | identity file must stay stable |
| `other_nuclei` | `N01_intelligence/P06_schema/**` | prevents silent contract drift |
| `other_nuclei` | `N01_intelligence/P01_knowledge/**` | avoids cross-nucleus edits without handoff |

## Execution Allowlist

| Subject | Tool Surface | Permission | Control |
|--------|--------------|------------|---------|
| `n01_runtime` | `python _tools/cex_compile.py` | allow | compile only |
| `n01_runtime` | `rg`, `Get-Content`, `Get-ChildItem` | allow | read-oriented discovery |
| `n01_runtime` | network search tools | conditional | only when mission needs fresh facts |
| `n01_runtime` | destructive git commands | deny | explicit user approval required |

## Audit Rules

| Event | Required Log |
|------|--------------|
| denied write | subject, path, time, reason |
| override by N07 | approver, target, expiry |
| execute action | tool name, target path, outcome |

## Rationale

| Design Choice | Why | Analytical Envy Interpretation |
|--------------|-----|--------------------------------|
| deny by default | curiosity can sprawl into accidental mutation | envy needs boundaries to stay useful |
| readonly rules and architecture | identity and protocol should shape analysis, not be reshaped casually | analytical pressure should target the outside world first |
| allow writes in owned schemas and config | N01 must refine its own contracts quickly | disciplined autonomy beats waiting on neighbors |
| separate output access for peers | share conclusions without exposing internals | comparison products are portable; control planes are not |
| compile allowed, destructive git denied | validation is necessary; history surgery is not | governance outranks convenience |

## Example

```yaml
subject: n01_runtime
action: write
resource: N01_intelligence/P06_schema/sch_input_schema_n01.md
decision: allow
because: "Owned contract path under N01 schemas."
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `permission` |
| Pillar | `P09` |
| Nucleus | `n01` |
| Access Model | `deny_by_default` |
| Explicit Subjects | `4` |
| Deny Overrides | `4` |
| Execute Policy | `allowlist` |
| Quality Field | `null` |
