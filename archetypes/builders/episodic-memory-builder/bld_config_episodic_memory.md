---
kind: config
id: bld_config_episodic_memory
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, size limits for episodic_memory production
effort: medium
max_turns: 20
quality: null
title: "Config Episodic Memory"
version: "1.0.0"
author: n03_builder
tags: [episodic_memory, builder, config]
tldr: "Naming, paths, size limits, and enum constraints for episodic_memory production."
domain: "episodic memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---
# Config: episodic_memory Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_ep_{scope}.md` | `p10_ep_n07_orchestration.md` |
| Builder directory | kebab-case | `episodic-memory-builder/` |
| Frontmatter fields | snake_case | `episode_schema`, `retrieval_method`, `decay_policy` |
| Store slug | snake_case, lowercase | `n07_orchestration`, `n01_research` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `N0x_{domain}/P10_memory/p10_ep_{scope}.md`
- Compiled: `N0x_{domain}/P10_memory/compiled/p10_ep_{scope}.yaml`

## Size Limits
- Body: max 4096 bytes
- Density: >= 0.80

## Retrieval Method Enum
| Value | Mechanism |
|-------|-----------|
| recency | Most recent N episodes |
| relevance | Embedding similarity search |
| hybrid | Recency score + relevance score fusion |

## Decay Policy Methods
| Method | When to use |
|--------|-------------|
| time | Age-based: purge after N days |
| count | Size-based: remove oldest when > max |
| relevance | Utility-based: remove never-retrieved episodes |
| hybrid | Time + relevance combined |

## Episode Count Guidelines
| Agent Type | Recommended Count |
|-----------|------------------|
| Single-task agent | 50-100 |
| Multi-domain agent | 100-500 |
| Long-running orchestrator | 200-1000 |
| Never | unlimited (null) |
