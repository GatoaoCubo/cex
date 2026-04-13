#!/usr/bin/env python3
"""One-shot script to create 8 sub-agent files for new builders."""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent

kinds = {
    "batch_config": {
        "pillar": "P09", "llm_fn": "CALL", "max_bytes": 2048,
        "naming": "p09_bc_{{name}}.yaml",
        "desc": "Async batch processing config for bulk API operations",
        "boundary": "Batch processing configuration for async API calls. NOT a schedule (P12) nor a queue.",
    },
    "cost_budget": {
        "pillar": "P09", "llm_fn": "GOVERN", "max_bytes": 3072,
        "naming": "p09_cb_{{name}}.yaml",
        "desc": "Token budget allocation, spend tracking, cost alerts per provider/model",
        "boundary": "Cost and token budget tracking. NOT a rate_limit_config (P09) nor a billing system.",
    },
    "experiment_config": {
        "pillar": "P09", "llm_fn": "GOVERN", "max_bytes": 4096,
        "naming": "p09_ec_{{name}}.yaml",
        "desc": "A/B test and prompt experiment configuration with variants and metrics",
        "boundary": "Experiment and A/B test config. NOT an eval_dataset (P07) nor a benchmark (P07).",
    },
    "finetune_config": {
        "pillar": "P02", "llm_fn": "CONSTRAIN", "max_bytes": 4096,
        "naming": "p02_ft_{{name}}.yaml",
        "desc": "Fine-tuning job configuration: dataset, base model, adapter type, hyperparameters",
        "boundary": "Fine-tuning job spec. NOT a model_provider (P02) nor a model_card (P02).",
    },
    "hitl_config": {
        "pillar": "P11", "llm_fn": "GOVERN", "max_bytes": 3072,
        "naming": "p11_hitl_{{name}}.yaml",
        "desc": "Human-in-the-loop approval flow: review triggers, escalation rules",
        "boundary": "HITL approval flows. NOT a guardrail (P11) nor a quality_gate (P11).",
    },
    "knowledge_graph": {
        "pillar": "P01", "llm_fn": "INJECT", "max_bytes": 8192,
        "naming": "p01_kg_{{name}}.md",
        "desc": "Graph-based knowledge schema with entity types and relation types",
        "boundary": "Knowledge graph schema. NOT a knowledge_card (P01) nor an ontology (P01).",
    },
    "ontology": {
        "pillar": "P01", "llm_fn": "CONSTRAIN", "max_bytes": 8192,
        "naming": "p01_ont_{{name}}.md",
        "desc": "Formal taxonomy and ontology definitions (OWL, SKOS patterns)",
        "boundary": "Formal ontology/taxonomy. NOT a knowledge_graph (P01) nor a glossary_entry (P01).",
    },
    "streaming_config": {
        "pillar": "P05", "llm_fn": "PRODUCE", "max_bytes": 2048,
        "naming": "p05_sc_{{name}}.yaml",
        "desc": "SSE, WebSocket, and chunked response streaming configuration",
        "boundary": "Streaming protocol config. NOT a response_format (P05) nor a webhook (P04).",
    },
}

TEMPLATE = """---
name: {agent_name}
description: "Builds ONE {kind} artifact via 8F pipeline. Loads {agent_name} ISOs. Produces draft with frontmatter + body. Never self-scores quality."
model: sonnet
tools: Read, Write, Edit, Bash, Glob, Grep
quality: null
title: "{title}"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, {kind}, {pillar}]
tldr: "Specialized builder for {kind} artifacts ({short_desc})."
domain: "CEX system"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# {agent_name} Sub-Agent

You are a specialized builder for **{kind}** artifacts (pillar: {pillar}).

## Kind Definition

| Field | Value |
|-------|-------|
| Kind | `{kind}` |
| Pillar | `{pillar}` |
| LLM Function | `{llm_fn}` |
| Max Bytes | {max_bytes} |
| Naming | `{naming}` |
| Description | {desc} |
| Boundary | {boundary} |

## How You Work

1. You receive a **target name/topic** for the artifact
2. You load builder ISOs from `archetypes/builders/{agent_name}/`
3. You read these ISOs in order:
   - `bld_manifest_{kind}.md` -- MANIFEST (builder identity + metadata)
   - `bld_schema_{kind}.md` -- CONSTRAINTS (what fields, what format)
   - `bld_system_prompt_{kind}.md` -- IDENTITY (who you become)
   - `bld_instruction_{kind}.md` -- PROCESS (research > compose > validate)
   - `bld_output_template_{kind}.md` -- TEMPLATE (the shape to fill)
   - `bld_examples_{kind}.md` -- EXAMPLES (what good looks like)
   - `bld_memory_{kind}.md` -- PATTERNS (learned from past builds)
   - `bld_tools_{kind}.md` -- TOOLS (available tools + usage)
   - `bld_quality_gate_{kind}.md` -- QUALITY (scoring rubric + gates)
   - `bld_knowledge_card_{kind}.md` -- KNOWLEDGE (domain KC for this kind)
   - `bld_architecture_{kind}.md` -- ARCHITECTURE (structural patterns)
   - `bld_collaboration_{kind}.md` -- COLLABORATION (how to work with other builders)
   - `bld_config_{kind}.md` -- CONFIG (runtime configuration)
4. You produce the artifact following the template
5. You compile: `python _tools/cex_compile.py {{path}}`

## Rules

1. `quality: null` ALWAYS -- never self-score
2. Frontmatter MUST parse as valid YAML
3. Body MUST stay under {max_bytes} bytes
4. Follow naming pattern: `{naming}`
5. Read existing file first if it exists -- rebuild, don't start from zero
6. ONE artifact per invocation -- stay focused

## 8F Trace (show this for every build)

```
F1 CONSTRAIN: kind={kind}, pillar={pillar}
F2 BECOME: {agent_name} ISOs loaded
F3 INJECT: schema + examples + memory loaded
F4 REASON: plan decided
F5 CALL: tools ready (Read, Write, compile)
F6 PRODUCE: artifact written to {{path}}
F7 GOVERN: gates checked (quality: null)
F8 COLLABORATE: compiled to YAML
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `{kind}` |
| Pillar | {pillar} |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
"""

for kind, meta in kinds.items():
    slug = kind.replace("_", "-")
    agent_name = f"{slug}-builder"
    agent_path = CEX_ROOT / ".claude" / "agents" / f"{agent_name}.md"

    content = TEMPLATE.format(
        agent_name=agent_name,
        kind=kind,
        title=agent_name.replace("-", " ").title(),
        pillar=meta["pillar"],
        llm_fn=meta["llm_fn"],
        max_bytes=meta["max_bytes"],
        naming=meta["naming"],
        desc=meta["desc"],
        short_desc=meta["desc"][:60],
        boundary=meta["boundary"],
    )

    agent_path.write_text(content, encoding="utf-8")
    print(f"  Created: .claude/agents/{agent_name}.md")

print(f"Done: 8 sub-agents wired")
