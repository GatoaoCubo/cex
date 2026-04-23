---
kind: architecture
id: bld_architecture_naming_rule
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of naming_rule — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Naming Rule"
version: "1.0.0"
author: n03_builder
tags: [naming_rule, builder, examples]
tldr: "Golden and anti-examples for naming rule construction, demonstrating ideal structure and common pitfalls."
domain: "naming rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - naming-rule-builder
  - p01_kc_naming_rule
  - p03_ins_naming_rule
  - p11_qg_naming_rule
  - bld_knowledge_card_naming_rule
  - bld_collaboration_naming_rule
  - bld_memory_naming_rule
  - bld_architecture_type_def
  - p03_sp_naming_rule_builder
  - bld_tools_naming_rule
---

# Architecture: naming_rule in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, scope, case_style, separator, etc.) | naming-rule-builder | active |
| pattern_definition | Regex or glob pattern defining valid names for the scope | author | active |
| prefix_suffix_rules | Required prefixes, suffixes, and their semantic meaning | author | active |
| case_style | Enforced casing convention (snake_case, kebab-case, PascalCase, etc.) | author | active |
| separator_config | Allowed separators and their positional constraints | author | active |
| version_segment | How version information is encoded within the name | author | active |
| collision_resolution | Strategy for resolving name conflicts within the scope | author | active |
## Dependency Graph
```
scope_owner     --produces-->  naming_rule  --consumed_by-->  validator
naming_rule     --enforced_by-->  formatter  --produces-->     canonical_name
naming_rule     --signals-->      naming_violation
```
| From | To | Type | Data |
|------|----|------|------|
| scope_owner (orchestrator) | naming_rule | data_flow | scope definition and domain constraints |
| naming_rule | validator (P06) | consumes | validators enforce naming patterns at commit time |
| naming_rule | formatter (P05) | data_flow | formatters apply naming conventions to output |
| naming_rule | code_generator | consumes | generators use patterns to produce compliant names |
| naming_rule | naming_violation | signals | emitted when a name fails pattern validation |
| type_def (P06) | naming_rule | dependency | type definitions may reference naming conventions |
## Boundary Table
| naming_rule IS | naming_rule IS NOT |
|----------------|-------------------|
| A formal pattern defining how entities are named within a scope | An abstract type declaration (type_def P06) |
| Machine-validated via regex or glob patterns | An output formatting specification (formatter P05) |
| Scoped to a specific artifact domain or file category | A data extraction rule (parser P05) |
| Includes collision resolution for name conflicts | A validation rule checking content, not names (validator P06) |
| Prescribes prefix, suffix, case, and separator conventions | A runtime configuration parameter (path_config P09) |
| Versioning-aware when names embed version segments | A changelog or history document |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Scope | frontmatter, scope_owner | Define which entities and domains this rule governs |
| Pattern | pattern_definition, case_style, separator_config | Specify the structural rules for valid names |
| Segments | prefix_suffix_rules, version_segment | Define semantic segments within the name |
| Conflict | collision_resolution | Handle duplicate or ambiguous name scenarios |
| Enforcement | validator, formatter, naming_violation | Downstream systems that check and apply the rule |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[naming-rule-builder]] | upstream | 0.42 |
| [[p01_kc_naming_rule]] | related | 0.41 |
| [[p03_ins_naming_rule]] | upstream | 0.38 |
| [[p11_qg_naming_rule]] | downstream | 0.37 |
| [[bld_knowledge_card_naming_rule]] | upstream | 0.37 |
| [[bld_collaboration_naming_rule]] | upstream | 0.35 |
| [[bld_memory_naming_rule]] | downstream | 0.34 |
| [[bld_architecture_type_def]] | sibling | 0.32 |
| [[p03_sp_naming_rule_builder]] | upstream | 0.31 |
| [[bld_tools_naming_rule]] | upstream | 0.30 |
