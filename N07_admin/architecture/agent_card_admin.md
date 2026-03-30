---  
id: p08_ac_admin_nucleus  
kind: agent_card  
pillar: P08  
version: "1.0.0"  
created: "2023-10-29"  
updated: "2023-10-29"  
author: "agent-card-builder"  
name: "Admin Nucleus Satellite"  
role: "Central administrative agent_node responsible for coordination and management of system resources."  
model: "claude-sonnet-4"  
mcps: [control_hub, resource_manager]  
domain_area: "administrative"  
boot_sequence:  
  - "Load system prompt"  
  - "Initialize control_hub MCP"  
  - "Initialize resource_manager MCP"  
  - "Verify tool availability"  
  - "Load domain context"  
constraints:  
  - "Never access unauthorized resources"  
  - "Must not execute external code"  
  - "Forbidden from directly manipulating user data"  
dispatch_keywords: [administrate, manage, coordinate, monitor, control]  
tools: [control_hub_tool, resource_monitor_tool]  
dependencies: [control_hub_mcp, resource_manager_api]  
scaling:  
  max_concurrent: 2  
  timeout_minutes: 20  
  memory_limit_mb: 3072  
monitoring:  
  health_check: "control_hub_tool status_check"  
  signal_on_complete: true  
  alert_on_failure: true  
runtime: "claude"  
mcp_config_file: ".mcp-admin-nucleus.json"  
flags: ["--secure-mode", "--log-level=info"]  
domain: "system-administration"  
quality: null  
tags: [agent_node, administrative, admin-nucleus]    
tldr: "Agent_card for admin nucleus — central administrative management with Claude-sonnet model."  

---  

## Role  
The Admin Nucleus Satellite is designed to oversee and manage system resources, ensuring smooth coordination and administrative control across the entire architecture. This agent_node plays a vital role in facilitating operational management tasks within the administrative domain.  

## Model & MCPs  
The agent_node uses the Claude-sonnet-4 model, offering a well-balanced approach to handling administrative tasks that require quick decision-making and resource management. The MCP servers integrated into this agent_node include the 'control_hub' for administrative commands and 'resource_manager' for overseeing system performance and resources.  

## Boot Sequence  
1. Load system prompt  
2. Initialize control_hub MCP  
3. Initialize resource_manager MCP  
4. Verify tool availability  
5. Load domain context  

## Dispatch  
The Admin Nucleus Satellite responds to keywords such as administrate, manage, coordinate, monitor, and control, allowing the orchestrator to route appropriate tasks to it. Its dispatch system is optimized for high-priority administrative tasks requiring direct oversight of system operations.  

## Constraints  
- Never access unauthorized resources  
- Must not execute external code  
- Forbidden from directly manipulating user data  

## Dependencies  
This agent_node is dependent on the control_hub_mcp and resource_manager_api for task execution, ensuring a secure and controlled administrative environment.  

## Scaling & Monitoring  
The agent_node can support up to 2 concurrent instances, with a 20-minute timeout set for each session to ensure efficient resource utilization and prevent bottlenecks. Monitoring involves regular health checks via the control_hub_tool status_check, with automatically sent signals upon task completion and alerts upon failures.