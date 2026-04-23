---
quality: 8.0
id: kc_pillar_brief_p06_schema_en
kind: knowledge_card
pillar: P06
title: "P06 Schema — Your AI's Skeleton: Contracts That Hold Everything Together"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
language: en
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p06, schema, input-schema, validation, contracts, type-safety, json-schema, llm-engineering]
tldr: "P06 Schema covers the 8 kinds that define data contracts for AI systems — input schemas, validators, interfaces, type definitions — the structural layer that prevents invalid data from propagating through your pipeline."
source_concepts: [kc_lens_index, mentor_context, p03_pc_cex_universal]
related:
  - kc_pillar_brief_p06_schema_pt
  - kc_pillar_brief_p05_output_en
  - kc_pillar_brief_p07_evals_en
  - kc_pillar_brief_p08_architecture_en
  - n00_p06_kind_index
density_score: 0.87
updated: "2026-04-22"
---

# P06 Schema — The Skeleton: Contracts That Hold Everything Together

## The Universal Principle: AI Systems Break at Boundaries

Here is the structural truth about AI pipelines: every component that calls another component is a potential failure point. An LLM calling a tool, a tool returning data to an agent, an agent passing context to a downstream model, a pipeline step writing to a database — every one of these transitions is a boundary where data can arrive malformed, incomplete, or of the wrong type.

Without explicit contracts at these boundaries, you are building on sand. Components that work individually fail when integrated. Bugs manifest late, far from their origin, making them expensive to diagnose. Systems become brittle against any change to upstream output format.

P06 Schema is the pillar that hardens these boundaries. It provides typed artifacts for defining what goes in (input schemas), what comes out (validation schemas), what data types exist in the system (type definitions and enums), how components talk to each other (interfaces), what constraints must always hold (validators), and how external APIs are documented (API references).

This discipline predates LLMs. It is the same lesson learned by REST API designers in the 2010s, microservice teams in the 2010s, and database engineers before that: explicit contracts at system boundaries are what make complex systems maintainable. LLMs add a new wrinkle — the contract boundary now includes the LLM's own input and output, not just the surrounding code. But the principle is identical.

This framework is universal. JSON Schema, Pydantic, Zod, TypeScript interfaces, OpenAPI specs — all implementations of the same principle. The P06 kinds give you a way to reason about which type of contract you need, regardless of the implementation technology.

### Why Schemas Matter More with LLMs Than Without

Traditional software contracts are static: you define them once, they do not change unless you explicitly change them. LLM-adjacent contracts have a new challenge: the LLM's output is probabilistic. Even with a perfect response format instruction (P05), there is always some probability that the LLM deviates.

This makes input validation more important, not less. When you cannot fully trust that upstream output will conform to the expected structure, you need robust contracts at every layer:

- Input to the LLM (what the system sends to the model)
- Output from the LLM (what the model returns to the system)
- Input to tools (what the LLM tells its tools to do)
- Output from tools (what tool results get returned to the LLM)
- Agent-to-agent communication (what one agent tells another)

Five schema boundaries in a single LLM agent call. Every one of them can propagate bad data if not contracted.

---

## All 8 Kinds in P06 — The Complete Schema Arsenal

| Kind | Purpose | Layer | Function |
|------|---------|-------|----------|
| `input_schema` | Data contract for what a component accepts | Spec | CONSTRAIN |
| `validation_schema` | Post-generation contract applied by the system | Spec | GOVERN |
| `validator` | Reusable pass/fail validation rule | Governance | GOVERN |
| `interface` | Bilateral integration contract between agents | Spec | CONSTRAIN |
| `type_def` | Custom type definition in the system | Spec | GOVERN |
| `enum_def` | Finite enumeration of valid values | Runtime | CONSTRAIN |
| `api_reference` | API documentation with endpoints, params, auth | Spec | INJECT |
| `edit_format` | LLM-to-host file change format specification | Spec | GOVERN |

P06 has 8 kinds — the smallest pillar in the 12-pillar taxonomy. This is intentional: schema kinds are fundamental, not numerous. A system with 300 knowledge cards still only needs these 8 types of contracts. What scales is the number of instances, not the number of kinds.

---

## Key Engineering Patterns — Universal, Any AI

### Pattern 1: The Input Schema Firewall

