---
id: p06_if_builder_protocol
kind: interface
pillar: P06
title: "Interface -- Builder Protocol Contract"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: null
tags: [interface, builder, protocol, contract, 8F, N03, interoperability]
tldr: "Bilateral contract defining what every builder (any of the 259 builder agents) must EXPOSE and what every caller (N03, N07, grid dispatch) must PROVIDE. Enables LLM-to-LLM interoperability across all 4 runtimes."
density_score: 0.92
---

# Interface: Builder Protocol Contract

## Purpose

A builder is not a free-form agent. It is a CONTRACT-BOUND component.
This interface defines the bilateral agreement between BUILDER (any builder agent)
and CALLER (N03 dispatcher, N07 orchestrator, or direct human invocation).

Implementing this interface is what makes a builder a first-class CEX component.
Violating it produces orphan artifacts with no quality record and no signal.

## Interface Definition

```typescript
interface Builder {
  // --- IDENTITY (static, set at design time) ---
  kind: string;              // canonical kind this builder produces
  pillar: Pillar;            // canonical pillar for this kind
  nucleus: NucleusId;        // owning nucleus (usually n03)
  builder_id: string;        // "{kind}-builder"
  iso_count: number;         // number of builder ISOs loaded (must be 13)
  sin_lens: SinLens;         // cultural filter applied to F6 PRODUCE

  // --- EXECUTION (runtime, per build invocation) ---
  execute(task: BuildTask): BuildResult;

  // --- REQUIRED CAPABILITIES ---
  loadISOs(): BuilderContext;          // F2 BECOME: load all 13 ISOs
  injectContext(kind: string): void;   // F3 INJECT: load KCs + examples + brand
  validateOutput(artifact: string): ValidationResult;  // F7 GOVERN
  saveAndSignal(artifact: string, score: number): void;  // F8 COLLABORATE

  // --- OPTIONAL CAPABILITIES ---
  dryRun?(task: BuildTask): string;    // simulate without writing
  estimate?(task: BuildTask): TokenBudget;  // token cost estimate
}
```

## BuildTask Type

```typescript
type BuildTask = {
  intent: string | null;
  kind: string;
  pillar: Pillar;
  verb: BuildAction;
  quality_target: number;      // default 9.0
  context: string | null;
  domain: string | null;
  output_path: string;
  compile: boolean;
  signal: boolean;
  session_id: string;
}
```

## BuildResult Type

```typescript
type BuildResult = {
  status: "success" | "fail" | "warn" | "retry";
  artifact_path: string | null;
  quality_score: number | null;    // null = not scored (peer-review pending)
  validation: ValidationResult;
  iso_count: number;               // ISOs loaded during F2
  context_sources: string[];       // files injected during F3
  bytes_written: number;
  pipeline_trace: string;          // 8F trace output (F1-F8)
  signal_sent: boolean;
}
```

## Caller Obligations (what N03/N07 must provide)

| Obligation | Description |
|-----------|-------------|
| C-01 | Provide resolved `kind` (not raw intent alone) |
| C-02 | Provide writable `output_path` within repo root |
| C-03 | Confirm builder ISOs exist before dispatch |
| C-04 | Set `session_id` for signal correlation |
| C-05 | Set `quality_target` >= 7.0 (below = warning logged) |
| C-06 | Wait for signal before treating build as complete |

## Builder Obligations (what every builder must guarantee)

| Obligation | Description |
|-----------|-------------|
| B-01 | Load ALL 13 ISOs before F6 PRODUCE (F2 BECOME) |
| B-02 | Load KC for the kind before producing (F3 INJECT) |
| B-03 | Set `quality: null` in frontmatter (never self-score) |
| B-04 | Write artifact to the exact `output_path` provided |
| B-05 | Run cex_compile.py on output if `compile=true` |
| B-06 | Send signal if `signal=true` |
| B-07 | Output complete 8F trace to stdout |
| B-08 | Retry F6 up to 2 times if F7 fails before raising |

## 13 Required ISOs (F2 BECOME)

Every builder loads exactly 13 ISOs from `archetypes/builders/{kind}-builder/`:

| ISO | File Pattern | F-Function |
|-----|-------------|-----------|
| 1 | bld_manifest_{kind}.md | F1 |
| 2 | bld_instruction_{kind}.md | F4 |
| 3 | bld_system_prompt_{kind}.md | F2 |
| 4 | bld_schema_{kind}.md | F1 |
| 5 | bld_template_{kind}.md | F6 |
| 6 | bld_quality_gates_{kind}.md | F7 |
| 7 | bld_examples_{kind}.md | F3 |
| 8 | bld_anti_examples_{kind}.md | F3 |
| 9 | bld_knowledge_{kind}.md | F3 |
| 10 | bld_prompt_cache_{kind}.md | F5 |
| 11 | bld_compiler_{kind}.md | F8 |
| 12 | bld_scorer_{kind}.md | F7 |
| 13 | bld_memory_{kind}.md | F3b |

## Runtime Interoperability

This interface is honoured by all 4 runtimes:

| Runtime | Protocol | Variation |
|---------|---------|----------|
| Claude | native tool calls | full interface |
| Codex | file I/O + subprocess | no signal auto-send; N07 commits |
| Gemini | native tool calls | flash vs pro tier per nucleus |
| Ollama | HTTP API | context capped at model max_tokens |

Differences are encapsulated by `cex_router.py`. The interface contract is identical
across all runtimes -- routing is a deployment concern, not a builder concern.
