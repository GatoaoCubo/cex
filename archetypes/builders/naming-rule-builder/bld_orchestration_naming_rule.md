---
kind: collaboration
id: bld_collaboration_naming_rule
pillar: P05
llm_function: COLLABORATE
purpose: How naming-rule-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Naming Rule"
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
  - bld_memory_naming_rule
  - bld_collaboration_builder
  - bld_tools_naming_rule
  - bld_collaboration_validation_schema
  - bld_collaboration_output_validator
  - bld_architecture_kind
  - bld_collaboration_quality_gate
  - p01_kc_naming_rule
  - bld_collaboration_golden_test
---

# Collaboration: naming-rule-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what naming convention governs this artifact domain?"
I define scope-bound patterns (prefix, suffix, separator, case, versioning, collision resolution). I do NOT validate whether existing names comply — that goes to validator-builder.
## Crew Compositions
### Crew: "New Artifact Domain Bootstrap"
```
  1. type-def-builder          -> "defines what the artifact IS abstractly"
  2. naming-rule-builder       -> "defines how the artifact must be named"
  3. validation-schema-builder -> "encodes naming rule as machine-checkable schema"
```
### Crew: "Convention + Enforcement"
```
  1. naming-rule-builder  -> "produces p05_nr_{scope}.md with naming pattern"
  2. validator-builder    -> "checks existing artifacts against the naming rule"
  3. formatter-builder    -> "formats output so names appear in canonical form"
```
### Crew: "Code Generator Pipeline"
```
  1. naming-rule-builder  -> "specifies variable and file naming conventions"
  2. instruction-builder  -> "embeds naming rules into agent execution steps"
  3. parser-builder       -> "extracts named fields from generated output"
```
## Handoff Protocol
### I Receive
- seeds: scope name, artifact domain, target platform (files/variables/agents/tables)
- optional: existing naming examples, collision frequency, versioning needs
### I Produce
- naming_rule artifact (Markdown, max 4KB)
- committed to: `cex/P05/examples/p05_nr_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- type-def-builder: clarifies what entity is being named before conventions are set
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| validator-builder | needs the naming rule to check compliance |
| formatter-builder | uses naming conventions to canonicalize output |
| instruction-builder | embeds naming rules into procedural steps |
| validation-schema-builder | encodes naming pattern as enforceable schema |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[naming-rule-builder]] | related | 0.44 |
| [[bld_memory_naming_rule]] | downstream | 0.41 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_tools_naming_rule]] | upstream | 0.38 |
| [[bld_collaboration_validation_schema]] | sibling | 0.37 |
| [[bld_collaboration_output_validator]] | sibling | 0.36 |
| [[bld_architecture_kind]] | downstream | 0.34 |
| [[bld_collaboration_quality_gate]] | sibling | 0.34 |
| [[p01_kc_naming_rule]] | downstream | 0.33 |
| [[bld_collaboration_golden_test]] | sibling | 0.32 |
