---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for system_prompt production
sources: OpenAI, Anthropic, Google, LangChain, constitutional AI literature
---

# Domain Knowledge: system_prompt

## Foundational Concept
System prompts are the first message in a conversation that defines the LLM's identity,
capabilities, constraints, and response format. Every major LLM provider (OpenAI, Anthropic,
Google) supports a system/developer message that is processed before user input. The system
prompt is the primary mechanism for turning a general-purpose LLM into a specialist.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| OpenAI system message | Identity + instructions + format | Direct: our system_prompt |
| Anthropic system prompt | Persona + rules + safety | Direct: identity + rules + constraints |
| Google system instruction | Role + behavior + output format | Direct: all 4 body sections |
| LangChain SystemMessagePromptTemplate | Template for system messages | Our prompt_template wraps this |
| Constitutional AI (Bai 2022) | Self-critique + revision rules | Informs our ALWAYS/NEVER pattern |

## Key Patterns
- Dense identity: 2-4 sentences establishing WHO, not paragraphs of context
- ALWAYS/NEVER rules: binary constraints are more reliable than soft guidance
- Knowledge boundary: explicit "I know X, I do NOT know Y" prevents hallucination
- Output format section: LLMs follow format instructions better in system prompt than user prompt
- Boundary statement: "I do NOT build X" prevents scope drift at conversation start
- Numbered rules: LLMs follow numbered lists more reliably than prose
- No task mixing: system_prompt defines IDENTITY, action_prompt defines TASK

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| target_agent | Links prompt to specific agent identity | OpenAI "name" parameter |
| rules_count | Integrity check: count matches body | No industry equivalent |
| knowledge_boundary | Explicit scope to prevent hallucination | Anthropic guidelines |
| safety_level | Graduated constraint strictness | Constitutional AI levels |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT system_prompt |
|------|------------|---------------------------|
| action_prompt | Task-focused prompt with input/output | Task execution, not identity |
| instruction | Step-by-step operational recipe | Procedural, not persona |
| prompt_template | Reusable template with {{vars}} | Template mechanics, not identity |
| user_prompt | One-time task from human/orchestrator | Ephemeral task, not persistent identity |
| mental_model | Agent routing/decision map | Design-time blueprint, not runtime prompt |

## References
- OpenAI: Chat Completions API — system message
- Anthropic: System prompts guide
- Bai et al. 2022: Constitutional AI
- LangChain: SystemMessagePromptTemplate docs