Every agent, tool, or pipeline step should have an explicit input schema that validates incoming data before processing begins. This is the firewall pattern: invalid data is rejected at the boundary, not propagated into the core.

The canonical structure of an input schema:

```yaml
# input_schema.yaml
id: is_research_pipeline_input
kind: input_schema
target_component: research_pipeline
schema_format: pydantic
strict_mode: true
fields:
  - name: query
    type: str
    required: true
    constraints: {min_length: 3, max_length: 500}
  - name: max_sources
    type: int
    required: false
    default: 10
    constraints: {min: 1, max: 50}
  - name: include_domains
    type: list[str]
    required: false
    default: []
  - name: language
    type: LanguageEnum
    required: false
    default: en
example:
  query: "LLM context window techniques 2025"
  max_sources: 15
  language: en
```

This schema does several things: it documents accepted inputs (so callers know what to provide), validates at runtime (so bad inputs fail loudly), enables SDK generation (tools like FastAPI, Pydantic, and OpenAPI can generate client code directly from this), and serves as living documentation that is always current with the implementation.

In practice:
- Python: `pydantic.BaseModel` or `dataclasses`
- TypeScript: `zod.z.object({...})` or `interface` declarations
- API: OpenAPI `requestBody` schema
- LangChain tools: `args_schema` field on `BaseTool`
- Function calling: JSON Schema in tool definitions

**Try this now:** Pick any function in your codebase that processes LLM input or tool output. Write a Pydantic model (Python) or Zod schema (TypeScript) for its inputs. Add validation at the function entry point. Run your existing tests — any that were passing with malformed data will now correctly fail.

### Pattern 2: Pre vs. Post Generation Contracts

This is the most important conceptual distinction in P06. There are two types of output contracts:

**Pre-generation (response_format, P05)**: the LLM SEES this. It shapes what the model produces. It is a prompt-level instruction: "format your response as JSON with these fields."

**Post-generation (validation_schema, P06)**: the SYSTEM APPLIES this. The LLM does not see it. It is a technical contract applied to the raw output after the LLM has finished generating.

Why do you need both?

Because the response format tells the LLM what to do, but it does not guarantee compliance. An LLM under high temperature, or one that has been prompted with a complex task, can deviate from the format instructions. The validation schema catches this deviation before it propagates.

```
User request -> prompt (with response_format) -> LLM generates -> raw output
                                                                      |
                                                         validation_schema.validate(raw_output)
                                                                      |
                                                             PASS: deliver output
                                                             FAIL: retry generation or raise error
```

This two-layer approach is the industry standard in production LLM systems. OpenAI's "structured outputs" mode uses JSON Schema validation on the backend. Anthropic's tool use validates tool call schemas. You should replicate this at the application level for any schema that matters.

**Try this now:** Look at a place in your code where you use the LLM's output directly without validation. Write a JSON Schema (or Pydantic model) for the expected output structure. Validate the LLM response against it before using it. Handle the validation error explicitly.

### Pattern 3: The Validator Composition Pattern

Validators are atomic: each one tests a single assertion. Validation schemas and output validators are composite: they reference multiple validators and define how failures aggregate.

The power of this separation is reusability. A validator that checks "frontmatter has required fields" can be referenced by 50 different validation schemas that apply to different kinds of artifacts. Change the validator once, all 50 schemas benefit.

```yaml
# validator: atomic check
id: validator_quality_in_range
check_type: business_rule
assertion: "quality is null OR quality between 0.0 and 10.0"
severity: error
error_message: "quality must be null (unreviewed) or a float in [0, 10]. Got: {value}"
applies_to: [knowledge_card, agent, prompt_template, workflow]

# validation_schema: composes validators
id: vs_knowledge_card_standard
validators:
  - validator_has_frontmatter
  - validator_quality_in_range
  - validator_kind_in_registry
  - validator_pillar_valid
  - validator_no_empty_sections
on_fail: raise_first_error
```

This pattern is universal across validation libraries:
- Pydantic: `@validator` decorators compose into model validation
- Zod: `.refine()` callbacks compose into schema validation
- JSON Schema: `allOf` / `anyOf` patterns compose validators
- CEXAI: `validator` kind instances reference via `validation_schema`

