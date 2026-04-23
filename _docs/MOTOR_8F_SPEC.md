# 8F ENGINE -- Complete Spec
**Status**: SPEC | **Version**: 1.0.0 | **Author**: knowledge_agent | **Created**: 2026-03-28
**Quality**: 9.2 | **Source**: LLM_PIPELINE.md + TAXONOMY_LAYERS.yaml + 71 builders

---

## What Is the 8F Engine

The 8F Engine is the algorithm that receives an **intent** (natural language string)
and produces a structured **execution plan**: which builders to activate, in what order,
with which dependencies, to satisfy the 8 functions of the LLM pipeline.

```
intent string
     |
     v
  [8F ENGINE]
     |
     +-- PARSE    (extracts verb, object, domain, quality)
     +-- CLASSIFY (maps object -> CEX kinds)
     +-- FAN-OUT  (functions -> required builders)
     +-- PLAN     (orders by dependency)
     +-- OUTPUT   (JSON execution plan)
     |
     v
execution_plan.json
```

---

## 1. Decomposition Algorithm

### Step 1: PARSE

Extract 4 fields from the intent string:

| Field | Description | Example |
|-------|-------------|---------|
| `verb` | Main action (infinitive) | create, improve, rebuild, analyze |
| `object` | Target artifact or entity | agent, workflow, knowledge card |
| `domain` | Application domain | sales, research, marketing |
| `quality_target` | Expected score (default 9.0) | 9.0, 9.5 |

**Parse rules:**
- Verb: first imperative verb found. If absent, infer from context ("sales agent" -> "create")
- Object: main noun after verb. May be plural or have qualifiers
- Domain: business entity or technical context after "for", "of", "in"
- Quality: extract from decimal numbers in the intent. Default: 9.0

**Examples:**

```
"create sales agent for ML"
  -> verb: "create", object: "agent", domain: "sales/ML", quality: 9.0

"improve the quality of the onboarding knowledge card"
  -> verb: "improve", object: "knowledge_card", domain: "onboarding", quality: 9.0

"rebuild the knowledge-card-builder with score 9.5"
  -> verb: "rebuild", object: "knowledge-card-builder", domain: "meta", quality: 9.5

"create agent AND research workflow"
  -> verb: "create", object: ["agent", "workflow"], domain: "research", quality: 9.0
```

---

### Step 2: CLASSIFY

Map `object` to CEX `kind(s)` using TAXONOMY_LAYERS.yaml:

| Object Keyword | Primary Kind(s) | Pillar | Function |
|----------------|-----------------|--------|----------|
| agent | agent | P02 | BECOME |
| system, agent_group | agent_card | P08 | BECOME |
| prompt, instruction | system_prompt, instruction | P03 | BECOME/REASON |
| workflow, pipeline | workflow | P12 | COLLABORATE |
| knowledge | knowledge_card | P01 | INJECT |
| rag, source | rag_source | P01 | INJECT |
| skill, ability | skill | P04 | CALL |
| tool | cli_tool, mcp_server | P04 | CALL |
| evaluation, eval, test | unit_eval, e2e_eval | P07 | GOVERN |
| schema, contract | input_schema, interface | P06 | CONSTRAIN |
| signal | signal | P12 | COLLABORATE |
| handoff | handoff | P12 | COLLABORATE |
| model | model_card | P02 | BECOME |
| rule | law, runtime_rule | P08/P09 | CONSTRAIN |
| guardrail, restriction | guardrail | P11 | GOVERN |
| chain | chain | P03 | REASON |
| router, routing | router | P02 | REASON |
| dag, graph | dag | P12 | COLLABORATE |
| spawn, launch | spawn_config | P12 | COLLABORATE |
| iso, package | agent_package | P02 | BECOME |
| connector, api | connector, client | P04 | CALL |
| lens, perspective | lens | P02 | BECOME |
| memory | knowledge_index, session_state | P10 | INJECT |
| glossary | glossary_entry | P01 | INJECT |
| axiom | axiom | P10 | INJECT |

