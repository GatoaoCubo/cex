---
kind: config
id: bld_config_fallback_chain
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: fallback_chain Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_fc_{slug}.md` | `p02_fc_research_model.md` |
| Builder directory | kebab-case | `fallback-chain-builder/` |
| Frontmatter fields | snake_case | `steps_count`, `timeout_per_step_ms` |
| FC slug | snake_case, lowercase | `research_model`, `api_gateway` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P02_model/examples/p02_fc_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_fc_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5800 bytes
- Density: >= 0.80

## Provider Enum

| Value | Models | Notes |
|-------|--------|-------|
| anthropic | claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5 | Primary CEX provider |
| openai | gpt-4.1, gpt-4.1-mini, gpt-4.1-nano | Alternative provider |
| google | gemini-2.5-pro, gemini-2.5-flash | Google models |
| local | ollama/codexaft:v3, ollama/nomic-embed-text | Self-hosted models |

## Degradation Order Guidelines

| Tier | Capability | Cost | Latency | Example |
|------|-----------|------|---------|---------|
| 1 (primary) | Highest | Highest | Slowest | opus-4-6, gpt-4.1 |
| 2 (degraded) | Medium | Medium | Medium | sonnet-4-6, gpt-4.1-mini |
| 3 (minimum) | Lowest | Lowest | Fastest | haiku-4-5, gpt-4.1-nano |

## Timeout Guidelines

| Task type | Recommended timeout | Rationale |
|-----------|-------------------|-----------|
| Simple (classification) | 5000-10000 ms | Fast response expected |
| Medium (generation) | 15000-30000 ms | Standard LLM generation |
| Complex (research) | 30000-60000 ms | Multi-step reasoning |
| Batch (non-interactive) | 60000-120000 ms | Latency not critical |
