---
id: "p11_lc_{{RULE_SLUG}}"
kind: lifecycle_rule
pillar: P11
version: 1.0.0
title: Template - Lifecycle Rule
tags: [template, lifecycle, rule, retention, cleanup]
tldr: When artifacts are created, updated, archived, deleted. Controls retention and versioning.
quality: 9.0
updated: "2026-04-07"
domain: "feedback and quality"
author: n03_builder
created: "2026-04-07"
density_score: 0.96
---

# Lifecycle Rule: [NAME]

## Purpose
[WHAT this lifecycle_rule does]
## Stages
| Stage | Trigger | Action |
|-------|---------|--------|
| Create | F8 complete | Save .md + compile |
| Update | Re-run 8F | Overwrite + version bump |
| Review | Peer score | Set quality |
| Archive | Unused > N days | Move to archive |
| Delete | Manual/policy | Remove + log |
## Retention
| Type | Active | Archive | Delete |
|------|--------|---------|--------|
| Builders | Forever | Never | Never |
| KCs | Forever | Never | On deprecation |
| Runtime state | 24h | 7d | After 7d |
| Learning records | 90d | 1y | After 1y |
| Signals | 24h | -- | After 24h |
## Versioning
- **Major**: Breaking schema change
- **Minor**: Content enrichment
- **Patch**: Typo fixes
## Quality Gate
- [ ] Every type has retention period
- [ ] Archive before delete
- [ ] Semver versioning
- [ ] Cleanup automated

## Cross-References

- **Pillar**: P11 (Feedback)
- **Kind**: `lifecycle rule`
- **Artifact ID**: `p11_lc_{{RULE_SLUG}}`
- **Tags**: [template, lifecycle, rule, retention, cleanup]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P11 | Feedback domain |
| Kind `lifecycle rule` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: lifecycle_rule
pillar: P11
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```
