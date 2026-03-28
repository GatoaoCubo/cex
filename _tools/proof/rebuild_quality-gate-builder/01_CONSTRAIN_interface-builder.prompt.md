# CEX Crew Runner -- Builder Execution
**Builder**: `interface-builder`
**Function**: CONSTRAIN
**Intent**: reconstroi quality-gate-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:18.951813

## Intent Context
- **Verb**: reconstroi
- **Object**: quality-gate-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_interface.md
---
id: interface-builder
kind: type_builder
pillar: P06
parent: null
domain: interface
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, interface, P06, specialist, integration]
---

# interface-builder
## Identity
Especialista em construir interfaces — contratos bilaterais de integracao entre agentes.
Sabe tudo sobre API contracts, method signatures, input/output schemas,
versioning strategies, backward compatibility, deprecation policies,
and the boundary between interfaces (P06), input_schemas (P06), and signals (P12).
## Capabilities
- Definir contratos bilaterais com methods, input e output tipados
- Produzir interfaces com frontmatter completo (20+ campos)
- Garantir backward compatibility e planejar deprecation paths
- Compor mock specifications para testing
- Validar artifact contra quality gates (8 HARD + 10 SOFT)
## Routing
keywords: [interface, contract, integration, api, methods, bilateral, interop, agent-to-agent]
triggers: "define integration contract between agents", "what is the API between X and Y", "create interface for agent communication"
## Crew Role
In a crew, I handle INTEGRATION CONTRACTS.
I answer: "what is the formal contract between these two agents/systems?"
I do NOT handle: input schemas (P06 input_schema, unilateral), validation rules (P06 validator), runtime signals (P12 signal).

### bld_instruction_interface.md
---
kind: instruction
id: bld_instruction_interface
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for interface
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an interface
## Phase 1: RESEARCH
1. Identify the two systems or agents being integrated — name both the provider and the consumer explicitly
2. List every method the provider exposes to the consumer
3. For each method, define the input schema (what the consumer sends) and the output schema (what the provider returns)
4. Determine the versioning strategy: semver (1.0.0) or date-based (2026-01-01)
5. Assess backward compatibility requirements: which changes are allowed without a version bump?
6. Plan the deprecation path: which methods may be removed, on what timeline, and what replaces them?
7. Check existing interfaces via brain_query [IF MCP] for the same provider-consumer pair — avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and body constraints
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: all 20+ fields (null is acceptable for recommended fields)
4. Set quality: null — never self-score
5. Write the Methods section: one entry per method with name / direction / input schema / output schema / description
6. Write the Versioning section: strategy, current version, and the compatibility promise
7. Write the Backward Compatibility section: what changes are allowed without bumping the version
8. Write the Deprecation Policy section: timeline, migration path, and sunset date for any deprecated methods
9. Write the Mock Specification section: mock responses per method for use in testing
10. Write the Error Contracts section: error codes, messages, and retry guidance per method
11. Verify body is within 3072 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — apply each gate manually
2. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - id matches pattern `p06_iface_[a-z][a-z0-9_]+`
   - kind == interface
   - methods list has at least 2 entries
   - each method has name, input schema, output schema, and description
   - provider and consumer are both specified
   - versioning strategy is stated
   - quality == null
3. SOFT gates (score each against QUALITY_GATES.md):
   - backward compatibility policy is explicit
   - deprecation policy present (or null with a reason)
   - mock specification covers at least one method
   - error contracts cover failure cases per method
4. Cross-check scope boundaries:
   - bilateral contract (both sides documented), not a unilateral input_schema?
   - not a runtime event or signal (P12)?
   - not validation logic that belongs in a validator?
   - both provider and consumer sides fully documented?
5. If score < 8.0: revise in the same pass before outputting

### bld_knowledge_card_interface.md
---
kind: knowledge_card
id: bld_knowledge_card_interface
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for interface production — bilateral integration contracts
sources: Gamma et al. 1994, OpenAPI 3.x, gRPC/Protobuf, contract-first API design
---

