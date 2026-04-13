---
id: n06_task
kind: knowledge_card
type: task
pillar: P06
title: "Task — Quality Gate for Session Backend"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 8.9
tags: [task, p06, quality-gate, session-backend]
tldr: "Systematic validation of session backend artifacts through structured checks and automated gates"
when_to_use: "Auditing, validating, or improving session backend artifacts"
keywords: [task, quality-gate, session-backend, validation, artifact, check]
feeds_kinds: [task]
density_score: 0.85
---

# Task

## Spec
```yaml
kind: task
pillar: P06
llm_function: VALIDATOR
max_bytes: 4096
naming: p06_task_{{name}}.md + .yaml
core: true
```

## What It Is
A task is a structured validation process that ensures session backend artifacts meet predefined quality criteria. It defines a systematic way to check for compliance with technical standards, security protocols, and operational requirements. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what checks execute to validate this artifact?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ValidationChain` | Sequential checks with defined rules |
| LlamaIndex | `ValidationPipeline` | Multi-step verification with phase management |
| CrewAI | `Validator` + `Process` | Task definition with sequential/hierarchical checks |
| DSPy | `dspy.Module.validate()` method | Structured validation with defined phases |
| Haystack | `ValidationPipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `GroupChat` workflow | Multi-agent verification patterns |
| Microsoft Semantic Kernel | `ValidationPlan` / `KernelFunction` | Function orchestration with step management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| check_type | enum | "auto" | auto (system-defined) vs manual (user-defined) |
| phases | array | required | More phases = granular control vs complexity |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "json" | Structured output vs natural language |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| audit | System check | artifact, rules | audit_report |
| validate | Compliance check | audit_report, criteria | validation_result |
| report | Summary generation | validation_result | final_report |

## Check Patterns
| Check Type | Example | Activation |
|--------------|---------|------------|
| auto_check | "schema_validation", "security_check" | System-defined rules |
| manual_check | "user_review", "peer_review" | User-defined criteria |
| hybrid_check | "combined_validation" | Mixed rule set |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute validation |
| H02_check_valid | check_type in allowed values | Cannot activate task |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# Auto-validation task
check_type: auto
phases: [audit, validate, report]

# Manual review task
check_type: manual
phases: [audit, report]

# Hybrid validation
check_type: hybrid
phases: [audit, validate, report]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase task | Not reusable, just a rule | Use check_rule for one-off validations |
| No check definition | Cannot be activated | Define clear check conditions |
| Agent identity in task | Mixing concerns | Use agent for identity, task for validation |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Tasks are loaded by agents to extend validation capabilities
- **F3 INJECT**: Tasks can inject domain-specific validation rules
- **F5 CALL**: Tasks orchestrate rule usage across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

Tasks enable modular, reusable validation definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~12 bundled tasks as battle-tested implementations:

| Task | Check | Pattern | CEX Equivalent |
|-------|-------|---------|----------------|
| /validate | auto_check | 3-phase validation | p06_task_validate |
| /review | manual_check | peer review | p06_task_review |
| /audit | auto_check | system audit | p06_task_audit |
| /secure | auto_check | security scan | p06_task_secure |
| /check | hybrid_check | combined validation | n/a (Anthropic-specific) |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter,
not as code. The task body IS the prompt injected when the task triggers. This
maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /validate):
- Phase 1: Identify validation rules (schema, security)
- Phase 2: Dispatch 3 validators concurrently, each with the full rules + specialized focus
- Phase 3: Aggregate findings and flag issues
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /review):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial task | Agent explicitly tries to BREAK the implementation | p06_task_validate |
| Parallel review | Multiple focused agents analyze same artifact concurrently | p06_task_review |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | p06_task_review |
| Background extract | Runs silently after N turns, extracts persistent memories | p06_task_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p06_task_validate |
