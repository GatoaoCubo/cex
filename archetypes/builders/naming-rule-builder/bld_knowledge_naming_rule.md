---
kind: knowledge_card
id: bld_knowledge_card_naming_rule
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for naming_rule production — atomic searchable facts
sources: naming-rule-builder MANIFEST.md + SCHEMA.md, PEP 8, BEM CSS, DNS naming, NPM
quality: 9.1
title: "Knowledge Card Naming Rule"
version: "1.0.0"
author: n03_builder
tags: [naming_rule, builder, examples]
tldr: "Golden and anti-examples for naming rule construction, demonstrating ideal structure and common pitfalls."
domain: "naming rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_naming_rule
  - bld_memory_naming_rule
  - p01_kc_naming_rule
  - bld_collaboration_naming_rule
  - bld_examples_naming_rule
  - p11_qg_naming_rule
  - naming-rule-builder
  - p03_sp_naming_rule_builder
  - bld_config_naming_rule
  - bld_architecture_naming_rule
---

# Domain Knowledge: naming_rule
## Executive Summary
Naming rules are formal specifications defining the string format that artifacts, files, variables, or entities within a bounded scope must follow. Each rule declares a regex pattern, case style, prefix/suffix conventions, and collision resolution strategy. They differ from validators (which check content against rules), formatters (which present output), parsers (which extract data), and type definitions (which categorize abstractly) by being the single source of truth for "how is this thing named."
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P05 (formatting/convention) |
| Kind | `naming_rule` (exact literal) |
| ID pattern | `p05_nr_{scope_slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 8 HARD + 10 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Key fields | regex, case_style, scope, prefix, separator |
## Patterns
| Pattern | Application |
|---------|-------------|
| Pillar prefix | `p{NN}_` scopes artifact to pillar (e.g., `p01_`, `p05_`) |
| Kind abbreviation | Short token after prefix: kc, nr, mc, sig |
| Regex validation | Machine-checkable pattern: `^p05_nr_[a-z][a-z0-9_]+$` |
| Case style declaration | One of: snake_case, kebab-case, PascalCase, camelCase |
| Collision resolution | Strategy for conflicts: append sequence number, hash suffix, or reject |
| Scope boundary | Naming rule applies to ONE artifact kind or ONE namespace |
### Common Case Styles
| Style | Example | Domain |
|-------|---------|--------|
| snake_case | `my_variable` | Python, YAML keys, file stems |
| kebab-case | `my-component` | URLs, CSS, package names, directory names |
| PascalCase | `MyClass` | Classes, types, components |
| camelCase | `myFunction` | JavaScript functions, JSON keys |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No regex pattern | Cannot machine-validate; enforcement is manual-only |
| Mixed case styles in one scope | Inconsistent; tools cannot predict name format |
| No collision resolution strategy | Name conflicts cause silent overwrites |
| Scope: "all artifacts" | Too broad; different kinds need different patterns |
| Prefix without pillar number | Loses namespace scoping; collisions across pillars |
| Missing separator specification | Ambiguous: is it `my_name` or `my-name`? |
## Application
1. Define the scope: which artifact kind or namespace does this rule govern?
2. Choose case_style (snake_case, kebab-case, PascalCase, camelCase)
3. Define prefix pattern (e.g., `p05_nr_`) and separator
4. Write regex pattern for machine validation
5. Specify collision resolution strategy
6. Provide 3+ valid examples and 3+ invalid examples
7. Validate: body <= 3072 bytes, density >= 0.80, 8 HARD + 10 SOFT gates
## References
- naming-rule-builder SCHEMA.md v1.0.0
- PEP 8 (Python naming conventions)
- BEM CSS naming methodology
- DNS naming (RFC 1035, max 63 chars per label)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_naming_rule]] | downstream | 0.50 |
| [[bld_memory_naming_rule]] | downstream | 0.50 |
| [[p01_kc_naming_rule]] | sibling | 0.42 |
| [[bld_collaboration_naming_rule]] | downstream | 0.39 |
| [[bld_examples_naming_rule]] | downstream | 0.37 |
| [[p11_qg_naming_rule]] | downstream | 0.36 |
| [[naming-rule-builder]] | downstream | 0.36 |
| [[p03_sp_naming_rule_builder]] | downstream | 0.35 |
| [[bld_config_naming_rule]] | downstream | 0.32 |
| [[bld_architecture_naming_rule]] | downstream | 0.31 |
