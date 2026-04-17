---
kind: output_template
id: bld_output_template_kind
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce each ISO in a builder package
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.1
title: "Output Template Kind Builder"
version: "1.0.0"
author: n03_builder
tags: [kind_builder, builder, output_template, meta-builder]
tldr: "Template for each of the 13 ISOs in a builder package, with frontmatter and body structure."
domain: "kind builder construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Output Template: kind-builder

## ISO 1: Manifest

```yaml
---
id: {{kind}}-builder
kind: type_builder
pillar: {{target_pillar}}
parent: null
domain: {{kind}}
llm_function: {{target_llm_function}}
version: 1.0.0
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: builder_agent
tags: [kind-builder, {{kind}}, {{target_pillar}}, {{tag_3}}, {{tag_4}}]
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}, {{keyword_4}}]
triggers: [{{trigger_1}}, {{trigger_2}}, {{trigger_3}}]
capabilities: >
  L1: {{one_sentence_capability}}.
  L2: {{detail_sentence}}.
  L3: {{when_to_use}}.
quality: null
title: "Manifest {{Kind_Title}}"
tldr: "{{dense_summary_max_160ch}}"
density_score: 0.90
---
```

## ISO 2: Schema

```yaml
---
kind: schema
id: bld_schema_{{kind}}
pillar: P06
llm_function: CONSTRAIN
purpose: {{purpose_of_schema}}
quality: null
title: "Schema {{Kind_Title}}"
...
---
```

Body sections:
1. `## Frontmatter Fields` -- table: field, type, required, default, notes
2. `## ID Pattern` -- regex + rule
3. `## Body Structure` -- required sections list
4. `## Constraints` -- max_bytes, naming, machine_format, boundary

## ISO 3: System Prompt

```yaml
---
id: p03_sp_{{kind}}_builder
kind: system_prompt
pillar: P03
...
quality: null
---
```

Body sections:
1. `## Identity` -- 1 paragraph: who you are, what you produce, what you do NOT do
2. `## Rules` -- 13 numbered rules grouped by scope, quality, domain

## ISO 4: Instruction

Body sections:
1. `## Phase 1: RESEARCH` -- 5-8 numbered steps
2. `## Phase 2: COMPOSE` -- 8-12 numbered steps
3. `## Phase 3: VALIDATE` -- 8-12 numbered checks

## ISO 5: Output Template

Body: YAML frontmatter template with `{{vars}}` + body section templates

## ISO 6: Examples

Body sections:
1. `## Golden Example` -- INPUT + OUTPUT (complete artifact with frontmatter)
2. `WHY THIS IS GOLDEN:` -- list of gate passes
3. `## Anti-Example` -- INPUT + BAD OUTPUT
4. `FAILURES:` -- numbered list of gate failures

## ISO 7: Memory

Body sections:
1. `## Summary` -- 1-2 paragraphs
2. `## Pattern` -- what works, with evidence
3. `## Anti-Pattern` -- numbered list of what fails

## ISO 8: Tools

Body sections:
1. `## Production Tools` -- table: tool, purpose, when, status
2. `## Data Sources` -- table: source, path, data
3. `## Tool Permissions` -- table: category, tools, status

## ISO 9: Quality Gate

Body sections:
1. `## Definition` -- metric, threshold, operator, scope
2. `## HARD Gates` -- table: ID, check, failure message (8-12 gates)
3. `## SOFT Scoring` -- table: dimension, weight, what to assess (8-12 dims)
4. `## Actions` -- score tiers: golden, publish, review, reject

## ISO 10: Knowledge Card

Body sections:
1. `## Executive Summary` -- 2-3 sentences
2. `## Spec Table` -- property/value pairs
3. `## Patterns` -- domain patterns with tables
4. `## Anti-Patterns` -- table: anti-pattern, why it fails
5. `## References` -- industry sources

## ISO 11: Architecture

Body sections:
1. `## Component Inventory` -- table: name, role, owner, status
2. `## Dependency Graph` -- ASCII graph + table
3. `## Boundary Table` -- two-column: IS / IS NOT

## ISO 12: Collaboration

Body sections:
1. `## My Role in Crews` -- 2-3 sentences
2. `## Crew Compositions` -- 2-3 crew examples
3. `## Handoff Protocol` -- I Receive / I Produce / I Signal
4. `## Builders I Depend On` -- list
5. `## Builders That Depend On Me` -- table

## ISO 13: Config

Body sections:
1. `## Naming Convention` -- table: scope, convention, example
2. `## File Paths` -- output + compiled paths
3. `## Size Limits` -- body max, total max, density floor

## Sub-Agent File

```markdown
# {{Kind}} Builder

## System Prompt
Load: archetypes/builders/{{kind}}-builder/bld_system_prompt_{{kind}}.md

## Instructions
Load: archetypes/builders/{{kind}}-builder/bld_instruction_{{kind}}.md

## Context
Load all 13 ISOs from archetypes/builders/{{kind}}-builder/
```
