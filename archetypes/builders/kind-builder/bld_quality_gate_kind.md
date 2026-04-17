---
id: p11_qg_kind_builder
kind: quality_gate
pillar: P11
title: "Gate: kind_builder"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
domain: "kind_builder -- meta-builder that produces complete 13-ISO builder packages for any CEX kind"
quality: 9.1
tags: [quality-gate, kind-builder, meta-builder, architecture, iso, P11]
tldr: "Gates for builder packages: validates 13-file completeness, frontmatter consistency, quality:null, naming, sub-agent."
density_score: 0.92
llm_function: GOVERN
---
# Gate: kind_builder

## Definition

| Field | Value |
|-------|-------|
| metric | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator | AND (all HARD) + weighted_sum (SOFT) |
| scope | All builder packages at archetypes/builders/{kind}-builder/ |

## HARD Gates

All must pass. Any single failure = REJECT regardless of SOFT score.

| ID | Check | Failure message |
|----|-------|----------------|
| H01 | Directory contains exactly 13 bld_*.md files | "Incomplete package: {N}/13 ISOs found" |
| H02 | All 13 files have parseable YAML frontmatter | "ISO {file} has invalid YAML frontmatter" |
| H03 | All 13 files have quality: null in frontmatter | "ISO {file} has quality != null (never self-score)" |
| H04 | All file names match bld_{iso_type}_{kind}.md pattern | "File {file} does not match naming pattern" |
| H05 | Sub-agent file exists at .claude/agents/{kind}-builder.md | "Sub-agent definition missing" |
| H06 | bld_manifest has >= 4 capabilities listed | "Manifest has fewer than 4 capabilities" |
| H07 | bld_schema has Frontmatter Fields table with >= 8 rows | "Schema has incomplete frontmatter field definitions" |
| H08 | bld_quality_gate has >= 6 HARD gates defined | "Quality gate has fewer than 6 HARD gates" |
| H09 | bld_examples has both Golden Example and Anti-Example sections | "Examples missing golden or anti-example" |
| H10 | bld_system_prompt has >= 8 numbered rules | "System prompt has fewer than 8 rules" |
| H11 | bld_architecture has Boundary Table section | "Architecture missing boundary table" |
| H12 | Every ISO has domain-specific content (not generic placeholders) | "ISO {file} contains generic filler text" |

## SOFT Scoring

Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.

| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Internal consistency | 1.5 | Schema fields match template vars match gate checks |
| Boundary clarity | 1.0 | IS/IS NOT boundaries in schema, KC, and architecture |
| Domain specificity | 1.5 | Content is specific to the target kind, not generic builder text |
| Cross-referencing | 1.0 | Related kinds from same pillar are mentioned and differentiated |
| Golden example quality | 1.0 | Golden example passes all HARD gates listed in quality_gate ISO |
| Instruction completeness | 1.0 | 3 phases with >= 5 steps each, covering research/compose/validate |
| Memory patterns | 0.5 | Patterns backed by evidence, anti-patterns listed |
| Tool accuracy | 0.5 | Listed tools exist and are correctly described |
| Collaboration clarity | 0.5 | Crew compositions realistic, handoff protocol complete |
| Config precision | 0.5 | Naming, paths, size limits match kinds_meta.json values |

Weight sum: 1.5+1.0+1.5+1.0+1.0+1.0+0.5+0.5+0.5+0.5 = 9.0

Normalize: multiply final by 10/9 to reach 10.0 scale.

## Actions

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as reference builder for future kind-builder runs |
| >= 8.0 | PUBLISH | Builder is functional, ready for dispatch |
| >= 7.0 | REVIEW | Flag for manual review before first use |
| < 7.0 | REJECT | Return to kind-builder with failure report |

## Bypass

| Field | Value |
|-------|-------|
| conditions | Experimental kind with no established domain knowledge yet |
| approver | N07 orchestrator approval required; quality: null still mandatory |
