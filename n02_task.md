---
id: n02_task_system_prompt_auditor
kind: task
type: improvement
pillar: N04
title: "System Prompt Auditor — Deep Knowledge for audit"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: system_prompt
quality: 9.0
tags: [system_prompt, n04, reusable, kind-kc]
tldr: "Reusable framework for auditing system prompts with structured phases, trigger conditions, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about system prompt artifacts"
keywords: [system_prompt, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [system_prompt]
density_score: 89.5
---

# System Prompt Auditor

## Spec
```yaml
kind: system_prompt
pillar: N04
llm_function: TOOL
max_bytes: 4096
naming: n04_system_prompt_{{name}}.md + .yaml
core: true
```

## What It Is
A system prompt auditor is a reusable framework for auditing system prompts with structured phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. System prompt auditors are NOT agents (P02, which define identity/persona) nor skill artifacts (P04, which define capability). A system prompt auditor answers "what phases execute to achieve this audit?" while agents answer "who am I?" and skills answer "how do I communicate?"

## Cross-Platform Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `PromptTemplate` / `RunnableSequence` | Sequential execution with defined steps |
| LlamaIndex | `QueryPipeline` / `IngestionPipeline` | Multi-step workflows with phase management |
| CrewAI | `Task` + `Process` | Task definition with sequential/hierarchical execution |
| DSPy | `dspy.Module.forward()` method | Structured computation with defined phases |
| Haystack | `Pipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `GroupChat` workflow | Multi-agent conversation patterns |
| Microsoft Semantic Kernel | `Plan` / `KernelFunction` | Function orchestration with step management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| trigger_type | enum | "user_invocable" | user_invocable (slash commands) vs agent_only (programmatic) |
| phases | array | required | More phases = granular control vs complexity |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "markdown" | Structured output vs natural language |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| discover | Context gathering | system_prompt, audit_criteria | context_data |
| analyze | Quality assessment | context_data, feedback_rules | assessment_results |
| suggest | Improvement recommendations | assessment_results, best_practices | improvement_plan |
| finalize | Review summary | improvement_plan, original_prompt | review_summary |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| manual_request | "Audit this prompt" | User explicitly requests audit |
| quality_gate | "Below 8.5" | Automated trigger based on quality score |
| periodic_check | "Weekly audit" | Scheduled audit cycle |
| system_update | "Prompt version 2.0" | Triggered by system changes |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_audit_criteria | audit_criteria not empty | Incomplete assessment |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# Full system prompt audit
trigger_type: user_invocable
slash_command: "/audit"
phases: [discover, analyze, suggest, finalize]
audit_criteria:
  - clarity
  - consistency
  - specificity
  - token_efficiency

# Automated quality gate trigger
trigger_type: agent_only
invoke_pattern: "crew.audit_prompt('version_2.0')"
phases: [discover, analyze]
quality_gate: true
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| No audit criteria | Incomplete assessment | Define clear audit criteria |
| Natural language feedback | Not reusable | Use structured feedback format |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |
| Mixed audit phases | Confusing workflow | Define clear phase sequence |

## Integration Points
- **F2 BECOME**: Auditors are loaded by agents to extend capabilities
- **F3 INJECT**: Auditors can inject domain-specific knowledge
- **F5 CALL**: Auditors orchestrate tool usage across phases
- **Handoffs**: Auditors can be passed between nuclei for specialized execution
- **Memory**: Auditors can persist state between phases via memory_scope

System prompt auditors enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Auditors
OpenClaude ships ~18 bundled auditors as battle-tested implementations:

| Auditor | Trigger | Pattern | CEX Equivalent |
|--------|--------|---------|----------------|
| /audit | manual_request | 3-parallel-agent review | n06_auditor_review |
| /verify | quality_gate | adversarial verification | n06_auditor_verify |
| /optimize | periodic_check | 9-section summarization | n06_auditor_optimize |
| /loop | system_update | recurring cron schedule | n06_auditor_loop (future) |
| /stuck | manual_request | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Auditors are defined as prompt text with frontmatter, not as code. The auditor body IS the prompt injected when the auditor triggers. This maps directly to CEX's auditor-as-artifact model.

**Parallel dispatch pattern** (from /audit):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any auditor can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /verify):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Auditor Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial auditor | Agent explicitly tries to BREAK the implementation | n06_auditor_verify |
| Parallel review | Multiple focused agents analyze same diff concurrently | n06_auditor_review |
| Scratchpad auditor | <analysis> block for private reasoning, stripped from output | n06_auditor_optimize |
| Background extract | Runs silently after N turns, extracts persistent memories | n06_auditor_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | n06_auditor_verify |
