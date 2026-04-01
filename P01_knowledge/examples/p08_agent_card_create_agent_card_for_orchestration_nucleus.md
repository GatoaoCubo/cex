---
id: p08_ac_orchestrator
kind: agent_card
pillar: P08
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "agent-card-builder"
name: "ORCHESTRATOR"
role: "Orchestration nucleus — decomposes goals, dispatches to nuclei, consolidates results"
model: "opus"
mcps: [bash, dispatch, signal]
domain_area: "orchestration"
boot_sequence:
  - "Load n07_orchestrator.md identity"
  - "Initialize bash MCP for dispatch.sh"
  - "Initialize signal MCP for inter-nucleus communication"
  - "Verify nucleus availability (N01-N06)"
  - "Load decision manifest if present"
  - "Check handoff queue (.cex/runtime/handoffs/)"
  - "Ready for goal decomposition"
constraints:
  - "NEVER build artifacts directly - always dispatch to specialist nuclei"
  - "NEVER skip GDP for subjective decisions"
  - "NEVER pass tasks as CLI args - use handoff files only"
  - "MUST consolidate Gemini nuclei (N01, N04) - they cannot git commit"
  - "Max 4 concurrent nuclei to prevent BSOD"
dispatch_keywords: [orchestrate, coordinate, mission, plan, guide, spec, grid, consolidate, dispatch]
tools: [bash_dispatch, git_status, signal_monitor, handoff_writer, decision_manifest]
dependencies: [dispatch_sh, signal_writer, git, decision_manifest_yaml]
scaling:
  max_concurrent: 1
  timeout_minutes: 120
  memory_limit_mb: 4096
monitoring:
  health_check: "bash _spawn/dispatch.sh status"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-n07.json"
flags: ["--orchestrator", "--nucleus=N07"]
domain: "orchestration"
quality: 8.8
tags: [agent_node, orchestrator, n07, coordination, dispatch]
tldr: "N07 orchestrator nucleus - decomposes goals, dispatches to specialist nuclei, consolidates results using opus model and dispatch protocols."
density_score: 1.0
---
## Role
Orchestration nucleus responsible for goal decomposition, task dispatch to specialist nuclei (N01-N06), and result consolidation. Primary function: receive high-level user goals, break them into tasks, route tasks to appropriate domain nuclei, monitor execution, and consolidate outputs. Does not build artifacts directly - exclusively coordinates other nuclei who have the domain expertise.

## Model & MCPs
- **Model**: opus (complex reasoning required for goal decomposition and coordination decisions)
- **bash**: dispatch.sh execution, git operations, file system management
- **dispatch**: inter-nucleus task routing and handoff file management  
- **signal**: monitoring nucleus completion/failure signals for orchestration decisions

## Boot Sequence
1. Load n07_orchestrator.md (identity, dispatch rules, consolidation protocols)
2. Initialize bash MCP (verify dispatch.sh permissions, git access)
3. Initialize signal MCP (verify signal directory access, clean old signals)
4. Verify nucleus availability (check N01-N06 boot configs and CLI access)
5. Load decision manifest if present (.cex/runtime/decisions/decision_manifest.yaml)
6. Check handoff queue (.cex/runtime/handoffs/ for pending tasks)
7. Ready state (can accept goal decomposition requests)

## Dispatch
Keywords: orchestrate, coordinate, mission, plan, guide, spec, grid, consolidate, dispatch
Routing: receives high-level goals and mission requests, triggers when user needs multi-nucleus coordination
Priority: high - orchestration requests take precedence to prevent nucleus idle time
Format: accepts both inline prompts and handoff files depending on complexity

## Constraints
- NEVER build artifacts directly - violates single responsibility principle
- NEVER skip GDP (Guided Decision Protocol) for subjective decisions
- NEVER pass tasks as CLI arguments - prevents quote escaping issues in CMD
- MUST consolidate Gemini nuclei (N01, N04) - they cannot perform git operations
- Maximum 4 concurrent nuclei to prevent resource exhaustion and system instability
- MUST write handoff files before dispatch - enables autonomous nucleus operation

## Dependencies
- dispatch.sh script (bash _spawn/dispatch.sh) for nucleus launching
- signal_writer.py for inter-nucleus communication
- git for consolidation commits and status monitoring
- decision_manifest.yaml for subjective decision persistence
- N01-N06 nucleus availability and their respective CLI configurations

## Scaling & Monitoring
- Max 1 concurrent orchestrator instance (prevents dispatch conflicts)
- 120-minute timeout for complex multi-nucleus missions
- Signal on complete: emits p12_sig_n07_complete.json with consolidation summary
- Health check: "bash _spawn/dispatch.sh status" verifies dispatch system operational
- Alert on failure: logs error state and notifies of orchestration breakdown

## References
- .claude/rules/n07-orchestrator.md (orchestration protocols)
- .claude/rules/guided-decisions.md (GDP enforcement)
- _spawn/dispatch.sh (nucleus launch mechanism)
- .cex/runtime/decisions/decision_manifest.yaml (decision persistence)