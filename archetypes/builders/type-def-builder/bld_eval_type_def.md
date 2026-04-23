---
id: p11_qg_type_def
kind: quality_gate
pillar: P06
llm_function: GOVERN
version: 1.0.0
created: '2026-03-27'
updated: '2026-03-27'
author: builder
tags:
- eval
- P06
- quality_gate
- examples
quality: 9.0
title: 'Gate: Type Def'
tldr: Validates reusable type declarations for base type, constraints, serialization,
  and composition rules.
domain: type_def
density_score: 0.85
related:
  - p11_qg_system_prompt
  - bld_memory_type_def
  - type-def-builder
  - p11_qg_response_format
  - bld_examples_type_def
  - p11_qg_validation_schema
  - p11_qg_quality_gate
  - bld_knowledge_card_type_def
  - bld_output_template_type_def
  - bld_collaboration_type_def
---

## Quality Gate

## Definition
A type definition ofclares a named, reusable data structure: its base type, constraints, nullable semantics, serialization format, and composition rules. Type defs are consumed by validation schemas, validators, and code generators. This gate ensures every type def is machine-usable, unambiguous, and backward compatible.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p06_td_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `type_def` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `type_name`, `base_type`, `nullable` all defined and non-empty |
| H07 | Base type specified | `base_type` is present and comes from the controlled vocabulary in CONFIG.md |
| H08 | Constraints section present | Body contains a `## Constraints` section with at least one named constraint |
| H09 | Serialization format present | Body contains a `## Serialization` section specifying wire format (JSON, YAML, Protobuf, etc.) |
| H10 | Type name is PascalCase | `type_name` matches `^[A-Z][A-Za-z0-9]*$` |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | Definition is tight; no tautological descriptions or repeated field names |
| Constraints are machine-validatable | 1.0 | Each constraint is expressed as a checkable rule (min, max, pattern, enum) |
| Composition rules documented | 1.0 | Union, intersection, or tuple composition is explicit when base_type is composite |
| Nullable semantics explicit | 0.5 | `nullable: true` or `nullable: false` is set; absence is not acceptable |
| Generics parameters documented | 0.5 | If the type is generic, type parameters are named and constrained |
| Tags include type-def | 0.5 | `tags` list contains `"type-def"` |
| Inheritance chain documented | 0.5 | If the type extends another, the parent type is named with a reference |
| Valid and invalid examples | 1.0 | Body contains at least one valid instance and one invalid instance |
| Backward compatibility notes | 0.5 | If version > 1.0.0, breaking changes are listed in body |
| Consumers cross-referenced | 0.5 | Body or frontmatter lists at least one artifact that consumes this type |
Sum of weights: 7.5. `soft_score = sum(weight * gate_score) / 7.5 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as canonical type definition |
| >= 8.0 | PUBLISH — safe to reference in schemas and validators |
| >= 7.0 | REVIEW — usable but constraints or examples need work |
| < 7.0 | REJECT — do not reference; ambiguous or incomplete definition |
## Bypass
| Field | Value |
|-------|-------|
| condition | Bootstrapping a new domain where no controlled vocabulary exists yet and the type is needed to unblock other artifacts |
| approver | Architect responsible for the P06 pillar |
| audit_log | Entry required in `.claude/bypasses/type_def_{date}.md` noting which HARD gates are waived and why |
| expiry | 14 days; type must reach PUBLISH score before any dependent artifact is published |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.

## Examples

## Golden Example
```yaml
id: p06_td_agent_score
kind: type_def
pillar: P06
layer: spec
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
type_name: AgentScore
base_type: number
domain: quality
nullable: false
quality: 8.9
tags: [quality, scoring, agent, numeric]
tldr: "A bounded decimal representing an agent output quality score from 0.0 to 10.0."
## Definition
AgentScore represents the numeric quality evaluation of an agent-produced artifact within the CEX governance system. Scores drive pool eligibility, routing decisions, and golden artifact promotion. All scores are floating-point in [0.0, 10.0] with two decimal places of precision.
## Constraints
minimum: 0.0
maximum: 10.0
precision: 2
format: decimal
## Examples
- value: 9.5
  note: "Golden tier — qualifies for pool promotion"
- value: 7.3
  note: "Learning tier — experimental use only"
- value: 4.9
  note: "Below threshold — rejected, requires redo"
## Keywords
quality, score, rating, decimal, bounded, agent, governance, pool, tier
```
### WHY THIS IS GOLDEN
- **H01**: `id` matches `^p06_td_[a-z][a-z0-9_]*$` — `p06_td_agent_score` valid
- **H02**: `kind: type_def` present and correct
- **H03**: `pillar: P06` and `layer: spec` both set
- **H04**: `base_type: number` from controlled vocabulary
- **H05**: `constraints` is a structured object with 4 keyed entries
- **H06**: `nullable: false` explicitly stated
- **H07**: `quality: null` — correctly deferred to governance
- **H08**: 3 examples with values and notes present
- **S01**: `tldr` is a single precise sentence
- **S02**: `domain: quality` clearly scoped
- **S03**: `tags` has 4 entries (minimum 2)
- **S04**: `keywords` section present with 9 discovery terms
- **S05**: Definition prose explains domain role, not just what the field is
- **S06**: Examples span min, mid, and max semanticslly meaningful values
- 19 frontmatter fields populated — exceeds golden minimum
- Artifact is terse, no filler prose, body under 3072 bytes
## Anti-Example
```yaml
id: AgentScore
kind: type_definition
pillar: P6
version: v1
created: today
author: me
type_name: agent score
base_type: decimal
domain: quality
nullable: yes
quality: 8.5
tags: [score]
A score for agents. Should be between 0 and 10. Can be null sometimes.
Constraints: must be a number.
```
### FAILURES
1. **[H01]** `id: AgentScore` — violates pattern `^p06_td_[a-z][a-z0-9_]*$`; must be `p06_td_agent_score`
2. **[H02]** `kind: type_definition` — invalid; only `type_def` is accepted
3. **[H03]** `pillar: P6` — invalid shorthand; must be exactly `P06`
4. **[H04]** `base_type: decimal` — not in controlled vocabulary; must be `number`
5. **[H05]** `constraints: must be a number` — free-text string, not a structured object with keyed entries
6. **[H06]** `nullable: yes` — not a boolean; must be `true` or `false`
7. **[H07]** `quality: 8.5` — author must not assign quality; only governance assigns; must be `null`
8. **[H08]** No `examples` section in body — hard gate violation
9. **[S01]** No `tldr` field — recommended field absent
10. **[S03]** `tags` has only 1 entry — minimum is 2
11. **[S05]** Definition prose is vague ("should be between 0 and 10") — no structured constraints object
12. **[S06]** `version: v1` — not SemVer; must be `1.0.0`

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
