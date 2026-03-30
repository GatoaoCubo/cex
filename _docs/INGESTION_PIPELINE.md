# CEX Ingestion Pipeline Spec

**Version**: 1.0.0 | **Pillar**: P01 (Knowledge) + P04 (Tools)

## Purpose

Define how raw knowledge enters a CEX instance and becomes processed artifacts.

## Architecture

```
inbox/raw/        → User drops files (any format)
inbox/queue/      → Triage agent classifies and drafts
inbox/processed/  → Audit log of completed ingestions
pool/{category}/  → Final destination (CEX-compliant artifacts)
```

## Triage Classification

The triage agent (knowledge_agent recommended) reads each raw file and determines:

```yaml
classification:
  type: knowledge_card | research | benchmark | data | spec | code
  lp: P01-P12
  destination: pool/{category}/
  satellite: pytha | shaka | lily | york | edison
  confidence: 0.0-1.0
  suggested_name: "KC_DOMAIN_NNN.md"
```

## Processing Rules

1. **One artifact per raw file** (split large files into multiple)
2. **Frontmatter required** on output (id, type, lp, version, quality, source)
3. **Source traceability**: output always references `source: inbox/raw/{original_file}`
4. **Quality gate**: >= 7.0 to enter pool
5. **Idempotent**: re-processing same raw file overwrites, doesn't duplicate

## Doclinking (External References)

For URLs and external docs that shouldn't be downloaded:

```yaml
# In any CEX artifact frontmatter
sources:
  - type: url
    href: "https://example.com/article"
    accessed: "2026-03-22"
    summary: "Key insights about X"
  - type: doclink
    path: "inbox/raw/original_file.pdf"
    pages: "12-15"
    summary: "Pricing framework from chapter 3"
```

## Batch Processing

```bash
# Process entire inbox (orchestrator dispatches satellites)
"processa inbox"

# Process specific file
"processa inbox/raw/competitor_analysis.pdf"

# Process with specific satellite
"research_agent processa inbox/raw/arxiv_paper.pdf"
```

## Lifecycle

```
raw/ (max 48h) → queue/ (max 24h) → pool/ (permanent)
                                   ↘ rejected/ (feedback loop)
```

Files in raw/ older than 48h get flagged. Queue items older than 24h get escalated.
