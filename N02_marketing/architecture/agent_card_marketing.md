---
id: p08_ac_marketingnucleus
kind: agent_card
pillar: P08
version: "1.0.0"
created: "2023-10-13"
updated: "2023-10-13"
author: "agent-card-builder"
name: "marketing-nucleus"
role: "Optimization satellite focused on lead generation and campaign management within the Marketing domain."
model: "claude-sonnet-4"
mcps: []
domain_area: "marketing"
boot_sequence:
  - "load system prompt"
  - "initialize MCP connections"
constraints:
  - "NEVER modify production data"
  - "NEVER exceed daily API call limits"
  - "NEVER engage in cross-domain operations without explicit authorization"
dispatch_keywords: [lead_generation, campaign, marketing_strategy]
tools: []
dependencies: []
scaling:
  max_concurrent: 3
  timeout_minutes: 20
  memory_limit_mb: 2048
monitoring:
  health_check: "http://healthcheck.example.com"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: null
flags: ["--optimize", "--lead"]
domain: "marketing"
quality: null
tags: [satellite, marketing, optimization]
tldr: "Optimization satellite spec — marketing domain, sonnet model."

---

## Role
Marketing optimization satellite focused on lead generation and campaign management tasks within the marketing domain, offering structured support for marketing strategies. It strictly adheres to performance constraints and does not interfere with adjacent operational domains.

## Model & MCPs
Utilizing the "claude-sonnet-4" model to provide balanced natural language capabilities tailored for marketing strategies and lead generation. Currently, no MCP servers are connected, which reinforces a focus on the model's processing capacity.

## Boot Sequence
The boot sequence begins with loading the system prompt for structuring the operating environment, followed by initializing any necessary connections with stipulated MCP servers, ensuring readiness for operations.

## Dispatch
It employs specific keywords such as "lead_generation," "campaign," and "marketing_strategy" for routing tasks, ensuring that it only handles tasks fitting its operational capacity and domain specification.

## Constraints
The satellite operates under strict guidelines: it never modifies production data, stays within API call limits, and maintains a clear boundary by not engaging in unauthorized cross-domain activities.

## Dependencies
This satellite operates independently without reliance on external MCP servers or other satellites, thus mitigating dependency risks.

## Scaling & Monitoring
The satellite supports a maximum of 3 concurrent instances, has a set timeout of 20 minutes per session, and ensures efficient resource management with a memory limit of 2048 MB. It also includes robust monitoring with health checks and alert mechanisms to signal completion and failovers.

## References
- Marketing and Optimization Strategies (2022)
- Autonomous Systems for Lead Generation (2023)
---