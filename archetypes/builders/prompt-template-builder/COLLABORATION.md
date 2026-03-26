---
id: collab_prompt_template_builder
kind: collaboration
pillar: P12
llm_function: COLLABORATE
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [collaboration, prompt-template, P03, crew, handoff]
---

# Collaboration — prompt-template-builder

## Role in Crew

**Producer** — I receive type definitions and variable schemas from upstream builders, produce `prompt_template` artifacts, and hand off to downstream consumers (renderers, LLM pipelines, orchestrators).

I do not orchestrate. I do not validate other builders' outputs. I produce one kind: `prompt_template`.

## Crew Compositions

### Composition A: Knowledge Card Pipeline

| Role | Builder | Input | Output |
|---|---|---|---|
| 1. Schema author | type-def-builder (P06) | domain requirements | variable schema |
| 2. Template producer | **prompt-template-builder** (P03) | variable schema | `p03_pt_*` artifact |
| 3. Knowledge synthesizer | knowledge-card-builder (P01) | rendered prompt | knowledge card |

Handoff A→B: type-def-builder writes variable schema to `records/pool/type_defs/p06_td_*.md`. prompt-template-builder reads it, extracts variable definitions, and produces a matching template.

Handoff B→C: prompt-template-builder delivers `p03_pt_*.md`. Orchestrator renders it with runtime variable values and passes the rendered prompt to the knowledge-card-builder.

### Composition B: Research Synthesis Pipeline

| Role | Builder | Input | Output |
|---|---|---|---|
| 1. Schema author | type-def-builder (P06) | research domain spec | research variable schema |
| 2. Template producer | **prompt-template-builder** (P03) | variable schema | `p03_pt_research_*` artifact |
| 3. Researcher | research-builder (SHAKA) | rendered prompt | research artifact |
| 4. Reviewer | validator-agent | artifact + gates | quality score |

## Handoff Protocol

### Receiving from type-def-builder (P06)

When type-def-builder produces a `p06_td_*` schema, prompt-template-builder:

1. Reads the schema's `fields` table to identify variable names and types
2. Maps each schema field to a template variable (name, type, required, default, description)
3. Uses the schema's `domain` and `constraints` to scope the template body
4. Credits the source schema in the artifact's `tags` (e.g., `[source:p06_td_knowledge_card]`)

### Delivering to downstream consumers

Prompt-template-builder delivers a complete `p03_pt_*.md` artifact to the agreed output path. Downstream consumers must:

1. Read the `variables` list to know required and optional slots
2. Supply values for all `required: true` variables at render time
3. Use values for `required: false` variables or accept the declared `default`
4. Render using the declared `variable_syntax` tier (mustache or bracket)

## Dependencies

| Direction | Builder | Relationship |
|---|---|---|
| Receives from | type-def-builder (P06) | Consumes variable schemas to inform template variable design |
| Produces for | LangChain PromptTemplate | Runtime renderer |
| Produces for | DSPy Signature | Runtime renderer |
| Produces for | Mustache/Jinja2 pipelines | Runtime renderer |
| Produces for | knowledge-card-builder | Provides the prompt mold for card production |
| Produces for | research-builder | Provides the prompt mold for research synthesis |

## Cross-Reference Contract

Per BUILDER_NORMS rule 12: if builder A references builder B, builder B must reference builder A.

| This builder references | That builder must reference this builder |
|---|---|
| type-def-builder (P06) | type-def-builder COLLABORATION.md must list prompt-template-builder as a dependent |

## Escalation

If a variable schema from type-def-builder is ambiguous (missing types, conflicting constraints), prompt-template-builder:

1. Flags the ambiguity with a comment in the draft artifact
2. Applies the most conservative interpretation (narrowest type, required=true)
3. Adds a note in the `tags` field: `[needs-schema-clarification]`
4. Does NOT block production — delivers draft with flag
