---
id: n03_task
kind: task
type: instruction
pillar: P04
title: "Task — Intent Resolution Benchmark Translation"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: translation
quality: 9.1
tags: [translation, p04, benchmark, task]
tldr: "Translate Portuguese intent resolution benchmark to English while preserving structure, metadata, and formatting"
when_to_use: "When translating benchmark artifacts between languages"
keywords: [translation, benchmark, metadata, formatting, structure]
feeds_kinds: [task]
density_score: null
---

# Task

## Spec
```yaml
kind: task
pillar: P04
llm_function: TRANSLATOR
max_bytes: 4096
naming: p04_task_{{name}}.md + .yaml
core: true
```

## What It Is
A task is a structured instruction for translating artifacts between languages while preserving metadata, structure, and formatting. It defines a specific workflow that can be executed repeatedly across different language contexts. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what steps execute to achieve this translation?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `TranslationChain` | Sequential execution with defined steps |
| LlamaIndex | `TranslationPipeline` | Multi-step workflows with phase management |
| CrewAI | `TranslationTask` | Task definition with sequential/hierarchical execution |
| DSPy | `dspy.TranslationModule` | Structured computation with defined phases |
| Haystack | `TranslationPipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `TranslationGroupChat` | Multi-agent conversation patterns |
| Microsoft Semantic Kernel | `TranslationPlan` | Function orchestration with step management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| source_lang | string | "pt" | Source language code vs flexibility |
| target_lang | string | "en" | Target language code vs flexibility |
| format_preservation | boolean | true | Strict formatting vs natural translation |
| metadata_preservation | boolean | true | Metadata retention vs translation accuracy |
| structure_preservation | boolean | true | Structural integrity vs natural language flow |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| analyze | Language detection | source_text | language_data |
| parse | Metadata extraction | source_text | metadata |
| translate | Core translation | source_text, metadata | translated_text |
| format | Output structuring | translated_text | formatted_output |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_language_detected | source_lang in supported languages | Translation failure |
| H02_metadata_extracted | metadata schema valid | Metadata loss |
| H03_translation_valid | target_lang in supported languages | Translation failure |
| H04_format_valid | format schema valid | Formatting errors |

## Usage Examples
```yaml
# Portuguese to English translation task
source_lang: pt
target_lang: en
format_preservation: true
metadata_preservation: true
structure_preservation: true
phases: [analyze, parse, translate, format]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| No language specification | Cannot determine translation | Specify source/target languages |
| Format relaxation | Loss of structural integrity | Preserve original formatting |
| Metadata omission | Loss of contextual information | Extract and preserve metadata |
| Manual translation | Inconsistent results | Use automated translation pipeline |

## Integration Points
- **F2 BECOME**: Tasks are loaded by agents to extend translation capabilities
- **F3 INJECT**: Tasks can inject language-specific knowledge
- **F5 CALL**: Tasks orchestrate translation across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

Tasks enable modular, reusable translation definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Translation Tasks
OpenClaude ships ~18 bundled translation tasks as battle-tested implementations:

| Task | Source | Target | Pattern |
|-------|---------|---------|----------------|
| /translate-pt-en | pt | en | 3-parallel-agent review |
| /translate-en-pt | en | pt | adversarial verification |
| /translate-pt-es | pt | es | 9-section summarization |
| /translate-es-pt | es | pt | recurring cron schedule |
| /translate-pt-fr | pt | fr | diagnostic investigation |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter,
not as code. The task body IS the prompt injected when the task triggers. This
maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /translate-pt-en):
- Phase 1: Identify language and structure
- Phase 2: Dispatch 3 agents concurrently, each with the full text + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /translate-pt-es):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial translation | Agent explicitly tries to BREAK the translation | /translate-pt-en |
| Parallel review | Multiple focused agents analyze same text concurrently | /translate-pt-es |
| Scratchpad translation | <analysis> block for private reasoning, stripped from output | /translate-pt-fr |
| Background extract | Runs silently after N turns, extracts persistent memories | /translate-pt-es |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | /translate-pt-en |
