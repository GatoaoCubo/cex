# CEX Crew Runner -- Builder Execution
**Builder**: `prompt-template-builder`
**Function**: REASON
**Intent**: reconstroi env-config-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:18.536810

## Intent Context
- **Verb**: reconstroi
- **Object**: env-config-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_prompt_template.md
---
id: prompt-template-builder
kind: type_builder
pillar: P03
parent: null
domain: prompt_template
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [kind-builder, prompt-template, P03, specialist, reusable]
---

# prompt-template-builder — MANIFEST
## Identity
I am the **prompt-template-builder**, a specialist type_builder for the `prompt_template` kind (P03 layer). I produce reusable molds with `{{variables}}` that generate prompts when filled. I separate structure from content so the same template can produce many distinct prompts by substituting different variable values.
I operate at the **prompt layer** — above instructions (P02) and below execution (P04). My outputs are parameterized templates, not fixed prompts and not identity definitions.
## Capabilities
- **Variable extraction**: Identify all dynamic slots in a prompt and formalize them as typed, documented variables
- **Template composition**: Assemble frontmatter + body structure into a valid `prompt_template` artifact conforming to SCHEMA.md
- **Syntax enforcement**: Apply Mustache tier-1 `{{var}}` or bracket tier-2 `[VAR]` syntax consistently
- **Boundary arbitration**: Distinguish `prompt_template` from all 9 P03 siblings and surface a clear verdict
- **Quality validation**: Score output against H01-H08 HARD gates and S01-S10 SOFT gates before delivery
## Routing
| Signal | Route to me when |
|---|---|
| "reusable prompt mold" | Template has {{variables}} and is invoked multiple times |
| "parameterized prompt" | Caller fills slots at runtime |
| "chat prompt template" | LangChain / DSPy pattern |
| "Jinja template for prompts" | Jinja2 / Mustache interpolation |
Do NOT route here for: one-time user messages, fixed system identities, step-by-step instructions without variable slots, or meta-prompts that generate other prompts.
## Crew Role
**Producer** in the `prompt_template` production crew. I receive type definitions from P06 type_def builders and produce P03 artifacts consumed by LangChain PromptTemplate, DSPy Signature, Mustache renderers, and Jinja2 pipelines.

### bld_instruction_prompt_template.md
---
id: p03_ins_prompt_template
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Prompt Template Builder Instructions
target: "prompt-template-builder agent"
phases_count: 4
prerequisites:
  - "Input describes a prompt with at least one dynamic slot (a value that changes per invocation)"
  - "Target rendering engine is known or inferable (mustache, bracket, jinja2, langchain, dspy)"
  - "Domain of the template is identifiable (e.g. research, code, marketing, knowledge)"
validation_method: checklist
domain: prompt_template
quality: null
tags: [instruction, prompt-template, P03, parameterization, reusable]
idempotent: true
atomic: false
rollback: "Delete the produced .md file. No side effects — templates are inert until rendered."
dependencies: []
logging: true
tldr: "Extract variable slots, compose a reusable mustache template with full frontmatter, validate all 8 HARD gates, then deliver."
density_score: 0.93
---

