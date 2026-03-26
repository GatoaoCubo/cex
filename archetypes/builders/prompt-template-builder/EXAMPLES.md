---
id: examples_prompt_template_builder
kind: examples
pillar: P07
llm_function: GOVERN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [examples, prompt-template, P03, golden, anti-example]
---

# Examples — prompt-template-builder

## Golden Example

A complete, valid `prompt_template` artifact with 19+ fields.

```yaml
---
id: p03_pt_knowledge_card_production
kind: prompt_template
pillar: P03
title: "Knowledge Card Production Template"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: PYTHA
variables:
  - name: topic
    type: string
    required: true
    default: null
    description: The subject or concept the knowledge card will cover
  - name: domain
    type: string
    required: true
    default: null
    description: The knowledge domain (e.g., machine_learning, finance, biology)
  - name: audience
    type: string
    required: false
    default: "intermediate"
    description: Target reader level (beginner, intermediate, expert)
  - name: max_sections
    type: integer
    required: false
    default: 5
    description: Maximum number of body sections to generate
  - name: include_examples
    type: boolean
    required: false
    default: true
    description: Whether to include concrete examples in each section
  - name: source_refs
    type: list
    required: false
    default: []
    description: List of source URLs or citation keys to incorporate
variable_syntax: "mustache"
composable: false
domain: knowledge
quality: 0.92
tags: [knowledge-card, pytha, production, parameterized]
tldr: "Generates a structured knowledge card for any topic and domain with configurable depth."
keywords: [knowledge, card, synthesis, structured, reusable, topic]
density_score: 0.87
---

# Knowledge Card Production Template

## Purpose

Produces a structured knowledge card for any topic within a specified domain. Reuse scope: any subject requiring a dense, well-organized reference document. Invoke once per topic; vary `topic`, `domain`, and `audience` to produce distinct cards from the same mold.

## Variables Table

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| topic | string | true | null | The subject or concept the knowledge card will cover |
| domain | string | true | null | The knowledge domain (e.g., machine_learning, finance) |
| audience | string | false | "intermediate" | Target reader level (beginner, intermediate, expert) |
| max_sections | integer | false | 5 | Maximum number of body sections to generate |
| include_examples | boolean | false | true | Whether to include concrete examples in each section |
| source_refs | list | false | [] | List of source URLs or citation keys to incorporate |

## Template Body

```
You are a knowledge synthesis expert. Produce a knowledge card for the following topic.

Topic: {{topic}}
Domain: {{domain}}
Audience level: {{audience}}
Maximum sections: {{max_sections}}
Include examples: {{include_examples}}
Source references: {{source_refs}}

Structure your output as follows:
1. TLDR (1 sentence)
2. Core Definition (2-3 sentences, precise, domain-appropriate)
3. Key Concepts (up to {{max_sections}} bullet points)
4. Relationships (how {{topic}} connects to adjacent concepts in {{domain}})
5. Common Misconceptions (2-3 items, audience-calibrated for {{audience}})
{{#include_examples}}
6. Concrete Examples (2-3 examples grounded in {{domain}})
{{/include_examples}}
7. References: {{source_refs}}

Calibrate terminology and depth for a {{audience}}-level reader in {{domain}}.
```

## Quality Gates

| Gate | Status | Notes |
|---|---|---|
| H01 id pattern | PASS | `p03_pt_knowledge_card_production` matches `^p03_pt_[a-z][a-z0-9_]+$` |
| H02 required fields | PASS | id, kind, title, variables, quality all present |
| H03 no undeclared vars | PASS | All `{{vars}}` in body declared in variables list |
| H04 no unused vars | PASS | All 6 declared variables appear in template body |
| H05 size <= 8192 bytes | PASS | ~1.8KB |
| H06 valid syntax tier | PASS | variable_syntax: mustache |
| H07 var fields complete | PASS | All 6 vars have name, type, required, default, description |
| H08 body non-empty | PASS | Body has 7 structured sections with multiple {{vars}} |

## Examples

### Filled Example

**Variables:**
```yaml
topic: "Retrieval-Augmented Generation"
domain: "machine_learning"
audience: "intermediate"
max_sections: 5
include_examples: true
source_refs: ["Lewis et al. 2020", "https://arxiv.org/abs/2005.11401"]
```

**Rendered Output (excerpt):**
```
Topic: Retrieval-Augmented Generation
Domain: machine_learning
Audience level: intermediate
Maximum sections: 5
Include examples: true
Source references: ["Lewis et al. 2020", "https://arxiv.org/abs/2005.11401"]

Structure your output as follows:
1. TLDR (1 sentence)
2. Core Definition (2-3 sentences, precise, domain-appropriate)
3. Key Concepts (up to 5 bullet points)
4. Relationships (how Retrieval-Augmented Generation connects to adjacent concepts in machine_learning)
5. Common Misconceptions (2-3 items, audience-calibrated for intermediate)
6. Concrete Examples (2-3 examples grounded in machine_learning)
7. References: ["Lewis et al. 2020", "https://arxiv.org/abs/2005.11401"]
```
```

---

## Anti-Example

The following artifact FAILS and must NOT be used as a model.

```yaml
---
id: knowledge_card_template
kind: prompt_template
title: Knowledge Card
variables: []
---
You are an expert. Write a knowledge card about the topic.
The topic is important in the domain.
```

### Failures (8)

1. **[H01] ID pattern violation**: `knowledge_card_template` does not match `^p03_pt_[a-z][a-z0-9_]+$` — missing `p03_pt_` prefix
2. **[H02] Missing required fields**: `pillar`, `quality`, `variable_syntax`, `composable`, `domain`, `tldr`, `version`, `created`, `updated`, `author` all absent
3. **[H03/H04] Variables empty, body references none**: `variables: []` but body references "the topic" and "the domain" as implicit slots — undeclared dynamic content
4. **[H08] Template body is not parameterized**: "the topic" and "the domain" are prose, not `{{variables}}` — this is a static user_prompt, not a reusable template mold
5. **[H07] No variable objects defined**: variables list is empty — no name, type, required, default, or description for any slot
6. **[BODY] Missing all 5 required body sections**: Purpose, Variables Table, Template Body, Quality Gates, and Examples sections are all absent
7. **[KIND CONFUSION] This is a user_prompt, not a prompt_template**: Fixed text with no substitution slots has no reuse contract — it will always produce the same output regardless of invocation context
8. **[SCHEMA DRIFT] Frontmatter does not match OUTPUT_TEMPLATE.md**: None of the REC fields (keywords, density_score, tags, composable, variable_syntax) are present — artifact cannot be validated or pool-submitted
