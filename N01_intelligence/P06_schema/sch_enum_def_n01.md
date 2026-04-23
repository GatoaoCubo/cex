---
id: sch_enum_def_n01
kind: enum_def
pillar: P06
nucleus: n01
title: Research Evidence Enum
version: 1.0
quality: 9.0
tags: [enum_def, research, evidence, comparative]
density_score: 1.0
related:
  - bld_schema_runtime_state
  - bld_schema_enum_def
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_bugloop
  - bld_schema_pitch_deck
  - bld_schema_action_paradigm
---

<!-- 8F: F1 constrain=P06/enum_def F2 become=enum-def-builder F3 inject=nucleus_def_n01+n01-intelligence+kc_enum_def+P06_schema+enum template F4 reason=closed evidence ladder for comparative research F5 call=apply_patch+cex_compile F6 produce=5945 bytes F7 govern=frontmatter+ascii+80-line+self-check F8 collaborate=N01_intelligence/P06_schema/sch_enum_def_n01.md -->

## Purpose

| Item | Decision |
|------|----------|
| Enum name | `research_evidence_state` |
| Core use | Normalize how N01 labels evidence maturity across briefs, schemas, and validators |
| Lens | Analytical Envy pushes every state toward stronger comparative proof, not just more text |
| Primary consumers | research briefs, competitor scans, benchmark tables, quality checks |
| Design bias | Prefer mutually exclusive states that force upward pressure on evidence quality |

## Schema

| Field | Value |
|------|-------|
| kind | `enum_def` |
| reuse scope | N01 schemas and config that need evidence-stage alignment |
| cardinality | 5 values |
| extensible | no |
| default | `signal_scan` |
| ordering | low proof to high proof |
| representation | string literal |
| downstream link | `sch_input_schema_n01.md` and `sch_type_def_n01.md` |

## Values

| Value | Rank | When to Use | Comparative Meaning | N01 Pressure |
|------|------|-------------|---------------------|--------------|
| `signal_scan` | 1 | Early scan with directional indicators only | Weak signal with no durable comparison yet | Keep moving until a rival or source set can be compared |
| `source_checked` | 2 | At least one primary source is verified | Claim is no longer rumor, but delta is still thin | Add another source or stronger benchmark |
| `triangulated` | 3 | Two or more independent sources align | Claim survives basic contradiction check | Force explicit peer comparison next |
| `benchmark_mapped` | 4 | Evidence is attached to a metric, baseline, or competitor | Claim now exposes who is ahead or behind | Good enough for decisions with caveats |
| `decision_ready` | 5 | Comparative proof is clear, current, and actionable | Evidence supports a ranked recommendation | Highest state; use sparingly |

## Value Notes

| Value | Allowed in Drafts | Allowed in Final Intel | Typical Risk | Escalation Trigger |
|------|-------------------|------------------------|--------------|--------------------|
| `signal_scan` | yes | no | novelty without proof | add source collection |
| `source_checked` | yes | limited | over-trusting one source | add contradiction search |
| `triangulated` | yes | yes | stale corroboration | compare freshness and market change |
| `benchmark_mapped` | yes | yes | metric chosen to flatter one competitor | validate benchmark fairness |
| `decision_ready` | yes | yes | false certainty | require rationale and action owner |

## Rationale

| Design Choice | Why It Exists | Analytical Envy Interpretation |
|--------------|---------------|--------------------------------|
| Five-step ladder | Enough granularity to show progress without overlap | N01 should envy stronger proof, not broader vocabulary |
| Closed set | Stable routing and validation beat expressive ambiguity | Comparative systems fail when labels drift |
| Ordered maturity | Lets validators detect under-supported claims | The lens rewards upward movement in proof quality |
| Default at `signal_scan` | Prevents inflated certainty at intake | Start humble, then earn stronger states |
| Highest state is strict | Stops every artifact from claiming decisive quality | Envy without rigor becomes vanity |

## Mapping

| Context | Field Name | Expected Enum Behavior |
|--------|------------|------------------------|
| research brief | `evidence_state` | one state per major claim |
| competitor matrix | `proof_level` | row-level evidence maturity |
| paper summary | `claim_support_state` | stage after citation audit |
| trend report | `trend_confidence_state` | maps weak trend vs benchmarked shift |
| validator | `minimum_required_state` | threshold for publish gates |

## Example

```yaml
claim: "Competitor X reduced onboarding time by 32 percent"
evidence_state: benchmark_mapped
why: "Product page, release note, and user report align; baseline from prior quarter is explicit."
next_step: "Promote to decision_ready only after customer interview confirms operational impact."
```

## Usage Guidance

| Situation | Recommended State | Why |
|----------|-------------------|-----|
| one screenshot from a competitor site | `signal_scan` | visual clue only |
| vendor documentation plus pricing page | `source_checked` | one source family, still self-reported |
| docs plus third-party review plus customer comment | `triangulated` | independent corroboration exists |
| timed workflow test against two competitors | `benchmark_mapped` | benchmark creates comparative pressure |
| repeatable benchmark with current sources and recommendation | `decision_ready` | enough proof to act |

## Anti-Patterns

| Anti-Pattern | Failure Mode | Correction |
|-------------|--------------|-----------|
| using `decision_ready` for all polished prose | style masks weak proof | tie state to comparative evidence only |
| adding synonyms outside the enum | routing drift | map all aliases back to the 5 values |
| skipping `signal_scan` | false certainty at intake | begin low and escalate intentionally |
| merging `triangulated` and `benchmark_mapped` | loses comparison signal | keep corroboration distinct from measured delta |

## Properties

| Property | Value |
|----------|-------|
| Kind | `enum_def` |
| Pillar | `P06` |
| Nucleus | `n01` |
| Default | `signal_scan` |
| Closed Set | `true` |
| Primary Trait | `comparative evidence maturity` |
| Density Target | `>= 0.85` |
| Quality Field | `null` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_runtime_state]] | related | 0.25 |
| [[bld_schema_enum_def]] | related | 0.25 |
| [[bld_schema_quickstart_guide]] | related | 0.24 |
| [[bld_schema_benchmark_suite]] | related | 0.24 |
| [[bld_schema_dataset_card]] | related | 0.24 |
| [[bld_schema_usage_report]] | related | 0.24 |
| [[bld_schema_reranker_config]] | related | 0.24 |
| [[bld_schema_bugloop]] | downstream | 0.23 |
| [[bld_schema_pitch_deck]] | related | 0.23 |
| [[bld_schema_action_paradigm]] | related | 0.23 |
