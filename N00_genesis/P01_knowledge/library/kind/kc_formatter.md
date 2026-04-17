---
id: p01_kc_formatter
kind: knowledge_card
type: kind
pillar: P01
title: "Formatter — Deep Knowledge for formatter"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: formatter
quality: 9.1
tags: [formatter, P05, GOVERN, kind-kc, output]
tldr: "Post-generation structural transformer that converts raw LLM output into a target format (Markdown, JSON, YAML, HTML) without extracting semantic data"
when_to_use: "Building, reviewing, or reasoning about formatter artifacts"
keywords: [formatter, markdown, json, yaml, output-transform]
feeds_kinds: [formatter]
density_score: null
---

# Formatter

## Spec
```yaml
kind: formatter
pillar: P05
llm_function: GOVERN
max_bytes: 4096
naming: p05_fmt_{{format}}.md
core: false
```

## What It Is
A formatter is a post-generation structural transformer that converts raw LLM text output into a target format (Markdown, JSON, YAML, HTML, plain text). It applies structural rules: headings, indentation, key ordering, escaping, line wrapping. Its boundary is pure format transformation — it does NOT extract semantic data from text (that is the parser's job) and does NOT define what format the LLM should generate in the first place (that is response_format's job in P05).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | StrOutputParser (trivial), custom transform step | Post-chain Runnable transform |
| LlamaIndex | ResponseSynthesizer with custom formatter | Applied after synthesis step |
| CrewAI | Callback or post_action transform | No native formatter kind |
| DSPy | OutputField with format= hint | Hint-based; not strict programmatic transform |
| Haystack | OutputAdapter component | Maps component output format to next input |
| OpenAI | n/a (prompt-driven format) | Format defined in system prompt |
| Anthropic | n/a (prompt-driven format) | Format defined in system prompt |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| target_format | str | markdown | json / yaml / html / md / plain |
| preserve_structure | bool | true | False = flatten; True = preserve nesting |
| escape_special | bool | true | Required for JSON/YAML correctness |
| trim_whitespace | bool | true | Avoids blank line artifacts in output |
| max_line_length | int | null | Enforces hard wrap for terminal output |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Markdown to JSON | API response normalization | Convert agent report text to structured JSON |
| JSON pretty-print | Human-readable logs and debug | json.dumps(data, indent=2, sort_keys=True) |
| YAML serializer | Config file generation from agent output | yaml.dump(data, default_flow_style=False) |
| HTML sanitize + format | Safe web rendering of agent output | bleach.clean() + html.prettify() |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Formatter that extracts semantic fields | Conflates format transform with data parsing | Use parser for extraction; formatter for shape |
| Formatter applied in LLM prompt | Prompt bloat; inconsistent LLM compliance | Apply programmatically post-generation |
| No escape for special characters | JSON or YAML parse failure downstream | Always escape in JSON/YAML formatters |
| Chaining multiple formatters | Order-dependent fragility; hard to debug | Single formatter with a clear target_format |

## Integration Graph
```
[raw_llm_output_str] --> [formatter] --> [formatted_output_str]
                              |
                    [target_format, escape, trim]
                              |
                    feeds --> [delivery / storage / display]
```

## Decision Tree
- IF need to extract semantic fields from output THEN use parser
- IF need to define what format LLM generates THEN use response_format
- IF need to validate output correctness or safety THEN use output_validator (P05)
- DEFAULT: formatter for any structural post-processing of raw LLM text output

## Quality Criteria
- GOOD: target_format declared, escaping correct, handles empty or null input
- GREAT: format-specific edge cases handled (JSON null, YAML multiline str, HTML entities), round-trip safe
- FAIL: modifies semantic content values, used as parser substitute, no escape logic for target format
