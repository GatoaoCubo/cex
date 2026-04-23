---
id: mem_memory_summary_n03
kind: memory_summary
pillar: P10
nucleus: N03
title: "N03 Memory Summary"
version: "1.0.0"
created: "2026-04-16"
updated: "2026-04-16"
author: n03_engineering
domain: engineering operational memory
quality: 9.1
tags: [memory_summary, p10, n03, compression, context, inventive_pride]
density_score: 1.0
related:
  - p01_kc_memory_summary
  - p10_memory_summary
  - bld_collaboration_memory_summary
  - memory-summary-builder
  - p10_lr_memory_summary_builder
  - bld_examples_memory_summary
  - bld_config_memory_summary
  - bld_instruction_memory_summary
  - p03_sp_memory_summary_builder
  - bld_knowledge_card_memory_summary
---
<!-- 8F: F1=memory_summary/P10 F2=memory-summary-builder F3=nucleus_def_n03+kc_memory_summary+P10_schema F4=lossy but high-dignity summary policy
     F5=Get-Content+rg+apply_patch+cex_compile.py F6=bytes:5093 F7=self-check:frontmatter+8f+properties+80l+ascii F8=N03_engineering/P10_memory/mem_memory_summary_n03.md -->

# N03 Memory Summary

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory_summary` |
| Pillar | `P10` |
| Nucleus | `N03` |
| Lens | `Inventive Pride` |
| Source type | session and build history |
| Compression method | structured abstractive summary |
| Target budget | under 1800 bytes |
| Mandatory sections | decisions, failures, open loops, active defaults |
| Trigger | session end or context pressure |
| Primary rule | compress narrative, preserve decisions |

## Function

N03 needs memory summaries that compress work without degrading judgment.
The summary is a briefing for future construction, not a sentimental recap.
Inventive Pride means the summary must keep what changes build quality and discard the rest.

## Required Sections

1. decisions
2. failures
3. active defaults
4. unresolved risks
5. next useful action

If a summary lacks these, it is not serving the nucleus.

## Compression Method

| Step | Action | Intent |
|-----|--------|--------|
| 1 | extract concrete decisions | preserve durable direction |
| 2 | collapse repetitive narration | reclaim byte budget |
| 3 | retain only evidence-rich failures | teach future sessions |
| 4 | list open loops explicitly | avoid hidden drift |
| 5 | remove pleasantries and filler | maintain density |

## Byte Discipline

- target under `1800` bytes
- hard stop under `2048` bytes
- use short declarative lines
- avoid quoted dialogue unless essential
- name files, tools, and kinds directly
- keep chronology only when causality matters

## Inventive Pride Lens

Proud summaries do not romanticize process.
They preserve the parts that matter:
- what was chosen
- what broke
- what remains risky
- what default should be reused
Everything else is overhead pretending to be memory.

## What Must Survive Compression

| Preserve | Why |
|---------|-----|
| final design choices | future builds must start from stable ground |
| failure causes | prevents repeated mistakes |
| active tool defaults | saves re-discovery cost |
| unresolved blockers | protects continuity |
| meaningful metrics | helps compare future sessions |

## What Should Be Dropped

| Drop | Reason |
|-----|--------|
| conversational niceties | no operational value |
| repeated observations | duplicates waste space |
| raw command chatter | too verbose for carry-forward memory |
| transient speculation | low confidence and low reuse |
| full source excerpts | belongs in knowledge artifacts, not summary |

## Failure Modes

| Failure | Result | Fix |
|--------|--------|-----|
| summary as transcript | context cost stays high | abstract aggressively |
| summary as slogan | loses operational details | restore decisions and risks |
| missing failures | repeat mistakes | preserve failure causes |
| missing defaults | rebuild from zero | keep chosen parameters |
| stale summaries | next session misled | refresh after major change |

## Trigger Policy

- summarize at session end when material decisions occurred
- summarize immediately if context pressure threatens continuity
- skip summary if session produced no durable signal
- roll prior summaries forward when they remain accurate
- replace, do not endlessly append, once the core state is stable

## Retrieval Role

Summaries are for fast bootstrap.
They should be indexed, but ranked below source artifacts when deep detail is needed.
Their value is orientation, not authority.
When a summary conflicts with a source artifact, the source artifact wins.

## Recommended Template

- `decisions:` one-line bullets
- `failures:` cause plus correction
- `defaults:` chosen chunk size, top_k, backend, provider family
- `risks:` active uncertainties
- `next:` concrete next step

This structure is simple enough to regenerate and dense enough to reuse.

## Synchronization Rules

When the summary changes materially:
- refresh runtime state defaults if needed
- review entity memory for stale tool facts
- ensure knowledge index reflects new chosen infrastructure
- retire older summaries that no longer add signal

## Quality Standard

- compressed but not vague
- terse but still causal
- under budget without losing decisions
- readable by both humans and retrievers
- capable of starting the next N03 session with confidence

## Final Position

N03 memory summaries should be lossy, structured, and ruthless about preserving only build-relevant signal.
A proud summary is small because it is selective, not because it is thin.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_summary]] | related | 0.37 |
| [[p10_memory_summary]] | sibling | 0.34 |
| [[bld_collaboration_memory_summary]] | downstream | 0.32 |
| [[memory-summary-builder]] | related | 0.31 |
| [[p10_lr_memory_summary_builder]] | related | 0.25 |
| [[bld_examples_memory_summary]] | upstream | 0.25 |
| [[bld_config_memory_summary]] | upstream | 0.23 |
| [[bld_instruction_memory_summary]] | upstream | 0.22 |
| [[p03_sp_memory_summary_builder]] | related | 0.21 |
| [[bld_knowledge_card_memory_summary]] | upstream | 0.21 |
