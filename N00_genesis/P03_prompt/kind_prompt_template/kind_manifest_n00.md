---
id: n00_prompt_template_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Prompt Template -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, prompt_template, p03, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A prompt_template is a reusable template with `{{variable}}` placeholders that generates concrete prompts when hydrated with context. It separates the stable structure of a prompt (instructions, role, format) from the dynamic content (brand, domain, audience) so the same template can be instantiated across many contexts. The output is a parameterized prompt artifact ready for runtime hydration via brand_inject.py or equivalent.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `prompt_template` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| variables | list | yes | All `{{VAR}}` placeholders with descriptions |
| template_body | string | yes | The full prompt text with placeholders embedded |
| required_variables | list | yes | Variables that must be provided at hydration time |
| output_format | string | no | Expected output format when this template is used |

## When to use
- When building a reusable prompt that will be instantiated with different brand or domain values
- When creating builder ISOs that other nuclei will hydrate at runtime
- When the same prompt structure applies to multiple use cases with varying parameters

## Builder
`archetypes/builders/prompt_template-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind prompt_template --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: tpl_cold_email_outreach
kind: prompt_template
pillar: P03
nucleus: n02
title: "Cold Email Outreach Template"
version: 1.0
quality: null
---
variables:
  - BRAND_NAME: "Company name"
  - TARGET_PERSONA: "Ideal customer role"
  - VALUE_PROP: "Primary value proposition"
required_variables: [BRAND_NAME, TARGET_PERSONA, VALUE_PROP]
template_body: |
  Write a cold email from {{BRAND_NAME}} to a {{TARGET_PERSONA}}.
  Lead with {{VALUE_PROP}}. Keep under 150 words. End with a soft CTA.
```

## Related kinds
- `prompt_version` (P03) -- version snapshot of a prompt_template after changes
- `system_prompt` (P03) -- identity-level template consumed by agents at boot
- `constraint_spec` (P03) -- constraints applied during template hydration
- `action_prompt` (P03) -- runtime invocation that hydrates a prompt_template