# Domain Knowledge: interface
## Executive Summary
Interfaces are bilateral contracts where both provider and consumer agree on methods, input shapes, and output shapes. Rooted in interface-based programming (GoF 1994) and API-first design. Interfaces define what CAN happen between two systems — they are static specifications, not runtime events. They differ from input schemas (unilateral), signals (runtime notifications), and connectors (runtime implementations).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 (contracts/schema) |
| Frontmatter fields | 20+ |
| Quality gates | 8 HARD + 10 SOFT |
| Direction | Bilateral (both parties agree) |
| Key sections | methods (name, input, output), versioning, deprecation |
| Versioning | semver with backward_compatible flag |
| Mock support | Test doubles derivable from interface |
## Patterns
- **Method-based contracts**: named operations with typed input and output
| Source | Concept | Application |
|--------|---------|-------------|
| OpenAPI 3.x | REST paths, schemas, responses | methods structure |
| gRPC/Protobuf | Typed RPC method definitions | Strongly typed method contracts |
| TypeScript | Structural type contracts | Bilateral type agreement |
| GraphQL | Query/mutation typed fields | Method-level I/O contracts |
| Java interfaces | Abstract method signatures | Method signature pattern |
- **Bilateral agreement**: both provider and consumer acknowledge the contract — unlike unilateral input schemas
- **Versioning with semver**: breaking changes require major version bump; backward_compatible flag explicit
- **Deprecation planning**: every method has planned sunset timeline — no sudden removal
- **Mock derivation**: interfaces generate test doubles automatically — testing does not require real implementation
- **Static specification**: interfaces define what CAN happen, not what DID happen (that is a signal)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Unilateral contract | That is an input_schema; interfaces require both parties |
| No versioning | Breaking changes break consumers silently |
| No deprecation timeline | Methods removed without warning; consumer breakage |
| Free-text I/O types | Cannot generate mocks or validate compliance |
| Runtime state in interface | Interfaces are static specs; use signals for events |
| No mock specification | Cannot test without real implementation |
## Application
1. Identify parties: who is provider, who is consumer?
2. Define methods: name, typed input, typed output per operation
3. Set version: semver with backward_compatible flag
4. Plan deprecation: sunset timeline for methods to be removed
5. Add mock spec: example inputs and outputs for test doubles
6. Validate: bilateral agreement, all methods typed, version declared
## References
- Gamma et al. 1994: "Design Patterns" — interface segregation principle
- OpenAPI 3.x: REST API contract specification
- gRPC: service definition and typed RPC methods
- Contract-first API design: swagger.io best practices

### bld_quality_gate_interface.md
---
id: p11_qg_interface
kind: quality_gate
pillar: P11
title: "Gate: Interface"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "interface — bilateral integration contracts defining methods, I/O schemas, versioning, and compatibility between agents"
quality: null
tags: [quality-gate, interface, contract, bilateral, integration, versioning, compatibility]
tldr: "Gates ensuring interface artifacts define complete bilateral contracts with typed methods, versioning strategy, backward compatibility guarantees, and mock specs."
density_score: 0.92
---

# Gate: Interface
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: interface` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: agent_a_b` in file `agent_b_c.md` |
| H04 | Kind equals literal `interface` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: methods, provider, consumer, or version |
| H07 | Every method has both `input` and `output` defined | Any method with only one side defined |
| H08 | `provider` and `consumer` are distinct identifiers | Same value in both fields |
| H09 | `version` follows semver (`^\d+\.\d+\.\d+$`) | Non-semver version string |
| H10 | At least one method defined | Empty or missing methods list |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Type precision | 1.0 | All method inputs and outputs use typed field definitions | Typed but incomplete coverage | Untyped — described in prose only |
| S02 | Backward compatibility | 1.0 | Compatibility policy stated (breaking vs non-breaking changes defined) | Policy mentioned but vague | No compatibility statement |
| S03 | Versioning strategy | 1.0 | Version bump rules documented (what triggers major/minor/patch) | Semver used but bump rules absent | No versioning guidance |
| S04 | Deprecation path | 0.5 | Deprecated methods marked + migration path to replacement provided | Deprecated methods marked, no migration | No deprecation policy |
| S05 | Error contract | 1.0 | Error responses typed per method (error codes, shapes) | Generic error response defined | No error contract |
| S06 | Mock specification | 1.0 | Mock inputs and expected outputs for at least 2 methods | One method has mock data | No mock spec |
| S07 | Bilaterality enforced | 1.0 | Both provider and consumer roles clearly scoped; no unilateral creep | Mostly bilateral with minor leakage | Reads as a unilateral input schema |
| S08 | Method naming | 0.5 | Method names use verb_noun pattern (e.g., `get_status`, `send_result`) | Names present but inconsistent | Arbitrary names |
| S09 | Timeout and SLA | 0.5 | Expected response time or SLA documented per method | Overall SLA present, not per-method | None |
| S10 | Signal distinction | 0.5 | Interface defines synchronous request-response, not fire-and-forget | Mostly clear | Indistinguishable from a signal |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden integration contract |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Prototyping integration between two new agents where final method signatures are not yet known |
| Approver | Both provider and consumer team leads |