**Try this now:** Find a complex validation function in your codebase. Decompose it into atomic assertions, each testing one thing. Rebuild the compound validation by calling the atomic ones in sequence. Measure how much easier the unit tests become.

### Pattern 4: Interface Contracts for Agent-to-Agent Communication

When you have two agents that communicate — one calling the other, one passing data to the other, one reading from the other's output — you need a bilateral contract. This is what the `interface` kind formalizes.

The key property of an interface vs. an input_schema: an input_schema is unilateral (defines what ONE component accepts). An interface is bilateral (defines the contract BETWEEN two components, including both the request format and the response format).

```yaml
# interface: bilateral agent contract
id: iface_n07_to_n03_dispatch
kind: interface
parties:
  caller: n07_orchestrator
  callee: n03_engineering
request:
  fields:
    - {name: task, type: str, required: true}
    - {name: kind, type: KindEnum, required: true}
    - {name: handoff_path, type: str, required: true}
response:
  fields:
    - {name: status, type: DispatchStatusEnum, required: true}
    - {name: artifact_path, type: str, required: false}
    - {name: quality_score, type: float, required: false}
    - {name: signal_written, type: bool, required: true}
error_contract:
  timeout: 3600
  retry_policy: no_retry
  on_failure: write_failed_signal
```

This interface is machine-readable. N07 can validate its dispatch call against it before sending. N03 can validate the incoming task against it before executing. Both parties have a shared source of truth that prevents protocol drift.

---

## Architecture Deep Dive — How P06 Kinds Relate

```
P02 MODEL
  agent_def (defines what an agent is)
      |
      v
P06 SCHEMA: DEFINITION LAYER
  enum_def <------ (finite value sets that type_def uses)
      |
      v
  type_def <------ (custom types: KindEnum, NucleusId, QualityScore)
      |
      v
  input_schema <--- (what the agent accepts: validates callers)
      |
      v
  interface <------ (bilateral: request + response contract between 2 agents)

P05 OUTPUT: generates data
      |
      v
P06 SCHEMA: VALIDATION LAYER
  validator <------ (atomic assertions: one check, pass/fail)
      |
      v
  validation_schema <- (composite: references multiple validators)
      |
      v
  api_reference <-- (documents all of the above for external consumers)
```

The definition layer (enums, types, input schemas, interfaces) runs BEFORE processing — it constrains what enters the system. The validation layer (validators, validation schemas) runs AFTER generation — it audits what the system produced. Both layers reference the same type definitions, creating a coherent type system across the entire pipeline.

---

## Real Examples from N00_genesis

**Input Schema in practice** (`N00_genesis/P06_schema/kind_input_schema/kind_manifest_n00.md`):
```yaml
id: input_schema_cex_8f_runner
kind: input_schema
target_component: cex_8f_runner
schema_format: pydantic
strict_mode: true
fields:
  - {name: intent, type: str, required: true}
  - {name: kind, type: NucleusId, required: false}
  - {name: execute, type: bool, required: false, default: false}
```
This schema is the entry gate for the CEXAI build engine. Any call to `cex_8f_runner` with a missing `intent` or an invalid `kind` is rejected at the boundary, not inside the engine.

**Validator for structural integrity** (`N00_genesis/P06_schema/kind_validator/kind_manifest_n00.md`):
```yaml
id: validator_has_frontmatter
check_type: structural
assertion: "Artifact has id, kind, pillar, nucleus, title, version, quality fields"
severity: error
error_message: "Missing required frontmatter field: {field}"
applies_to: [knowledge_card, agent, prompt_template, workflow]
```
This single validator is referenced by dozens of validation schemas. It enforces the frontmatter contract across all artifact types.

**Partner registration schema** (`N00_genesis/P06_schema/ex_input_schema_partner_registration.md`):
A complete input schema for a partner API registration endpoint, with fields for company name, contact email, API tier selection, webhook URL, and signature validation — demonstrating how P06 kinds scale to production API contracts.

**Supabase table interface** (`N00_genesis/P06_schema/ex_interface_supabase_tables.md`):
An interface defining the contract between an AI agent and a Supabase database backend — request schemas for queries, response schemas for result sets, error contracts for connection failures, and retry policies.

---

## Anti-Patterns — The Universal Mistakes

### Anti-Pattern 1: Duck-Typing LLM Outputs