**Verb classification:**

| Verb | Extra Builders Activated |
|------|--------------------------|
| create | builders for the primary kind |
| improve | quality-gate-builder + kind builders |
| rebuild | _builder-builder + kind builders |
| analyze | scoring-rubric-builder + unit-eval-builder |
| validate | validator-builder + quality-gate-builder |
| document | knowledge-card-builder + context-doc-builder |
| integrate | connector-builder + interface-builder |

---

### Step 3: FAN-OUT

For each classified kind, expand to the 8 functions and select builders:

**Selection rule by tier:**
- **ALWAYS** (primary): Builders without which the artifact cannot exist
- **IF_MENTIONED**: Builders activated if the intent mentions specific keywords
- **OPTIONAL**: Builders that elevate quality but are not mandatory

See Section 2 for the complete Mapping Tables.

---

### Step 4: PLAN

Order builders by dependency:

```
Mandatory execution order:
1. CONSTRAIN first (schemas define the contract)
2. BECOME second (identity assumes the schema)
3. INJECT third (context populates the agent)
4. REASON fourth (reasoning logic)
5. CALL fifth (available tools)
6. PRODUCE sixth (generates output)
7. GOVERN seventh (validates quality)
8. COLLABORATE last (propagates result)

Parallelism allowed WITHIN each function.
Never parallel BETWEEN functions (the order of the 8 is sequential).
```

**Dependency rules between builders:**
- `validation-schema-builder` BEFORE `validator-builder` (schema before rule)
- `system-prompt-builder` AFTER `agent-builder` (identity before instruction)
- `knowledge-card-builder` BEFORE `rag-source-builder` (content before source)
- `quality-gate-builder` BEFORE `scoring-rubric-builder` (gate defines the rubric)
- `signal-builder` AFTER `workflow-builder` (signal presupposes workflow)
- `few-shot-example-builder` AFTER `output-template` (examples follow template)

---

### Step 5: OUTPUT

Generate JSON execution plan (see complete Schema in Section 3).

---

## 2. Mapping Tables -- All 71 Builders

> Each builder appears in at least 1 function. Multi-function builders appear
> at the highest tier of each function where they are relevant.

### BECOME -- "Who am I?"
*Configures identity, persona, rules, model before everything else*
*Pillars: P02 (Model), P03 (Prompt)*

| Tier | Builders |
|------|---------|
| **primary** | agent-builder, system-prompt-builder, model-card-builder, boot-config-builder, agent-package-builder |
| **secondary** | mental-model-builder, router-builder, fallback-chain-builder, lens-builder, supervisor-builder* |
| **optional** | _builder-builder (meta-bootstrap only) |

> *supervisor-builder: manifest id=`agent-card-builder`, pillar=P08, domain=agent_card.
> Activate when intent mentions "agent_group" or "complete system".

---

### INJECT -- "What do I know?"
*Provides context and knowledge to the LLM before reasoning*
*Pillars: P01 (Knowledge), P10 (Memory)*

| Tier | Builders |
|------|---------|
| **primary** | knowledge-card-builder, rag-source-builder, context-doc-builder, few-shot-example-builder |
| **secondary** | glossary-entry-builder, embedding-config-builder, knowledge-index-builder, learning-record-builder, axiom-builder |
| **optional** | runtime-state-builder, session-state-builder, mental-model-builder (P10 aspect) |

---

### REASON -- "How do I think?"
*Reasons, plans, decomposes before acting*
*Pillars: P03 (Prompt)*

| Tier | Builders |
|------|---------|
| **primary** | instruction-builder, chain-builder, prompt-template-builder |
| **secondary** | action-prompt-builder, router-builder, dag-builder |
| **optional** | supervisor-builder (orchestration planning) |

---

### CALL -- "What tools do I use?"
*Invokes tools, APIs, CLIs, MCPs*
*Pillars: P04 (Tools)*

