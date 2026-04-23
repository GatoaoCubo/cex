---
id: p01_kc_axiom
kind: knowledge_card
type: kind
pillar: P02
title: "Axiom — Deep Knowledge for axiom"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: axiom
quality: 9.1
tags: [axiom, p02, BECOME, kind-kc]
tldr: "Immutable fundamental principle — part of the entity's deep identity that never changes regardless of context"
when_to_use: "Building, reviewing, or reasoning about axiom artifacts"
keywords: [axiom, principle, immutable, identity, governance]
feeds_kinds: [axiom]
density_score: null
related:
  - bld_knowledge_card_axiom
  - p10_lr_axiom-builder
  - p03_sp_axiom_builder
  - bld_collaboration_axiom
  - axiom-builder
  - bld_architecture_axiom
  - bld_config_axiom
  - tpl_axiom
  - p11_qg_axiom
  - bld_instruction_axiom
---

# Axiom

## Spec
```yaml
kind: axiom
pillar: P02
llm_function: BECOME
max_bytes: 3072
naming: p10_ax_{{rule}}.md
core: true
```

## What It Is
An axiom is a fundamental, immutable principle that forms part of an entity's deep identity. Unlike laws (P08, operationally adjustable rules) or instructions (P03, flexible directives), axioms cannot be overridden by context, user requests, or runtime conditions. They represent the non-negotiable core values and constraints of the system. Axioms answer "what must ALWAYS be true?" — laws answer "what should usually be true?" and instructions answer "what should I do now?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Constitutional AI principles | `ConstitutionalChain` with immutable principles |
| LlamaIndex | System-level guardrails | Hardcoded validation in query pipeline |
| CrewAI | Agent `allow_delegation` + process constraints | Structural constraints, not content-level |
| DSPy | `dspy.Assert` / `dspy.Suggest` | Assert = hard constraint (axiom-like); Suggest = soft |
| Haystack | Pipeline validation rules | Pre/post-processing validators |
| OpenAI | Usage policies / system prompt rules | Model-level safety constraints |
| Anthropic | Constitutional AI / system prompt blocks | Immutable safety rules in system context |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| rule | string | required | More specific = easier to enforce but less flexible |
| scope | enum | system-wide | Narrower scope = fewer conflicts but gaps in coverage |
| priority | int | highest | Axioms always override laws and instructions |
| enforcement | enum | hard | Hard = reject violation; soft = warn (but soft is a law, not axiom) |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Safety axiom | Prevent harmful outputs | "NEVER generate content that enables physical harm" |
| Identity axiom | Maintain consistent persona | "ALWAYS identify as organization, never claim to be human" |
| Quality axiom | Non-negotiable output standards | "NEVER output with quality < 7.0 without explicit flag" |
| Boundary axiom | Prevent scope creep | "NEVER execute code — only dispatch to agent_groups" (orchestrator) |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Too many axioms (>10) | Over-constrained; conflicts emerge; LLM struggles to satisfy all | Keep axioms minimal; move adjustable rules to laws (P08) |
| Vague axioms | "Be good" is unenforceable | Make axioms specific and testable |
| Axioms that should be laws | Operational rules change; calling them axioms blocks improvement | If rule might need adjustment, it's a law not an axiom |

## Integration Graph
```
[system identity] --> [axiom] --> [agent (P02), law (P08)]
                        |
                 [boot_config, mental_model]
```

## Decision Tree
- IF rule is immutable and identity-defining THEN axiom
- IF rule is operational and may need adjustment THEN law (P08)
- IF rule is task-specific and context-dependent THEN instruction (P03)
- IF rule defines safety boundaries THEN axiom
- DEFAULT: law (P08) — most rules should be adjustable; axioms are rare

## Quality Criteria
- GOOD: Clear, specific, testable statement; marked as immutable; no overlap with laws
- GREAT: Minimal set (<10); each axiom has clear enforcement mechanism; tested for conflict-freedom
- FAIL: Vague or aspirational; overlaps with existing laws; too many (>15); contains "should" instead of "must/never"

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_axiom]] | sibling | 0.53 |
| [[p10_lr_axiom-builder]] | downstream | 0.52 |
| [[p03_sp_axiom_builder]] | downstream | 0.52 |
| [[bld_collaboration_axiom]] | downstream | 0.49 |
| [[axiom-builder]] | downstream | 0.49 |
| [[bld_architecture_axiom]] | downstream | 0.46 |
| [[bld_config_axiom]] | downstream | 0.44 |
| [[tpl_axiom]] | related | 0.44 |
| [[p11_qg_axiom]] | downstream | 0.41 |
| [[bld_instruction_axiom]] | downstream | 0.41 |
