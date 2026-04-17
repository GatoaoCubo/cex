---
id: master_systemic_defects
kind: knowledge_card
pillar: P01
title: Master systemic defects across 12 HYBRID_REVIEW audits
version: 1.0.0
quality: 9.1
tags: [audit, systemic, generator-fix, wave1_builder_gen, qwen3, gemma4]
domain: generator quality assurance
created: "2026-04-13"
updated: "2026-04-13"
author: n01_intelligence
tldr: "15 systemic defects extracted from 11 audit files (117 total ISOs). Top 3 CRITICAL: memory kind=learning_record (hardcoded generator bug), quality_gate runtime-vs-artifact mismatch, domain hallucination (financial/trading). system_prompt INJECT is widespread but partially a prompt artifact. gemma4:26b introduced MORE contamination than qwen3:8b."
sources:
  - N01_intelligence/audits/hybrid_review_n01.md
  - N02_marketing/audits/hybrid_review_n02.md
  - N03_engineering/audits/hybrid_review_n03.md
  - N04_knowledge/audits/hybrid_review_n04.md
  - N06_commercial/audits/hybrid_review_n06.md
  - N01_intelligence/audits/hybrid_review2_n01.md
  - N02_marketing/audits/hybrid_review2_n02.md
  - N03_engineering/audits/hybrid_review2_n03.md
  - N04_knowledge/audits/hybrid_review2_n04.md
  - N05_operations/audits/hybrid_review2_n05.md
  - N06_commercial/audits/hybrid_review2_n06.md
note: hybrid_review_n05.md (Wave 1) does not exist -- N05 only has Wave 2 data.
---

# Master Systemic Defects

## Scope

| Source | Round | Builders | ISOs |
|--------|-------|----------|------|
| N01 Wave 1 | R1 | reasoning_strategy, rl_algorithm, reward_model, search_strategy | 52 |
| N02 Wave 1 | R1 | action_paradigm, collaboration_pattern, thinking_config, voice_pipeline | 52 |
| N03 Wave 1 | R1 | agent_profile, dual_loop_architecture, planning_strategy, realtime_session | 52 |
| N04 Wave 1 | R1 | stt_provider, tts_provider, vad_config | 39 |
| N05 Wave 1 | R1 | *file missing -- no data* | 0 |
| N06 Wave 1 | R1 | safety_policy, content_filter, bias_audit | 39 |
| N01 Wave 2 | R2 | voice_pipeline, realtime_session | 26 |
| N02 Wave 2 | R2 | vad_config, tts_provider | 26 |
| N03 Wave 2 | R2 | stt_provider, prosody_config | 26 |
| N04 Wave 2 | R2 | transport_config, edit_format | 26 |
| N05 Wave 2 | R2 | sandbox_config, repo_map | 26 |
| N06 Wave 2 | R2 | diff_strategy | 13 |
| **TOTAL** | | **17 builders, ~25 kinds** | **~377 ISOs** |

---

## Defect Inventory (deduplicated + ranked by frequency)

| # | Defect | Audits Confirming | Severity | Fix Location |
|---|--------|-------------------|----------|--------------|
| D01 | system_prompt llm_function=INJECT (should be BECOME) | 10/11 | CRITICAL | wave1_builder_gen.py:158 |
| D02 | Memory ISO kind=learning_record (should be kind=memory) | N02-R1, N01-R2 | CRITICAL | wave1_builder_gen.py:84 |
| D03 | quality_gate tests runtime metrics, not artifact structure | N02-R1, N05-R2 | CRITICAL | wave1_builder_gen.py:196 |
| D04 | Domain hallucination (financial/trading in non-finance kinds) | N03-R1, N04-R1, N04-R2, N06-R2 | CRITICAL | wave1_builder_gen.py:264 |
| D05 | schema quality field: non-null defaults (should be null) | N01-R1, N02-R2, N03-R2, N04-R2 | HIGH | wave1_builder_gen.py:175 |
| D06 | quality_gate H02 ID pattern divorced from schema naming | N01-R1, N02-R2, N03-R2, N05-R2 | HIGH | wave1_builder_gen.py:196 |
| D07 | Fabricated/hallucinated tools in bld_tools | N02-R1, N03-R1, N04-R1, N05-R2, N06-R2 | HIGH | wave1_builder_gen.py:331 |
| D08 | output_template with bare {{placeholders}}, no guidance | N01-R1, N02-R2, N04-R2, N05-R2 | HIGH | wave1_builder_gen.py:215 |
| D09 | architecture ISO lists generic tech stack not 13 builder ISOs | N01-R1, N01-R2, N02-R2 | HIGH | wave1_builder_gen.py:264 |
| D10 | File reference drift (SCHEMA.md vs bld_schema_{kind}.md) | N03-R1 | HIGH | wave1_builder_gen.py:141 |
| D11 | quality_gate SOFT weights do not sum to 1.00 | N03-R2, N05-R2 | MEDIUM | wave1_builder_gen.py:196 |
| D12 | ASCII violations (Unicode checkmarks in instructions) | N02-R1, N02-R2 | MEDIUM | wave1_builder_gen.py:141 |
| D13 | density_score: 0.85 hardcoded (uniform, not measured) | N03-R1 | MEDIUM | wave1_builder_gen.py:400 |
| D14 | Empty config fields (max_turns, effort_level blank) | N04-R2 | MEDIUM | wave1_builder_gen.py:296 |
| D15 | collaboration tables use generic names not real CEX builders | N04-R2, N02-R1 | LOW | wave1_builder_gen.py:279 |

