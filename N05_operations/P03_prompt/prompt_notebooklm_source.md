---
id: prompt_notebooklm_source
kind: prompt_template
8f: F6_produce
pillar: P03
title: "NotebookLM Source Document Generator"
version: 1.0.0
created: 2026-04-19
author: n05_operations
domain: media_production
quality: 8.8
tags: [prompt_template, notebooklm, media, mentor, teaching]
tldr: "Renders a CEX concept as a NotebookLM-optimized source document for Audio/Video Overview generation."
density_score: 0.90
target_engine: mustache
composable: false
related:
  - bld_schema_lens
  - bld_schema_voice_pipeline
  - bld_schema_multimodal_prompt
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_prompt_technique
  - bld_schema_audit_log
  - bld_schema_app_directory_entry
  - bld_schema_sdk_example
  - bld_schema_reranker_config
updated: "2026-04-22"
---

## Purpose

This template converts a CEX concept (kind, pipeline step, pillar, nucleus) into a
long-form source document optimized for NotebookLM's Audio Overview and Video Overview
features. The output is designed to be uploaded as a "Copied text" source and produce
a natural-sounding 2-host podcast discussion.

## Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| concept_name | string | yes | null | The CEX concept to teach (e.g., "8F pipeline", "knowledge_card") |
| concept_type | string | yes | null | One of: kind, pipeline, pillar, nucleus, system |
| lens_name | string | no | factory | Which analogy lens to use (factory, city, biology, game) |
| lens_content | string | yes | null | Full lens KC content for the selected lens |
| language | string | yes | en | Target language: en or pt-br |
| locale_voice | string | no | "" | Locale-specific voice instructions from mentor_locale template |
| audience | string | no | non_dev_solo_builders | Target audience descriptor |
| related_concepts | string | no | "" | Comma-separated list of related CEX concepts for cross-references |
| technical_definition | string | no | "" | The canonical technical definition from the taxonomy |
| source_content | string | no | "" | Full module/lesson content when rendering a course module (primary material for podcast) |

## Template Body

```mustache
# {{concept_name}} -- A Deep Dive

## What This Document Covers

This is a comprehensive exploration of {{concept_name}} in the CEXAI (Cognitive Exchange AI)
system. CEXAI is a typed knowledge system for LLM agents -- think of it as an AI brain
that turns vague human requests into professional outputs through structured pipelines.

{{locale_voice}}

## The Core Idea

{{concept_name}} is a {{concept_type}} in CEX.

{{#technical_definition}}
**Technical definition:** {{technical_definition}}
{{/technical_definition}}

## Understanding Through Analogy: The {{lens_name}} Lens

To make this concrete, let's use the {{lens_name}} analogy:

{{lens_content}}

{{#source_content}}
## Source Material

The following is the full lesson content for this concept. Use it as the primary
material for the podcast discussion -- reference specific examples, analogies,
and exercises from it.

{{source_content}}
{{/source_content}}

## Why {{concept_name}} Matters

For {{audience}}, understanding {{concept_name}} is essential because it directly affects
how the system produces value. Without it, the pipeline breaks at a critical point.

Here's the key insight: {{concept_name}} isn't just a technical component -- it's the
mechanism that bridges the gap between what a user asks for and what they actually need.

## How It Works (Step by Step)

Let's walk through how {{concept_name}} operates in practice:

1. **Entry point**: When does {{concept_name}} activate in the system?
2. **Processing**: What transformation does it perform?
3. **Output**: What does the system produce as a result?
4. **Quality check**: How do we know it worked correctly?

## Real-World Example

Imagine you're a solo builder who just typed a simple request into the system.
Here's exactly what happens when {{concept_name}} kicks in:

[The system takes your vague input and through {{concept_name}}, transforms it into
a precise, professional output -- the same quality that would take a team of specialists
days to produce.]

## Common Misconceptions

People often confuse {{concept_name}} with simpler alternatives. Here's what it is NOT:
- It's not just a template or checklist
- It's not manual work disguised as automation
- It's not optional -- the system quality depends on it

{{#related_concepts}}
## Connected Concepts

{{concept_name}} doesn't work in isolation. It connects to: {{related_concepts}}.
Understanding these relationships reveals the full architecture.
{{/related_concepts}}

## Key Takeaways

1. {{concept_name}} is the {{concept_type}} that ensures [core value proposition]
2. Through the {{lens_name}} lens, it maps to [analogy] -- making it intuitive
3. Without it, the system would [consequence of removal]
4. For {{audience}}, this means [practical benefit]

## Discussion Questions

- How does {{concept_name}} compare to similar concepts in traditional software?
- What would break if we removed {{concept_name}} from the pipeline?
- How might {{concept_name}} evolve as the system grows?
```

## Quality Gates

| Gate | Check | Threshold |
|------|-------|-----------|
| H01 | All variables resolved (no raw mustache in output) | 0 unresolved |
| H02 | Word count sufficient for Audio Overview | >= 500 words |
| H03 | Character count within NotebookLM source limit | <= 200,000 chars |
| H04 | Contains discussion questions (drives podcast dialogue) | >= 3 questions |
| H05 | Lens content integrated (not placeholder) | lens_content length > 100 |
| H06 | Language matches locale_voice instructions | manual check |

## Examples

### Minimal Invocation

```yaml
concept_name: "8F Pipeline"
concept_type: pipeline
lens_name: factory
language: en
lens_content: "The 8F pipeline is the assembly line..."
```

### Full Invocation

```yaml
concept_name: "knowledge_card"
concept_type: kind
lens_name: biology
language: pt-br
lens_content: "Um knowledge_card e como uma celula..."
locale_voice: "Use tom conversacional brasileiro, referencias culturais locais..."
audience: "empreendedores solo sem background tecnico"
related_concepts: "glossary_entry, citation, chunk_strategy"
technical_definition: "Atomic unit of domain knowledge with structured frontmatter..."
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lens]] | downstream | 0.28 |
| [[bld_schema_voice_pipeline]] | downstream | 0.27 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.27 |
| [[bld_schema_pitch_deck]] | downstream | 0.27 |
| [[bld_schema_benchmark_suite]] | downstream | 0.26 |
| [[bld_schema_prompt_technique]] | downstream | 0.26 |
| [[bld_schema_audit_log]] | downstream | 0.25 |
| [[bld_schema_app_directory_entry]] | downstream | 0.25 |
| [[bld_schema_sdk_example]] | downstream | 0.25 |
| [[bld_schema_reranker_config]] | downstream | 0.25 |
