---
id: spec_n07_bootstrap_context
kind: context_doc
title: CEX Architecture -- Theory vs Practice Gap Analysis
version: 1.0.0
quality: 8.9
created: 2026-04-07
purpose: Give a fresh N07 instance full understanding of what was designed vs what exists
density_score: 1.0
---

# CEX Architecture: Theory vs Practice

## What CEX Is

| Attribute | Value |
|-----------|-------|
| Purpose | Universal categorized dictionary for LLMs |
| Format | Structured artifacts (.md with YAML frontmatter) |
| Language | LLM-to-LLM (tables, lists, code blocks -- zero prose filler) |
| Test | Would Llama-7B understand this term without explanation? |
| Value | Context does the work, not the model's intelligence |

## Structural Layers

### Base Layer (read-only molds)

| Component | Path | Count | Purpose |
|-----------|------|-------|---------|
| Pillar schemas | P{01-12}_*/_schema.yaml | 12 | Structure contracts per category |
| Builder archetypes | archetypes/builders/{kind}-builder/ | 121 | 13 components per kind (instruction, examples, quality gate, output template, schema, etc) |
| Knowledge library | P01_knowledge/library/ | 270+ KCs | Domain knowledge in structured form |
| Templates | P{01-12}_*/templates/tpl_*.md | 67+ | Output patterns with {{variable}} slots |
| Kind registry | .cex/kinds_meta.json | 117 kinds | Every artifact type CEX understands |
| Rules | .claude/rules/*.md | 13 | Behavioral constraints |

### Instance Layer (filled per agent)

| Component | Path | Count per nucleus | Purpose |
|-----------|------|-------------------|---------|
| Nucleus directory | N{01-06}_*/ | ~40 artifacts | Domain-specific filled molds |
| Subdirectories | agents/, prompts/, knowledge/, schemas/, output/, orchestration/, quality/, ... | 9-14 subdirs | Mirrors 12 pillar categories |
| Agent card manifest | N{0X}_*/agent_card_n0X.md | 1 | Self-discovery: what this agent has |

### Runtime Layer (assembled per task)

| Component | Path | Purpose |
|-----------|------|---------|
| Handoffs | .cex/runtime/handoffs/ | Task + artifact references |
| Decisions | .cex/runtime/decisions/ | User preferences (GDP) |
| Signals | .cex/runtime/signals/ | Completion signals |
| Plans | .cex/runtime/plans/ | Mission decomposition |
| PIDs | .cex/runtime/pids/ | Process tracking |

## Context Assembly (the theory)

### Phase 1: Boot (agent self-assembles)

When a nucleus starts, it should ALREADY know its capabilities:

| What loads | How | Status |
|-----------|-----|--------|
| CLAUDE.md | pi reads automatically on startup | WIRED |
| agent_card_n0X.md | --append-system-prompt in boot .cmd | WIRED (Apr 7) |
| .claude/rules/n0X*.md | pi reads automatically | WIRED |
| Sin identity | --append-system-prompt in boot .cmd | WIRED |
| Pi skills (/build, /mission, /status) | cex-pi-package installed | WIRED |

### Phase 2: Task (orchestrator assembles)

When N07 dispatches, the handoff should include everything the nucleus needs:

| What to include | How | Status |
|----------------|-----|--------|
| Task description | Handoff .md | WIRED |
| Builder path (13 components) | ## Relevant artifacts section | RULE EXISTS (dispatch-depth.md), NOT ENFORCED IN CODE |
| Relevant KCs | Listed in handoff | RULE EXISTS, NOT ENFORCED IN CODE |
| Output template | Listed in handoff | RULE EXISTS, NOT ENFORCED IN CODE |
| Brand config | Auto-loaded if /init was run | WIRED (brand_inject.py) |
| Decision manifest | Auto-included if GDP ran | WIRED (spawn_solo.ps1) |

### Phase 3: Pipeline (8F execution)

During task execution, the 8F pipeline enriches further:

| Step | What happens | Status |
|------|-------------|--------|
| F1 CONSTRAIN | Resolve kind, pillar from intent | WIRED (cex_8f_runner.py) |
| F2 BECOME | Load builder 13 components | WIRED (cex_skill_loader.py) |
| F3 INJECT | Assemble KCs + examples + memory + brand | CODE EXISTS but BROKEN -- needs LLM subprocess, should be pure Python |
| F4 REASON | Plan approach | WIRED |
| F5 CALL | Tool enrichment (retriever, query, providers) | WIRED |
| F6 PRODUCE | Generate with all context | WIRED (but depends on F3 working) |
| F7 GOVERN | Quality gate check | WIRED |
| F8 COLLABORATE | Save, compile, commit, signal | WIRED |