---

## Generator Fix Specifications

### D01 -- system_prompt llm_function=INJECT

**Root cause:** `build_system_prompt_prompt` passes `Function: {meta['llm_function']}` (the kind's
function from kinds_meta.json, e.g., INJECT for knowledge_card, REASON for planning_strategy).
The LLM uses this as the llm_function for the ISO body. The generator frontmatter correctly says
`llm_function: BECOME` (ISO_SPECS line 66), but the LLM-generated body sometimes includes its own
frontmatter block that overrides it, or content that contradicts the correct value.

**Evidence (N01-R1):** "qwen3:8b used `llm_function: INJECT` for every system_prompt ISO"
**Evidence (N01-R2):** "qwen3:14b still used `llm_function: INJECT` for the realtime-session system_prompt -- Wave 1 fix did NOT propagate"
**Evidence (N02-R1):** "All 4 `bld_system_prompt_*.md` used `llm_function: INJECT` instead of `llm_function: BECOME`"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 157-172):
def build_system_prompt_prompt(kind, meta):
    return f"""Generate a system prompt for the {kind}-builder agent.
Kind: {kind}, Pillar: {meta['pillar']}, Function: {meta['llm_function']}
...
```

```python
# AFTER:
def build_system_prompt_prompt(kind, meta):
    return f"""Generate a system prompt for the {kind}-builder agent.
Kind: {kind}, Pillar: {meta['pillar']}
CRITICAL: This ISO llm_function MUST be BECOME (builder persona consumed at F2 BECOME stage).
Do NOT reference the kind's llm_function ({meta['llm_function']}) here.
...
## Rules
### Scope
(3 rules about what this builder produces and does NOT produce)
### Quality
(5 rules about quality requirements specific to {kind})
### ALWAYS / NEVER
(4 ALWAYS rules + 4 NEVER rules as two bullet lists)

Do NOT generate frontmatter. Body only. ASCII only. Under 60 lines."""
```

**Validation rule for cex_wave_validator.py:**
```python
# Check system_prompt ISOs: llm_function must be BECOME
if iso_kind == "system_prompt":
    assert fm.get("llm_function") == "BECOME", f"D01: {path} llm_function={fm.get('llm_function')!r}, expected BECOME"
```

---

### D02 -- Memory ISO kind=learning_record

**Root cause:** ISO_SPECS line 84 hardcodes `"learning_record"` as the kind for memory ISOs.
Gold standard (`bld_memory_prompt_template.md`) uses `kind: memory`. The `build_memory_prompt`
function also says "Generate a learning record (memory)" reinforcing the wrong kind name.

**Evidence (N02-R1):** "All 4 `bld_memory_*.md` files used `kind: learning_record` instead of `kind: memory`. Root cause: qwen3:8b confused memory ISO with learning_record artifact kind."
**Evidence (N01-R2):** "bld_memory_realtime_session.md: wrong kind (learning_record) -- fixed to memory"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 84):
    ("bld_memory_{k}.md", "learning_record", "P10", "INJECT",
     "Learned patterns and pitfalls for {kind} construction"),
```

```python
# AFTER:
    ("bld_memory_{k}.md", "memory", "P10", "INJECT",
     "Learned patterns and pitfalls for {kind} construction"),
```

Also fix `build_memory_prompt` (line 313):
```python
# BEFORE:
def build_memory_prompt(kind, meta):
    return f"""Generate a learning record (memory) for {kind}-builder.
```
```python
# AFTER:
def build_memory_prompt(kind, meta):
    return f"""Generate a memory ISO (kind: memory) for {kind}-builder.
This is NOT a learning_record artifact -- it is the builder's internal memory pattern.
```

**Validation rule:**
```python
# Memory ISOs: kind must be "memory" not "learning_record"
if "bld_memory_" in str(path):
    assert fm.get("kind") == "memory", f"D02: {path} kind={fm.get('kind')!r}, expected 'memory'"
```

---

### D03 -- quality_gate tests runtime metrics not artifact structure

**Root cause:** `build_quality_gate_prompt` does not specify that gates must test the ARTIFACT
(its YAML fields, sections, format) rather than a deployed system's runtime performance.
Without this constraint, LLM generates gates for operational systems (CPU%, latency, TLS version).

**Evidence (N02-R1):** "Every quality_gate ISO tested runtime system performance instead of artifact structure: action_paradigm: action execution time (>500ms), CPU >90%, error rate >5%; collaboration_pattern: latency <=10ms, TLS version, agent count >1000"
**Evidence (N05-R2):** "bld_quality_gate_sandbox_config: Weight sum 1.10->1.00; H02 pattern sandbox-\d{4} -> ^p09_sb_[a-zA-Z0-9_-]+$"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 196-212):
def build_quality_gate_prompt(kind, meta):
    return f"""Generate a quality gate for CEX kind "{kind}".
