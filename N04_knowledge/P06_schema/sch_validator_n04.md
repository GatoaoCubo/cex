---
id: sch_validator_n04
kind: validator
pillar: P06
nucleus: n04
title: Knowledge Intake Validator
version: 1.0
quality: 8.7
tags: [schema, validator, knowledge, provenance, quality]
density_score: 1.0
related:
  - p01_kc_validator
  - bld_examples_validator
  - agent_card_n04
  - self_audit_n04_codex_2026_04_15
  - validator-builder
  - bld_collaboration_knowledge_card
  - n04_knowledge
  - n04_dr_knowledge
  - bld_knowledge_card_validator
  - p08_kc_capability_registry
---
<!-- 8F: F1 constrain=P06/validator F2 become=validator-builder F3 inject=n04-knowledge+kc_validator+P06 examples+N04 schema goals F4 reason=atomic pass-fail rule for provenance and freshness completeness F5 call=shell,apply_patch F6 produce=4841 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/P06_schema/sch_validator_n04.md -->
# Knowledge Intake Validator
## Purpose
This validator blocks thin, source-poor knowledge from entering N04 as if it were trustworthy.
The Knowledge Gluttony lens does not mean accepting everything; it means collecting aggressively and then governing the collection with hard binary checks.
This rule targets the intake payload and fails artifacts that lack enough evidence density to deserve indexing.
## Schema
```yaml
validator_id: n04_knowledge_intake_guard
target: N04_knowledge/**/sch_*_n04.md and intake payloads
trigger: pre_commit
rule_type: structural_and_provenance
severity: error
on_fail: block
checks:
  - provenance_min
  - raw_text_min
  - taxonomy_presence
  - freshness_window_valid
```
## Checks
| # | Check | Expression | On Fail |
|---|-------|------------|---------|
| 1 | provenance_min | `len(provenance) >= 1` | reject |
| 2 | raw_text_min | `len(raw_text.strip()) >= 80` | reject |
| 3 | taxonomy_presence | `len(taxonomy_candidates or taxonomy) >= 1` | reject |
| 4 | freshness_window_valid | `review_after_days <= stale_after_days` | reject |
| 5 | forbidden_placeholder | `raw_text not matches /^(todo|tbd|lorem ipsum)$/i` | reject |
| 6 | enum_exactness | `target_signal_state in knowledge_signal_state` | reject |
## Error Messages
| Check | Message | Fix Hint |
|-------|---------|----------|
| provenance_min | `N04 requires at least one provenance record.` | add direct source metadata |
| raw_text_min | `Knowledge payload is too thin for indexing.` | provide substantive text, not summary only |
| taxonomy_presence | `Knowledge payload must carry at least one taxonomy hint.` | add normalized labels |
| freshness_window_valid | `Freshness window is inverted.` | make review threshold earlier than stale threshold |
| forbidden_placeholder | `Placeholder text cannot enter the knowledge index.` | replace stub with real content |
| enum_exactness | `target_signal_state is not canonical.` | map to approved enum value |
## Pass Example
```yaml
artifact_id: kc_embedding_batch_tuning
raw_text: "Batch sizing for embeddings should balance throughput and provider token ceilings..."
taxonomy_candidates: [embeddings, batching, throughput]
target_signal_state: normalized
provenance:
  - source_id: kc_mcp_tool_infrastructure
    source_type: doc
    confidence: 0.91
    observed_at: 2026-04-16
freshness_days: 30
```
Result: PASS
## Fail Example
```yaml
artifact_id: temp
raw_text: "todo"
taxonomy_candidates: []
target_signal_state: done
provenance: []
freshness_days: 30
```
Result: FAIL - provenance_min, raw_text_min, taxonomy_presence, forbidden_placeholder, enum_exactness
## Rationale
| Decision | Knowledge Gluttony expression | Benefit |
|----------|------------------------------|---------|
| block placeholders | N04 wants more facts, not more empty files | keeps index signal-rich |
| require taxonomy | gluttony without labeling is hoarding, not knowledge | retrieval remains navigable |
| require provenance | stored claims must remain traceable | supports audits and conflict resolution |
| use binary failure | this is governance, not scoring | callers know exactly what to fix |
| combine freshness inversion check | time-aware appetite avoids rotten knowledge | stale logic stays coherent |
## Execution Notes
| Aspect | Rule |
|--------|------|
| When | pre-commit and pre-index enqueue |
| Scope | intake payloads and schema-linked examples |
| Auto-fix | none for evidence fields |
| Bypass | only N07-approved emergency import with audit trail |
| Audit log | record validator id, artifact id, failed checks |
## Enforcement Targets
| Target surface | Why it matters |
|----------------|----------------|
| markdown artifacts | prevents weak examples from teaching bad patterns |
| compiled YAML payloads | stops invalid records before storage |
| import scripts | preserves consistency across automated backfills |
## Properties
| Property | Value |
|----------|-------|
| Validator id | `n04_knowledge_intake_guard` |
| Trigger | `pre_commit` |
| Severity | `error` |
| Action on fail | `block` |
| Atomic rule count | 6 |
| Auto-fix | no |
| Primary concern | provenance and evidence sufficiency |
| Secondary concern | freshness coherence |
| Intended owner | N04 knowledge |
| Related enum | `knowledge_signal_state` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_validator]] | related | 0.26 |
| [[bld_examples_validator]] | downstream | 0.26 |
| [[agent_card_n04]] | upstream | 0.25 |
| [[self_audit_n04_codex_2026_04_15]] | downstream | 0.24 |
| [[validator-builder]] | related | 0.23 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.22 |
| [[n04_knowledge]] | upstream | 0.22 |
| [[n04_dr_knowledge]] | related | 0.22 |
| [[bld_knowledge_card_validator]] | upstream | 0.21 |
| [[p08_kc_capability_registry]] | downstream | 0.21 |
