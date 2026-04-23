---
kind: quality_gate
id: p02_qg_nucleus_def
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for nucleus_def
quality: 9.0
title: "Quality Gate Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for nucleus_def"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_nucleus_def
  - bld_instruction_nucleus_def
  - bld_knowledge_card_nucleus_def
  - bld_schema_nucleus_def
  - p02_nd_n05.md
  - p10_lr_nucleus_def_builder
  - bld_collaboration_nucleus_def
  - bld_tools_nucleus_def
  - bld_output_template_nucleus_def
  - nucleus-def-builder
---

## Quality Gate

## Definition

| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Nucleus registry completeness | 7/7 (N01-N07) | equals | All active nuclei |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p02_nd_n0[0-7]\.md$ | ID format mismatch |
| H03 | kind field equals "nucleus_def" | Kind field incorrect or missing |
| H04 | nucleus_id is one of N00-N07 | Invalid or missing nucleus_id |
| H05 | role is valid enum value | Role not in: genesis, intelligence, marketing, builder, knowledge, operations, commercial, orchestrator |
| H06 | pillars_owned is non-empty array | Empty or missing pillars_owned |
| H07 | cli_binding matches nucleus_models.yaml | CLI mismatch with source of truth |
| H08 | boot_script path exists | boot/n0{X}.ps1 file not found |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D01 | Schema completeness (all required + recommended fields present) | 0.25 | All fields = 1.0, missing recommended = 0.7, missing required = 0 |
| D02 | Data accuracy (cli_binding + model_tier verified against nucleus_models.yaml) | 0.25 | Verified exact match = 1.0, reasonable estimate = 0.5, guessed = 0 |
| D03 | Composability (crew_templates_exposed + domain_agents populated and accurate) | 0.20 | Real templates + agents listed = 1.0, placeholder values = 0.5, empty = 0 |
| D04 | Fractal alignment (pillars_owned reflects actual artifact production) | 0.20 | Verified against agent_card = 1.0, estimated = 0.5, all-12 claimed = 0 |
| D05 | Boot contract validity (boot_script + handoff + signal format correct) | 0.10 | All three correct = 1.0, partial = 0.5, missing = 0 |

## Actions

| Score | Threshold | Action |
|-------|-----------|--------|
| GOLDEN | >=9.5 | Auto-register in nucleus registry |
| PUBLISH | >=8.0 | Auto-register after validation |
| REVIEW | >=7.0 | Require N07 review before registration |
| REJECT | <7.0 | Reject -- fix cli_binding, pillars_owned, or boot_script |

## Bypass

| Conditions | Approver | Audit Trail |
|------------|---------|-------------|
| New nucleus being bootstrapped (boot_script not yet created) | N07 Orchestrator | Decision manifest entry |

## Examples

## Golden Example

```markdown
---
id: p02_nd_n05.md
kind: nucleus_def
pillar: P02
nucleus_id: N05
role: operations
sin_lens: "Gating Wrath"
cli_binding: claude
model_tier: sonnet
model_specific: claude-sonnet-4-6
context_tokens: 200000
boot_script: boot/n05.ps1
agent_card_path: N05_operations/agent_card_n05.md
pillars_owned: [P07, P08, P09, P11]
crew_templates_exposed:
  - ci_cd_review_crew
  - deploy_gate_crew
  - test_automation_crew
domain_agents:
  - railway_superintendent
  - deploy_ops_agent
  - test_ops_agent
  - code_review_agent
fallback_cli: codex
title: "Nucleus Def N05"
quality: null
tags: [nucleus_def, n05, operations, composable]
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N05 |
| Role | operations |
| Sin Lens | Gating Wrath |
| CLI Binding | claude |
| Model Tier | sonnet |
| Model | claude-sonnet-4-6 |
| Context | 200000 tokens |
| Boot Script | `boot/n05.ps1` |
| Agent Card | `N05_operations/agent_card_n05.md` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|-------------|
| P07 | Evaluation | benchmark, golden_test, e2e_eval, scoring_rubric |
| P08 | Architecture | decision_record, component_map, diagram |
| P09 | Config | env_config, rate_limit_config, secret_config |
| P11 | Feedback | bugloop, regression_check, lifecycle_rule |
```

## Why it succeeds:
- nucleus_id is canonical (N05).
- role matches the operations domain.
- cli_binding verified against nucleus_models.yaml.
- pillars_owned reflects actual artifact production (P07/P08/P09/P11).
- crew_templates_exposed names concrete patterns (ci_cd_review_crew).
- domain_agents lists real agent files from N05_operations/P02_model/.

---

## Anti-Example 1: Wrong Pillar Assignment

```markdown
---
id: p02_nd_n05.md
kind: nucleus_def
nucleus_id: N05
role: operations
pillars_owned: [P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12]
---
```

## Why it fails:
Claiming ALL 12 pillars for a single nucleus violates the fractal contract.
N05 does not produce knowledge cards (P01), prompt templates (P03), or commercial
artifacts (P11). pillars_owned must reflect actual production, not aspirational scope.

---

## Anti-Example 2: Role/Nucleus Mismatch

```markdown
---
id: p02_nd_n03.md
kind: nucleus_def
nucleus_id: N03
role: operations
sin_lens: "Gating Wrath"
cli_binding: claude
model_tier: sonnet
---
```

## Why it fails:
N03 role is "builder" (Inventive Pride sin), not "operations".
The model_tier should be "opus" (N03 uses claude-opus-4-6).
Role must match the nucleus identity -- this would cause N07 to mis-route tasks to N03
thinking it is an operations nucleus.

---

## Anti-Example 3: Missing Boot Contract

```markdown
---
id: p02_nd_n01.md
kind: nucleus_def
nucleus_id: N01
role: intelligence
cli_binding: claude
model_tier: sonnet
---
```

## Why it fails:
Missing boot_script and agent_card_path. Without these, N07 cannot dispatch the nucleus
(boot scripts read handoff files) and cannot load the capability manifest. These fields
are REQUIRED for the nucleus to participate in orchestration.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
