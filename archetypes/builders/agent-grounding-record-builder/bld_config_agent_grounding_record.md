---
kind: config
id: bld_config_agent_grounding_record
pillar: P09
llm_function: CONSTRAIN
purpose: Naming convention, output paths, byte limits, and post-build hooks for agent_grounding_record artifacts
quality: 9.1
title: "Agent Grounding Record Builder -- Config"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, config]
tldr: "Naming: p10_gr_{{inference_id_prefix}}.md, Path: P10_memory/grounding/, Max: 4096 bytes, Hook: auto hash-verify"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_agent_grounding_record
  - bld_architecture_agent_grounding_record
  - bld_collaboration_agent_grounding_record
  - bld_output_template_agent_grounding_record
  - bld_quality_gate_agent_grounding_record
  - bld_knowledge_card_agent_grounding_record
  - bld_memory_agent_grounding_record
  - bld_config_webinar_script
  - bld_examples_agent_grounding_record
  - bld_manifest_agent_grounding_record
---
# Agent Grounding Record Builder -- Config

## Naming Convention

| Property           | Pattern                              | Example                            |
|--------------------|--------------------------------------|------------------------------------|
| File naming        | p10_gr_{{inference_id_prefix}}.md    | p10_gr_7f3a2c1b.md                 |
| Prefix source      | First 8 chars of inference_id UUID   | From 7f3a2c1b-e8d4-4f21-...        |
| Artifact ID (YAML) | p10_gr_{{inference_id_prefix}}       | id: p10_gr_7f3a2c1b                |
| Regex validation   | ^p10_gr_[a-z0-9_]+\.md$             | Enforced by Hard Gate H02          |
| Case               | Lowercase only                       | No uppercase in file name          |
| Separator          | Underscore (_)                       | No hyphens in the prefix part      |

### Naming Anti-Patterns (REJECTED by H02)

| Wrong Pattern                    | Reason Rejected                        |
|----------------------------------|----------------------------------------|
| p01_gr_7f3a2c1b.md               | Wrong pillar prefix (should be p10)    |
| p10_7f3a2c1b.md                  | Missing "gr" kind marker               |
| p10_gr_7F3A2C1B.md               | Uppercase in name                      |
| p10-gr-7f3a2c1b.md               | Hyphens not allowed in this pattern    |
| grounding_record_7f3a2c1b.md     | Missing pillar prefix entirely         |
| p10_gr_inference_7f3a2c1b.md     | Verbose -- use UUID prefix only        |
## Output Paths

| Context                         | Path                                          |
|---------------------------------|-----------------------------------------------|
| Primary output directory        | P10_memory/grounding/                         |
| Archive (after 30 days)         | P10_memory/grounding/archive/{{YYYY-MM}}/     |
| Compiled YAML mirror            | P10_memory/grounding/.compiled/               |
| Proposal files (concurrent)     | .cex/runtime/proposals/                       |
| Full trace log (overflow ref)   | P10_memory/grounding/traces/{{inference_id}}.json |
## Byte Limits

| Limit Type        | Value  | Enforcement               |
|-------------------|--------|---------------------------|
| Max artifact size | 4096 B | cex_compile.py --check-size |
| Warn threshold    | 3800 B | Builder self-check at F6  |
| Overflow strategy | Truncate tool_calls and rag_chunks to counts + representative hashes; add full_trace_log_ref pointer |

### Byte Budget Per Section (Target)

| Section               | Target Bytes | Hard Max |
|-----------------------|--------------|----------|
| Frontmatter           | 400          | 500      |
| Inference Identity    | 250          | 350      |
| Model block           | 200          | 300      |
| Tool Calls table      | 180 per row  | 220/row  |
| RAG Chunks table      | 170 per row  | 210/row  |
| Integrity block       | 150          | 200      |
| Audit Summary         | 300          | 500      |
| Total (3 tools, 5 chunks) | ~2650   | 4096     |
## Post-Build Hooks

### Hook 1: output-hash Verification (MANDATORY)

Runs automatically after F6 PRODUCE if output_hash was not provided by the caller.

