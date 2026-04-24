---
id: n00_mcp_app_extension_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "MCP App Extension -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, mcp_app_extension, p04, n00, archetype, template]
density_score: 0.99
related:
  - bld_schema_mcp_app_extension
  - bld_schema_reranker_config
  - bld_schema_marketplace_app_manifest
  - bld_schema_app_directory_entry
  - bld_schema_multimodal_prompt
  - bld_schema_voice_pipeline
  - bld_schema_search_strategy
  - bld_schema_thinking_config
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An mcp_app_extension is an MCP (Model Context Protocol) Apps Extension that defines the app manifest, installation procedure, launch lifecycle, and termination sequence for a standalone MCP application. It enables LLMs to install, run, and interact with desktop or cloud applications through the MCP protocol. The output is a complete app extension specification that MCP hosts can discover, install, and manage autonomously.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `mcp_app_extension` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| app_name | string | yes | Application display name |
| install_command | string | yes | Command to install the application |
| launch_command | string | yes | Command to start the application |
| terminate_command | string | yes | Command to cleanly stop the application |

## When to use
- When extending the MCP ecosystem with a new application that LLMs can install and manage
- When packaging a CEX tool (like cex_doctor.py) as a discoverable MCP app
- When building agentic workflows that require autonomous app lifecycle management

## Builder
`archetypes/builders/mcp_app_extension-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind mcp_app_extension --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: mae_cex_doctor_app
kind: mcp_app_extension
pillar: P04
nucleus: n05
title: "CEX Doctor MCP App Extension"
version: 1.0
quality: null
---
app_name: "CEX Doctor"
install_command: "pip install cex-sdk"
launch_command: "python _tools/cex_doctor.py --mcp"
terminate_command: "pkill -f cex_doctor"
```

## Related kinds
- `mcp_server` (P04) -- MCP server that exposes tools the mcp_app_extension orchestrates
- `plugin` (P04) -- simpler plugin alternative that does not manage a full app lifecycle
- `hook_config` (P04) -- hook configuration that fires when mcp_app_extension lifecycle events occur
- `agent_name_service_record` (P04) -- ANS registration for the MCP app endpoint

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_mcp_app_extension]] | downstream | 0.47 |
| [[bld_schema_reranker_config]] | downstream | 0.41 |
| [[bld_schema_marketplace_app_manifest]] | downstream | 0.40 |
| [[bld_schema_app_directory_entry]] | downstream | 0.40 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.40 |
| [[bld_schema_voice_pipeline]] | downstream | 0.39 |
| [[bld_schema_search_strategy]] | downstream | 0.39 |
| [[bld_schema_thinking_config]] | downstream | 0.39 |
| [[bld_schema_benchmark_suite]] | downstream | 0.39 |
| [[bld_schema_dataset_card]] | downstream | 0.39 |
