---
quality: 7.8
quality: 7.6
kind: tools
id: bld_tools_prospective_memory
pillar: P04
llm_function: CALL
purpose: Tools for prospective_memory production
title: "Tools Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, tools]
tldr: "Tools for prospective_memory production."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_tools_hitl_config
  - bld_tools_cli_tool
  - bld_tools_kind
  - bld_tools_memory_scope
  - bld_tools_boot_config
  - bld_tools_retriever_config
  - bld_tools_experiment_config
  - bld_tools_citation
  - bld_tools_quality_gate
  - bld_tools_streaming_config
---
# Tools: prospective-memory-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_retriever.py | Find similar prospective_memory artifacts | Phase 1 | AVAILABLE |
| cex_score.py | Score artifact | Phase 3 | AVAILABLE |
| cex_compile.py | Compile to yaml | Phase 3 | AVAILABLE |

## Execution Mechanisms Reference
| Mechanism | CEX Tool | Notes |
|-----------|---------|-------|
| schedule_signal | ScheduleWakeup (Claude Code) | Native Claude Code scheduling |
| polling | cex_signal_watch.py | Polling loop for condition triggers |
| wake_notification | boot/cex.ps1 | Session-start check of pending reminders |

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Permitted |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | |

## Validation
id `^p10_pm_`, owner non-empty, reminders >= 1, trigger_type per reminder, action_payload non-vague, execution_mechanism declared, quality null, body <= 2048 bytes.

## Tool Integration Checklist

- Verify tool name follows snake_case convention
- Validate input/output schema matches interface contract
- Cross-reference with capability_registry for discoverability
- Test tool invocation in sandbox before production use

## Invocation Pattern

```yaml
# Tool invocation contract
name: tool_name
input_schema: validated
output_schema: validated
error_handling: defined
timeout: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_hitl_config]] | sibling | 0.38 |
| [[bld_tools_cli_tool]] | sibling | 0.38 |
| [[bld_tools_kind]] | sibling | 0.37 |
| [[bld_tools_memory_scope]] | sibling | 0.37 |
| [[bld_tools_boot_config]] | sibling | 0.36 |
| [[bld_tools_retriever_config]] | sibling | 0.36 |
| [[bld_tools_experiment_config]] | sibling | 0.35 |
| [[bld_tools_citation]] | sibling | 0.35 |
| [[bld_tools_quality_gate]] | sibling | 0.35 |
| [[bld_tools_streaming_config]] | sibling | 0.35 |
