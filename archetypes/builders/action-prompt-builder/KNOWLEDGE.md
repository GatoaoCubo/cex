---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for action_prompt production
sources: OpenAI, Anthropic, LangChain, DSPy, prompt engineering literature
---

# Domain Knowledge: action_prompt

## Foundational Concept
Action prompts are task-focused messages injected at runtime that tell an LLM WHAT
to do with specific input and WHAT output to produce. They sit between system_prompts
(identity) and raw user messages (unstructured). The concept draws from function
signatures (typed I/O), API contracts (request/response), and prompt engineering
best practices (specificity, structure, validation).

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| OpenAI user messages | Task with context | Direct: our action_prompt |
| Anthropic Human turn | Task injection | Direct: Context + Input + Execution |
| LangChain HumanMessagePromptTemplate | Typed task message | Informs: input_required field |
| DSPy Signature | Typed I/O contract | Informs: input_required + output_expected |
| Function calling (OpenAI/Anthropic) | Structured I/O | Informs: structured output section |

## Key Patterns
- Verb-first action: "Extract metrics from log" not "Log metric extraction"
- Typed input: specify data types ("list[string]", "JSON object") not vague ("some data")
- Structured output: define format (JSON, table, markdown) with example
- Edge case enumeration: >= 2 known failure modes with handling guidance
- Validation criteria: verifiable checks, not subjective ("output is good")
- Purpose statement: WHY this action exists, not just WHAT it does
- No identity mixing: action_prompt assumes agent already has identity from system_prompt
- Concise execution: 3-7 steps max, not a detailed runbook (that is instruction)

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| edge_cases | Explicit failure mode documentation | DSPy assertions |
| purpose | Links prompt to business reason | No direct equivalent |
| timeout | Runtime constraint for long tasks | API timeout parameter |
| constraints | Explicit exclusion list | Constitutional AI deny-list |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT action_prompt |
|------|------------|---------------------------|
| system_prompt | Agent identity and rules | Defines WHO, not WHAT to do now |
| instruction | Step-by-step recipe with prerequisites | Detailed recipe, not concise task |
| prompt_template | Reusable template with {{vars}} | Template mechanics, not specific task |
| user_prompt | Raw unstructured human message | No typed I/O contract |
| chain | Sequence of prompts (A->B->C) | Multiple prompts, not single action |

## References
- OpenAI: Chat Completions API best practices
- Anthropic: Prompt engineering guide
- DSPy: Signatures and typed I/O
- Zamfirescu-Pereira et al. 2023: Why Johnny Can't Prompt
