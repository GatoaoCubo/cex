---
kind: config
id: bld_config_compression_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: compression_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_cc_{{name}}.yaml` | `p10_cc_aggressive.yaml` |
| Builder directory | kebab-case | `compression-config-builder/` |
| Frontmatter fields | snake_case | `trigger_ratio`, `preserve_types` |
| Strategy names | snake_case, lowercase | `rolling_window`, `priority_keep` |
| Preset names | snake_case, lowercase, descriptive | `aggressive`, `conservative`, `balanced` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P10_memory/examples/p10_cc_{{name}}.yaml`
- Compiled: `cex/P10_memory/compiled/p10_cc_{{name}}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80 (no filler)
## Strategy Enum
| Value | When to use |
|-------|-------------|
| summarize | Semantic compression — LLM summarizes older messages into a condensed block |
| truncate_oldest | Positional — drop oldest messages first, keep newest |
| rolling_window | Sliding window — keep last N messages or N tokens |
| priority_keep | Weighted — each message type has a priority; compress lowest first |
| tiered | Multi-stage — execute compression stages in order until target ratio is met |
## Trigger Ratio Conventions
| Range | Label | When to use |
|-------|-------|-------------|
| 0.90-0.99 | aggressive | Compress early — maximize headroom for long tasks |
| 0.80-0.89 | balanced | Default — good trade-off between context and headroom |
| 0.50-0.79 | conservative | Compress late — preserve maximum context at cost of headroom |
| < 0.50 | INVALID | Never trigger below 50% — wastes compute, loses information |
