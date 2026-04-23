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
related:
  - bld_schema_agent_computer_interface
  - bld_examples_agent_computer_interface
  - p11_qg_agent_computer_interface
  - bld_knowledge_card_agent_computer_interface
  - bld_architecture_agent_computer_interface
  - bld_tools_agent_computer_interface
  - bld_output_template_input_schema
  - bld_collaboration_agent_computer_interface
  - p03_ins_mcp_server
  - bld_knowledge_card_mcp_server
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_agent_computer_interface]] | downstream | 0.48 |
| [[bld_examples_agent_computer_interface]] | downstream | 0.39 |
| [[p11_qg_agent_computer_interface]] | downstream | 0.37 |
| [[bld_knowledge_card_agent_computer_interface]] | upstream | 0.34 |
| [[bld_architecture_agent_computer_interface]] | downstream | 0.32 |
| [[bld_tools_agent_computer_interface]] | upstream | 0.26 |
| [[bld_output_template_input_schema]] | sibling | 0.23 |
| [[bld_collaboration_agent_computer_interface]] | downstream | 0.22 |
| [[p03_ins_mcp_server]] | upstream | 0.22 |
| [[bld_knowledge_card_mcp_server]] | upstream | 0.20 |
