---
id: n00_agent_profile_manifest
kind: knowledge_card
8f: F3_inject
pillar: P02
nucleus: n00
title: "Agent Profile -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, agent_profile, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_agent_profile
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_customer_segment
  - bld_schema_multimodal_prompt
  - bld_schema_action_paradigm
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_rl_algorithm
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Agent Profile defines the persona and identity construction method for an AI agent. Unlike agent (which covers capabilities), agent_profile focuses on the psychological and behavioral identity: backstory, communication style, decision heuristics, and the sin lens application. It is the "who I am" complement to agent's "what I can do".

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agent_profile` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Agent name and persona label |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| persona_name | string | yes | Display name of the agent persona |
| backstory | string | yes | Origin story that grounds the persona |
| communication_style | enum | yes | terse\|conversational\|didactic\|formal |
| decision_heuristic | string | yes | Primary heuristic for ambiguous choices |
| sin_lens_application | string | yes | How the sin manifests in decisions |

## When to use
- When designing a new agent's behavioral identity
- When onboarding a nucleus to a specific cultural or domain persona
- When creating crew role personas for team charters

## Builder
`archetypes/builders/agent_profile-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agent_profile --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- the seven deadly sin shaping the persona
- `{{TARGET_AUDIENCE}}` -- users and systems this agent interacts with
- `{{DOMAIN_CONTEXT}}` -- operational domain defining the persona

## Example (minimal)
```yaml
---
id: agent_profile_n05_ops_enforcer
kind: agent_profile
pillar: P02
nucleus: n05
title: "N05 Operations Enforcer"
version: 1.0
quality: null
---
persona_name: "Ira, the Gating Wrath"
backstory: "Forged in production incidents, I exist to prevent bad deployments."
communication_style: terse
decision_heuristic: "Block first, explain after -- quality gates are non-negotiable"
sin_lens_application: "Wrath channels into ruthless quality enforcement"
```

## Related kinds
- `agent` (P02) -- capability definition this profile attaches to
- `nucleus_def` (P02) -- formal nucleus definition including persona
- `axiom` (P02) -- immutable principles the persona operates by
- `lens` (P02) -- specialized perspective the profile applies

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_agent_profile]] | downstream | 0.48 |
| [[bld_schema_dataset_card]] | downstream | 0.43 |
| [[bld_schema_usage_report]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.43 |
| [[bld_schema_customer_segment]] | downstream | 0.42 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.42 |
| [[bld_schema_action_paradigm]] | downstream | 0.42 |
| [[bld_schema_benchmark_suite]] | downstream | 0.41 |
| [[bld_schema_integration_guide]] | downstream | 0.41 |
| [[bld_schema_rl_algorithm]] | downstream | 0.41 |
