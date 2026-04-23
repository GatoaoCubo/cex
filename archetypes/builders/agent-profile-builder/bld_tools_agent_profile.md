---
kind: tools
id: bld_tools_agent_profile
pillar: P04
llm_function: CALL
purpose: Tools available for agent_profile production
quality: 8.9
title: "Tools Agent Profile"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_profile, builder, tools]
tldr: "Tools available for agent_profile production"
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p01_kc_agent
  - bld_collaboration_agent
  - agent-builder
  - bld_architecture_agent_profile
  - bld_architecture_agent
  - bld_collaboration_effort_profile
  - bld_examples_effort_profile
  - bld_knowledge_card_agent
  - agent-profile-builder
  - bld_tools_capability_registry
---

## Production Tools
| Tool              | Purpose                          | When                          |
|-------------------|----------------------------------|-------------------------------|
| cex_compile.py    | Compile agent profiles into code | Deploying agent systems       |
| cex_score.py      | Evaluate profile quality         | Validating agent performance  |
| cex_retriever.py  | Fetch external data sources      | Building knowledge base       |
| cex_doctor.py     | Diagnose profile inconsistencies | Debugging agent behavior      |
| cex_analyzer.py   | Deep profile analysis            | Optimizing agent parameters   |
| cex_optimizer.py  | Tune agent configuration         | Refining system performance   |

## Validation Tools
| Tool              | Purpose                          | When                          |
|-------------------|----------------------------------|-------------------------------|
| val_check.py      | Validate syntax and structure    | Initial profile creation      |
| val_compare.py    | Compare profile versions         | Version control               |
| val_audit.py      | Ensure compliance with standards | Regulatory checks             |

## External References
- LangChain (agent orchestration framework)
- Hugging Face Transformers (NLP models)
- Neo4j (knowledge graph storage)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agent]] | upstream | 0.35 |
| [[bld_collaboration_agent]] | downstream | 0.34 |
| [[agent-builder]] | upstream | 0.32 |
| [[bld_architecture_agent_profile]] | downstream | 0.29 |
| [[bld_architecture_agent]] | downstream | 0.28 |
| [[bld_collaboration_effort_profile]] | downstream | 0.25 |
| [[bld_examples_effort_profile]] | downstream | 0.25 |
| [[bld_knowledge_card_agent]] | upstream | 0.24 |
| [[agent-profile-builder]] | upstream | 0.24 |
| [[bld_tools_capability_registry]] | sibling | 0.23 |