| Tier | Builders |
|------|---------|
| **primary** | skill-builder, mcp-server-builder, cli-tool-builder, connector-builder, scraper-builder, client-builder |
| **secondary** | hook-builder, plugin-builder, daemon-builder |
| **optional** | *(none)* |

---

### PRODUCE -- "What do I generate?"
*Produces final output -- text, code, structured data*
*Pillars: P05 (Output)*

| Tier | Builders |
|------|---------|
| **primary** | response-format-builder, formatter-builder, parser-builder |
| **secondary** | naming-rule-builder, action-prompt-builder |
| **optional** | chain-builder (when chain is the final output) |

---

### CONSTRAIN -- "Is it in the right format?"
*Validates against schemas, rules, contracts*
*Pillars: P06 (Schema), P08 (Architecture), P09 (Config)*

| Tier | Builders |
|------|---------|
| **primary** | validator-builder, input-schema-builder, interface-builder, validation-schema-builder, type-def-builder, validator-builder-codex |
| **secondary** | invariant-builder, pattern-builder, guardrail-builder, component-map-builder, diagram-builder |
| **optional** | env-config-builder, path-config-builder, feature-flag-builder, runtime-rule-builder, permission-builder |

---

### GOVERN -- "Did it pass the quality gate?"
*Quality gates, evals, benchmarks, feedback loops*
*Pillars: P07 (Evals), P11 (Feedback)*

| Tier | Builders |
|------|---------|
| **primary** | quality-gate-builder, scoring-rubric-builder, golden-test-builder, unit-eval-builder, e2e-eval-builder |
| **secondary** | benchmark-builder, smoke-eval-builder, lifecycle-rule-builder, optimizer-builder, bugloop-builder |
| **optional** | guardrail-builder (safety boundary), permission-builder (access control) |

---

### COLLABORATE -- "Who receives it?"
*Signals, delegates, propagates to the next agent*
*Pillars: P12 (Orchestration)*

| Tier | Builders |
|------|---------|
| **primary** | signal-builder, handoff-builder, workflow-builder, spawn-config-builder, dispatch-rule-builder |
| **secondary** | dag-builder, hook-builder |
| **optional** | supervisor-builder (high-level orchestration) |

---

### Coverage: Validation

| Function | Primary | Secondary | Optional | Total |
|----------|---------|-----------|----------|-------|
| BECOME | 5 | 5 | 1 | 11 |
| INJECT | 4 | 5 | 3 | 12 |
| REASON | 3 | 3 | 1 | 7 |
| CALL | 6 | 3 | 0 | 9 |
| PRODUCE | 3 | 2 | 1 | 6 |
| CONSTRAIN | 6 | 5 | 5 | 16 |
| GOVERN | 5 | 5 | 2 | 12 |
| COLLABORATE | 5 | 2 | 1 | 8 |

> Multi-function builders (appear in >1 function):
> - mental-model-builder: BECOME (P02) + INJECT (P10)
> - router-builder: BECOME (P02 identity) + REASON (routing logic)
> - action-prompt-builder: REASON (planning) + PRODUCE (output)
> - chain-builder: REASON (logical sequence) + PRODUCE (final output)
> - guardrail-builder: CONSTRAIN (validation) + GOVERN (safety gate)
> - permission-builder: CONSTRAIN (P09) + GOVERN (P11)
> - dag-builder: REASON (dependency planning) + COLLABORATE (P12)
> - hook-builder: CALL (P04 event trigger) + COLLABORATE (P12 lifecycle)
> - supervisor-builder: BECOME (agent_group spec) + REASON (orchestration planning) + COLLABORATE

> **builders_unassigned: []** -- all 71 builders are mapped.

---

## 3. Plan Format -- JSON Schema