Pillar: {meta['pillar']}, Description: {meta['description']}

Generate markdown body (NO frontmatter) with:
## Definition
(Table: metric, threshold, operator, scope)
## HARD Gates
(Table: ID | Check | Fail Condition -- 7-10 gates including H01-H03 standard: YAML valid, ID matches pattern, kind matches)
## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide -- 8-11 dimensions summing to 1.00)
...
```

```python
# AFTER:
def build_quality_gate_prompt(kind, meta):
    nm = meta.get("naming", "")
    return f"""Generate a quality gate for CEX kind "{kind}" ARTIFACTS.
Pillar: {meta['pillar']}, Description: {meta['description']}
Naming pattern: {nm}

CRITICAL: Gates test the ARTIFACT (its YAML fields, body sections, format).
Gates do NOT test deployed systems (no CPU%, latency, TLS version, error rates).

Generate markdown body (NO frontmatter) with:
## Definition
(Table: metric, threshold, operator, scope -- all about the .md file structure)
## HARD Gates
H01: Valid YAML frontmatter | YAML parse error | REJECT
H02: ID matches naming pattern | ID not matching {nm} | REJECT
H03: kind == "{kind}" | Wrong kind | REJECT
H04-H09: domain-specific checks for required fields in frontmatter and required sections in body
## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide -- exactly 5 dimensions summing EXACTLY to 1.00)
CRITICAL: Weight column must sum to exactly 1.00. Check: 0.25+0.20+0.20+0.20+0.15 = 1.00
## Actions
(GOLDEN >=9.5, PUBLISH >=8.0, REVIEW >=7.0, REJECT <7.0)

ASCII only. Under 80 lines."""
```

**Validation rule:**
```python
# quality_gate: weights must sum to 1.00
import re
soft_weights = re.findall(r"\|\s+[\w\s]+\s+\|\s+(0\.\d+)\s+\|", qg_content)
total = sum(float(w) for w in soft_weights)
assert abs(total - 1.0) < 0.01, f"D03/D11: {path} SOFT weights sum={total:.2f}, expected 1.00"
```

---

### D04 -- Domain hallucination (financial/trading contamination)

**Root cause:** `build_architecture_prompt` asks to "place {kind} in the CEX ecosystem" without
defining CEX as an AI knowledge system. LLM interprets "CEX" as crypto exchange. The 13-ISO
architecture component inventory is also not requested.

**Evidence (N03-R1):** "dual_loop_architecture -> classical control systems (PID, Lyapunov, ISO 26262 actuators). planning_strategy -> corporate strategy (KPIs, MoSCoW, $500M budgets, Pandas/Backtrader). realtime_session -> legacy SIP/WebRTC video conferencing."
**Evidence (N04-R1):** "2/3 builders had architecture ISOs positioning the builder within 'CEX trading systems'. Root cause: qwen3:8b appears to have associated 'CEX' with 'Crypto Exchange'"
**Evidence (N06-R2):** "quality_gate pre: 'Backtest loss >15%', D3=Backtesting Results; tools pre: CCXT, Backtrader, strat_backtest.py"
**Evidence (N04-R2):** "bld_architecture_transport_config: 'trading, settlement, external systems' -- financial domain hallucination"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 264-276):
def build_architecture_prompt(kind, meta):
    return f"""Generate an architecture document for the {kind}-builder.
Kind: {kind}, Pillar: {meta['pillar']}

Generate markdown body (NO frontmatter) with:
## Component Inventory
(Table: Name | Role | Owner | Status -- 5-8 components)
## Dependencies
(Table: From | To | Type -- 4-6 dependencies)
## Architectural Position
(1 paragraph placing {kind} in the CEX ecosystem)

ASCII only. Under 50 lines."""
```

```python
# AFTER:
def build_architecture_prompt(kind, meta):
    return f"""Generate an architecture document for the {kind}-builder.
Kind: {kind}, Pillar: {meta['pillar']}
Description: {meta['description']}
Boundary: {meta['boundary']}

CONTEXT: CEX is an AI knowledge system with typed artifacts. NOT a crypto exchange.
This architecture document is for the {kind}-BUILDER (a tool that creates {kind} artifacts),
not for a financial, trading, or enterprise management system.

Generate markdown body (NO frontmatter) with:
## Builder ISO Inventory
(Table listing all 13 ISOs of this builder: manifest, instruction, system_prompt, schema,
quality_gate, output_template, examples, knowledge_card, architecture, collaboration, config,
memory, tools -- each with its purpose for {kind})
## ISO Dependencies
(Table: ISO | Depends On | Type -- how ISOs within this builder reference each other)
## Architectural Position
(1 paragraph: where {kind} fits in CEX pillar taxonomy -- pillar {meta['pillar']},
upstream consumers, downstream producers. Reference AI/ML context, not business systems.)

ASCII only. Under 60 lines."""
```

