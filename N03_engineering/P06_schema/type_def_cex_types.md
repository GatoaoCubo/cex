---
id: p06_td_cex_types
kind: type_def
8f: F1_constrain
pillar: P06
title: "Type Definitions -- CEX Core Types"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [type-def, CEX, core-types, kind, pillar, nucleus, quality, pipeline, N03]
tldr: "Canonical type definitions for the CEX typed knowledge system: Kind, Pillar, Nucleus, Quality, Pipeline, BuildAction, Signal. The source of truth for structural contracts across all 8 nuclei."
density_score: 0.92
updated: "2026-04-17"
related:
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_schema_multimodal_prompt
  - p06_is_creation_data
  - bld_schema_tagline
  - n06_schema_brand_config
  - bld_schema_training_method
  - bld_schema_prompt_compiler
  - bld_schema_audit_log
  - bld_schema_benchmark_suite
---

# Type Definitions: CEX Core Types

## Purpose

Defines the canonical structural types used throughout the CEX system.
Every artifact, builder, nucleus, and signal maps to one or more of these types.
These definitions are the machine-readable ground truth for the 257-kind taxonomy.

## Core Types

### Kind

```typescript
type Kind = {
  id: string;               // snake_case identifier, globally unique
  name: string;             // human-readable display name
  pillar: Pillar;           // canonical pillar assignment (P01-P12)
  description: string;      // one-line purpose description
  max_bytes: number;        // maximum artifact size in bytes
  naming_pattern: string;   // regex pattern for artifact filename
  builder: string;          // builder agent reference: {kind}-builder
  schema_id: string;        // input_schema artifact id for this kind
  tags: string[];           // classification tags
}
```

### Pillar

```typescript
type Pillar = 
  | "P01"  // Knowledge -- storage, retrieval, KCs
  | "P02"  // Model -- agent definitions, providers
  | "P03"  // Prompt -- templates, actions, chains
  | "P04"  // Tools -- external capabilities
  | "P05"  // Output -- production artifacts
  | "P06"  // Schema -- data contracts
  | "P07"  // Evaluation -- quality, scoring, testing
  | "P08"  // Architecture -- system structure
  | "P09"  // Config -- runtime settings
  | "P10"  // Memory -- state, context, indexing
  | "P11"  // Feedback -- learning, correction
  | "P12"  // Orchestration -- workflows, dispatch
```

### Nucleus

```typescript
type Nucleus = {
  id: NucleusId;              // n00-n07
  name: string;               // display name (e.g. "N03_engineering")
  sin_lens: SinLens;          // cultural DNA driving optimization
  domain: string;             // primary domain
  model: "haiku" | "sonnet" | "opus";  // assigned model tier
  context_window: number;     // token limit (200000 or 1000000)
  primary_pillars: Pillar[];  // top priority pillars
  agent_card_path: string;    // path to agent_card artifact
}

type NucleusId = "n00" | "n01" | "n02" | "n03" | "n04" | "n05" | "n06" | "n07"

type SinLens =
  | "analytical_envy"         // N01
  | "creative_lust"           // N02
  | "inventive_pride"         // N03
  | "knowledge_gluttony"      // N04
  | "gating_wrath"            // N05
  | "strategic_greed"         // N06
  | "orchestrating_sloth"     // N07
```

### Quality

```typescript
type Quality = {
  score: number | null;       // null until peer-reviewed; range [0.0, 10.0]
  tier: QualityTier | null;   // derived from score
  dimensions: QualityDimension[];  // D1-D5 scores
  reviewer: string | null;    // nucleus that assigned quality
  reviewed_at: string | null; // ISO date
}

type QualityTier =
  | "exemplary"    // score >= 9.5
  | "excellent"    // score >= 9.0
  | "good"         // score >= 8.0
  | "acceptable"   // score >= 7.0
  | "below_floor"  // score < 7.0 (blocked from publication)

type QualityDimension = {
  id: "D1" | "D2" | "D3" | "D4" | "D5";
  name: string;   // D1=Structural, D2=Rubric, D3=Semantic, D4=Coverage, D5=Novelty
  weight: number; // percentage, D1+D2+D3+D4+D5 = 100
  score: number;  // 0.0-10.0
}
```

### Pipeline

```typescript
type Pipeline = {
  id: string;           // 8F instance id
  nucleus: NucleusId;   // executing nucleus
  kind: string;         // artifact kind being built
  started_at: string;   // ISO timestamp
  functions: PipelineFunction[];  // F1-F8 execution records
  status: "running" | "complete" | "failed" | "retrying";
  artifact_path: string | null;   // output artifact path on complete
}

type PipelineFunction = {
  fn: "F1" | "F2" | "F2b" | "F3" | "F3b" | "F3c" | "F4" | "F5" | "F6" | "F7" | "F7b" | "F8";
  name: string;         // CONSTRAIN, BECOME, SPEAK, INJECT, etc.
  status: "pending" | "running" | "complete" | "skipped";
  output: string;       // trace output line
  bytes_consumed: number;
}
```

### BuildAction

```typescript
type BuildAction = "CREATE" | "REWRITE" | "MIGRATE" | "IMPROVE" | "VALIDATE"

// CREATE: produce artifact from scratch, fail if already exists (unless force=true)
// REWRITE: discard existing artifact, build fresh from same intent
// MIGRATE: update artifact structure/schema while preserving content
// IMPROVE: enhance quality score of existing artifact (F7 loop)
// VALIDATE: run F7 GOVERN only, do not produce/save
```

### Signal

```typescript
type Signal = {
  nucleus: NucleusId;
  event: "complete" | "error" | "partial" | "ready";
  score: number | null;
  artifacts: string[];    // paths of produced artifacts
  timestamp: string;      // ISO timestamp
  session_id: string;     // N07 session this belongs to
  wave: string | null;    // mission wave identifier
}
```

## Type Hierarchy

```
CEX System
  |-- Kind (257 types in kinds_meta.json)
  |-- Pillar (P01-P12, 12 domain groups)
  |-- Nucleus (N00-N07, 8 operational agents)
        |-- Pipeline (8F execution: F1->F8)
        |-- Signal (completion notification)
  |-- Artifact (instance of a Kind, governed by Quality)
        |-- Quality (null until peer-reviewed)
```

## Type Invariants

1. Every Artifact has exactly one Kind
2. Every Kind maps to exactly one Pillar
3. Quality.score is null until explicitly assigned by a peer nucleus (never self-assigned)
4. Pipeline.functions execute in strict order F1->F2->F3->F4->F5->F6->F7->F8
5. Signal.nucleus must match the nucleus that produced the artifact

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | related | 0.44 |
| [[bld_schema_experiment_tracker]] | related | 0.41 |
| [[bld_schema_multimodal_prompt]] | related | 0.36 |
| [[p06_is_creation_data]] | related | 0.35 |
| [[bld_schema_tagline]] | related | 0.35 |
| [[n06_schema_brand_config]] | related | 0.35 |
| [[bld_schema_training_method]] | related | 0.35 |
| [[bld_schema_prompt_compiler]] | related | 0.34 |
| [[bld_schema_audit_log]] | related | 0.33 |
| [[bld_schema_benchmark_suite]] | related | 0.33 |
