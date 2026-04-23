---
id: p03_pt_marketing_task_execution
kind: prompt_template
pillar: P03
title: "Marketing Task Execution Template"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: prompt-template-builder
variables:
  - name: task_type
    type: string
    required: true
    default: null
    description: The specific marketing deliverable to produce (e.g., email subject line, social caption, ad headline, landing page hero copy)
  - name: target_audience
    type: string
    required: true
    default: null
    description: Description of the intended reader — demographics, pain points, and knowledge level
  - name: brand_voice
    type: string
    required: true
    default: null
    description: Tone and personality descriptors that govern word choice and register (e.g., "conversational and witty", "authoritative and technical")
  - name: product_name
    type: string
    required: true
    default: null
    description: Name of the product, service, or offer being promoted
  - name: key_benefits
    type: list
    required: true
    default: null
    description: Ordered list of core value propositions to weave into the copy, highest-impact first
  - name: channel
    type: string
    required: true
    default: null
    description: Distribution channel that constrains format and length (e.g., Instagram, email newsletter, Google Ads, landing page)
  - name: cta
    type: string
    required: false
    default: "Learn More"
    description: Call-to-action phrase the copy must drive the reader toward
  - name: word_limit
    type: integer
    required: false
    default: 200
    description: Maximum word count for the output copy
  - name: competitor_differentiation
    type: string
    required: false
    default: null
    description: One-sentence statement of what sets this product apart from alternatives; used as the sharpest hook when present
variable_syntax: "mustache"
composable: true
domain: marketing
quality: 9.2
tags: [prompt-template, marketing, copywriting, P03, reusable, multi-channel]
tldr: "Generates persuasive marketing copy for any channel, audience, and task type with enforced brand voice and CTA focus."
keywords: [marketing, copywriting, ads, CTA, brand voice, social media, email, landing page, conversion]
density_score: 0.88
injection_point: user
related:
  - p03_pt_brand_task_driver
  - p03_sp_marketing_nucleus
  - examples_prompt_template_builder
  - p03_pt_creation_task
  - p01_kc_brand_voice_consistency_channels
  - n02_tool_copy_analyzer
  - p03_ins_prompt_template
  - schema_prompt_template_builder
  - p03_ap_visual_frontend_marketing
  - tpl_content_distribution_plan
---
## Purpose

Produces channel-specific marketing copy calibrated to a named audience and an enforced brand voice. Reuse scope: any single-channel marketing deliverable — email subject lines, social captions, paid ad headlines, CTA button variants, landing page hero copy, or product descriptions. Invoke once per deliverable; vary `task_type`, `channel`, and `target_audience` to produce distinct copy assets from the same mold. Marked `composable: true` — embed as a copy-generation block inside larger campaign or funnel templates.

## Variables Table

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| task_type | string | true | null | The specific marketing deliverable to produce |
| target_audience | string | true | null | Reader demographics, pain points, and knowledge level |
| brand_voice | string | true | null | Tone and personality descriptors governing word choice |
| product_name | string | true | null | Name of the product, service, or offer being promoted |
| key_benefits | list | true | null | Ordered value propositions, highest-impact first |
| channel | string | true | null | Distribution channel constraining format and length |
| cta | string | false | "Learn More" | Call-to-action phrase the copy drives toward |
| word_limit | integer | false | 200 | Maximum word count for the output |
| competitor_differentiation | string | false | null | One-sentence differentiator; used as hook when present |

## Template Body