```json
{
  "$schema": "https://cex.dev/schemas/execution_plan/v1",
  "intent": "string -- original intent unchanged",
  "parsed": {
    "verb": "string -- extracted main action",
    "object": "string | string[] -- target artifact(s)",
    "domain": "string -- application domain",
    "quality": "number -- target score (default: 9.0)",
    "multi_object": "boolean -- true if object is array"
  },
  "classified_kinds": [
    {
      "object": "string",
      "kind": "string -- CEX kind from TAXONOMY_LAYERS.yaml",
      "pillar": "string -- P01..P12",
      "primary_function": "string -- BECOME|INJECT|REASON|CALL|PRODUCE|CONSTRAIN|GOVERN|COLLABORATE"
    }
  ],
  "functions": [
    {
      "name": "string -- BECOME|INJECT|REASON|CALL|PRODUCE|CONSTRAIN|GOVERN|COLLABORATE",
      "position": "number -- 1..8 (pipeline order)",
      "builders": [
        {
          "id": "string -- builder name (e.g.: agent-builder)",
          "tier": "string -- primary|secondary|optional",
          "active": "boolean -- true if should be activated in this plan",
          "reason": "string -- why it was selected"
        }
      ],
      "deps": "string[] -- names of functions that must complete before",
      "parallel": "boolean -- true if builders in this function run in parallel",
      "estimated_tokens": "number"
    }
  ],
  "total_builders": "number -- builders with active:true",
  "estimated_tokens": "number -- sum of estimated_tokens from all functions",
  "warnings": "string[] -- detected edge cases"
}
```

**Complete example -- "create sales agent for ML":**

```json
{
  "intent": "create sales agent for ML",
  "parsed": {
    "verb": "create",
    "object": "agent",
    "domain": "sales/ML",
    "quality": 9.0,
    "multi_object": false
  },
  "classified_kinds": [
    {
      "object": "agent",
      "kind": "agent",
      "pillar": "P02",
      "primary_function": "BECOME"
    }
  ],
  "functions": [
    {
      "name": "CONSTRAIN",
      "position": 1,
      "builders": [
        {"id": "input-schema-builder", "tier": "primary", "active": true, "reason": "defines agent input contract"},
        {"id": "interface-builder", "tier": "primary", "active": true, "reason": "defines interface with other systems"},
        {"id": "validator-builder", "tier": "primary", "active": true, "reason": "validates agent conformance"}
      ],
      "deps": [],
      "parallel": true,
      "estimated_tokens": 8000
    },
    {
      "name": "BECOME",
      "position": 2,
      "builders": [
        {"id": "agent-builder", "tier": "primary", "active": true, "reason": "builds agent definition"},
        {"id": "system-prompt-builder", "tier": "primary", "active": true, "reason": "writes identity and rules"},
        {"id": "model-card-builder", "tier": "primary", "active": true, "reason": "selects appropriate LLM model"},
        {"id": "agent-package-builder", "tier": "primary", "active": true, "reason": "packages agent for deployment"},
        {"id": "boot-config-builder", "tier": "primary", "active": false, "reason": "not mentioned in intent"},
        {"id": "mental-model-builder", "tier": "secondary", "active": true, "reason": "routing map for sales agent"},
        {"id": "router-builder", "tier": "secondary", "active": false, "reason": "no complex routing mentioned"}
      ],
      "deps": ["CONSTRAIN"],
      "parallel": true,
      "estimated_tokens": 16000
    },
    {
      "name": "INJECT",
      "position": 3,
      "builders": [
        {"id": "knowledge-card-builder", "tier": "primary", "active": true, "reason": "sales and ML knowledge"},
        {"id": "context-doc-builder", "tier": "primary", "active": true, "reason": "sales domain context"},
        {"id": "few-shot-example-builder", "tier": "primary", "active": true, "reason": "interaction examples"},
        {"id": "rag-source-builder", "tier": "primary", "active": false, "reason": "no external RAG source mentioned"}
      ],
      "deps": ["BECOME"],
      "parallel": true,
      "estimated_tokens": 12000
    },
    {
      "name": "REASON",
      "position": 4,
      "builders": [
        {"id": "instruction-builder", "tier": "primary", "active": true, "reason": "agent operational instructions"},
        {"id": "chain-builder", "tier": "primary", "active": false, "reason": "no prompt chain mentioned"},
        {"id": "prompt-template-builder", "tier": "primary", "active": true, "reason": "sales action template"}
      ],
      "deps": ["INJECT"],
      "parallel": true,
      "estimated_tokens": 6000
    },
    {
      "name": "CALL",
      "position": 5,
      "builders": [
        {"id": "skill-builder", "tier": "primary", "active": true, "reason": "search and CRM skills"},
        {"id": "mcp-server-builder", "tier": "primary", "active": false, "reason": "no specific MCP mentioned"},
        {"id": "connector-builder", "tier": "primary", "active": false, "reason": "no external integration mentioned"}
      ],
      "deps": ["REASON"],
      "parallel": true,
      "estimated_tokens": 4000
    },
    {
      "name": "PRODUCE",
      "position": 6,
      "builders": [
        {"id": "response-format-builder", "tier": "primary", "active": true, "reason": "agent response format"},
        {"id": "formatter-builder", "tier": "primary", "active": false, "reason": "no special formatting mentioned"},
        {"id": "parser-builder", "tier": "primary", "active": false, "reason": "no output parsing mentioned"}
      ],
      "deps": ["CALL"],
      "parallel": true,
      "estimated_tokens": 3000
    },
    {
      "name": "GOVERN",
      "position": 7,
      "builders": [
        {"id": "quality-gate-builder", "tier": "primary", "active": true, "reason": "mandatory agent gates"},
        {"id": "scoring-rubric-builder", "tier": "primary", "active": true, "reason": "rubric for 9.0+ score"},
        {"id": "unit-eval-builder", "tier": "primary", "active": true, "reason": "agent unit tests"},
        {"id": "golden-test-builder", "tier": "primary", "active": true, "reason": "sales golden case"},
        {"id": "smoke-eval-builder", "tier": "secondary", "active": true, "reason": "quick pre-deploy sanity check"}
      ],
      "deps": ["PRODUCE"],
      "parallel": true,
      "estimated_tokens": 8000
    },
    {
      "name": "COLLABORATE",
      "position": 8,
      "builders": [
        {"id": "signal-builder", "tier": "primary", "active": true, "reason": "agent completion signal"},
        {"id": "handoff-builder", "tier": "primary", "active": true, "reason": "handoff to next step"},
        {"id": "dispatch-rule-builder", "tier": "primary", "active": false, "reason": "no routing policy mentioned"},
        {"id": "workflow-builder", "tier": "primary", "active": false, "reason": "no multi-step workflow mentioned"}
      ],
      "deps": ["GOVERN"],
      "parallel": true,
      "estimated_tokens": 4000
    }
  ],
  "total_builders": 16,
  "estimated_tokens": 61000,
  "warnings": []
}
```

