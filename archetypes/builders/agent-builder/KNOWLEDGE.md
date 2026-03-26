---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for agent production
sources: CEX schema, iso_vectorstore pattern, CODEXA agent catalog, agentic AI literature
---

# Domain Knowledge: agent

## Foundational Concept
An agent is the core runtime entity in any agentic AI system. It represents a persistent
identity — who the LLM BECOMES when loaded — with scoped capabilities, assigned tools,
a satellite position, and a structured iso_vectorstore (10+ ISO files) that makes it
portable, searchable, and auditable. The CEX agent kind (P02) is the canonical definition.

## Agent vs Nearby Types

| Type | What it is | Why it is NOT agent |
|------|------------|---------------------|
| system_prompt | How the agent speaks — rules and persona | Voice/style layer, not identity package |
| skill | Executable capability with phases and trigger | Callable function, not persistent identity |
| mental_model (P02) | Static design-time routing blueprint | Blueprint, not runtime entity |
| mental_model (P10) | Runtime session state | Ephemeral state, not permanent definition |
| model_card | LLM spec (pricing, context, capabilities) | Describes underlying model, not agent using it |
| iso_package | Portable distributable bundle | Distribution format, not canonical definition |

## ISO Vectorstore Pattern
Every agent requires 10+ ISO files:

| File | Pillar | Purpose |
|------|--------|---------|
| ISO_*_001_MANIFEST.md | P02 | Identity, version, capabilities list |
| ISO_*_002_QUICK_START.md | P01 | 5-minute onboarding guide |
| ISO_*_003_PRIME.md | P03 | Entry point prompt for this agent |
| ISO_*_004_INSTRUCTIONS.md | P03 | Step-by-step execution protocol |
| ISO_*_005_ARCHITECTURE.md | P08 | Boundary, dependency graph, position |
| ISO_*_006_OUTPUT_TEMPLATE.md | P05 | Template with {{vars}} for agent output |
| ISO_*_007_EXAMPLES.md | P07 | Golden + anti-examples |
| ISO_*_008_ERROR_HANDLING.md | P11 | Failure modes and remediation |
| ISO_*_009_UPLOAD_KIT.md | P04 | How to load/deploy the agent |
| ISO_*_010_SYSTEM_INSTRUCTION.md | P03 | Full system prompt for LLM injection |

## Key Patterns
- BECOME function: agent definition is read by LLM which then assumes that identity
- Satellite assignment: every agent belongs to a satellite or is explicitly "agnostic"
- Capability scoping: 4-8 concrete bullets — no vague "can help with" entries
- Boundary discipline: each agent explicitly lists what it does NOT handle
- Density rule: no filler — every sentence in the artifact carries information
- iso_vectorstore naming: ISO_{AGENT_UPPER}_{NNN}_{TYPE}.md — consistent across all agents

## CEX-Specific Fields

| Field | Justification | No direct industry equivalent |
|-------|--------------|-------------------------------|
| satellite | Links agent to owning satellite in the grid | CODEXA-specific orchestration unit |
| iso_files_count | Integrity check for vectorstore completeness | CEX-specific |
| capabilities_count | Ensures body matches frontmatter declaration | CEX-specific |
| routing_keywords | Drives brain_query discovery | CEX brain search |
| llm_function | BECOME signals identity vs callable | CEX taxonomy |

## References
- CEX P02_model/_schema.yaml — canonical field definitions
- CEX archetypes/builders/system-prompt-builder/ — upstream dependency
- CODEXA records/agents/ — 118+ real agent examples with complete iso_vectorstore
- Anthropic: Claude system prompt and identity patterns
