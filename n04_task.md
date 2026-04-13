---
id: n04_task
kind: task
type: guide
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: n04_task_review.md + .yaml
core: true
---

# System Prompt Review Task

## Overview
This task guides the improvement of system prompts to achieve 9.0+ quality. The review process follows the structured format of skill artifacts (kc_skill.md) with emphasis on structured data, industry references, and practical examples.

## Structure & Format
Follow the skill artifact format with these elements:
- ## Headers for each section
- Comparison tables for framework mappings
- Bullet lists for key parameters
- Structured data for quality gates
- Minimum 80 lines of substantive content

| Format Element | Requirement | Example |
|----------------|-------------|---------|
| YAML Frontmatter | Must remain intact | Preserved from original |
| Section Headers | ## for major sections | ## Quality Gates |
| Tables | Minimum 1 per section | Framework Mapping Table |
| Bullet Lists | Key parameters | Key Parameters section |
| Structured Data | JSON-like format | Quality Gates table |

## Industry References
Adhere to these industry standards and frameworks:

| Standard | Description | Example |
|---------|-------------|---------|
| ISO/IEC 23894 | AI Management Standard | Framework for AI system governance |
| LangChain | Sequential execution framework | Chain/RunnableSequence pattern |
| LlamaIndex | Multi-step workflows | QueryPipeline/IngestionPipeline |
| CrewAI | Task definition framework | Task + Process hierarchy |
| DSPy | Structured computation | dspy.Module.forward() |
| Haystack | Explicit DAG execution | Pipeline with nodes |
| AutoGen | Multi-agent conversation | GroupChat workflow |
| Microsoft Semantic Kernel | Function orchestration | Plan/KernelFunction |

## Practical Examples
### Example 1: Structure Mapping
```markdown
## Framework Map
| Framework | CEX Equivalent | Notes |
|-----------|----------------|-------|
| LangChain | P04_skill | Sequential execution |
| CrewAI | P04_task | Task definition |
| DSPy | P04_pipeline | Structured computation |
```

### Example 2: Quality Gates
```markdown
## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate skill |
```

## Quality Gates
| Gate | Validation | Failure Impact | Remediation |
|------|------------|----------------|------------|
| H01_format_valid | YAML frontmatter intact | Task rejection | Preserve original metadata |
| H02_structure_complete | 8+ sections with tables | Content sparse | Add framework mapping |
| H03_industry_references | 3+ standards cited | Lack of context | Add ISO/IEC 23894 |
| H04_practical_examples | 2+ code examples | No implementation | Add LangChain pattern |
| H05_quality_score | 9.0+ peer review | Rejection | Add 3 peer reviews |

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|----------|------------------|
| Sparse content | No structured data | Add framework mapping table |
| No industry references | Lack of context | Cite ISO/IEC 23894 |
| Single example | No practical implementation | Add LangChain code snippet |
| No quality gates | No validation criteria | Define 5+ quality checks |
| Missing frontmatter | Task rejection | Preserve original metadata |

## Integration Points
- **F2 BECOME**: Task artifacts are loaded by agents to extend capabilities
- **F3 INJECT**: Tasks can inject domain-specific knowledge
- **F5 CALL**: Tasks orchestrate tool usage across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

## Production Reference
Real-world implementations include:

| Implementation | Trigger | Pattern | CEX Equivalent |
|----------------|--------|---------|----------------|
| /simplify | slash_command | 3-agent review | P04_task_review |
| /verify | slash_command | adversarial verification | P04_task_audit |
| /compact | agent_invoked | 9-section summarization | P04_task_summary |
| /loop | slash_command | recurring cron schedule | P04_task_scheduler (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter, not as code. The task body IS the prompt injected when the task triggers. This maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /simplify):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /compact):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial task | Agent explicitly tries to BREAK the implementation | P04_task_audit |
| Parallel review | Multiple focused agents analyze same diff concurrently | P04_task_review |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | P04_task_summary |
| Background extract | Runs silently after N turns, extracts persistent memories | P04_task_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | P04_task_verify |
