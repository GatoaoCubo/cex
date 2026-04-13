---
id: n02_task_system_prompt_review
kind: task
type: improvement
pillar: P05
llm_function: TOOL
max_bytes: 4096
naming: p05_task_system_prompt_review.md + .yaml
core: true
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_operations
domain: system_prompt
quality: 9.1
tags: [system_prompt, p05, improvement, task]
tldr: "Structured framework for evaluating and enhancing system prompts through multi-dimensional analysis"
when_to_use: "Auditing, refining, or benchmarking system prompts"
keywords: [system_prompt, review, improvement, analysis, evaluation]
feeds_kinds: [system_prompt]
density_score: 8.9
---

# System Prompt Review Task

## Spec
```yaml
kind: task
pillar: P05
llm_function: TOOL
max_bytes: 4096
naming: p05_task_{{name}}.md + .yaml
core: true
```

## What It Is
A system prompt review is a structured evaluation of a system prompt's effectiveness, alignment with objectives, and adherence to quality standards. It provides a framework for analyzing prompts through multiple dimensions, identifying gaps, and proposing enhancements.

## Cross-Platform Map
| Platform | Compatibility | Notes |
|---------|---------------|-------|
| Claude | ✅ Full | Native support for all prompt types |
| OpenAI | ✅ Partial | Limited to text-based prompts |
| Google | ✅ Partial | Requires specialized formatting |
| Anthropic | ✅ Full | Native support with enhanced features |
| Azure | ✅ Partial | Requires API-specific adaptations |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---------|------|---------|---------|
| scope | enum | "audit" | "audit" (comprehensive review) vs "quick" (surface-level check) |
| audience | string | "developers" | Target audience affects review focus |
| quality_floor | float | 8.5 | Higher floor = stricter evaluation |
| format | enum | "markdown" | "markdown" (structured output) vs "plain" (raw text) |

## Review Phases
| Phase | Purpose | Input | Output |
|------|--------|-------|--------|
| audit | Context analysis | prompt_content, environment | audit_report |
| benchmark | Quality assessment | audit_report, standards | benchmark_results |
| optimize | Enhancement suggestions | benchmark_results | optimization_plan |
| validate | Final verification | optimization_plan | validated_prompt |

## Trigger Scenarios
| Scenario | Trigger | Activation |
|---------|--------|-----------|
| New Prompt | `create` | User initiates prompt creation |
| Update | `update` | Prompt undergoes significant changes |
| Audit | `audit` | Scheduled or triggered review |
| Compliance | `compliance` | Regulatory or policy changes |

## Quality Assurance Metrics
| Metric | Description | Threshold |
|-------|-------------|-----------|
| Clarity | Understanding difficulty | ≤ 2.5 |
| Consistency | Internal coherence | ≥ 8.5 |
| Relevance | Task alignment | ≥ 9.0 |
| Efficiency | Execution speed | ≤ 3.0 |
| Adaptability | Context flexibility | ≥ 7.5 |

## Usage Examples
```yaml
# Full audit scenario
scope: audit
audience: developers
quality_floor: 9.0
format: markdown

# Quick check for compliance
scope: quick
audience: compliance
format: plain
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|-------------|----------|------------------|
| Single-phase review | Misses critical analysis stages | Use full audit workflow |
| No quality thresholds | Inconsistent evaluation | Define clear quality metrics |
| Overlooking context | Misaligned suggestions | Include environmental factors |
| Ignoring compliance | Legal risks | Add regulatory checks |

## Integration Points
- **F2 BECOME**: Reviews are triggered by system prompt creation
- **F3 INJECT**: Injects review findings into development workflows
- **F5 CALL**: Orchestrate multi-stage review processes
- **Handoffs**: Results passed to documentation or compliance teams
- **Memory**: Stores review history for future reference

## Industry References
| Standard | Description | Relevance |
|---------|-------------|----------|
| ISO 26514 | AI Management Systems | Framework for prompt governance |
| IEEE 7000 | AI System Standards | Technical requirements for prompt design |
| NIST AI Risk Management | Risk assessment framework | Compliance alignment |
| OpenAI Prompt Engineering Guide | Best practices | Implementation reference |

## Production Reference: OpenClaude System Prompt Reviews
OpenClaude ships ~12 pre-configured review templates:

| Template | Scope | Format | CEX Equivalent |
|---------|------|--------|----------------|
| /audit | Full | Markdown | p05_task_system_prompt_review |
| /quick | Basic | Plain | p05_task_quick_review |
| /compliance | Legal | JSON | p05_task_compliance_check |
| /optimize | Enhancement | YAML | p05_task_optimization |
| /benchmark | Quality | CSV | p05_task_benchmark |

**Key architectural insight**: System prompt reviews are defined as structured workflows with frontmatter metadata, not as code. The review process itself is the prompt injected when the review triggers. This maps directly to CEX's task-as-artifact model.

**Parallel review pattern** (from /audit):
- Phase 1: Analyze prompt structure and context
- Phase 2: Dispatch 3 reviewers concurrently, each with specialized focus
- Phase 3: Aggregate findings and propose enhancements
This pattern generalizes: any review can dispatch parallel sub-reviewers with typed foci.

**Analysis scratchpad pattern** (from /benchmark):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Review Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial review | Reviewer explicitly tries to BREAK the prompt | p05_task_adversarial_review |
| Parallel audit | Multiple focused reviewers analyze same prompt concurrently | p05_task_parallel_audit |
| Scratchpad review | <analysis> block for private reasoning, stripped from output | p05_task_scratchpad_review |
| Background extract | Runs silently after N turns, extracts persistent memories | p05_task_memory_extract |
| Rationalization counter | Lists excuses the reviewer will generate, pre-emptively counters | p05_task_rationalization_counter |
