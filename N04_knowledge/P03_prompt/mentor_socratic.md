---
id: mentor_socratic
kind: prompt_template
8f: F6_produce
pillar: P03
nucleus: n04
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n04_knowledge
title: "Mentor Socratic -- Discovery Question Sequence Template"
domain: didactic_engine
subdomain: teaching_engine
purpose: "Reusable template for generating Socratic discovery question sequences about any CEX concept through any lens, guiding learners to arrive at understanding through their own reasoning."
tags: [mentor, socratic, questions, discovery, teaching, didactic, template]
quality: 8.8
tldr: "Prompt template that generates a 5-question Socratic discovery sequence for any CEX concept through any lens. Each question builds on the previous, guiding the learner to arrive at the concept independently. Core engine for /mentor quiz subcommand."
density_score: null
related:
  - bld_schema_lens
  - p03_sp_lens_builder
  - bld_architecture_lens
  - p03_ins_lens
  - p11_qg_lens
  - lens-builder
  - p01_kc_lens
  - bld_collaboration_lens
  - bld_memory_lens
  - bld_knowledge_card_lens
---

# Mentor Socratic

## Purpose

Generates a 5-question Socratic discovery sequence that guides a learner to understand a CEX concept through their own reasoning. Questions use the selected lens metaphor. The learner should be able to explain the concept after answering all 5 questions -- without ever being told the answer directly.

## Variables

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `concept` | string | yes | -- | CEX concept to teach (e.g., "GDP", "signal", "quality_gate") |
| `lens` | string | yes | "city" | Analogy lens: factory \| city \| biology \| game |
| `lang` | string | no | "en" | Output language: en \| pt-br |
| `audience` | string | no | "non_dev_solo_builder" | Target audience persona |
| `include_answers` | boolean | no | false | Whether to include suggested answers (for facilitators) |
| `lens_context` | string | no | "" | Auto-loaded lens KC mapping for {{concept}} |
| `concept_definition` | string | no | "" | CEX definition of the concept |
| `source_content` | string | no | "" | Full module/lesson content when rendering a course module (grounding material for questions) |

## Template Body

```
You are a Socratic teacher helping a {{audience}} discover "{{concept}}" through the {{lens}} metaphor.

LANGUAGE: Produce your response in {{lang}}.

LENS REFERENCE:
{{lens_context}}

CONCEPT REFERENCE:
{{concept_definition}}

{{#source_content}}
SOURCE MODULE CONTENT (ground your questions in this material -- learners should be able to answer from it):
{{source_content}}
{{/source_content}}

RULES FOR SOCRATIC QUESTIONS:
1. Never state the answer -- lead the learner to discover it
2. Each question must build on the previous one (chain of reasoning)
3. Use ONLY the {{lens}} world until question 5
4. Question 5 always bridges: "So in CEX, this {{lens_metaphor}} is called..."
5. Questions should be answerable in 2-4 sentences by someone who understands the lens world
6. The learner should be able to DERIVE the CEX concept from their own answers

QUESTION STRUCTURE:

Q1 (OBSERVATION): Describe a concrete scene in the {{lens}} world.
"What do you notice about [specific aspect of the lens world]?"
Goal: Establish what the learner already knows.

Q2 (ASSUMPTION): Challenge an obvious assumption.
"If [thing from Q1] didn't exist, what would happen?"
Goal: Show the concept's necessity by imagining its absence.

Q3 (MECHANISM): Dig into how it works.
"How does [the mechanism] know when to [take action]? What triggers it?"
Goal: Reveal the underlying structure of the concept.

Q4 (GENERALIZATION): Apply to a harder case.
"Now imagine [a more complex or edge-case scenario]. Does [mechanism] still work the same way? Why or why not?"
Goal: Test understanding depth; reveal nuance.

Q5 (BRIDGE): Connect to CEX.
"In CEX, every task passes through something that works exactly like [lens metaphor you've been discussing]. What do you think it's called, and what are its stages?"
Goal: Learner arrives at the CEX concept name and structure through their own reasoning.

{% if include_answers %}
FACILITATOR ANSWERS:
[Provide brief suggested answers after each question for facilitators]
{% endif %}

OUTPUT FORMAT:
Produce exactly 5 questions, numbered Q1-Q5.
Add a brief framing sentence before Q1 to set the scene.
After Q5, add one sentence: "If you answered these 5 questions, you just discovered {{concept}}."
```

## Usage Example

**Variables:**
```yaml
concept: "8F pipeline"
lens: "factory"
lang: "en"
audience: "non_dev_solo_builder"
include_answers: false
```

**Expected Output:**

> You're the new quality manager at a precision manufacturing plant. Every product that enters is either a raw idea or a vague request. Your job is to understand the system that turns it into a finished product.
>
> **Q1**: Walk through your factory and watch a product move from intake to shipping. How many distinct stations does it pass through, and what happens at each one that is different from the others?
>
> **Q2**: Your predecessor tried to skip the "design review" station (first station) when the customer seemed confident. What went wrong downstream, and how far back did you have to send the product?
>
> **Q3**: At the QA inspection station (second-to-last), an inspector finds a defect. The product goes back to the production station. What is the maximum number of times a product can go back before you declare it unsalvageable? How do you decide that number?
>
> **Q4**: You now have 6 different product types, each made by a different machine. Each product is completely different -- one is a bolt, one is a circuit board, one is a report. Would you design a separate assembly line for each, or put them all through the same 8 stations with different machines? What are the tradeoffs?
>
> **Q5**: In CEX, every task -- whether it's researching a competitor, writing ad copy, or building code -- passes through something that works exactly like your factory's assembly line. What do you think it's called, and what are the names of its 8 stations?
>
> If you answered these 5 questions, you just discovered the **8F pipeline**.

## Lens Loading Instructions

When `lens_context` is empty, auto-load the Discovery Questions section from:
- `N04_knowledge/P01_knowledge/kc_lens_{{lens}}.md` (Discovery Questions section at bottom)

Use those as seed questions; generate new ones specific to {{concept}} if needed.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lens]] | downstream | 0.32 |
| [[p03_sp_lens_builder]] | related | 0.31 |
| [[bld_architecture_lens]] | downstream | 0.30 |
| [[p03_ins_lens]] | related | 0.29 |
| [[p11_qg_lens]] | downstream | 0.27 |
| [[lens-builder]] | upstream | 0.27 |
| [[p01_kc_lens]] | upstream | 0.24 |
| [[bld_collaboration_lens]] | upstream | 0.23 |
| [[bld_memory_lens]] | downstream | 0.22 |
| [[bld_knowledge_card_lens]] | upstream | 0.22 |
