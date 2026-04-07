---
id: p06_if_builder_nucleus
kind: interface
pillar: P06
title: Interface -- Builder Nucleus
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [interface, builder, N03]
tldr: Public API surface -- CLI commands, Python imports, I/O contracts.
density_score: 0.88
---

# Interface: Builder Nucleus

## CLI Commands

| Command | Purpose |
|---------|---------|
| cex_8f_motor.py --intent ... | Parse intent to kind |
| cex_8f_runner.py --kind X | Build single artifact |
| cex_doctor.py | Health check |
| cex_compile.py PATH | Compile .md to .yaml |
| cex_index.py | Rebuild index |
| cex_kind_register.py --kind X | Register new kind |
| cex_nucleus_builder.py --nucleus N0x | Build nucleus |
| cex_forge.py | Batch build |
| cex_feedback.py | Apply feedback |

## Input Contract

Minimum: intent string OR explicit kind name.
Maximum: intent + kind + pillar + context + domain + output_dir + model + dry_run.

## Output Contract

Success: file path + compiled path + quality score + signal JSON.
Failure: error signal with step number and reason.

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | engineering | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Schema changes require backward compatibility assessment
- Required fields enforced at validation time, not at parse time
- Version field tracks breaking vs non-breaking schema evolution
- Example payloads included for every schema to enable testing

### Usage Reference

```yaml
# interface integration
artifact: interface_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

