---
id: p03_ins_context_file
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-04-18
updated: 2026-04-18
author: context-file-builder
title: "Context File Builder Instructions"
target: "context-file-builder agent"
phases_count: 5
prerequisites:
  - "Target scope is defined: workspace | nucleus | session | global"
  - "Injection point is known or can be derived from use case"
  - "At least 3 standing behavioral rules can be derived from the scope"
  - "Parent context_files in inheritance chain are known (or chain is empty)"
validation_method: checklist
domain: context_file
quality: 9.1
tags: [instruction, context-file, workspace, hermes_origin, P03]
idempotent: true
atomic: false
rollback: "Delete generated context_file and revert inheritance_chain in parent"
dependencies: []
logging: true
tldr: "Build a static instruction context_file with correct scope, injection_point, inheritance_chain, and instruction-only body."
density_score: 0.93
llm_function: REASON
related:
  - p03_ins_system_prompt
  - bld_instruction_context_doc
  - p03_ins_path_config
  - p06_is_quality_audit
  - p03_ins_validation_schema
  - bld_instruction_instruction
  - p03_ins_naming_rule
  - bld_instruction_input_schema
  - bld_collaboration_memory_scope
  - bld_instruction_action_prompt
---

## Context
The context-file-builder produces a `context_file` artifact -- a static, project-scoped instruction
file automatically injected into agent context windows. It implements the HERMES CLAUDE.md / AGENTS.md
pattern: standing behavioral rules for a scope that shape every agent turn without redefining identity.

**Critical distinction**: a context_file is INSTRUCTIONS (behavioral rules, standing constraints) not
FACTS (knowledge_card), not IDENTITY (system_prompt), not PARAMETERIZED (prompt_template), not
PROCEDURAL RECIPE (instruction kind). Confusing these types produces broken injection behavior.

**Input contract**:
- `scope_domain`: the target workspace, nucleus, session, or global context
- `scope_type`: enum -- `workspace` | `nucleus` | `session` | `global`
- `injection_point`: enum -- `session_start` | `every_turn` | `f3_inject`
- `parent_context_files`: list of parent IDs (empty = root)
- `priority`: integer (0 = highest authority)
- `applies_to_nuclei`: `[all]` or list of nucleus IDs
- `rules`: list of standing behavioral rules for this scope (min 3)

**Output contract**: a single `context_file` artifact with 13 required frontmatter fields and
instruction-only body sections stored at the appropriate pillar path.

## Phases

### Phase 1: Classify Scope and Injection Strategy
**Action**: Determine correct scope and injection_point from inputs.
```
scope_map = {
    "all sessions all nuclei":      "global",
    "all nuclei one project":       "workspace",
    "one nucleus all sessions":     "nucleus",
    "current session only":         "session"
}
scope = scope_map[derived_coverage]

injection_map = {
    "stable rules loaded once":     "session_start",  -- cheapest, most common
    "compliance-critical per turn": "every_turn",      -- expensive, use sparingly
    "on-demand via 8F pipeline":    "f3_inject"        -- zero cost until called
}
injection_point = injection_map[use_case_urgency]
```
Verifiable exit: scope and injection_point are both set with justification.

### Phase 2: Build Inheritance Chain
**Action**: Identify parent context_files this artifact inherits from.
```
IF scope == "global":
    inheritance_chain = []   # root; nothing to inherit
ELIF scope == "workspace":
    inheritance_chain = [global_ctx_id] IF global exists ELSE []
ELIF scope == "nucleus":
    inheritance_chain = [workspace_ctx_id, global_ctx_id] filtered to existing
ELIF scope == "session":
    inheritance_chain = [nucleus_ctx_id, workspace_ctx_id, global_ctx_id] filtered to existing

FOR each parent_id in inheritance_chain:
    ASSERT parent_id is a valid existing context_file id
    ASSERT parent_id scope is broader than this context_file's scope
```
Child extends parent. Override only what differs; never duplicate parent rules.
Verifiable exit: inheritance_chain contains valid parent IDs or is empty.

### Phase 3: Author Instruction Body
**Action**: Write static behavioral rules for this scope.
```
FOR each rule_domain in derived_rule_set:
    section = "## " + rule_domain_title
    FOR each rule in rule_domain:
        ASSERT rule is an instruction (behavioral) NOT a fact (knowledge)
        ASSERT rule has no "{{vars}}" placeholders
        ASSERT rule is actionable and verifiable
    body += section + rule_list

ASSERT len(all_rules) >= 3
ASSERT body_bytes <= max_bytes
ASSERT no_facts_in_body (redirect facts to knowledge_card)
ASSERT no_template_vars (redirect to prompt_template)
```
Verifiable exit: body has >= 1 section, >= 3 rules, all instructions, <= max_bytes.

### Phase 4: Compose context_file Frontmatter
**Action**: Assemble all resolved values into the 13-field YAML structure.
Required fields in order:
1. `id` -- `ctx_{{scope_slug}}` -- regex: `^ctx_[a-z][a-z0-9_]+$`
2. `kind` -- `context_file`
3. `pillar` -- `P03`
4. `title` -- human-readable scope description
5. `scope` -- workspace | nucleus | session | global
6. `injection_point` -- session_start | every_turn | f3_inject
7. `inheritance_chain` -- list of parent IDs (may be empty)
8. `max_bytes` -- integer (default 8192)
9. `priority` -- 0 = most authoritative
10. `applies_to_nuclei` -- [all] or explicit list
11. `version` -- "1.0.0"
12. `quality` -- null (invariant -- never self-score)
13. `tags` -- list >= 3; include scope name and `hermes_origin`

Verifiable exit: YAML parses cleanly; all 13 fields present; quality is null.

### Phase 5: Validate Against Quality Gates
**Action**: Run HARD gates before emitting; log SOFT gates as warnings.
```
HARD gates (all must pass):
  H01: Frontmatter parses as valid YAML -- no syntax errors
  H02: id matches regex ^ctx_[a-z][a-z0-9_]+$
  H03: id equals filename stem
  H04: kind is exactly "context_file"
  H05: quality is null
  H06: scope is one of: workspace, nucleus, session, global
  H07: injection_point is one of: session_start, every_turn, f3_inject
  H08: body contains at least one ## section with >= 3 rule items

SOFT gates (warnings):
  S01: body_bytes <= max_bytes
  S02: no {{vars}} in body
  S03: no facts in body (no "X is defined as", no citations)
  S04: inheritance_chain references valid existing context_file IDs
  S05: tags include scope name
  S06: tags include "hermes_origin"
  S07: density_score field present
```
Verifiable exit: all HARD gates pass; SOFT gate failures logged with remediation.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_system_prompt]] | sibling | 0.24 |
| [[bld_instruction_context_doc]] | sibling | 0.23 |
| [[p03_ins_path_config]] | sibling | 0.22 |
| [[p06_is_quality_audit]] | downstream | 0.22 |
| [[p03_ins_validation_schema]] | sibling | 0.22 |
| [[bld_instruction_instruction]] | sibling | 0.21 |
| [[p03_ins_naming_rule]] | sibling | 0.20 |
| [[bld_instruction_input_schema]] | sibling | 0.20 |
| [[bld_collaboration_memory_scope]] | downstream | 0.20 |
| [[bld_instruction_action_prompt]] | sibling | 0.20 |
