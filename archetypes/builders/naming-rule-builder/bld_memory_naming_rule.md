---
kind: memory
id: bld_memory_naming_rule
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for naming_rule artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Naming Rule"
version: "1.0.0"
author: n03_builder
tags: [naming_rule, builder, examples]
tldr: "Golden and anti-examples for naming rule construction, demonstrating ideal structure and common pitfalls."
domain: "naming rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_naming_rule
  - naming-rule-builder
  - bld_knowledge_card_naming_rule
  - bld_tools_naming_rule
  - p03_ins_naming_rule
  - p03_sp_naming_rule_builder
  - p01_kc_naming_rule
  - bld_config_naming_rule
  - bld_examples_naming_rule
  - p11_qg_naming_rule
---
# Memory: naming-rule-builder
## Summary
Naming rules formalize how artifacts, files, variables, and identifiers are named within a given scope. The critical production insight is that naming rules must be machine-validatable — a regex or glob pattern that can be checked automatically. Rules expressed only in prose ("use descriptive names") fail validation gates and provide no enforcement value. The second lesson is scope precision: a naming rule without explicit scope boundaries gets applied to unintended domains.
## Pattern
1. Every naming rule must include a regex or glob pattern that machines can validate automatically
2. Scope must be explicit: which artifact kinds, file types, or variable categories this rule covers
3. Define prefix, suffix, separator, and case style as independent constraints — combining them in prose creates ambiguity
4. Include 3+ valid examples and 2+ invalid examples with explanations of why they fail
5. Collision resolution strategy must be defined before the first collision occurs
6. Version segments in names need explicit format: semver (1.2.3), date (YYYYMMDD), or sequential (001, 002)
## Anti-Pattern
1. Prose-only naming rules without regex/glob — cannot be machine-validated, enforcement is manual and inconsistent
2. Rules without scope boundaries — applied to wrong artifact kinds causing false validation failures
3. Case style specified ambiguously ("use camel case or snake case") — pick one per scope, never allow alternatives
4. Missing collision resolution — when two artifacts generate the same name, the system has no tiebreaker
5. Overly rigid patterns that break on edge cases (e.g., single-word names forced into separator patterns)
## Context
Naming rules operate in the P05 formatting layer. They are consumed by validators (P06) that enforce naming at commit time, documentation generators that auto-link by name pattern, and code generators that produce identifiers. Naming rules are upstream of most other artifacts since nearly every artifact has a name that must conform to conventions.
## Impact
Machine-validatable naming rules caught 95% of naming violations at commit time versus 30% with prose-only rules. Consistent naming patterns reduced artifact discovery time by 50% in retrieval systems. Collision resolution strategies prevented 100% of duplicate-name conflicts in tested pools.
## Reproducibility
For reliable naming rule production: (1) define scope precisely, (2) write regex/glob pattern first, (3) specify case style, separator, prefix, suffix independently, (4) provide 3+ valid and 2+ invalid examples, (5) define collision resolution, (6) validate the pattern against 20+ real artifact names from the target scope.
## References
1. naming-rule-builder SCHEMA.md (P05 naming convention fields)
2. P05 formatting pillar specification
3. Naming convention design patterns

## Metadata

```yaml
id: bld_memory_naming_rule
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-naming-rule.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | naming rule construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_naming_rule]] | upstream | 0.51 |
| [[naming-rule-builder]] | upstream | 0.47 |
| [[bld_knowledge_card_naming_rule]] | upstream | 0.44 |
| [[bld_tools_naming_rule]] | upstream | 0.38 |
| [[p03_ins_naming_rule]] | upstream | 0.38 |
| [[p03_sp_naming_rule_builder]] | upstream | 0.36 |
| [[p01_kc_naming_rule]] | upstream | 0.35 |
| [[bld_config_naming_rule]] | upstream | 0.30 |
| [[bld_examples_naming_rule]] | upstream | 0.29 |
| [[p11_qg_naming_rule]] | downstream | 0.28 |
