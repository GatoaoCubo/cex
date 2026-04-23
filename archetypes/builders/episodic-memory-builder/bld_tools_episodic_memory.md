---
quality: 8.0
quality: 7.6
kind: tools
id: bld_tools_episodic_memory
pillar: P04
llm_function: CALL
purpose: Tools for episodic_memory production
title: "Tools Episodic Memory"
version: "1.0.0"
author: n03_builder
tags: [episodic_memory, builder, tools]
tldr: "Tools for episodic_memory: discovery, scoring, compilation, retrieval platform reference."
domain: "episodic memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_tools_memory_scope
  - bld_tools_hitl_config
  - bld_tools_quality_gate
  - bld_tools_citation
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_tools_streaming_config
  - bld_tools_mcp_server
  - bld_tools_kind
  - bld_tools_experiment_config
---

# Tools: episodic-memory-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Find existing episodic_memory artifacts | Phase 1 | CONDITIONAL |
| cex_retriever.py | Semantic search for similar stores | Phase 1 | AVAILABLE |
| cex_score.py | Score artifact quality | Phase 3 | AVAILABLE |
| cex_compile.py | Compile .md to .yaml | Phase 3 | AVAILABLE |

## External Reference
| Platform | Purpose |
|----------|---------|
| MemGPT (letta.ai) | In-context + external episodic memory management |
| Zep (getzep.com) | Server-side temporal episode store with NLP extraction |
| Mem0 (mem0.ai) | Hybrid entity + episode memory with graph links |
| LangChain | ConversationSummaryBufferMemory for episode summarization |

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | |

## Validation
id `^p10_ep_`, episode_schema >= 3 fields + timestamp, retrieval_method in enum,
episode_count numeric, decay_policy declared, quality == null, body <= 4096 bytes.

## Tool Integration Checklist

- Verify tool name follows snake_case convention
- Validate input/output schema matches interface contract
- Cross-reference with capability_registry for discoverability
- Test tool invocation in sandbox before production use

## Invocation Pattern

```yaml
# Tool invocation contract
name: tool_name
input_schema: validated
output_schema: validated
error_handling: defined
timeout: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_scope]] | sibling | 0.42 |
| [[bld_tools_hitl_config]] | sibling | 0.40 |
| [[bld_tools_quality_gate]] | sibling | 0.40 |
| [[bld_tools_citation]] | sibling | 0.39 |
| [[bld_tools_cli_tool]] | sibling | 0.39 |
| [[bld_tools_retriever_config]] | sibling | 0.38 |
| [[bld_tools_streaming_config]] | sibling | 0.38 |
| [[bld_tools_mcp_server]] | sibling | 0.38 |
| [[bld_tools_kind]] | sibling | 0.37 |
| [[bld_tools_experiment_config]] | sibling | 0.37 |
