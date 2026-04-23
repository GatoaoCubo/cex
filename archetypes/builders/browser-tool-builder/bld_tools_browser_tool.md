---
kind: tools
id: bld_tools_browser_tool
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for browser_tool production
quality: 9.0
title: "Tools Browser Tool"
version: "1.0.0"
author: n03_builder
tags: [browser_tool, builder, examples]
tldr: "Golden and anti-examples for browser tool construction, demonstrating ideal structure and common pitfalls."
domain: "browser tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_function_def
  - bld_tools_path_config
  - bld_tools_prompt_version
  - bld_tools_output_validator
  - bld_tools_client
  - bld_tools_handoff_protocol
  - bld_tools_runtime_rule
---

# Tools: browser-tool-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing browser_tool artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, browser_tool kind |
| CEX Examples | P04_tools/examples/ | Real browser_tool artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_browser_tool |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Engine Reference
| Engine | Language | Headless | JS | Use Case |
|--------|----------|----------|----|----------|
| playwright | Python/JS/TS | yes | yes | Default: cross-browser, modern sites |
| puppeteer | Node.js | yes | yes | Chrome/Chromium-specific automation |
| selenium | Python/Java/JS | yes | yes | Legacy/enterprise, cross-browser grid |
| browser_use | Python | yes | yes | LLM-driven autonomous navigation |
| browserbase | Python/JS | yes (cloud) | yes | Scalable cloud headless sessions |
| stagehand | TypeScript | yes | yes | AI-assisted, natural language actions |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, actions list matches body,
body <= 2048 bytes, quality == null, engine is recognized, selectors have fallback chain.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_cli_tool]] | sibling | 0.51 |
| [[bld_tools_retriever_config]] | sibling | 0.48 |
| [[bld_tools_memory_scope]] | sibling | 0.48 |
| [[bld_tools_function_def]] | sibling | 0.47 |
| [[bld_tools_path_config]] | sibling | 0.47 |
| [[bld_tools_prompt_version]] | sibling | 0.47 |
| [[bld_tools_output_validator]] | sibling | 0.46 |
| [[bld_tools_client]] | sibling | 0.46 |
| [[bld_tools_handoff_protocol]] | sibling | 0.46 |
| [[bld_tools_runtime_rule]] | sibling | 0.46 |
