---
id: "p11_lc_{{RULE_SLUG}}"
kind: lifecycle_rule
pillar: P11
version: 1.0.0
title: Template - Lifecycle Rule
tags: [template, lifecycle, rule, retention, cleanup]
tldr: When artifacts are created, updated, archived, deleted. Controls retention and versioning.
quality: 8.6
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
