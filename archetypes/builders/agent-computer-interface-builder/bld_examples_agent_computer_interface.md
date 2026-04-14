---
kind: examples
id: bld_examples_agent_computer_interface
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of agent_computer_interface artifacts
quality: null
title: "Examples Agent Computer Interface"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_computer_interface, builder, examples]
tldr: "Golden and anti-examples of agent_computer_interface artifacts"
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
---
type: agent_computer_interface
name: sys_daemon_protocol
version: 1.2
---
# System Daemon Interface (SDI)
# Description: A structured JSON-RPC protocol for interacting with the local system management daemon.
# Transport: Unix Domain Socket (/var/run/sys_daemon.sock)

## Command Schema
All requests must follow the JSON-RPC 2.0 format.

### Method: list_processes
- Description: Returns a list of all running processes managed by the daemon.
- Parameters: None
- Response: `{"result": [{"pid": 123, "name": "nginx", "status": "running"}]}`

### Method: terminate_process
- Description: Sends a SIGTERM to a specific PID.
- Parameters: `{"pid": integer}`
- Response: `{"result": "success"}`

### Method: get_resource_usage
- Description: Returns CPU and Memory utilization.
- Parameters: `{"metric": "cpu" | "memory"}`
- Response: `{"result": {"value": 45.2, "unit": "percent"}}`

## Error Codes
- -3
| Anti-pattern: missing action_space | Always define what actions the ACI exposes |
| Anti-pattern: no error handling spec | Document tool failure / timeout behavior |
