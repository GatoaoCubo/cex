---
id: p12_wf_create_orchestration_agent
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "workflow-builder"
title: "Create Agent for Orchestration Nucleus"
steps_count: 4
execution: mixed
agent_nodes: [n01, n03, n05]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [complete, error, agent_ready]
spawn_configs: [p12_spawn_n01_research, p12_spawn_n03_build, p12_spawn_n05_validate]
domain: "orchestration"
quality: 8.7
tags: [workflow, orchestration, agent-creation, multi-nucleus]
tldr: "4-step mixed workflow to research, design, build and validate an orchestration agent for N07 nucleus coordination"
density_score: 0.92
---
## Purpose
Orchestrates the creation of a specialized agent for the orchestration nucleus (N07) that can coordinate multi-agent missions, manage handoffs, monitor signals, and consolidate results. The workflow ensures the agent meets N07's requirements for autonomous coordination while maintaining quality gates and operational safety.

## Steps

### Step 1: Research Orchestration Patterns [n01]
- **Agent**: n01 (research nucleus)
- **Action**: Research orchestration patterns, multi-agent coordination strategies, and N07 operational requirements
- **Input**: N07 nucleus documentation, existing orchestration frameworks, coordination patterns
- **Output**: research brief with orchestration requirements and best practices
- **Signal**: research_complete
- **Depends on**: none (wave 1)

### Step 2: Design Agent Architecture [n03]
- **Agent**: n03 (builder nucleus)
- **Action**: Design agent specification including capabilities, interfaces, coordination protocols, and decision frameworks
- **Input**: orchestration requirements from Step 1, N07 operational constraints
- **Output**: agent architecture specification and interface definitions
- **Signal**: design_complete
- **Depends on**: Step 1

### Step 3: Build Orchestration Agent [n03]
- **Agent**: n03 (builder nucleus)
- **Action**: Implement the orchestration agent following architecture specification with coordination logic and safety constraints
- **Input**: agent architecture from Step 2, validated design patterns
- **Output**: complete orchestration agent with coordination capabilities
- **Signal**: build_complete
- **Depends on**: Step 2

### Step 4: Validate Agent Operations [n05]
- **Agent**: n05 (operations nucleus)
- **Action**: Test agent coordination capabilities, validate safety constraints, and verify integration with N07 protocols
- **Input**: built orchestration agent from Step 3, N07 test scenarios
- **Output**: validated agent ready for N07 deployment with test results
- **Signal**: agent_ready
- **Depends on**: Step 3

## Dependencies
- N07 nucleus documentation and operational requirements must be accessible
- Spawn configurations for n01, n03, and n05 must be valid and active
- Test scenarios and validation criteria for orchestration agents must be defined

## Signals
- **On step complete**: nucleus_complete signal emitted by executing nucleus with quality score
- **On workflow complete**: agent_ready signal with deployment readiness status
- **On error**: nucleus_error signal with retry per step (max 1), escalate to N07 if global failure