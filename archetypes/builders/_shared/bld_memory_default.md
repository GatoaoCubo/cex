---
id: bld_memory_default
kind: builder_default
pillar: P10
source: shared
title: "Memory Default: Learning Record Schema"
llm_function: INJECT
version: 1.1.0
quality: 7.8
tags: [memory, learning_record, P10, shared, default]
related:
  - bld_collaboration_memory_type
  - p01_kc_memory_scope
  - p01_kc_memory_persistence
  - bld_collaboration_memory_scope
  - memory-scope-builder
  - ex_learning_record_ad_success
  - bld_manifest_memory_type
  - bld_collaboration_entity_memory
  - bld_examples_memory_scope
  - bld_knowledge_card_memory_scope
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-22"
---

# P10 Memory — Default Learning Record Schema

## What to Persist (F3b PERSIST)

After assembling context (F3), declare what new knowledge should survive:

| Type | When | Target kind |
|------|------|-------------|
| New entity discovered | domain entity not in existing KCs | entity_memory |
| Updated fact | existing KC has stale or wrong data | knowledge_card update |
| Session learning | pattern observed across 3+ builds | learning_record |
| User preference | explicit correction or confirmed approach | feedback memory file |

## Learning Record Schema

```yaml
---
id: lr_{kind}_{date}
kind: learning_record
pillar: P10
nucleus: {nucleus}
domain: {kind}
date: {YYYY-MM-DD}
quality: null
---

## Observation
{What was learned or confirmed}

## Evidence
{2-3 concrete examples from this session}

## Impact
{How this changes future builds of this kind}

## Applied From
{Session date, artifact ID that triggered this learning}
```

## Memory Scope Rules

- **Session memory**: context window only -- do not persist
- **Build memory**: persist if the learning changes HOW to build the kind
- **Error memory**: persist if the error is likely to recur (structural, not one-off)
- **Preference memory**: persist user corrections immediately (use Claude memory system)

## When to Override

Override `bld_memory_{kind}.md` when the kind has domain-specific entity types
or lookup tables (e.g., agent builders track capability registries; schema builders
track field type conventions).

## Hard Gates (H01-H07) -- ALL must pass

| Gate | Check | Fail Action |
|------|-------|-------------|
| H01 | Frontmatter present and valid YAML | Return to F6, add frontmatter |
| H02 | `quality: null` in frontmatter (never self-score) | Remove score, set null |
| H03 | Required fields: id, kind, 8f, pillar, title | Add missing fields |
| H04 | Body density >= 0.85 (content lines / total lines) | Add structured data, remove filler |
| H05 | No hallucinated sources (cited paths must exist) | Remove or verify citations |
| H06 | ASCII-only in any generated code blocks | Replace non-ASCII per cex_sanitize rules |
| H07 | Output matches pillar schema constraints | Restructure to match schema |

## Scoring Dimensions (5D)

| Dimension | Weight | Criteria |
|-----------|--------|---------|
| D1 Structural | 30% | Frontmatter complete, naming correct, file in right pillar dir |
| D2 Content | 25% | Density >= 0.85, no filler, tables preferred over prose |
| D3 Accuracy | 20% | No hallucination, sources verified, constraints respected |
| D4 Usefulness | 15% | Actionable, implementable, unambiguous |
| D5 CEX fit | 10% | Kind/pillar/nucleus alignment, 8F stage correctness |

## Memory Persistence Checklist

- Verify memory type matches taxonomy (entity, episodic, procedural, working)
- Validate retention policy aligns with data lifecycle rules
- Cross-reference with memory_scope for boundary correctness
- Check for stale entries that need decay or pruning

## Memory Pattern

```yaml
# Memory lifecycle
type: classified
retention: defined
scope: bounded
decay: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_memory_update.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_type]] | downstream | 0.36 |
| [[p01_kc_memory_scope]] | upstream | 0.32 |
| [[p01_kc_memory_persistence]] | upstream | 0.30 |
| [[bld_collaboration_memory_scope]] | downstream | 0.30 |
| [[memory-scope-builder]] | upstream | 0.29 |
| [[ex_learning_record_ad_success]] | related | 0.28 |
| [[bld_manifest_memory_type]] | upstream | 0.28 |
| [[bld_collaboration_entity_memory]] | downstream | 0.28 |
| [[bld_examples_memory_scope]] | upstream | 0.26 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.25 |