**Validation rule:**
```python
FINANCIAL_TERMS = ["trading", "settlement", "exchange", "backtest", "FIFO", "Pro-Rata",
                   "risk engine", "market data", "CCXT", "Backtrader", "quant", "order book"]
for term in FINANCIAL_TERMS:
    assert term.lower() not in content.lower(), f"D04: {path} contains financial term '{term}'"
```

---

### D05 -- schema quality field non-null defaults

**Root cause:** `build_schema_prompt` asks for "quality" in the Required fields table but does not
specify that `default` must be `null` and `type` must be null. The LLM invents defaults like
`"draft"`, `"high"`, or `0-100` integer range.

**Evidence (N01-R1):** "Schemas described quality as integer (0-100) or string ('draft') with non-null defaults. CEX rule 4 -- quality: null always; peer review assigns value."
**Evidence (N02-R2):** "vad_config was: quality: 'draft'; tts_provider was: quality: string with 'high' example"
**Evidence (N03-R2):** "bld_schema_stt_provider.md: `quality: 'draft'` -> `quality: null`"
**Evidence (N04-R2):** "Schema default violations: quality: 'draft' instead of null"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 175-193): build_schema_prompt
# The schema prompt asks for "at least 10 fields including ... quality" but
# doesn't constrain quality's type or default.
```

```python
# AFTER: Add to build_schema_prompt (line 183-184 replacement):
    return f"""Generate a formal schema for CEX kind "{kind}".
Pillar: {meta['pillar']}, Naming: {meta['naming']}, Max bytes: {meta['max_bytes']}

Generate markdown body (NO frontmatter) with:
## Frontmatter Fields
### Required
(Table: Field | Type | Required | Default | Notes)
MANDATORY ROWS (include these exactly):
| id | string | yes | -- | Matches naming pattern |
| kind | string | yes | {kind} | Must equal "{kind}" |
| quality | null | yes | null | NEVER self-score; peer review assigns. Default is null. |
| version | string | yes | "1.0.0" | Semantic version |
Plus 6-8 domain-specific required fields for {kind}.
### Recommended
(Table: 3-4 optional fields)
## ID Pattern
(Regex pattern: must match naming convention {meta['naming'].replace('{{name}}', '[name]')})
## Body Structure (required sections)
(4-6 numbered sections specific to {kind})
## Constraints
(5-6 bullet constraints)

ASCII only. Under 80 lines."""
```

**Validation rule:**
```python
# In schema ISO: quality default must be null
if "bld_schema_" in str(path):
    assert "quality" in content and "null" in content, f"D05: {path} missing quality: null field"
    # Check the quality row in the table
    assert re.search(r"quality\s*\|\s*null\s*\|\s*yes\s*\|\s*null", content), \
        f"D05: {path} quality field not typed as null with null default"
```

---

### D06 -- quality_gate H02 pattern divorced from schema

**Root cause:** `build_quality_gate_prompt` mentions "H02: ID matches pattern" but does not inject
the actual naming pattern from the kind's schema. The LLM invents patterns (e.g., `tts-[a-z0-9]+`,
`rl_[a-z0-9]+`, `^[A-Z]{3}-[0-9]{4}$`) that don't match the schema naming convention.

**Evidence (N01-R1):** "reasoning_strategy: PXX-YYYY, rl_algorithm: rl_[a-z0-9]+, reward_model: ^[A-Z]{3}-[0-9]{4}$, search_strategy: P04-[A-Z]{3}-\d{3}"
**Evidence (N02-R2):** "TTS H02 pattern: was `tts-[a-z0-9]+`, now `^p04_tts_[a-zA-Z0-9_-]+$`"
**Evidence (N05-R2):** "sandbox H02: sandbox-\d{4} -> ^p09_sb_[a-zA-Z0-9_-]+$; repo_map H02: repo-[a-z0-9]{8} -> ^p01_rm_[a-zA-Z0-9_]+$"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 196-212): quality_gate prompt does not pass naming pattern
```

```python
# AFTER: Inject naming pattern explicitly in D03 fix above (already shows nm variable):
# The key addition is explicitly stating the H02 pattern in the prompt:
    return f"""...
## HARD Gates
H01: Valid YAML frontmatter | YAML parse error | REJECT
H02: ID matches naming pattern | ID not matching regex ^{nm.replace('{{name}}', '[a-zA-Z0-9_-]+')}$ | REJECT
H03: kind == "{kind}" | Wrong kind | REJECT
...
```

