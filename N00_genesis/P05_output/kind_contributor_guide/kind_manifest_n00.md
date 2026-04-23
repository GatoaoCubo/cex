---
id: n00_contributor_guide_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Contributor Guide -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, contributor_guide, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_contributor_guide
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_app_directory_entry
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Contributor guide produces an OSS CONTRIBUTING.md specification that covers the full contributor lifecycle: environment setup, coding standards, PR workflow, testing requirements, review process, and maintainer decision authority. It reduces onboarding friction and ensures consistent contribution quality across the project.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `contributor_guide` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Project name + "Contributing Guide" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| setup_steps | list | yes | Numbered environment setup instructions |
| coding_standards | string | yes | Style guide reference or inline rules |
| pr_requirements | list | yes | Checklist for pull request acceptance |
| review_process | string | yes | How PRs are reviewed and merged |
| maintainer_contact | string | yes | How to reach maintainers for questions |

## When to use
- Setting up a new open-source repository that expects external contributions
- Onboarding a new engineering team to contribution norms
- Updating contribution guidelines after process or toolchain changes

## Builder
`archetypes/builders/contributor_guide-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind contributor_guide --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N04 knowledge or N05 operations manages contributor docs
- `{{SIN_LENS}}` -- Knowledge Gluttony: thorough, unambiguous specification
- `{{TARGET_AUDIENCE}}` -- external contributors and new team members
- `{{DOMAIN_CONTEXT}}` -- language, toolchain, test framework, CI/CD pipeline

## Example (minimal)
```yaml
---
id: contributor_guide_cex_oss
kind: contributor_guide
pillar: P05
nucleus: n04
title: "CEX Platform -- Contributing Guide"
version: 1.0
quality: null
---
setup_steps:
  - "git clone + python -m venv"
  - "pip install -r requirements.txt"
  - "python _tools/cex_doctor.py --quick"
pr_requirements: [tests pass, 8F trace in PR description, quality >= 8.0]
```

## Related kinds
- `code_of_conduct` (P05) -- companion community governance document
- `github_issue_template` (P05) -- enforces contribution process at issue creation
- `quickstart_guide` (P05) -- first-contact doc that links to contributor guide

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_contributor_guide]] | downstream | 0.58 |
| [[bld_schema_integration_guide]] | downstream | 0.50 |
| [[bld_schema_quickstart_guide]] | downstream | 0.47 |
| [[bld_schema_reranker_config]] | downstream | 0.46 |
| [[bld_schema_benchmark_suite]] | downstream | 0.46 |
| [[bld_schema_app_directory_entry]] | downstream | 0.46 |
| [[bld_schema_dataset_card]] | downstream | 0.46 |
| [[bld_schema_pitch_deck]] | downstream | 0.45 |
| [[bld_schema_usage_report]] | downstream | 0.45 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.45 |
