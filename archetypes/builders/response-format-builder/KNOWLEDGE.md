---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for response_format production
sources: [OpenAI JSON mode, Anthropic structured output, Instructor, Outlines, CEX _schema.yaml]
---

# Domain Knowledge: response_format

## Foundational Concepts
Response formats originate from structured output research in LLM systems.
Key insight: LLMs follow format instructions better when given explicit structure with examples.
In CEX: response_format is injected in the prompt so the LLM knows HOW to structure its output before generating.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| OpenAI JSON mode | Force JSON output via API parameter | format_type: json |
| Anthropic tool_use | Structured output via tool schema | Sections with typed fields |
| Instructor (Python) | Pydantic models as output schema | Field-level type constraints |
| Outlines | Regex-guided generation for format | Grammar-level (P06, not P05) |
| LangChain OutputParser | Parse LLM output into structured data | Parser (P05, downstream) |

## Key Principles
- response_format is GUIDANCE, not enforcement (LLM may deviate)
- Example output is the most effective format instruction (show, don't just tell)
- Fewer sections = higher compliance (LLMs struggle with 10+ sections)
- JSON format has highest compliance rate (LLMs trained on JSON)
- Markdown format is best for human-readable output
- injection_point matters: system_prompt for persistent, user_message for per-request
- Sections should be in logical order (LLMs generate sequentially)
- Field names should be descriptive (LLM uses names as semantic cues)

## The P05/P06 Boundary (critical distinction)
| Aspect | response_format (P05) | validation_schema (P06) |
|--------|----------------------|------------------------|
| Who sees it? | LLM (injected in prompt) | System only (post-generation) |
| When applied? | Before/during generation | After generation |
| Enforcement | Soft (LLM guidance) | Hard (system enforcement) |
| Language | Natural language + examples | Formal constraints (regex, enum) |

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| injection_point | Specifies WHERE in the prompt to inject | OpenAI: response_format param |
| sections | Ordered output structure | Instructor: Pydantic field order |
| composable | Enables format combination | No direct equivalent |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| validation_schema (P06) | System ENFORCES output structure post-generation | Invisible to LLM |
| parser (P05) | EXTRACTS data from existing output | Works on already-generated output |
| formatter (P05) | TRANSFORMS output between formats | Post-generation transformation |
| grammar (P06) | CONSTRAINS decoder tokens during generation | Operates at token level, not semantic |

## References
- OpenAI JSON mode: https://platform.openai.com/docs/guides/structured-outputs
- Instructor: https://python.useinstructor.com/
- Outlines: https://github.com/outlines-dev/outlines
- Anthropic tool use: https://docs.anthropic.com/en/docs/build-with-claude/tool-use
