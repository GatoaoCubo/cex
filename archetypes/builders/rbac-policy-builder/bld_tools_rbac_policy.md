---
kind: tools
id: bld_tools_rbac_policy
pillar: P04
llm_function: CALL
purpose: Tools available for rbac_policy production
quality: 8.9
title: "Tools Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, tools]
tldr: "Tools available for rbac_policy production"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile artifact .md to .yaml | After save |
| cex_score.py --apply | Peer review scoring (D1-D5 weighted) | Before publish |
| cex_doctor.py | Builder health check (validates all 13 ISOs) | Post-build |
| cex_hygiene.py | Artifact CRUD + 8-rule enforcement | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Validates frontmatter + kind/pillar/llm_function | CI gate |
| cex_hooks.py pre-commit | ASCII enforcement + schema check | Pre-commit |
| cex_retriever.py | TF-IDF similarity search (find similar artifacts) | F3 INJECT |

## External References
- OPA (Open Policy Agent) -- rego rule enforcement for RBAC policies
- Casbin -- RBAC model library (Node, Go, Python)
- NIST SP 800-162 -- attribute-based access control standard
