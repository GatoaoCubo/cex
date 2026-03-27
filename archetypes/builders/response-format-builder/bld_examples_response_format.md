---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of response_format artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: response-format-builder

## Golden Example

INPUT: "Cria response_format para knowledge_card output em YAML frontmatter + markdown"

OUTPUT:
```yaml
---
id: p05_rf_knowledge_card
kind: response_format
pillar: P05
title: "Response Format: Knowledge Card"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
target_kind: "knowledge_card"
format_type: "yaml"
injection_point: "system_prompt"
sections: [frontmatter, tldr, core_concepts, patterns, anti_patterns, quick_reference, references]
sections_count: 7
domain: "knowledge"
quality: null
tags: [response-format, knowledge-card, yaml-frontmatter, structured-output]
tldr: "KC output format: YAML frontmatter (id, kind, pillar, tags, tldr) + 6 markdown sections, injected in system_prompt"
example_output: "see body"
composable: false
density_score: 0.91
linked_artifacts:
  primary: "knowledge-card-builder"
  related: [p06_vs_knowledge_card, p01_kc_prompt_caching]
---

## Format Overview
Defines how the LLM should structure knowledge_card output: YAML frontmatter with required fields followed by 6 ordered markdown sections.
Injected in system_prompt so every KC production follows the same structure.

## Sections
| # | Section | Description | Required | Constraints |
|---|---------|-------------|----------|-------------|
| 1 | frontmatter | YAML block with id, kind, pillar, quality: null, tags, tldr | yes | all required fields per P01 schema |
| 2 | TL;DR | 1-2 sentence dense summary | yes | <= 160 chars, no filler |
| 3 | Core Concepts | Key facts as bullet list | yes | >= 3 bullets, <= 80 chars each |
| 4 | Patterns | Proven approaches | yes | >= 2 bullets with context |
| 5 | Anti-Patterns | What to avoid | yes | >= 1 bullet with why |
| 6 | Quick Reference | Commands, snippets, tables | yes | Actionable, copy-paste ready |
| 7 | References | Source URLs with dates | yes | >= 1 URL, verifiable |

## Example Output
```yaml
---
id: p01_kc_example_topic
kind: knowledge_card
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
domain: "example"
quality: null
tags: [example, knowledge-card, template]
tldr: "Example KC showing expected output structure with all 7 sections"
---

## TL;DR
Example knowledge card demonstrating the response format structure.

## Core Concepts
- First key concept with concrete data
- Second key concept with specific reference
- Third key concept with actionable detail

## Patterns
- Pattern 1: when X, do Y (proven in context Z)
- Pattern 2: use A instead of B (measured 30% improvement)

## Anti-Patterns
- Anti-pattern 1: avoid X because Y (causes Z failure)

## Quick Reference
| Command | Purpose |
|---------|---------|
| `example_cmd` | Does specific thing |

## References
- Source: https://example.com (2026-03-26)
```

## Injection Instructions
- **Point**: system_prompt
- **Position**: after identity rules, before task instructions
- **Template**: "When producing a knowledge_card, use the following output format:"
- **Composable**: false — KC format is self-contained

## References
- P01_knowledge/_schema.yaml: field definitions
- knowledge-card-builder SCHEMA.md: authoritative field reference
```

WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p05_rf_ pattern (H02 pass)
- kind: response_format (H04 pass)
- 17 required fields present (H07 pass)
- sections_count 7 >= 1 (H08 pass)
- format_type "yaml" in valid enum (H09 pass)
- injection_point "system_prompt" in valid enum (H10 pass)
- target_kind non-empty (H11 pass)
- Sections table with all 7 sections, ordered (S03 pass)
- Example Output complete and matches sections (S04 pass)
- Injection Instructions with point, position, template (S05 pass)
- tldr <= 160 chars, dense (S01 pass)

## Anti-Example

INPUT: "Format para output"

BAD OUTPUT:
```yaml
---
id: output_format
kind: format
pillar: Output
format_type: text
sections_count: 0
quality: 8.0
tags: format
---

## Instructions
The output should be formatted nicely.
Make sure it looks good and is well-structured.
Use appropriate headers and sections.
```

FAILURES:
1. id: no p05_rf_ prefix -> H02 FAIL
2. kind: "format" not "response_format" -> H04 FAIL
3. pillar: "Output" not "P05" -> H05 FAIL
4. quality: 8.0 (not null) -> H06 FAIL
5. sections_count: 0 < 1 minimum -> H08 FAIL
6. format_type: "text" not in enum -> H09 FAIL
7. injection_point: missing -> H10 FAIL
8. target_kind: missing -> H11 FAIL
9. tags: string not list, len < 3 -> S02 FAIL
10. body: filler prose ("looks good", "well-structured", "appropriate") -> S07 FAIL
11. No Example Output section -> S04 FAIL
12. No Sections table -> S03 FAIL
