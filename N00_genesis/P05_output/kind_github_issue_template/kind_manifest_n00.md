---
id: n00_github_issue_template_manifest
kind: knowledge_card
8f: F3_inject
pillar: P05
nucleus: n00
title: "Github Issue Template -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, github_issue_template, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_github_issue_template
  - github-issue-template-builder
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_contributor_guide
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_repo_map
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
GitHub issue template produces structured YAML-based issue forms for GitHub repositories covering the three standard types: bug report, feature request, and question/discussion. Each template enforces required fields, sets default labels, and guides reporters toward providing actionable information that reduces triage time.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `github_issue_template` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Repository name + template type |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| template_type | enum | yes | bug / feature / question / all |
| repo_path | string | yes | Target .github/ISSUE_TEMPLATE/ path |
| required_fields | list | yes | Fields reporters must fill |
| default_labels | list | no | Auto-applied GitHub labels |
| assignees | list | no | Default assignees for triage |

## When to use
- Setting up issue tracking for a new GitHub repository
- Standardizing bug reports to include reproduction steps and environment info
- Reducing noise from incomplete or off-topic issue submissions

## Builder
`archetypes/builders/github_issue_template-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind github_issue_template --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations manages repo governance artifacts
- `{{SIN_LENS}}` -- Gating Wrath: enforce quality at the point of intake
- `{{TARGET_AUDIENCE}}` -- external contributors and internal team filing issues
- `{{DOMAIN_CONTEXT}}` -- project type, triage workflow, labeling taxonomy

## Example (minimal)
```yaml
---
id: github_issue_template_cex_bug
kind: github_issue_template
pillar: P05
nucleus: n05
title: "CEX -- Bug Report Template"
version: 1.0
quality: null
---
template_type: bug
default_labels: [bug, needs-triage]
required_fields: [reproduction_steps, expected_behavior, actual_behavior, environment]
```

## Related kinds
- `contributor_guide` (P05) -- references issue templates in the PR/issue workflow
- `code_of_conduct` (P05) -- governs behavior in issue discussions
- `validation_schema` (P06) -- schema that could validate issue form field values

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_github_issue_template]] | downstream | 0.61 |
| [[github-issue-template-builder]] | related | 0.48 |
| [[bld_schema_integration_guide]] | downstream | 0.41 |
| [[bld_schema_reranker_config]] | downstream | 0.40 |
| [[bld_schema_usage_report]] | downstream | 0.40 |
| [[bld_schema_quickstart_guide]] | downstream | 0.39 |
| [[bld_schema_contributor_guide]] | downstream | 0.39 |
| [[bld_schema_pitch_deck]] | downstream | 0.39 |
| [[bld_schema_benchmark_suite]] | downstream | 0.38 |
| [[bld_schema_repo_map]] | downstream | 0.38 |
