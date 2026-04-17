---
id: n00_changelog_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Changelog -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, changelog, p01, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Changelog is a structured product changelog entry following semantic versioning conventions. It documents features added, bugs fixed, and breaking changes introduced in each release. It produces a machine-readable and human-readable record that feeds into release notes, migration guides, and stakeholder communications.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `changelog` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Release version + codename |
| version | semver | yes | Artifact version (matches release version) |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| release_date | date | yes | ISO 8601 release date |
| added | list | no | New features introduced |
| fixed | list | no | Bugs resolved |
| changed | list | no | Modified behavior (non-breaking) |
| deprecated | list | no | Features marked for removal |
| breaking | list | no | Breaking changes requiring migration |

## When to use
- When releasing a new version of a product, SDK, or tool
- When communicating changes to downstream consumers or stakeholders
- When maintaining an auditable history of system evolution

## Builder
`archetypes/builders/changelog-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind changelog --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (typically N05 or N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- developers, end users, or internal teams
- `{{DOMAIN_CONTEXT}}` -- product or service being versioned

## Example (minimal)
```yaml
---
id: changelog_cex_sdk_v2_1_0
kind: changelog
pillar: P01
nucleus: n05
title: "cex_sdk v2.1.0 -- Signal Watch"
version: 2.1.0
quality: null
release_date: 2026-04-17
---
## Added
- cex_signal_watch.py: blocking poll for nucleus completion
## Fixed
- dispatch.sh stop: session-aware kill now handles orphaned workers
```

## Related kinds
- `knowledge_card` (P01) -- atomic facts that feed into release documentation
- `software_project` (P02) -- the project this changelog belongs to
- `dataset_card` (P01) -- structured documentation for data releases
