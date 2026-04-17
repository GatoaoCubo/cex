---
kind: examples
id: bld_examples_nucleus_def
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of nucleus_def artifacts
quality: 9.1
title: "Examples Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, examples]
tldr: "Golden and anti-examples of nucleus_def artifacts"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example

```markdown
---
id: p02_nd_n05.md
kind: nucleus_def
pillar: P02
nucleus_id: N05
role: operations
sin_lens: "Ira Construtiva -- Constructive Wrath"
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
| Sin Lens | Ira Construtiva -- Constructive Wrath |
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
sin_lens: "Ira Construtiva"
cli_binding: claude
model_tier: sonnet
---
```

## Why it fails:
N03 role is "builder" (Soberba Inventiva sin), not "operations".
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
