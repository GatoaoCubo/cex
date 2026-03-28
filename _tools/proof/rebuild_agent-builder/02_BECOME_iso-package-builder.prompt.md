# CEX Crew Runner -- Builder Execution
**Builder**: `iso-package-builder`
**Function**: BECOME
**Intent**: reconstroi agent-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:20.283811

## Intent Context
- **Verb**: reconstroi
- **Object**: agent-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_iso_package.md
---
id: iso-package-builder
kind: type_builder
pillar: P02
parent: null
domain: iso_package
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, iso-package, P02, specialist, packaging, portable, agent-bundle]
---

# iso-package-builder
## Identity
Especialista em construir `iso_package` artifacts — pacotes portaveis self-contained de agente AI em formato ISO.
Domina tier system (minimal/standard/complete/whitelabel), LP mapping (file-to-pillar),
portability enforcement (no hardcoded paths), file inventory validation, and system_instruction
token budgeting. Produz packages densos com manifest.yaml completo e todos os files corretos por tier.
## Capabilities
- Produzir iso_package com manifest.yaml completo (14 campos required + 5 recommended)
- Validar tier compliance (3/7/10/12 files por tier)
- Enforcar portabilidade (no hardcoded paths, LLM-agnostic instructions)
- Gerar file inventory com LP mapping correto por file
- Verificar system_instruction.md <= 4096 tokens
- Detectar boundary violations (iso_package vs agent, boot_config, mental_model)
## Routing
keywords: [iso-package, packaging, portable, bundle, self-contained, agent-package, distribute, deploy-agent, whitelabel]
triggers: "package this agent for distribution", "create ISO bundle for agent", "build portable agent package"
## Crew Role
In a crew, I handle AGENT PACKAGING AND DISTRIBUTION.
I answer: "how do I bundle this agent into a portable, self-contained, tier-validated package?"
I do NOT handle: agent definition (agent-builder), boot configuration (boot-config-builder), system prompt writing (system-prompt-builder [PLANNED]).

### bld_instruction_iso_package.md
---
kind: instruction
id: bld_instruction_iso_package
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for iso_package
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an iso_package
## Phase 1: RESEARCH
1. Identify the target agent by name and domain
2. Determine the tier based on delivery requirements:
   - minimal (3 files): manifest.yaml, system_instruction.md, instructions.md
   - standard (7 files): minimal + architecture.md, output_template.md, examples.md, error_handling.md
   - complete (10 files): standard + quick_start.md, input_schema.yaml, upload_kit.md
   - whitelabel (12 files): complete + upload_kit_whitelabel.md, branding_config.yaml
3. Verify all required files for the selected tier exist or can be produced
4. Check portability: no hardcoded paths (/home/, /Users/, C:\, records/), no provider-specific references, no internal project names in the instructions
5. Calculate the system_instruction token count — must be at or below 4096 tokens
6. Map each file to its pillar using the LP mapping (manifest=P02, system_instruction=P03, instructions=P03, architecture=P08, output_template=P05, examples=P07, error_handling=P11, quick_start=P01, input_schema=P06, upload_kit=P04)
7. Check existing iso_packages via brain_query [IF MCP] for the same agent — avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and tier requirements
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: 14 required fields + 5 recommended fields (null is acceptable for recommended)
4. Set quality: null — never self-score
5. Write manifest.yaml with all required fields: id, kind, tier, version, files inventory with LP mapping
6. Write the File Inventory section: one row per file with name / pillar / purpose / size
7. Write system_instruction.md as a composite document — must be at or below 4096 tokens
8. Write the Portability Checklist: confirm no absolute paths, no provider-specific references, no internal jargon in any file
9. Write the Tier Compliance section: declared tier, file count expected vs actual, list any gaps
10. Set files_count to match the actual number of files in the directory
11. Verify each individual file is within 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — apply each gate manually
2. HARD gates (all must pass):
   - YAML in manifest.yaml parses without errors
   - id matches pattern `p02_iso_[a-z][a-z0-9_]+`
   - kind == iso_package
   - tier is one of: minimal, standard, complete, whitelabel
   - files_count matches actual file count in the directory
   - file count meets the tier minimum (minimal=3, standard=7, complete=10, whitelabel=12)
   - system_instruction.md is at or below 4096 tokens
   - manifest.yaml body is within 4096 bytes
   - quality == null
3. SOFT gates (score each against QUALITY_GATES.md):
   - LP mapping covers all included files
   - portability check passed — no hardcoded paths in any file
   - examples.md has at least 2 examples (if tier >= standard)
   - density >= 0.80 across all files