```
You are a senior conversion copywriter. Your task: produce {{task_type}} copy for {{channel}}.

## Assignment
- Product: {{product_name}}
- Audience: {{target_audience}}
- Brand voice: {{brand_voice}}
- Word limit: {{word_limit}}
- CTA: {{cta}}

## Value Propositions
Use all of the following; sequence them by resonance with {{target_audience}}:
{{#key_benefits}}
- {{.}}
{{/key_benefits}}

{{#competitor_differentiation}}
## Differentiation Angle
{{competitor_differentiation}}
This is your sharpest hook — lead with it or anchor the headline to it.
{{/competitor_differentiation}}

## Channel Constraints
Write specifically for {{channel}}. Apply its native format, character limits, and
engagement conventions. Copy that ignores channel context will be rejected — adapt
sentence length, whitespace, and structure to what performs on {{channel}}.

## Output Rules
1. Produce final {{task_type}} copy only — no preamble, no meta-commentary.
2. Stay within {{word_limit}} words.
3. Every sentence must advance the reader toward: "{{cta}}".
4. Voice must match throughout: {{brand_voice}}.
5. If {{channel}} supports A/B testing conventions (e.g. email subject lines, ad
   headlines), produce exactly 2 variants labeled A and B.
```

## Quality Gates

| Gate | Status | Notes |
|---|---|---|
| H01 YAML parses | PASS | Frontmatter is valid YAML |
| H02 id namespace | PASS | `p03_pt_marketing_task_execution` matches `^p03_pt_[a-z][a-z0-9_]+$` |
| H03 id equals filename stem | PASS | Filename: `p03_pt_marketing_task_execution.md` |
| H04 kind literal | PASS | `kind: prompt_template` |
| H05 quality null | PASS | `quality: null` |
| H06 required frontmatter fields | PASS | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 body contains `{{variable}}` | PASS | Multiple `{{}}` slots present in Template Body |
| H08 body vars == declared vars | PASS | All 9 declared variables appear in body; no undeclared slots |
| H09 injection_point declared | PASS | `injection_point: user` |

## Examples

### Example A — Social Caption (Instagram)

**Variables**
```yaml
task_type: "Instagram caption"
target_audience: "freelance designers aged 25-35 who feel overwhelmed by client revision cycles"
brand_voice: "direct, empathetic, and slightly irreverent"
product_name: "Loopless"
key_benefits:
  - "Cuts client revision rounds from 6 to 1 on average"
  - "Auto-generates revision briefs from voice notes"
  - "Integrates with Figma and Notion in one click"
channel: "Instagram"
cta: "Try free for 14 days"
word_limit: 80
competitor_differentiation: "Unlike generic project tools, Loopless was built exclusively for the designer-client feedback loop"
```

**Rendered Output**
```
Six rounds of revisions. Sound familiar? 🙃

Loopless turns client voice notes into structured briefs — so your next revision
is your last. Figma + Notion, one click, zero chaos.

Built exclusively for the designer-client feedback loop. Not a generic PM tool.

Try free for 14 days → link in bio
```

---

### Example B — Email Subject Line (A/B)

**Variables**
```yaml
task_type: "email subject line"
target_audience: "B2B SaaS founders who struggle to convert trial users to paid"
brand_voice: "data-driven and conversational"
product_name: "Nudgeflow"
key_benefits:
  - "Identifies at-risk trial users 72 hours before churn"
  - "Sends personalised in-app nudges automatically"
  - "Increases trial-to-paid conversion by 34% on average"
channel: "email newsletter"
cta: "See the case study"
word_limit: 15
competitor_differentiation: null
```

**Rendered Output**
```
A: Your trial users are leaving 72 hours before you notice
B: +34% trial-to-paid — here's what Nudgeflow changed
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_brand_task_driver]] | sibling | 0.46 |
| [[p03_sp_marketing_nucleus]] | related | 0.29 |
| [[examples_prompt_template_builder]] | downstream | 0.29 |
| [[p03_pt_creation_task]] | sibling | 0.26 |
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.25 |
| [[n02_tool_copy_analyzer]] | downstream | 0.24 |
| [[p03_ins_prompt_template]] | related | 0.24 |
| [[schema_prompt_template_builder]] | downstream | 0.24 |
| [[p03_ap_visual_frontend_marketing]] | related | 0.23 |
| [[tpl_content_distribution_plan]] | sibling | 0.23 |
