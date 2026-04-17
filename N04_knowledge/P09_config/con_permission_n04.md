---
id: con_permission_n04
kind: permission
pillar: P09
nucleus: n04
title: Knowledge Permission Matrix
version: 1.0
quality: 9.0
tags: [config, permission, knowledge, access, governance]
density_score: 1.0
---
<!-- 8F: F1 constrain=P09/permission F2 become=permission-builder F3 inject=n04-knowledge+kc_permission+P09 examples+N04 ownership model F4 reason=least-privilege access for evidence-rich knowledge assets F5 call=shell,apply_patch F6 produce=4454 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/P09_config/con_permission_n04.md -->
# Knowledge Permission Matrix
## Purpose
Knowledge assets are valuable because they accumulate evidence, provenance, and organizational memory.
The Knowledge Gluttony lens pushes N04 to store a lot, but that makes access control more important, not less: hungry systems must know who may read, write, execute, and export knowledge-bearing resources.
This permission artifact defines the least-privilege matrix for N04 resources.
## Values
| Subject | Resource | Read | Write | Execute | Export | Notes |
|---------|----------|------|-------|---------|--------|-------|
| n04_knowledge | schemas_dir | yes | yes | no | yes | owns schema authoring |
| n04_knowledge | config_dir | yes | yes | no | yes | owns config authoring |
| n04_knowledge | prompts_dir | yes | limited | no | no | prompt edits require explicit review |
| n04_knowledge | compiled_dir | yes | yes | no | yes | compiler outputs |
| n04_knowledge | cache_dir | yes | yes | yes | no | may purge and rebuild cache |
| n07_admin | runtime_handoffs | yes | limited | no | yes | orchestration intake oversight |
| n07_admin | runtime_signals | yes | yes | no | yes | may coordinate signal flow |
| n01_intelligence | schemas_dir | yes | no | no | no | may consult contracts only |
| n05_operations | cache_dir | yes | limited | yes | no | runtime troubleshooting only |
| humans_reviewers | export_dir | yes | limited | no | yes | consume audit bundles |
## Deny Rules
| Subject | Deny | Reason |
|---------|------|--------|
| all non-n04 nuclei | write to `schemas_dir` and `config_dir` | ownership boundary |
| all subjects except n04 and n05 | execute on `cache_dir` | prevent unsupervised cache mutation |
| all subjects | delete `runtime_handoffs` | handoffs are evidence records |
| all subjects except approved reviewers | export contested records without audit tag | protects disputed knowledge |
## Escalation
| Scenario | Escalation path |
|----------|-----------------|
| urgent fix to N04 config | request N07 approval with scope and expiry |
| cache rebuild during outage | N05 gets temporary execute on cache_dir |
| prompt rewrite | N04 owner plus reviewer sign-off |
| contested knowledge export | audit ticket and reviewer identity required |
## Example
```yaml
subject: n05_operations
resource: ${CEX_ROOT}/_data/n04_cache
actions: [read, execute]
write: limited
expires_at: 2026-04-17T03:00:00Z
reason: "Rebuild embedding cache after provider outage"
```
## Rationale
| Decision | Knowledge Gluttony angle | Benefit |
|----------|--------------------------|---------|
| deny broad writes | evidence hoarding becomes corruption if everyone edits history | ownership remains legible |
| preserve handoffs | N04 learns from task lineage too | audit trail survives |
| export contested data carefully | hungry systems keep conflicts, but exports must show context | lower misinformation risk |
| allow N05 limited cache execution | operational recovery should not require schema ownership transfer | fast remediation |
| separate export from read | not every reader should mass-distribute knowledge | reduces spill risk |
## Enforcement Model
| Layer | Mechanism |
|-------|-----------|
| documentation | this matrix is the declared policy |
| runtime | wrapper tools map aliases to allow or deny decisions |
| audit | signal log records escalations and temporary grants |
| review | N07 oversees exceptions and expiry |
## Properties
| Property | Value |
|----------|-------|
| Permission model | RBAC with explicit deny override |
| Primary owner | `n04_knowledge` |
| Temporary grants allowed | yes |
| Export tracked | yes |
| Delete on handoffs | denied |
| Cross-nucleus write access | denied by default |
| Cache execute path | tightly scoped |
| Contested-data handling | reviewer gated |
| Audit expectation | every escalation logged |
| Governing principle | least privilege with evidence preservation |
