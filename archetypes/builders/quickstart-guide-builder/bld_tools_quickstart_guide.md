---
kind: tools
id: bld_tools_quickstart_guide
pillar: P04
llm_function: CALL
purpose: Tools available for quickstart_guide production
quality: 8.9
title: "Tools Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, tools]
tldr: "Tools available for quickstart_guide production"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles guide ISOs into deployable artifact | Initial build |
| cex_score.py | Scores guide quality via 3-layer rubric | Post-creation validation |
| cex_retriever.py | Fetches related guides and examples via TF-IDF | During content integration |
| cex_doctor.py | Diagnoses structure and frontmatter issues | Debugging phase |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Validates frontmatter, ISO count, kind fields | Pre-commit |
| cex_hooks.py | Pre/post build validation hooks | On build events |
| cex_system_test.py | Full system validation (54 checks) | Release gate |

## External References
- Diataxis framework (Tutorial / How-To / Reference / Explanation quadrants)
- Write the Docs (developer documentation standards)
- OpenAPI Specification (api_reference cross-reference)