4. Cross-check scope boundaries:
   - portable self-contained bundle, not a bare agent definition (agent-builder)?
   - not a boot or runtime configuration (boot-config-builder)?
   - not a standalone system prompt (system-prompt-builder)?
   - no hardcoded paths in any file across the entire package?
5. If score < 8.0: revise files before outputting

### bld_knowledge_card_iso_package.md
---
kind: knowledge_card
id: bld_knowledge_card_iso_package
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for iso_package production — portable agent bundle packaging
sources: Docker OCI spec, ISO 42001 AI management, HuggingFace Model Hub, agent packaging patterns
---

# Domain Knowledge: iso_package
## Executive Summary
ISO packages are self-contained, portable, LLM-agnostic bundles that encapsulate an AI agent's complete operational context. Inspired by Docker images and ISO 42001 AI management systems, each package provides everything needed to instantiate an agent on any compatible runtime. They use a tiered file system with pillar-mapped contents and quality validation. ISO packages differ from agent definitions (source), boot configs (provider-specific init), and spawn configs (orchestration params).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (identity/model) |
| Frontmatter fields | 14 required + 5 recommended |
| Quality gates | 9 HARD + 10 SOFT |
| system_instruction max | 4096 tokens |
| Density minimum | >= 0.80 per file |
| Portability | Zero hardcoded paths |
| Entry point | manifest.yaml |
## Patterns
- **Tier system**: graduated completeness
| Tier | Files | Use case |
|------|-------|----------|
| minimal | 3 | Prototype, early development |
| standard | 7 | Production-ready deployment |
| complete | 10 | Full-featured with all extensions |
| whitelabel | 12 | Distributable, rebrandable |
- **Manifest-first**: manifest.yaml is the single entry point — everything discoverable from it
| Source | Concept | Application |
|--------|---------|-------------|
| Docker OCI | Layered manifest with image config | Tiered manifest.yaml |
| ISO 42001 | AI management documentation | Quality gates, audit trail |
| HuggingFace | Model card + weights + tokenizer | manifest + system_instruction + instructions |
| OpenAI GPTs | System prompt + knowledge + actions | system_instruction + instructions + input_schema |
- **LP mapping**: each file maps to a pillar — enables fractal navigation within the package
- **Token budgeting**: system_instruction.md capped at 4096 tokens to fit context windows across providers
- **Portability enforcement**: zero hardcoded paths guarantees cross-platform, cross-machine deployment
- **File inventory**: manifest lists all files with status (present/absent) for completeness audit
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Hardcoded paths in files | Package breaks on different machine/OS |
| system_instruction > 4096 tokens | Overflows context window; silently truncated |
| Missing manifest.yaml | No entry point; package is undiscoverable |
| Filler in files (density < 0.80) | Wastes token budget; low information value |
| Tier mismatch (claiming standard, missing files) | Audit failure; false completeness claim |
| LLM-specific instructions | Not portable; tied to one provider |
## Application
1. Select tier: minimal (3), standard (7), complete (10), or whitelabel (12)
2. Create manifest.yaml: list all files with LP mapping and status
3. Write system_instruction.md: <= 4096 tokens, LLM-agnostic
4. Ensure portability: grep for hardcoded paths; replace with relative
5. Verify density: every file >= 0.80 density — no filler
6. Validate: file count matches tier, manifest is complete, all files present
## References
- Docker OCI Image Spec: layered manifest and portability patterns
- ISO 42001:2023: AI management systems documentation standards
- HuggingFace Model Hub: model card and packaging conventions
- Agent packaging: portable agent distribution best practices

### bld_quality_gate_iso_package.md
---
id: p11_qg_iso_package
kind: quality_gate
pillar: P11
title: "Gate: ISO Package"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "iso_package — portable self-contained agent bundles with tier-validated file inventories"
quality: null
tags: [quality-gate, iso-package, packaging, portable, bundle, tier, distribution]
tldr: "Gates ensuring iso_package artifacts are self-contained, tier-compliant, portability-enforced bundles with valid manifests and correct LP file mappings."
density_score: 0.93
---

