---
id: prompt_ppt_generator
kind: prompt_template
8f: F6_produce
pillar: P03
title: "Marp Slide Deck Generator"
version: 1.0.0
created: 2026-04-19
author: n05_operations
domain: media_production
quality: 8.8
tags: [prompt_template, marp, slides, ppt, media, mentor, teaching]
tldr: "Renders a CEX concept as a Marp-compatible markdown slide deck for PPTX/PDF generation."
density_score: 0.90
target_engine: mustache
composable: false
related:
  - bld_schema_lens
  - bld_schema_voice_pipeline
  - schema_prompt_template_builder
  - bld_schema_multimodal_prompt
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_e2e_eval
  - bld_schema_benchmark_suite
  - bld_schema_sdk_example
  - bld_schema_action_prompt
updated: "2026-04-22"
---

## Purpose

This template converts a CEX concept into a Marp markdown slide deck. The output is
processed by `npx @marp-team/marp-cli` to produce PPTX and PDF files. Designed for
teaching non-dev solo builders through visual storytelling with analogy lenses.

## Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| concept_name | string | yes | null | The CEX concept to present |
| concept_type | string | yes | null | One of: kind, pipeline, pillar, nucleus, system |
| lens_name | string | no | factory | Analogy lens (factory, city, biology, game) |
| lens_mappings | string | yes | null | Key concept-to-metaphor mappings from lens KC |
| language | string | yes | en | Target language: en or pt-br |
| locale_voice | string | no | "" | Locale voice instructions |
| subtitle | string | no | "" | Deck subtitle |
| author_name | string | no | CEX Mentor | Presenter attribution |
| total_slides | integer | no | 12 | Target slide count (8-20) |
| include_quiz | boolean | no | true | Append Socratic quiz slides at the end |
| source_content | string | no | "" | Full module/lesson content when rendering a course module (provides real examples for slides) |

## Template Body

````mustache
---
marp: true
theme: default
paginate: true
header: "CEX Mentor -- {{concept_name}}"
footer: "{{author_name}} | {{language}}"
style: |
  section {
    font-family: 'Segoe UI', system-ui, sans-serif;
  }
  h1 {
    color: #1a1a2e;
  }
  h2 {
    color: #16213e;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
  }
  table {
    font-size: 0.8em;
  }
  blockquote {
    border-left: 4px solid #e94560;
    padding-left: 1rem;
    font-style: italic;
  }
---

# {{concept_name}}
## {{subtitle}}

**{{lens_name}} lens** | {{language}}

---

## What is {{concept_name}}?

- **Type:** {{concept_type}}
- **Role in CEX:** [one-line purpose]
- **Why it matters:** [value proposition for {{audience}}]

> "The system that turns 5 words into professional output."

---

## The {{lens_name}} Analogy

{{lens_mappings}}

---

{{#source_content}}
## Module Content

{{source_content}}

---

{{/source_content}}

## How It Works

```
[Input] --> {{concept_name}} --> [Output]
```

1. **Step 1:** [entry point]
2. **Step 2:** [transformation]
3. **Step 3:** [output + quality check]

---

## Before vs. After

| Without {{concept_name}} | With {{concept_name}} |
|--------------------------|----------------------|
| Vague output | Precise, typed output |
| Manual quality checks | Automated gates |
| Inconsistent results | Reproducible quality |

---

## Real Example

**User says:** "make me a landing page"

**{{concept_name}} does:**
- Resolves intent to specific kind + pillar
- Loads 12 builder ISOs
- Injects brand, memory, examples
- Produces production-ready artifact

---

## Architecture View

```
[Component diagram showing {{concept_name}} in context]
```

---

## Key Properties

| Property | Value |
|----------|-------|
| Type | {{concept_type}} |
| Pipeline stage | [F1-F8 position] |
| Quality target | 9.0+ |
| Dependencies | [upstream components] |

---

## Common Mistakes

1. **Mistake:** Skipping {{concept_name}}
   **Result:** Quality drops below gate threshold

2. **Mistake:** Using it without context injection
   **Result:** Generic output, misses brand voice

3. **Mistake:** Treating it as optional
   **Result:** Pipeline breaks downstream

---

## Connected Concepts

- **Upstream:** [what feeds into {{concept_name}}]
- **Downstream:** [what consumes its output]
- **Parallel:** [what runs alongside it]

---

## Summary

1. {{concept_name}} is [core role]
2. Through the {{lens_name}} lens: [analogy]
3. Without it: [consequence]
4. For you: [practical benefit]

---

{{#include_quiz}}
## Quick Check

1. What would happen if you removed {{concept_name}} from the pipeline?
2. In the {{lens_name}} analogy, what is {{concept_name}} equivalent to?
3. Name two things that depend on {{concept_name}} working correctly.

---

## Think Deeper

> If {{concept_name}} is the [lens metaphor], then what is the [related concept]?

*Hint: Think about how [analogy element A] connects to [analogy element B].*
{{/include_quiz}}

---

# Thank You

**CEX Mentor** -- Teaching the system to teach itself.

Learn more: `/mentor explain {{concept_name}}`
````

## Quality Gates

| Gate | Check | Threshold |
|------|-------|-----------|
| H01 | All variables resolved | 0 unresolved |
| H02 | Slide count within range | 8-20 slides |
| H03 | Marp frontmatter valid (marp: true present) | required |
| H04 | Each slide has content (no empty slides) | 0 empty |
| H05 | Consistent language throughout | manual check |
| H06 | Marp CLI renders without error | exit code 0 |

## Examples

### Minimal Invocation

```yaml
concept_name: "8F Pipeline"
concept_type: pipeline
lens_name: factory
language: en
lens_mappings: "8F = assembly line, F1 = raw material intake, F7 = QA station"
```

### Full Invocation

```yaml
concept_name: "nucleus"
concept_type: system
lens_name: city
language: pt-br
lens_mappings: "nucleus = distrito da cidade, N01 = centro de pesquisa..."
locale_voice: "Use metaforas urbanas brasileiras..."
subtitle: "Os 7 Nucleos do CEXAI"
author_name: "CEX Mentor"
total_slides: 15
include_quiz: true
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lens]] | downstream | 0.28 |
| [[bld_schema_voice_pipeline]] | downstream | 0.28 |
| [[schema_prompt_template_builder]] | downstream | 0.26 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.26 |
| [[bld_schema_reranker_config]] | downstream | 0.26 |
| [[bld_schema_dataset_card]] | downstream | 0.26 |
| [[bld_schema_e2e_eval]] | downstream | 0.26 |
| [[bld_schema_benchmark_suite]] | downstream | 0.26 |
| [[bld_schema_sdk_example]] | downstream | 0.26 |
| [[bld_schema_action_prompt]] | downstream | 0.25 |