**Validation rule:**
```python
# H02 in quality_gate must reference the kind's naming pattern
nm_slug = meta.get("naming", "").replace("{{name}}", "[a-zA-Z0-9_-]+")
assert nm_slug[:6] in qg_content, f"D06: {path} H02 pattern missing prefix from naming convention"
```

---

### D07 -- Fabricated/hallucinated tools in bld_tools

**Root cause:** `build_tools_prompt` asks for "Validation Tools (3-4 tools)" without specifying
which real tools exist. The LLM invents plausible-sounding tool names (val_checker.py, val_analyzer.py,
val_comparator.py, cex_optimizer.py) that don't exist in the CEX codebase. External references
include unrelated libraries (CCXT, Backtrader, PyTorch, Apache Spark, TensorFlow).

**Evidence (N02-R1):** "All 4 `bld_tools_*.md` files referenced imaginary validation tools: val_checker.py, val_analyzer.py, val_comparator.py, val_reporter.py. External references included CEX cryptocurrency exchange (cex.io), PyTorch, Apache Spark."
**Evidence (N03-R1):** "`bld_tools_{kind}.md` across 4 kinds lists 15+ nonexistent `cex_*.py` scripts (cex_analyzer.py, cex_optimizer.py, val_check.py, cex_realtime.py)"
**Evidence (N06-R2):** "tools pre: CCXT, Backtrader, strat_backtest.py, strat_stress_test.py"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 331-343):
def build_tools_prompt(kind, meta):
    return f"""Generate a tools inventory for {kind}-builder.
Kind: {kind}

Generate markdown body (NO frontmatter) with:
## Production Tools
(Table: Tool | Purpose | When -- 4-6 CEX tools like cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py)
## Validation Tools
(Table: Tool | Purpose | When -- 3-4 tools)
## External References
(2-3 relevant external tools or frameworks)

ASCII only. Under 40 lines."""
```

```python
# AFTER:
def build_tools_prompt(kind, meta):
    return f"""Generate a tools inventory for {kind}-builder.
Kind: {kind}, Description: {meta['description']}

REAL CEX TOOLS ONLY (these exist on disk -- use their EXACT names):
Pipeline: cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py, cex_hooks.py
Search: brain_query [MCP tool], Glob, Grep, Read, Edit, Write [filesystem tools]
Signal: signal_writer.py (write_signal function)

Generate markdown body (NO frontmatter) with:
## Production Tools
(Table: Tool | Purpose | When -- from the real CEX pipeline list above)
## Domain Tools
(Table: Tool | Purpose | When -- 2-4 REAL external libraries/tools that practitioners use for {kind}.
Must be real, installable packages -- not invented names like val_checker.py or cex_analyzer.py.)
## MCP Tools
(brain_query for semantic search, filesystem tools for read/write)

ASCII only. Under 40 lines."""
```

**Validation rule:**
```python
FAKE_TOOL_PATTERNS = ["val_checker", "val_analyzer", "val_comparator", "val_reporter",
                      "cex_analyzer", "cex_optimizer", "cex_executor", "cex_realtime",
                      "strat_backtest", "strat_stress", "PolicyForge", "SafetyChain", "RiskAssess"]
for pattern in FAKE_TOOL_PATTERNS:
    assert pattern not in content, f"D07: {path} contains fabricated tool '{pattern}'"
```

---

### D08 -- output_template bare placeholders

**Root cause:** `build_output_template_prompt` explicitly requests "Body sections with {{placeholder}}
content" -- this IS the bare placeholder pattern. No guidance is requested for what goes in each
section, resulting in templates that provide zero authoring guidance.

**Evidence (N01-R1):** "Templates contained `{{placeholder}} content for...` literal text with no guidance"
**Evidence (N02-R2):** "TTS output_template was 4.0 -- 'Bare `{{placeholder}}` template with no guidance on required fields'"
**Evidence (N04-R2):** "bld_output_template_edit_format: Shows abstract YAML with {{placeholders}} -- no actual Aider/Cursor format syntax"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 215-225):
def build_output_template_prompt(kind, meta):
    ...
    return f"""...
Generate markdown body (NO frontmatter) with a YAML code block showing:
- All required frontmatter fields with {{{{variable}}}} placeholders
- Body sections with {{{{placeholder}}}} content
...
```