## Context
A **prompt_template** is a reusable mold: a prompt body where dynamic values are represented as named placeholders (`{{variable}}`). The same template produces many distinct prompts by substituting different values at invocation time. This builder operates at the prompt layer — above identity definitions (system_prompt) and below live execution.
**Inputs**
| Field | Type | Description |
|---|---|---|
| `raw_prompt` | string | The prompt or prompt sketch provided by the caller |
| `target_engine` | string | `mustache` (default) or `bracket` (only when `{{}}` conflicts with target system) |
| `domain` | string | Subject area the template serves (e.g. `code_review`, `summarization`, `research`) |
| `composable` | boolean | True if this template is designed to be embedded inside a larger template |
**Output**
A single `.md` file conforming to SCHEMA.md and OUTPUT_TEMPLATE.md. Contains YAML frontmatter (16 fields) + 5 mandatory body sections: Purpose, Variables Table, Template Body, Quality Gates, Examples.
**Boundary rules**
- If the input has zero variable slots → it is a fixed `user_prompt`, not a template. Reject and explain.
- If the input defines an agent's identity/persona → it is a `system_prompt`. Route there.
- If the input generates or improves other prompts → it is a `meta_prompt`. Route there.
## Phases
### Phase 1: Analyze — Extract Variables
Scan `raw_prompt` and identify every value that will differ between invocations.
```
FOR each token or phrase in raw_prompt:
  IF the value is domain-specific, caller-supplied, or context-dependent:
    mark as candidate variable
  ELSE (always the same regardless of invocation):
    mark as literal text
IF candidate_variables.count == 0:
  RETURN error: "No dynamic slots found. This is a fixed prompt, not a template."
FOR each candidate variable:
  name        <- snake_case descriptor (e.g. topic, audience, word_limit)
  type        <- string | list | integer | boolean | object
  required    <- true if omitting breaks the prompt; false otherwise
  default     <- concrete value for optional vars; null for required vars
  description <- one sentence stating the variable's purpose
variable_syntax:
  USE "mustache"  by default  ->  {{variable_name}}
  USE "bracket"   only when target system reserves {{ }} -> [VARIABLE_NAME]
composable:
  true  if this template will be embedded in a larger template
  false otherwise (default)
```
Deliverable: variable registry with name, type, required, default, description for every slot.
### Phase 2: Classify — Boundary Check
Confirm the artifact is `prompt_template` and not a sibling kind.
```
IF prompt defines agent role, values, or personality:
  RETURN "This is a system_prompt — route to system-prompt builder."
IF prompt is invoked once with no variable substitution:
  RETURN "This is a user_prompt — no template needed."
IF prompt's purpose is to generate or refine other prompts:
  RETURN "This is a meta_prompt — route to meta-prompt builder."
IF variables.count >= 1 AND body will be rendered repeatedly:
  PROCEED as prompt_template
```
Deliverable: confirmed `kind: prompt_template` with one-line justification.
### Phase 3: Compose — Build the Artifact
Assemble frontmatter and all 5 required body sections using OUTPUT_TEMPLATE.md as the structural guide.
```
ID generation:
  id = "p03_pt_" + topic_slug
  topic_slug: lowercase, underscores, describes template purpose
  pattern must match: ^p03_pt_[a-z][a-z0-9_]+$
Frontmatter (all 16 fields from SCHEMA.md):
  id, kind, pillar, title, version, created, updated, author,
  variables (list of objects), variable_syntax, composable,
  domain, quality (= null), tags, tldr, keywords, density_score
Body sections (in this order):
  ## Purpose
    One paragraph: what this template produces and its reuse scope.
  ## Variables Table
    Markdown table with columns: name | type | required | default | description
    One row per variable from Phase 1.
  ## Template Body
    Fenced code block containing the parameterized prompt text.
    Apply syntax: mustache -> {{variable_name}}, bracket -> [VARIABLE_NAME]
    Every variable from the table must appear at least once here.
    No hard-coded values where a variable slot was identified.
  ## Quality Gates
    Table: gate | status | notes
    Fill H01-H08 status as PASS or FAIL with one-line note each.
  ## Examples
    At least one filled example:
      - Variables block (yaml): concrete values for each variable
      - Rendered Output block: the actual prompt text after substitution
```
Deliverable: complete `.md` file with frontmatter + 5 body sections.
### Phase 4: Validate — Gate Check
Run all quality gates before delivering.
```
HARD gates (all must pass — fix before delivering):
  H01: id matches ^p03_pt_[a-z][a-z0-9_]+$
  H02: all frontmatter required fields present (id, kind, title, variables, quality)
  H03: no {{var}} in template body that is absent from variables list
  H04: no variable in variables list that is absent from template body
  H05: file size <= 8192 bytes
  H06: variable_syntax is "mustache" or "bracket" (not mixed)

### bld_knowledge_card_prompt_template.md
---
kind: knowledge_card
id: bld_knowledge_card_prompt_template
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for prompt_template production — atomic searchable facts
sources: prompt-template-builder MANIFEST.md + SCHEMA.md, LangChain, Mustache, Jinja2
---

# Domain Knowledge: prompt_template
## Executive Summary
Prompt templates are parameterized text molds where fixed structure and dynamic content are separated via typed {{variable}} slots filled at invocation time. The same template produces N distinct prompts by substituting different variable values — this is the core reuse contract. They differ from system prompts (fixed identity, no slots), user prompts (one-time tasks), few-shot examples (fixed examples), and meta-prompts (which generate other prompts) by being reusable molds with declared, typed variable slots.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompts) |
| Kind | `prompt_template` (exact literal) |
| ID pattern | `p03_pt_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 8 HARD + 10 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Min variables | 1 (at least one {{variable}} slot) |
| Injection point | `system` or `user` |
| Tier-1 syntax | `{{variable}}` (Mustache-compatible) |
| Tier-2 syntax | `[VARIABLE]` (when Mustache conflicts) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Uniform syntax | All {{}} Mustache OR all [] bracket — never mixed in one template |
| Typed variables | Declare type (string, list, integer, boolean, object) for validation |
| Required vs optional | Required variables have no default; optional carry default value |
| Injection point | Declare system or user — determines where in conversation template lands |
| Composability | Template designed for embedding in larger templates via partials |
| Idempotency | Same template + same variables MUST always produce same rendered prompt |
| Variable-body match | Every {{variable}} in body must be declared in Variables section |
| Rendering pipeline | Template -> variable substitution -> rendered prompt -> LLM call |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No {{variable}} in body | Not a template — it's a fixed prompt |
| Undeclared variable in body | Variable present in body but missing from Variables section |
| Mixed syntax ({{}} and []) | Inconsistent; tools cannot reliably extract all variables |
| Hardcoded content in variable slots | Slots must be empty placeholders only |
| No injection_point declared | Consumer doesn't know where to place rendered text |
| Variables without constraints | No type/enum/regex means any value accepted — fragile |
| Template with side effects | Templates must be pure text transformation, no side effects |
## Application
1. Identify the reuse contract: what varies between invocations?
2. Extract variables: name, type, required/optional, constraints
3. Choose syntax tier: {{variable}} (tier-1) or [VARIABLE] (tier-2)
4. Set injection_point: system or user
5. Write template body with all variable slots as empty placeholders
6. Provide at least one complete invocation example with all slots filled
7. Declare output format (what rendered template produces)
8. Validate: all body vars declared, 8 HARD + 10 SOFT gates, body <= 4096 bytes
## References
- prompt-template-builder SCHEMA.md v1.0.0
- LangChain PromptTemplate / ChatPromptTemplate
- Mustache specification (logic-less templates)
- Jinja2 template engine documentation

