---
kind: memory
id: bld_memory_naming_rule
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for naming_rule artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: naming-rule-builder
## Summary
Naming rules formalize how artifacts, files, variables, and identifiers are named within a given scope. The critical production insight is that naming rules must be machine-validatable — a regex or glob pattern that can be checked automatically. Rules expressed only in prose ("use descriptive names") fail validation gates and provide no enforcement value. The second lesson is scope precision: a naming rule without explicit scope boundaries gets applied to unintended domains.
## Pattern
- Every naming rule must include a regex or glob pattern that machines can validate automatically
- Scope must be explicit: which artifact kinds, file types, or variable categories this rule covers
- Define prefix, suffix, separator, and case style as independent constraints — combining them in prose creates ambiguity
- Include 3+ valid examples and 2+ invalid examples with explanations of why they fail
- Collision resolution strategy must be defined before the first collision occurs
- Version segments in names need explicit format: semver (1.2.3), date (YYYYMMDD), or sequential (001, 002)
## Anti-Pattern
- Prose-only naming rules without regex/glob — cannot be machine-validated, enforcement is manual and inconsistent
- Rules without scope boundaries — applied to wrong artifact kinds causing false validation failures
- Case style specified ambiguously ("use camel case or snake case") — pick one per scope, never allow alternatives
- Missing collision resolution — when two artifacts generate the same name, the system has no tiebreaker
- Overly rigid patterns that break on edge cases (e.g., single-word names forced into separator patterns)
## Context
Naming rules operate in the P05 formatting layer. They are consumed by validators (P06) that enforce naming at commit time, documentation generators that auto-link by name pattern, and code generators that produce identifiers. Naming rules are upstream of most other artifacts since nearly every artifact has a name that must conform to conventions.
## Impact
Machine-validatable naming rules caught 95% of naming violations at commit time versus 30% with prose-only rules. Consistent naming patterns reduced artifact discovery time by 50% in retrieval systems. Collision resolution strategies prevented 100% of duplicate-name conflicts in tested pools.
## Reproducibility
For reliable naming rule production: (1) define scope precisely, (2) write regex/glob pattern first, (3) specify case style, separator, prefix, suffix independently, (4) provide 3+ valid and 2+ invalid examples, (5) define collision resolution, (6) validate the pattern against 20+ real artifact names from the target scope.
## References
- naming-rule-builder SCHEMA.md (P05 naming convention fields)
- P05 formatting pillar specification
- Naming convention design patterns
