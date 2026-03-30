---
kind: examples
id: bld_examples_boot_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of boot_config artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: boot-config-builder
## Golden Example
INPUT: "Create boot config for a research agent on Claude Code provider"
OUTPUT:
```yaml
id: p02_boot_claude_code_research
kind: boot_config
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
provider: "claude_code"
identity:
  name: "Research Agent"
  role: "Deep web research and knowledge extraction"
  agent_node: "agnostic"
constraints:
  max_tokens: 16384
  context_window: 200000
  timeout_seconds: 300
  max_retries: 2
  temperature: 0.3
tools: [brain_query, web_search, web_fetch, read, grep, glob]
model: "claude-sonnet-4-6"
temperature: 0.3
flags: [--no-chrome, --strict-mcp-config]
mcp_config:
  brain: stdio
  firecrawl: stdio
permissions:
  read: [records/, archetypes/]
  write: [records/pool/]
  execute: [python, git]
system_prompt_ref: "p03_sp_research_agent"
domain: "research"
quality: null
tags: [boot-config, research, claude-code, P02]
tldr: "Claude Code boot config for research agent with brain+firecrawl MCPs and 200K context"
density_score: 0.89
```
## Provider Overview
Claude Code CLI runtime for research-focused agents.
Supports MCP servers, 200K context window, file system access.
## Identity Block
Name: Research Agent
Role: Deep web research and knowledge extraction
Satellite: agnostic (cross-agent_node utility)
## Constraints
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| max_tokens | 16384 | Research outputs need extended generation |
| context_window | 200000 | Claude Sonnet 4.6 full context |
| timeout_seconds | 300 | Web research may take 3-5 minutes |
| max_retries | 2 | Retry transient web fetch failures |
## Tools Configuration
| Tool | Type | Purpose |
|------|------|---------|
| brain_query | mcp | Search existing knowledge in pool |
| web_search | mcp | Discover relevant URLs |
| web_fetch | mcp | Extract content from URLs |
| read | cli | Read local files |
| grep | cli | Search file contents |
| glob | cli | Find files by pattern |
## Flags
| Flag | Purpose |
|------|---------|
| --no-chrome | No browser needed for CLI research |
| --strict-mcp-config | Only use declared MCP servers |
## References
- Provider docs: claude --help
- Related config: p02_boot_claude_code_builder
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_boot_ pattern (H02 pass) | kind: boot_config (H04 pass)
- 22 fields in frontmatter (H06 pass) | identity complete (H07 pass)
- constraints complete with max_tokens, context_window, timeout_seconds (H08 pass)
- tools: 6 items non-empty (H09 pass) | model set (S03 pass) | temperature 0.3 (S04 pass)
- flags present (S05 pass) | mcp_config present (S06 pass) | Constraints table (S07 pass)
- Tools table (S08 pass) | density 0.89 (S09 pass) | no filler (S10 pass)
## Anti-Example
INPUT: "Make a config for my agent"
BAD OUTPUT:
```yaml
id: my_agent_config
kind: config
provider: AI
tools: []
quality: 7.5
tags: [config]
tldr: "This configuration file sets up the necessary parameters for the agent to work properly in the system."
```
Set up the agent with default settings and make sure everything works fine.
FAILURES:
1. id: no `p02_boot_` prefix -> H02 FAIL
2. kind: "config" not "boot_config" -> H04 FAIL
3. quality: 7.5 (not null) -> H05 FAIL
4. Missing 11 required fields (pillar, version, created, updated, author, identity, constraints, domain, quality as null, tags proper, tldr proper) -> H06 FAIL
5. identity object missing entirely -> H07 FAIL
6. constraints object missing entirely -> H08 FAIL
7. tools: empty list -> H09 FAIL
8. tags: only 1 item, missing "boot-config" -> S02 FAIL
9. provider: "AI" is not a valid provider name -> S03 FAIL
10. tldr: filler phrase "This configuration file sets up the necessary parameters" -> S01+S10 FAIL
11. No Constraints table in body -> S07 FAIL
12. No Tools Configuration table in body -> S08 FAIL
