---
kind: examples
id: bld_examples_supervisor
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of supervisor artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Supervisor"
version: "1.0.0"
author: n03_builder
tags: [supervisor, builder, examples]
tldr: "Golden and anti-examples for supervisor construction, demonstrating ideal structure and common pitfalls."
domain: "supervisor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: supervisor-builder
## Golden Example
INPUT: "Create supervisor for a brand launch mission coordinating research, content, and marketing"
OUTPUT:
```yaml
id: ex_director_brand_launch
kind: supervisor
pillar: P08
title: "Brand Launch Supervisor"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n07_orchestrator"
topic: "brand_launch"
builders: [research-builder, content-builder, marketing-builder, landing-page-builder]
dispatch_mode: sequential
signal_check: true
wave_topology:
  - wave: 1
    builders: [research-builder]
    gate: "signal_research_complete"
  - wave: 2
    builders: [content-builder, marketing-builder]
    gate: "signal_content_and_marketing_complete"
  - wave: 3
    builders: [landing-page-builder]
    gate: "signal_launch_ready"
fallback_per_builder:
  research-builder: retry
  content-builder: retry
  marketing-builder: substitute(copywriter-builder)
  landing-page-builder: abort
llm_function: ORCHESTRATE
domain: "brand_launch"
quality: 8.9
tags: [supervisor, brand, launch, orchestration, P08]
tldr: "Coordinates brand launch across 4 builders in 3 waves — research first, then parallel content+marketing, then landing page."
density_score: 0.89
```
## Identity
Brand Launch Supervisor coordinates a 4-builder mission for launching a new brand presence.
Dispatches research first, then content and marketing in parallel, then landing page assembly.
## Builders
| Builder | Nucleus | Role |
|---------|---------|------|
| research-builder | N01 | Competitor analysis and market positioning |
| content-builder | N03 | Core content artifacts (copy, assets) |
| marketing-builder | N02 | Campaign copy, CTAs, email sequences |
| landing-page-builder | N03 | Final landing page assembly |
## Wave Topology
Wave 1: research-builder -> signal_research_complete
Wave 2: content-builder + marketing-builder (parallel) -> signal_content_and_marketing_complete
Wave 3: landing-page-builder -> signal_launch_ready
## Dispatch Config
Mode: sequential (waves are ordered). Signal check: true. Timeout: 1800s per wave.
WHY THIS IS GOLDEN:
- quality: null (H05) | id ex_director_ pattern (H02) | kind: supervisor (H04)
- builders: 4 entries (H08) | llm_function: ORCHESTRATE (H07) | signal_check: true (H06)
- wave_topology: 3 waves (S03) | fallback_per_builder: all 4 covered (S04)
- No task execution logic (S10) | density: 0.89 (S09)
## Anti-Example
INPUT: "Create supervisor that writes marketing copy and coordinates builders"
BAD OUTPUT:
```yaml
id: marketing_director
kind: supervisor
pillar: P02
builders: [copywriter]
dispatch_mode: auto
signal_check: maybe
quality: 7.5
```
## Content
Here is the marketing copy I wrote for the campaign: "Buy our product today!"
Also dispatching copywriter to write more copy.
FAILURES:
1. id: no `ex_director_` prefix -> H02 FAIL
2. pillar: "P02" not "P08" -> H06 FAIL
3. quality: 7.5 (not null) -> H05 FAIL
4. builders: only 1 entry (need >= 2) -> H08 FAIL
5. dispatch_mode: "auto" not in enum -> H06 FAIL
6. signal_check: "maybe" not boolean -> H06 FAIL
7. Supervisor WRITES copy ("Buy our product") -> S10 FAIL (purity violation)
8. Missing fields: topic, title, version, tags, tldr, llm_function -> H06 FAIL
9. No wave_topology -> S03 FAIL
10. No fallback_per_builder -> S04 FAIL