## Gaps Between Theory and Practice

### GAP G3: 37% of artifacts are prose-heavy

| Metric | Value |
|--------|-------|
| Total artifacts | 3562 |
| Prose-heavy (more prose than structured data) | 1302 (37%) |
| Target | < 20% |
| Fix | Overnight evolve sweep: prose -> tables |
| Tool | cex_evolve.py sweep --target 9.0 |

### GAP G4: F3 INJECT is broken

| Metric | Value |
|--------|-------|
| Current F3 | Calls execute_prompt() which needs LLM subprocess |
| Problem | execute_prompt() can't reach LLM (no API key, nested pi fails) |
| Fix | Refactor F3 to use Python code only: cex_retriever + cex_prompt_layers |
| Impact | Pipeline works on ANY model, even offline/free |
| File | _tools/cex_8f_runner.py (1385 lines, F3 at ~line 200) |

### GAP G5: Template variables not systematic

| Metric | Value |
|--------|-------|
| Builder files with {{variables}} | 320 |
| Template files with {{variables}} | 67 |
| Templates WITHOUT {{BRAND_*}} slots | Unknown -- needs audit |
| Fix | Audit all bld_output_template_*.md, add missing {{BRAND_*}} and contextual slots |

### GAP G6: 6+ stale docs from March 30

| Doc | Status | Problem |
|-----|--------|---------|
| ROADMAP_CONSOLIDATED.md | STALE | Says 70 builders (now 121), 8F theoretical (now implemented) |
| ARCHITECTURE.md | STALE | Wrong counts, no pi runtime |
| HIERARCHY.md | STALE | Fractal structure changed |
| QUICKSTART.md | STALE | References claude not pi |
| NAMING_CONVENTION.md | STALE | Convention updated |
| ONBOARDING.md | STALE | Runtime changed |
| PATTERN_NUCLEUS_BOOT.md | STALE | Boot pattern completely different now |

### GAP G7: Handoff artifact selection not automated

| Metric | Value |
|--------|-------|
| Theory | N07 selects relevant builders, KCs, templates per task |
| Practice | N07 writes text descriptions, nucleus discovers on its own |
| Fix | Build a handoff composer that reads kinds_meta.json, finds builder path, finds KC, lists in handoff |
| Impact | Nucleus starts producing on turn 1 instead of spending 5 turns discovering files |

### GAP G8: Nucleus doesn't self-select context during task

| Metric | Value |
|--------|-------|
| Theory | Nucleus reads handoff references + autonomously pulls more relevant artifacts |
| Practice | Nucleus follows handoff literally, doesn't explore library |
| Fix | Nucleus boot prompt should instruct: "After reading handoff, scan P01_knowledge/library/ for relevant KCs before producing" |
| Impact | Richer context = better output |

## Runtime Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| N07 runtime | pi (this process) | Orchestration, dispatch, monitoring |
| N01-N06 runtime | pi (spawned via CMD) | Nucleus execution |
| Themes | cex-pi-package (7 themes) | Visual identity per nucleus |
| Skills | cex-pi-package (/build, /mission, /status) | CEX commands in pi |
| Extension | cex-nucleus-ui.ts | Custom footer with identity + context bar |
| Process management | _spawn/*.ps1 | Spawn, monitor, kill, grid layout |
| Quality | _tools/cex_doctor.py + cex_flywheel_audit.py | Health checks |
| Evolution | _tools/cex_evolve.py + boot/overnight_h1.cmd | Autonomous improvement |

## Spec Reference

| Spec | Path | What it defines |
|------|------|----------------|
| Context assembly | _docs/specs/spec_context_assembly.md | Two-phase loading, fractal structure |
| NotebookLM pipeline | _docs/specs/spec_notebooklm_pipeline.md | KC -> human content |
| Content factory | _docs/specs/spec_content_factory_v1.md | Multi-format content production |
| AutoResearch | _docs/specs/spec_autoresearch_assimilation.md | Karpathy pattern for CEX |

## Memory (N07 persistent across sessions)

| File | Purpose |
|------|---------|
| cex_core_purpose.md | INVIOLABLE: universal taxonomy, zero jargon, LLM-to-LLM |
| roadmap_cex.md | 3 horizons, 10 principles, current state |
| operational_lessons.md | 7 hard-learned lessons (permanent) |
| cex_game_architecture.md | Internal metaphor (NOT taxonomy) |
| project_cex_product_context.md | CEX ships as blank brain |
| project_notebooklm_pipeline.md | NotebookLM integration |
