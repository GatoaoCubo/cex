---  
```yaml
id: p12_spawn_operations_nucleus  
kind: spawn_config  
pillar: P12  
version: "1.0.0"  
created: "2023-11-18"  
updated: "2023-11-18"  
author: "builder"  
title: "Operations Nucleus Launch"  
mode: grid  
agent_node: "builder_lead"  
model: "opus"  
flags:  
  - "--dangerously-skip-permissions"  
  - "--no-chrome"  
  - "-p"  
  - "--model opus"  
  - "--mcp-config .mcp-edison.json"  
  - "--strict-mcp-config"  
mcp_config: ".mcp-edison.json"  
timeout_seconds: 3000  
prompt_inline: false  
handoff_path: "handoffs/operations_task.md"  
quality: null  
tags: [spawn_config, edison, operations_nucleus, grid]  
tldr: "Grid spawn for Operations Nucleus with builder_lead, 3000s timeout, using handoff prompt strategy"
```  
---  
## Spawn Command  
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File records/framework/powershell/spawn_grid.ps1 -sat edison -task "Load handoff file from handoffs/operations_task.md and execute." -interactive  
```  
## Parameters  
| Parameter | Value | Rationale |  
|-----------|-------|-----------|  
| mode | grid | Utilizes multiple agent_node agents in parallel |  
| agent_node | builder_lead | Task requires builder_lead for operations execution |  
| model | opus | builder_lead is paired with opus for build tasks |  
| timeout | 3000s | Provides a sufficient window for operations task completion |  
| interactive | true | Keeps terminal open for monitoring and adjustments |  
## Constraints  
- Handoff file must be pre-existing and accessible at specified path  
- Maximum inline prompt constraint bypassed by handoff usage  
- builder_lead requires specific MCP configuration provided by a JSON file  
## References  
- handoffs/operations_task.md