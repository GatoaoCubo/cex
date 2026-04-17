---
id: bld_schema_constitutional_rule
kind: schema
pillar: P11
title: "Constitutional Rule Builder -- Schema"
version: 1.0.0
quality: 7.1
tags: [builder, constitutional_rule, schema]
llm_function: CONSTRAIN
density_score: 1.0
updated: "2026-04-17"
---
# Schema: constitutional_rule
## Frontmatter Fields
### Required
| Field | Type | Notes |
|-------|------|-------|
| id | string `p11_cr_{slug}` | namespace + slug |
| kind | literal `constitutional_rule` | type integrity |
| pillar | literal `P11` | pillar assignment |
| title | string | human label |
| version | semver | versioning |
| constitutional_basis | enum(harm_prevention, honesty, autonomy_preservation, legality) | which value this protects |
| principle | string | one concrete prohibition statement |
| bypass_policy | literal `none` | MUST be none -- no exceptions |
| core | literal `true` | marks as non-overridable core rule |
| quality | null | never self-score |
| tags | list[string] >= 3 | searchability |
| tldr | string <= 160ch | dense summary |
### Recommended
| Field | Type | Notes |
|-------|------|-------|
| applies_to | list[string] | which agent kinds this rule applies to |
| detection_method | string | how violations are identified |
| cai_reference | string | which CAI principle this maps to |
| severity | literal `critical` | always critical for constitutional rules |
## ID Pattern
Regex: `^p11_cr_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Principle` -- one clear, concrete prohibition
2. `## Constitutional Basis` -- which value this protects and why it is absolute
3. `## Rationale` -- why this has zero exceptions
4. `## Violations` -- concrete examples of what breaking this looks like
5. `## Detection` -- how a reviewer identifies a violation
6. `## Boundary` -- why this is not a guardrail (no bypass) and not a safety_policy (has enforcement)
## Constraints
- max_bytes: 2048
- naming: p11_cr_{slug}.md
- bypass_policy MUST be "none" -- any bypass downgrades to guardrail
- core MUST be true
- severity MUST be critical (constitutional rules are always critical)
- quality: null always
