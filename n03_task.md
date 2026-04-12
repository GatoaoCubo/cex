---
id: n03_task_aider_integration_patterns
kind: knowledge_card
type: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_task_aider_integration_patterns.md + .yaml
core: true
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: integration
quality: 9.1
tags: [integration, p04, reusable, kind-kc]
tldr: "Reusable capability with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about integration artifacts"
keywords: [integration, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [integration]
density_score: 8.9
---

# Task Integration Patterns

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
A task integration pattern is a reusable capability with structured phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. Task integrations are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task integration answers "what phases execute to achieve this capability?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Platform Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| GitHub Actions | `Workflow` / `Job` | Sequential execution with defined steps |
| GitLab CI/CD | `Pipeline` / `Stage` | Multi-step workflows with phase management |
| Jenkins | `Job` + `Stage` | Task definition with sequential/hierarchical execution |
| Azure DevOps | `Build` / `Release` | Structured computation with defined phases |
| CircleCI | `Workflow` with jobs | Explicit DAG execution with phase transitions |
| GitHub Copilot | `Code Action` | Multi-agent conversation patterns |
| Microsoft Azure | `Function` / `Pipeline` | Function orchestration with step management |

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
| slash_command | "/build", "/deploy" | User types exact command |
| keyword_match | "deploy", "test" | Natural language contains keywords |
| event_driven | commit, pull_request | System event occurs |
| agent_invoked | crew.use_task("deploy") | Programmatic call from agent |

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
slash_command: "/deploy"
phases: [discover, analyze, deploy]

# Agent-only task (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_task('ci_cd')"
phases: [setup, build, test, deploy]

# Event-driven task
trigger_type: event_driven
event_pattern: "push:main"
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

## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~18 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /build | slash_command | 3-parallel-agent review | p04_task_build |
| /test | slash_command | adversarial verification | p04_task_test |
| /deploy | agent_invoked | 9-section summarization | p04_task_deploy |
| /loop | slash_command | recurring cron schedule | p04_task_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter, not as code. The task body IS the prompt injected when the task triggers. This maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /build):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /test):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial task | Agent explicitly tries to BREAK the implementation | p04_task_test |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_task_build |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | p04_task_test |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_task_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_task_test |
```
