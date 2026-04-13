---
id: n05_task
kind: task
type: improvement
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_task_n05.md + .yaml
core: true
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.0
tags: [task, p04, improvement, iteration, history]
tldr: "Structured approach to enhance iteration history documentation with cross-framework patterns, quality gates, and industry benchmarks"
when_to_use: "Improving iteration history artifacts for knowledge systems"
keywords: [task, iteration, history, documentation, quality, benchmark, structured]
feeds_kinds: [task]
density_score: 85
---

# Task: Improve Iteration History Documentation

## Current State
| Artifact | Quality | Lines | Issues |
|---------|--------|------|--------|
| iteration_history.md | 8.9 | 68 | - Missing structured data<br>- Limited industry references<br>- No quality gates |
| kc_skill.md | 9.1 | 125 | - Comprehensive structure<br>- Cross-framework mapping<br>- Anti-patterns |

## Target Improvements
| Aspect | Requirement | Benefit |
|-------|------------|--------|
| Structure | Match kc_skill.md format | Consistent documentation standards |
| Density | 80+ lines | Comprehensive coverage |
| Quality | 9.0+ | Peer-reviewed benchmarks |
| References | Industry examples | Practical implementation guidance |

## Structure & Format
```yaml
kind: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_task_{{name}}.md + .yaml
core: true
```

## Cross-Industry Patterns
| Framework | Pattern | CEX Equivalent |
|----------|--------|----------------|
| Git | Commit history | iteration_history.md |
| CI/CD | Pipeline logs | task_execution_log.md |
| Agile | Sprint retrospectives | iteration_review.md |
| DevOps | CI/CD pipelines | task_automation.md |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_structure_defined | Required sections missing | Non-compliant documentation |
| H02_references_valid | Industry examples missing | Limited practical value |
| H03_quality_metrics | No quality score | Cannot assess improvement |
| H04_format_correct | YAML frontmatter invalid | Cannot process artifact |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| audit | Document review | current_artifact | gap_analysis |
| plan | Improvement strategy | gap_analysis | improvement_plan |
| execute | Format implementation | improvement_plan | formatted_artifact |
| validate | Quality assessment | formatted_artifact | quality_report |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| /improve | "Enhance iteration history" | User request |
| /benchmark | "Compare with industry standards" | Quality assessment |
| /structure | "Format as skill documentation" | Style guide |
| /reference | "Add industry examples" | Practical guidance |

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| No structured data | Difficult to audit | Use tables and YAML |
| No industry references | Limited practical value | Add cross-framework examples |
| No quality gates | Cannot assess improvement | Define validation criteria |
| No execution plan | No clear improvement path | Create step-by-step guide |

## Integration Points
- **F2 BECOME**: Task artifacts are loaded by knowledge systems to extend documentation capabilities
- **F3 INJECT**: Tasks can inject structured iteration patterns
- **F5 CALL**: Tasks orchestrate documentation improvements across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

## Practical Examples
```yaml
# User request to improve iteration history
trigger_type: user_invocable
slash_command: "/improve"
phases: [audit, plan, execute, validate]

# Industry benchmark comparison
trigger_type: agent_invoked
invoke_pattern: "task.compare_benchmarks()"
phases: [load, analyze, report]

# Automated documentation improvement
trigger_type: event_driven
event_pattern: "file_change:iteration_history.md"
phases: [detect, audit, improve, validate]
```

## Industry References
| Reference | Description | CEX Equivalent |
|----------|------------|----------------|
| Git Commit History | Version control documentation | iteration_history.md |
| CI/CD Pipeline Logs | Automation execution tracking | task_execution_log.md |
| Agile Retrospectives | Iteration review patterns | iteration_review.md |
| DevOps CI/CD | Pipeline automation documentation | task_automation.md |
| OpenClaude Skill Patterns | Reusable capability documentation | kc_skill.md |

## Production Reference: OpenClaude Task Patterns
OpenClaude ships ~12 bundled task patterns as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /improve | slash_command | 3-phase documentation review | p04_task_improve |
| /benchmark | slash_command | Industry standard comparison | p03_task_benchmark |
| /structure | agent_invoked | Format as skill documentation | p04_task_structure |
| /reference | slash_command | Add industry examples | p04_task_reference |
| /automate | event_driven | Auto-improve on file change | p04_task_automate |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter, not as code. The task body IS the prompt injected when the task triggers. This maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /improve):
- Phase 1: Audit current documentation
- Phase 2: Dispatch 3 agents concurrently, each with the full audit + specialized focus
- Phase 3: Aggregate findings and implement improvements
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /benchmark):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Benchmark task | Compare with industry standards | p04_task_benchmark |
| Parallel review | Multiple focused agents analyze same document concurrently | p04_task_improve |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | p04_task_reference |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_task_automate |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_task_validate |
```
```