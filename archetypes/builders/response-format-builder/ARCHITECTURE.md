---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of response_format — inventory, dependencies, and architectural position
---

# Architecture: response_format in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 19-field metadata header (id, kind, pillar, domain, format_type, etc.) | response-format-builder | active |
| format_type | Output structure type (json, yaml, markdown, csv, plaintext) | author | active |
| sections | Ordered sections the LLM must include in its response | author | active |
| field_definitions | Named fields with types and descriptions within each section | author | active |
| injection_point | Where the format is placed (system_prompt or user_message) | author | active |
| example_output | Concrete example showing a correctly formatted response | author | active |

## Dependency Graph

```
system_prompt   --injects-->    response_format  --consumed_by-->  LLM
response_format --produces-->   formatted_output  --validated_by--> validation_schema
response_format --signals-->    format_deviation
```

| From | To | Type | Data |
|------|----|------|------|
| system_prompt (P03) | response_format | data_flow | format injected into system prompt for LLM guidance |
| response_format | LLM | consumes | LLM reads format instructions during generation |
| response_format | formatted_output | produces | response structured according to format spec |
| formatted_output | validation_schema (P06) | data_flow | post-generation contract validates the output |
| formatted_output | parser (P05) | data_flow | parser extracts structured data from formatted output |
| response_format | format_deviation (P12) | signals | emitted when LLM output deviates from format |

## Boundary Table

| response_format IS | response_format IS NOT |
|--------------------|------------------------|
| An instruction injected into the prompt that the LLM sees | A post-generation contract the system enforces (validation_schema P06) |
| Guides how the LLM structures its output during generation | A data extractor applied after generation (parser P05) |
| Specifies sections, fields, and format type | A format converter between representations (formatter P05) |
| Placed at a specific injection point in the prompt | A naming convention for files or artifacts (naming_rule P05) |
| Defines what the response looks like, not what it contains | A task instruction defining what to accomplish (action_prompt P03) |
| Format type: json, yaml, markdown, csv, or plaintext | A binary or image output specification |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Injection | system_prompt, injection_point | Where and how the format enters the prompt |
| Definition | frontmatter, format_type, sections, field_definitions | Specify the structure the LLM must follow |
| Example | example_output | Concrete reference for the expected format |
| Generation | LLM, formatted_output | LLM produces output following the format |
| Validation | validation_schema, parser, format_deviation | Post-generation checking and data extraction |
