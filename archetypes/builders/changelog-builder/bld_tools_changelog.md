---
kind: tools
id: bld_tools_changelog
pillar: P04
llm_function: CALL
purpose: Tools available for changelog production
quality: 8.9
title: "Tools Changelog"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, tools]
tldr: "CEX tools available for changelog production and validation"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml sidecar | After write |
| cex_score.py | Score changelog artifact against quality gate | Pre-publish |
| cex_retriever.py | Find similar changelogs for cross-reference | During research |
| cex_doctor.py | Validate frontmatter, kind, ID pattern compliance | Pre-publish |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Check all builder ISOs for schema compliance | Post-build |
| cex_hooks.py | Pre-commit YAML validation and quality gate | On git commit |

## External References
- keepachangelog.com (format specification)
- semver.org (version numbering specification)
- Git log (source of commit entries for changelog generation)
- GitHub Releases API (structured versioned release format)
