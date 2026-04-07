---
kind: examples
id: bld_examples_agent_card
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of agent_card artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Agent Card"
version: "1.0.0"
author: n03_builder
tags: [agent_card, builder, examples]
tldr: "Golden and anti-examples for agent card construction, demonstrating ideal structure and common pitfalls."
domain: "agent card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: agent-card-builder
## Golden Example
INPUT: "Especifica o agent_group researcher for research de mercado"
OUTPUT:
```yaml
id: p08_ac_shaka
kind: agent_card
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
name: "researcher"
role: "Research agent_group — market intelligence, competitor analysis, web scraping"
model: "sonnet"
mcps: [firecrawl, brain]
domain_area: "research"
boot_sequence:
  - "Load prime_researcher.md"
  - "Initialize firecrawl MCP"
  - "Initialize brain MCP"
  - "Check dispatch queue"
constraints:
  - "Read-only: never modify production data"
  - "Max 10 credits per research session (firecrawl budget)"
  - "No code generation — delegate to builder"
  - "Results must include source URLs"
dispatch_keywords: [researchr, market, competitor, scrape, analysis, research]
tools: [firecrawl_scrape, firecrawl_extract, brain_query, web_search]
dependencies: [brain_mcp, firecrawl_api]
scaling:
  max_concurrent: 1
  timeout_minutes: 30
  memory_limit_mb: 2048
monitoring:
  health_check: "brain_query('shaka status')"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-shaka.json"
flags: ["--no-chrome", "-p"]
domain: "research-intelligence"
quality: null
tags: [agent_group, research, shaka, market-intelligence, scraping]
tldr: "researcher agent_group spec — research domain, sonnet model, firecrawl+brain MCPs, market intelligence."
```
## Role
Research agent_group focused on market intelligence, competitor analysis, and web data extraction.
Primary function: gather, structure, and deliver research findings as knowledge cards or reports.
Does not generate code or modify production systems.
## Model & MCPs
- **Model**: sonnet (balanced cost/quality for research tasks)
- **firecrawl**: web scraping and structured data extraction (3000 credits/month)
- **brain**: knowledge search and deduplication check
## Boot Sequence
1. Load prime_researcher.md (identity, constraints, dispatch protocol)
2. Initialize firecrawl MCP (verify API key, check credit balance)
3. Initialize brain MCP (verify Ollama running, index freshness)
4. Check dispatch queue (.claude/handoffs/shaka_*.md)
## Dispatch
Keywords: researchr, market, competitor, scrape, analysis, research
Routing: orchestrator matches keywords against dispatch_keywords list.
Priority: research tasks routed to researcher before any other agent_group.
## Constraints
- Read-only: never modify production data or commit to main
- Budget: max 10 firecrawl credits per research session
- Boundary: no code generation (delegate to builder)
- Quality: all findings must include source URLs
## Dependencies
- brain MCP server (Ollama + FAISS index)
- firecrawl API ($19/month tier)
- No sibling agent_group dependencies (fully independent)
## Scaling & Monitoring
- Max 1 concurrent instance (avoid firecrawl rate limits)
- 30-minute timeout per session
- Signal on complete: emits p12_sig_shaka_complete.json
- Alert on failure: logs error + notifies orchestrator
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p08_ac_ pattern (H02 pass)
- kind: agent_card (H04 pass)
- 26 frontmatter fields present (H06 pass)
- name non-empty "researcher" (H07 pass)
- model is valid "sonnet" (H08 pass)
- mcps is list (H09 pass)
- role non-empty (H10 pass)
- YAML parses cleanly (H01 pass)
- id == filename stem (H03 pass)
- tldr <= 160 chars (S01 pass)
- tags list len >= 3 (S02 pass)
- All 7 body sections present (S03-S09 pass)
## Anti-Example
INPUT: "Define researcher agent_group"
BAD OUTPUT:
```yaml
id: shaka_agent_group
kind: agent_group
pillar: Architecture
name: Shaka
model: Claude Sonnet 4
mcps: firecrawl
role: This agent_group is responsible for doing various types of research including market research, competitor analysis, web scraping, and many other research-related activities
quality: 9.0

## Golden Example 2 (Production — OpenClaude Verification Agent Card)
INPUT: "Create agent card for adversarial verification agent"
OUTPUT: Reference artifact `P08_architecture/compiled/p08_ac_verification.yaml`

Key patterns:
1. **Tool allowlist/denylist**: Explicit `allowed` and `disallowed` tool lists.
   Not "has access to tools" but "exactly these tools, and explicitly NOT these."
2. **background: true**: Agent runs independently from the calling agent.
3. **model: inherit**: Uses the calling nucleus's model, not a fixed one.
4. **omit_project_rules: true**: Verification agent interprets results independently;
   loading project-specific rules would bias it toward the implementer's assumptions.
5. **input/output contract**: Typed input (task_description, files_changed, approach, plan_path)
   and typed output (VERDICT enum with structured check reports).
6. **dispatch command**: Exact CLI invocation to spawn this agent.

WHY THIS IS GOLDEN:
- Explicit allowed/disallowed tools (not vague "read-only")
- background flag enables concurrent execution
- Input/output contracts are typed, not prose
- Dispatch command is copy-pasteable

## Golden Example 3 (Production — OpenClaude Explore Agent Card)
INPUT: "Create agent card for fast codebase exploration agent"
OUTPUT: Reference artifact `P08_architecture/compiled/p08_ac_explore.yaml`

Key patterns:
1. **model: haiku** (not inherit): Explore is optimized for speed, not depth.
   Uses the cheapest/fastest model available. Different from Plan (inherit for depth).
2. **thoroughness_levels**: [quick, medium, very_thorough]. Caller specifies desired depth.
3. **when_not_to_use**: "Simple directed search (use grep directly)."
   Prevents over-engineering simple lookups with a full agent dispatch.

## Anti-Example 2 (Bad — No tool restrictions)
```yaml
agent_type: reviewer
tools: all
model: opus
```
FAIL: No tool denylist. A reviewer agent with write access can modify what it's reviewing.
Compare to p08_ac_verification which explicitly denies edit/write/spawn/git-write tools.
