---
id: p01_kc_naming_rule
kind: knowledge_card
type: kind
pillar: P08
title: "Naming Rule — Deep Knowledge for naming_rule"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: naming_rule
quality: 9.1
tags: [naming_rule, P08, GOVERN, kind-kc]
tldr: "naming_rule is a machine-checkable pattern governing artifact names within a bounded scope — enforcing pillar prefix, kind infix, and extension conventions."
when_to_use: "Building, reviewing, or reasoning about naming_rule artifacts"
keywords: [naming_convention, artifact_naming, pattern_enforcement]
feeds_kinds: [naming_rule]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - bld_collaboration_naming_rule
  - bld_memory_naming_rule
  - bld_knowledge_card_naming_rule
  - naming-rule-builder
  - bld_examples_naming_rule
  - p03_ins_naming_rule
  - bld_tools_naming_rule
  - bld_architecture_naming_rule
  - p01_kc_output_formatting
  - p11_qg_naming_rule
---

# Naming Rule

## Spec
```yaml
kind: naming_rule
pillar: P08
llm_function: GOVERN
max_bytes: 4096
naming: p05_nr_{{scope}}.md
core: false
```

## What It Is
A naming_rule is a machine-checkable regex pattern governing artifact names within a bounded scope — encoding pillar prefix, kind infix, descriptor, and extension conventions. It is NOT a validator (P06, which validates content/schema), NOT a type_def (P06, which defines a type's structure rather than its name).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Runnable naming conventions | snake_case for chain/tool names; no formal rule |
| LlamaIndex | Module naming | PascalCase classes, snake_case instances — Python conventions |
| CrewAI | Agent/task/crew naming | role as noun, task description as verb phrase |
| DSPy | Signature field naming | `InputField`/`OutputField` named by semantic role |
| Haystack | `@component` class naming | PascalCase class, snake_case output port names |
| OpenAI | Tool/function naming | snake_case, max 64 chars per API spec |
| Anthropic | Tool naming | snake_case, max 64 chars; `tool_use` id is UUID |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| scope | string | required | Which artifact type this rule governs |
| pattern | regex | required | Machine-checkable — tighter = safer, too tight = brittle |
| examples | list[str] | required | ≥2 positive + ≥1 negative — drives instant validation |
| exceptions | list[str] | [] | Named exceptions; more = rule erosion |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Pillar prefix | All artifacts scoped by pillar code | `p01_kc_`, `p08_law_`, `p09_env_` |
| Kind infix | Type encoded in the middle segment | `_kc_` for knowledge card, `_ac_` for agent card |
| Kebab-case agents | Multi-word agent/tool names | `tool-shed`, `scout-agent` (not `toolShed`) |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Free-form naming | Names without pattern become unsearchable | Always enforce pillar+kind prefix for P01-P12 |
| Abbreviation overload | `p08_ac_shl_crd` is unreadable after 3 months | Max 2 abbreviations per name segment |
| Missing scope | Naming rule without scope applies ambiguously | Always specify which artifact type the rule governs |

## Integration Graph
```
type_def, schema --> [naming_rule] --> validator, agent_card, path_config
                          |
                     law, decision_record, knowledge_card
```

## Decision Tree
- IF naming a P01-P12 artifact THEN {pillar}_{kind}_{descriptor}.{ext}
- IF naming a runtime/temp file THEN {prefix}_{timestamp}.{ext}
- IF naming a human-readable label/title THEN title case without restriction
- DEFAULT: `{pillar}_{kind}_{descriptor}.{ext}` — all lowercase, underscores

## Quality Criteria
- GOOD: scope, pattern (regex), positive examples, negative example all present
- GREAT: validator script linked, edge cases documented, migration guide for renames
- FAIL: pattern without examples, ambiguous scope, no machine-checkable form

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_naming_rule]] | upstream | 0.46 |
| [[bld_memory_naming_rule]] | downstream | 0.39 |
| [[bld_knowledge_card_naming_rule]] | sibling | 0.39 |
| [[naming-rule-builder]] | upstream | 0.35 |
| [[bld_examples_naming_rule]] | upstream | 0.35 |
| [[p03_ins_naming_rule]] | upstream | 0.34 |
| [[bld_tools_naming_rule]] | upstream | 0.33 |
| [[bld_architecture_naming_rule]] | related | 0.30 |
| [[p01_kc_output_formatting]] | sibling | 0.28 |
| [[p11_qg_naming_rule]] | downstream | 0.28 |
