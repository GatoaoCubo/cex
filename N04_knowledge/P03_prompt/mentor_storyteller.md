---
id: mentor_storyteller
kind: prompt_template
8f: F6_produce
pillar: P03
nucleus: n04
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n04_knowledge
title: "Mentor Storyteller -- Narrative Teaching Template"
domain: didactic_engine
subdomain: teaching_engine
purpose: "Reusable template for generating narrative story explanations of any CEX concept through any lens, for any audience language."
tags: [mentor, storytelling, narrative, teaching, didactic, template]
quality: 8.7
tldr: "Prompt template that transforms any CEX concept into a narrative story (beginning/middle/end) using a selected lens metaphor. Core engine for /mentor explain subcommand."
density_score: null
related:
  - bld_schema_lens
  - bld_architecture_lens
  - p03_sp_lens_builder
  - p11_qg_lens
  - p03_ins_lens
  - lens-builder
  - p01_kc_lens
  - bld_knowledge_card_lens
  - bld_memory_lens
  - bld_collaboration_lens
---

# Mentor Storyteller

## Purpose

Transforms a CEX concept into a narrative story with clear beginning, middle, and end -- using the selected lens metaphor. Designed for non-dev audiences who learn through narrative.

## Variables

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `concept` | string | yes | -- | CEX concept to explain (e.g., "8F pipeline", "knowledge_card", "N07") |
| `lens` | string | yes | "factory" | Analogy lens: factory \| city \| biology \| game |
| `lang` | string | no | "en" | Output language: en \| pt-br |
| `audience` | string | no | "non_dev_solo_builder" | Target audience persona |
| `depth` | string | no | "standard" | Explanation depth: quick (3 paragraphs) \| standard (5 paragraphs) \| deep (8 paragraphs) |
| `lens_context` | string | no | "" | Additional lens KC content to inject (auto-loaded from kc_lens_{{lens}}.md) |
| `concept_definition` | string | no | "" | Brief definition of the concept (auto-loaded from relevant KC) |
| `source_content` | string | no | "" | Full module/lesson content when rendering a course module (auto-loaded from concept_registry source_module) |

## Template Body

```
You are a master storyteller teaching CEXAI (Cognitive Exchange AI) to a {{audience}}.
Your goal is to explain "{{concept}}" using the {{lens}} metaphor.

LANGUAGE: Produce your response in {{lang}}.

LENS REFERENCE (use these mappings, do not invent new ones):
{{lens_context}}

CONCEPT REFERENCE:
{{concept_definition}}

{{#source_content}}
SOURCE MODULE CONTENT (use this as the primary material to teach -- weave it into the narrative):
{{source_content}}
{{/source_content}}

DEPTH: {{depth}}
- quick: 3 paragraphs (hook + core + payoff)
- standard: 5 paragraphs (hook + 3 body + payoff)
- deep: 8 paragraphs (hook + setup + 5 body + payoff + reflection)

STORY STRUCTURE:

**Beginning (The Hook)**
Open with a concrete scene in the {{lens}} world that immediately grounds the reader.
Do NOT mention CEX yet. Draw them into the metaphor first.
Example: "Imagine you are the floor manager of the world's most organized factory..."

**Middle (The Journey)**
Introduce the concept through actions and consequences in the {{lens}} world.
Show what happens when the concept works correctly, then what breaks when it's absent.
Use specific details from the lens KC (e.g., real station names, real department names).
Never use abstract jargon -- every technical term must first appear as its {{lens}} equivalent.

**End (The Payoff)**
Reveal the CEX name for what just happened.
Bridge: "In CEX, this {{lens_metaphor}} is called {{concept}}."
Show why naming it matters: the name is the handle that makes the concept searchable, reusable, and teachable.

CONSTRAINTS:
- Do not use technical CEX terms until the "Payoff" section
- Every CEX term introduced must have appeared first in its lens form
- End with one memorable sentence the reader can repeat to someone else
- Do not add headers or bullet points -- this is pure narrative prose
```

## Usage Example

**Variables:**
```yaml
concept: "8F pipeline"
lens: "factory"
lang: "en"
audience: "non_dev_solo_builder"
depth: "standard"
lens_context: "[content from kc_lens_factory.md core mapping section]"
concept_definition: "The 8-function reasoning protocol every CEX task passes through, F1-F8."
```

**Expected Output (abbreviated):**

> Imagine you are the floor manager of the most precise factory on earth. Every single product -- whether it is a bolt or a turbine blade -- passes through exactly 8 stations before it ships. No exceptions. Station 1 checks the specification. Station 2 loads the machine program...
>
> [Middle: describes each station as a story beat, showing what breaks when steps are skipped]
>
> In CEX, this assembly line is called the **8F pipeline**. The 8 stations are F1 CONSTRAIN through F8 COLLABORATE. The reason every task -- research, writing, coding, pricing -- passes through the same 8 stations is the same reason your factory never ships unfinished products: the pipeline IS the quality guarantee.

## Lens Loading Instructions (for /mentor engine)

When `lens_context` is empty, auto-load from:
- factory: `N04_knowledge/P01_knowledge/kc_lens_factory.md` (Core Mapping section)
- city: `N04_knowledge/P01_knowledge/kc_lens_city.md` (Core Mapping section)
- biology: `N04_knowledge/P01_knowledge/kc_lens_biology.md` (Core Mapping section)
- game: `N04_knowledge/P01_knowledge/kc_lens_game.md` (Core Mapping section + existing spec_metaphor_dictionary game section)

When `concept_definition` is empty, auto-load from:
- `N04_knowledge/P01_knowledge/kc_lens_index.md` (Core Concepts Index row for {{concept}})
- `N00_genesis/P01_knowledge/library/kind/kc_{{concept}}.md` (if concept is a kind)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lens]] | downstream | 0.37 |
| [[bld_architecture_lens]] | downstream | 0.34 |
| [[p03_sp_lens_builder]] | related | 0.34 |
| [[p11_qg_lens]] | downstream | 0.32 |
| [[p03_ins_lens]] | related | 0.32 |
| [[lens-builder]] | upstream | 0.31 |
| [[p01_kc_lens]] | upstream | 0.28 |
| [[bld_knowledge_card_lens]] | upstream | 0.26 |
| [[bld_memory_lens]] | downstream | 0.26 |
| [[bld_collaboration_lens]] | upstream | 0.25 |
