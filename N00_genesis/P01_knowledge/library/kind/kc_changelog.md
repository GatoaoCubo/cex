---
id: kc_changelog
kind: knowledge_card
8f: F3_inject
title: Changelog Entry
version: 1.0.0
quality: 8.7
pillar: P01
tldr: "Versioned record of product changes using SemVer with features, fixes, and breaking changes sections"
when_to_use: "When tracking release history and communicating changes to users or downstream consumers"
density_score: 1.0
related:
  - bld_knowledge_card_changelog
  - changelog-builder
  - bld_output_template_changelog
  - bld_instruction_changelog
  - bld_examples_changelog
  - p10_mem_changelog_builder
  - p03_sp_changelog_builder
  - p01_qg_changelog
  - bld_schema_changelog
  - p04_ct_bump_version
---

# Changelog Entry

A changelog documents changes to a product using semantic versioning (SemVer). It should include:

## Semantic Versioning
Use `MAJOR.MINOR.PATCH` format:
- **MAJOR**: Breaking changes (e.g., 2.0.0)
- **MINOR**: New features (e.g., 1.1.0)
- **PATCH**: Bug fixes (e.g., 1.0.1)

## Entry Structure
```markdown
## [1.2.0] - 2023-10-15
### Features
- Added dark mode support
- Improved search algorithm

### Fixes
- Fixed login timeout issue
- Resolved CSS layout bug

### Breaking Changes
- Removed deprecated API endpoints
- Changed configuration format to JSON
```

## Best Practices
1. Use clear, concise language
2. Include release dates
3. Highlight security updates
4. Mention compatibility requirements
5. Keep entries ordered by date

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_changelog]] | sibling | 0.43 |
| [[changelog-builder]] | related | 0.42 |
| [[bld_output_template_changelog]] | downstream | 0.41 |
| [[bld_instruction_changelog]] | downstream | 0.40 |
| [[bld_examples_changelog]] | downstream | 0.37 |
| [[p10_mem_changelog_builder]] | downstream | 0.35 |
| [[p03_sp_changelog_builder]] | downstream | 0.33 |
| [[p01_qg_changelog]] | downstream | 0.30 |
| [[bld_schema_changelog]] | downstream | 0.30 |
| [[p04_ct_bump_version]] | downstream | 0.29 |
