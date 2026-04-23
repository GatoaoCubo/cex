---
kind: quality_gate
id: p11_qg_context_file
pillar: P03
llm_function: GOVERN
purpose: Golden and anti-examples of context_file artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.1
title: 'Gate: context_file'
version: 1.0.0
author: n03_builder
tags:
- eval
- P03
- quality_gate
- examples
tldr: Validates context_file artifacts for correct scope, injection_point, instruction-only
  body, and inheritance chain integrity.
domain: context_file
created: '2026-04-18'
updated: '2026-04-18'
density_score: 0.92
related:
  - p11_qg_system_prompt
  - p11_qg_validator
  - p11_qg_quality_gate
  - p11_qg_type_def
  - p11_qg_validation_schema
  - p11_qg_chunk_strategy
  - p11_qg_prompt_template
  - bld_knowledge_card_quality_gate
  - p11_qg_constraint_spec
  - p11_qg_runtime_state
---

## Quality Gate

## Definition
A context_file is a static, project-scoped instruction file auto-injected into agent context.
It must carry behavioral rules (not facts, not template vars, not procedural recipes) and
be correctly scoped with a valid injection strategy. This gate ensures scope taxonomy
correctness, body instruction purity, byte budget compliance, and inheritance chain validity.

## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.

| ID | Check | Rule |
|----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid with no syntax errors |
| H02 | id regex match | `id` matches `^ctx_[a-z][a-z0-9_]+$` |
| H03 | id equals filename stem | `id` slug matches the filename stem |
| H04 | kind literal | `kind` is exactly `context_file` |
| H05 | quality is null | `quality` field is `null` (never self-scored) |
| H06 | scope valid | `scope` is one of: `workspace`, `nucleus`, `session`, `global` |
| H07 | injection_point valid | `injection_point` is one of: `session_start`, `every_turn`, `f3_inject` |
| H08 | body has instruction sections | Body contains at least one `##` section with >= 3 rule items |

## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Scale to 0-10.

| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Byte budget respected | 1.0 | body_bytes <= max_bytes |
| No template vars in body | 1.0 | Body contains no `{{var}}` placeholders |
| No facts in body | 1.0 | Body contains behavioral rules only (no "X is defined as...", no citations) |
| inheritance_chain valid | 0.5 | All parent IDs in chain reference existing context_files |
| hermes_origin tag present | 0.5 | `tags` list contains `hermes_origin` |
| scope name in tags | 0.5 | `tags` list contains the scope value |
| density_score present | 0.5 | `density_score` field populated |
| Child does not duplicate parent rules | 1.0 | Rules in body are not exact copies of inheritance_chain parent rules |
| applies_to_nuclei valid | 0.5 | Value is `[all]` or contains valid nucleus IDs (n01-n07) |
| priority is non-negative integer | 0.5 | `priority` >= 0 |
| Body has >= 3 rules | 1.0 | Total instruction items across all sections >= 3 |
| ALWAYS/NEVER pattern used | 0.5 | At least 50% of rules use ALWAYS or NEVER prefix |

