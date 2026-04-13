---
id: n01_task
kind: task
type: improvement
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_task_n01.md + .yaml
core: true
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.0
tags: [task, p04, improvement, artifact]
tldr: "Structured task improvement framework with quality gates, phase analysis, and cross-framework mapping"
when_to_use: "Artifact refinement, quality assurance, or knowledge system enhancement"
keywords: [task, phases, trigger, improvement, lifecycle, quality]
feeds_kinds: [task]
density_score: 0.92
---

# Task Improvement Framework

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
A task is a structured unit of work with defined phases, trigger conditions, and quality assurance mechanisms. It defines a specific workflow that can be executed repeatedly across different contexts. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what phases execute to achieve this work?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Platform Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` | Sequential execution with defined steps |
| LlamaIndex | `QueryPipeline` | Multi-step workflows with phase management |
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
| archive | Long-term storage | validated_output, metadata | archived_artifact |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| slash_command | "/optimize", "/analyze" | User types exact command |
| keyword_match | "debug", "benchmark" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_task("data_analysis") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate task |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |


## Industry References
| Standard | Organization | Description |
|---------|-------------|-------------|
| ISO/IEC 23894 | ISO | Reference architecture for AI systems |
| IEEE P7003-2021 | IEEE | Standard for AI system quality assurance |
| NIST AI Risk Management Framework | NIST | Guidelines for AI system governance |
| GDPR | EU | Data protection regulations impacting task execution |

## Practical Examples
1. **Code Optimization Task**  
   - Trigger: `/optimize`  
   - Phases: Code analysis → Performance benchmark → Code refactoring  
   - Tools: Linter, Profiler, Code formatter  

2. **Data Analysis Task**  
   - Trigger: `crew.use_task('data_analysis')`  
   - Phases: Data loading → Data cleaning → Statistical analysis  
   - Tools: Pandas, NumPy, Visualization libraries  

3. **Documentation Task**  
   - Trigger: Event-driven (file change)  
   - Phases: Content discovery → Structure analysis → Documentation generation  
   - Tools: Markdown processor, API explorer, Version control  

## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~15 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /optimize | slash_command | 3-parallel-agent review | p04_task_optimize |
| /benchmark | slash_command | adversarial verification | p04_task_benchmark |
| /summarize | agent_invoked | 9-section summarization | p04_task_summarize |
| /monitor | slash_command | recurring cron schedule | p04_task_monitor (future) |
| /diagnose | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter, not as code. The task body IS the prompt injected when the task triggers. This maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /optimize):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /summarize):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial task | Agent explicitly tries to BREAK the implementation | p04_task_benchmark |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_task_optimize |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | p04_task_summarize |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_task_monitor |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_task_benchmark |
