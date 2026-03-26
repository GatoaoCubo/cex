---
pillar: P12
llm_function: COLLABORATE
purpose: Crew role, handoff contracts, and inter-builder coordination
---

# Collaboration: few-shot-example-builder

## My Role
FEW-SHOT EXAMPLE CRAFTER.
I answer: "what input/output pair best teaches this format?"
I do NOT evaluate quality (golden_test), do NOT test assertions (unit_eval).

## Prompt Engineering Crew

| Builder | Role | Answers |
|---------|------|---------|
| few-shot-example-builder | Format teaching via input/output pairs | "What shows this format?" |
| prompt-template-builder | Reusable prompt with {{variables}} | "What is the prompt pattern?" |
| system-prompt-builder | LLM persona and operational rules | "Who is the LLM and what are its rules?" |

**Sequence**: few-shot-example-builder -> prompt-template-builder -> system-prompt-builder
(Examples inform templates; templates inform system prompts.)

## Handoff Protocol

### Receives (from requester or crew lead)
```yaml
input_contract:
  domain: string          # artifact kind being exemplified (knowledge_card, validator, etc.)
  format_to_exemplify: string  # what format rule to teach
  difficulty: easy|medium|hard  # optional, defaults to easy
  edge_case_focus: string  # optional, boundary condition to cover
```

### Produces (for downstream consumers)
```yaml
output_contract:
  artifact: p01_fse_{topic}.md   # few_shot_example with complete frontmatter
  quality: null                   # scored externally
  hard_gates: all 7 passed        # confirmed before handoff
  soft_score: >= 8.0              # target for publish
```

## Upstream Dependencies
- None: few_shot_example is standalone. Can start from scratch with only domain + format.

## Downstream Consumers
- prompt-template-builder: injects examples into {{few_shot_examples}} slot
- system-prompt-builder: may reference examples for format grounding
- LLM context at inference: examples loaded directly into prompt window

## Escalation
If domain is ambiguous or format unclear: ask requester before composing.
If request includes scoring criteria: redirect to golden_test-builder (P07).
If request includes assertions: redirect to unit-eval-builder (P07).

## Independence
few-shot-example-builder operates independently.
No blocking dependency on other builders.
Can produce artifacts in isolation given domain + format_to_exemplify.
