---
kind: quality_gate
id: p11_qg_agent_computer_interface
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for agent_computer_interface
quality: 9.1
title: "Quality Gate Agent Computer Interface"
version: "1.0.0"
author: n01_review
tags: [agent_computer_interface, builder, quality_gate]
tldr: "10-gate quality check for agent_computer_interface: validates frontmatter, action space, error protocol, and domain accuracy."
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
related:
  - bld_examples_agent_computer_interface
  - bld_schema_agent_computer_interface
  - p11_qg_input_schema
  - p02_qg_training_method
  - bld_output_template_agent_computer_interface
  - p11_qg_knowledge_card
  - p11_qg_interface
  - p11_qg_model_architecture
  - p11_qg_instruction
  - p11_qg_handoff
---

## Quality Gate

## Definition
| Field | Value |
|-------|-------|
| metric | weighted soft score + all HARD gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.0 for golden |
| operator | AND (all HARD) + weighted average (SOFT) |
| scope | any artifact with kind: agent_computer_interface |

## HARD Gates
All must pass. Any failure = immediate reject.
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches ^p08_aci_[a-z][a-z0-9_]+$ | Wrong prefix, uppercase, or bad chars |
| H03 | kind equals literal agent_computer_interface | Any other kind value |
| H04 | pillar equals P08 | Wrong pillar |
| H05 | quality field is null | Any non-null value |
| H06 | domain field is one of allowed enum values | terminal/browser/gui/api/file_system/code_execution |
| H07 | Action Space section present with >= 1 action row | Missing section or empty table |
| H08 | Error Protocol section present with >= 1 error code | Missing section or empty table |
| H09 | Total file size <= 7168 bytes | Exceeds size limit |
| H10 | No credentials, tokens, or secrets in any field | Credential detected |

## SOFT Scoring
Total weights sum to 1.00.
| ID | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|----|-----------|--------|--------|-------|-------|
| S01 | Action space completeness | 0.20 | >= 3 actions with input/output/error schemas | 1-2 actions, partial schemas | No actions or schemas |
| S02 | Observation schema quality | 0.15 | All observation fields typed with source | Fields present, types missing | No observation schema |
| S03 | Error protocol coverage | 0.15 | >= 3 error codes with recovery strategies | 1-2 codes, no recovery | No error codes |
| S04 | Security constraints defined | 0.15 | Scope, auth, rate limit all specified | Partial security spec | No security section |
| S05 | Protocol precision | 0.15 | Named protocol + transport + version | Protocol named, no transport | No protocol specified |
| S06 | Domain accuracy | 0.10 | All content matches stated domain (e.g., terminal not browser) | Minor domain drift | Wrong domain throughout |
| S07 | Density discipline | 0.05 | No padding prose, all content in tables | Minor prose padding | Mostly prose, low density |
| S08 | tldr precision | 0.05 | tldr is a standalone sentence capturing the interface purpose | tldr too vague | tldr absent or >160 chars |

**Score = sum(pts * weight) / sum(max_pts * weight) * 10**

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.0 | Golden | Publish as reference ACI spec |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |

## Bypass
| Field | Value |
|-------|-------|
| Conditions | Experimental ACI for a novel interface type with no prior art |
| Approver | N03 builder or N01 researcher |

## Examples

## Golden Example: Terminal ACI via JSON-RPC

```markdown
---
id: p08_aci_bash_executor
kind: agent_computer_interface
pillar: P08
title: "Bash Executor ACI"
version: "1.0.0"
domain: terminal
protocol: json_rpc
quality: null
tldr: "JSON-RPC 2.0 ACI for executing bash commands with structured stdout/stderr observation."
---

## Overview
| Attribute | Value |
|-----------|-------|
| Interface type | terminal |
| Protocol | JSON-RPC 2.0 |
| Transport | Unix domain socket (/var/run/agent_exec.sock) |
| Auth method | token (bearer) |

## Action Space
| Action | Input Schema | Output Schema | Error States |
|--------|-------------|--------------|--------------|
| bash_exec | {cmd: string, timeout_ms: int} | {stdout: string, stderr: string, exit_code: int} | timeout / permission_denied |
| file_read | {path: string} | {content: string, size_bytes: int} | not_found / permission_denied |
| file_write | {path: string, content: string} | {written_bytes: int} | disk_full / permission_denied |

## Observation Schema
| Field | Type | Source | Notes |
|-------|------|--------|-------|
| stdout | string | subprocess stdout | Truncated at 65536 chars |
| stderr | string | subprocess stderr | Truncated at 8192 chars |
| exit_code | int | process exit status | 0 = success |

## Error Protocol
| Code | Meaning | Recovery |
|------|---------|---------|
| -32600 | Invalid request JSON | Retry with corrected schema |
| timeout | Command exceeded timeout_ms | Reduce scope or increase budget |
| permission_denied | Action outside sandbox scope | Check sandbox_config constraints |

## Security & Sandboxing
| Constraint | Value | Enforcement |
|-----------|-------|------------|
| Execution scope | /tmp and /workspace only | seccomp allowlist |
| Auth required | Yes -- bearer token | Verified per request |
| Rate limit | 60 requests/min | Token bucket |
```

## Anti-Examples

| Anti-pattern | Problem | Correct Approach |
|-------------|---------|-----------------|
| action: "run any command" | No schema, unbounded scope | Define typed actions with input/output schemas |
| Missing error_protocol | Agent cannot recover from failures | Document all error codes and recovery strategies |
| protocol: "custom" without spec | Unimplementable, ambiguous | Use named standard (JSON-RPC / MCP / REST) |
| No auth_method field | Security gap for autonomous agents | Always specify auth_method, even if "none" |
| Observation as raw text blob | LLM cannot parse reliably | Structure observations as typed fields |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
