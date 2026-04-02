---
id: p02_agent_creation_nucleus_agent
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
tools_count: 4
iso_files_count: 10
routing_keywords: [create, build, generate, artifact, nucleus, construction, scaffold, produce]
quality: 9.1
tags: [agent, builder, artifact_creation, P02, nucleus]
tldr: "Builder nucleus specialist in artifact construction - analyzes requirements, generates high-quality artifacts, validates outputs across all CEX kinds"
density_score: 0.89
---
## Overview
creation_nucleus_agent is a builder specialist in artifact construction and generation. Serves as the primary creation engine for CEX systems, transforming user intents into complete artifacts across all 114 supported kinds with quality validation and template-driven construction.

## Architecture
### Capabilities
- Analyzes user intents and decomposes them into buildable specifications
- Generates complete artifacts following 8F pipeline and quality gates
- Validates artifact output against schemas and quality thresholds  
- Coordinates multi-artifact builds with dependency management
- Manages template libraries and construction patterns
- Orchestrates builder crews for complex creation tasks

### Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | cex_compile.py | Artifact compilation and validation |
| 2 | cex_8f_runner.py | Full 8F pipeline execution |
| 3 | cex_query.py | Builder discovery and matching |
| 4 | cex_doctor.py | Quality validation and health checks |

### Satellite Position
- Satellite: builder
- Peers: instruction_builder, system_prompt_builder, schema_builder
- Upstream: plan_builder, mental_model_builder  
- Downstream: quality_gate_builder, validator_builder

## File Structure
```
agents/creation_nucleus_agent/
  agent_package/
    SPEC_CREATION_NUCLEUS_AGENT_001_MANIFEST.md
    SPEC_CREATION_NUCLEUS_AGENT_002_QUICK_START.md
    SPEC_CREATION_NUCLEUS_AGENT_003_PRIME.md
    SPEC_CREATION_NUCLEUS_AGENT_004_INSTRUCTIONS.md
    SPEC_CREATION_NUCLEUS_AGENT_005_ARCHITECTURE.md
    SPEC_CREATION_NUCLEUS_AGENT_006_OUTPUT_TEMPLATE.md
    SPEC_CREATION_NUCLEUS_AGENT_007_EXAMPLES.md
    SPEC_CREATION_NUCLEUS_AGENT_008_ERROR_HANDLING.md
    SPEC_CREATION_NUCLEUS_AGENT_009_UPLOAD_KIT.md
    SPEC_CREATION_NUCLEUS_AGENT_010_SYSTEM_INSTRUCTION.md
```

## When to Use
### Triggers
- "Create [artifact_type] for [domain]"
- "Build me a [kind] that does [function]"  
- "Generate [artifact] with [requirements]"
- "I need to scaffold [artifact_type]"

### Keywords
create, build, generate, artifact, construct, scaffold, produce, make

### NOT when
- Simple queries about existing artifacts (knowledge_card_builder)
- Research or analysis tasks (intelligence_builder)
- Marketing copy or content (marketing_builder)
- Code deployment or operations (operations_builder)

## Input / Output
### Input
- Required: intent_description, target_kind, domain_context
- Optional: quality_target, template_preference, constraints

### Output  
- Primary: complete artifact with frontmatter + body
- Secondary: quality_assessment, build_log, dependency_graph

## Integration
Receives build requests from orchestrator or direct user interaction. Produces artifacts for downstream validation, compilation, and deployment. Integrates with all pillar builders through standardized handoff protocols.

## Quality Gates
HARD gates: YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null, required fields present, agent_package >= 10 files, llm_function == BECOME.

SOFT gates: tldr <= 160 characters, tags >= 3, capabilities_count matches body, density >= 0.80, agent_node assigned, domain specific.

## Common Issues
1. Intent ambiguity: decompose complex intents into specific artifact types before building
2. Quality threshold miss: validate against gates early, iterate on content density  
3. Template mismatch: verify template compatibility with target kind before generation
4. Dependency conflicts: check artifact relationships and resolve before final output
5. Schema violations: validate frontmatter fields against pillar schemas during construction

## Invocation
```bash
python cex_run.py --intent "create agent for X" --nucleus creation_nucleus_agent
```

## Related Agents
- instruction_builder: provides step-by-step creation protocols
- system_prompt_builder: defines agent behavioral patterns
- quality_gate_builder: establishes validation criteria
- validator_builder: performs artifact quality assessment

## Footer
version: 1.0.0 | author: agent-builder | quality: null