```bash
# Verify or compute output_hash
python _tools/cex_compile.py P10_memory/grounding/p10_gr_{{prefix}}.md --verify-hash
```

Behavior:
- If output_hash is present: verify it is exactly 64 lowercase hex chars
- If output_hash is null: FAIL immediately -- do not proceed to F7
- If output_hash was auto-computed: log the computation method in the Audit Summary

### Hook 2: OTel Span Validation (RECOMMENDED)

```bash
# Check that otel_span_id is a valid 16-char hex W3C format
python _tools/cex_compile.py P10_memory/grounding/p10_gr_{{prefix}}.md --validate-span-id
```

### Hook 3: Compile and Size Check (MANDATORY)

```bash
python _tools/cex_compile.py P10_memory/grounding/p10_gr_{{prefix}}.md
```

Fails if:
- YAML frontmatter has parse errors
- Artifact exceeds 4096 bytes
- ID does not match naming regex

### Hook 4: Quality Score (MANDATORY before publish)

```bash
python _tools/cex_score.py --apply P10_memory/grounding/p10_gr_{{prefix}}.md
```

A score below 8.0 blocks publication. Score between 8.0 and 9.0 allowed with documented waiver.
## Runtime Flags

| Flag                    | Type    | Default  | Description                                                   |
|-------------------------|---------|----------|---------------------------------------------------------------|
| auto_compute_hash       | boolean | true     | If true, compute output_hash from raw_output when not provided|
| require_c2pa            | boolean | false    | If true, fail if c2pa_manifest_ref is null                   |
| require_model_signature | boolean | false    | If true, fail if model-signature is null                     |
| downstream_use_default  | string  | "test"   | Default when downstream_use not explicitly set               |
| archive_after_days      | integer | 30       | Move records to archive after this many days                 |
| max_tool_calls_inline   | integer | 10       | Truncate tool_calls table beyond this count                  |
| max_rag_chunks_inline   | integer | 20       | Truncate rag_chunks table beyond this count                  |

### Setting Flags

Flags are set in the grounding record builder section of the CEX config:

```yaml
# .cex/config/builder_config.yaml
agent_grounding_record:
  auto_compute_hash: true
  require_c2pa: false
  require_model_signature: false
  downstream_use_default: "test"
  archive_after_days: 30
  max_tool_calls_inline: 10
  max_rag_chunks_inline: 20
```
## Environment Requirements

| Requirement              | Value                   | Notes                                              |
|--------------------------|-------------------------|----------------------------------------------------|
| Python version           | >= 3.9                  | Required for SHA-256 hashlib functions             |
| OTel SDK                 | opentelemetry-api >= 1.37 | For span ID retrieval integration                |
| C2PA library             | c2pa-python (optional)  | Only required if require_c2pa: true               |
| Disk space per record    | ~8 KB                   | Includes MD source + compiled YAML + trace log    |
| Write permissions        | P10_memory/grounding/   | Builder must have write access to this directory  |
## Retention Policy

| Record Type              | Retention            | Archive Action                                       |
|--------------------------|----------------------|------------------------------------------------------|
| Production records       | 7 years              | Archive to P10_memory/grounding/archive/ after 30d  |
| Test records             | 90 days              | Delete after 90 days (no archive required)           |
| Eval records             | 1 year               | Archive after 30 days                                |
| Failed records (< H01)   | 7 days               | Auto-delete after investigation window               |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_agent_grounding_record]] | upstream | 0.42 |
| [[bld_architecture_agent_grounding_record]] | upstream | 0.33 |
| [[bld_collaboration_agent_grounding_record]] | downstream | 0.32 |
| [[bld_output_template_agent_grounding_record]] | upstream | 0.31 |
| [[bld_quality_gate_agent_grounding_record]] | downstream | 0.26 |
| [[bld_knowledge_card_agent_grounding_record]] | upstream | 0.26 |
| [[bld_memory_agent_grounding_record]] | downstream | 0.25 |
| [[bld_config_webinar_script]] | sibling | 0.25 |
| [[bld_examples_agent_grounding_record]] | upstream | 0.24 |
| [[bld_manifest_agent_grounding_record]] | downstream | 0.23 |