# Gate: ISO Package
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: iso_package` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | `manifest.yaml` parses as valid YAML | Parse error anywhere in manifest |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem or package directory name | ID `weather_agent` in package dir `news_agent/` |
| H04 | Kind equals literal `iso_package` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All 14 required manifest fields present | Any required field absent from manifest.yaml |
| H07 | Tier is one of: `minimal`, `standard`, `complete`, `whitelabel` | Unknown or custom tier value |
| H08 | File count matches tier (minimal=3, standard=7, complete=10, whitelabel=12) | File count off by any amount |
| H09 | No hardcoded absolute paths in any bundled file | Any `/home/`, `C:\`, `~`, or machine-specific path found |
| H10 | `system_instruction.md` is <= 4096 tokens | Token count exceeds limit |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | LP mapping accuracy | 1.0 | Every file lists correct pillar-layer mapping in inventory | Most files mapped; some gaps | LP mapping absent |
| S02 | Self-containment | 1.0 | Package requires no external files to function at stated tier | Minor external deps documented | Undocumented external dependencies |
| S03 | LLM-agnostic instructions | 1.0 | `system_instruction.md` avoids model-specific syntax or API references | Minor model-specific hints | Instructions tied to one LLM vendor |
| S04 | Portability enforcement | 1.0 | All internal references use relative paths | Most relative; a few absolute slipped through | Absolute paths in multiple files |
| S05 | Tier justification | 0.5 | README or manifest explains why this tier was chosen | Tier stated, no rationale | No tier explanation |
| S06 | File inventory completeness | 1.0 | Every file in the package is listed in manifest inventory | Most listed; fewer than 2 missing | Inventory incomplete or absent |
| S07 | Token budget discipline | 1.0 | `system_instruction.md` uses 80-100% of 4096-token budget efficiently | 50-79% utilization (underused) | Under 50% or over budget |
| S08 | Version pinning | 0.5 | Manifest version pinned; changelog entry present | Version present, no changelog | No version |
| S09 | Whitelabel readiness | 0.5 | If tier=whitelabel: branding slots documented and parameterized | Partial parameterization | Not applicable or missing entirely |
| S10 | Distribution metadata | 0.5 | `author`, `license`, and `contact` all present in manifest | Partial metadata | None |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to distribution pool as golden package template |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|

### bld_schema_iso_package.md
---
kind: schema
id: bld_schema_iso_package
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for iso_package
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: iso_package
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_iso_{agent_slug}) | YES | - | Namespace compliance |
| kind | literal "iso_package" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Semantic versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| agent_name | string | YES | - | Target agent this package represents |
| tier | enum [minimal, standard, complete, whitelabel] | YES | "standard" | Package completeness level |
| files_count | integer | YES | - | Actual file count in directory |
| domain | string | YES | - | Agent primary domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "iso-package" |
| tldr | string <= 160ch | YES | - | Dense one-liner |
| portable | boolean | REC | true | No hardcoded paths in any file |
| llm_function | literal "BECOME" | REC | "BECOME" | Package carries agent identity |
| lp_mapping | object | REC | - | File-to-pillar mapping |
| system_instruction_tokens | integer | REC | - | Token count of system_instruction.md |
| density_score | float 0.80-1.00 | OPT | - | Content density across all files |
## Tier System
| Tier | Min Files | Required Contents |
|------|-----------|-------------------|
| minimal | 3 | manifest.yaml, system_instruction.md, instructions.md |
| standard | 7 | minimal + architecture.md, output_template.md, examples.md, error_handling.md |
| complete | 10 | standard + quick_start.md, input_schema.yaml, upload_kit.md |
| whitelabel | 12 | complete + upload_kit_whitelabel.md, branding_config.yaml |
## LP Mapping (file to pillar)
| File | Pillar | Purpose |
|------|--------|---------|
| manifest.yaml | P02 | Package identity and inventory |
| system_instruction.md | P03 | Full system prompt for LLM injection |
| instructions.md | P03 | Step-by-step execution protocol |
| architecture.md | P08 | Boundary, position, dependency graph |
| output_template.md | P05 | Template with {{vars}} for agent output |
| examples.md | P07 | Golden + anti-examples (min 2) |
| error_handling.md | P11 | Failure modes and remediation |
| quick_start.md | P01 | 5-minute onboarding guide |
| input_schema.yaml | P06 | Input contract definition |
| upload_kit.md | P04 | Deployment and loading instructions |
## ID Pattern
Regex: `^p02_iso_[a-z][a-z0-9_]+$`
Rule: id MUST equal directory name with p02_iso_ prefix.
## Body Structure (required sections in manifest.yaml)
1. `## Agent Identity` — who the packaged agent is, one paragraph
2. `## File Inventory` — table of all files with pillar, tier requirement, status
3. `## Tier Compliance` — declared tier, files present vs expected, gaps
4. `## Portability Notes` — platform dependencies, no hardcoded paths check
5. `## References` — source agent definition, upstream builders
## Constraints
- max_bytes: 4096 (manifest.yaml body only)
- per_file_max: 4096 bytes (each file in the package)
- system_instruction_tokens: max 4096
- min_examples: 2 (in examples.md)
- density: >= 0.80 across all files
- no_hardcoded_paths: true (no /home/, /Users/, C:\, records/)
- id == directory name prefix
- files_count MUST match actual file count
- tier MUST match actual file count thresholds

