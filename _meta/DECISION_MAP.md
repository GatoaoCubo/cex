# CEX Decision Map: File Category -> LP -> Type -> Machine Format

> **Given any file in codexa-core, this table tells you which LP type it is and what format to compile to.**

v1.0.0 | 2026-03-23 | 73 types across 12 LPs

---

## Quick Decision: "I have a file, which type is it?"

### P02 Agent ISO Pack (124 agents x 10+ files each)

| ISO File | LP | Type | machine_format |
|---|---|---|---|
| ISO_*_MANIFEST | P02 | `agent` | yaml |
| ISO_*_PRIME | P02 | `agent` | yaml |
| ISO_*_SYSTEM_INSTRUCTION | P03 | `system_prompt` | yaml |
| ISO_*_INSTRUCTIONS | P03 | `user_prompt` | yaml |
| ISO_*_EXAMPLES | P03 | `few_shot` | yaml |
| ISO_*_DOMAIN_KNOWLEDGE | P01 | `knowledge_card` | yaml |
| ISO_*_QUICK_START | P01 | `context_doc` | yaml |
| ISO_*_TOOLS_AND_APIS | P04 | `skill` | yaml |
| ISO_*_OUTPUT_TEMPLATE | P05 | `output_schema` | yaml |
| ISO_*_ERROR_HANDLING | P11 | `guardrail` | yaml |
| ISO_*_ARCHITECTURE | P08 | `component_map` | yaml |
| ISO_*_TESTING | P07 | `smoke_eval` | yaml |

### Satellite Files (7 satellites)

| File | LP | Type | machine_format |
|---|---|---|---|
| PRIME_*.md | P03 | `system_prompt` | yaml |
| mental_model.yaml | P02 | `mental_model` | yaml |
| boot/*.cmd | P02 | `boot_config` | yaml |
| .mcp-*.json | P04 | `mcp_server` | json |

### Pool Artifacts (2000+ files)

| Pool Category | LP | Type | machine_format |
|---|---|---|---|
| pool/knowledge/KC_*.md | P01 | `knowledge_card` | yaml |
| pool/prompts/HOP_*.md | P03 | `user_prompt` | yaml |
| pool/workflows/ADW_*.md | P03 | `chain` or P12 `workflow` | yaml |
| pool/blocks/BLK_*.md | P01 | `knowledge_card` | yaml |
| pool/reports/*.md | P07 | `benchmark` | yaml |
| pool/templates/*.md | P03 | `prompt_template` | yaml |
| pool/schemas/*.yaml | P06 | `type_def` | yaml |
| pool/contexts/*.md | P01 | `context_doc` | yaml |
| pool/routes/*.md | P03 | `router_prompt` | yaml |
| pool/skills/*.md | P04 | `skill` | yaml |

### Core/Framework Files

| File | LP | Type | machine_format |
|---|---|---|---|
| .claude/rules/*.md | P09 | `runtime_rule` | yaml |
| .claude/handoffs/*.md | P12 | `handoff` | yaml |
| .claude/signals/*.json | P12 | `signal` | json |
| LAWS_v3_PRACTICAL.md | P08 | `law` | yaml |
| MANDAMENTOS.md | P10 | `axiom` | yaml |
| GLOSSARY.md | P01 | `glossary_entry` | yaml |
| path_registry.json | P09 | `path_config` | yaml |
| .env | P09 | `env_config` | yaml |
| few_shot_bank.yaml | P03 | `few_shot` | yaml |
| learning/*.yaml | P10 | `learning_record` | yaml |
| spawn_*.ps1 | P12 | `spawn_config` | yaml |

### Skills Directory (129 skills)

| File | LP | Type | machine_format |
|---|---|---|---|
| skills/*/SKILL.md | P04 | `skill` | yaml |

---

## Disambiguation Rules

When a file could map to multiple types:

| Ambiguity | Rule |
|---|---|
| ADW = chain (P03) or workflow (P12)? | If steps are PROMPTS -> P03 `chain`. If steps are AGENTS+TOOLS -> P12 `workflow` |
| KC = knowledge_card (P01) or context_doc (P01)? | If density >= 0.8 -> `knowledge_card`. If <0.8 -> `context_doc` |
| Rules = runtime_rule (P09) or guardrail (P11)? | If safety/never-do -> P11 `guardrail`. If operational -> P09 `runtime_rule` |
| HOP = user_prompt or router_prompt? | If routes/classifies -> P03 `router_prompt`. Otherwise -> P03 `user_prompt` |
| mental_model = P02 or P10? | If identity (fixed) -> P02. If session state (variable) -> P10 |
| output_schema = P05 or P06? | P05 = LLM response format. P06 = data contract validation |

---

## Format Summary

| machine_format | Types | % | When |
|---|---|---|---|
| **yaml** | 64 types | 87% | Prose + structured data (default) |
| **json** | 9 types | 12% | API schemas, tool defs, events, feature flags |

---

## Examples: Before / After Compilation

### Example 1: system_prompt (.md -> .yaml)

**Before** (`P03_prompt/examples/ex_system_prompt.md` frontmatter):
```yaml
id: ex_system_prompt
type: system_prompt
lp: P03
machine_format: yaml
```

**After** (`P03_prompt/compiled/ex_system_prompt.yaml`):
```yaml
id: ex_system_prompt
type: system_prompt
lp: P03
content: |
  You are a gateway agent responsible for routing...
```

### Example 2: few_shot (.md -> .yaml)

**Before** (`P03_prompt/examples/ex_few_shot.md` frontmatter):
```yaml
id: ex_few_shot
type: few_shot
lp: P03
machine_format: yaml
```

**After** (`P03_prompt/compiled/ex_few_shot.yaml`):
```yaml
id: ex_few_shot
type: few_shot
lp: P03
examples:
  - input: "classify this request"
    output: "ROUTE: research"
    rationale: "keyword match: pesquisar"
```

### Example 3: tool schema (.md -> .json)

**Before** (`P04_tools/examples/ex_mcp_server.md` frontmatter):
```yaml
id: ex_mcp_server
type: mcp_server
lp: P04
machine_format: json
```

**After** (`P04_tools/compiled/ex_mcp_server.json`):
```json
{
  "id": "ex_mcp_server",
  "type": "mcp_server",
  "lp": "P04",
  "server": "firecrawl",
  "tools": ["scrape", "extract", "crawl"]
}
```

---

*Generated 2026-03-23 | CEX v3.0*
