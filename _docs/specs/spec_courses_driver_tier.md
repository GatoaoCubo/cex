---
id: spec_courses_driver_tier
kind: constraint_spec
pillar: P06
title: "Spec -- Driver Tier Course Content Pipeline"
version: 1.0.0
created: "2026-04-21"
author: n07_orchestrator
domain: infoproduct
quality: 8.5
status: SPEC
scope: n02_marketing + n04_knowledge
depends_on:
  - spec_oss_wiring_final
tags: [spec, courses, infoproduct, driver, lenses, monetization]
tldr: "3-wave spec to scaffold Driver-tier course content: lens KCs, 4 modules in PT-BR, pipeline validation."
density_score: 0.92
updated: "2026-04-22"
---

# Spec: Driver Tier Course Content Pipeline

## Problem

CEXAI has 293 kinds, 8F pipeline, 12 pillars, 7 sin-driven nuclei -- but zero
educational content that non-technical users can consume. The OSS repo IS the
engine; courses teach people to drive it. No courses = no monetization path.

## Vision

4-module Driver-tier course in PT-BR, each module teaching one core CEXAI concept
through 7 parallel analogy lenses. Content lives in `_courses/driver/`, is stripped
from the public OSS export, and feeds into the existing media pipeline
(`cex_media_produce.py` + NotebookLM + Marp).

## Decisions (from manifest)

- Tier: Driver (non-technical, largest PT-BR audience)
- Modules: 4 (structured_thinking, seven_sins, twelve_pillars, naming_things)
- Platform: Hotmart primary, YouTube free funnel
- Language: PT-BR primary
- Format: Text first, slides second, audio third
- Lenses: All 7 scaffolded (bible, anatomy, games, car, enterprise, factory, technical)
- Constraints: No code, no jargon without analogy, quality: null

## Artifacts

### Wave 1: Lens Infrastructure (3 new KCs + config update)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | N04_knowledge/P01_knowledge/kc_lens_bible.md | knowledge_card | 4KB | Biblical metaphor mapping for all CEX concepts |
| CREATE | N04_knowledge/P01_knowledge/kc_lens_car.md | knowledge_card | 4KB | Automotive metaphor mapping |
| CREATE | N04_knowledge/P01_knowledge/kc_lens_technical.md | knowledge_card | 4KB | Technical/engineering direct mapping |
| UPDATE | N04_knowledge/P01_knowledge/kc_lens_index.md | knowledge_card | +2KB | Add bible, car, technical columns |
| UPDATE | N05_operations/P09_config/media_config.yaml | config | +0.5KB | Add bible, car, technical to lenses section |

Dependencies: None. Wave 1 is self-contained.

### Wave 2: Course Modules (4 artifacts)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | _courses/driver/01_structured_thinking.md | course_module | 6KB | Brain organization concept, 7 lens hooks |
| CREATE | _courses/driver/02_seven_sins.md | course_module | 6KB | Constraint = excellence, 7 lens hooks |
| CREATE | _courses/driver/03_twelve_pillars.md | course_module | 6KB | Organization concept, 7 lens hooks |
| CREATE | _courses/driver/04_naming_things.md | course_module | 6KB | Taxonomy concept, 7 lens hooks |

Dependencies: Wave 1 (lens KCs must exist for reference).

### Wave 3: Pipeline Validation (1 test run)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| TEST | _output/courses/driver/01_structured_thinking/ | output | varies | Dry-run cex_media_produce.py with Module 1 |
| UPDATE | N05_operations/P09_config/concept_registry.yaml | config | +1KB | Add 4 course concepts if pipeline works |

Dependencies: Wave 2 (modules must exist to generate from).

## Module Outline (lens-agnostic core)

### Module 1: Structured Thinking
- **Concept**: Your brain (AI) already knows things -- it just has no system
- **Source**: kc_cex_cortex_enterprise, 8F pipeline
- **Learning objective**: Understand that AI output quality depends on process, not prompt length
- **Key takeaway**: 8 steps turn chaos into professional output

### Module 2: Seven Sins
- **Concept**: Constraint is not limitation -- it is specialization
- **Source**: kc_artificial_sins, nucleus_def_n01..n07
- **Learning objective**: Understand why a focused AI beats a generalist
- **Key takeaway**: Choose your AI's personality bias deliberately

### Module 3: Twelve Pillars
- **Concept**: Organization multiplies intelligence
- **Source**: mentor_context.md Section 2, _schema.yaml files
- **Learning objective**: See that 12 categories cover ALL knowledge an AI needs
- **Key takeaway**: If you can name the category, you can find (and reuse) anything

### Module 4: Naming Things
- **Concept**: Taxonomy = findability = reusability
- **Source**: mentor_context.md Section 3, kinds_meta.json
- **Learning objective**: Understand that naming things precisely is 80% of AI quality
- **Key takeaway**: 293 names for 293 types of output -- nothing unnamed, nothing lost

## Acceptance Criteria

- [ ] 3 new lens KCs pass compilation
- [ ] 4 course modules have valid frontmatter (kind: course_module)
- [ ] All content in PT-BR (Driver tier)
- [ ] Zero code in any module
- [ ] Each module references source KCs by path
- [ ] Each module has 7 lens hook sections
- [ ] media_config.yaml updated with 3 new lenses
- [ ] concept_registry.yaml updated with course concepts (if Wave 3 passes)
- [ ] All artifacts have quality: null

## Nucleus Assignments

| Wave | Nucleus | Role |
|------|---------|------|
| W1 | N04 (knowledge) | Create lens KCs |
| W2 | N02 (marketing) | Write course content in PT-BR |
| W3 | N05 (operations) | Pipeline validation |

N07 orchestrates all waves. N07 does NOT write content directly.