### bld_examples_iso_package.md
---
kind: examples
id: bld_examples_iso_package
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of iso_package artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: iso-package-builder
## Golden Example
INPUT: "Package the data-analyst agent as a standard ISO bundle"
OUTPUT:
```yaml
id: p02_iso_data_analyst
kind: iso_package
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
agent_name: "data-analyst"
tier: "standard"
files_count: 7
domain: "data_analysis"
llm_function: BECOME
portable: true
lp_mapping:
  manifest.yaml: P02
  system_instruction.md: P03
  instructions.md: P03
  architecture.md: P08
  output_template.md: P05
  examples.md: P07
  error_handling.md: P11
system_instruction_tokens: 2840
quality: null
tags: [iso-package, data-analysis, analytics, P02]
tldr: "Standard 7-file ISO bundle for data-analyst agent with analysis pipeline and error handling"
density_score: 0.88
```
## Agent Identity
data-analyst is a data analysis specialist. Transforms raw datasets into structured
insights via statistical analysis, visualization, and pattern detection.
## File Inventory
| File | Pillar | Tier | Status |
|------|--------|------|--------|
| manifest.yaml | P02 | minimal | present |
| system_instruction.md | P03 | minimal | present |
| instructions.md | P03 | minimal | present |
| architecture.md | P08 | standard | present |
| output_template.md | P05 | standard | present |
| examples.md | P07 | standard | present |
| error_handling.md | P11 | standard | present |
| quick_start.md | P01 | complete | absent |
| input_schema.yaml | P06 | complete | absent |
| upload_kit.md | P04 | complete | absent |
## Tier Compliance
Declared: standard. Files present: 7/7. No gaps.
## Portability Notes
- Platform: platform_agnostic
- Hardcoded paths: none
- External dependencies: none (self-contained analysis prompts)
## References
- Source agent: agents/data_analyst/README.md
- Builder: iso-package-builder v1.0.0
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_iso_ pattern (H02 pass) | kind: iso_package (H04 pass)
- 19 fields in frontmatter (H06 pass) | 3 required files present (H07 pass)
- files_count: 7 matches directory (H08 pass) | system_instruction: 2840 tokens (H09 pass)
- No hardcoded paths (H10 pass) | tier "standard" matches 7 files (S03 pass)
- tldr: 82ch (S01 pass) | tags: 4 items with "iso-package" (S02 pass) | density: 0.88 (S06 pass)
- lp_mapping present for all 7 files (S08 pass) | File Inventory table complete (S10 pass)
## Anti-Example
INPUT: "Package my helper agent"
BAD OUTPUT:
```yaml
id: helper_package
kind: package
tier: large
files_count: 3
quality: 9.0
tags: [helper]
tldr: "This is a comprehensive package that contains all the necessary files for the helper agent to function properly across various platforms."
```
Files included: manifest.yaml, prompt.txt, readme.md
FAILURES:
1. id: no `p02_iso_` prefix -> H02 FAIL
2. kind: "package" not "iso_package" -> H04 FAIL
3. quality: 9.0 (not null) -> H05 FAIL
4. Missing 10 required fields (pillar, version, created, updated, author, agent_name, domain, quality as null, tags proper, tldr proper) -> H06 FAIL
5. Required files wrong names (prompt.txt not system_instruction.md, readme.md not instructions.md) -> H07 FAIL
6. tier: "large" not in enum [minimal, standard, complete, whitelabel] -> S03 FAIL
7. tags: only 1 item, missing "iso-package" -> S02 FAIL
8. tldr: 134ch with filler ("This is a comprehensive package that contains") -> S01+S09 FAIL
9. No lp_mapping -> S08 FAIL
10. No File Inventory table -> S10 FAIL
11. No portability check -> S11 FAIL
12. No Agent Identity section -> body structure FAIL

