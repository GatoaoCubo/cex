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