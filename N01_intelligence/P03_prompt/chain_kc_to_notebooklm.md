---
id: p03_ch_kc_to_notebooklm
kind: chain
pillar: P03
title: "Chain: KC Selection + Formatting for NotebookLM Upload"
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: N01_intelligence
domain: notebooklm-pipeline
steps: 4
flow: discover -> score -> format -> validate
quality: 9.0
tags: [chain, notebooklm, kc, formatting, pipeline, content-factory]
tldr: "4-step prompt chain: discover KCs by domain -> score relevance -> format for NotebookLM input -> validate output. Transforms structured KCs into plain text optimized for NotebookLM indexing."
density_score: null
related:
  - p03_ch_content_pipeline
  - bld_output_template_function_def
  - n06_schema_brand_config
  - bld_schema_model_registry
  - bld_examples_function_def
  - bld_schema_validation_schema
  - bld_schema_input_schema
  - p06_td_quality_score
  - p03_react_web_research
  - bld_schema_agent_grounding_record
---

# Chain: KC to NotebookLM

## Purpose

Transforms raw CEX knowledge cards into text optimized for NotebookLM's source indexing.
NotebookLM processes plain text differently from structured markdown -- it excels with
narrative prose and clear headings but struggles with complex tables, YAML frontmatter,
and cross-references to other files.

This chain bridges that gap: it discovers relevant KCs, scores them for upload priority,
converts their format, and validates the output fits NotebookLM's constraints.

Compared to alternative approaches:
- **vs raw KC upload**: Raw KCs contain YAML frontmatter and internal links that confuse NotebookLM
- **vs manual copy-paste**: This chain automates selection, prioritization, and formatting
- **vs custom summarizer**: We preserve full KC content (NotebookLM does its own summarization)

## Steps

### Step 1: Discover
**Model**: haiku (fast enumeration, no synthesis needed)
**Fallback**: none (deterministic file scan)

**Input Schema:**
```json
{
  "type": "object",
  "properties": {
    "domain": {"type": "string", "description": "Target domain (meta, brand, kind, integration, operations, commercial)"},
    "explicit_paths": {"type": "array", "items": {"type": "string"}, "description": "Override: specific KC paths to include"},
    "max_sources": {"type": "integer", "default": 50, "maximum": 50, "description": "NotebookLM limit per notebook"},
    "library_root": {"type": "string", "default": "P01_knowledge/library/"}
  },
  "required": ["domain"]
}
```

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "candidates": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "path": {"type": "string"},
          "title": {"type": "string"},
          "domain": {"type": "string"},
          "kind_type": {"type": "string"},
          "byte_size": {"type": "integer"},
          "quality": {"type": "number"},
          "tags": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "total_found": {"type": "integer"},
    "total_bytes": {"type": "integer"}
  }
}
```

**Logic**: Scan `library_root` for KCs matching domain. If `explicit_paths` given, use those.
Extract frontmatter metadata for scoring in Step 2.

### Step 2: Score
**Model**: sonnet (relevance assessment, comparative ranking)
**Fallback**: haiku

**Input**: `candidates` array from Step 1 + `domain` context

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "ranked": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "path": {"type": "string"},
          "title": {"type": "string"},
          "relevance_score": {"type": "number", "minimum": 0, "maximum": 1},
          "priority": {"type": "string", "enum": ["must_include", "high", "medium", "low"]},
          "reason": {"type": "string"}
        }
      }
    },
    "selected_count": {"type": "integer"},
    "excluded_count": {"type": "integer"},
    "total_bytes_selected": {"type": "integer"}
  }
}
```

**Scoring criteria**:
| Factor | Weight | Rationale |
|--------|--------|-----------|
| Quality score | 0.3 | Higher quality = better source material |
| Domain match | 0.25 | Exact domain match > tangential |
| Content density | 0.2 | Dense KCs provide more value per source slot |
| Recency | 0.15 | Fresher content preferred |
| Unique coverage | 0.1 | Avoids redundant sources |

**Filter**: Exclude KCs with quality < 7.0. Cap at `max_sources`.

### Step 3: Format
**Model**: haiku (deterministic transformation, no creativity needed)
**Fallback**: none (template-based, should not fail)