Sum of weights: 9.0. `soft_score = sum(weight * gate_score) / 9.0 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN -- archive to HERMES context_file pool as reference |
| >= 8.0 | PUBLISH -- safe to activate for scope injection |
| >= 7.0 | REVIEW -- usable but scope or body needs clarification |
| < 7.0 | REJECT -- do not activate; injection will produce unreliable results |

## Bypass
| Field | Value |
|-------|-------|
| condition | Temporary session_scope file created during rapid prototyping (scope: session, expires on close) |
| approver | Nucleus owner for that session |
| audit_log | Entry in `.cex/runtime/decisions/` with session ID and bypass justification |
| expiry | Session close; no durable bypass allowed |

H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.

## Examples

# Examples: context-file-builder

## Golden Example 1 -- Workspace Scope (CLAUDE.md equivalent)
INPUT: "Create workspace context file for the CEX engineering repo"
OUTPUT:
```yaml
id: ctx_cex_workspace
kind: context_file
pillar: P03
title: "CEX Engineering Workspace Context"
scope: workspace
injection_point: session_start
inheritance_chain: []
max_bytes: 8192
priority: 0
applies_to_nuclei: [all]
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "n03_builder"
quality: null
tags: [quality_gate, context_file, P03]
tldr: "Standing rules for all nuclei in the CEX engineering workspace."
density_score: 0.91
```
## Build Rules
1. ALWAYS follow the 8F pipeline (F1-F8) for every artifact produced
2. NEVER commit without compiling (`python _tools/cex_compile.py {path}`) and signaling
3. ALWAYS set `quality: null` -- never self-score
4. NEVER use non-ASCII characters in .py or .ps1 files
5. ALWAYS save artifacts to the correct pillar directory before compiling

## Commit Rules
1. ALWAYS prefix commit messages with `[N0X] ` where X is the nucleus ID
2. NEVER amend published commits -- create a new commit instead
3. ALWAYS run `python _tools/cex_doctor.py` after wave completion

WHY THIS IS GOLDEN:
- scope: workspace + inheritance_chain: [] (root, correct for CLAUDE.md equivalent)
- injection_point: session_start (cheapest; rules are stable)
- body: instructions only -- no facts, no template vars, no procedural recipes
- quality: null (H05 pass)
- id matches ^ctx_ pattern (H02 pass)
- hermes_origin in tags (S05 pass)
- 8 rules across 2 sections >= 3 minimum (H08 pass)

---

## Golden Example 2 -- Nucleus Scope (per-builder conventions)
INPUT: "Create nucleus context file for N03 builder nucleus"
OUTPUT:
```yaml
id: ctx_n03_nucleus
kind: context_file
pillar: P03
title: "N03 Engineering Nucleus Build Conventions"
scope: nucleus
injection_point: session_start
inheritance_chain: [ctx_cex_workspace]
max_bytes: 4096
priority: 2
applies_to_nuclei: [n03]
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "n03_builder"
quality: null
tags: [context_file, nucleus, n03, hermes_origin, builder]
tldr: "N03-specific build conventions: ISO structure, kind taxonomy, HERMES wave naming."
density_score: 0.90
```
## ISO Structure Rules
1. ALWAYS produce all 13 ISOs for any new builder kind
2. ALWAYS name ISOs `bld_{iso_type}_{kind}.md` in kebab-case builder directory
3. NEVER skip bld_schema, bld_instruction, or bld_manifest ISOs -- they are mandatory

## Kind Registry Rules
1. ALWAYS update `_schema.yaml`, `kind_index.md`, `.cex/kinds_meta.json`, and p03_pc_cex_universal.md for any new kind
2. ALWAYS update sub-agent definition in `.claude/agents/{kind}-builder.md`

WHY THIS IS GOLDEN:
- scope: nucleus + applies_to_nuclei: [n03] (correctly scoped)
- inheritance_chain: [ctx_cex_workspace] (correctly inherits from broader scope)
- priority: 2 (correctly higher number than workspace priority: 1)
- body: new rules only; does NOT duplicate workspace rules (child extends parent)
- max_bytes: 4096 (narrower scope, smaller budget -- correct)

---

## Golden Example 3 -- Session Scope (ephemeral sprint context)
INPUT: "Create session context for HERMES assimilation sprint"
OUTPUT:
```yaml
id: ctx_hermes_sprint_session
kind: context_file
pillar: P03
title: "HERMES Assimilation Sprint Session Context"
scope: session
injection_point: f3_inject
inheritance_chain: [ctx_n03_nucleus, ctx_cex_workspace]
max_bytes: 2048
priority: 3
applies_to_nuclei: [n03]
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "n03_builder"
quality: null
tags: [context_file, session, hermes_origin, sprint, ephemeral]
tldr: "Ephemeral context for HERMES W1 wave: 4 kinds, HERMES tags, stub contracts."
density_score: 0.88
```
## HERMES Wave Rules
1. ALWAYS tag HERMES-origin artifacts with `hermes_origin` in tags
2. ALWAYS include `upstream_source` field referencing NousResearch/hermes-agent
3. NEVER implement live platform code in HERMES stubs -- spec only (DP5)
4. ALWAYS note stub contract in kind KC boundary table

WHY THIS IS GOLDEN:
- scope: session + injection_point: f3_inject (ephemeral + on-demand = minimal token cost)
- inheritance_chain covers both nucleus and workspace (correct full chain)
- priority: 3 (correctly highest number = last override in session)
- expires on session close (auto-cleanup, no manual removal needed)

---

## Anti-Example
INPUT: "Create context file for code review"
BAD OUTPUT:
```yaml
id: code_review_context
kind: context
pillar: prompt
scope: all
injection: always
quality: 8.5
tags: [context, code]
```
Code review context: Be helpful. Give good feedback. Review code carefully.
FACTS: Code review is the process of examining source code to identify defects.
Variables: REVIEWER_NAME should check FILE_PATH.

FAILURES:
1. id: no `ctx_` prefix -> H02 FAIL
2. kind: "context" not "context_file" -> H04 FAIL
3. pillar: "prompt" not "P03" -> H01 FAIL
4. scope: "all" not in enum -> H06 FAIL
5. injection: "always" not in enum -> H07 FAIL
6. quality: 8.5 (not null) -> H05 FAIL
7. Body contains facts: "Code review is the process..." -> S03 FAIL
8. Body contains template var placeholders in body -> S02 FAIL
9. Rules are soft guidance ("Be helpful") not ALWAYS/NEVER -> S12 FAIL
10. Missing: inheritance_chain, max_bytes, priority, applies_to_nuclei -> H01 FAIL
11. tags missing hermes_origin -> S05 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
