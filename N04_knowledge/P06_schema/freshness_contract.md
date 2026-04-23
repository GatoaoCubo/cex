---
id: p06_schema_freshness
kind: schema
pillar: P06
title: "Freshness Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [schema, n04, freshness, staleness, monitoring]
tldr: "Staleness rules: 30/60/90 day thresholds by KC type. Auto-flag, review triggers, deprecation policy."
density_score: 0.92
related:
  - bld_examples_lifecycle_rule
  - p10_out_kc_audit_report
  - bld_knowledge_card_lifecycle_rule
  - p03_ins_lifecycle_rule
  - p11_lc_cex_lifecycle
  - bld_collaboration_lifecycle_rule
  - output_kc_quality_audit_20260408
  - p06_schema_source_quality
  - p03_ch_kc_to_notebooklm
  - p03_sp_lifecycle_rule_builder
---

# Freshness Contract

## Thresholds by KC Type

| KC Type | Fresh | Aging | Stale | Deprecated |
|---------|-------|-------|-------|------------|
| Platform (API, tools) | <30d | 30-60d | 60-90d | >90d |
| Domain (patterns, methods) | <90d | 90-180d | 180-365d | >1y |
| Kind (CEX structural) | <180d | 180-365d | >1y | >2y |
| Infrastructure | <60d | 60-120d | 120-180d | >180d |

## Actions per State

| State | Icon | Action |
|-------|------|--------|
| Fresh | ✅ | No action needed |
| Aging | 🟡 | Schedule review |
| Stale | ⚠️ | Flag in output, prioritize refresh |
| Deprecated | ❌ | Archive, remove from active injection |

## Implementation Guide

| Step | Check | Action |
|------|-------|--------|
| Daily | `git log --since="30 days"` on Platform KCs | Flag aging items |
| Weekly | Scan aging KCs | Queue for expert review |
| Monthly | Run freshness audit | Update stale items or deprecate |

### Edge Cases
- **Breaking changes**: Reset threshold to 0 days regardless of type
- **Seasonal content**: Extend threshold by 50% for annual patterns
- **Legacy systems**: Use Infrastructure thresholds even for Platform KCs

## Freshness Score Formula
```
freshness = max(0, 1 - (days_since_update / threshold_stale))
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_lifecycle_rule]] | related | 0.26 |
| [[p10_out_kc_audit_report]] | downstream | 0.25 |
| [[bld_knowledge_card_lifecycle_rule]] | downstream | 0.19 |
| [[p03_ins_lifecycle_rule]] | upstream | 0.18 |
| [[p11_lc_cex_lifecycle]] | downstream | 0.18 |
| [[bld_collaboration_lifecycle_rule]] | downstream | 0.18 |
| [[output_kc_quality_audit_20260408]] | upstream | 0.18 |
| [[p06_schema_source_quality]] | sibling | 0.17 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.17 |
| [[p03_sp_lifecycle_rule_builder]] | upstream | 0.17 |
