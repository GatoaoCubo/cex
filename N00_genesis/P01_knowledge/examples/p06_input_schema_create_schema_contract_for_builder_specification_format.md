---
id: p06_is_builder_specification
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
scope: "builder specification creation — defines the identity, capabilities, routing, and crew role of a CEX builder"
fields:
  - name: "builder_id"
    type: "string"
    required: true
    default: null
    description: "Unique builder identifier in kebab-case (e.g., input-schema-builder)"
    error_message: "builder_id is required — provide a kebab-case identifier"
  - name: "kind"
    type: "string"
    required: true
    default: null
    description: "Builder category: type_builder, content_builder, config_builder, code_builder, or eval_builder"
    error_message: "kind is required — must be one of: type_builder, content_builder, config_builder, code_builder, eval_builder"
  - name: "pillar"
    type: "string"
    required: true
    default: null
    description: "Target output pillar code (P01–P12) where built artifacts are stored"
    error_message: "pillar is required — must be P01 through P12"
  - name: "domain"
    type: "string"
    required: true
    default: null
    description: "Specialized domain or subject area the builder covers (e.g., input_schema, agent, workflow)"
    error_message: "domain is required — name the artifact type or subject area"
  - name: "identity"
    type: "string"
    required: true
    default: null
    description: "One-sentence statement of what this builder specializes in and knows"
    error_message: "identity is required — describe the builder's expertise in one sentence"
  - name: "capabilities"
    type: "list"
    required: true
    default: null
    description: "Enumerated list of what this builder can produce or perform (min 3 items)"
    error_message: "capabilities is required — list at least 3 concrete builder actions"
  - name: "routing_keywords"
    type: "list"
    required: true
    default: null
    description: "Lowercase keywords used by the router to match this builder (min 3)"
    error_message: "routing_keywords is required — provide at least 3 discovery keywords"
  - name: "routing_triggers"
    type: "list"
    required: true
    default: null
    description: "Natural language phrases that activate this builder (min 2)"
    error_message: "routing_triggers is required — provide at least 2 trigger phrases"
  - name: "crew_role"
    type: "string"
    required: true
    default: null
    description: "Role label in multi-builder crews: SPECIALIST, ORCHESTRATOR, or VALIDATOR"
    error_message: "crew_role is required — specify the builder's function in a crew"
  - name: "llm_function"
    type: "string"
    required: false
    default: "PRODUCE"
    description: "Primary 8F function: CONSTRAIN, BECOME, INJECT, REASON, CALL, PRODUCE, GOVERN, or COLLABORATE"
    error_message: null
  - name: "max_turns"
    type: "integer"
    required: false
    default: 25
    description: "Maximum LLM turns allowed per build execution"
    error_message: null
  - name: "version"
    type: "string"
    required: false
    default: "1.0.0"
    description: "Semantic version of this builder specification"
    error_message: null
  - name: "author"
    type: "string"
    required: false
    default: "builder_agent"
    description: "Identity of the agent or person that produced this spec"
    error_message: null
  - name: "tags"
    type: "list"
    required: false
    default: []
    description: "Classification tags for indexing and retrieval (include builder kind)"
    error_message: null
coercion:
  - from: "string"
    to: "string"
    rule: "pillar: normalize 'p06' → 'P06' — uppercase P-prefix always"
  - from: "string"
    to: "string"
    rule: "llm_function: normalize lowercase 'produce' → 'PRODUCE' — uppercase always"
  - from: "string"
    to: "integer"
    rule: "max_turns: parse numeric string '25' → 25; reject non-numeric strings with error"
  - from: "string"
    to: "list"
    rule: "capabilities/routing_keywords/routing_triggers: comma-separated string → list of trimmed strings"
examples:
  - builder_id: "input-schema-builder"
    kind: "type_builder"
    pillar: "P06"
    domain: "input_schema"
    identity: "Specialist in building unilateral entry contracts with typed fields, defaults, and coercion rules."
    capabilities:
      - "Define typed field contracts with required/optional semantics"
      - "Specify coercion rules for mixed-type input normalization"
      - "Produce complete input_schema artifacts with frontmatter"
    routing_keywords: ["input-schema", "input", "contract", "fields", "entry"]
    routing_triggers: ["define input contract for this agent", "what data does X need"]
    crew_role: "SPECIALIST"
    llm_function: "PRODUCE"
    max_turns: 25
  - builder_id: "agent-builder"
    kind: "type_builder"
    pillar: "P02"
    domain: "agent"
    identity: "Specialist in constructing autonomous agent definitions with identity, tools, and routing."
    capabilities:
      - "Define agent identity and role"
      - "Specify tool access and permissions"
      - "Compose agent routing rules for discovery"
    routing_keywords: ["agent", "autonomous", "specialist", "nucleus"]
    routing_triggers: ["build an agent for", "create a specialist agent"]
    crew_role: "SPECIALIST"
