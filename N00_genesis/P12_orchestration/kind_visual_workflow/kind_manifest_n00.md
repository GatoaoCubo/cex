---
id: n00_visual_workflow_manifest
kind: knowledge_card
8f: F3_inject
pillar: P12
nucleus: n00
title: "Visual Workflow -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, visual_workflow, p12, n00, archetype, template]
density_score: 1.0
related:
  - visual-workflow-builder
  - bld_schema_workflow
  - bld_schema_visual_workflow
  - kc_visual_workflow
  - bld_schema_contributor_guide
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A visual_workflow is a GUI-based workflow editor configuration that defines how a workflow is rendered, edited, and exported in visual tools like n8n, LangGraph, or Flowise. It bridges the gap between declarative workflow definitions and graphical interfaces, enabling non-technical stakeholders to view, review, and approve workflow designs without reading YAML or code.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `visual_workflow` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| editor_tool | enum | yes | n8n \| langgraph \| flowise \| custom |
| workflow_ref | string | yes | ID of the workflow artifact being visualized |
| canvas_config | object | yes | Editor canvas settings (zoom, grid, layout algorithm) |
| node_styles | array | no | Visual style overrides per node kind |
| export_formats | array | yes | Supported export formats (json, png, svg, mermaid) |
| read_only | boolean | yes | Whether the visual editor is locked for view-only |

## When to use
- When presenting a workflow to non-technical stakeholders for review or approval
- When configuring n8n or Flowise to execute a CEX workflow via GUI
- When generating Mermaid diagrams for workflow documentation

## Builder
`archetypes/builders/visual_workflow-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind visual_workflow --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: vw_fractal_fill_w3_view
kind: visual_workflow
pillar: P12
nucleus: n07
title: "Example Visual Workflow"
version: 1.0
quality: null
---
# Visual Workflow: FRACTAL_FILL Wave 3
editor_tool: custom
workflow_ref: wf_fractal_fill
export_formats: [mermaid, png]
read_only: true
canvas_config: {layout: top_down, zoom: 1.0}
```

## Related kinds
- `workflow` (P12) -- workflow definition this visual configuration renders
- `dag` (P12) -- dependency graph that may be rendered as a visual workflow
- `diagram` (P08) -- architecture diagram using similar visual representation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[visual-workflow-builder]] | related | 0.45 |
| [[bld_schema_workflow]] | upstream | 0.41 |
| [[bld_schema_visual_workflow]] | upstream | 0.40 |
| [[kc_visual_workflow]] | sibling | 0.39 |
| [[bld_schema_contributor_guide]] | upstream | 0.38 |
| [[bld_schema_reranker_config]] | upstream | 0.38 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.38 |
| [[bld_schema_usage_report]] | upstream | 0.37 |
| [[bld_schema_integration_guide]] | upstream | 0.37 |
| [[bld_schema_benchmark_suite]] | upstream | 0.37 |
