---
id: n06_task
kind: knowledge_card
type: kind
pillar: P04
title: "Task — Structured Workflow Execution for repeatable operations"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.1
tags: [task, p04, reusable, kind-kc]
tldr: "Reusable workflow unit with defined phases, dependencies, and execution guarantees for repeatable operations"
when_to_use: "Designing, reviewing, or reasoning about task artifacts"
keywords: [task, phases, dependency, reusable, workflow, execution, lifecycle]
feeds_kinds: [task]
density_score: 0.92
---

# Task

## Spec
```yaml
kind: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_task_{{name}}.md + .yaml
core: true
```

## What It Is
A task is a reusable workflow unit with defined phases, dependencies, and execution guarantees. It defines a specific operation that can be executed repeatedly across different contexts. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what steps execute to achieve this operation?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| CEX | `Task` / `Workflow` | Sequential execution with defined steps |
| Airflow | `DAG` / `Operator` | Multi-step workflows with dependency management |
| Prefect | `Flow` / `Task` | Task definition with sequential/hierarchical execution |
| Apache Beam | `Pipeline` with transforms | Explicit DAG execution with phase transitions |
| Kubeflow | `Pipeline` with operators | Multi-agent conversation patterns |
| Microsoft Azure | `Pipeline` / `Activity` | Function orchestration with step management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| phase_type | enum | "sequential" | sequential (linear) vs parallel (concurrent) |
| dependencies | array | [] | More dependencies = granular control vs complexity |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "json" | Structured output vs natural language |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |
| memory_scope | enum | "none" | "none" (ephemeral) vs "persistent" (stateful) |
| retry_policy | object | { max_retries: 3 } | Retry logic for failed steps |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| plan | Context gathering | user_input, environment | context_data |
| prepare | Parameter setup | context_data, user_preferences | configuration |
| execute | Main workflow | configuration, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |
| archive | Long-term storage | validated_output, metadata | archived_artifact |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| user_invocable | "/run", "/execute" | User types exact command |
| keyword_match | "deploy", "test" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_task("deploy") | Programmatic call from agent |
| cron_schedule | "0 0 * * *" | Periodic execution via cron |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate task |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |
| H05_quality_floor | Score ≥ 8.5 | Artifact rejected for deployment |
| H06_memory_valid | memory_scope in allowed values | State management errors |

## Industry References
| Standard | Organization | Description |
|---------|-------------|-------------|
| ISO/IEC 23894 | ISO | Reference architecture for AI systems |
| IEEE P7003-2021 | IEEE | Standard for AI system quality assurance |
| NIST AI Risk Management Framework | NIST | Guidelines for AI system governance |
| GDPR | EU | Data protection regulations impacting task execution |

## Practical Examples
1. **System Optimization Task**  
   - Trigger: `/optimize`  
   - Phases: System analysis → Performance benchmark → System refactoring  
   - Tools: Profiler, System monitor, Configuration manager  
   - Output: Optimization report with metrics  

2. **Data Analysis Task**  
   - Trigger: `crew.use_task('data_analysis')`  
   - Phases: Data loading → Data cleaning → Statistical analysis  
   - Tools: Pandas, NumPy, Visualization libraries  
   - Output: Analytical insights and visualizations  

3. **Documentation Task**  
   - Trigger: Event-driven (file change)  
   - Phases: Content discovery → Structure analysis → Documentation generation  
   - Tools: Markdown processor, API explorer, Version control  
   - Output: Formatted documentation in multiple formats  

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase task | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in task | Mixing concerns | Use agent for identity, task for operation |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |
| Missing memory_scope | State management errors | Define memory_scope for persistent tasks |

## Integration Points
- **F2 BECOME**: Tasks are loaded by agents to extend capabilities
- **F3 INJECT**: Tasks can inject domain-specific knowledge
- **F5 CALL**: Tasks orchestrate tool usage across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope
- **Retry Policy**: Tasks can define retry logic for failed steps

## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~18 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /run | slash_command | 3-parallel-agent review | p04_task_run |
| /test | slash_command | adversarial verification | p04_task_test |
| /deploy | agent_invoked | 9-section deployment | p04_task_deploy |
| /loop | slash_command | recurring cron schedule | p04_task_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |
| /backup | event_driven | file_change:*.backup | p04_task_backup |
| /audit | cron_schedule | 0 0 * * * | p04_task_audit |
| /optimize | user_invocable | performance benchmark | p04_task_optimize |
| /benchmark | keyword_match | "speed", "performance" | p04_task_benchmark |
| /extract | event_driven | file_change:*.csv | p04_task_extract |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter, not as code. The task body IS the prompt injected when the task triggers. This maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /run):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /test):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

**Memory persistence pattern** (from /backup):
- Phase 1: Detect file changes
- Phase 2: Archive current state
- Phase 3: Store in persistent memory
- Ensures data integrity across sessions

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial task | Agent explicitly tries to BREAK the implementation | p04_task_test |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_task_run |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | p04_task_test |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_task_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_task_test |
| Retry task | Automatic retry logic for failed steps | p04_task_retry |
| Stateful task | Persists state between executions | p04_task_stateful |
| Conditional task | Executes based on dynamic criteria | p04_task_conditional |
| Pipeline task | Combines multiple sub-tasks in sequence | p04_task_pipeline |
| Distributed task | Executes across multiple nodes | p04_task_distributed |
```
```