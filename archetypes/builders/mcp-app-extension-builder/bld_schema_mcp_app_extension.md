---
kind: schema
id: bld_schema_mcp_app_extension
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for mcp_app_extension
quality: 9.1
title: "Schema MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for mcp_app_extension"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_rbac_policy
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_api_reference
  - bld_schema_search_strategy
---

## Frontmatter Fields
### Required
| Field        | Type   | Required | Default | Notes |
|--------------|--------|----------|---------|-------|
| id           | string | yes      |         | Matches ID pattern below |
| kind         | string | yes      |         | Must be `mcp_app_extension` |
| pillar       | string | yes      |         | P04 |
| title        | string | yes      |         |       |
| version      | string | yes      |         | SemVer |
| created      | date   | yes      |         |       |
| updated      | date   | yes      |         |       |
| author       | string | yes      |         |       |
| domain       | string | yes      |         | `mcp_app_extension construction` |
| quality      | null   | yes      | null    | Never self-score; peer review assigns |
| tags         | array  | yes      |         |       |
| tldr         | string | yes      |         |       |
| app_id       | string | yes      |         | Reverse-DNS or p04_mae slug |
| entry_url    | url    | yes      |         | HTTPS iframe URL |
| capabilities | array  | yes      |         | MCP tools/resources requested |
| permissions  | array  | yes      |         | Scoped permission grants |

### Recommended
| Field         | Type   | Notes |
|---------------|--------|-------|
| description   | string | Manifest summary |
| icon_url      | url    | HTTPS icon |
| homepage      | url    | Public site |
| spec_version  | string | SEP-1865 draft tag |

## ID Pattern
^p04_mae_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Overview** -- purpose of the MCP app extension and target client set.
2. **App Manifest** -- app_id, version, entry_url, icon, homepage.
3. **Capabilities** -- list of MCP tools and resources requested, citing SEP-1865.
4. **Permissions** -- scope list with justification per scope (Anthropic + OpenAI review expects this).
5. **Lifecycle** -- install, launch, terminate handlers with postMessage payload schemas.
6. **Sandbox Policy** -- iframe CSP, allowed origins, postMessage channel, forbidden APIs.

## Constraints
- All required fields must be present and valid.
- `id` must match the regex pattern exactly.
- `kind` must equal `mcp_app_extension`; never `mcp_server` or `browser_tool`.
- `entry_url` must use HTTPS and resolve to an iframe-loadable document.
- `capabilities` must reference MCP tools/resources declared by the backing mcp_server.
- `permissions` must be minimal and each must be justified inline.
- Must conform to SEP-1865 and MCP spec 2025-11-25.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.66 |
| [[bld_schema_quickstart_guide]] | sibling | 0.65 |
| [[bld_schema_reranker_config]] | sibling | 0.64 |
| [[bld_schema_sandbox_config]] | sibling | 0.63 |
| [[bld_schema_rbac_policy]] | sibling | 0.63 |
| [[bld_schema_pitch_deck]] | sibling | 0.63 |
| [[bld_schema_benchmark_suite]] | sibling | 0.62 |
| [[bld_schema_dataset_card]] | sibling | 0.62 |
| [[bld_schema_api_reference]] | sibling | 0.61 |
| [[bld_schema_search_strategy]] | sibling | 0.61 |
