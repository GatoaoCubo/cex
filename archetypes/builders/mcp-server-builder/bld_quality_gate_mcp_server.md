---
id: p11_qg_mcp_server
kind: quality_gate
pillar: P11
title: "Gate: MCP Server"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
domain: mcp_server
quality: 9.0
tags: [quality-gate, mcp-server, protocol, P04, integration]
tldr: "Quality gate for mcp_server artifacts: enforces tool list, transport type, auth strategy, and JSON-Schema params."
density_score: 0.85
llm_function: GOVERN
---
# Gate: MCP Server
## Definition
A `mcp_server` artifact specifies an MCP protocol server: its tools, resources, transport mechanism, and authentication strategy. It is a specification, not an implementation. Gates here ensure every server is unambiguously identifiable, its tools carry machine-readable schemas, and auth matches transport — preventing integration failures before a line of code is written.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p04_mcp_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"mcp_server"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `name`, `transport`, `tools_provided`, `auth`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `tools_provided` is a list with >= 1 named tool | Server with no tools has no purpose |
| H08 | `transport` is one of: `stdio`, `sse`, `http` | Unknown transport — integration impossible |
| H09 | `auth` field is explicitly declared (value or `"none"`) | Missing auth strategy causes insecure defaults |
| H10 | `Tools` section present in body with >= 1 tool entry | Spec without tool details is incomplete |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names the server's purpose and primary tool |
| S02 | Tool schemas have JSON-Schema params | 1.0 | Each tool entry includes `parameters` block with type annotations |
| S03 | Resource URIs follow templates | 1.0 | Resource URIs use `{variable}` template syntax, not hard-coded paths |
| S04 | Auth matches transport type | 1.0 | `stdio` paired with `none`; `sse`/`http` paired with `api_key`, `oauth`, or `bearer` |
| S05 | Error handling documented | 1.0 | Each tool documents at least one error code or failure mode |
| S06 | `tags` includes `"mcp-server"` | 0.5 | Minimum tag for routing |
| S07 | Health endpoint defined | 0.5 | `http`/`sse` transports specify a health check path |
| S08 | Rate limits specified | 0.5 | Rate limit per tool or server-wide limit documented |
| S09 | Dependency versions pinned | 0.5 | Runtime dependencies list exact versions, not ranges |
| S10 | Examples for each tool | 1.0 | At least one request/response example per tool in body |
| S11 | No implementation code in body | 1.0 | Body is specification only — no executable code blocks |
| S12 | Density >= 0.80 | 0.5 | No filler: "this server provides", "allows you to", "in order to" |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|
| condition | Proof-of-concept server with single tool and no auth requirement (local stdio only) |
| approver | P04 integration owner |