---

## 4. Edge Cases

### 4.1 Intent with Multiple Objects

**Trigger**: `object` is an array (e.g.: "create agent AND research workflow")

**Algorithm:**
1. Parse returns `multi_object: true`, `object: ["agent", "workflow"]`
2. CLASSIFY runs for each object independently
3. FAN-OUT performs UNION of builders from all objects per function
4. Duplicate builders (same builder in both objects) are deduplicated
5. `estimated_tokens` multiplied by 1.6x factor (shared context overhead)

**Plan differential:**
- BECOME: agent-builder + system-prompt-builder + workflow-builder (P12, BECOME aspect)
- COLLABORATE: workflow-builder (P12, primary) -- already active from workflow object
- Warning: `"multi_object: complexity increases 60%. Consider splitting into 2 plans."`

---

### 4.2 Intent without Clear Domain

**Trigger**: `domain` is empty or generic (e.g.: "improve the quality")

**Algorithm:**
1. Parse returns `domain: "generic"` and `verb: "improve"`
2. CLASSIFY cannot map a specific object -- returns kind `quality_gate`
3. FAN-OUT activates predominantly the GOVERN function
4. Verb "improve" activates quality-gate-builder + scoring-rubric-builder always
5. Warning: `"domain not identified -- plan focused on GOVERN. Specify the target artifact."`

