---
id: sch_input_schema_n01
kind: input_schema
pillar: P06
nucleus: n01
title: Intelligence Intake Schema
version: 1.0
quality: 9.0
tags: [input_schema, intake, research, comparison]
density_score: 1.0
related:
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
  - bld_schema_sandbox_config
  - bld_schema_quickstart_guide
  - bld_schema_agent_profile
  - bld_schema_input_schema
---

<!-- 8F: F1 constrain=P06/input_schema F2 become=input-schema-builder F3 inject=nucleus_def_n01+n01-intelligence+kc_input_schema+P06_schema+input template F4 reason=unilateral intake contract for comparative research F5 call=apply_patch+cex_compile F6 produce=6163 bytes F7 govern=frontmatter+ascii+80-line+self-check F8 collaborate=N01_intelligence/P06_schema/sch_input_schema_n01.md -->

## Purpose

| Item | Decision |
|------|----------|
| Contract name | `intelligence_intake` |
| Scope | Input payload for N01 research, competitor, and paper-analysis requests |
| Caller | N07 orchestration or any nucleus requesting research support |
| Lens | Analytical Envy requires every request to name the comparison pressure, not just the topic |
| Bias control | Force explicit source expectations and evidence target before work starts |

## Schema

| Field | Type | Required | Default | Constraint | Comparative Intent |
|------|------|----------|---------|------------|--------------------|
| `request_id` | string | yes | none | `^req_[a-z0-9_]+$` | Trace who asked for which comparison |
| `mission_slug` | string | yes | none | snake_case | Ties work to a larger wave or deliverable |
| `research_goal` | string | yes | none | 24-240 chars | States what must be learned |
| `comparison_axis` | string | yes | none | 12-120 chars | Forces the envy vector: speed, cost, quality, reach |
| `subject_entities` | list[string] | yes | none | 1-8 items | Names the thing being evaluated |
| `peer_entities` | list[string] | yes | none | 1-12 items | Names who the subject is measured against |
| `primary_source_expectation` | integer | yes | `2` | range `1..10` | Minimum primary sources needed |
| `time_horizon_days` | integer | yes | `90` | range `1..365` | Freshness window for evidence |
| `evidence_target` | string | yes | `triangulated` | enum from `research_evidence_state` | Controls stopping threshold |
| `deliverable_mode` | string | yes | `brief` | enum `brief|matrix|notebook|audit` | Shapes output format |
| `budget_tokens` | integer | no | `16000` | range `1000..120000` | Prevents shallow envy or runaway spend |
| `urgency` | string | no | `normal` | enum `low|normal|high|critical` | Helps trade breadth vs speed |
| `requester_role` | string | no | `orchestrator` | snake_case | Clarifies downstream accountability |
| `notes` | string | no | empty | max 400 chars | Holds caveats without polluting the contract |

## Required Set

| Order | Required Field | Why N01 Needs It |
|------|----------------|------------------|
| 1 | `request_id` | audit and retry tracing |
| 2 | `mission_slug` | mission binding |
| 3 | `research_goal` | intent clarity |
| 4 | `comparison_axis` | envy lens anchor |
| 5 | `subject_entities` | focal subject list |
| 6 | `peer_entities` | benchmark set |
| 7 | `primary_source_expectation` | evidence floor |
| 8 | `time_horizon_days` | freshness bound |
| 9 | `evidence_target` | stopping condition |
| 10 | `deliverable_mode` | output contract |

## Coercion Rules

| From | To | Rule | Risk if Skipped |
|------|----|------|-----------------|
| comma-delimited string | list[string] | split on comma, trim, drop blanks | peers collapse into one string |
| numeric string | integer | cast if digits only | budget and horizon become ambiguous |
| title case | snake_case | lower, replace spaces with underscore | trace ids drift |
| empty string | null or default | normalize before validation | false presence passes |

## Validation Notes

| Check | Pass Condition | Fail Message |
|------|----------------|-------------|
| entity count | both entity lists non-empty | "At least one subject and one peer are required." |
| comparison clarity | `comparison_axis` names one dimension | "comparison_axis must express the evaluation dimension." |
| evidence target | valid enum member only | "evidence_target must use research_evidence_state." |
| freshness | horizon within range | "time_horizon_days must be between 1 and 365." |
| source floor | expectation >= 1 | "primary_source_expectation must be at least 1." |

## Rationale

| Design Choice | Why | Analytical Envy Interpretation |
|--------------|-----|--------------------------------|
| Comparison axis is mandatory | N01 should answer "better than what" up front | Envy without a rival becomes generic analysis |
| Peer list is mandatory | Comparative work needs an actual benchmark set | Forces concrete external pressure |
| Evidence target is explicit | Prevents under-researched deliverables from looking complete | Proof level becomes a contract, not a mood |
| Budget field stays optional | Some missions are fixed-budget, others not | Control cost without blocking all work |
| Notes are capped | Keep the contract dense and operational | Overflow belongs in context docs, not intake |

## Example

```yaml
request_id: req_wave1_comp_scan
mission_slug: fractal_fill_w1
research_goal: "Compare N01 research contracts against peer nuclei and sharpen evidence governance."
comparison_axis: "evidence rigor"
subject_entities: ["n01_intelligence"]
peer_entities: ["n02_marketing", "n03_engineering", "n06_commercial"]
primary_source_expectation: 3
time_horizon_days: 30
evidence_target: benchmark_mapped
deliverable_mode: matrix
budget_tokens: 22000
urgency: high
requester_role: orchestrator
notes: "Prefer internal exemplars before external synthesis."
```

## Example Review

| Aspect | Observation |
|-------|-------------|
| comparison pressure | explicit via `evidence rigor` |
| source demand | elevated to 3 for stronger confidence |
| horizon | tight enough to avoid stale examples |
| output mode | matrix supports side-by-side envy lens |

## Properties

| Property | Value |
|----------|-------|
| Kind | `input_schema` |
| Pillar | `P06` |
| Nucleus | `n01` |
| Contract Style | `unilateral` |
| Additional Properties | `false by policy` |
| Required Count | `10` |
| Comparative Core | `comparison_axis + peer_entities` |
| Quality Field | `null` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | related | 0.49 |
| [[bld_schema_reranker_config]] | related | 0.49 |
| [[bld_schema_benchmark_suite]] | related | 0.48 |
| [[bld_schema_pitch_deck]] | related | 0.48 |
| [[bld_schema_dataset_card]] | related | 0.48 |
| [[bld_schema_multimodal_prompt]] | related | 0.47 |
| [[bld_schema_sandbox_config]] | related | 0.47 |
| [[bld_schema_quickstart_guide]] | related | 0.47 |
| [[bld_schema_agent_profile]] | related | 0.46 |
| [[bld_schema_input_schema]] | related | 0.46 |
