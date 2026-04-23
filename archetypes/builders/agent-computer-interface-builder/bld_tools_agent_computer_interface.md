---
kind: tools
id: bld_tools_agent_computer_interface
pillar: P04
llm_function: CALL
quality: 9.0
title: "Tools Agent Computer Interface"
version: "1.0.0"
author: n05_builder
tags: [agent_computer_interface, tools, P04, builder]
tldr: "Tools and integrations for agent-computer-interface-builder: retriever, doctor, compiler, validator."
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_knowledge_card_agent_computer_interface
  - bld_tools_model_architecture
  - bld_tools_training_method
  - bld_architecture_agent_computer_interface
  - bld_output_template_agent_computer_interface
  - p11_qg_knowledge
  - bld_examples_agent_computer_interface
  - bld_collaboration_agent_computer_interface
  - hybrid_review3_n01
  - validate
---

# Tools: agent-computer-interface-builder

## Build-Time Tools
| Tool | Command | When to Use |
|------|---------|------------|
| Retriever | `python _tools/cex_retriever.py agent_computer_interface` | Find similar ACI artifacts |
| Doctor | `python _tools/cex_doctor.py` | Verify builder completeness (13 ISOs) |
| Compiler | `python _tools/cex_compile.py {path}` | Compile artifact after save |
| Hooks | `python _tools/cex_hooks.py validate {path}` | Validate frontmatter before commit |
| Score | `python _tools/cex_score.py --apply {path}` | Request quality score (peer review) |

## Validation Tools
| Tool | Command | Purpose |
|------|---------|---------|
| Schema check | `python _tools/cex_hooks.py pre-save {path}` | Validate required fields |
| Size check | `wc -c {path}` | Verify <= 4096 bytes (body) |
| ASCII check | `python _tools/cex_sanitize.py --check {path}` | Verify ASCII-only in code sections |
| Density check | `python _tools/cex_score.py --density {path}` | Verify >= 0.85 density |

## Discovery Tools
| Tool | Query Pattern | Purpose |
|------|--------------|---------|
| Retriever | `agent_computer_interface action_space` | Find existing ACI specs |
| Retriever | `tool_use observation_space` | Find observation/action patterns |
| Query | `python _tools/cex_query.py agent_computer_interface` | Discover related builders |

## Integration Points
| System | How | Purpose |
|--------|-----|---------|
| agent | ACI -> agent | ACI defines computer interface for agent to use |
| cli_tool | ACI uses cli_tool | Terminal commands exposed via ACI |
| browser_tool | ACI uses browser_tool | Web browsing exposed via ACI |
| mcp_server | ACI uses mcp_server | MCP tools exposed via ACI action space |
| computer_use | ACI extends computer_use | GUI-level computer control |

## Action Space Definitions
| Interface Type | Action Examples | Observation Type |
|---------------|----------------|-----------------|
| terminal | bash_exec, file_read, file_write | stdout, stderr, exit_code |
| browser | navigate, click, type, screenshot | page_content, screenshot |
| GUI | mouse_move, click, key_press | screenshot, accessibility_tree |
| API | http_get, http_post, http_put | response_body, status_code |
| file_system | read, write, list, delete | file_content, directory_listing |
| code_execution | run_python, run_js, run_bash | output, errors, artifacts |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_agent_computer_interface]] | upstream | 0.50 |
| [[bld_tools_model_architecture]] | sibling | 0.39 |
| [[bld_tools_training_method]] | sibling | 0.36 |
| [[bld_architecture_agent_computer_interface]] | downstream | 0.30 |
| [[bld_output_template_agent_computer_interface]] | downstream | 0.29 |
| [[p11_qg_knowledge]] | downstream | 0.28 |
| [[bld_examples_agent_computer_interface]] | downstream | 0.27 |
| [[bld_collaboration_agent_computer_interface]] | downstream | 0.26 |
| [[hybrid_review3_n01]] | upstream | 0.26 |
| [[validate]] | downstream | 0.25 |
