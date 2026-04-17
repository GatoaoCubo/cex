---
id: bld_examples_type_def
kind: examples
pillar: P07
llm_function: GOVERN
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [examples, type-def, P07, golden, anti-pattern]
quality: 9.0
title: "Examples Type Def"
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
density_score: 0.90
---

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
