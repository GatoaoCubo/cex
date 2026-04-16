---
kind: output_template
id: bld_output_template_agent_computer_interface
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for agent_computer_interface production
quality: 9.1
title: "Output Template Agent Computer Interface"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_computer_interface, builder, output_template]
tldr: "Template with vars for agent_computer_interface production"
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

Copy this template. Replace every `{{placeholder}}` with real content. Remove placeholder text.
Use tables over prose. All sections are required.

```markdown
---
id: p08_aci_{{name}}
kind: agent_computer_interface
pillar: P08
title: "{{Interface display name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
domain: "{{terminal|browser|gui|api|file_system|code_execution}}"
protocol: "{{json_rpc|cli|rest|grpc|mcp}}"
quality: null
tags: [agent_computer_interface, {{domain}}, {{protocol}}]
tldr: "{{One-sentence description of what computing environment this ACI exposes}}"
---

# `{{Interface display name}}` -- ACI Specification

## Overview
| Attribute | Value |
|-----------|-------|
| Interface type | {{terminal / browser / GUI / API / file_system}} |
| Protocol | {{JSON-RPC 2.0 / CLI / REST / gRPC / MCP}} |
| Transport | {{Unix socket / HTTP / stdio / TCP}} |
| Auth method | {{none / token / mTLS / API key}} |
| Scope | {{What computing environment this ACI exposes}} |

## Action Space
| Action | Input Schema | Output Schema | Error States |
|--------|-------------|--------------|--------------|
| {{action_name}} | {{input fields + types}} | {{output fields + types}} | {{timeout / not_found / forbidden}} |

## Observation Schema
| Field | Type | Source | Notes |
|-------|------|--------|-------|
| {{field_name}} | {{string/int/bool}} | {{stdout/response_body/accessibility_tree}} | {{when present}} |

## Error Protocol
| Code | Meaning | Recovery |
|------|---------|---------|
| {{error_code}} | {{human description}} | {{retry / fallback / abort}} |

## Security & Sandboxing
| Constraint | Value | Enforcement |
|-----------|-------|------------|
| Execution scope | {{what is allowed}} | {{sandbox / allowlist / firewall}} |
| Auth required | {{yes/no}} | {{mechanism}} |
| Rate limit | {{requests/min}} | {{enforced by}} |
```