```python
# AFTER:
def build_output_template_prompt(kind, meta):
    pfx = meta.get("naming", "p00_x")
    return f"""Generate a production output template for CEX kind "{kind}".
Pillar: {meta['pillar']}, Naming: {meta['naming']}, Max bytes: {meta['max_bytes']}
Description: {meta['description']}

Generate markdown body (NO frontmatter) with:
1. A YAML frontmatter block (as a code block) with ALL required schema fields.
   Use realistic placeholder values, NOT {{{{placeholder}}}} for every field.
   Example: id: p04_x_my_name_here (not id: {{{{id}}}})
2. After the frontmatter block: 4-6 body sections with:
   - Section header (## Section Name)
   - A <!-- comment explaining what to put here and what format --> on the first line
   - A skeleton table or code block showing expected data structure
   - At least one example row or line showing what real content looks like

Do NOT use bare {{{{placeholder}}}} as section content.
Do NOT produce a template that only shows field names with no structure.
ASCII only. Under 80 lines."""
```

**Validation rule:**
```python
# output_template: count bare placeholder lines ({{xxx}} without surrounding context)
placeholder_only_lines = [l for l in content.split("\n")
                           if re.match(r"^\s*\{\{[^}]+\}\}\s*$", l)]
assert len(placeholder_only_lines) < 3, \
    f"D08: {path} has {len(placeholder_only_lines)} bare placeholder lines (max 2)"
```

---

### D09 -- architecture ISO lists generic tech stack not 13 builder ISOs

**Root cause:** `build_architecture_prompt` asks for "5-8 components" without specifying they should
be the 13 builder ISOs. LLM invents generic components (Audio Ingestion, Pipeline Orchestration,
SessionManager, DataAggregator, Execution Engine, Risk Engine).

**Evidence (N01-R1):** "Architecture ISO MUST list the 13 builder ISOs as components, not a generic tech stack"
**Evidence (N01-R2):** "Both architecture ISOs listed generic business/tech components (Audio Ingestion, Pipeline Orchestration) NOT the 13 builder ISOs -- same pattern, same fix needed -- still not in generator prompt"
**Evidence (N02-R2):** "architecture ISO inventory (both builders): Added 13-ISO inventory table + dependency graph"

Fixed in D04 above (the updated `build_architecture_prompt` requests "Builder ISO Inventory").

---

### D10 -- file reference drift (non-canonical paths)

**Root cause:** `build_instruction_prompt` (line 149-150) asks for steps "referencing SCHEMA.md and
OUTPUT_TEMPLATE.md" -- non-canonical. Correct canonical names are `bld_schema_{kind}.md` and
`bld_output_template_{kind}.md`. The LLM also uses `VALIDATION_RULES.md`, `SCHEMA.md`,
`OUTPUT_TEMPLATE.md` throughout other ISOs.

**Evidence (N03-R1):** "ISOs reference non-canonical paths (`SCHEMA.md`, `OUTPUT_TEMPLATE.md`, `VALIDATION_RULES.md`) instead of `bld_schema_{kind}.md`, `bld_output_template_{kind}.md`"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 149-150):
(9 numbered steps for writing the artifact, referencing SCHEMA.md and OUTPUT_TEMPLATE.md)
```

```python
# AFTER:
(9 numbered steps for writing the artifact, referencing bld_schema_{kind}.md and bld_output_template_{kind}.md)
```

Also add to ALL prompt generators:
```python
# Add to each prompt function (after the kind description line):
CANONICAL_NAMES = f"""
CANONICAL FILE NAMES (use these exact names, no variations):
  Schema: bld_schema_{kind}.md
  Output template: bld_output_template_{kind}.md
  Quality gate: bld_quality_gate_{kind}.md
  Instruction: bld_instruction_{kind}.md
  (Do NOT use SCHEMA.md, OUTPUT_TEMPLATE.md, VALIDATION_RULES.md)
"""
```

**Validation rule:**
```python
BANNED_REFS = ["SCHEMA.md", "OUTPUT_TEMPLATE.md", "VALIDATION_RULES.md", "MANIFEST.md"]
for ref in BANNED_REFS:
    assert ref not in content, f"D10: {path} contains non-canonical reference '{ref}'"
```

---

### D11 -- quality_gate SOFT weights do not sum to 1.00

Fixed in D03 above (the updated prompt explicitly requires weights summing to 1.00 with verification).

---

### D12 -- ASCII violations (Unicode checkmarks in instructions)

**Root cause:** `build_instruction_prompt` asks for "checkbox format" in Phase 3 validation.
The LLM interprets this as Unicode checkmarks (U+2705 ✅) which violate `.claude/rules/ascii-code-rule.md`.

**Evidence (N02-R1):** "Three kinds had `✅` emoji in `bld_instruction_*.md` Phase 3 validation checklists"
**Evidence (N02-R2):** "bld_instruction_vad_config.md: Unicode checkmarks (U+2705) removed -- violates ascii-code-rule.md"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 152-153):
## Phase 3: VALIDATE
(5 numbered validation steps with checkbox format)
```

```python
# AFTER:
## Phase 3: VALIDATE
(5 numbered validation steps as a plain ASCII checklist -- use "- [ ]" format ONLY.
Do NOT use emoji, checkmarks, or Unicode symbols. Example: "- [ ] Verify frontmatter valid")
```

