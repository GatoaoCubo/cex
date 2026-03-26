---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for iso_package production
sources: CEX schema, ISO 42001 AI management, agent packaging patterns, CODEXA iso_vectorstore
---

# Domain Knowledge: iso_package

## Foundational Concept
An iso_package is a self-contained, portable, LLM-agnostic bundle that encapsulates
an AI agent's complete operational context. Inspired by container images (Docker) and
ISO 42001 AI management systems, the package provides everything needed to instantiate
an agent on any compatible runtime. The CEX iso_package kind (P02) standardizes this
into a tiered file system with pillar-mapped contents and quality validation.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Docker images | Layered container with manifest + files | Tiered package with manifest.yaml |
| ISO 42001 | AI management system documentation | Quality gates, audit trail, portability |
| HuggingFace Model Hub | Model card + weights + tokenizer | manifest + system_instruction + instructions |
| LangChain agents | Agent definition + tools + prompts | manifest + instructions + system_instruction |
| OpenAI GPT configs | System prompt + knowledge + actions | system_instruction + instructions + input_schema |

## Key Patterns
- Tier escalation: start minimal (3 files), promote to standard (7) when production-ready
- Manifest-first: manifest.yaml is the single entry point — everything discoverable from it
- LP mapping: each file maps to a CEX pillar — enables fractal navigation within the package
- Token budgeting: system_instruction.md capped at 4096 tokens to fit context windows
- Portability: zero hardcoded paths guarantees cross-platform deployment
- File inventory: manifest lists all files with status (present/absent) for audit
- Density: every file must be >= 0.80 density — no filler, no "this document describes"

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| tier | Graduated completeness (3/7/10/12 files) | Docker multi-stage builds |
| lp_mapping | File-to-pillar mapping for fractal navigation | No direct equivalent |
| portable | Boolean portability guarantee | Docker --platform flag |
| system_instruction_tokens | Token budget enforcement | Context window management |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT iso_package |
|------|------------|--------------------------|
| agent (P02) | Canonical definition in repo | Source definition, not distributable bundle |
| boot_config (P02) | Provider-specific init params | How to start, not what to package |
| model_card (P02) | LLM spec (pricing, context) | Describes underlying model, not agent package |
| spawn_config (P12) | Runtime spawn parameters | Orchestration config, not portable bundle |
| upload_kit (file) | Deployment instructions | One file inside iso_package, not the package |

## References
- CEX P02_model/_schema.yaml — canonical field definitions for iso_package
- ISO 42001:2023 — AI management systems (portability and documentation)
- Docker OCI Image Spec — layered manifest pattern
- CODEXA records/agents/ — 118+ agents with complete iso_vectorstore
