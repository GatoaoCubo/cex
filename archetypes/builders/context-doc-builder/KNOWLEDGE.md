---
pillar: P01
llm_function: INJECT
purpose: Foundational domain knowledge for context-doc-builder
---

# Knowledge: context_doc

## Foundational Concept
A context_doc is a domain background document for prompt hydration. Its LLM function is
INJECT: it is loaded into agent context to provide situational awareness before task
execution. It is NOT a reference document (no density gate), NOT a definition (no term
scope), NOT an instruction (no steps).

## Industry Analogs
- README context sections in software repos
- Project brief / discovery document in consulting
- Technical context memo in engineering teams
- Onboarding background packet for new team members
- Situation report (SITREP) in operations contexts

## Key Patterns
- **Scope before write**: Define boundaries first. What domain? What time horizon? What is excluded?
- **Stakeholder-focused**: Who needs this context? Tailor precision to their decisions.
- **Constraint-driven**: List what cannot change. Constraints bound the domain context.
- **Time-bounded**: Context ages. Include timeline, created/updated dates.
- **Dependency-aware**: Context_docs often link to or are consumed by system_prompts and action_prompts.

## CEX Extensions
- `domain` field: machine-readable domain label (e.g., "ecommerce_imports", "api_auth")
- `scope` field: one-sentence scope boundary (e.g., "Brazilian import regulations 2025-2026")
- `quality: null` always — scored externally, never self-assigned

## Boundary vs Siblings
| Kind | Function | Density Gate | Key Difference |
|------|----------|-------------|----------------|
| context_doc | INJECT | none | Domain background, multiple facts, narrative allowed |
| knowledge_card | INJECT | >= 0.80 | Atomic single fact, high density, no narrative |
| glossary_entry | INJECT | none | Single term definition, controlled vocabulary |

## Consumption Pattern
context_doc is consumed by: system_prompt (BECOME), action_prompt (REASON), agent boot
sequences. It answers "what is the background?" before the agent answers "what do I do?"
