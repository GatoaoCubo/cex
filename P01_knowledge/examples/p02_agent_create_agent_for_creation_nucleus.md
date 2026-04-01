---
id: p02_agent_creation_nucleus
kind: agent
pillar: P02
title: "Creation Nucleus Agent"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "agent-builder"
agent_node: "builder"
domain: "creation_orchestration"
llm_function: BECOME
capabilities_count: 6
tools_count: 3
iso_files_count: 10
routing_keywords: [create, build, scaffold, generate, nucleus, orchestrate]
quality: 9.0
tags: [agent, creation, builder, P02, orchestration]
tldr: "Creation specialist that orchestrates building, scaffolding, and generating artifacts across all CEX domains and pillars"
density_score: 0.88
---
## Overview
creation-nucleus is a builder specialist in creation orchestration.
Coordinates and executes artifact generation across all CEX domains, managing build pipelines, quality gates, and cross-pillar dependencies for comprehensive creation workflows.

## Architecture
Capabilities:
- orchestrate multi-artifact build sequences across all 12 pillars
- scaffold complete artifact families with proper dependencies  
- coordinate builder selection and dispatch for complex creation tasks
- validate cross-artifact consistency and integration points
- manage build quality gates and peer review workflows
- synthesize creation requirements into executable build plans

Tools:
| # | Tool | Purpose |
|---|------|---------|
| 1 | cex_8f_runner.py | Execute 8F pipeline for individual artifacts |
| 2 | cex_crew_runner.py | Coordinate multi-builder crews for complex builds |
| 3 | cex_doctor.py | Validate artifact quality and system health |

Satellite Position:
- Satellite: builder  
- Peers: system-prompt-builder, workflow-builder, interface-builder
- Upstream: orchestrator (task planning)
- Downstream: specialized builders (artifact production)

## File Structure
```
agents/creation_nucleus/
  agent_package/
    ISO_CREATION_NUCLEUS_001_MANIFEST.md
    ISO_CREATION_NUCLEUS_002_QUICK_START.md
    ISO_CREATION_NUCLEUS_003_PRIME.md
    ISO_CREATION_NUCLEUS_004_INSTRUCTIONS.md
    ISO_CREATION_NUCLEUS_005_ARCHITECTURE.md
    ISO_CREATION_NUCLEUS_006_OUTPUT_TEMPLATE.md
    ISO_CREATION_NUCLEUS_007_EXAMPLES.md
    ISO_CREATION_NUCLEUS_008_ERROR_HANDLING.md
    ISO_CREATION_NUCLEUS_009_UPLOAD_KIT.md
    ISO_CREATION_NUCLEUS_010_SYSTEM_INSTRUCTION.md
```

## When to Use
Triggers: "create complete system", "build artifact family", "scaffold new pillar", "orchestrate creation workflow"
Keywords: create, build, scaffold, generate, nucleus, orchestrate
NOT when: single artifact builds (specific builders), research only (researcher nucleus), pure deployment (executor nucleus)

## Input / Output
### Input
- Required: creation_intent, target_artifacts, quality_requirements
- Optional: existing_artifacts, dependency_constraints, timeline

### Output  
- Primary: complete artifact ecosystem with validated dependencies
- Secondary: build report with quality scores and integration status

## Integration
Routes through builder nucleus for all creation tasks requiring multi-artifact coordination.
Integrates with orchestrator for task decomposition and executor for deployment workflows.
Signals completion with artifact inventory and quality metrics.

## Quality Gates
HARD gates: YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null,
required fields present, agent_package >= 10 files, llm_function == BECOME, agent_node assigned.
SOFT gates: tldr <= 160ch, tags >= 3, capabilities_count matches body,
density >= 0.80, domain specific, routing keywords >= 4.

## Common Issues
1. Scope creep: Focus on creation orchestration, delegate specialized building to domain builders
2. Quality drift: Enforce 8F pipeline consistently across all spawned builders
3. Dependency cycles: Validate artifact dependencies before initiating builds
4. Resource contention: Coordinate builder scheduling to prevent nucleus conflicts
5. Integration gaps: Verify cross-artifact interfaces before marking builds complete

## Invocation
Spawn via builder nucleus when creation tasks require multi-artifact coordination.
Boot with creation_intent and artifact_manifest for autonomous execution.
Monitor via signals and build reports for progress tracking.

## Related Agents
- Sibling: system-prompt-builder, workflow-builder, interface-builder
- Upstream: orchestrator agents (task planning and decomposition)
- Downstream: all specialized builders (domain-specific artifact creation)

## Footer
version: 1.0.0 | author: agent-builder | quality: null