# ISO Package Spec v1.0

> Universal portable format for AI agent distribution.
> Copy folder -> paste in any LLM/pipeline -> agent works.

## What It Is

An ISO Package is a self-contained, portable bundle that fully defines an AI agent.
It is LLM-agnostic: the same package works with Claude, GPT-4, Gemini, LLaMA, or any custom pipeline.

**Analogy**: npm/pip/docker packages code. ISO packages agents.

## Anatomy of an ISO Package

```
agent_name/
  manifest.yaml            # REQUIRED: identity + capabilities + dependencies
  system_instruction.md    # REQUIRED: system prompt (copy-paste in any LLM)
  instructions.md          # REQUIRED: how to use the agent
  architecture.md          # RECOMMENDED: diagram + flow
  output_template.md       # RECOMMENDED: output format spec
  examples.md              # RECOMMENDED: input/output pairs
  error_handling.md        # RECOMMENDED: common errors + solutions
  quick_start.md           # OPTIONAL: getting started in 5 min
  input_schema.yaml        # OPTIONAL: input contract
  upload_kit.md            # OPTIONAL: platform installation guide
  upload_kit_whitelabel.md # OPTIONAL: white-label version
```

## Required Files

### manifest.yaml

Identity card of the agent. Machine-readable metadata.

```yaml
id: agent_name
version: "1.0.0"
kind: agent_package
title: "Human-Readable Agent Name"
description: "One-line description of what this agent does"
domain: "marketing"           # primary domain
agent_group: "marketing_agent"             # organization agent_group (if applicable)
quality: 8.5                  # CEX quality score

capabilities:
  - "capability_1"
  - "capability_2"

target_llms:
  - claude
  - gpt4
  - gemini
  - llama

min_context: 8192             # minimum context window (tokens)
tools_required: []            # MCP tools, APIs, external deps

variables:                    # template variables for customization
  AGENCY_NAME: "Your Agency"
  DOMAIN: "your-domain"

tags:
  - tag1
  - tag2

created: "2026-03-23"
updated: "2026-03-23"
```

### system_instruction.md

The core system prompt. Must be:
- **Self-contained**: works as the ONLY file pasted into any LLM
- **No external dependencies**: no file paths, no imports
- **Templated**: uses `{{VARIABLES}}` for customization
- **Compact**: < 4096 tokens (fits in any context window)

### instructions.md

Human-readable guide for using the agent:
- When to use (and when NOT to use)
- Step-by-step usage
- Integration with other agents
- Expected inputs and outputs

## Maturity Tiers

| Tier | Files | Status | Use Case |
|------|:-----:|--------|----------|
| Minimal | 3 (manifest + system + instructions) | Prototype | Quick test |
| Standard | 7 (+arch, output, examples, errors) | Production | Most agents |
| Complete | 10+ (+quickstart, upload, schemas) | Enterprise | Distribution |
| Whitelabel | 12+ (+whitelabel versions) | Commercial | Resale/licensing |

### Tier Requirements

**Minimal** (3 files):
- `manifest.yaml` with all required fields
- `system_instruction.md` < 4096 tokens
- `instructions.md` with usage guide

**Standard** (7 files): Minimal +
- `architecture.md` with flow diagram
- `output_template.md` with format spec
- `examples.md` with >= 2 input/output pairs
- `error_handling.md` with >= 3 error scenarios

**Complete** (10+ files): Standard +
- `quick_start.md` with 5-min setup
- `input_schema.yaml` with JSON/YAML contract
- `upload_kit.md` with platform instructions

**Whitelabel** (12+ files): Complete +
- `upload_kit_whitelabel.md` with branding variables
- `system_instruction_whitelabel.md` with `{{AGENCY_NAME}}` substitution

## Portability Rules

1. **No hardcoded paths**: no `C:/`, `/home/`, `/Users/` in any file
2. **No platform-specific commands**: use generic instructions
3. **Variables for customization**: `{{VAR}}` syntax, declared in manifest
4. **Token budget**: system_instruction.md < 4096 tokens
5. **UTF-8 encoding**: all files must be UTF-8
6. **Markdown format**: all .md files use standard CommonMark

## CEX pillar Mapping

Each ISO file maps to a CEX Liquidity Pool:

| ISO File | CEX pillar | Type |
|----------|:------:|------|
| manifest.yaml | P02 | agent |
| system_instruction.md | P03 | system_prompt |
| instructions.md | P03 | instruction |
| architecture.md | P08 | pattern |
| output_template.md | P05 | output_schema |
| examples.md | P07 | golden_test |
| error_handling.md | P11 | bugloop |
| quick_start.md | P01 | knowledge_card |
| input_schema.yaml | P06 | input_schema |
| upload_kit.md | P04 | skill |

## Quality Gates

Before publishing an ISO Package:

1. **manifest.yaml** present and valid YAML
2. **system_instruction.md** < 4096 tokens
3. **At least 2 concrete examples** (input/output pairs) in examples.md
4. **No hardcoded paths** (scan for `C:/`, `/home/`, `/Users/`, absolute paths)
5. **Density >= 0.8** in all .md files (information density metric)
6. **Overall score >= 8.0** across all quality dimensions

## Existing Inventory

organization currently has **118 agents** in ISO format with **~1148 files** across the pool.
The ISO format has been battle-tested across all 7 agent_groups (orchestrator, research_agent, marketing_agent, builder_agent, knowledge_agent, operations_agent, commercial_agent).

### Legacy Naming Convention

Existing agents use the naming pattern:
```
ISO_{AGENT_GROUP}_{NNN}_{TYPE}.md
```

Example: `ISO_marketing_agent_015_MANIFEST.md`, `ISO_builder_agent_032_SYSTEM_INSTRUCTION.md`

The canonical ISO Package spec uses simplified names (`manifest.yaml`, `system_instruction.md`)
for portability. The compile/decompile tools handle conversion between formats.

## Tooling

| Tool | Purpose |
|------|---------|
| `_tools/compile_iso.py` | Compile CEX pillar sources into ISO Package |
| `_tools/decompile_iso.py` | Decompile existing ISO Package into CEX pillars |
| `_tools/validate_iso.py` | Validate ISO Package completeness + quality |

---

*ISO Package Spec v1.0 | CEX Framework | 2026-03-23*
