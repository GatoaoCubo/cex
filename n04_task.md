---
id: n04_task
kind: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: n04_task_{{name}}.md + .yaml
core: true
---

# Task

## Spec
```yaml
kind: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: n04_task_{{name}}.md + .yaml
core: true
```

## What It Is
A task is a structured unit of work that defines specific objectives, execution parameters, and quality requirements. It represents a discrete action that can be executed autonomously or in coordination with other tasks. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what needs to be done?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` / `AgentExecutor` | Sequential execution with defined steps |
| LlamaIndex | `QueryEngine` / `RetrievalAugmentedGenerator` | Multi-step workflows with phase management |
| CrewAI | `Task` + `Process` | Task definition with sequential/hierarchical execution |
| DSPy | `dspy.Module.forward()` method | Structured computation with defined phases |
| Haystack | `Pipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `GroupChat` workflow | Multi-agent conversation patterns |
| Microsoft Semantic Kernel | `Plan` / `KernelFunction` | Function orchestration with step management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| objective | string | required | Clear goal vs ambiguity |
| dependencies | array | [] | Parallel execution vs sequential |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "json" | Structured output vs natural language |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| plan | Define execution strategy | objective, dependencies | execution_plan |
| execute | Main workflow | execution_plan, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |
| report | Documentation | validated_output | task_summary |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| user_invocable | "/generate", "/retrieve" | User types exact command |
| keyword_match | "query", "search" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_task("analyze") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_objective_defined | objective not empty | Cannot execute workflow |
| H02_dependencies_valid | dependencies array not empty | Execution order ambiguity |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable task (slash command)
trigger_type: user_invocable
slash_command: "/generate"
phases: [plan, execute, validate, report]

# Agent-only task (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_task('data_analysis')"
phases: [plan, execute, validate]

# Event-driven task
trigger_type: event_driven
event_pattern: "file_change:*.md"
phases: [detect, plan, execute, report]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase task | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in task | Mixing concerns | Use agent for identity, task for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Tasks are loaded by agents to extend capabilities
- **F3 INJECT**: Tasks can inject domain-specific knowledge
- **F5 CALL**: Tasks orchestrate tool usage across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

Tasks enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~18 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /generate | slash_command | 3-parallel-agent review | n04_task_generate |
| /retrieve | slash_command | adversarial verification | n04_task_retrieve |
| /analyze | agent_invoked | 9-section summarization | n04_task_analyze |
| /loop | slash_command | recurring cron schedule | n04_task_loop (future) |
| /stuck | slash
```