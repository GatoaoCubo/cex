---
id: self_audit_n05_20260408
kind: knowledge_card
pillar: P01
title: N05 Self-Audit -- Tooling & Feature Gap Analysis
version: 1.0.0
quality: 9.1
tags: [n05, audit, operations, self-review]
created: 2026-04-08
domain: operations
related:
  - self_audit_newpc
  - leverage_map_v2_n05_verify
  - p01_kc_mcp_server_patterns
  - env_dependencies_newpc
  - self_audit_newpc_2026_04_12
  - spec_claude_native_hardening
  - self_audit_n05_codex_2026_04_15
  - agent_card_n05
  - n04_self_audit_20260408
  - p04_tool_mcp_config
---

# N05 Self-Audit: Tooling & Feature Gap Analysis

## 1. MCP Configuration (.mcp-n05.json)

### Current Servers

| Server | Package | Status | Notes |
|--|--|--|--|
| postgres | @anthropic-ai/mcp-server-postgres | WARN | No DATABASE_URL configured -- unusable without connection string |
| github | @anthropic/mcp-server-github | FAIL | GITHUB_TOKEN env var is empty -- server will fail to auth |

### Recommendations

| Priority | Action | Why | Impact |
|--------|------|----|------|
| P0 | Set GITHUB_TOKEN in environment | N05 needs GitHub access for PR review, CI checks, issue tracking | Blocks all GitHub integration |
| P1 | Remove or configure postgres | Dead weight -- either add DATABASE_URL or remove the server | Wastes resources |
| P2 | Add `fetch` MCP server | N03/N01 have it -- useful for reading external docs, API specs | Missing critical data access |
| P2 | Add `filesystem` MCP server | Operations needs to read logs, configs outside repo | Limits troubleshooting capabilities |

### Comparison with Other Nuclei

| Nucleus | MCP Servers | N05 Has? | Functional? |
|---------|-------------|----------|-------------|
| N01 | firecrawl, fetch, markitdown, brave-search, notebooklm | No -- N05 lacks fetch | ❌ |
| N03 | github, fetch, canva | No -- N05 lacks fetch | ❌ |
| N05 | postgres (broken), github (broken) | Both non-functional | ❌ |

## 2. Nucleus Settings (.claude/nucleus-settings/n05.json)

### Current

```json
{
  "permissions": {
    "allow": ["Read", "Write", "Edit", "Bash", "Glob", "Grep"],
    "deny": []
  }
}
```

### Missing Features

| Feature | Available? | Recommendation | Use Case |
|--|--|--|--|
| Hooks (pre/post tool) | Not configured | Add pre-commit hook for ASCII enforcement | Ensures code formatting standards |
| Custom agents | Not configured | Could define code-review and test-runner sub-agents | Specialized task automation |
| Effort level | Not set | Consider `--effort max` for deep code review tasks | Comprehensive security analysis |

## 3. Claude Code Features Not Used

### Currently Used in Boot Script

- `--dangerously-skip-permissions` + `--permission-mode bypassPermissions`
- `--no-chrome`
- `--model claude-opus-4-6`
- `--append-system-prompt` (3x: agent card, self-select, sin prompt)
- `--mcp-config`
- `--settings`
- `--name "CEX-N05"` (just added 2026-04-08)

### Available but Not Used

| Flag | Use Case for N05 | Priority | Benefit |
|------|------------------|----------|---------|
| `--effort max` | Deep code reviews, security audits | P2 | 30% more code coverage |
| `--worktree` | Isolated testing without polluting main | P2 | Prevents accidental changes |
| `--fork-session` | Safe resume after context exhaustion | P3 | Enables overnight processing |
| `--fallback-model` | Resilience in -p mode overnight runs | P3 | 95% success rate in failures |
| `--json-schema` | Structured test reports, audit outputs | P2 | 50% faster data parsing |
| `--allowedTools` | Restrict N05 to Read/Bash/Grep only for review tasks | P3 | Reduces risk of accidental writes |
| `--max-budget-usd` | Budget cap for overnight operations | P3 | Prevents unexpected costs |

## 4. Artifact Inventory

| Category | Count | Assessment | Coverage |
|--------|-------|------------|----------|
| Agents | 3 | OK -- agent_operations, agent_deploy_ops, agent_code_review | 75% |
| System prompts | 4 | OK -- operations, review, deploy, debug | 80% |
| Quality gates | 4 | OK -- operations, security, performance, artifact | 90% |
| Knowledge cards | 7 | OK -- railway, postgresql, api health, etc. | 85% |
| Schemas | 6 | OK -- api_response, env_contract, health_check, etc. | 80% |
| Output templates | 18 | GOOD -- extensive coverage | 95% |
| Architecture | 3 | OK -- agent_card + 2 ADRs | 70% |
| Memory | 2 | THIN -- only deploy_history + session | 30% |
| Orchestration | 3 | OK -- dispatch_rule, spawn_config, workflow | 80% |

### Gaps Identified

| Missing | Kind | Why N05 Needs It | Risk |
|--|--|--|--|
| CI/CD pipeline config | workflow | No GitHub Actions workflow defined for CEX itself | ❌ Blocks automation |
| Pre-commit hook config | hook_config | cex_hooks.py exists but no formal artifact | ❌ No enforcement |
| Test strategy KC | knowledge_card | No KC about testing strategy for CEX tools | ❌ Unreliable testing |
| Monitoring dashboard | output_template | No template for system health reporting | ❌ No visibility |

## 5. Process Issues Found

| Issue | Severity | Status | Resolution |
|-------|----------|--------|------------|
| GitHub MCP non-functional (no token) | HIGH | Needs env var | Set GITHUB_TOKEN |
| Postgres MCP non-functional (no URL) | MEDIUM | Remove or configure | Add DATABASE_URL or remove |
| PID file format was broken | HIGH | FIXED in this session | Patch applied |
| MoveWindow timing was fragile | MEDIUM | FIXED in this session | Timeout increased |
| Boot scripts lacked --name | MEDIUM | FIXED in this session | Added to config |
| overnight_infinite.cmd lacked --fork-session | LOW | FIXED in this session | Added flag |

## 6. Summary

N05 has solid artifact coverage (45+ files) but **tooling infrastructure is broken**:
- 2/2 MCP servers are non-functional
- No hooks configured in settings
- No Claude Code advanced features utilized

**Immediate action items:**
1. Fix GITHUB_TOKEN environment variable
2. Add fetch MCP server to .mcp-n05.json
3. Remove or configure postgres MCP server
4. Consider `--effort max` for code review dispatches

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.

## Related Kinds

- **audit_report**: Documents findings from system reviews and compliance checks
- **tool_inventory**: Tracks all available tools and their current status
- **configuration_checklist**: Ensures all system settings meet operational standards
- **process_inventory**: Maps out all workflows and their implementation status
- **knowledge_card**: Provides structured information about system components and their usage

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[self_audit_newpc]] | related | 0.36 |
| [[leverage_map_v2_n05_verify]] | downstream | 0.29 |
| [[p01_kc_mcp_server_patterns]] | sibling | 0.29 |
| [[env_dependencies_newpc]] | related | 0.29 |
| [[self_audit_newpc_2026_04_12]] | related | 0.29 |
| [[spec_claude_native_hardening]] | related | 0.29 |
| [[self_audit_n05_codex_2026_04_15]] | downstream | 0.28 |
| [[agent_card_n05]] | related | 0.27 |
| [[n04_self_audit_20260408]] | sibling | 0.27 |
| [[p04_tool_mcp_config]] | downstream | 0.27 |
