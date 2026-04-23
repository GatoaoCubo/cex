---
kind: output_template
id: bld_output_template_changelog
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for changelog production
quality: 9.0
title: "Output Template Changelog"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, output_template]
tldr: "Keep a Changelog format template for changelog artifact production"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_changelog
  - bld_knowledge_card_changelog
  - bld_schema_changelog
  - bld_examples_changelog
  - kc_changelog
  - changelog-builder
  - p03_sp_changelog_builder
  - p01_qg_changelog
  - p10_mem_changelog_builder
  - p04_ct_bump_version
---

```yaml
---
id: p01_ch_{{slug}}.md
kind: changelog
pillar: P01
title: "{{product_name}} Changelog"
version: "{{semver}}"
release_date: "{{YYYY-MM-DD}}"
author: "{{maintainer_name}}"
domain: "{{product_domain}}"
quality: null
tags: [{{tag1}}, {{tag2}}]
tldr: "{{one_sentence_summary_of_changes}}"
---
```

<!-- slug: lowercase, underscores (e.g., myapp_v2_1_0) -->
<!-- semver: MAJOR.MINOR.PATCH per semver.org (no leading v) -->
<!-- release_date: ISO 8601 YYYY-MM-DD -->

## [Unreleased]
<!-- In-progress changes not yet versioned -->

## [{{semver}}] - {{YYYY-MM-DD}}

### Added
- {{added_entry_1}} (#{{issue_or_pr_id}})
- {{added_entry_2}}

<!-- Added: new capabilities, endpoints, fields, or behaviors -->

### Changed
- {{changed_entry_1}} (#{{issue_or_pr_id}})

<!-- Changed: modifications to existing behavior, not new features -->

### Deprecated
- {{deprecated_entry_1}} -- removal scheduled for {{target_version}}

<!-- Deprecated: features still present but slated for removal -->

### Removed
- BREAKING: {{removed_entry_1}} -- migrate using {{migration_guide_link}}

<!-- Removed: features deleted in this release -->

### Fixed
- {{fixed_entry_1}} (fixes #{{issue_id}})
- {{fixed_entry_2}}

<!-- Fixed: bug fixes, regression patches -->

### Security
- {{security_entry_1}} (CVE-{{cve_id}}, affects {{versions_range}})

<!-- Security: vulnerability patches; always include CVE ID if available -->

## Migration Guide (MAJOR versions only)

**From {{prev_major}}.x to {{semver}}:**
1. {{migration_step_1}}
2. {{migration_step_2}}
3. Verify with: `{{verification_command}}`

## [{{prev_semver}}] - {{prev_date}}
<!-- Previous release entries follow same structure -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_changelog]] | upstream | 0.49 |
| [[bld_knowledge_card_changelog]] | upstream | 0.46 |
| [[bld_schema_changelog]] | downstream | 0.45 |
| [[bld_examples_changelog]] | downstream | 0.44 |
| [[kc_changelog]] | upstream | 0.42 |
| [[changelog-builder]] | upstream | 0.34 |
| [[p03_sp_changelog_builder]] | upstream | 0.33 |
| [[p01_qg_changelog]] | downstream | 0.32 |
| [[p10_mem_changelog_builder]] | downstream | 0.27 |
| [[p04_ct_bump_version]] | upstream | 0.19 |