**Input**: `ranked` array from Step 2 (paths + metadata)

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "formatted_sources": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "original_path": {"type": "string"},
          "title": {"type": "string"},
          "content": {"type": "string", "maxLength": 200000},
          "char_count": {"type": "integer"},
          "transforms_applied": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "total_chars": {"type": "integer"},
    "sources_formatted": {"type": "integer"}
  }
}
```

**Transforms** (applied in order):

| # | Transform | Why |
|---|-----------|-----|
| 1 | Strip YAML frontmatter (everything between `---` markers) | NotebookLM can't parse YAML; it confuses the indexer |
| 2 | Prepend `# {title}` as H1 | Source identification in NotebookLM UI |
| 3 | Convert markdown tables to prose lists | NotebookLM extracts more meaning from prose than table cells |
| 4 | Remove internal cross-references (`[text](../path)`) | Broken links in NotebookLM context |
| 5 | Expand abbreviations (KC -> Knowledge Card, 8F -> 8-Function Pipeline) | NotebookLM users may not know CEX jargon |
| 6 | Truncate to 200K chars | NotebookLM source limit is 500K words but practical limit is lower |

**Table-to-prose example**:
```
Before: | Kind | Pillar | Description |
        | agent | P02 | Autonomous entity |

After:  - **agent** (Pillar P02): Autonomous entity that executes tasks independently.
```

### Step 4: Validate
**Model**: haiku (checklist validation)
**Fallback**: none

**Input**: `formatted_sources` from Step 3

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "valid": {"type": "boolean"},
    "sources_valid": {"type": "integer"},
    "sources_invalid": {"type": "integer"},
    "issues": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source": {"type": "string"},
          "issue": {"type": "string"},
          "severity": {"type": "string", "enum": ["error", "warning"]},
          "fix": {"type": "string"}
        }
      }
    },
    "ready_for_upload": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Paths of sources that passed validation"
    }
  }
}
```

**Validation checklist**:
| Check | Severity | Rule |
|-------|----------|------|
| No YAML frontmatter remains | error | No `---` block at start |
| Title present as H1 | error | First line is `# Title` |
| Char count < 200K | error | NotebookLM source limit |
| Char count > 100 | warning | Too short to be useful |
| No broken internal links | warning | No `](../` patterns |
| No raw code blocks > 50 lines | warning | NotebookLM processes prose better |

## Data Flow

```
[Domain Request]
       |
       v
  Step 1: DISCOVER (scan library, extract metadata)
       |  {candidates[]: path, title, domain, quality, size}
       v
  Step 2: SCORE (rank by relevance, filter by quality)
       |  {ranked[]: path, title, relevance, priority}
       |  [exclude quality < 7.0, cap at max_sources]
       v
  Step 3: FORMAT (strip frontmatter, tables->prose, truncate)
       |  {formatted[]: title, content, char_count, transforms}
       v
  Step 4: VALIDATE (checklist: size, structure, links)
       |  {ready_for_upload[]: validated source paths}
       v
  [Ready for workflow_notebooklm_pipeline Step 4: Upload]
```

## Error Handling

| Step | Error | Action |
|------|-------|--------|
| 1 | No KCs found for domain | Return empty, suggest broader domain or explicit_paths |
| 2 | All KCs score below threshold | Lower threshold to 6.0, warn in output |
| 3 | KC file unreadable | Skip source, add to issues list, continue |
| 4 | Source fails validation | Move to issues, exclude from ready_for_upload |

## Research Base

- NotebookLM indexing tested 2026-04-06: prose > tables for comprehension quality
- 75 flashcards generated from 14.6KB KC (kc_8f_pipeline.md) -- validates format works
- Source limit: 50 per notebook, 500K words per source (practical: 200K chars safe)
- Chain pattern: output A -> input B with explicit data contracts (DSPy MIPRO paradigm)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ch_content_pipeline]] | sibling | 0.50 |
| [[bld_output_template_function_def]] | downstream | 0.32 |
| [[n06_schema_brand_config]] | downstream | 0.31 |
| [[bld_schema_model_registry]] | downstream | 0.30 |
| [[bld_examples_function_def]] | downstream | 0.29 |
| [[bld_schema_validation_schema]] | downstream | 0.28 |
| [[bld_schema_input_schema]] | downstream | 0.28 |
| [[p06_td_quality_score]] | downstream | 0.28 |
| [[p03_react_web_research]] | related | 0.27 |
| [[bld_schema_agent_grounding_record]] | downstream | 0.27 |
