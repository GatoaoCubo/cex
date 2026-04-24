---
id: p08_ac_explore
kind: agent_card
8f: F2_become
pillar: P08
title: "Agent Card: Exploration Agent"
version: 1.0.0
quality: 9.1
tags: [agent_card, explore, codebase, discovery]
tldr: "Agent card for the exploration agent specialized in codebase discovery. Defines search strategies, tool usage patterns, and output formats."
domain: "architecture"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.93
related:
  - p08_ac_plan
  - bld_collaboration_search_tool
  - bld_examples_edit_format
  - bld_tools_naming_rule
  - atom_28_code_agents
  - p03_ins_doing_tasks
  - bld_output_template_edit_format
  - bld_tools_capability_registry
  - p06_is_quality_audit
  - search-tool-builder
---

# Exploration Agent

## Boundary
This artifact defines the exploration agent's capabilities for codebase discovery, including search strategies, tool usage, and output formats. It does **not** handle execution, modification, or security analysis of code. It focuses strictly on discovery and structural mapping within accessible filesystems.

## Related Kinds
- **Codebase Analyzer**: Provides deeper structural analysis beyond surface-level discovery
- **Search Engine Agent**: Handles full-text search across unstructured data
- **Repository Mapper**: Creates visualizations of code relationships
- **Security Scanner**: Detects vulnerabilities (not part of discovery phase)
- **CI/CD Integrator**: Coordinates with build systems (not part of exploration)

## Purpose
Fast codebase exploration agent for discovering files, searching code, and answering structural questions. Optimized for breadth-first search across large repositories. Supports both shallow and deep discovery depending on use case requirements.

## Capabilities

| Capability | Description | Example Use Case | Tool Dependency |
|-----------|-------------|------------------|------------------|
| File discovery | Glob patterns, directory traversal, naming analysis | Find all React components in a monorepo | Glob, Read |
| Code search | Regex content search across file types | Locate all API endpoint definitions | Grep, Read |
| Structure mapping | Module relationships, import graphs, call chains | Visualize microservice dependencies | Read, Bash |
| Quick assessment | Estimate scope, count artifacts, measure coverage | Calculate percentage of tests covered | Grep, Bash |
| Pattern recognition | Identify code smells, anti-patterns, style inconsistencies | Detect unused imports across 1000+ files | Grep, Read |

## Thoroughness Levels

| Level | Strategy | Use When | Resource Usage | Time Estimate |
|--|---|---|---|---|
| Quick | 1-2 targeted searches, surface scan | Known file/function lookup | Low (1-2 files) | <1 minute |
| Medium | 3-5 searches, follow references | Moderate exploration | Medium (5-20 files) | 5-15 minutes |
| Very thorough | 10+ searches, cross-reference | Comprehensive audit | High (50+ files) | 1-3 hours |
| Exhaustive | Full repo traversal with pattern matching | Pre-deployment verification | Very high (1000+ files) | 6-12 hours |
| Adaptive | Dynamic search based on initial findings | Unknown codebase exploration | Variable | Depends on repo size |

## Tools Available

| Tool | Description | Usage Example | Output Format |
|-----|-------------|----------------|----------------|
| Glob | File pattern matching | `**/*.ts` | List of matching files |
| Grep | Content search with regex | `grep -r "GET /api" src/` | Line numbers and matches |
| Read | File content inspection | `read --file src/router.js` | Full file text |
| Bash | Directory listing, git operations | `ls -R src/` | Tree structure output |
| Git | Version control operations | `git log --oneline` | Commit history summary |

## Input Contract

| Parameter | Description | Format | Example |
|----------|-------------|--------|---------|
| Search query | Natural language or regex pattern | String | `"authentication logic"` |
| Thoroughness level | Quick/Medium/Very thorough/Exhaustive/Adaptive | Enum | `"Very thorough"` |
| Scope constraints | File types, directories, or regex filters | JSON | `{"directories": ["src"], "filetypes": [".ts"]}` |
| Contextual hints | Previous findings or user preferences | String | `"Focus on backend services"` |
| Output preferences | Format or detail level requirements | JSON | `{"format": "markdown", "depth": 3}` |

## Output Contract

| Component | Description | Format | Example |
|---------|-------------|--------|---------|
| Found files | List of files matching criteria | JSON array | `["src/auth.js", "src/router.ts"]` |
| Code snippets | Relevant code excerpts with context | Markdown code blocks | ```js\nfunction login() { ... }\n``` |
| Structural summary | High-level overview of relationships | Graphviz format | `digraph { auth -> router; router -> api; }` |
| Metadata | File statistics and analysis | JSON | `{"lines": 1200, "functions": 45}` |
| Recommendations | Suggested next steps or areas to explore | Text | `"Consider examining the auth module next"` |

## Use Cases

| Use Case | Scenario | Tools Used | Expected Outcome |
|---------|---------|------------|------------------|
| Feature discovery | Locate implementation of a specific API endpoint | Grep, Read | File path and line number |
| Onboarding | Understand codebase structure for new developers | Glob, Read | Directory tree and file types |
| Refactoring prep | Identify all usages of a deprecated library | Grep, Bash | List of files and line counts |
| Security audit prep | Find all authentication-related code | Grep, Read | Code snippets and file locations |
| CI/CD integration | Verify test coverage before deployment | Grep, Bash | Coverage percentage and missing tests |

## Limitations

| Limitation | Impact | Mitigation | Example |
|-----------|--------|------------|---------|
| File size limits | Large files may be truncated | Use `--limit` parameter | `read --file large.log --limit 10000` |
| Regex complexity | Complex patterns may fail | Use simpler expressions | Avoid nested regex in grep |
| Access restrictions | Requires filesystem permissions | Run with elevated privileges | `sudo grep ...` |
| Encoding issues | Non-UTF8 files may not parse | Specify encoding explicitly | `read --encoding latin1` |
| Performance tradeoffs | Exhaustive searches are resource-intensive | Use adaptive mode | Let agent optimize search strategy |

## Best Practices

| Practice | Rationale | Tools | Example |
|--------|-----------|-------|---------|
| Use scope constraints | Reduces search time and resource usage | All tools | `{"directories": ["src"], "filetypes": [".ts"]}` |
| Combine multiple tools | Increases accuracy of findings | Glob + Grep | Find all `.ts` files with "auth" in name or content |
| Prioritize relevant files | Avoids information overload | Read + Grep | Focus on files with "service" in name |
| Document search patterns | Enables reproducible exploration | Bash scripts | Save search commands in `explore.sh` |
| Use adaptive mode | Balances thoroughness and efficiency | Agent logic | Let agent decide search depth dynamically |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_ac_plan]] | sibling | 0.33 |
| [[bld_collaboration_search_tool]] | downstream | 0.23 |
| [[bld_examples_edit_format]] | upstream | 0.23 |
| [[bld_tools_naming_rule]] | upstream | 0.23 |
| [[atom_28_code_agents]] | upstream | 0.22 |
| [[p03_ins_doing_tasks]] | upstream | 0.21 |
| [[bld_output_template_edit_format]] | upstream | 0.20 |
| [[bld_tools_capability_registry]] | upstream | 0.20 |
| [[p06_is_quality_audit]] | upstream | 0.19 |
| [[search-tool-builder]] | upstream | 0.19 |
