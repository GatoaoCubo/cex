---
id: n05_core
kind: core
pillar: P05
llm_function: TOOL
max_bytes: 4096
naming: n05_core_{{name}}.md + .yaml
core: true
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_core
domain: core
quality: 8.7
tags: [core, p05, evolve, pattern, overnight]
tldr: "Structured framework for automated refinement through iterative cycles with quality gates and feedback mechanisms"
when_to_use: "Systematic improvement of knowledge artifacts, workflow optimization, or model performance tuning"
keywords: [core, evolve, pattern, overnight, refinement, feedback, quality, automation]
feeds_kinds: [core]
density_score: 0.88
---

# Overnight Evolve Core

## Spec
```yaml
kind: core
pillar: P05
llm_function: TOOL
max_bytes: 4096
naming: n05_core_{{name}}.md + .yaml
core: true
```

## What It Is
The Overnight Evolve Core is a structured framework for automated refinement through iterative cycles with quality gates and feedback mechanisms. It provides the foundational architecture for continuous improvement of knowledge artifacts, workflow optimization, and model performance tuning. This core enables systematic enhancement without manual intervention, aligning with the principles of CEX's automated evolution patterns.

## Cross-Tool Map
| Tool/Provider | Feature | Notes |
|-------------------|-----------|-------|
| GitHub Actions | CI/CD pipelines | Automated refinement workflows |
| GitLab CI | Merge request pipelines | Quality gate enforcement |
| Azure DevOps | Pipeline stages | Multi-phase refinement |
| CircleCI | Job orchestration | Parallel refinement tasks |
| Jenkins | Pipeline scripting | Custom refinement logic |
| AWS CodePipeline | Continuous delivery | Artifact quality checks |
| Gitpod | Development environment | Isolated refinement sessions |
| Docker | Containerization | Encapsulated refinement processes |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| quality_floor | float | 8.5 | Higher floor = better quality vs resource usage |
| max_cycles | int | 10 | More cycles = better refinement vs computational cost |
| feedback_threshold | float | 0.8 | Higher threshold = stricter feedback vs improvement potential |
| parallelism | int | 4 | More parallelism = faster refinement vs resource contention |
| timeout_seconds | int | 3600 | Longer timeout = more thorough refinement vs system responsiveness |

## Integration Points
- **F2 BECOME**: Evolve cores are applied to knowledge artifacts for continuous improvement
- **F3 INJECT**: Refinement processes can inject domain-specific knowledge into workflows
- **F5 CALL**: Evolve cores orchestrate tool usage across refinement phases
- **Handoffs**: Refinement processes can be passed between nuclei for specialized execution
- **Memory**: Refinement can persist state between cycles via memory_scope

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| G01_quality_floor | quality < quality_floor | Stuck in suboptimal state |
| G02_feedback_threshold | feedback < feedback_threshold | Missed improvement opportunities |
| G03_max_cycles | cycles > max_cycles | Resource exhaustion risk |
| G30_parallelism | parallelism > system_capacity | Performance degradation |

## Production Reference: OpenClaude Evolve Cores
OpenClaude ships ~12 bundled evolve cores as battle-tested implementations:

| Core | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /refine | slash_command | 3-phase refinement | n05_core_refine |
| /optimize | slash
```
`


n05_phases.md
