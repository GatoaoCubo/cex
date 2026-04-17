---
kind: learning_record
id: p10_lr_nucleus_def_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for nucleus_def construction
quality: 8.9
title: "Learning Record Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, learning_record]
tldr: "Learned patterns and pitfalls for nucleus_def construction"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation
The CEX architecture has 8 nuclei (N00-N07) but lacked a formal machine-readable
contract for each. Dispatch logic was hardcoded in spawn scripts. Routing decisions
relied on implicit knowledge. nucleus_def was created to make this explicit.

## Pattern
Effective nucleus_def artifacts extract ground truth from 4 sources:
1. nucleus_models.yaml (cli_binding, model_tier, fallback_chain)
2. .claude/rules/n0{X}-*.md (role, sin_lens, routing rules)
3. N0{X}_*/agent_card_n0{X}.md (domain_agents, kinds_owned)
4. N00_genesis/README.md (fractal structure, pillar map)

Never guess these values -- always read the source files first.

## Evidence
- N03 uses opus (not sonnet) because it runs the 8F build pipeline which requires
  deep reasoning. Guessing "sonnet" for N03 would cause dispatch failures.
- N05 pillars_owned is [P07, P08, P09, P11] -- not all 12. Claiming all pillars
  caused routing confusion where N07 sent RAG tasks to N05 instead of N04.
- The boot_script field prevented a dispatch failure when N07 could not find
  the correct boot path for a newly registered nucleus.

## Recommendations
- Always read nucleus_models.yaml before setting cli_binding or model_tier.
- Verify pillars_owned by scanning N0{X}_*/P05_output/ for actual artifact kinds.
- List domain_agents by running: `ls N0{X}_*/agents/*.md` and reading agent IDs.
- Keep crew_templates_exposed lean (2-5 templates) -- overly broad lists mislead N07.
- After writing nucleus_def, run cex_doctor.py to verify the boot_script path exists.
- Update nucleus_def whenever a nucleus changes model (e.g., opus->sonnet migrations).
