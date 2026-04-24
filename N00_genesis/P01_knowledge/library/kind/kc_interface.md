---
id: p01_kc_interface
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P06
title: "Interface — Deep Knowledge for interface"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: interface
quality: 9.1
tags: [interface, P06, CONSTRAIN, kind-kc]
tldr: "Bilateral integration contract specifying both input and output shapes between two communicating agents."
when_to_use: "Building, reviewing, or reasoning about interface artifacts"
keywords: [interface, contract, bilateral, agent-to-agent]
feeds_kinds: [interface]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_input_schema
  - interface-builder
  - p03_sp_interface_builder
  - bld_architecture_interface
  - bld_collaboration_input_schema
  - bld_architecture_input_schema
  - p01_kc_type_def
  - p01_kc_handoff_protocol
  - p03_sp_input_schema_builder
  - p10_lr_interface_builder
---

# Interface

## Spec
```yaml
kind: interface
pillar: P06
llm_function: CONSTRAIN
max_bytes: 3072
naming: p06_iface_{{contract}}.yaml
core: false
```

## What It Is
A bilateral contract that defines both the input and output schemas for a communication channel between two agents or pipeline stages. Specifies caller obligations AND callee guarantees in one file. NOT an input_schema (unilateral—only the caller side). NOT a signal (P12—event with no structured payload; fire-and-forget, no response contract).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | RunnableInterface | Typed Runnable with input/output TypeVars |
| LlamaIndex | QueryPipeline edge | Typed connection between pipeline nodes |
| CrewAI | Agent handoff schema | Task context passing between agents |
| DSPy | Module signature | Inputs + Outputs defined in Signature |
| Haystack | ComponentSocket pair | Input + Output socket type pair |
| OpenAI | Assistant thread protocol | Message schema for multi-agent threads |
| Anthropic | Tool + response schema | tool_use + tool_result shape contract |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| input | input_schema ref | required | Loose = flexible but unsafe |
| output | type_def ref | required | Strict = predictable downstream |
| version | semver | 1.0.0 | Minor = compatible, major = breaking |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Agent handoff | Output of A is input of B | p06_iface_research_to_writer.yaml |
| Tool protocol | Tool caller + tool responder | p06_iface_search_tool.yaml |
| Versioned upgrade | Evolving contracts without breaking | v1 -> v2 with backward compat shim |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Undocumented implicit contract | Breaks silently on schema change | Always codify as interface file |
| Using input_schema for bidirectional | Misses output contract | Use interface when both sides matter |
| Duplicating type_defs inline | Drift between interface + type files | Reference type_def, never duplicate |

## Integration Graph
```
[input_schema] --> [interface] --> [type_def (output)]
[enum_def] ------> [interface]
                       |-------> [agent (P02) caller]
                       |-------> [agent (P02) callee]
```

## Decision Tree
- IF only defining inputs THEN input_schema
- IF defining both input + output for an agent pair THEN interface
- IF event-only with no structured payload THEN signal (P12)
- DEFAULT: interface for any stable agent-to-agent channel

## Quality Criteria
- GOOD: Both input and output sections declared, versioned, named for the pair
- GREAT: SemVer tracked, backward-compat notes, linked to both agent README files
- FAIL: Only input OR output defined, no version, inline duplicate type definitions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_input_schema]] | sibling | 0.45 |
| [[interface-builder]] | related | 0.37 |
| [[p03_sp_interface_builder]] | upstream | 0.36 |
| [[bld_architecture_interface]] | downstream | 0.36 |
| [[bld_collaboration_input_schema]] | downstream | 0.32 |
| [[bld_architecture_input_schema]] | downstream | 0.31 |
| [[p01_kc_type_def]] | sibling | 0.30 |
| [[p01_kc_handoff_protocol]] | sibling | 0.29 |
| [[p03_sp_input_schema_builder]] | upstream | 0.29 |
| [[p10_lr_interface_builder]] | downstream | 0.28 |
