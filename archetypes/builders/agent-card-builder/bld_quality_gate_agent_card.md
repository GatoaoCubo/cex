---
id: p11_qg_agent-card
kind: quality_gate
pillar: P11
title: "Gate: Agent_group Spec"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
domain: agent_card
quality: 9.1
density_score: 0.97
tags:
  - quality-gate
  - agent-card
  - autonomous-agent
  - p11
tldr: "Gates ensuring agent_group spec files define a fully autonomous agent with role, model, tools, boot sequence, and dispatch rules."
llm_function: GOVERN
---
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
