---
kind: quality_gate
id: p11_qg_director
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of supervisor artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: supervisor"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, supervisor, P11, P08, governance, orchestration, dispatch]
tldr: "Gates for supervisor artifacts — wave topology + dispatch config + signal protocol ready for multi-builder coordination."
domain: supervisor
created: "2026-04-06"
updated: "2026-04-06"
density_score: 0.90
related:
  - bld_examples_supervisor
  - bld_collaboration_supervisor
  - p03_sp_director_builder
  - bld_instruction_supervisor
  - supervisor-builder
  - bld_architecture_supervisor
  - p01_kc_supervisor
  - bld_knowledge_card_supervisor
  - bld_config_supervisor
  - bld_schema_supervisor
---

## Quality Gate

# Gate: supervisor
## Definition
| Field     | Value                                               |
|-----------|-----------------------------------------------------|
| metric    | orchestration completeness + dispatch navigability  |
| threshold | 8.0                                                 |
| operator  | >=                                                  |
| scope     | all supervisor artifacts (P08)                        |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = broken dispatch |
| H02 | id matches `^ex_director_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Mission runner relies on this |
| H04 | kind == "supervisor" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, title, version, topic, builders, dispatch_mode, signal_check, quality, tags, tldr | Completeness |
| H07 | llm_function == "ORCHESTRATE" | Supervisor orchestrates, never executes |
| H08 | builders list has >= 2 entries | Single-builder supervisor is pointless — use direct spawn |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 |
| S02 | tags is list, len >= 3, includes "supervisor" | 0.5 |
| S03 | wave_topology defined with >= 1 wave | 1.0 |
| S04 | fallback_per_builder covers every builder in list | 1.0 |
| S05 | dispatch_mode is explicit (not defaulted) | 0.5 |
| S06 | signal_check is explicit boolean (not inferred) | 0.5 |
| S07 | body has ## Wave Topology with wave sequence documented | 1.0 |
| S08 | body has ## Routing with explicit NOT-when exclusions | 0.5 |
| S09 | density_score >= 0.85 | 0.5 |
| S10 | No task execution logic in body (purity check) | 1.0 |
Weights sum: 7.5. Normalize: divide each by 7.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference supervisor definition |
| >= 8.0 | PUBLISH — register in dispatch system, deploy supervisor |
| >= 7.0 | REVIEW — complete wave topology or sharpen builder list |
| < 7.0  | REJECT — rework orchestration plan and dispatch config |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical mission requiring immediate multi-builder dispatch |
| approver | p08-chief |
| audit_trail | Log in records/audits/ with justification and timestamp |
| expiry | 72h — full gate pass required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
