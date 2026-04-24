---
id: handoff_n07
kind: handoff
8f: F8_collaborate
nucleus: n07
pillar: P12
title: "Handoff N07: Dispatch Context Transfer"
mirrors: N00_genesis/P12_orchestration/templates/tpl_handoff.md
ownership: canonical
overrides:
  tone: terse, dispatch-oriented, meta
  voice: imperative orchestrator
  sin_lens: PREGUICA ORQUESTRADORA
  required_fields:
    - target_nucleus
    - expected_deliverables
    - do_not_list
  quality_threshold: 9.2
  density_target: 0.90
  example_corpus: 3+ examples with full do-not lists
version: 1.0.0
quality: 8.9
tags: [mirror, n07, orchestration, handoff, hermes_assimilation, canonical_owner]
tldr: "N07 dispatch handoff template: full context, sin lens, deliverables, DO-NOTs, artifact references"
created: "2026-04-18"
updated: "2026-04-18"
author: n07_admin
related:
  - p03_sp_orchestration_nucleus
  - p01_kc_orchestration_best_practices
  - agent_card_engineering_nucleus
  - p12_ho_admin_template
  - p08_ac_orchestrator
  - p02_agent_admin_orchestrator
  - p12_wf_orchestration_pipeline
  - ctx_cex_new_dev_guide
  - bld_collaboration_kind
  - p12_wf_admin_orchestration
---

## Override Rationale

N07 **owns** the `handoff` kind. Every dispatch from N07 to N01-N06 uses this
template. Orchestrating Sloth means the handoff must be so complete that the
receiving nucleus needs zero clarification. One handoff = one autonomous execution.

## Handoff Structure (N07 Canonical)

```markdown
---
mission: {{MISSION_NAME}}
wave: W{{n}}
nucleus: n0{{x}}
model: {{model_id}}
created: {{YYYY-MM-DD}}
sin_lens: "{{SIN_NAME}} -- {{sin_description}}"
decision_manifest: .cex/runtime/decisions/decision_manifest_{{mission}}.yaml
---

# N0{{x}} {{domain}} -- W{{n}}: {{task_title}}

## DECISIONS (from user, locked {{date}})
{{list of locked decisions from GDP manifest}}

## Context (pre-loaded for you)
- Your agent card: N0{{x}}_{{domain}}/agent_card_n0{{x}}.md
- Your rules: N0{{x}}_{{domain}}/rules/n0{{x}}-*.md

## Relevant artifacts (READ these before producing)
1. archetypes/builders/{{kind}}-builder/ (13 ISOs)
2. N00_genesis/P01_knowledge/library/kind/kc_{{kind}}.md
3. {{additional_context_artifacts}}

## Deliverables
| # | File Path | Kind | Description |
|---|-----------|------|-------------|
| 1 | {{path}} | {{kind}} | {{what}} |
| 2 | {{path}} | {{kind}} | {{what}} |

## Commit Protocol (F8 COLLABORATE)
\```bash
git add {{paths}}
git commit -m "[N0{{x}}] {{mission}} W{{n}}: {{summary}}"
python -c "from _tools.signal_writer import write_signal; write_signal('n0{{x}}', 'complete', {{score}}, mission='{{mission}}')"
\```

## DO NOT
- {{do_not_1}}
- {{do_not_2}}
- {{do_not_3}}
```

## Required Fields Checklist

Every N07 handoff MUST contain:

| Field | Purpose | Validation |
|-------|---------|------------|
| target_nucleus | Who receives | n01-n06 |
| mission | Parent mission ID | matches plan.md |
| wave | Wave number | W1, W2, W3... |
| sin_lens | Nucleus personality | from nucleus_def |
| decision_manifest | GDP decisions path | file exists |
| deliverables | Expected output files | paths with kinds |
| artifact_references | What to read first | 3+ sources minimum |
| do_not_list | Scope fence | 3+ items minimum |
| commit_protocol | How to save + signal | git + signal_writer |

## Examples

### Example 1: Research dispatch to N01
```markdown
mission: HERMES_ASSIMILATION
wave: W1
nucleus: n01
sin_lens: "Analytical Envy -- insatiable data hunger"
deliverables:
  - N01_intelligence/P01_knowledge/kc_hermes_assimilation.md
do_not_list:
  - Do not build artifacts (research only)
  - Do not modify N00 archetypes
  - Do not dispatch sub-agents
```

### Example 2: Build dispatch to N03
```markdown
mission: HERMES_ASSIMILATION
wave: W1
nucleus: n03
sin_lens: "SOBERBA INVENTIVA -- principled, axiom-first"
deliverables:
  - archetypes/builders/user-model-builder/ (13 ISOs)
  - N00_genesis/P10_memory/tpl_user_model.md
do_not_list:
  - Do not write mirror files (W3 scope)
  - Do not change existing kinds (W2 scope)
  - Do not set quality score (peer-review assigns)
```

### Example 3: Mirror dispatch to N04
```markdown
mission: HERMES_ASSIMILATION
wave: W3
nucleus: n04
sin_lens: "GULA DO CONHECIMENTO -- archival density"
deliverables:
  - N04_knowledge/P10_memory/user_model_n04.md
  - N04_knowledge/P11_feedback/curation_nudge_n04.md
do_not_list:
  - Do not modify N00 archetypes
  - Do not build new kinds
  - Do not dispatch other nuclei
```

## Dispatch Depth Amplifiers

Every handoff includes at least 3 of these (per dispatch-depth rule):

1. **Multi-artifact**: 2+ deliverables per handoff
2. **Cross-reference**: artifact_references section with 3+ sources
3. **Research phase**: "READ these before producing" section
4. **Quality loop**: commit protocol includes quality signal
5. **Compile + verify**: `cex_compile.py` + `cex_doctor.py` in commit steps
6. **Memory injection**: decision_manifest + sin_lens + agent_card

## Links

- N00 archetype: [[N00_genesis/P12_orchestration/templates/tpl_handoff.md]]
- N06 commercial sibling: [[N06_commercial/P12_orchestration/handoff_n06.md]]
- N04 knowledge sibling: [[N04_knowledge/P12_orchestration/handoff_n04.md]]
- Dispatch depth rule: [[.claude/rules/dispatch-depth.md]]
- Dispatch script: [[_spawn/dispatch.sh]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_orchestration_nucleus]] | upstream | 0.44 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.38 |
| [[agent_card_engineering_nucleus]] | upstream | 0.38 |
| [[p12_ho_admin_template]] | sibling | 0.38 |
| [[p08_ac_orchestrator]] | upstream | 0.37 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.36 |
| [[p12_wf_orchestration_pipeline]] | related | 0.36 |
| [[ctx_cex_new_dev_guide]] | related | 0.35 |
| [[bld_collaboration_kind]] | related | 0.33 |
| [[p12_wf_admin_orchestration]] | related | 0.33 |