### bld_schema_interface.md
---
kind: schema
id: bld_schema_interface
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for interface
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: interface
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_iface_{contract}) | YES | - | Namespace compliance |
| kind | literal "interface" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| contract | string | YES | - | Human-readable contract name |
| provider | string | YES | - | Provider agent/system |
| consumer | string | YES | - | Consumer agent/system |
| methods | list[object] | YES | - | Method definitions (min 1) |
| backward_compatible | boolean | YES | true | Breaking change flag |
| deprecation | object {deprecated_methods, sunset_date, migration} | REC | null | Deprecation plan |
| mock | object {enabled, example_payloads} | REC | null | Test specification |
| domain | string | YES | - | Integration domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "interface" |
| tldr | string <= 160ch | YES | - | Dense summary |
| keywords | list[string] | REC | - | Brain search terms |
| density_score | float 0.80-1.00 | REC | - | Content density |
## Methods Object
```yaml
methods:
  - name: "{{method_name}}"
    input: {{type_or_object}}
    output: {{type_or_object}}
    description: "{{what_it_does}}"
```
Each method MUST have: name, input, output, description.
Input/output can be primitives (string, integer, boolean) or structured objects.
## Deprecation Object
```yaml
deprecation:
  deprecated_methods: ["method_a", "method_b"]
  sunset_date: "2026-06-01"
  migration: "Use method_c instead of method_a"
```
All fields optional. If no deprecation planned: deprecation: null.
## Mock Object
```yaml
mock:
  enabled: true
  example_payloads:
    - method: "get_status"
      input: {"agent_id": "shaka"}
      output: {"status": "active", "uptime": 3600}
```
## ID Pattern
Regex: `^p06_iface_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Contract Definition` — what this interface enables, in plain language
2. `## Methods` — table with name/input/output/description for each method
3. `## Versioning` — version, backward_compatible, changelog, migration
4. `## Mock Specification` — example payloads for testing
## Constraints
- max_bytes: 3072 (body only)
- naming: p06_iface_{contract}.yaml
- machine_format: json (compiled form)
- id == filename stem
- methods MUST have at least 1 entry
- backward_compatible MUST be boolean
- quality: null always
- interface is bilateral — provider AND consumer must be specified

