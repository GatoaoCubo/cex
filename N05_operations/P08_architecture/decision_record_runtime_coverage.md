---
id: decision_record_runtime_coverage
kind: decision_record
8f: F4_reason
pillar: P08
nucleus: n05
version: 1.0.0
date: 2026-04-18
status: accepted
quality: 8.0
tags: [runtime, multi-runtime, coverage, gaps, claude, codex, gemini, ollama]
related:
  - bld_schema_nucleus_def
  - bld_schema_bugloop
  - bld_schema_quickstart_guide
  - bld_schema_context_window_config
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_knowledge_card_vision_tool
  - bld_schema_spawn_config
  - bld_schema_pitch_deck
  - smoke_test_gemini_20260415
density_score: 1.0
updated: "2026-04-22"
---

# Decision Record: Multi-Runtime Coverage Matrix

## Context

CEX supports 4 runtimes: Claude Code, Codex CLI, Gemini CLI, and Ollama (via direct API).
Each runtime has different capabilities, tool access, and operational constraints.
This record documents what works where and what gaps exist.

## Decision

Maintain Claude Code as primary runtime (full capability). Support Codex/Gemini/Ollama
for cost optimization and redundancy, accepting documented capability gaps.

## Runtime Capability Matrix

| Capability | Claude Code | Codex CLI | Gemini CLI | Ollama API |
|------------|:-----------:|:---------:|:----------:|:----------:|
| 8F pipeline execution | FULL | FULL | FULL | FULL |
| Sub-agent spawn | YES (5 parallel) | NO | NO | NO |
| MCP server access | YES | NO | NO | NO |
| Git auto-commit | YES | NO | YES | NO |
| Signal auto-emit | YES | YES (via hook) | YES (via wrapper) | NO |
| Interactive GDP | YES | NO | NO | NO |
| Worktree isolation | YES | YES | NO | NO |
| Context window | 1M tokens | 200K | 1M | model-dependent |
| Tool use (native) | YES | YES | YES | NO (prompt-only) |
| Hook system | YES (settings.json) | YES (env script) | YES (env script) | NO |
| Browser/Playwright | YES (MCP) | NO | NO | NO |
| File read/write | YES | YES | YES | prompt-only |
| Bash execution | YES | YES (sandboxed) | YES | NO |

## Runtime-Specific Constraints

### Claude Code (primary)
- Full capability baseline
- Max subscription: Anthropic Max (Opus 4.6, 1M context)
- Rate limits: ~32 concurrent Sonnet, ~5 concurrent Opus
- All hooks, MCP, sub-agents available

### Codex CLI
- Writes files but does NOT auto-commit (N07 must verify + commit)
- No --model flag (uses default)
- Sandbox prevents some file system operations
- No MCP server support
- Exit without signal if task file missing

### Gemini CLI
- Free tier: aggressive RPM limits, hangs on "Thinking..." for 25+ min
- No gemini.exe binary -- runs as node.exe (orphan cleanup targets node by parent)
- flash-lite model ignores .gitignore (generates in ignored dirs)
- Auto-signals on exit via boot wrapper
- Separate quota pools: gemini-2.5-pro vs gemini-2.5-flash

### Ollama (local)
- Zero cost, full privacy
- No native tool use -- all via prompt engineering
- Fabricates KC evidence (hallucination risk on sourced claims)
- Best models: llama3.1:8b (agentic), gemma2:9b (structural)
- qwen3:14b wins N03+N04 but thinking-budget causes failures elsewhere
- No hooks, no signals, no git -- all external orchestration

## Known Gaps

| Gap | Affected Runtime | Severity | Mitigation |
|-----|-----------------|----------|------------|
| No auto-commit | Codex, Ollama | HIGH | N07 verifies + commits post-dispatch |
| No sub-agents | Codex, Gemini, Ollama | MEDIUM | Sequential execution only |
| No MCP | Codex, Gemini, Ollama | LOW | Direct tool calls replace MCP |
| Ollama hallucination | Ollama | HIGH | Verify all claims; structural-only tasks |
| Gemini free tier hang | Gemini | HIGH | Skip until paid tier or use flash model |
| No interactive GDP | Codex, Gemini, Ollama | MEDIUM | Pre-resolve all decisions in manifest |

## Boot Config Implications

- boot_config builders should document all 4 runtimes, not just Claude+Codex
- Fallback chains in nucleus_models.yaml: Claude -> Gemini -> Ollama
- cex_router_v2.py handles per-task routing based on capability requirements
- Grid dispatch: prefer Claude for complex tasks, Ollama for bulk structural

## Consequences

- All handoffs must be runtime-agnostic (no Claude-specific tool assumptions)
- Skills mirrored to .cex/skills/ for non-Claude runtimes
- Signal emission handled by boot wrappers, not the runtime itself
- N07 consolidation must always verify deliverables, not trust signals alone

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_nucleus_def]] | upstream | 0.40 |
| [[bld_schema_bugloop]] | downstream | 0.38 |
| [[bld_schema_quickstart_guide]] | upstream | 0.36 |
| [[bld_schema_context_window_config]] | upstream | 0.36 |
| [[bld_schema_reranker_config]] | upstream | 0.35 |
| [[bld_schema_usage_report]] | upstream | 0.35 |
| [[bld_knowledge_card_vision_tool]] | upstream | 0.35 |
| [[bld_schema_spawn_config]] | upstream | 0.34 |
| [[bld_schema_pitch_deck]] | upstream | 0.34 |
| [[smoke_test_gemini_20260415]] | upstream | 0.34 |