### bld_config_iso_package.md
---
kind: config
id: bld_config_iso_package
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: iso_package Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Package directory | `{agent_slug}/` | `scout_agent/` |
| Manifest file | `manifest.yaml` | `scout_agent/manifest.yaml` |
| ISO files | lowercase with underscores | `system_instruction.md` |
| Builder directory | kebab-case | `iso-package-builder/` |
| Frontmatter fields | snake_case | `agent_name`, `files_count` |
| Agent slug | snake_case, lowercase | `knowledge_card_builder` |
| Package id | `p02_iso_{agent_slug}` | `p02_iso_scout_agent` |
Rule: id MUST equal directory name with p02_iso_ prefix.
Rule: manifest.yaml is ALWAYS the entry point file.
## File Paths
- Output: `cex/agents/{agent_slug}/manifest.yaml`
- Package dir: `cex/agents/{agent_slug}/`
- Each file lives at root of agent directory (no subdirectories)
## Size Limits (aligned with SCHEMA)
- Manifest body: max 4096 bytes
- Per-file: max 4096 bytes
- system_instruction.md: max 4096 tokens
- Density: >= 0.80 across all files
## Tier Rules
| Tier | Files | When to use |
|------|-------|-------------|
| minimal | 3 | Quick prototype, internal-only agent |
| standard | 7 | Production agent with full documentation |
| complete | 10 | Sharable agent with onboarding and deployment |
| whitelabel | 12 | Redistributable agent with branding support |
Rule: files_count MUST match actual files in directory.
Rule: tier MUST match file count (minimal=3, standard=7, complete=10, whitelabel=12).
## Portability Rules
- No hardcoded paths: `/home/`, `/Users/`, `C:\`, `records/`, `.claude/`
- No framework-specific satellite names in system_instruction.md
- All file references use relative paths within package directory
- LLM-agnostic: no provider-specific API calls in instructions.md
## LP Mapping Enum
| File | Pillar | Function |
|------|--------|----------|
| manifest.yaml | P02 | BECOME |
| system_instruction.md | P03 | BECOME |
| instructions.md | P03 | REASON |
| architecture.md | P08 | CONSTRAIN |
| output_template.md | P05 | PRODUCE |
| examples.md | P07 | GOVERN |
| error_handling.md | P11 | GOVERN |
| quick_start.md | P01 | INJECT |
| input_schema.yaml | P06 | CONSTRAIN |
| upload_kit.md | P04 | CALL |

### bld_output_template_iso_package.md
---
kind: output_template
id: bld_output_template_iso_package
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an iso_package manifest
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: iso_package
```yaml
id: p02_iso_{{agent_slug}}
kind: iso_package
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
agent_name: "{{agent_name}}"
tier: "{{minimal|standard|complete|whitelabel}}"
files_count: {{integer_matching_directory}}
domain: "{{primary_domain}}"
llm_function: BECOME
portable: {{true|false}}
lp_mapping:
  manifest.yaml: P02
  system_instruction.md: P03
  instructions.md: P03
  architecture.md: P08
  output_template.md: P05
  examples.md: P07
  error_handling.md: P11
  quick_start.md: P01
  input_schema.yaml: P06
  upload_kit.md: P04
