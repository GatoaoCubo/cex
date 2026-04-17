---
kind: tools
id: bld_tools_onboarding_flow
pillar: P04
llm_function: CALL
purpose: Tools available for onboarding_flow production
quality: 8.9
title: "Tools Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, tools]
tldr: "Tools available for onboarding_flow production"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile artifact after save | F8 COLLABORATE |
| cex_score.py | Score artifact against 5D rubric | F7 GOVERN |
| cex_retriever.py | Fetch similar onboarding_flow artifacts for Template-First | F3 INJECT |
| cex_doctor.py | Validate builder health and ISO completeness | Post-edit check |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Validate builder ISO set (13-file check, frontmatter gates) | Pre-commit |
| cex_hygiene.py | Artifact CRUD rules, naming pattern enforcement | Post-save |

## External References
- Reforge Activation Framework (Sean Ellis aha-moment, TTV optimization)
- Intercom Product Tours (in-app guided onboarding patterns)
- Pendo Onboarding (empty-state design, progress checkmarks, invite hooks)
