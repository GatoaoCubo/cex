---
id: n02_task_git_workflow_for_agents
kind: task
type: guide
pillar: P04
title: "Git Workflow for Agents — Structured, Reusable, and Scalable"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: git
quality: 9.1
tags: [git, p04, reusable, task-guide]
tldr: "Structured Git workflow for agent-based development with phase-driven execution, trigger conditions, and lifecycle management"
when_to_use: "Building, reviewing, or reasoning about Git workflow artifacts"
keywords: [git, phases, trigger, reusable, workflow, lifecycle]
feeds_kinds: [git]
density_score: 89
---

# Git Workflow for Agents

## What It Is
A Git workflow for agents is a structured, reusable process for managing code changes in agent-based development. It defines a specific workflow that can be executed repeatedly across different contexts. Git workflows are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A Git workflow answers "what phases execute to achieve this capability?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| Git | `branch`, `merge`, `rebase` | Core operations for version control |
| GitHub | `pull request`, `merge queue` | Workflow automation for code reviews |
| GitLab | `merge request`, `CI/CD pipeline` | Integrated development lifecycle |
| Azure DevOps | `branch policy`, `pull request` | Enterprise-grade workflow management |
| Bitbucket | `branch`, `pull request`, `merge` | Distributed version control system |
| GitKraken | `visual workflow`, `branching strategy` | GUI-based workflow visualization |
| Gitpod | `workspace`, `branch isolation` | Development environment management |

## Key Concepts
| Concept | Description | Example |
|--------|------------|--------|
| Branching Strategy | Pattern for creating and managing branches | Git Flow, GitHub Flow, Trunk-Based Development |
| Merge Strategy | Method for merging changes | Fast-Forward, Rebase, Merge |
| Code Review | Process for validating changes | Pull Request, Code Review, Peer Review |
| CI/CD Integration | Automated testing and deployment | GitHub Actions, GitLab CI, Jenkins |
| Conflict Resolution | Handling merge conflicts | Manual resolution, automated tools |
| Workflow Automation | Scripting workflow steps | GitHub Actions, GitLab CI, Jenkins |

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
| slash_command | "/commit", "/deploy" | User types exact command |
| keyword_match | "debug", "optimize" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_skill("analyze") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate skill |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable workflow (slash command)
trigger_type: user_invocable
slash_command: "/commit"
phases: [discover, analyze, report]

# Agent-only workflow (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_workflow('code_review')"
phases: [load, transform, analyze, export]

# Event-driven workflow
trigger_type: event_driven
event_pattern: "file_change:*.py"
phases: [detect, lint, test, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase workflow | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in workflow | Mixing concerns | Use agent for identity, workflow for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Workflows are loaded by agents to extend capabilities
- **F3 INJECT**: Workflows can inject domain-specific knowledge
- **F5 CALL**: Workflows orchestrate tool usage across phases
- **Handoffs**: Workflows can be passed between nuclei for specialized execution
- **Memory**: Workflows can persist state between phases via memory_scope

## Production Reference: OpenClaude Bundled Workflows
OpenClaude ships ~18 bundled workflows as battle-tested implementations:

| Workflow | Trigger | Pattern | CEX Equivalent |
|-------|-------|---------|----------------|
| /simplify | slash_command | 3-parallel-agent review | p04_workflow_simplify |
| /verify | slash_command | adversarial verification | p04_workflow_verify |
| /compact | agent_invoked | 9-section summarization | p04_workflow_compact |
| /loop | slash_command | recurring cron schedule | p04_workflow_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Workflows are defined as prompt text with frontmatter,
not as code. The workflow body IS the prompt injected when the workflow triggers. This
maps directly to CEX's workflow-as-artifact model.

**Parallel dispatch pattern** (from /simplify):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any workflow can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /compact):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Workflow Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial workflow | Agent explicitly tries to BREAK the implementation | p04_workflow_verify |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_workflow_simplify |
| Scratchpad workflow | <analysis> block for private reasoning, stripped from output | p04_workflow_compact |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_workflow_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_workflow_verify |
```
```