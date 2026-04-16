---
kind: architecture
id: bld_architecture_webinar_script
pillar: P08
llm_function: CONSTRAIN
purpose: Component inventory, dependency map, and architectural position of the webinar_script builder
quality: 9.1
title: "Webinar Script Builder Architecture"
version: "1.0.0"
author: n02_wave6
tags: [webinar_script, builder, architecture]
tldr: "13-ISO builder architecture for webinar_script: component inventory, dependency graph, and P03 positioning."
domain: "webinar_script construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
## Component Inventory

All 13 ISOs of the webinar-script-builder with role, pillar, and status.

| ISO | File | Kind | Pillar | LLM Function | Role |
|-----|------|------|--------|-------------|------|
| 1 | bld_manifest_webinar_script.md | type_builder | P03 | BECOME | Builder identity, capabilities, and routing signals |
| 2 | bld_instruction_webinar_script.md | instruction | P03 | REASON | 3-phase production instructions: research, compose, validate |
| 3 | bld_system_prompt_webinar_script.md | system_prompt | P03 | BECOME | Persona activation with ALWAYS/NEVER quality rules |
| 4 | bld_schema_webinar_script.md | schema | P06 | CONSTRAIN | Frontmatter field definitions, ID pattern, body section order |
| 5 | bld_quality_gate_webinar_script.md | quality_gate | P11 | GOVERN | 8 hard gates + 5 scored dimensions, publish floor 8.0 |
| 6 | bld_output_template_webinar_script.md | output_template | P05 | PRODUCE | Canonical script template with all section placeholders |
| 7 | bld_examples_webinar_script.md | examples | P07 | GOVERN | Golden example + 2 anti-examples with failure analysis |
| 8 | bld_knowledge_card_webinar_script.md | knowledge_card | P01 | INJECT | Domain knowledge: benchmarks, concepts, patterns, pitfalls |
| 9 | bld_architecture_webinar_script.md | architecture | P08 | CONSTRAIN | Component inventory, dependency map, system position |
| 10 | bld_collaboration_webinar_script.md | collaboration | P12 | COLLABORATE | Crew roles, receives-from, produces-for, boundary |
| 11 | bld_config_webinar_script.md | config | P09 | CONSTRAIN | Naming, paths, limits, hooks |
| 12 | bld_memory_webinar_script.md | memory | P10 | INJECT | Observed patterns, evidence, and builder recommendations |
| 13 | bld_tools_webinar_script.md | tools | P04 | CALL | Production tools, validation tools, external platform references |
## Dependency Graph

Dependencies listed as: ISO -> depends on -> ISO (load order).

| ISO | Depends On | Reason |
|-----|-----------|--------|
| manifest | config | Routing keywords aligned with naming convention |
| instruction | system_prompt | Compose phase applies persona rules from system prompt |
| output_template | schema | Template placeholders must match required frontmatter fields |
| quality_gate | examples | Gate thresholds calibrated against golden example scores |
| quality_gate | schema | H01-H03 gates enforce schema constraints |
| collaboration | manifest | Crew role derived from builder identity |
| tools | quality_gate | Validation tools implement gate checks |
| memory | examples | Learning records derived from example pattern analysis |

**Load order for 8F pipeline**:
1. config (F1 CONSTRAIN -- naming, limits)
2. schema (F1 CONSTRAIN -- field validation)
3. manifest (F2 BECOME -- identity)
4. system_prompt (F2 BECOME -- persona)
5. knowledge_card (F3 INJECT -- domain knowledge)
6. memory (F3 INJECT -- learned patterns)
7. examples (F3 INJECT -- calibration)
8. instruction (F4 REASON -- production plan)
9. tools (F5 CALL -- available tools)
10. output_template (F6 PRODUCE -- scaffold)
11. quality_gate (F7 GOVERN -- validation)
12. collaboration (F8 COLLABORATE -- handoff routing)
13. architecture (reference -- no pipeline stage, used for system audits)
## External Dependencies

| Dependency | Type | Used By | Notes |
|-----------|------|---------|-------|
| cex_compile.py | Tool | F8 COLLABORATE | Compiles .md -> .yaml after save |
| cex_score.py | Tool | F7 GOVERN | Applies quality scores |
| cex_retriever.py | Tool | F3 INJECT | Finds similar webinar scripts |
| cex_doctor.py | Tool | F8 COLLABORATE | Post-build health check |
| Zoom Webinar API | External | tools ISO | Platform integration reference |
| GoToWebinar API | External | tools ISO | Platform integration reference |
| Teams Live Events API | External | tools ISO | Platform integration reference |
## Architectural Position

The webinar_script builder occupies the **P03 Prompt / Live Delivery** layer of CEX. It bridges prompt engineering (structured speaker narration) with audience engagement mechanics (hook frameworks, Q&A facilitation, conversion CTAs).

**Upstream**: Marketing brief (N02), product demo assets (N05 or product team), slide deck outline (design team or pitch_deck-builder).

**Downstream**: Presenter delivery, event platform (Zoom/GoToWebinar/Teams), email follow-up sequence (N02 email-copy-builder), recording and replay distribution.

**Boundary enforcement**: webinar_script does NOT produce visual slides (pitch_deck-builder), 1:1 sales scripts (sales_playbook-builder), or recorded course content (online-course-builder). Any request for those artifact types must be routed to the appropriate builder.

**Naming space**: All artifacts occupy `p03_ws_*.md` within `P03_prompt/`. Compiled YAML counterparts stored in `archetypes/builders/compiled/`.
