---
kind: tools
id: bld_tools_workflow_primitive
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to workflow_primitive production
quality: 9.0
title: "Tools Workflow Primitive"
version: "1.0.0"
author: n03_builder
tags: [workflow_primitive, builder, examples]
tldr: "Golden and anti-examples for workflow primitive construction, demonstrating ideal structure and common pitfalls."
domain: "workflow primitive construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_workflow_primitive
  - bld_collaboration_workflow_primitive
  - bld_config_workflow_primitive
  - p03_ins_workflow_primitive_builder
  - workflow-primitive-builder
  - p03_sp_workflow_primitive_builder
  - bld_tools_signal
  - bld_memory_workflow_primitive
  - bld_schema_workflow_primitive
  - bld_knowledge_card_workflow_primitive
---

# Tools: workflow-primitive-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `cex_mission_runner.py` | Executes primitives in wave order during missions | Runtime execution | ACTIVE |
| `cex_coordinator.py` | Manages synthesis gates between workflow waves | Wave orchestration | ACTIVE |
| `cex_compile.py` | Compiles .md/.yaml to indexed artifacts | Post-save compilation | ACTIVE |
| `cex_doctor.py` | Builder health check — validates primitive structure | Validation phase | ACTIVE |
| `cex_signal_watch.py` | Monitors signals that feed into gate primitives | Gate threshold input | CONDITIONAL |
| `cex_score.py` | Peer review scoring (--apply) | Quality assessment | CONDITIONAL |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| Primitive output directory | `P12_orchestration/compiled/` | write compiled YAML primitive files |
| P12 schema | `P12_orchestration/_schema.yaml` | naming, format, limits |
| Primitive template | `P12_orchestration/templates/tpl_workflow_primitive.md` | human reference for primitive structure |
| SDK workflow module | `cex_sdk/workflow/` | runtime primitive instantiation |
| Mission runner | `_tools/cex_mission_runner.py` | wave execution engine |
| Coordinator | `_tools/cex_coordinator.py` | synthesis gate management |
| Signal directory | `.cex/runtime/signals/` | signals that feed gate thresholds |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Until a dedicated workflow_primitive validator exists, validate manually:
- filename matches `p12_wp_{type}.yaml` or `p12_wp_{type}_{name}.yaml`
- YAML parses without errors
- required fields present: type, description, inputs, outputs
- type is one of the 7-value enum
- each input has name, type, required
- each output has name, type
- loop has max_iter (1-100)
- parallel has merge_ref
- gate has numeric threshold
- router has default_route
- no full workflow graph in the primitive
- total size <= 4096 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_workflow_primitive]] | downstream | 0.48 |
| [[bld_collaboration_workflow_primitive]] | upstream | 0.47 |
| [[bld_config_workflow_primitive]] | downstream | 0.45 |
| [[p03_ins_workflow_primitive_builder]] | upstream | 0.44 |
| [[workflow-primitive-builder]] | downstream | 0.43 |
| [[p03_sp_workflow_primitive_builder]] | upstream | 0.39 |
| [[bld_tools_signal]] | sibling | 0.39 |
| [[bld_memory_workflow_primitive]] | downstream | 0.37 |
| [[bld_schema_workflow_primitive]] | downstream | 0.37 |
| [[bld_knowledge_card_workflow_primitive]] | upstream | 0.37 |
