---
id: n00_sdk_example_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "SDK Example -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, sdk_example, p04, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An sdk_example is a canonical code example showing correct integration patterns for an SDK, demonstrating authentication, error handling, pagination, and idiomatic usage. It serves as the gold standard that agents inject during F3 when building new api_clients or tool integrations. The output is a tested, runnable code snippet that prevents agents from fabricating incorrect SDK usage patterns.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `sdk_example` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| sdk_name | string | yes | SDK being demonstrated (e.g., anthropic, openai, supabase) |
| language | string | yes | Programming language: python, typescript, go |
| pattern | string | yes | Integration pattern: auth, streaming, tool_use, batch, retry |
| tested | boolean | yes | Whether the example has been verified to run correctly |

## When to use
- When N03 or N05 builds an api_client and needs a canonical usage example to inject at F3
- When documenting CEX SDK (cex_sdk) integration patterns for new nucleus builders
- When generating onboarding code examples that demonstrate correct CEX runtime usage

## Builder
`archetypes/builders/sdk_example-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind sdk_example --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sdk_ex_anthropic_tool_use_py
kind: sdk_example
pillar: P04
nucleus: n03
title: "Anthropic Tool Use Example (Python)"
version: 1.0
quality: null
---
sdk_name: anthropic
language: python
pattern: tool_use
tested: true
```

## Related kinds
- `api_client` (P04) -- client artifact that sdk_example demonstrates how to use
- `function_def` (P04) -- tool definition that the sdk_example shows being called
- `knowledge_card` (P01) -- knowledge card that stores sdk_example as reusable reference
- `prompt_technique` (P03) -- complementary prompt pattern for the SDK interaction
