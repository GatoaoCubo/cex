---
id: p07_rt_8f_constrain
kind: reasoning_trace
pillar: P07
title: "Reasoning Trace -- F1 CONSTRAIN Live Example"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: pipeline-reasoning
quality: 8.8
tags: [reasoning_trace, F1, CONSTRAIN, intent-resolution, 8F, example, coc]
tldr: "Live F1 CONSTRAIN trace for input: 'build a landing page for my SaaS'. Shows intent resolution, kind mapping, schema load, and ambiguity handling. Loadable as F2 BECOME ISO to teach any LLM how CONSTRAIN works."
density_score: 0.90
updated: "2026-04-17"
related:
  - bld_memory_landing_page
  - p03_ins_prompt_compiler
  - bld_collaboration_landing_page
  - bld_schema_landing_page
  - bld_output_template_landing_page
  - bld_tools_landing_page
  - landing-page-builder
  - bld_architecture_kind
  - p01_kc_prompt_compiler
  - report_intent_resolution_value_prop
---

# Reasoning Trace: F1 CONSTRAIN

**Input:** `"build a landing page for my SaaS"`
**Nucleus:** N03 (Engineering)
**Timestamp:** 2026-04-17T14:30:00

---

## F-Annotation: F1 CONSTRAIN

F1 is intent resolution. It transforms raw user input into a typed tuple:
`{kind, pillar, nucleus, verb, constraints}`.

Without F1, F2-F8 operate on ambiguous input. F1 is the "type safety" of the pipeline.

---

## Step 1: Verb Resolution

| Input token | Candidate verbs | Resolution |
|------------|----------------|-----------|
| "build" | create, scaffold, generate, design | `verb = create` (artifact construction) |
| "landing page" | (direct kind match) | `kind = landing_page` |
| "SaaS" | context tag | `domain = saas, vertical = b2b_software` |

**Resolution confidence:** 91% (direct kind match)

---

## Step 2: Kind Lookup

```
cex_intent_resolver.py: "build landing page"
  -> pattern match: "landing page" -> landing_page (kinds_meta.json)
  -> pillar: P05 (Output)
  -> nucleus: N03 (Engineering / builder)
  -> max_bytes: 16384
  -> naming: landing_page_{domain}.md
  -> confidence: 91%
```

Verified against `N00_genesis/P05_output/_schema.yaml`:
- kind: landing_page
- pillar: P05
- builder: `archetypes/builders/landing-page-builder/`
- isolation: worktree (heavy builder, per frontmatter)

---

## Step 3: Schema Load

```yaml
# From N00_genesis/P05_output/_schema.yaml
kind: landing_page
pillar: P05
required_fields:
  - id
  - kind
  - title
  - version
  - created
  - author
  - domain
  - quality
  - tags
  - tldr
  - target_audience
  - cta_primary
optional_fields:
  - cta_secondary
  - brand_voice
  - sections[]
max_bytes: 16384
```

---

## Step 4: Ambiguity Resolution

| Ambiguity | Options considered | Resolution |
|-----------|-------------------|-----------|
| "SaaS" — product or company? | (a) product landing page, (b) company homepage | Need GDP decision: "Is this for a specific product or the company?" |
| Audience unclear | (a) developers, (b) business buyers, (c) end users | GDP: "Who is the primary visitor?" |
| CTA unclear | (a) free trial, (b) demo, (c) contact sales | Inferred from SaaS context: likely free_trial |

**GDP gate:** 2 decisions needed (audience + product scope).
If running autonomously with decision_manifest.yaml: check manifest for `landing_page.target_audience`.
If no manifest entry: use `★ Recommended` = `b2b_software_buyers` + flag for user review.

---

## Step 5: CONSTRAIN Output

```
F1 CONSTRAIN
  kind       : landing_page
  pillar     : P05
  schema     : N00_genesis/P05_output/_schema.yaml
  max_bytes  : 16384
  naming     : landing_page_saas_product.md
  confidence : 91%
  ambiguities: target_audience (defaulted: b2b_software_buyers), cta (defaulted: free_trial)
  gdp_needed : yes (2 decisions -- flag in F4 if no manifest)
  nucleus    : N03 (builder)
```

---

## Step 6: What CONSTRAIN Ruled Out

| Rejected interpretation | Why rejected |
|------------------------|-------------|
| `kind = component_map` | "landing page" is not a component map |
| `kind = pitch_deck` | "landing" implies web page, not slide deck |
| `nucleus = N06` | N06 handles pricing/commercial; N03 handles build/scaffold |
| `kind = pricing_page` | SaaS context without "pricing" keyword -> landing_page first |

---

## Key Insights (What F1 Teaches)

| Principle | Demonstrated here |
|-----------|-------------------|
| **Direct match wins** | "landing page" -> `landing_page` without fuzzy search |
| **Context narrows pillar** | "build" -> P05 Output (production artifacts) |
| **Ambiguity is explicit** | 2 GDP decisions flagged, not silently assumed |
| **Confidence score matters** | 91% = proceed; <60% = GDP first |
| **Schema is loaded, not recalled** | Every F1 reads `_schema.yaml`; no cached assumptions |

---

## Cross-References

- `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md` — authoritative kind-to-pillar map
- `N03_engineering/P08_architecture/pattern_8f_full_trace.md` — F1 field format in full trace
- `N03_engineering/P07_evals/reasoning_trace_8f_govern.md` — F7 trace complement
- `N03_engineering/P01_knowledge/kc_intent_resolution_map.md` — 123-kind resolution table

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_landing_page]] | downstream | 0.32 |
| [[p03_ins_prompt_compiler]] | upstream | 0.30 |
| [[bld_collaboration_landing_page]] | downstream | 0.30 |
| [[bld_schema_landing_page]] | upstream | 0.29 |
| [[bld_output_template_landing_page]] | upstream | 0.29 |
| [[bld_tools_landing_page]] | upstream | 0.29 |
| [[landing-page-builder]] | upstream | 0.29 |
| [[bld_architecture_kind]] | downstream | 0.28 |
| [[p01_kc_prompt_compiler]] | upstream | 0.26 |
| [[report_intent_resolution_value_prop]] | upstream | 0.25 |
