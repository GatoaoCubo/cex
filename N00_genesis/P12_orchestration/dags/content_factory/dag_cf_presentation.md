---
id: p12_dag_cf_presentation
kind: dag
8f: F8_collaborate
pillar: P12
lp: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
pipeline: "content_factory_presentation"
nodes:
  - id: "receive_longform"
    label: "Receive master longform draft and brand context from dag_cf_master"
    agent_group: "n07_orchestrator"
  - id: "define_outline"
    label: "Structure presentation: sections, slide count per section, key messages"
    agent_group: "n01_research"
  - id: "write_slide_content"
    label: "Write slide titles, bullet points, and key data per slide"
    agent_group: "n03_builder"
  - id: "write_speaker_notes"
    label: "Write detailed speaker notes per slide for presenter guidance"
    agent_group: "n02_marketing"
  - id: "design_slides"
    label: "Create visual slides via Canva API with brand template"
    agent_group: "n06_brand"
  - id: "generate_charts"
    label: "Generate data charts, diagrams, and visual assets for slides"
    agent_group: "n03_builder"
  - id: "assemble_deck"
    label: "Merge slide content + visuals + speaker notes into final deck"
    agent_group: "n05_operations"
  - id: "quality_check"
    label: "Validate against cs_cf_presentation constraints (slide count, bullets)"
    agent_group: "n04_knowledge"
  - id: "export"
    label: "Export to PPTX + PDF + Google Slides and upload to CDN staging"
    agent_group: "n05_operations"
edges:
  - from: "receive_longform"
    to: "define_outline"
  - from: "define_outline"
    to: "write_slide_content"
  - from: "write_slide_content"
    to: "write_speaker_notes"
  - from: "write_slide_content"
    to: "design_slides"
  - from: "write_slide_content"
    to: "generate_charts"
  - from: "write_speaker_notes"
    to: "assemble_deck"
  - from: "design_slides"
    to: "assemble_deck"
  - from: "generate_charts"
    to: "assemble_deck"
  - from: "assemble_deck"
    to: "quality_check"
  - from: "quality_check"
    to: "export"
domain: "orchestration"
quality: 9.0
tags: [dag, content-factory, presentation-pipeline, canva, slides, pptx]
tldr: "9-node presentation DAG: longform→outline→content→parallel(notes+design+charts)→assemble→QA→export PPTX/PDF"
execution_order:
  - ["receive_longform"]
  - ["define_outline"]
  - ["write_slide_content"]
  - ["write_speaker_notes", "design_slides", "generate_charts"]
  - ["assemble_deck"]
  - ["quality_check"]
  - ["export"]
parallel_groups:
  - ["write_speaker_notes", "design_slides", "generate_charts"]
critical_path: ["receive_longform", "define_outline", "write_slide_content", "design_slides", "assemble_deck", "quality_check", "export"]
estimated_duration: "40min"
node_count: 9
edge_count: 10
max_parallelism: 3
keywords: [presentation, slides, canva, pptx, speaker-notes, content-factory]
linked_artifacts:
  primary: "P12_orchestration/dags/content_factory/dag_cf_master.md"
  related:
    - "P03_prompts/constraints/content_factory/p03_constraint_cf_presentation.md"
density_score: 1.0
related:
  - p12_dag_cf_course
  - p12_dag_cf_video
  - p12_dag_cf_ebook
  - p12_dag_cf_social
  - p12_dag_cf_master
  - n01_output_cf_dags_and_specs
  - wave2_quality_report
  - n04_output_monetization_curriculum
  - p12_wf_content_factory_v1
  - commercial_readiness_20260414c
---

## Nodes

| ID | Label | Agent | Type |
|----|-------|-------|------|
| receive_longform | Receive longform draft + brand context | n07_orchestrator | input |
| define_outline | Structure sections, slide count, key messages | n01_research | compute |
| write_slide_content | Write titles, bullets, data per slide | n03_builder | compute |
| write_speaker_notes | Write detailed presenter guidance per slide | n02_marketing | compute |
| design_slides | Create visual slides via Canva + brand template | n06_brand | compute |
| generate_charts | Generate charts, diagrams, visual assets | n03_builder | compute |
| assemble_deck | Merge content + visuals + notes into deck | n05_operations | join |
| quality_check | Validate against cs_cf_presentation constraints | n04_knowledge | gate |
| export | Export PPTX + PDF + Google Slides to CDN | n05_operations | output |

## Edges

| From | To | Type |
|------|----|------|
| receive_longform | define_outline | data |
| define_outline | write_slide_content | data |
| write_slide_content | write_speaker_notes | data |
| write_slide_content | design_slides | data |
| write_slide_content | generate_charts | data |
| write_speaker_notes | assemble_deck | data |
| design_slides | assemble_deck | data |
| generate_charts | assemble_deck | data |
| assemble_deck | quality_check | control |
| quality_check | export | control |

## Topological Order

receive_longform → define_outline → write_slide_content → write_speaker_notes → design_slides → generate_charts → assemble_deck → quality_check → export

## Parallel Groups

- **Wave 1**: receive_longform
- **Wave 2**: define_outline
- **Wave 3**: write_slide_content
- **Wave 4**: write_speaker_notes, design_slides, generate_charts (max parallelism = 3)
- **Wave 5**: assemble_deck (join barrier — waits for all 3)
- **Wave 6**: quality_check
- **Wave 7**: export

## Critical Path

receive_longform (1min) → define_outline (5min) → write_slide_content (10min) → design_slides (10min) → assemble_deck (5min) → quality_check (2min) → export (2min) = **35min**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dag_cf_course]] | sibling | 0.65 |
| [[p12_dag_cf_video]] | sibling | 0.63 |
| [[p12_dag_cf_ebook]] | sibling | 0.61 |
| [[p12_dag_cf_social]] | sibling | 0.57 |
| [[p12_dag_cf_master]] | sibling | 0.21 |
| [[n01_output_cf_dags_and_specs]] | upstream | 0.20 |
| [[wave2_quality_report]] | upstream | 0.19 |
| [[n04_output_monetization_curriculum]] | upstream | 0.17 |
| [[p12_wf_content_factory_v1]] | related | 0.17 |
| [[commercial_readiness_20260414c]] | upstream | 0.16 |
