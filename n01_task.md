---
id: n01_task
kind: task
type: task
pillar: P01
title: "Translation Task - LLM Judge Template"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_translator
domain: translation
quality: 8.5
tags: [translation, p01, task, template]
tldr: "Translate Portuguese content to English while preserving structure, tables, and formatting"
when_to_use: "When translating content between languages while maintaining technical structure"
keywords: [translation, structure, formatting, template, task]
feeds_kinds: [task]
density_score: null
---

# Translation Task - LLM Judge Template

## Spec
```yaml
kind: task
pillar: P01
llm_function: TOOL
max_bytes: 4096
naming: p01_task_{{name}}.md + .yaml
core: true
```

## What It Is
This task defines a structured approach to translating content between languages while preserving technical structure, tables, and formatting. It ensures that all Portuguese text is converted to English, with special attention to maintaining the original document's organization and presentation.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `TranslationChain` | Sequential translation with format preservation |
| LlamaIndex | `TranslationPipeline` | Multi-step translation with structure retention |
| CrewAI | `TranslationTask` | Task definition with format-aware execution |
| DSPy | `dspy.TranslationModule` method | Structured translation with format validation |
| Haystack | `TranslationPipeline` with nodes | Explicit format preservation during translation |
| AutoGen | `TranslationGroupChat` workflow | Multi-agent translation patterns |
| Microsoft Semantic Kernel | `TranslationPlan` / `KernelFunction` | Function orchestration with format management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| source_language | string | "pt" | Language to translate from |
| target_language | string | "en" | Language to translate to |
| preserve_format | boolean | true | Maintain original structure vs. flexibility |
| format_rules | object | {} | Custom formatting rules vs. standard |
| timeout_seconds | int | 300 | Execution time limit vs. complex formats |

## Format Preservation Rules
| Rule | Purpose | Input | Output |
|-------|---------|-------|--------|
| frontmatter_translation | Translate metadata | Portuguese frontmatter | English frontmatter |
| structure_preservation | Maintain document hierarchy | Original sections | Translated sections |
| table_formatting | Preserve table structure | Portuguese tables | English tables |
| code_block_retention | Keep code formatting | Original code blocks | Translated code blocks |
| list_preservation | Maintain list structure | Portuguese lists | English lists |

## Translation Patterns
| Pattern | Description | Example |
|---------|-------------|---------|
| Frontmatter Translation | Translate metadata while preserving structure | Translate title, description, tags |
| Structure Preservation | Maintain document hierarchy during translation | Keep section headings and subheadings |
| Table Formatting | Preserve table structure and alignment | Maintain column widths and alignment |
| Code Block Retention | Keep code formatting and syntax | Preserve indentation and syntax highlighting |
| List Preservation | Maintain list structure and numbering | Preserve bullet points and numbering |

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Full-text translation | Loses structure and formatting | Use format-preserving translation |
| Language detection | May misidentify source language | Specify source language explicitly |
| Format conversion | Changes document structure | Use format-preserving translation |
| Inline translation | Loses document organization | Use structured translation approach |
| No format rules | May produce inconsistent results | Define explicit format rules |

## Integration Points
- **F2 BECOME**: Translation tasks are loaded by agents to extend capabilities
- **F3 INJECT**: Translation can inject language-specific knowledge
- **F5 CALL**: Translation orchestrates tool usage across phases
- **Handoffs**: Translation tasks can be passed between nuclei for specialized execution
- **Memory**: Translation can persist state between phases via memory_scope

Translation tasks enable modular, reusable format-preserving translation that bridges the gap between simple content translation and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Translation Tasks
OpenClaude ships ~12 bundled translation tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /translate | slash_command | 3-parallel-agent review | p01_task_translate |
| /verify | slash_command | adversarial verification | p01_task_verify |
| /compact | agent_invoked | 9-section summarization | p01_task_compact |
| /loop | slash_command | recurring cron schedule | p01_task_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Translation tasks are defined as prompt text with frontmatter, not as code. The task body IS the prompt injected when the task triggers. This maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /translate):
- Phase 1: Identify translation scope (document structure)
- Phase 2: Dispatch 3 agents concurrently, each with the full document + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any translation task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /compact):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Translation Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial translation | Agent explicitly tries to BREAK the implementation | p01_task_verify |
| Parallel review | Multiple focused agents analyze same document concurrently | p01_task_translate |
| Scratchpad translation | <analysis> block for private reasoning, stripped from output | p01_task_compact |
| Background extract | Runs silently after N turns, extracts persistent memories | p01_task_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p01_task_verify |
