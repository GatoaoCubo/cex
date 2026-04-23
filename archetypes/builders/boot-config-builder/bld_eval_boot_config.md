---
kind: quality_gate
id: p11_qg_boot_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of boot_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: boot_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, boot-config, P11, P02, governance, initialization, provider]
tldr: "Gates for boot_config artifacts — provider-specific agent initialization parameters and constraints."
domain: boot_config
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.88
related:
  - bld_examples_boot_config
  - boot-config-builder
  - bld_instruction_boot_config
  - p03_sp_boot_config_builder
  - bld_knowledge_card_boot_config
  - p11_qg_agent
  - bld_collaboration_boot_config
  - p01_kc_boot_config
  - bld_schema_boot_config
  - p10_lr_boot-config-builder
---

## Quality Gate

# Gate: boot_config
## Definition
| Field     | Value                                                  |
|-----------|--------------------------------------------------------|
| metric    | provider completeness + constraint rationalization     |
| threshold | 8.0                                                    |
| operator  | >=                                                     |
| scope     | all boot_config artifacts (P02)                        |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = agent fails to boot |
| H02 | id matches `^p02_boot_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Discovery relies on this |
| H04 | kind == "boot_config" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 15 required fields present: id, kind, pillar, version, created, updated, author, provider, identity, constraints, tools, domain, quality, tags, tldr | Completeness |
| H07 | identity object has name, role, agent_group | Identity block completeness |
| H08 | constraints object has max_tokens, context_window, timeout_seconds | Runtime constraints completeness |
| H09 | tools is non-empty list | Agent requires at least one tool to function |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 |
| S02 | tags is list, len >= 3, includes "boot-config" | 0.5 |
| S03 | model field is set to specific model identifier | 0.5 |
| S04 | temperature is float 0.0-2.0 | 0.5 |
| S05 | flags list present and non-empty | 0.5 |
| S06 | mcp_config present when provider supports MCP | 1.0 |
| S07 | body has ## Constraints table with per-field rationale | 1.0 |
| S08 | body has ## Tools Configuration table listing each tool | 1.0 |
| S09 | density_score >= 0.80 | 0.5 |
| S10 | No filler phrases or generic descriptions | 1.0 |
Weights sum: 7.5. Normalize: divide each by 7.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference config for this provider |
| >= 8.0 | PUBLISH — active boot configuration |
| >= 7.0 | REVIEW — rationalize constraints or complete tools list |
| < 7.0  | REJECT — identity block or constraints block incomplete |
## Bypass
| Field | Value |
|-------|-------|
| conditions | New provider integration requiring immediate bootstrap before full spec |
| approver | p02-chief |
| audit_trail | Log in records/audits/ with provider justification and timestamp |
| expiry | 48h — complete constraints spec required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

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
  agent_group: "agnostic"
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
quality: 8.9
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
Agent_group: agnostic (cross-agent_group utility)
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
