---
kind: knowledge_card
id: bld_knowledge_card_toolkit
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for toolkit production — atomic searchable facts
sources: toolkit-builder schema + cex_skill_loader.py + cex_router.py
quality: 9.1
title: "Knowledge Card Toolkit"
version: "1.0.0"
author: n03_builder
tags: [toolkit, builder, examples]
tldr: "Golden and anti-examples for toolkit construction, demonstrating ideal structure and common pitfalls."
domain: "toolkit construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_toolkit_builder
  - p03_ins_toolkit_builder
  - bld_memory_toolkit
  - toolkit-builder
  - p11_qg_toolkit
  - bld_config_toolkit
  - bld_schema_toolkit
  - p01_kc_toolkit
  - bld_collaboration_toolkit
  - bld_output_template_toolkit
---

# Domain Knowledge: toolkit
## Executive Summary
Toolkits are YAML permission bundles — thand access control mechanism for agent tool usage. Each toolkit defines which tools an agent or nucleus can access, what confirmation level each tool requires (auto for reads, confirm for writes, deny for dangerous), and which agents are explicitly denied specific tools. Unlike tool implementations (code), agent identities (system_prompts), or workflows (step graphs), toolkits carry only permission metadata — no execution logic, no persona rules, no sequencing.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| Format | YAML |
| Naming | `p04_tk_{name}.yaml` |
| Max bytes | 4096 |
| Required fields | 4: name, tools, category, requires_confirmation |
| Tool object fields | 3 required (name, description, confirmation) + 3 optional (mcp_endpoint, denied_for, risk_level) |
| Confirmation tiers | `auto` (read) / `confirm` (write) / `deny` (dangerous) |
| Max tools per toolkit | 15 |
| Categories | file_ops, git_ops, search, web, system, build, analysis |
| Scope levels | nucleus, global, agent |
## Patterns
| Pattern | Rule |
|---------|------|
| Least-privilege | Start with zero tools, add only what the agent demonstrably needs |
| Read = auto | Read operations (list, search, read, glob) get `confirmation: auto` |
| Write = confirm | Write operations (write, edit, create) MUST get `confirmation: confirm` |
| Dangerous = deny | Delete, force-push, reset default to `confirmation: deny` |
| Deny over allow | Deny lists override allow lists — denied tools cannot be re-enabled |
| One toolkit per domain | file_ops, git_ops, search each get their own toolkit |
| One tool per toolkit | Each tool lives in exactly one toolkit — no duplicates |
| 15-tool cap | More than 15 indicates the domain should be split |
| MCP mapping | Remote tools include MCP server endpoint for execution |
| Quarterly review | Remove tools the agent hasn't used in 90 days |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Kitchen-sink toolkit with 20+ tools | Violates least-privilege, exceeds tool limit, increases cognitive load |
| Write tool with `confirmation: auto` | Accidental state mutations — HARD gate failure |
| No deny lists | Every agent can use every tool, including dangerous ones |
| Implementation code in toolkit | Toolkits define permissions, not implementations |
| Duplicate tools across toolkits | Conflicting permission states and audit confusion |
| Vague descriptions ("does stuff") | Agents need clear purpose to decide when to use each tool |
| Category mismatch (git tools in file_ops) | Breaks domain grouping and review process |
| Global scope for agent-specific tools | Grants unnecessary access to all agents |
## Application
1. Identify the target agent/nucleus and its required operations
2. Classify each operation by risk: read, write, delete, dangerous
3. Assign confirmation tiers: auto for reads, confirm for writes, deny for dangerous
4. Add deny lists for agents that should not have specific tools
5. Map tools to MCP endpoints if they execute remotely
6. Group tools by domain category (file_ops, git_ops, etc.)
7. Cap at 15 tools — split into sub-toolkits if more are needed
8. Validate no cross-toolkit duplication
9. Name file `p04_tk_{name}.yaml`, keep under 4096 bytes
10. Schedule quarterly review for least-privilege compliance
## References
- Schema: toolkit schema (P06)
- Runtime: cex_skill_loader.py, cex_router.py
- Pillar: P04 (tools)
- MCP: MCP protocol specification for tool-to-server mapping
- Boundary: tool_implementation (code), system_prompt (identity), workflow_primitive (steps) — all distinct from toolkit

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_toolkit_builder]] | downstream | 0.67 |
| [[p03_ins_toolkit_builder]] | downstream | 0.66 |
| [[bld_memory_toolkit]] | downstream | 0.66 |
| [[toolkit-builder]] | downstream | 0.61 |
| [[p11_qg_toolkit]] | downstream | 0.61 |
| [[bld_config_toolkit]] | downstream | 0.59 |
| [[bld_schema_toolkit]] | downstream | 0.58 |
| [[p01_kc_toolkit]] | sibling | 0.56 |
| [[bld_collaboration_toolkit]] | downstream | 0.54 |
| [[bld_output_template_toolkit]] | downstream | 0.50 |
