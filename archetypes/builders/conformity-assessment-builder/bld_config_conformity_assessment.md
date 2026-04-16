---
kind: config
id: bld_config_conformity_assessment
pillar: P09
llm_function: CONSTRAIN
purpose: Runtime configuration for the conformity-assessment-builder (naming, paths, limits, hooks)
quality: 9.2
title: "Conformity Assessment Builder -- Config"
version: "1.0.0"
author: wave7_n05
tags: [conformity_assessment, builder, config]
tldr: "Naming convention p11_ca_{system}.md, output path P11_govern/, max 5120 bytes, compile+score hooks"
domain: "conformity_assessment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Conformity Assessment Builder -- Config

## Naming Convention

| Element | Pattern | Example |
|---------|---------|---------|
| Artifact ID | p11_ca_{{system_slug}} | p11_ca_medtriage_v2 |
| Artifact file | p11_ca_{{system_slug}}.md | p11_ca_medtriage_v2.md |
| System slug rule | lowercase, underscores, alphanumeric only | medtriage_v2 not MedTriage-v2 |
| ID regex | ^p11_ca_[a-z0-9_]+$ | validated at H02 gate |
| Builder ISO prefix | bld_{{iso}}_conformity_assessment.md | bld_manifest_conformity_assessment.md |

### Slug Derivation Rules

| Input | Derived Slug |
|-------|-------------|
| "MedTriage-v2 Clinical Decision Support" | medtriage_v2 |
| "HR Screening AI v3.0" | hr_screening_ai_v3 |
| "CreditScore Pro 2024" | creditscore_pro_2024 |
| "BorderControl-NLP-1" | bordercontrol_nlp_1 |

Rules:
1. Convert to lowercase
2. Replace spaces and hyphens with underscores
3. Strip non-alphanumeric characters (except underscores)
4. Truncate to 40 characters maximum
5. Remove leading/trailing underscores

## Paths

| Path | Purpose |
|------|---------|
| archetypes/builders/conformity-assessment-builder/ | Builder ISO directory (this directory) |
| P11_govern/ | Output directory for conformity_assessment artifacts |
| P11_govern/p11_ca_{{system_slug}}.md | Individual artifact path |
| P01_knowledge/library/kind/kc_conformity_assessment.md | Kind knowledge card for retrieval |
| .cex/runtime/handoffs/ | Incoming task handoffs from N07 |
| .cex/runtime/signals/ | Outgoing completion signals |

## Size Limits

| Limit | Value | Applies To |
|-------|-------|-----------|
| max_bytes | 5120 | Conformity assessment artifact |
| min_bytes | 2048 | Minimum content to be substantive |
| max_risks | 20 | Maximum rows in RMS risk table (use summary if more) |
| max_datasets | 10 | Maximum rows in data governance table (use reference if more) |
| max_kpis | 10 | Maximum rows in PMM KPI table |

## Hooks

### Pre-Build Hooks

| Hook | Command | Trigger |
|------|---------|---------|
| Schema validation | python _tools/cex_schema_hydrate.py --kind conformity_assessment | Before F6 PRODUCE |
| Similar artifact scan | python _tools/cex_retriever.py --kind conformity_assessment | At F5 CALL |
| Memory load | python _tools/cex_memory_select.py --query "conformity assessment EU AI Act" | At F3 INJECT |

### Post-Build Hooks

| Hook | Command | Trigger |
|------|---------|---------|
| Compile | python _tools/cex_compile.py P11_govern/p11_ca_{{system_slug}}.md | After F6 PRODUCE |
| Quality score | python _tools/cex_score.py --apply P11_govern/p11_ca_{{system_slug}}.md | At F7 GOVERN |
| Doctor check | python _tools/cex_doctor.py --file P11_govern/p11_ca_{{system_slug}}.md | At F7 GOVERN |
| Signal | python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', {{score}})" | At F8 COLLABORATE |
| ASCII check | python _tools/cex_sanitize.py --check --scope P11_govern/p11_ca_{{system_slug}}.md | Before git commit |

### Commit Hook

```bash
git add P11_govern/p11_ca_{{system_slug}}.md
git commit -m "[N03] conformity_assessment: {{system_name}} v{{version}} (Annex III: {{category}})"
```

## Quality Configuration

| Parameter | Value |
|-----------|-------|
| quality_floor | 8.0 |
| quality_target | 9.0 |
| max_retries | 2 |
| self_score | false (quality: null always) |
| peer_score_tool | cex_score.py --apply |
| density_target | 0.85 |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| CEX_CONFORMITY_PATH | P11_govern/ | Output directory for artifacts |
| CEX_CONFORMITY_MAX_BYTES | 5120 | Maximum artifact size |
| CEX_CONFORMITY_QUALITY_FLOOR | 8.0 | Minimum publishable score |
| CEX_EU_AI_ACT_DEADLINE | 2026-08-01 | Aug-2026 deadline for flagging |

## Feature Flags

| Flag | Default | Description |
|------|---------|-------------|
| REQUIRE_NB_FOR_BIOMETRIC | true | Force notified_body_id when category=biometric_identification |
| AUTO_DERIVE_SLUG | true | Derive slug from system_name automatically |
| FLAG_DEADLINE_ITEMS | true | Always append [AUG-2026-DEADLINE] to mandatory sections |
| STRICT_CITATION_CHECK | true | H02 gate fails if any requirement lacks EU AI Act article cite |

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-04-14 | Initial builder config for EU AI Act Annex-IV conformity assessment |
