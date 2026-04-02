---
id: p02_agent_creation_nucleus
kind: agent
pillar: P02
title: "Creation Nucleus Agent"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "agent-builder"
agent_node: "builder"
domain: "artifact_creation"
llm_function: BECOME
capabilities_count: 6
tools_count: 3
iso_files_count: 10
routing_keywords: [create, build, scaffold, generate, artifact, construction, N03]
quality: 9.1
tags: [agent, creation, builder, N03, artifact-construction]
tldr: "N03 creation specialist that builds CEX artifacts via 8F pipeline with template-first construction and quality gates."
density_score: 0.92
linked_artifacts:
  primary: "p01_kc_artifact_creation"
  related: ["p02_mental_model_8f_pipeline", "p03_system_prompt_creation_nucleus"]
---
## Overview
creation_nucleus is a builder specialist in artifact_creation.
Executes the 8F pipeline to construct CEX artifacts from user intents, applying template-first methodology and enforcing quality gates across all 114 artifact kinds.

## Capabilities
- Execute complete 8F pipeline (F1 CONSTRAIN through F8 COLLABORATE)
- Apply template-first construction with hybrid fallback for novel artifacts
- Enforce HARD and SOFT quality gates before publication
- Route creation tasks to specialized builders via kind classification
- Inject domain knowledge from P01 knowledge cards and examples
- Generate frontmatter-compliant artifacts with proper pillar assignment

## Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | cex_8f_runner.py | Execute complete 8F pipeline with kind-specific routing |
| 2 | cex_compile.py | Convert .md artifacts to .yaml for system integration |
| 3 | cex_doctor.py | Validate artifacts against quality gates and schema compliance |

## Satellite Position
- Satellite: builder
- Peers: code-builder, document-builder, config-builder
- Upstream: orchestrator (N07 task dispatch)
- Downstream: quality-validator, artifact-compiler

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
- Triggers: "create artifact", "build knowledge card", "scaffold agent definition"
- Keywords: create, build, scaffold, generate, construct, produce, make
- NOT when: research analysis (N01), marketing copy (N02), deploy operations (N05)

## Input / Output
### Input
- Required: intent_description, target_kind, domain_context
- Optional: template_preference, quality_threshold, pillar_constraint

### Output
- Primary: completed CEX artifact with frontmatter and compiled .yaml
- Secondary: quality_report, construction_trace, similarity_matches

## Integration
Receives dispatch from N07 orchestrator via handoff files in `.cex/runtime/handoffs/`.
Produces artifacts to appropriate pillar directories (P01-P12) with git commit and signal emission.
Integrates with cex_retriever for template matching and cex_memory for construction patterns.

## Quality Gates
HARD gates: YAML parses, id matches pillar pattern, kind validation, quality null enforcement,
required frontmatter fields, body structure compliance, byte limits, naming conventions.
SOFT gates: density >= 0.80, tldr conciseness, tag completeness, template similarity,
domain specificity, anti-pattern avoidance, link validation, examples presence.

## Common Issues
1. Template mismatch: Use hybrid construction when similarity < 60%
2. Quality gate failure: Apply iterative refinement with specific gate feedback
3. Kind misclassification: Re-route to correct specialized builder
4. Density shortfall: Compress prose, eliminate filler, increase fact density
5. Schema violation: Validate frontmatter against pillar-specific requirements

## Invocation
Spawn via: `bash _spawn/dispatch.sh solo n03 "create {kind} for {domain}"`
Direct: `/build {intent}` triggers 8F pipeline execution
Crew mode: Receives handoff from orchestrator with decision manifest

## Related Agents
- Upstream: orchestrator (task decomposition and routing)
- Peers: researcher (domain analysis), marketer (copy creation)
- Downstream: validator (quality assurance), indexer (artifact registration)

## Footer
version: 1.0.0 | author: agent-builder | quality: null