### bld_examples_interface.md
---
kind: examples
id: bld_examples_interface
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of interface artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: interface-builder
## Golden Example
INPUT: "Define o contrato entre researcher (pesquisa) e marketer (marketing) para entrega de research results"
OUTPUT:
```yaml
id: p06_iface_research_to_marketing
kind: interface
pillar: P06
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
contract: "Research results delivery from researcher to marketer"
provider: "researcher"
consumer: "marketer"
methods:
  - name: "get_research_summary"
    input: {topic: string, max_sources: integer}
    output: {summary: string, sources: list, confidence: float}
    description: "Returns distilled research summary with sources and confidence score"
  - name: "get_competitor_data"
    input: {competitor_name: string, marketplace: string}
    output: {pricing: object, listings: list, rating: float}
    description: "Returns structured competitor data for a specific marketplace"
backward_compatible: true
deprecation: null
mock:
  enabled: true
  example_payloads:
    - method: "get_research_summary"
      input: {topic: "decoracao minimalista", max_sources: 5}
      output: {summary: "Tendencia crescente em 2026...", sources: ["url1", "url2"], confidence: 0.87}
domain: "satellite-integration"
quality: null
tags: [interface, shaka, lily, research, marketing, satellite-integration]
tldr: "Bilateral contract for researcher to deliver research results to marketer marketing workflows."
density_score: 0.91
```
## Contract Definition
researcher (research satellite) provides structured research data to marketer (marketing satellite).
marketer calls methods to get research summaries and competitor data for marketing campaigns.
## Methods
| # | Name | Input | Output | Description |
|---|------|-------|--------|-------------|
| 1 | get_research_summary | {topic, max_sources} | {summary, sources, confidence} | Distilled research with sources |
| 2 | get_competitor_data | {competitor_name, marketplace} | {pricing, listings, rating} | Structured competitor intel |
## Versioning
- **Version**: 1.0.0
- **Backward compatible**: yes
- **Changes from previous**: initial release
- **Migration notes**: none
## Mock Specification
```json
{
  "method": "get_research_summary",
  "input": {"topic": "decoracao minimalista", "max_sources": 5},
  "output": {"summary": "Tendencia crescente em 2026...", "sources": ["url1", "url2"], "confidence": 0.87}
}
```
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p06_iface_ pattern (H02 pass)
- kind: interface (H04 pass)
- 15+ required fields present (H06 pass)
- methods has 2 entries with name/input/output/description (H07 pass)
- backward_compatible is boolean (H08 pass)
- provider and consumer specified (H09 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "interface" (S02 pass)
- YAML parses cleanly (H01 pass)
## Anti-Example
INPUT: "Interface entre researcher e marketer"
BAD OUTPUT:
```yaml
id: shaka_lily_interface
kind: integration
pillar: Schema
contract: researcher-marketer
methods: "get data from researcher"
backward_compatible: maybe
quality: 9.0
tags: interface
```
researcher sends data to marketer when needed.
FAILURES:
1. id: no `p06_iface_` prefix -> H02 FAIL
2. kind: "integration" not "interface" -> H04 FAIL
3. pillar: "Schema" not "P06" -> H03 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. methods: string instead of list[object] -> H07 FAIL
6. backward_compatible: "maybe" not boolean -> H08 FAIL
7. provider/consumer: missing -> H09 FAIL
8. tags: string not list, len < 3 -> S02 FAIL
9. contract: not descriptive -> S05 FAIL
10. body: filler prose ("when needed") -> S07 FAIL

### bld_config_interface.md
---
kind: config
id: bld_config_interface
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: interface Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_iface_{contract_slug}.yaml` | `p06_iface_research_to_marketing.yaml` |
| Builder directory | kebab-case | `interface-builder/` |
| Frontmatter fields | snake_case | `backward_compatible`, `example_payloads` |
| Contract slugs | snake_case, lowercase | `research_to_marketing`, `brain_search` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P06_schema/examples/p06_iface_{contract_slug}.yaml`
- Compiled: `cex/P06_schema/compiled/p06_iface_{contract_slug}.json`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total: ~4000 bytes including frontmatter
- Density: >= 0.80
## Method Contract Rules
| Rule | Enforcement |
|------|-------------|
| Each method has name | HARD (H07) |
| Each method has input type | HARD (H07) |
| Each method has output type | HARD (H07) |
| Each method has description | SOFT (S05) |
| Methods list >= 1 entry | HARD (H07) |
## Versioning Policy
- New interfaces start at 1.0.0
- Breaking changes: bump major, set backward_compatible: false
- Additive methods: bump minor, backward_compatible: true
- Fix/doc changes: bump patch

### bld_output_template_interface.md
---
kind: output_template
id: bld_output_template_interface
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an interface
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: interface
```yaml
id: p06_iface_{{contract_slug}}
kind: interface
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
contract: "{{human_readable_contract_name}}"
provider: "{{provider_agent_or_system}}"
consumer: "{{consumer_agent_or_system}}"
methods:
  - name: "{{method_name}}"
    input: {{input_type_or_object}}
    output: {{output_type_or_object}}
    description: "{{what_this_method_does}}"
backward_compatible: {{true|false}}
deprecation:
  deprecated_methods: [{{method_names_or_empty}}]
  sunset_date: "{{YYYY-MM-DD_or_null}}"
  migration: "{{migration_notes_or_null}}"
mock:
  enabled: {{true|false}}
  example_payloads:
    - method: "{{method_name}}"
      input: {{example_input}}
      output: {{example_output}}
domain: "{{integration_domain}}"
quality: null
tags: [interface, {{provider_tag}}, {{consumer_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
```
## Contract Definition
{{what_this_interface_enables_between_provider_and_consumer}}
## Methods
| # | Name | Input | Output | Description |
|---|------|-------|--------|-------------|
| 1 | {{method}} | {{input}} | {{output}} | {{desc}} |
| 2 | {{method}} | {{input}} | {{output}} | {{desc}} |
## Versioning
- **Version**: {{current_version}}
- **Backward compatible**: {{yes_no}}
- **Changes from previous**: {{changelog_or_initial}}
- **Migration notes**: {{migration_or_none}}
## Mock Specification
```json
{
  "method": "{{method_name}}",
  "input": {{example_input_json}},
  "output": {{example_output_json}}
}
```
## References
- {{reference_1}}
- {{reference_2}}

### bld_architecture_interface.md
---
kind: architecture
id: bld_architecture_interface
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of interface — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| method_definitions | Named operations both parties agree exist | author | required |
| input_types | Typed input shape per method (may reference input_schema) | author | required |
| output_types | Typed output shape per method | author | required |
| version | Semantic version for backward compatibility tracking | author | required |
| deprecation_policy | How and when old methods are retired | author | recommended |
| mock_spec | Stub responses for testing without live implementation | author | optional |
| error_contract | Named error codes and shapes each method may return | author | recommended |
| compatibility_notes | Breaking vs non-breaking change classification | author | optional |
## Dependency Graph
```
interface     --consumes--> input_schema
connector     --implements--> interface
validator     --checks_against--> interface
system_prompt --references--> interface
interface     --produces--> mock_spec
```
| From | To | Type | Data |
|------|----|------|------|
| interface | input_schema | data_flow | method input shapes formalized as schemas |
| connector | interface | depends | runtime adapter implements the declared contract |
| validator | interface | data_flow | compliance check against method signatures |
| system_prompt | interface | data_flow | documents available methods to agent identity |
| interface | mock_spec | produces | stub responses derived from output_types |
## Boundary Table
| interface IS | interface IS NOT |
|--------------|-----------------|
| Bilateral contract agreed by both parties | Unilateral shape contract for one callee |
| Specifies methods with named input and output | Runtime event or status report |
| Design-time artifact (written before implementation) | Concrete implementation or adapter code |
| Versioned with deprecation and compatibility policy | Routing decision about who receives what |
| Defines what CAN happen between two agents | Validates whether something DID happen correctly |
| Shared reference for both producer and consumer | Orchestration logic or execution recipe |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Contract surface | method_definitions, version | Declare the operations both agents agree on |
| Type system | input_types, output_types | Enforce data shapes for each method direction |
| Safety | error_contract, compatibility_notes | Define failure modes and change impact |
| Lifecycle | deprecation_policy | Govern how the contract evolves over time |
| Testing | mock_spec | Enable development against the contract without live systems |

### bld_collaboration_interface.md
---
kind: collaboration
id: bld_collaboration_interface
pillar: P12
llm_function: COLLABORATE
purpose: How interface-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: interface-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the formal contract between these two agents/systems?"
I do not define unilateral input schemas. I do not build runtime signals.
I specify bilateral integration contracts so agents and systems interoperate reliably.
## Crew Compositions
### Crew: "Integration Design"
```
  1. component-map-builder -> "inventory of components that need interfaces"
  2. interface-builder -> "bilateral contracts between components"
  3. client-builder -> "client implementations against interfaces"
  4. connector-builder -> "bidirectional integrations via interfaces"
```
### Crew: "Contract Stack"
```
  1. input-schema-builder -> "unilateral input contracts"
  2. interface-builder -> "bilateral integration contracts"
  3. e2e-eval-builder -> "validation that contracts are honored"
```
## Handoff Protocol
### I Receive
- seeds: party A name, party B name, methods/operations list
- optional: versioning strategy, deprecation policy, mock specifications
### I Produce
- interface artifact (.md + .yaml frontmatter)
- committed to: `cex/P06/examples/p06_interface_{a}_{b}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- input-schema-builder: provides unilateral schemas that compose into bilateral contracts
- component-map-builder: identifies which components need interfaces
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| client-builder | Implements outbound side of the interface |
| connector-builder | Implements bidirectional side of the interface |
| e2e-eval-builder | Tests that interface contracts are honored end-to-end |
| dispatch-rule-builder | Routes to targets defined by interface contracts |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `interface-builder` for pipeline function `CONSTRAIN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
