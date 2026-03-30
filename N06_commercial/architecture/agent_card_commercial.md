---
id: p08_ac_commercial_nucleus
kind: agent_card
pillar: P08
version: "1.0.0"
created: "2023-10-25"
updated: "2023-10-25"
author: "agent-card-builder"
name: "commercial-nucleus"
role: "Handles commercial operations and strategic decision-making for revenue optimization."
model: "opus"
mcps: [commerce_api, finance_mcp]
domain_area: "commercial-operations"
boot_sequence:
  - "Load commercial_strategy.md"
  - "Initialize commerce_api MCP"
  - "Initialize finance_mcp MCP"
  - "Activate strategic modules"
  - "Ready for task dispatch"
constraints:
  - "Never handle transactions directly to prevent financial discrepancies."
  - "Must not exceed budget limits for strategic analyses."
  - "Forbidden from accessing private customer data."
dispatch_keywords: [optimize, revenue, strategy, pricing, sales]
tools: [commerce_toolkit, financial_analyzer]
dependencies: [finance_mcp, commerce_api]
scaling:
  max_concurrent: 2
  timeout_minutes: 20
  memory_limit_mb: 2048
monitoring:
  health_check: "commerce_api.health_check()"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-commercial.json"
flags: ["--secure-mode", "-v"]
domain: "commercial-operations"
quality: null
tags: [agent_node, commercial, revenue-optimization]
tldr: "commercial-nucleus: Opus model for strategic decision-making in commerce."
## Role
The commercial-nucleus agent_node is responsible for managing commercial operations, focusing on strategic decision-making to optimize revenue, using external tools such as commerce API and finance MCP.

## Model & MCPs
- **Model**: Opus - selected for its reasoning capabilities suitable for complex commercial strategies.
- **commerce_api**: Provides access to commercial data and analytics.
- **finance_mcp**: Supports financial modeling and analysis activities.

## Boot Sequence
1. Load commercial_strategy.md to establish role and constraints.
2. Initialize commerce_api MCP to connect to commercial data sources.
3. Initialize finance_mcp MCP to prepare for financial analysis.
4. Activate strategic modules for revenue optimization tasks.
5. Ready for task dispatch.

## Dispatch
- Keywords: optimize, revenue, strategy, pricing, sales.
- Ensures tasks related to commercial strategy are prioritized to this agent_node.

## Constraints
- Never handle transactions directly to prevent financial discrepancies.
- Must not exceed budget limits for strategic analyses.
- Forbidden from accessing private customer data to ensure compliance with privacy regulations.

## Dependencies
- finance MCP server for financial data processing.
- commerce API for access to commercial operations data.
- No dependencies on sibling agent_nodes for isolation and focus.

## Scaling & Monitoring
- Max 2 concurrent instances to manage load efficiently.
- 20-minute timeout to ensure timely task completion.
- Health checks via commerce_api, issuing signals on task completion, and alerts on failures.

## References
- agent-card-builder SCHEMA.md
- Principles of Strategic Management for Business (2021)

---