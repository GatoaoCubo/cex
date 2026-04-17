---
id: p01_kc_prompt_template
kind: knowledge_card
type: kind
pillar: P03
title: "Prompt Template — Deep Knowledge for prompt_template"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: prompt_template
quality: 9.1
tags: [prompt_template, P03, CONSTRAIN, kind-kc]
tldr: "Reusable prompt mold with {{variables}} that generates concrete prompts when filled with runtime data"
when_to_use: "Building, reviewing, or reasoning about prompt_template artifacts"
keywords: [template, variables, prompt-mold]
feeds_kinds: [prompt_template]
density_score: null
aliases: ["prompt mold", "reusable prompt", "template prompt", "prompt with variables", "parameterized prompt"]
user_says: ["write a prompt template", "criar template de prompt", "make a reusable prompt", "I need a prompt with placeholders", "create a prompt I can use for different inputs"]
long_tails: ["I need a reusable prompt that works for different inputs", "create a prompt with variables I can fill in at runtime", "build a template that structures how the AI responds to any topic", "make a parameterized prompt for repeated use across domains"]
cross_provider:
  langchain: "ChatPromptTemplate / PromptTemplate"
  llamaindex: "Prompt templates in QueryEngine"
  crewai: "system_template / prompt_template in Agent config"
  dspy: "Signature class with typed fields"
  openai: "System/user message templates (app-level)"
  anthropic: "System/user message templates (app-level)"
  haystack: "PromptBuilder with Jinja2"
---

# Prompt Template

## Spec
```yaml
kind: prompt_template
pillar: P03
llm_function: CONSTRAIN
max_bytes: 8192
naming: p03_pt_{{topic}}.md
core: true
```

## What It Is
A prompt template is a reusable mold containing {{variable}} placeholders that, when filled with runtime data, produces a concrete prompt. It separates structure (how to ask) from content (what to ask about). It is NOT a user_prompt/action_prompt (which is already filled and ready to execute) nor a system_prompt (which defines identity, not task structure). Templates CONSTRAIN generation by fixing the prompt's shape.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ChatPromptTemplate` / `PromptTemplate` | `PromptTemplate.from_template("Tell me about {topic}")` |
| LlamaIndex | Prompt templates in `QueryEngine` / `ResponseSynthesizer` | Custom prompt templates override default generation behavior |
| CrewAI | `system_template` / `prompt_template` in Agent config | Agent-level prompt customization via template strings |
| DSPy | `Signature` class with typed fields | `class QA(dspy.Signature): question -> answer` is a template |
| Haystack | `PromptBuilder` component with Jinja2 | `PromptBuilder(template="Given {{docs}}, answer {{query}}")` |
| OpenAI | System/user message templates (app-level) | No native template — apps build templates above the API |
| Anthropic | System/user message templates (app-level) | No native template — apps build templates above the API |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| variables | list[str] | required | More vars = more flexible but harder to validate inputs |
| format | enum | "markdown" | Markdown = readable; JSON = parseable; Jinja2 = powerful |
| required_vars | list[str] | all | Marking optional vars = flexible but risk of empty sections |
| max_rendered_tokens | int | null | Limits final prompt size but may truncate long variable content |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Fill-in-the-blank | Simple variable substitution | `"Analyze {{product}} for {{market}}"` |
| Conditional sections | Optional content blocks | `{% if context %}Context: {{context}}{% endif %}` |
| Loop template | Process lists of items | `{% for item in items %}Evaluate: {{item}}\n{% endfor %}` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Hardcoding values that should be variables | Template becomes single-use, not reusable | Extract any domain-specific content into {{variables}} |
| Too many variables | Template becomes unreadable and fragile | Max 7 variables; group related data into structured objects |
| No default values for optional vars | Renders with empty holes, confusing the LLM | Provide sensible defaults or conditional sections |

## Integration Graph
```
[few_shot_example] --> [prompt_template] --> [action_prompt]
                            |
                    [constraint_spec, prompt_version]
```

## Decision Tree
- IF prompt is used more than once with different data THEN create prompt_template
- IF prompt is one-time with no variables THEN use action_prompt directly
- IF template needs conditional logic THEN use Jinja2 format
- IF template must be versioned for A/B testing THEN pair with prompt_version
- DEFAULT: Markdown format with fill-in-the-blank {{variables}}

## Quality Criteria
- GOOD: Clear variables, renders correctly with sample data, under 8192 bytes
- GREAT: Includes default values, variable type hints, and example rendered output
- FAIL: No variables (it's just a prompt); >7 variables without grouping; broken template syntax