system_instruction_tokens: {{integer_token_count}}
quality: null
tags: [iso-package, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Agent Identity
{{agent_name}} is a {{domain}} specialist.
{{one_sentence_what_this_package_enables}}
## File Inventory
| File | Pillar | Tier | Status |
|------|--------|------|--------|
| manifest.yaml | P02 | minimal | present |
| system_instruction.md | P03 | minimal | present |
| instructions.md | P03 | minimal | present |
| architecture.md | P08 | standard | {{present|absent}} |
| output_template.md | P05 | standard | {{present|absent}} |
| examples.md | P07 | standard | {{present|absent}} |
| error_handling.md | P11 | standard | {{present|absent}} |
| quick_start.md | P01 | complete | {{present|absent}} |
| input_schema.yaml | P06 | complete | {{present|absent}} |
| upload_kit.md | P04 | complete | {{present|absent}} |
| upload_kit_whitelabel.md | P04 | whitelabel | {{present|absent}} |
| branding_config.yaml | P09 | whitelabel | {{present|absent}} |
## Tier Compliance
Declared: {{tier}}. Files present: {{files_count}}/{{tier_expected}}.
{{gap_description_if_any}}
## Portability Notes
- Platform: {{platform_agnostic|platform_specific}}
- Hardcoded paths: {{none|list_of_violations}}
- External dependencies: {{list_or_none}}
## References
- Source agent: {{agent_definition_path}}
- Builder: iso-package-builder v1.0.0

### bld_architecture_iso_package.md
---
kind: architecture
id: bld_architecture_iso_package
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of iso_package — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| manifest.yaml | Entry point: identity, tier, file inventory, LP mapping | author | required |
| system_instruction.md | Agent persona and behavioral rules, capped at 4096 tokens | author | required |
| instructions.md | Operational steps the agent follows (P03) | author | required |
| quick_start.md | Minimal usage example for immediate deployment | author | tier >= standard |
| examples.md | Input/output demonstration pairs | author | tier >= standard |
| input_schema.yaml | Typed input contract for the agent (P06) | author | tier >= complete |
| output_schema.yaml | Typed output contract for the agent (P06) | author | tier >= complete |
| knowledge_base/ | Domain knowledge cards bundled for retrieval | author | tier = whitelabel |
| upload_kit.md | Deployment instructions per target platform | author | tier >= standard |
| tier_label | One of: minimal / standard / complete / whitelabel | author | required |
## Dependency Graph
```
agent         --produces--> iso_package
system_prompt --produces--> system_instruction.md
knowledge_card --produces--> knowledge_base/
iso_package   --produces--> upload_kit
iso_package   --consumed_by--> spawn_config
iso_package   --consumed_by--> workflow
```
| From | To | Type | Data |
|------|----|------|------|
| agent | iso_package | data_flow | canonical identity, capabilities, domain |
| system_prompt | iso_package | data_flow | persona text becomes system_instruction.md |
| knowledge_card | iso_package | data_flow | domain facts bundled into knowledge_base/ |
| iso_package | upload_kit | produces | deployment instructions derived from manifest |
| iso_package | spawn_config | data_flow | tier, file paths, model recommendations |
| iso_package | workflow | data_flow | self-contained execution node |
## Boundary Table
| iso_package IS | iso_package IS NOT |
|----------------|-------------------|
| Portable, self-contained multi-file bundle | Canonical agent definition in a repository |
| Tiered completeness: minimal to whitelabel | Boot configuration (model flags, MCP profiles) |
| LLM-agnostic (no hardcoded model names) | Mental model for routing and decision-making |
| Static distributable artifact, not runtime | Spec for the underlying LLM itself |
| manifest.yaml is the required entry point | Single-file artifact |
| system_instruction.md capped at 4096 tokens | Fallback chain or multi-model routing logic |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | manifest.yaml, tier_label | Declare the package and its completeness level |
| Behavior | system_instruction.md, instructions.md | Carry agent persona and operational recipe |
| Contract | input_schema.yaml, output_schema.yaml | Define typed entry and exit data shapes |
| Knowledge | knowledge_base/, examples.md | Bundle domain facts and usage demonstrations |
| Deployment | upload_kit.md, quick_start.md | Enable immediate use on any target platform |

### bld_collaboration_iso_package.md
---
kind: collaboration
id: bld_collaboration_iso_package
pillar: P12
llm_function: COLLABORATE
purpose: How iso-package-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: iso-package-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how do I bundle this agent into a portable, self-contained, tier-validated package?"
I do not define agents. I do not write system prompts.
I package agent artifacts so they can be distributed and deployed on any compatible runtime.
## Crew Compositions
### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge"
  2. agent-builder -> "agent definition"
  3. instruction-builder -> "execution steps"
  4. boot-config-builder -> "provider configuration"
  5. iso-package-builder -> "portable deployable package (manifest + files)"
```
### Crew: "Distribution Pipeline"
```
  1. agent-builder -> "agent definition"
  2. fallback-chain-builder -> "model degradation config"
  3. guardrail-builder -> "safety boundaries"
  4. iso-package-builder -> "self-contained bundle (minimal/standard/complete)"
```
## Handoff Protocol
### I Receive
- seeds: agent name, target tier (minimal/standard/complete/whitelabel)
- optional: file inventory, LP mapping overrides, token budget constraints
### I Produce
- iso_package artifact (manifest.yaml + tier-appropriate files)
- committed to: `cex/P02/examples/p02_iso_{agent}/`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- agent-builder: provides agent definition to package
- boot-config-builder: provides provider configs included in package
- instruction-builder: provides execution steps included in package
- fallback-chain-builder: provides degradation config for resilient packages
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| _builder-builder | Meta-builder ensures package structure follows conventions |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `iso-package-builder` for pipeline function `BECOME`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
