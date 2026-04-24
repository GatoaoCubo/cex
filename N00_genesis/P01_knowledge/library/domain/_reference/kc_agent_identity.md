---
id: p01_kc_agent_identity
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Agent Identity — Lenses, Mental Models, Model Cards, Boot Configs, ISO Packages, Axioms"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: identity
origin: manual
quality: 9.1
tags: [agent, identity, lens, mental-model, model-card, boot, iso, axiom, persona, config]
tldr: "Agent identity defines WHO an agent is — its cognitive lens, mental model, model selection, boot sequence, ISO packaging, and invariant axioms"
when_to_use: "Building or classifying components that define agent persona, configuration, packaging, or foundational rules"
keywords: [lens, mental_model, model_card, boot_config, agent_package, axiom, identity, persona]
long_tails:
  - "How to define agent cognitive lenses and map them to CEX lens kind"
  - "Which identity YAML structures map to CEX mental_model kind"
  - "How ISO packages bundle agent capabilities into deployable units"
axioms:
  - "Identity is not decoration — it constrains reasoning boundaries and tool selection"
  - "Mental models are the agent's worldview; they determine what the agent notices and ignores"
  - "Axioms are invariant rules that survive context compression — they never change per session"
linked_artifacts:
  primary: null
  related: [p01_kc_routing_resilience, p01_kc_prompt_engineering, p01_kc_langchain_patterns]
feeds_kinds:
  - lens           # Cognitive perspectives, domain focus filters, attention biases
  - mental_model   # Identity YAML, worldview maps, domain ontologies
  - model_card     # LLM selection criteria, capability profiles, cost/latency tradeoffs
  - boot_config    # Startup sequences, environment loading, MCP wiring, flag sets
  - agent_package    # Agent packaging (manifest + instructions + examples + schema)
  - axiom          # Invariant rules, hard constraints, non-negotiable behaviors
density_score: 0.88
related:
  - agent-builder
  - p01_kc_lens
  - lens-builder
  - bld_architecture_agent
  - bld_collaboration_lens
  - bld_architecture_lens
  - p01_kc_agent
  - bld_collaboration_agent
  - p03_sp_lens_builder
  - p03_ins_lens
---

# Agent Identity

## Quick Reference
```yaml
topic: Agent Identity & Configuration Patterns
scope: Lenses, mental models, model cards, boot configs, ISO packages, axioms
source: organization framework (records/agents/, records/agent_groups/)
criticality: high
```

## Key Concepts

| Concept | Category | CEX Kind | Role |
|---------|----------|----------|------|
| Cognitive Lens | Perspective | lens | Filters what the agent attends to (e.g., security-first, cost-first) |
| Domain Lens | Perspective | lens | Restricts reasoning to a specific domain (marketing, engineering) |
| Persona Lens | Perspective | lens | Communication style and tone constraints |
| Identity YAML | Worldview | mental_model | Structured self-description (domain, tools, constraints) |
| Domain Ontology | Worldview | mental_model | Concept hierarchy the agent reasons over |
| Capability Map | Worldview | mental_model | What the agent can and cannot do |
| LLM Profile | Selection | model_card | Model name, context window, cost, latency, strengths |
| Routing Score | Selection | model_card | Task-model fit score for intelligent dispatch |
| Benchmark Summary | Selection | model_card | Performance on domain-specific evaluations |
| Environment Loader | Startup | boot_config | Env vars, secrets, feature flags at boot |
| MCP Wiring | Startup | boot_config | Tool server connections and strict-mode config |
| Flag Set | Startup | boot_config | CLI flags (--dangerously-skip-permissions, -p, --no-chrome) |
| Agent Manifest | Packaging | agent_package | ISO_001: identity, version, capabilities list |
| Agent Instructions | Packaging | agent_package | ISO_002: step-by-step execution protocol |
| Agent Examples | Packaging | agent_package | ISO_003: 3+ input/output demonstrations |
| Agent Schema | Packaging | agent_package | ISO_004: input/output JSON schema |
| Hard Constraint | Rule | axiom | Never-violate rules (e.g., "never execute, only dispatch") |
| Quality Gate | Rule | axiom | Minimum score thresholds for output acceptance |
| Scope Fence | Rule | axiom | Paths/domains the agent must not touch |

## Patterns

| Trigger | Action |
|---------|--------|
| Define new agent | Create mental_model.yaml -> write ISO manifest -> add boot_config |
| Select model for task | Score task complexity -> match against model_cards -> route to best fit |
| Apply cognitive lens | Load lens definition -> filter context -> bias tool selection toward lens domain |
| Package agent for deploy | Bundle ISO_001-004 -> validate schema -> register in routing index |
| Enforce invariant rule | Load axioms at boot -> inject into system prompt -> validate outputs against axioms |
| Configure boot sequence | Define env vars -> wire MCP servers -> set CLI flags -> validate readiness |

## Anti-Patterns

- Defining agents without mental models (they become generic, unfocused)
- Selecting models by name instead of by task-model fit scoring
- Skipping ISO packaging (agents become undocumented, unroutable)
- Making axioms session-dependent (they must survive context compression)
- Hardcoding boot configs instead of parameterizing per environment
- Conflating lens (attention filter) with persona (communication style)

## CEX Mapping

```text
[axiom] -> constrains -> [mental_model] -> informs -> [lens] -> filters -> [reasoning]
[model_card] -> selects -> [boot_config] -> launches -> [agent_package] -> executes
```

## References

- source: organization records/agents/ structure, records/agent_groups/ PRIMEs
- related: p01_kc_routing_resilience, p01_kc_prompt_engineering

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-builder]] | downstream | 0.41 |
| [[p01_kc_lens]] | sibling | 0.39 |
| [[lens-builder]] | downstream | 0.38 |
| [[bld_architecture_agent]] | downstream | 0.38 |
| [[bld_collaboration_lens]] | downstream | 0.37 |
| [[bld_architecture_lens]] | downstream | 0.37 |
| [[p01_kc_agent]] | sibling | 0.36 |
| [[bld_collaboration_agent]] | downstream | 0.36 |
| [[p03_sp_lens_builder]] | downstream | 0.35 |
| [[p03_ins_lens]] | downstream | 0.34 |