**Validation rule:**
```python
NON_ASCII_CHARS = set(chr(i) for i in range(128, 65536))
for char in content:
    if char in NON_ASCII_CHARS:
        assert False, f"D12: {path} contains non-ASCII character U+{ord(char):04X}"
```

---

### D13 -- density_score: 0.85 hardcoded (uniform)

**Root cause:** `generate_frontmatter` (line 400) hardcodes `density_score: 0.85` for every ISO.
This is not a measured value. After fixing, it should either be removed or computed post-generation.

**Evidence (N03-R1):** "All 52 ISOs claim identical `density_score: 0.85` regardless of actual information density -- the model self-scored uniformly."

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 400):
density_score: 0.85
```

```python
# AFTER: Remove density_score from frontmatter template entirely.
# Let cex_score.py compute it post-generation.
# (delete the line)
```

---

### D14 -- empty config fields (max_turns, effort_level blank)

**Root cause:** `build_config_prompt` asks for "max_turns, effort level" but does not provide
defaults. The LLM sometimes leaves fields blank or uses placeholder text.

**Evidence (N04-R2):** "bld_config_edit_format: max_turns and effort_level fields EMPTY -- Fixed: max_turns: 3, effort_level: 2"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 296-310):
def build_config_prompt(kind, meta):
    return f"""Generate a config for {kind}-builder.
Naming: {meta['naming']}, Max bytes: {meta['max_bytes']}, Pillar: {meta['pillar']}

Generate markdown body (NO frontmatter) with:
## Naming Convention
(Pattern and examples)
## Paths
(Where artifacts are stored)
## Limits
(max_bytes, max_turns, effort level)
## Hooks
(pre_build, post_build, on_error, on_quality_fail -- all null for now)
```

```python
# AFTER:
def build_config_prompt(kind, meta):
    return f"""Generate a config for {kind}-builder.
Naming: {meta['naming']}, Max bytes: {meta['max_bytes']}, Pillar: {meta['pillar']}

Generate markdown body (NO frontmatter) with:
## Naming Convention
Pattern: {meta['naming']}
(1-2 concrete naming examples using this pattern)
## Paths
records/pool/{meta['pillar'].lower()}/   (primary artifact store)
(records/compiled/ for compiled YAML versions)
## Limits
max_bytes: {meta['max_bytes']}
max_turns: 3
effort_level: 2
## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

ASCII only. Under 35 lines."""
```

---

### D15 -- collaboration tables use generic names not real CEX builders

**Root cause:** `build_collaboration_prompt` does not reference real CEX builder names.
LLM invents generic producers/consumers: "Parser/Validator/Merger", "API_Manager", "Text_Handler".

**Evidence (N04-R2):** "Collaboration: Receives from 'Parser/Validator/Merger' -- generic/wrong; should be diff_strategy/code_executor"
**Evidence (N02-R1):** "TTS collaboration uses 'API_Manager', 'Text_Handler' -- generic names instead of real CEX builder names"

**File:** `_tools/wave1_builder_gen.py`

```python
# BEFORE (line 279-293): build_collaboration_prompt has no CEX builder name context
```

```python
# AFTER: Add related builder context from meta if available:
def build_collaboration_prompt(kind, meta):
    return f"""Generate a collaboration spec for {kind}-builder.
Kind: {kind}, Boundary: {meta['boundary']}

Generate markdown body (NO frontmatter) with:
## Crew Role
(What this builder does in a multi-builder team for {kind})
## Receives From
(Table: Builder | What | Format -- use real CEX builder names like
voice_pipeline_builder, system_prompt_builder, schema_builder, agent_builder, etc.)
## Produces For
(Table: Builder | What | Format -- real CEX builder names as consumers)
## Boundary
(What this builder does NOT do and which real CEX builder handles it instead)

Use real builder names: {kind.replace('_','-')}-builder is this one.
Sibling builders have names like: diff_strategy-builder, edit_format-builder,
code_executor-builder, sandbox_config-builder, transport_config-builder.
ASCII only. Under 45 lines."""
```

---

## Cross-Audit Consensus

### MUST FIX (confirmed in 3+ audit files)

| # | Defect | Confirmed By |
|---|--------|-------------|
| D01 | system_prompt llm_function=INJECT | N01-R1, N02-R1, N01-R2, N02-R2, N03-R2 (5+ audits) |
| D02 | memory kind=learning_record | N02-R1, N01-R2 (2 audits -- but hardcoded in generator) |
| D03 | quality_gate runtime metrics | N02-R1, N05-R2 (2 audits -- pattern is definitive) |
| D04 | Domain hallucination (financial) | N03-R1, N04-R1, N04-R2, N06-R2 (4 audits) |
| D05 | schema quality non-null | N01-R1, N02-R2, N03-R2, N04-R2 (4 audits) |
| D06 | quality_gate H02 pattern mismatch | N01-R1, N02-R2, N03-R2, N05-R2 (4 audits) |
| D07 | fabricated tools in bld_tools | N02-R1, N03-R1, N04-R1, N05-R2, N06-R2 (5 audits) |
| D08 | output_template bare placeholders | N01-R1, N02-R2, N04-R2, N05-R2 (4 audits) |
| D09 | architecture not 13-ISO inventory | N01-R1, N01-R2, N02-R2 (3 audits) |