Accessing LLM output fields without validation: `result["summary"]` when you have no guarantee that `summary` is in the response. This fails silently with `KeyError` or `None` in downstream code, usually at the worst possible time in production.

**Fix**: define a `validation_schema` for every LLM output structure your code depends on. Validate before accessing fields. Fail loudly at the validation step, not silently at the access step.

### Anti-Pattern 2: Using Strings as Type-Unsafe Identifiers

Passing around strings like `"n03"`, `"landing_page"`, `"P05"` without validation. A single typo — `"landing-page"` vs. `"landing_page"` — causes a failure at the dispatch layer that is painful to trace.

**Fix**: define `enum_def` for every finite set of valid values in your system. `NucleusEnum`, `KindEnum`, `PillarEnum`. Validate all identifiers at input boundaries using these enums.

### Anti-Pattern 3: Unstated Interface Assumptions

Two components that communicate but have never written down the contract. "It works because I know what N03 expects." This breaks as soon as N03 changes its expected format and the change is not communicated to callers.

**Fix**: write an `interface` artifact for every agent-to-agent communication channel in your system. Make it the source of truth. When you change the interface, update the artifact and notify all callers.

### Anti-Pattern 4: Monolithic Validators

A single validation function that checks 20 things. When it fails, you get a cryptic error and no way to know which of the 20 checks failed. When you want to reuse one of the 20 checks in a different context, you cannot.

**Fix**: one `validator` per assertion. Compose them in `validation_schema`. Each atomic validator has a descriptive ID and a clear error message.

### Anti-Pattern 5: Schema Drift

Input schemas and type definitions that are written once and never updated as the system evolves. After 6 months, the schema and the code are out of sync — the schema says `field_x` is required, but the code actually ignores it. The schema says `type: int`, but the code now handles strings too.

**Fix**: treat schemas as living documents. Add schema version numbers. When the system changes, update the schema first (schema-first development). Use code generation tools to derive implementation from schema where possible.

---

## Cross-Pillar Connections

| Pillar | Relationship to P06 |
|--------|---------------------|
| **P05 Output** | `response_format` (P05) constrains generation; `validation_schema` (P06) validates after generation — they are complementary, not alternatives |
| **P02 Model** | Agent definitions (P02) reference input schemas (P06) to document what inputs they accept — P06 makes P02 agents callable |
| **P04 Tools** | Tool definitions (P04) include function schemas (JSON Schema) — these are instances of P06 input_schema for tool parameters |
| **P07 Evals** | Eval datasets (P07) are validated against validation schemas (P06) to ensure test cases are well-formed before running evaluations |
| **P08 Architecture** | Component maps (P08) reference interfaces (P06) — the architecture diagram describes what connects; the interface defines how |
| **P11 Feedback** | Quality gates (P11) reference validators (P06) for structural checks — P06 defines the rules, P11 enforces them as pipeline gates |

### The P06-P07 Synergy

Schema validation (P06) and evaluation (P07) address different dimensions of quality:

- **P06 Schema**: binary pass/fail — either the data conforms to the contract or it does not. No partial credit.
- **P07 Evals**: graduated scoring — measures how good the output is on multiple dimensions. Partial credit, weighted criteria.

You need both. A response can be structurally valid (passes P06 validation) but semantically poor (scores 4/10 on P07 rubric). A response can fail P06 validation (missing required field) but contain brilliant content.

Run P06 validation first (it is cheap and fast). Only run P07 evaluation on responses that pass P06 (expensive, uses LLM calls or human review).

---

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p06_schema_pt]] | sibling (PT-BR) | 1.0 |
| [[kc_pillar_brief_p05_output_en]] | upstream | 0.72 |
| [[kc_pillar_brief_p07_evals_en]] | downstream | 0.65 |
| [[kc_pillar_brief_p08_architecture_en]] | related | 0.58 |
| [[n00_p06_kind_index]] | source | 0.55 |
| [[n00_input_schema_manifest]] | related | 0.52 |
| [[n00_validator_manifest]] | related | 0.49 |
| [[ex_input_schema_partner_registration]] | example | 0.44 |
| [[ex_interface_supabase_tables]] | example | 0.42 |
| [[kc_pillar_brief_p04_tools_en]] | upstream | 0.38 |