domain: "builder-specification"
quality: 9.1
tags: [input-schema, builder-specification, routing, capabilities, P06]
tldr: "Input contract for builder specs: requires identity, capabilities, routing keywords/triggers, crew role, and pillar assignment."
density_score: 0.91
keywords: [builder_spec, input_schema, routing, capabilities, crew_role, pillar, domain, llm_function]
related:
  - bld_schema_kind
  - bld_schema_dataset_card
  - bld_schema_action_paradigm
  - bld_schema_agent_profile
  - bld_schema_voice_pipeline
  - bld_schema_sandbox_config
  - bld_schema_search_strategy
  - bld_schema_safety_policy
  - bld_schema_usage_report
  - bld_schema_input_schema
---
## Contract Definition

Builder specification creation receives structured input defining a CEX builder's identity, functional scope, routing surface, and crew position. Callers provide a kebab-case identifier, output pillar, artifact domain, a one-sentence identity, enumerated capabilities, router keywords, natural language trigger phrases, and a crew role label. Optional fields cover the 8F function, execution limits, versioning, authorship, and tags. The receiver produces a complete builder spec (bld_manifest + ISOs) that the 8F pipeline, cex_query router, and crew orchestrator can consume.

## Fields

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | builder_id | string | YES | — | Kebab-case unique identifier |
| 2 | kind | string | YES | — | Builder category (type/content/config/code/eval) |
| 3 | pillar | string | YES | — | Output pillar P01–P12 |
| 4 | domain | string | YES | — | Artifact type or subject area |
| 5 | identity | string | YES | — | One-sentence expertise statement |
| 6 | capabilities | list | YES | — | Concrete builder actions (min 3) |
| 7 | routing_keywords | list | YES | — | Router discovery keywords (min 3) |
| 8 | routing_triggers | list | YES | — | Activation phrases (min 2) |
| 9 | crew_role | string | YES | — | SPECIALIST / ORCHESTRATOR / VALIDATOR |
| 10 | llm_function | string | NO | "PRODUCE" | Primary 8F function |
| 11 | max_turns | integer | NO | 25 | Max LLM turns per build |
| 12 | version | string | NO | "1.0.0" | Spec semver |
| 13 | author | string | NO | "builder_agent" | Producer identity |
| 14 | tags | list | NO | [] | Classification tags |

## Coercion Rules

| From | To | Rule |
|------|----|------|
| string (lowercase) | string (uppercase) | pillar "p06" → "P06"; llm_function "produce" → "PRODUCE" |
| string (numeric) | integer | max_turns "25" → 25; reject non-numeric strings |
| comma-separated string | list | capabilities, routing_keywords, routing_triggers split on "," with strip |

## Examples

```json
{
  "builder_id": "workflow-builder",
  "kind": "type_builder",
  "pillar": "P03",
  "domain": "workflow",
  "identity": "Specialist in composing multi-step workflow definitions with branching, signals, and handoffs.",
  "capabilities": [
    "Define sequential and parallel step graphs",
    "Specify branch conditions and fallback paths",
    "Compose handoff signals between nuclei"
  ],
  "routing_keywords": ["workflow", "pipeline", "steps", "dag", "sequence"],
  "routing_triggers": ["build a workflow for", "create a step-by-step pipeline"],
  "crew_role": "SPECIALIST",
  "llm_function": "PRODUCE",
  "max_turns": 25
}
```

```json
{
  "builder_id": "validator-builder",
  "kind": "eval_builder",
  "pillar": "P06",
  "domain": "validator",
  "identity": "Specialist in building pass/fail validation rule sets for artifact quality enforcement.",
  "capabilities": [
    "Define HARD and SOFT validation gates",
    "Specify per-field rule expressions",
    "Produce rejection messages with remediation hints"
  ],
  "routing_keywords": ["validator", "validation", "gate", "check", "enforce"],
  "routing_triggers": ["validate this artifact", "define quality gates for"],
  "crew_role": "VALIDATOR"
}
```

## References

- CEX kinds_meta.json — canonical kind and pillar registry
- archetypes/builders/ — builder directory structure (13 ISOs per builder)
- .claude/rules/n03-8f-enforcement.md — 8F pipeline functions reference

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_kind]] | related | 0.42 |
| [[bld_schema_dataset_card]] | related | 0.41 |
| [[bld_schema_action_paradigm]] | related | 0.41 |
| [[bld_schema_agent_profile]] | related | 0.41 |
| [[bld_schema_voice_pipeline]] | related | 0.40 |
| [[bld_schema_sandbox_config]] | related | 0.40 |
| [[bld_schema_search_strategy]] | related | 0.39 |
| [[bld_schema_safety_policy]] | related | 0.39 |
| [[bld_schema_usage_report]] | related | 0.39 |
| [[bld_schema_input_schema]] | related | 0.39 |
