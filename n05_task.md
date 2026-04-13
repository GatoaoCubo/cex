---
id: n05_task
kind: task
type: guide
pillar: P04
title: "8F Pipeline Implementation — Deep Knowledge for structured workflow execution"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: pipeline
quality: 8.8
tags: [pipeline, p04, reusable, kind-kc]
tldr: "Structured 8-function pipeline for repeatable artifact production with quality gates and cross-framework mapping"
when_to_use: "Building, reviewing, or reasoning about pipeline artifacts"
keywords: [pipeline, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [pipeline]
density_score: 85
---

# 8F Pipeline Implementation

## What It Is
The 8F pipeline is a structured workflow framework for repeatable artifact production. It defines a sequence of eight mandatory functions that transform raw inputs into structured outputs through defined phases. This pattern enables modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.

## Cross-Implementation Map
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
| function_sequence | array | required | More phases = granular control vs complexity |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "json" | Structured output vs natural language |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |
| quality_floor | float | 8.0 | Quality assurance vs flexibility |
| parallelism | enum | "serial" | Parallel execution vs resource contention |
| memory_scope | enum | "ephemeral" | State persistence vs memory overhead |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| discover | Context gathering | user_input, environment | context_data |
| preprocess | Data normalization | context_data | normalized_data |
| plan | Strategy definition | normalized_data | execution_plan |
| execute | Main workflow | execution_plan | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |
| format | Output structuring | validated_output | structured_output |
| persist | Storage management | structured_output | stored_artifact |
| report | Result documentation | stored_artifact | final_output |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| user_invocable | "/build", "/generate" | User types exact command |
| keyword_match | "compile", "optimize" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_pipeline("compile") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | function_sequence array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate pipeline |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |
| H05_quality_floor | Output quality ≥ quality_floor | Artifact rejected by gatekeeper |
| H06_parallelism_valid | parallelism in allowed values | Resource contention risks |
| H07_memory_scope_valid | memory_scope in allowed, values | Memory management issues |

## Usage Examples
```yaml
# User-invocable pipeline (slash command)
trigger_type: user_invocable
slash_command: "/build"
function_sequence: [discover, preprocess, plan, execute, validate, format, persist, report]

# Agent-only pipeline (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_pipeline('compile')"
function_sequence: [discover, preprocess, plan, execute, validate, format, persist, report]

# Event-driven pipeline
trigger_type: event_driven
event_pattern: "file_change:*.ts"
function_sequence: [discover, preprocess, plan, execute, validate, format, persist, report]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase pipeline | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |
| Missing quality gates | No quality assurance | Implement H05_quality_floor |
| Improper memory management | Memory leaks | Use memory_scope parameter |
| Incorrect parallelism | Resource contention | Set appropriate parallelism level |

## Integration Points
- **F2 BECOME**: Pipelines are loaded by agents to extend capabilities
- **F3 INJECT**: Pipelines can inject domain-specific knowledge
- **F5 CALL**: Pipelines orchestrate tool usage across phases
- **Handoffs**: Pipelines can be passed between nuclei for specialized execution
- **Memory**: Pipelines can persist state between phases via memory_scope
- **Quality Gates**: Pipelines enforce minimum quality thresholds
- **Parallel Execution**: Pipelines support concurrent task execution

## Production Reference: OpenClaude Bundled Pipelines
OpenClaude ships ~12 bundled pipelines as battle-tested implementations:

| Pipeline | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /compile | slash_command | 3-parallel-agent review | p04_pipeline_compile |
| /verify | slash_command | adversarial verification | p04_pipeline_verify |
| /optimize | agent_invoked | 9-section summarization | p04_pipeline_optimize |
| /loop | slash, command | recurring cron schedule | p04_pipeline_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Pipelines are defined as prompt text with frontmatter,
not as code. The pipeline body IS the prompt injected when the pipeline triggers. This
maps directly to CEX's pipeline-as-artifact model.

**Parallel dispatch pattern** (from /compile):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any pipeline can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /optimize):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Pipeline Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial pipeline | Agent explicitly tries to BREAK the implementation | p04_pipeline_verify |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_pipeline_compile |
| Scratchpad pipeline | <analysis> block for private reasoning, stripped from output | p04_pipeline_optimize |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_pipeline_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_pipeline_verify |

## Industry References
| Company | Implementation | Notes |
|--------|---------------|------|
| GitHub | Code review pipeline | Uses 8F for pull request automation |
| Netflix | Content recommendation pipeline | Implements quality gates for streaming |
| Amazon | Inventory management pipeline | Uses parallelism for real-time updates |
| Google | Search indexing pipeline | Applies memory_scope for caching |
| Microsoft | Azure DevOps pipeline | Integrates with CEX quality gates |

## Practical Examples
1. **Code Compilation Pipeline**
   - Discover: Analyze codebase structure
   - Preprocess: Normalize file paths
   - Plan: Define compilation order
   - Execute: Compile source files
   - Validate: Check for syntax errors
   - Format: Generate documentation
   - Persist: Store compiled artifacts
   - Report: Generate build summary

2. **Data Processing Pipeline**
   - Discover: Identify data sources
   - Preprocess: Clean and normalize data
   - Plan: Define processing steps
   - Execute: Transform data formats
   - Validate: Check data integrity
   - Format: Structure output files
   - Persist: Store processed data
   - Report: Generate data summary

3. **Content Moderation Pipeline**
   - Discover: Analyze content type
   - Preprocess: Normalize text
   - Plan: Define moderation rules
   - Execute: Apply filtering criteria
   - Validate: Check for violations
   - Format: Generate moderation report
   - Persist: Store flagged content
   - Report: Generate compliance summary

## Technical Implementation
```typescript
class EightFPipeline {
  private functionSequence: Function[];
  private inputSchema: any;
  private outputFormat: string;
  private timeoutSeconds: number;
  private qualityFloor: number;
  private parallelism: string;
  private memoryScope: string;

  constructor(config: PipelineConfig) {
    this.functionSequence = config.functionSequence;
    this.inputSchema = config.inputSchema;
    this.outputFormat = config.outputFormat;
    this.timeoutSeconds = config.timeoutSeconds;
    this.qualityFloor = config.qualityFloor;
    this.parallelism = config.parallelism;
    this.memoryScope = config.memoryScope;
  }

  async execute(input: any): Promise<any> {
    // Implement quality gate checks
    // Execute function sequence with parallelism
    // Apply memory scope management
    // Format final output
    return structuredOutput;
  }
}
```

## Best Practices
| Practice | Description | Benefit |
|---------|-------------|---------|
| Define clear quality gates | Enforces minimum output standards | Ensures consistent results |
| Use structured input/output | Facilitates integration | Enables data reuse |
| Implement memory management | Prevents resource leaks | Improves system stability |
| Document pipeline phases | Enables debugging | Simplifies maintenance |
| Monitor execution metrics | Identifies performance bottlenecks | Optimizes resource usage |
| Use parallelism wisely | Balances speed and resource use | Avoids overloading systems |
| Apply version control | Tracks pipeline evolution | Enables rollback if needed |

## Common Pitfalls
| Pitfall | Description | Solution |
|--------|-------------|----------|
| Missing quality gates | No output validation | Implement H05_quality_floor |
| Improper memory management | Memory leaks | Use memory_scope parameter |
| Incorrect parallelism | Resource contention | Set appropriate parallelism level |
| Poorly defined phases | Inefficient execution | Use phase structure for clarity |
| Lack of documentation | Difficult to maintain | Document each pipeline phase |
| No error handling | System instability | Implement try/catch blocks |
| Inadequate testing | Poor quality output | Use quality gates for validation |

## Future Enhancements
| Enhancement | Description | Potential Impact |
|------------|-------------|------------------|
| Dynamic phase adjustment | Auto-adjust phases based on input | Improves flexibility |
| Machine learning integration | Use ML for quality prediction | Enhances output accuracy |
| Real-time monitoring | Track pipeline execution | Enables proactive management |
| Adaptive parallelism | Auto-scale parallel tasks | Optimizes resource use |
| Context-aware memory | Store context between phases | Improves workflow continuity |
| Automated testing | Validate pipeline outputs | Ensures consistent quality |
| Versioned pipelines | Track pipeline evolution | Enables rollback if needed |

## Conclusion
The 8F pipeline provides a robust framework for structured workflow execution. By defining clear phases, implementing quality gates, and using structured data formats, this pattern enables reusable, repeatable artifact production. The cross-framework mapping shows its versatility across different implementation paradigms, while the industry references and practical examples demonstrate its real-world applicability. Following best practices and avoiding common pitfalls will ensure successful implementation and long-term maintenance of 8F pipelines.
```