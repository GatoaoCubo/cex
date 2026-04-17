---
id: p11_qg_boot_config
kind: quality_gate
pillar: P11
title: "Gate: boot_config"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: boot_config
quality: 9.0
tags: [quality-gate, boot-config, P11, P02, governance, initialization, provider]
tldr: "Gates for boot_config artifacts — provider-specific agent initialization parameters and constraints."
density_score: 0.88
llm_function: GOVERN
---
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