### bld_quality_gate_prompt_template.md
---
id: p11_qg_prompt_template
kind: quality_gate
pillar: P11
title: "Gate: Prompt Template"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: prompt_template
quality: null
density_score: 0.85
tags:
  - quality-gate
  - prompt-template
  - p11
  - variables
  - reusable
tldr: "Quality gate for reusable prompt molds with typed {{variables}}, injection points, and composable structure."
---

## Definition
A prompt template is a reusable text mold containing one or more `{{variable}}` placeholders filled at invocation time. It declares where in the conversation it is injected (system or user turn), documents each variable's type and constraints, and provides at least one complete invocation example with all slots filled.
Scope: files with `kind: prompt_template`. Does not apply to system prompts (fixed text, no slots) or instruction files (behavioral rules, no variable slots).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p03_pt_*` | `id.startswith("p03_pt_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `prompt_template` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | Body contains at least one `{{variable}}` placeholder | `re.search(r'\{\{[a-z_]+\}\}', body)` matches |
| H08 | Every `{{variable}}` in body is declared in the Variables section | set(body_vars) == set(declared_vars) |
| H09 | Injection point declared as `system` or `user` | `injection_point` field equals `system` or `user` |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Every variable has at least one constraint (enum, regex, max_len, or range) | 1.0 |
| 3  | Syntax is uniform throughout (all `{{}}` Mustache or all `[]` bracket, never mixed) | 1.0 |
| 4  | Complete invocation example present with every variable slot filled | 1.0 |
| 5  | Default values documented for all optional variables | 0.5 |
| 6  | Tags list includes `prompt-template` | 0.5 |
| 7  | Scope note confirms this is not a system_prompt and not an instruction | 1.0 |
| 8  | Output format specified (what the rendered template is expected to produce) | 1.0 |
| 9  | Template is composable — no hard-coded surrounding structure that prevents embedding | 0.5 |
| 10 | No hardcoded content placed inside variable slots (slots are empty placeholders only) | 1.0 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; add to curated prompt library |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Template is a one-off migration aid with a documented lifespan under 30 days |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 30 days from bypass grant; template must be retired or brought to full compliance |

### bld_schema_prompt_template.md
---
id: schema_prompt_template_builder
kind: type_def
pillar: P06
llm_function: CONSTRAIN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [schema, prompt-template, P03, source-of-truth]
---

# Schema — prompt-template-builder
> SOURCE OF TRUTH. All fields in this file MUST appear in OUTPUT_TEMPLATE.md. Zero drift permitted.
## ID Pattern
```
^p03_pt_[a-z][a-z0-9_]+$
```
Examples: `p03_pt_knowledge_card`, `p03_pt_research_synthesis`, `p03_pt_code_review`
## Frontmatter Fields
| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| id | string | YES | — | Unique identifier. Must match ID pattern above |
| kind | enum | YES | — | Fixed value: `prompt_template` |
| pillar | enum | YES | — | Fixed value: `P03` |
| title | string | YES | — | Human-readable name of the template |
| version | string | YES | `"1.0.0"` | Semver string |
| created | string | YES | — | ISO date: YYYY-MM-DD |
| updated | string | YES | — | ISO date: YYYY-MM-DD, updated on every change |
| author | string | YES | — | Satellite or human author ID |
| variables | list[object] | YES | — | List of variable definitions (see Variable Object below) |
| variable_syntax | enum | YES | `"mustache"` | `"mustache"` or `"bracket"` |
| composable | boolean | YES | `false` | True if template is designed for embedding in larger templates |
| domain | string | YES | — | Semantic domain: research, marketing, knowledge, code, etc. |
| quality | float or null | YES | `null` | Gate score 0.0-1.0; null until first validation |
| tags | list[string] | YES | `[]` | Searchability tags |
| tldr | string | YES | — | One-sentence summary for discovery |
| keywords | list[string] | REC | `[]` | Search keywords distinct from tags |
| density_score | float | REC | `null` | Content density 0.0-1.0; null until measured |
## Variable Object
Each item in the `variables` list MUST contain:
| Field | Type | Required | Description |
|---|---|---|---|
| name | string | YES | Variable name matching the slot in the template body |
| type | enum | YES | `string`, `list`, `integer`, `boolean`, `object` |
| required | boolean | YES | Whether the variable must be supplied at render time |
| default | any or null | YES | Default value; null for required variables |
| description | string | YES | One sentence describing the variable's purpose |
## Body Structure
Every `prompt_template` artifact MUST contain these 5 sections in order:
1. `## Purpose` — one paragraph describing what the template produces and its reuse scope
2. `## Variables Table` — markdown table listing all variables with all 5 object fields
3. `## Template Body` — the parameterized prompt text in a fenced code block
4. `## Quality Gates` — table showing H01-H08 gate status for this artifact
5. `## Examples` — at least one filled example with variable values and rendered output
## Constraints
| Constraint | Rule |
|---|---|
| max_bytes | 8192 bytes per file |
| variable_syntax | `mustache` is tier-1 (`{{var}}`); `bracket` is tier-2 (`[VAR]`) — use bracket only when Mustache conflicts with target system |
| body completeness | Every `{{var}}` in the body MUST be declared in `variables`. Every declared variable MUST appear in the body at least once. |
| id uniqueness | No two prompt_template artifacts may share the same id |
| kind lock | The `kind` field MUST be `prompt_template` — never overridden |
| quality null | `quality: null` is valid for draft artifacts; must be a float before pool submission |
## Enum Values
### variable_syntax
- `mustache` — `{{variable}}` syntax (Mustache, Handlebars, Anthropic-compatible)
- `bracket` — `[VARIABLE]` syntax (fallback for systems where `{{}}` is reserved)
### variable.type
- `string` — plain text
- `list` — array of items
- `integer` — whole number
- `boolean` — true/false
- `object` — structured key-value data

### bld_examples_prompt_template.md
---
id: examples_prompt_template_builder
kind: examples
pillar: P07
llm_function: GOVERN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [examples, prompt-template, P03, golden, anti-example]
---

# Examples — prompt-template-builder
## Golden Example
A complete, valid `prompt_template` artifact with 19+ fields.
```yaml
id: p03_pt_knowledge_card_production
kind: prompt_template
pillar: P03
title: "Knowledge Card Production Template"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: knowledge-engine
variables:
  - name: topic
    type: string
    required: true
    default: null
    description: The subject or concept the knowledge card will cover
  - name: domain
    type: string
    required: true
    default: null
    description: The knowledge domain (e.g., machine_learning, finance, biology)
  - name: audience
    type: string
    required: false
    default: "intermediate"
    description: Target reader level (beginner, intermediate, expert)
  - name: max_sections
    type: integer
    required: false
    default: 5
    description: Maximum number of body sections to generate
  - name: include_examples
    type: boolean
    required: false
    default: true
    description: Whether to include concrete examples in each section
  - name: source_refs
    type: list
    required: false
    default: []
    description: List of source URLs or citation keys to incorporate
variable_syntax: "mustache"
composable: false
domain: knowledge
quality: 0.92
tags: [knowledge-card, pytha, production, parameterized]
tldr: "Generates a structured knowledge card for any topic and domain with configurable depth."
keywords: [knowledge, card, synthesis, structured, reusable, topic]
density_score: 0.87
# Knowledge Card Production Template
## Purpose
Produces a structured knowledge card for any topic within a specified domain. Reuse scope: any subject requiring a dense, well-organized reference document. Invoke once per topic; vary `topic`, `domain`, and `audience` to produce distinct cards from the same mold.
## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| topic | string | true | null | The subject or concept the knowledge card will cover |
| domain | string | true | null | The knowledge domain (e.g., machine_learning, finance) |
| audience | string | false | "intermediate" | Target reader level (beginner, intermediate, expert) |
| max_sections | integer | false | 5 | Maximum number of body sections to generate |
| include_examples | boolean | false | true | Whether to include concrete examples in each section |
| source_refs | list | false | [] | List of source URLs or citation keys to incorporate |
## Template Body
```
You are a knowledge synthesis expert. Produce a knowledge card for the following topic.
Topic: {{topic}}
Domain: {{domain}}
Audience level: {{audience}}
Maximum sections: {{max_sections}}
Include examples: {{include_examples}}
Source references: {{source_refs}}
Structure your output as follows:
1. TLDR (1 sentence)
2. Core Definition (2-3 sentences, precise, domain-appropriate)
3. Key Concepts (up to {{max_sections}} bullet points)
4. Relationships (how {{topic}} connects to adjacent concepts in {{domain}})
5. Common Misconceptions (2-3 items, audience-calibrated for {{audience}})
{{#include_examples}}
6. Concrete Examples (2-3 examples grounded in {{domain}})
{{/include_examples}}
7. References: {{source_refs}}
Calibrate terminology and depth for a {{audience}}-level reader in {{domain}}.
```
## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 id pattern | PASS | `p03_pt_knowledge_card_production` matches `^p03_pt_[a-z][a-z0-9_]+$` |
| H02 required fields | PASS | id, kind, title, variables, quality all present |
| H03 no undeclared vars | PASS | All `{{vars}}` in body declared in variables list |
| H04 no unused vars | PASS | All 6 declared variables appear in template body |
| H05 size <= 8192 bytes | PASS | ~1.8KB |
| H06 valid syntax tier | PASS | variable_syntax: mustache |

### bld_config_prompt_template.md
---
id: config_prompt_template_builder
kind: config
pillar: P09
llm_function: CONSTRAIN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [config, prompt-template, P03, naming, constraints]
---

# Config — prompt-template-builder
## Naming Convention
**Pattern**: `p03_pt_{topic_slug}.md`
| Component | Rule |
|---|---|
| `p03` | Pillar prefix — always P03 for prompt layer |
| `pt` | Kind abbreviation — always `pt` for prompt_template |
| `{topic_slug}` | Lowercase, underscored, 2-5 words describing the template purpose |
| `.md` | Always markdown |
**Valid examples**:
- `p03_pt_knowledge_card_production.md`
- `p03_pt_research_synthesis.md`
- `p03_pt_code_review_checklist.md`
- `p03_pt_marketing_copy_generator.md`
**Invalid examples**:
- `prompt_template_knowledge.md` — missing pillar prefix
- `p03_knowledge_card.md` — missing kind abbreviation `pt`
- `p03_pt_KnowledgeCard.md` — uppercase not allowed
- `p03_pt_k.md` — topic_slug too short (min 2 chars after pt_)
## File Paths
| Context | Path |
|---|---|
| Pool artifacts | `records/pool/prompts/p03_pt_{topic_slug}.md` |
| Draft / WIP | `records/pool/drafts/p03_pt_{topic_slug}.md` |
| Builder reference | `archetypes/builders/prompt-template-builder/` |
## Size Limits
| Limit | Value | Scope |
|---|---|---|
| max_bytes | 8192 | Per artifact file |
| max_variables | 20 | Per template (practical limit; no hard schema cap) |
| max_body_lines | 80 | Recommended; keep templates scannable |
| min_variables | 1 | A template with zero variables is a user_prompt, not a template |
## Variable Syntax Rules
### Tier-1: Mustache (default)
```
{{variable_name}}
```
Use for: all new templates. Compatible with Mustache, Handlebars, Anthropic prompt libraries, and most CEX renderers.
**Conditional blocks** (Mustache):
```
{{#boolean_var}}
  Content shown when boolean_var is true
{{/boolean_var}}
```
**List iteration** (Mustache):
```
{{#items}}
  - {{.}}
{{/items}}
```
### Tier-2: Bracket (fallback)
```
[VARIABLE_NAME]
```
Use for: templates targeting systems where `{{}}` is reserved syntax (e.g., Vue.js templates, some shell scripts, Go HTML templates).
### Mixing Tiers
NEVER mix tier-1 and tier-2 syntax in the same template. Set `variable_syntax` to either `mustache` or `bracket` and use exclusively.
## Version Increment Rules
| Change type | Version bump |
|---|---|
| Add new optional variable | patch (1.0.0 → 1.0.1) |
| Add new required variable | minor (1.0.0 → 1.1.0) |
| Remove or rename variable | major (1.0.0 → 2.0.0) |
| Change template body structure | minor (1.0.0 → 1.1.0) |
| Fix typo or formatting | patch (1.0.0 → 1.0.1) |

### bld_architecture_prompt_template.md
---
kind: architecture
id: bld_architecture_prompt_template
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prompt_template — inventory, dependencies, and architectural position
---

# Architecture: prompt_template in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, variables, syntax_tier, etc.) | prompt-template-builder | active |
| variable_declarations | Typed variable slots with names, types, defaults, and descriptions | author | active |
| template_body | Parameterized text with {{variable}} or [VAR] placeholders | author | active |
| syntax_tier | Interpolation syntax level (tier-1 Mustache, tier-2 bracket) | author | active |
| rendering_context | Runtime context required to fill variables (data sources, APIs) | author | active |
| example_fills | Concrete variable fills demonstrating valid template usage | author | active |
## Dependency Graph
```
type_def        --produces-->  prompt_template  --consumed_by-->  renderer
knowledge_card  --produces-->  prompt_template  --produces-->     filled_prompt
prompt_template --signals-->   render_error
```
| From | To | Type | Data |
|------|----|------|------|
| type_def (P06) | prompt_template | data_flow | type definitions for variable constraints |
| knowledge_card (P01) | prompt_template | data_flow | domain facts injected as variable values |
| prompt_template | renderer (LangChain/DSPy/Mustache) | consumes | template consumed by rendering engine |
| prompt_template | filled_prompt | produces | concrete prompt after variable substitution |
| prompt_template | render_error (P12) | signals | emitted when variable fill fails validation |
| system_prompt (P03) | prompt_template | dependency | system identity may constrain template scope |
## Boundary Table
| prompt_template IS | prompt_template IS NOT |
|--------------------|------------------------|
| A reusable mold with {{variable}} slots for multiple invocations | A one-time task instruction (action_prompt P03) |
| Structure separated from content via parameterization | A fixed system identity definition (system_prompt P03) |
| Rendered by LangChain, DSPy, Mustache, or Jinja2 engines | A step-by-step recipe without variables (instruction P03) |
| Variable-typed with defaults and validation constraints | A raw user message without structure |
| Invoked multiple times with different variable fills | A single-use prompt discarded after execution |
| Produces filled prompts — not direct LLM responses | A meta-prompt that generates other prompts |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Types | type_def | Supply type definitions for variable constraints |
| Definition | frontmatter, variable_declarations, syntax_tier | Specify template identity and variable slots |
| Template | template_body, example_fills | The parameterized text and usage examples |
| Rendering | rendering_context, renderer | Runtime fill and template engine execution |
| Output | filled_prompt, render_error | Concrete prompt produced or error signaled |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `prompt-template-builder` for pipeline function `REASON`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
