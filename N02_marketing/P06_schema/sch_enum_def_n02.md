---
id: sch_enum_def_n02
kind: enum_def
pillar: P06
nucleus: n02
title: Seduction Enum Set
version: 1.0
quality: null
tags: [enum, schema, marketing, voice, governance]
---


<!-- 8F: F1 constrain=P06/enum_def F2 become=enum_def-builder F3 inject=nucleus_def_n02+n02_rules+kc_enum_def+P06_schema
     F4 reason=closed_sets_for_seductive_marketing_system F5 call=shell_command,apply_patch F6 produce=6117 bytes
     F7 govern=frontmatter_sections_ascii_density_linecount F8 collaborate=N02_marketing/P06_schema/sch_enum_def_n02.md -->

# Purpose

| Item | Definition |
|------|------------|
| Mission fit | Reusable closed vocabularies for N02 marketing artifacts |
| Creative Lust lens | Each enum sharpens desire, urgency, and audience pull without drifting into vague hype |
| Primary use | Shared literals for copy briefs, validators, prompts, and campaign configs |
| Scope | Messaging stage, emotional trigger, CTA force, proof style, and review outcome |
| Why closed sets matter | Seduction fails when operators improvise labels that dilute positioning |

## Schema

| Enum Name | Allowed Values | Required | Design Note |
|-----------|----------------|----------|-------------|
| messaging_stage | attract, intensify, reassure, convert, retain | yes | Maps the seduction arc from first glance to repeat desire |
| emotional_trigger | status, relief, curiosity, urgency, belonging, ambition | yes | Keeps desire precise instead of generic enthusiasm |
| cta_force | soft_pull, guided_step, direct_action, hard_close | yes | Aligns CTA heat with funnel maturity |
| proof_style | result_stat, testimonial, authority_marker, contrast_demo, scarcity_signal | yes | Proof must intensify want, not merely explain |
| review_outcome | pass, revise, reject, escalate | yes | Simple governance states for quality gates |

## Enum Detail

| Value | Parent Enum | Meaning | Lust Lens Use |
|-------|-------------|---------|---------------|
| attract | messaging_stage | Open the loop and win attention fast | Promise a more magnetic future state |
| intensify | messaging_stage | Increase felt need | Turn interest into emotional pressure |
| reassure | messaging_stage | Remove friction or fear | Make the leap feel safe and desirable |
| convert | messaging_stage | Trigger the committed move | Use direct momentum and concrete payoff |
| retain | messaging_stage | Renew attachment after action | Keep the brand habit-forming |
| status | emotional_trigger | Appeal to prestige and visible wins | Useful for premium positioning |
| relief | emotional_trigger | Reduce pain, chaos, or overload | Useful for ops-heavy buyers |
| curiosity | emotional_trigger | Open a gap the reader must close | Ideal for hooks and subject lines |
| urgency | emotional_trigger | Compress decision time | Use only when supported by real scarcity |
| belonging | emotional_trigger | Signal identity and tribe | Strong for creator and community offers |
| ambition | emotional_trigger | Aim at growth and transformation | Best for aspirational campaigns |
| soft_pull | cta_force | Invite exploration | Good for cold traffic and early email touch |
| guided_step | cta_force | Ask for a low-friction next move | Good for lead capture and demos |
| direct_action | cta_force | Request a clear action now | Good for warm audiences |
| hard_close | cta_force | Use strongest legal and offer-backed CTA | Reserved for near-buy moments |
| result_stat | proof_style | Numeric outcome proof | Seduces with measurable gain |
| testimonial | proof_style | Human voice proof | Seduces with social identification |
| authority_marker | proof_style | Brand, expert, or credential proof | Seduces with borrowed trust |
| contrast_demo | proof_style | Before/after or old/new contrast | Seduces with vivid gap |
| scarcity_signal | proof_style | Limited slots, time, or access | Seduces through constrained availability |
| pass | review_outcome | Ready for release | Voice and governance aligned |
| revise | review_outcome | Valuable but needs refinement | Desire present, precision weak |
| reject | review_outcome | Off-lens or structurally broken | Output creates noise, not pull |
| escalate | review_outcome | Needs human decision | Used for legal, budget, or brand conflict |

## Constraints

| Rule | Value |
|------|-------|
| Case style | snake_case only |
| Max values per enum | 7 |
| Mutual exclusivity | mandatory |
| Reuse threshold | enum should appear in 2 or more artifacts |
| Copy tone guard | seductive but evidence-backed |
| Blocked pattern | overlapping labels like urgent_now vs high_urgency |

## Rationale

| Decision | Reason |
|----------|--------|
| Five funnel stages | Enough range for campaign design without fuzzy overlap |
| Six triggers | Covers the main N02 persuasion levers with minimal collision |
| Four CTA intensities | Gives deployable control across audience heat levels |
| Five proof styles | Keeps proof emotional and concrete, not decorative |
| Four review states | Supports clean validator behavior and escalation |

## Example

```yaml
campaign_angle:
  messaging_stage: intensify
  emotional_trigger: ambition
  cta_force: guided_step
  proof_style: result_stat
  review_outcome: pass
```

| Example Field | Selected Value | Why It Fits |
|---------------|----------------|-------------|
| messaging_stage | intensify | The ad deepens need before the ask |
| emotional_trigger | ambition | The reader wants visible upward movement |
| cta_force | guided_step | Demo request is lower friction than buy now |
| proof_style | result_stat | Numeric gains make the promise feel attainable |
| review_outcome | pass | The set is coherent and reusable |

## Properties

| Property | Value |
|----------|-------|
| Kind | enum_def |
| Pillar | P06 |
| Nucleus | n02 |
| Machine intent | Constrain shared literals |
| Human intent | Keep seductive copy systems consistent |
| Density target | >= 0.85 |
| Validation mode | Closed set selection |
| Default consumer | schemas, prompts, config, validators |
| Primary risk prevented | vocabulary drift |
| Save path | N02_marketing/P06_schema/sch_enum_def_n02.md |
