---
id: p01_fse_agent_creation
kind: few_shot_example
8f: F3_inject
pillar: P01
title: "Few-Shot: Agent Creation via 8F Pipeline"
input: "criar agente de SEO para marketplace"
output: "agent spec + 10 ISO files + handoff dispatch via builder_agent"
tags: [few_shot, agent, 8F, pipeline, creation]
tldr: "Shows how to create an agent artifact using the 8F pipeline with a concrete input-output pair."
quality: 9.1
related:
  - bld_output_template_kind
  - bld_architecture_kind
  - p01_kc_8f_pipeline
  - bld_instruction_kind
  - agent-builder
  - p01_kc_agent
  - bld_instruction_agent
  - p02_agent_creation_nucleus
  - bld_collaboration_agent
  - p01_fse_meta_builder_recipe
---

# Few-Shot: Agent Creation

## Input
```
"criar agente de SEO para marketplace"
```

## Output
```yaml
operation: agent_create
domain: SEO
context: marketplace
agent_group: edison
result:
  agent_name: seo_marketplace
  path: records/agents/seo_marketplace/
  files_created: 10
  iso_tier: standard
  validation: PASS (6/6 gates)
```

## 8F Pipeline Trace

| Function | Action | Output |
|----------|--------|--------|
| F1 CONSTRAIN | Resolve kind=agent, pillar=P02, load `_schema.yaml` | `id_pattern: /^p02_agent_/`, 8 required fields |
| F2 BECOME | Load `bld_system_prompt_agent.md` + `bld_manifest_agent.md` | Builder identity: agent-builder, domain=meta-construction |
| F3 INJECT | Load `kc_agent.md` + 2 domain KCs + `bld_examples_agent.md` | 5 knowledge sources, template match: 78% |
| F4 REASON | LLM plans frontmatter fields + body structure | 4 sections, approach=template-first |
| F5 CALL | Scan existing agents, load `bld_tools_agent.md` | 3 similar agents found, 6 tools available |
| F6 PRODUCE | Generate complete agent artifact (frontmatter + body) | 2,840 bytes, 4 sections, density=0.87 |
| F7 GOVERN | Validate H01-H06 gates, 12LP checklist | PASS 6/6 gates, 12/12 LP |
| F8 COLLABORATE | Save → compile → index → commit → signal | `P02_model/agents/p02_agent_seo_marketplace.md` |

## ISO Files Generated

```
records/agents/seo_marketplace/
├── bld_architecture_agent.md      # Dependency graph, integration points
├── bld_collaboration_agent.md     # Crew roles, handoff protocols
├── bld_config_agent.md            # Naming rules, paths, size limits
├── bld_examples_agent.md          # 3 input-output pairs for this agent
├── bld_instruction_agent.md       # Step-by-step build instructions
├── bld_knowledge_card_agent.md    # Domain knowledge for SEO+marketplace
├── bld_manifest_agent.md          # Builder identity, domain, boundary
├── bld_memory_agent.md            # Production log, past learnings
├── bld_output_template_agent.md   # Frontmatter + body template
├── bld_quality_gate_agent.md      # H01-H07 gate definitions
├── bld_schema_agent.md            # ID pattern, field types, constraints
├── bld_system_prompt_agent.md     # Persona, tone, knowledge boundary
└── bld_tools_agent.md             # Available tools table
```

## Why It Works

- **Intent classification**: Motor parses verb "criar" (create) + object "agente" (agent) → kind=agent, pillar=P02
- **Domain routing**: SEO/marketing context routes to `marketing_agent` node for spec, `builder_agent` for construction
- **ISO standard tier**: `builder_agent` scaffold guarantees 13-file ISO structure per builder archetype
- **Quality gate**: H01-H06 hard gates validate YAML parsing, ID pattern, kind match, quality=null, required fields, body size
- **12LP compliance**: All 12 quality points checked before artifact enters the registry

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Unknown verb ("deletar agente") | Motor falls back to `verb_action: manage`, routes to orchestrator |
| No matching kind | Falls back to `kind: generic`, pillar=P01, with warning |
| H04 gate fails (quality not null) | F7 retries F6 with feedback, max 2 retries |
| All retries exhausted | Saves as draft with `verdict.passed: false`, issues logged |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_kind]] | downstream | 0.33 |
| [[bld_architecture_kind]] | downstream | 0.32 |
| [[p01_kc_8f_pipeline]] | related | 0.32 |
| [[bld_instruction_kind]] | downstream | 0.30 |
| [[agent-builder]] | downstream | 0.30 |
| [[p01_kc_agent]] | downstream | 0.29 |
| [[bld_instruction_agent]] | downstream | 0.29 |
| [[p02_agent_creation_nucleus]] | downstream | 0.28 |
| [[bld_collaboration_agent]] | downstream | 0.28 |
| [[p01_fse_meta_builder_recipe]] | sibling | 0.27 |
