---
id: n06_task
kind: task
type: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_task_{{name}}.md + .yaml
core: true
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.1
tags: [task, p04, reusable, kind-kc]
tldr: "Structured workflow for optimizing agent embedding engineers with phase-based execution, trigger conditions, and quality gates"
when_to_use: "Building, reviewing, or reasoning about task artifacts"
keywords: [task, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [task]
density_score: 92
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
A task is a structured workflow for optimizing agent embedding engineers with phase-based execution, trigger conditions, and quality gates. It defines a specific process that can be executed repeatedly across different contexts. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what phases execute to achieve this optimization?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Platform Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `Task` / `RunnableSequence` | Sequential execution with defined steps |
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
| timeout_seconds | int | 30,000 | Execution time limit vs complex workflows |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| discover | Context gathering | user_input, environment | context_data |
| configure | Parameter setup | context_data, user_preferences | configuration |
| execute | Main workflow | configuration, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| slash_command | "/optimize", "/refine" | User types exact command |
| keyword_match | "debug", "optimize" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_task("embedding") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate task |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable task (slash command)
trigger_type: user_invocable
slash_command: "/optimize"
phases: [discover, analyze, refine]

# Agent-only task (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_task('embedding')"
phases: [load, transform, analyze, export]

# Event-driven task
trigger_type: event_driven
event_pattern: "file_change:*.md"
phases: [detect, lint, test, notify]
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

## Industry References
| Framework | Description | Example |
|----------|-------------|--------|
| LangChain | Sequential execution with defined steps | `RunnableSequence` |
| LlamaIndex | Multi-step workflows with phase management | `QueryPipeline` |
| CrewAI | Task definition with sequential/hierarchical execution | `Task` + `Process` |
| DSPy | Structured computation with defined phases | `dspy.Module.forward()` |
| Haystack | Explicit DAG execution with phase transitions | `Pipeline` with nodes |
| AutoGen | Multi-agent conversation patterns | `GroupChat` workflow |
| Microsoft Semantic Kernel | Function orchestration with step management | `Plan` / `KernelFunction` |

## Practical Examples
1. **Code Optimization Task**
   - Trigger: `/optimize`
   - Phases: discover (analyze codebase), configure (set optimization parameters), execute (apply refactorings), validate (check code quality)
   - Tools: linter, formatter, static analyzer

2. **Knowledge Refinement Task**
   - Trigger: `/refine`
   - Phases: discover (identify gaps), configure (set refinement criteria), execute (apply knowledge updates), validate (check consistency)
   - Tools: knowledge graph, semantic search, validation framework

3. **Data Pipeline Task**
   - Trigger: `/pipeline`
   - Phases: discover (identify data sources), configure (set pipeline parameters), execute (process data), validate (check data quality)
   - Tools: data loader, transformer, validator

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Parallel optimization | Multiple focused agents analyze same codebase concurrently | Code refactoring with 3 parallel agents |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | Knowledge refinement with private drafting space |
| Background extraction | Runs silently after N turns, extracts persistent memories | Memory extraction for long-running tasks |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | Task validation with adversarial checks |
| Adaptive workflow | Dynamically adjusts phases based on intermediate results | Self-optimizing code refactoring pipeline |

## Quality Metrics
| Metric | Description | Target |
|-------|-------------|--------|
| Phase Completeness | Percentage of phases executed successfully | 100% |
| Trigger Accuracy | Percentage of triggers correctly identified | 95% |
| Input Validation | Percentage of invalid inputs rejected | 100% |
| Output Consistency | Percentage of outputs matching expected format | 98% |
| Error Recovery | Percentage of errors resolved automatically | 90% |

## Performance Benchmarks
| Benchmark | Current | Target |
|----------|--------|--------|
| Execution Time | 12s | 8s |
| Memory Usage | 256MB | 128MB |
| Throughput | 150 tasks/hour | 300 tasks/hour |
| Error Rate | 2% | 0.5% |
| Resource Utilization | 75% | 50% |

## Optimization Strategies
1. **Phase Parallelization**: Execute non-dependent phases concurrently to reduce execution time
2. **Dynamic Parameter Adjustment**: Automatically adjust parameters based on intermediate results
3. **Adaptive Trigger Detection**: Improve trigger recognition using machine learning models
4. **Memory Optimization**: Reduce memory usage by implementing efficient data structures
5. **Error Prediction**: Predict potential errors using historical data and prevent them proactively

## Future Enhancements
1. **AI-Driven Optimization**: Use machine learning to automatically suggest optimal parameters
2. **Self-Healing Tasks**: Automatically detect and fix errors during execution
3. **Contextual Awareness**: Improve trigger detection using contextual information
4. **Performance Monitoring**: Add real-time performance metrics and alerts
5. **User Feedback Loop**: Incorporate user feedback to continuously improve task quality

## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~12 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /optimize | slash_command | 3-parallel-agent review | p04_task_optimize |
| /refine | slash_command | adversarial verification | p04_task_refine |
| /pipeline | agent_invoked | 9-section summarization | p04_task_pipeline |
| /loop | slash_command | recurring cron schedule | p04_task_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |
```