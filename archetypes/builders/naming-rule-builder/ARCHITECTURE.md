---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of naming_rule — inventory, dependencies, and architectural position
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
