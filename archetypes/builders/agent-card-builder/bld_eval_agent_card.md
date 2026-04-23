---
kind: quality_gate
id: p11_qg_agent-card
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of agent_card artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.1
title: 'Gate: Agent_group Spec'
version: 1.0.0
author: builder_agent
tags:
- eval
- P11
- quality_gate
- examples
tldr: Gates ensuring agent_group spec files define a fully autonomous agent with role,
  model, tools, boot sequence, and dispatch rules.
domain: agent_card
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.97
related:
  - bld_collaboration_agent_card
  - bld_knowledge_card_agent_card
  - agent-card-builder
  - bld_memory_agent_card
  - p11_qg_dispatch_rule
  - p11_qg_scoring-rubric
  - p03_ins_agent_card_builder
  - p11_qg_spawn_config
  - p11_qg_boot_config
  - p11_qg_agent
---

## Quality Gate

## Definition
A agent_group spec describes a fully autonomous agent: its identity, the LLM it runs on, the external tools it can call, how it starts up, how it receives work, and how it shuts down. A spec passes this gate when any operator could launch and operate the agent_group from the document alone, without consulting the author.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`agent-card-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `agent_card` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Role** definition (one-paragraph description of what the agent_group does and does not do) | Without role boundary, operators cannot determine if a task is in scope |
| H08 | Spec contains a **Model** assignment: LLM provider and model name (e.g., `provider: anthropic`, `model: claude-opus-4-6`) | Agent_group cannot be launched without knowing which model to request |
| H09 | Spec contains an **MCP server list** (may be empty list `[]`, but must be explicitly declared) | Tool availability determines what the agent_group can execute |
| H10 | Spec contains a **Boot sequence**: ordered steps to bring the agent_group from cold to ready state | Without boot sequence, launch is non-reproducible |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Constraints documented (what the agent_group must never do) | 1.0 | No constraints listed | Partial list, vague | Explicit NEVER list with rationale per constraint |
| 3 | Dispatch rules present (how the agent_group receives and accepts tasks) | 1.0 | No dispatch described | Dispatch channel named, no detail | Full dispatch protocol: channel, format, acceptance criteria |
| 4 | Scaling rules defined (concurrency limits, queue behavior, overflow handling) | 0.5 | No mention | Single-instance only documented | Concurrency limits, queue behavior, and overflow all defined |
| 5 | Monitoring configuration (signals emitted, health check, alerting thresholds) | 1.0 | No monitoring | Logs only | Structured signals + health check + alerting thresholds |
| 6 | Tags include `agent-card` | 0.5 | Missing | Present but misspelled | Exactly `agent-card` in tags list |
| 7 | Domain boundaries explicit (data and systems the agent_group may and may not access) | 1.0 | No boundaries | Implicit in examples | Explicit allowed-access list and forbidden-access list |
| 8 | Tool availability listed with version or source per MCP server | 1.0 | None listed | Names only | Names + source/version + fallback if unavailable |

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental agent_card artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |

## Examples

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
role: Research agent_group — market research, competitor analysis, web scraping
quality: 9.0

## Golden Example 2 (Production — OpenClaude Verification Agent Card)
INPUT: "Create agent card for adversarial verification agent"
OUTPUT: Reference artifact `P08_architecture/compiled/p08_ac_verification.yaml`

| Pattern | Value | Why golden |
|---------|-------|-----------|
| Tool allowlist/denylist | Explicit allowed + disallowed | Not vague "read-only" |
| background: true | Runs independently | Concurrent execution |
| model: inherit | Uses caller's model | Flexible deployment |
| omit_project_rules | Interprets independently | No implementer bias |
| input/output contract | Typed VERDICT enum | Not prose |
| dispatch command | Exact CLI invocation | Copy-pasteable |

## Golden Example 3 (Production — Explore Agent Card)

| Pattern | Value | Why |
|---------|-------|-----|
| model | haiku (not inherit) | Speed over depth |
| thoroughness_levels | quick/medium/very_thorough | Caller controls depth |
| when_not_to_use | "Simple directed search" | Prevents over-engineering |

## Anti-Example 2 (Bad — No tool restrictions)
```yaml
agent_type: reviewer
tools: all
```
FAIL: No denylist. Reviewer with write access can modify what it reviews.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
