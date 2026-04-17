---
kind: tools
id: bld_tools_agents_md
pillar: P04
llm_function: CALL
purpose: Tools available for agents_md production
quality: 8.9
title: "Tools Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, tools]
tldr: "Tools available for AGENTS.md production"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool             | Purpose                                        | When                        |
|------------------|------------------------------------------------|-----------------------------|
| cex_compile.py   | Compile AGENTS.md source to project-root file  | After F6 PRODUCE            |
| cex_score.py     | Assign HARD/SOFT quality score                 | Post-validation phase       |
| cex_retriever.py | Fetch similar AGENTS.md from 60K corpus        | On-demand during F3 INJECT  |
| cex_doctor.py    | Diagnose missing command blocks                | Pre-validation checks       |
| codex            | OpenAI Codex CLI -- reference AAIF consumer    | Dry-run bootstrap test      |
| aider            | Aider coding-agent -- reference AAIF consumer  | Dry-run bootstrap test      |

## Validation Tools
| Tool              | Purpose                                     | When                    |
|-------------------|---------------------------------------------|-------------------------|
| agents_md_lint.py | Check spec conformance (AAIF schema)        | Pre-commit              |
| ci_mirror_check   | Verify command blocks match actual CI YAML  | Pre-publish             |
| vendor_scrub      | Detect Claude/Cursor-only directives leak   | Pre-publish             |
| shell_runnable    | Dry-run every fenced command in fresh shell | Release gate            |

## External References
- AGENTS.md spec: https://agents.md/ (AAIF governance, Dec 2025)
- OpenAI Codex CLI docs: reference parser implementation
- Block goose AGENTS.md guide: adoption patterns from 60K-projects corpus
- Conventional Commits 1.0.0: pr-format grammar source
- MCP (Model Context Protocol): complementary transport spec
