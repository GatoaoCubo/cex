---
kind: tools
id: bld_tools_github_issue_template
pillar: P04
llm_function: CALL
purpose: Tools available for github_issue_template production
quality: 8.9
title: "Tools Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, tools]
tldr: "Tools available for github_issue_template production"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool                   | Purpose                               | When                          |
|------------------------|---------------------------------------|-------------------------------|
| cex_compile.py         | Compile .md builder ISOs to .yaml     | After each ISO write          |
| cex_score.py           | Score artifact quality (5D + H gates) | Post-validation assessment    |
| cex_retriever.py       | TF-IDF similarity search on artifacts | When finding similar templates|
| cex_doctor.py          | Builder health check (118 assertions) | Pre-deployment checks         |
| cex_wave_validator.py  | Validate all ISOs in a builder dir    | After completing all 13 ISOs  |
| cex_hygiene.py         | Artifact CRUD + 8 hygiene rules       | Cleanup and consistency pass  |

## Validation Tools
| Tool                  | Purpose                               | When                          |
|-----------------------|---------------------------------------|-------------------------------|
| cex_hooks.py          | Pre-commit validation + ASCII check   | On git commit                 |
| cex_sanitize.py       | Detect and fix non-ASCII in code      | Before committing .py/.ps1    |
| cex_schema_hydrate.py | Hydrate ISOs with universal patterns  | After schema changes          |

## External References
- GitHub Issue Forms documentation: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests
- YAML 1.2 spec (frontmatter validation)
- .github/ISSUE_TEMPLATE/ directory conventions