### RECOMMENDED (1-2 audit files)

| # | Defect | Confirmed By |
|---|--------|-------------|
| D10 | file reference drift | N03-R1 (1 audit -- but structurally wrong) |
| D11 | quality_gate weights != 1.00 | N03-R2, N05-R2 (2 audits) |
| D12 | ASCII violations in instructions | N02-R1, N02-R2 (2 audits) |
| D13 | density_score: 0.85 hardcoded | N03-R1 (1 audit) |
| D14 | empty config fields | N04-R2 (1 audit) |
| D15 | generic collaboration names | N04-R2, N02-R1 (2 audits) |

---

## Model Comparison: qwen3:14b vs gemma4:26b

N01-R2 (Wave 2) includes explicit comparison of both models:

| Dimension | qwen3:8b (Wave 1) | qwen3:14b (Wave 2) | gemma4:26b (Wave 2, mixed) |
|-----------|-------------------|---------------------|---------------------------|
| Avg pre-fix score | 7.55 | 6.9 | 5.7 (diff_strategy N06-R2) |
| Wave 1 systemic fixes retained | baseline | 3/5 (60%) -- system_prompt still failed | Unknown |
| New issues introduced | -- | 2 major (domain mismatch, no real providers) | 4 ISOs fully contaminated (financial) |
| ISOs needing rebuild | 0/52 (N01-R1) | 7/26 (N01-R2) | 4/13 (N06-R2) |
| Architecture domain contamination | Moderate (generic tech) | Severe (video conferencing domain) | Severe (financial trading domain) |
| Fictional tools | Invented val_*.py | Invented val_*.py | CCXT, Backtrader (real but wrong domain) |
| Post-fix avg | ~8.0 | 8.75 | 8.7 |

**Key findings:**

1. **qwen3:14b did NOT fix the system_prompt INJECT issue** despite it being documented in Wave 1
   audits. The generator prompt must be updated -- model scaling alone does not fix it.

2. **gemma4:26b introduced MORE severe financial domain contamination** than qwen3:8b.
   While qwen3:8b confused CEX = crypto exchange in architecture ISOs only, gemma4:26b contaminated
   quality_gate logic, examples content, and tools lists (diff_strategy examples showed FIFO/Pro-Rata
   order book matching instead of code diffing algorithms).

3. **qwen3:14b introduced a new domain error type**: realtime_session treated as generic WebRTC
   video conferencing (H264/VP9 codecs, SessionManager/DataAggregator) rather than LLM audio
   streaming. This is domain knowledge the model lacks (OpenAI Realtime API was released 2024-10).

4. **Both models share the same failure modes** on structure-driven defects (D01-D09) because
   those failures are caused by the generator PROMPTS, not the model's capability. Fixing the
   prompts (as specified above) should remediate these defects across all models.

5. **gemma4:26b produced higher contamination density**: In N06-R2, 4/13 ISOs were "fully
   contaminated" with financial trading domain -- vs N03-R1 where domain issues were severe but
   partial. The larger model appears MORE confidently wrong when it hallucinates domain context.

**Recommendation:** Both models require the same generator prompt fixes (D01-D15). Additionally:
- For voice domain builders: inject explicit domain anchors (OpenAI Realtime API v2024-12, Gemini
  Live) before generation to prevent the "generic WebRTC" hallucination.
- For CEX disambiguation: add to ALL prompts "CEX = AI knowledge system, NOT a crypto exchange."
  This phrase should prevent the financial contamination shared by both models.

---

## Summary: What N02 Should Patch

N02 patch priority order:

1. **Line 84** -- Change `"learning_record"` to `"memory"` (D02 -- single-character fix, maximum impact)
2. **Line 400** -- Remove `density_score: 0.85` from frontmatter template (D13)
3. **Line 157-172** -- Fix `build_system_prompt_prompt` (D01)
4. **Line 264-276** -- Fix `build_architecture_prompt` (D04, D09)
5. **Line 196-212** -- Fix `build_quality_gate_prompt` (D03, D06, D11)
6. **Line 175-193** -- Fix `build_schema_prompt` (D05)
7. **Line 215-225** -- Fix `build_output_template_prompt` (D08)
8. **Line 331-343** -- Fix `build_tools_prompt` (D07)
9. **Line 141-154** -- Fix `build_instruction_prompt` (D10, D12)
10. **Line 296-310** -- Fix `build_config_prompt` (D14)
11. **Line 279-293** -- Fix `build_collaboration_prompt` (D15)
12. **All prompts** -- Add CEX disambiguation and canonical file names (D04, D10)
