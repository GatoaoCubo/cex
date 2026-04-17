---
id: n00_onboarding_flow_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Onboarding Flow -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, onboarding_flow, p05, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Onboarding flow produces a structured user activation sequence that guides new users from signup to their first meaningful value moment. It defines the steps, milestones, trigger conditions, and fallback paths that move users through the activation funnel. Each milestone has success criteria and associated in-product or email nudges.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `onboarding_flow` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Product + audience + "Onboarding Flow" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| activation_milestone | string | yes | The first aha moment / value event |
| steps | list | yes | Ordered steps with action, trigger, fallback |
| time_to_activate_target | string | yes | Target time from signup to activation milestone |
| nudge_channels | list | yes | email / in-app / sms / push |
| drop_off_recovery | list | no | Re-engagement flows for each drop-off point |

## When to use
- Designing the activation experience for a new product or user segment
- Reducing time-to-value for a complex product with a steep learning curve
- Rebuilding a broken onboarding flow identified through cohort drop-off analysis

## Builder
`archetypes/builders/onboarding_flow-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind onboarding_flow --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N02 marketing + N06 commercial design activation strategy
- `{{SIN_LENS}}` -- Strategic Greed: minimize CAC by maximizing activation rate
- `{{TARGET_AUDIENCE}}` -- new user persona (persona drives step content and language)
- `{{DOMAIN_CONTEXT}}` -- product complexity, activation definition, existing drop-off data

## Example (minimal)
```yaml
---
id: onboarding_flow_cex_developer
kind: onboarding_flow
pillar: P05
nucleus: n02
title: "CEX Platform -- Developer Onboarding Flow"
version: 1.0
quality: null
---
activation_milestone: "First artifact built via 8F pipeline"
time_to_activate_target: "< 10 minutes from signup"
nudge_channels: [in-app, email]
```

## Related kinds
- `user_journey` (P05) -- full lifecycle map; onboarding flow covers the early activation phase
- `product_tour` (P05) -- in-app tour that may be step 1 of the onboarding flow
- `course_module` (P05) -- educational content that can be embedded in onboarding steps
