---
id: p05_rf_edison_engineering_nucleus
kind: response_format
pillar: P05
title: "Response Format: Edison Engineering Nucleus"
version: "1.0.0"
created: "2023-10-05"
updated: "2023-10-05"
author: "response-format-builder"
target_kind: "engineering_documentation"
format_type: "markdown"
injection_point: "system_prompt"
sections: [frontmatter, introduction, key_concepts, implementation_steps, findings_and_analysis, conclusion, references]
sections_count: 7
domain: "engineering"
quality: null
tags: [response-format, engineering-documentation, markdown, structured-output]
tldr: "Structured output for engineering documentation: ordered markdown sections, injected in system_prompt"
example_output: "see body"
composable: false
density_score: 0.93
linked_artifacts:
  primary: "engineering-documentation-builder"
  related: [p06_vs_engineering_document, p01_kc_project_management]
---

## Format Overview
This response format specifies the structure for engineering documentation outputs. It includes a frontmatter section followed by six structured markdown sections: introduction, key concepts, implementation steps, findings and analysis, conclusion, and references. This format is injected in the system_prompt to ensure a consistent structure across all engineering documentation outputs generated.

## Sections
| # | Section                  | Description                                          | Required | Constraints                            |
|---|--------------------------|------------------------------------------------------|----------|----------------------------------------|
| 1 | frontmatter              | Metadata about the document                          | yes      | Must include id, kind, title, version  |
| 2 | introduction             | Brief description of the document's purpose          | yes      | 1-2 paragraphs, < 500 words            |
| 3 | key_concepts             | Key ideas and relevant theories                      | yes      | Bullet list, min 3 items               |
| 4 | implementation_steps     | Detailed procedures and methods                      | yes      | Numbered list, step-by-step guide      |
| 5 | findings_and_analysis    | Analysis and results from implementation             | yes      | Structured text with subsections       |
| 6 | conclusion               | Summary of the document and any closing thoughts     | yes      | 1 paragraph, concise and clear         |
| 7 | references               | Sources and further readings                         | yes      | Bulleted URLs with titles              |

## Example Output
---
markdown
# Edison Engineering Documentation

## Introduction
This document outlines the procedures and methodologies used in the Edison Engineering Nucleus project to develop sustainable energy solutions.

## Key Concepts
- Renewable energy sourcing
- Energy efficiency optimization
- Lifecycle impact analysis

## Implementation Steps
1. Conduct a preliminary resource assessment.
2. Develop a sustainability roadmap.
3. Implement pilot solutions and collect data.

## Findings and Analysis
### Resource Assessment
The initial resource assessment highlighted the potential for a 20% reduction in energy waste through optimized processes.

### Pilot Data
Data collected from pilot implementations indicate a 15% increase in system efficiency.

## Conclusion
The Edison Engineering Nucleus project demonstrates the feasibility and benefits of implementing sustainable engineering solutions.

## References
- [Energy Solutions](https://energysolutions.com) (Accessed: 2023-10-05)
```

## Injection Instructions
- **Point**: system_prompt
- **Position**: after identity and purpose statements, before main task instructions
- **Template**: "For engineering documentation, use the following output format defined in the system prompt:"
- **Composable**: false — This format structure is standalone and complete.
## References
- P05_engineering/_schema.yaml: field definitions
- engineering-documentation-builder SCHEMA.md: authoritative field reference
```