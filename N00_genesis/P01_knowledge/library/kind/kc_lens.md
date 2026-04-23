---
id: p01_kc_lens
kind: knowledge_card
type: kind
pillar: P02
title: "Lens — Deep Knowledge for lens"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: lens
quality: 9.1
tags: [lens, p02, INJECT, kind-kc]
tldr: "Specialized perspective overlay — adds domain expertise to an agent without creating a new agent identity"
when_to_use: "Building, reviewing, or reasoning about lens artifacts"
keywords: [lens, perspective, domain-expert, overlay, specialization]
feeds_kinds: [lens]
density_score: null
related:
  - lens-builder
  - bld_architecture_lens
  - bld_collaboration_lens
  - p03_ins_lens
  - p01_kc_agent
  - p03_sp_lens_builder
  - bld_schema_lens
  - bld_memory_lens
  - p11_qg_lens
  - bld_knowledge_card_lens
---

# Lens

## Spec
```yaml
kind: lens
pillar: P02
llm_function: INJECT
max_bytes: 2048
naming: p02_lens_{{perspective}}.md + .yaml
core: false
```

## What It Is
A lens is a specialized perspective injected into an agent to shift its reasoning toward a particular domain or viewpoint without changing the agent's core identity. Unlike an agent (which has full capabilities, tools, and routing), a lens adds expertise on top of an existing agent. It is NOT a mental_model (which includes routing rules and decision trees for the agent itself). Lenses answer "how should I think about this specific domain?" — agents answer "who am I?" and mental_models answer "how do I decide?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | System prompt augmentation | Additional context injected alongside base prompt |
| LlamaIndex | Query transform / `HyDEQueryTransform` | Transforms the perspective of query processing |
| CrewAI | Agent `backstory` modification | Perspective shift via backstory injection |
| DSPy | `dspy.InputField` with domain context | Typed perspective as an input field |
| Haystack | `PromptBuilder` with perspective slot | Template variable for domain expertise |
| OpenAI | Assistant additional_instructions | Runtime perspective injection on top of base instructions |
| Anthropic | System prompt addendum | Additional system block with domain perspective |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| perspective | string | required | More specific = better domain coverage but narrower applicability |
| applies_to | list | required | Wider applicability = more reuse but less precision |
| priority | int | medium | Higher priority = overrides base agent perspective |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Domain expert lens | Agent needs vertical expertise | "Brazilian e-commerce compliance" lens on generic listing agent |
| Audience lens | Same content for different audiences | "Technical" vs "Executive" lens on research agent |
| Regulatory lens | Compliance-specific perspective | "ANVISA" lens for health product descriptions |
| Cultural lens | Localization perspective | "Brazilian Portuguese" lens with cultural nuances |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Lens with tools/capabilities | That's an agent, not a lens | If it needs tools, create a full agent instead |
| Too many lenses stacked | Conflicting perspectives; incoherent output | Max 2 lenses per agent per task |
| Lens duplicating agent identity | Redundant tokens; version drift | Lens adds perspective, doesn't redefine identity |

## Integration Graph
```
[knowledge_card, context_doc] --> [lens] --> [agent (P02)]
                                    |
                             [template (P03)]
```

## Decision Tree
- IF need a full autonomous specialist THEN agent
- IF need perspective shift on existing agent THEN lens
- IF need routing and decision rules THEN mental_model
- IF need domain background without perspective THEN context_doc
- DEFAULT: lens when augmenting an existing agent for a specific vertical

## Quality Criteria
- GOOD: Clear perspective defined; applies_to specified; adds non-obvious domain expertise
- GREAT: Tested with target agents; measurable output quality improvement; no overlap with agent identity
- FAIL: Contains capabilities or tools (should be agent); perspective is generic; duplicates context_doc content

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[lens-builder]] | related | 0.55 |
| [[bld_architecture_lens]] | downstream | 0.55 |
| [[bld_collaboration_lens]] | related | 0.54 |
| [[p03_ins_lens]] | downstream | 0.53 |
| [[p01_kc_agent]] | sibling | 0.52 |
| [[p03_sp_lens_builder]] | downstream | 0.47 |
| [[bld_schema_lens]] | downstream | 0.45 |
| [[bld_memory_lens]] | downstream | 0.45 |
| [[p11_qg_lens]] | downstream | 0.41 |
| [[bld_knowledge_card_lens]] | sibling | 0.40 |
