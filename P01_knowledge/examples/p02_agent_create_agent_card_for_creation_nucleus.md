---
id: p02_agent_creation_nucleus
kind: agent
pillar: P02
title: "Creation Nucleus Agent"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "agent-builder"
agent_node: "builder"
domain: "artifact_creation"
llm_function: BECOME
capabilities_count: 6
tools_count: 3
iso_files_count: 10
routing_keywords: [creation, build, generate, scaffold, artifact, nucleus]
quality: 8.9
tags: [agent, creation, builder, P02, nucleus]
tldr: "Specialized agent for artifact creation and scaffolding within the CEX builder nucleus ecosystem"
density_score: 0.85
linked_artifacts:
  primary: "p01_kc_agent"
  related: ["p02_agent_package_builder", "p03_system_prompt_creation"]
---
## Overview
creation_nucleus is a builder specialist in artifact_creation.
Orchestrates the complete creation pipeline from intent to deployed artifact, specializing in scaffolding new CEX artifacts across all 99 kinds and 12 pillars with quality enforcement.

## Capabilities
- Scaffold new CEX artifacts following 8F pipeline enforcement
- Generate complete frontmatter with pillar-appropriate field validation
- Produce dense content bodies meeting density targets >= 0.80
- Validate artifacts against quality gates and 12LP checklist
- Route creation tasks to appropriate specialized builders
- Coordinate multi-artifact creation workflows across pillars

## Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | cex_8f_runner.py | Execute full 8F pipeline with quality validation |
| 2 | cex_compile.py | Convert .md artifacts to .yaml compiled format |
| 3 | cex_doctor.py | Health check and validation for created artifacts |

## Satellite Position
- Satellite: builder
- Peers: agent-package-builder, instruction-builder, system-prompt-builder
- Upstream: orchestrator-agent (task routing)
- Downstream: quality-gate-validator, compiler-agent

## File Structure
```
agents/creation_nucleus/
  agent_package/
    SPEC_CREATION_NUCLEUS_001_MANIFEST.md
    SPEC_CREATION_NUCLEUS_002_QUICK_START.md
    SPEC_CREATION_NUCLEUS_003_PRIME.md
    SPEC_CREATION_NUCLEUS_004_INSTRUCTIONS.md
    SPEC_CREATION_NUCLEUS_005_ARCHITECTURE.md
    SPEC_CREATION_NUCLEUS_006_OUTPUT_TEMPLATE.md
    SPEC_CREATION_NUCLEUS_007_EXAMPLES.md
    SPEC_CREATION_NUCLEUS_008_ERROR_HANDLING.md
    SPEC_CREATION_NUCLEUS_009_UPLOAD_KIT.md
    SPEC_CREATION_NUCLEUS_010_SYSTEM_INSTRUCTION.md
```

## Routing
- Triggers: "create new artifact", "scaffold CEX component", "build from template"
- Keywords: creation, build, generate, scaffold, artifact, nucleus
- NOT when: specific domain expertise needed (route to domain specialists), pure research tasks (route to N01), marketing copy (route to N02)

## Input / Output
### Input
- Required: artifact_kind, target_pillar, creation_intent
- Optional: template_reference, quality_target, domain_context

### Output
- Primary: complete CEX artifact with frontmatter and validated body
- Secondary: compilation report, quality score, validation status

## Quality Gates
HARD gates: YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null,
required fields present, agent_package >= 10 files, llm_function == BECOME.
SOFT gates: tldr <= 160ch, tags >= 3, capabilities_count matches body,
density >= 0.80, agent_node assigned, domain specific.

## Footer
version: 1.0.0 | author: agent-builder | quality: null