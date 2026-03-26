---
id: kb_prompt_template_builder
kind: knowledge
pillar: P01
llm_function: INJECT
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [knowledge, prompt-template, P03, langchain, mustache, jinja2]
---

# Knowledge — prompt-template-builder

## Foundational Concepts

A **prompt template** is a parameterized string or document where fixed structure and dynamic content are separated. Variables act as typed slots filled at runtime. The same template can produce N distinct prompts by substituting different variable values — this is the core reuse contract.

**Separation of concerns**: structure (template) vs content (variables). This mirrors HTML templates, SQL prepared statements, and mail-merge documents.

## Industry Implementations

| System | Syntax | Variable Typing | Notes |
|---|---|---|---|
| LangChain PromptTemplate | `{variable}` (single brace) | Implicit string | `from_template()` classmethod |
| LangChain ChatPromptTemplate | `{variable}` | Implicit string | Multi-role: system/human/ai messages |
| DSPy Signature | Field annotations | Python type hints | Input/output fields declared as class attrs |
| Mustache | `{{variable}}` | Untyped (string) | Logic-less; `{{#list}}` for loops |
| Handlebars | `{{variable}}` | Untyped | Extends Mustache with helpers |
| Jinja2 | `{{ variable }}` | Python types | Full logic: if/for/filters |
| Go text/template | `{{.Variable}}` | Go types | Dot-notation for struct fields |
| Anthropic (internal) | `{{VARIABLE}}` | Untyped | Used in prompt libraries |

**CEX tier-1 syntax**: `{{variable}}` (Mustache-compatible, Anthropic-compatible)
**CEX tier-2 syntax**: `[VARIABLE]` (when Mustache conflicts with target system, e.g., Vue.js)

## Key Patterns

1. **Required vs optional variables**: Required variables have no default; optional variables carry a default value in the schema.
2. **Type safety**: Declaring variable types (string, list, integer, boolean, object) enables validation before template rendering.
3. **Composability**: Templates can reference other templates via `{{> partial}}` (Mustache) or `{% include %}` (Jinja2).
4. **Versioning**: Templates are versioned independently of the prompts they generate; a v2 template can produce the same logical output with a different structure.
5. **Domain scoping**: A template's `domain` field constrains valid variable values to a semantic space (e.g., domain: research → variables expect research-context values).
6. **Role segmentation**: ChatPromptTemplates assign each segment to a role (system/human/ai), preserving the conversation structure while parameterizing content.
7. **Rendering pipeline**: Template → variable substitution → rendered prompt → LLM call. The template itself never reaches the LLM.
8. **Idempotency**: The same template + same variable values MUST always produce the same rendered prompt (no side effects in the template body).

## CEX Extensions

- `variable_syntax` field: explicitly declares which syntax tier the template uses
- `composable` boolean: signals whether this template is designed to be embedded in larger templates
- `quality` field: stores the latest gate score; starts as null, updated after validation
- `tldr` field: one-sentence summary for discovery and routing

## Boundary Table — P03 Siblings

| Kind | Is reusable mold? | Has {{vars}}? | Verdict |
|---|---|---|---|
| `prompt_template` | YES | YES | THIS kind |
| `system_prompt` | NO (fixed identity) | RARELY | NAO EH — different purpose |
| `user_prompt` | NO (one-time task) | NO | NAO EH — no reuse contract |
| `few_shot` | Partially (examples) | NO (fixed examples) | NAO EH — examples, not mold |
| `chain_of_thought` | NO (reasoning style) | NO | NAO EH — reasoning pattern |
| `react` | NO (loop pattern) | NO | NAO EH — Thought/Action loop |
| `chain` | NO (sequence) | NO | NAO EH — prompt sequence |
| `meta_prompt` | NO (generates prompts) | Sometimes | NAO EH — generates, not instantiates |
| `router_prompt` | NO (classifies) | Sometimes | NAO EH — routes, not fills |
| `planner` | NO (decomposes) | Sometimes | NAO EH — planning, not templating |
