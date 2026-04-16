---
kind: config
id: bld_config_nucleus_def
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for nucleus_def production
quality: 8.9
title: "Config Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, config]
tldr: "Naming, paths, limits for nucleus_def production"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p02_nd_{{nucleus_id_lower}}.md`
Examples: `p02_nd_n01.md`, `p02_nd_n05.md`, `p02_nd_n07.md`
Regex: `^p02_nd_n0[0-7]\.md$`

## Paths
Artifacts stored in: `P02_model/instances/p02_nd_{{nucleus_id_lower}}.md`
Builder ISOs: `archetypes/builders/nucleus-def-builder/`
Knowledge card: `P01_knowledge/library/kind/kc_nucleus_def.md`

## Limits
max_bytes: 5120
max_turns: 5
effort_level: 3

## Instance Set
| Artifact | Nucleus | Path |
|----------|---------|------|
| p02_nd_n00.md | N00 Genesis | P02_model/instances/ |
| p02_nd_n01.md | N01 Intelligence | P02_model/instances/ |
| p02_nd_n02.md | N02 Marketing | P02_model/instances/ |
| p02_nd_n03.md | N03 Builder | P02_model/instances/ |
| p02_nd_n04.md | N04 Knowledge | P02_model/instances/ |
| p02_nd_n05.md | N05 Operations | P02_model/instances/ |
| p02_nd_n06.md | N06 Commercial | P02_model/instances/ |
| p02_nd_n07.md | N07 Orchestrator | P02_model/instances/ |

## Hooks
pre_build: validate nucleus_id is in [N00..N07]
post_build: python _tools/cex_compile.py {path}
on_error: report missing source file (nucleus_models.yaml, agent_card, rule file)
on_quality_fail: re-verify pillars_owned against actual artifact production