**Active builders (minimum):**
- GOVERN: quality-gate-builder (primary), scoring-rubric-builder (primary), benchmark-builder (secondary)
- CONSTRAIN: validator-builder (primary) -- always active to validate output
- COLLABORATE: signal-builder (primary) -- completion signal

---

### 4.3 Meta Intent (Rebuild the Builder)

**Trigger**: object is a CEX builder (e.g.: "rebuild the knowledge-card-builder")

**Algorithm:**
1. Parse returns `object: "knowledge-card-builder"`, `domain: "meta"`, `verb: "rebuild"`
2. CLASSIFY maps to special kind `type_builder` (meta-kind)
3. FAN-OUT activates _builder-builder as primary in BECOME
4. Builders of the original type (knowledge-card) become secondary in INJECT
5. Warning: `"meta intent detected -- activating _builder-builder. 13-file pipeline."`

**Active builders (meta-plan):**
- BECOME: _builder-builder (primary), agent-builder (secondary -- for MANIFEST.md)
- INJECT: knowledge-card-builder (secondary -- reference content)
- CONSTRAIN: validator-builder (primary), input-schema-builder (primary)
- GOVERN: quality-gate-builder (primary), golden-test-builder (primary)
- COLLABORATE: signal-builder (primary)

**Note**: In a meta intent, the OUTPUT is not an artifact of the kind, but 13 builder files.
`estimated_tokens` multiplied by 13x (one context per generated file).

---

## 5. Keyword Activation Rules

Words in the intent that activate secondary/optional builders:

| Keyword in Intent | Activated Builders |
|-------------------|-------------------|
| "with memory", "remember" | knowledge-index-builder, learning-record-builder |
| "with RAG", "knowledge base" | rag-source-builder, embedding-config-builder |
| "with fallback", "resilient" | fallback-chain-builder, runtime-rule-builder |
| "for agent_group", "complete system" | supervisor-builder (agent-card), spawn-config-builder |
| "with scraping", "extract data" | scraper-builder, parser-builder |
| "with API", "integrate with" | connector-builder, client-builder, interface-builder |
| "with CLI", "command line" | cli-tool-builder |
| "with MCP" | mcp-server-builder |
| "with dag", "dependencies" | dag-builder |
| "with hooks", "pre/post" | hook-builder |
| "with permissions", "access" | permission-builder |
| "with feature flags" | feature-flag-builder |
| "with benchmark" | benchmark-builder |
| "with e2e" | e2e-eval-builder |
| "golden test", "reference case" | golden-test-builder |
| "multilingual" | glossary-entry-builder |
| "with axioms", "inviolable" | axiom-builder, invariant-builder |
| "with lens", "perspective" | lens-builder |
| "with daemon", "background" | daemon-builder |
| "with plugin" | plugin-builder |
| "isolate", "portable" | agent-package-builder |
| "optimize", "continuous improvement" | optimizer-builder, bugloop-builder |
| "session", "ephemeral state" | session-state-builder |
| "diagram", "visual architecture" | diagram-builder |
| "components", "map" | component-map-builder |
| "pattern", "reusable" | pattern-builder |

---

## 6. Token Estimation per Builder

| Builder Complexity | Builders | Estimated Tokens |
|-------------------|----------|-----------------|
| Simple | signal-builder, dispatch-rule-builder, env-config-builder, session-state-builder, naming-rule-builder | ~2,000 |
| Medium | knowledge-card-builder, quality-gate-builder, skill-builder, instruction-builder, hook-builder | ~4,000 |
| Complex | agent-builder, workflow-builder, model-card-builder, agent-package-builder, e2e-eval-builder | ~8,000 |
| Meta | _builder-builder (13 files) | ~40,000 |

Formula: `estimated_tokens = sum(active_builders * complexity_tokens) * 1.2 (overhead)`

---

*MOTOR_8F_SPEC.md -- knowledge_agent Wave 6A | CEX v1.0.0 | 2026-03-28*
