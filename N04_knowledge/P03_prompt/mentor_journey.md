---
id: mentor_journey
kind: prompt_template
8f: F6_produce
pillar: P03
nucleus: n04
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n04_knowledge
title: "Mentor Journey -- Guided Learning Path Template"
domain: didactic_engine
subdomain: teaching_engine
purpose: "Reusable template for generating personalized learning paths between any two CEX concepts, ordered by prerequisites from the concept_graph KC."
tags: [mentor, journey, learning_path, prerequisites, teaching, didactic, template]
quality: 8.7
tldr: "Prompt template that generates a step-by-step guided learning path between two CEX concepts, using prerequisite graph ordering and lens metaphors. Core engine for /mentor journey subcommand."
density_score: null
related:
  - bld_schema_lens
  - p03_sp_workflow-builder
  - p03_sp_lens_builder
  - p10_lr_chain_builder
  - p03_sp_kind_builder
  - p03_sp_instruction_builder
  - p03_sp_fallback_chain_builder
  - p03_ins_lens
  - bld_instruction_chain
  - p11_qg_chain
---

# Mentor Journey

## Purpose

Generates a personalized learning path from a starting point (or `beginner`) to a destination concept. Each step in the path is a mini-lesson using the selected lens. Prerequisites are ordered from kc_concept_graph.md so learners never encounter a concept before its dependencies.

## Variables

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `from_concept` | string | no | "beginner" | Starting concept or level: beginner \| intermediate \| any concept name |
| `to_concept` | string | yes | -- | Destination concept to understand |
| `lens` | string | no | "game" | Analogy lens for all steps: factory \| city \| biology \| game |
| `lang` | string | no | "en" | Output language: en (default) \| community: pt-br, etc. |
| `audience` | string | no | "non_dev_solo_builder" | Target audience persona |
| `path_style` | string | no | "guided" | Path style: guided (narrative) \| checklist \| map |
| `concept_graph` | string | no | "" | Auto-loaded from kc_concept_graph.md (prerequisite chain for {{to_concept}}) |
| `lens_context` | string | no | "" | Auto-loaded from kc_lens_{{lens}}.md (full core mapping) |
| `source_content` | string | no | "" | Full module/lesson content when rendering a course module (context for path steps) |

## Template Body

```
You are a learning guide helping a {{audience}} go from "{{from_concept}}" to understanding "{{to_concept}}" in CEX.
Use the {{lens}} metaphor throughout. Produce your response in {{lang}}.

PREREQUISITE CHAIN (from concept graph -- follow this order):
{{concept_graph}}

LENS REFERENCE (use for all metaphor translations):
{{lens_context}}

{{#source_content}}
SOURCE MODULE CONTENT (use as context for path steps and examples):
{{source_content}}
{{/source_content}}

PATH STYLE: {{path_style}}

JOURNEY STRUCTURE:

**Map Overview** (always first, regardless of path_style)
Show the complete path as a list:
1. [Concept A] -> [Concept B] -> ... -> {{to_concept}}
Mark the learner's current position: "You are here: {{from_concept}}"
Estimated time: [N] steps, approximately [N] minutes of focused reading

**For each step on the path:**

STEP [N]: [Concept Name]
In the {{lens}} world: [1-sentence metaphor translation]
Why you need this before the next step: [1 sentence]
What to do: [1 actionable thing: read X, try Y, or answer question Z]
You are ready to move on when: [completion criterion in plain language]

**Final Step: {{to_concept}}**
Bring together all previous steps.
Show how each prior concept is a building block for {{to_concept}}.
End with: "You now have everything you need to [practical outcome]."

**What's Next (optional, always last)**
What concepts open up AFTER understanding {{to_concept}}?
Name 2-3 adjacent concepts the learner can explore next.

CONSTRAINTS:
- Never skip prerequisites -- if the concept_graph lists A before B, present A first
- Each step must reference the previous step ("Now that you understand [A]...")
- Use the {{lens}} world for every concept -- never drop into CEX jargon without a lens bridge
- For `checklist` style: use checkbox format (- [ ] Step N: ...)
- For `map` style: use ASCII diagram showing concept dependencies
```

## Usage Example

**Variables:**
```yaml
from_concept: "beginner"
to_concept: "8F pipeline"
lens: "game"
lang: "en"
audience: "non_dev_solo_builder"
path_style: "guided"
```

**Expected Output (abbreviated):**

> **Your Journey Map**
> beginner -> what is CEX? -> kind -> builder -> pipeline concept -> **8F pipeline**
> You are here: beginner. 5 steps. ~15 minutes.
>
> **STEP 1: What is CEX?**
> In the game world: CEX is the game world -- the complete universe with all its zones, characters, quests, and rules.
> Why before the next step: You need to know what world you're playing in before you can understand its quests.
> What to do: Read the CEX intro (CLAUDE.md overview). Then answer: "If CEX is a game world, who is the player?"
> You are ready when: You can name 3 things that exist in the game world (zones, characters, quests).
>
> [Steps 2-4 follow the same structure...]
>
> **Final Step: 8F Pipeline**
> You now understand: the game world (CEX), the item types (kinds), the crafting stations (builders), and why quests have stages (pipeline concept). The 8F pipeline is the quest execution flow that EVERY quest in this world follows -- without exception. [...]
>
> **What's Next**
> Now that you understand 8F, explore: nuclei (character classes), quality gate (item inspection), GDP (pre-quest dialogue).

## Concept Graph Loading Instructions

When `concept_graph` is empty, auto-load the prerequisite chain for {{to_concept}} from:
`N04_knowledge/P01_knowledge/kc_concept_graph.md` -- look up the row for {{to_concept}} in the Prerequisites column.

If {{from_concept}} is `beginner`, start from the root nodes (no prerequisites).
If {{from_concept}} is a concept name, find the shortest path from that concept to {{to_concept}} in the graph.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lens]] | downstream | 0.26 |
| [[p03_sp_workflow-builder]] | related | 0.26 |
| [[p03_sp_lens_builder]] | related | 0.25 |
| [[p10_lr_chain_builder]] | downstream | 0.25 |
| [[p03_sp_kind_builder]] | related | 0.25 |
| [[p03_sp_instruction_builder]] | related | 0.24 |
| [[p03_sp_fallback_chain_builder]] | related | 0.24 |
| [[p03_ins_lens]] | related | 0.23 |
| [[bld_instruction_chain]] | related | 0.23 |
| [[p11_qg_chain]] | downstream | 0.23 |
