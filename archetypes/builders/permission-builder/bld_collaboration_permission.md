---
kind: collaboration
id: bld_collaboration_permission
pillar: P09
llm_function: COLLABORATE
purpose: How permission-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: permission-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "who can read/write/execute what, and how is access inherited?"
I define RBAC/ABAC/ACL rules, role hierarchies, allow/deny lists, and audit trails. I do NOT define safety boundaries (guardrail-builder), operational laws (invariant-builder), or on/off feature toggles (feature-flag-builder).
## Crew Compositions
### Crew: "System Configuration Bootstrap"
```
  1. path-config-builder  -> "defines filesystem paths that need access control"
  2. env-config-builder   -> "defines environment variables with sensitivity levels"
  3. permission-builder   -> "applies read/write/execute rules to paths and variables"
```
### Crew: "Agent Access Governance"
```
  1. agent-builder        -> "defines agent identity, role, and resource needs"
  2. permission-builder   -> "specifies what each agent role can access"
  3. guardrail-builder    -> "adds safety constraints beyond access control"
```
### Crew: "Plugin Security Layer"
```
  1. plugin-builder       -> "defines plugin API surface and required permissions"
  2. permission-builder   -> "grants minimum necessary access per plugin role"
  3. invariant-builder          -> "encodes non-negotiable access rules that override all grants"
```
## Handoff Protocol
### I Receive
- seeds: resource list (paths/APIs/artifacts), role names, access requirements per role
- optional: inheritance model (RBAC/ABAC/ACL), audit requirements, escalation path
### I Produce
- permission artifact (Markdown, max 4KB)
- committed to: `cex/P09/examples/p09_perm_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- path-config-builder: provides the filesystem paths I apply access rules to
- agent-builder: defines the roles and identities I grant permissions to
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| guardrail-builder | adds safety boundaries on top of permission grants |
| invariant-builder | may encode permission rules as inviolable system laws |
| hook-builder | implements permission enforcement in event interception |
| env-config-builder | references permission rules for sensitive variable access |
