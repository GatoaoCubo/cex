---
id: hybrid_review3_n01_aci
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: agent_computer_interface (N01)"
version: 1.0.0
quality: 8.9
tags: [audit, hybrid_review3, agent_computer_interface, gemma4, wave2]
domain: AI research quality assurance
created: "2026-04-14"
author: n01_intelligence
tldr: "agent_computer_interface builder: 7 defects found across 13 ISOs (gemma4:26b Wave 2). 6 fixed (D02, D03, D08, D09, D10, D15), final score 13/13 PASS."
---

# HYBRID_REVIEW3 Audit: agent_computer_interface

## Scope
| Attribute | Value |
|-----------|-------|
| Builder | agent-computer-interface-builder |
| ISOs audited | 13 |
| Source model | gemma4:26b (Wave 2) |
| Audit date | 2026-04-14 |
| Auditor | N01 (claude-sonnet-4-6) |
| Validator result | 13/13 PASS after fixes |

## Defect Inventory

| ISO | Defect Code | Severity | Pre-Fix Score | Action | Post-Fix Score |
|-----|------------|----------|--------------|--------|---------------|
| bld_memory | D02: kind=learning_record | CRITICAL | 5.0 | Surgical fix: kind -> memory | 8.5 |
| bld_quality_gate | D03: runtime metrics; truncated at 40 lines | CRITICAL | 2.0 | Full rebuild | 8.8 |
| bld_schema | Truncated: only 2 required fields | CRITICAL | 2.0 | Full rebuild | 9.0 |
| bld_architecture | D09: generic team names (Schema_Gen, Action_Mapper) | HIGH | 4.0 | Full rebuild: 13-ISO layout + dependency graph | 9.0 |
| bld_examples | Corrupted at line 47 (-3 error code truncation) | HIGH | 4.5 | Full rebuild: golden+anti-patterns | 9.0 |
| bld_knowledge_card | Truncated at line 29 (Key Concepts table cut off) | MEDIUM | 4.0 | Full rebuild: added protocol reference, boundaries | 9.0 |
| bld_output_template | D08: bare {{placeholders}} no guidance prose | HIGH | 6.5 | Surgical fix: added "Copy this template" + section guides | 8.8 |
| bld_instruction | D10: SCHEMA.md / OUTPUT_TEMPLATE.md refs | HIGH | 7.0 | Surgical fix: correct ISO filenames | 8.5 |
| bld_collaboration | D15: generic names (System Architect, etc.) | LOW | 7.5 | Surgical fix: real CEX builders | 8.5 |
| bld_system_prompt | PASS | - | 8.5 | None | 8.5 |
| bld_tools | PASS | - | 8.5 | None | 8.5 |
| bld_manifest | PASS | - | 8.0 | None | 8.0 |
| bld_config | PASS | - | 7.5 | None | 7.5 |

## Defect Pattern Analysis

### What gemma4:26b got right (ACI)
- bld_system_prompt: llm_function=BECOME (D01 avoided) -- unusual, most builders fail this
- bld_tools: referenced real CEX tool commands (cex_retriever.py, cex_doctor.py)
- bld_manifest: solid identity and capability description
- bld_collaboration: boundary section was correct (NOT browser_tool, NOT computer_use)

### What gemma4:26b got wrong (ACI)
- **Truncation pattern**: 3 ISOs (schema, quality_gate, knowledge_card) were truncated mid-content
  - Root cause: gemma4 context window management -- longer ISOs were cut off by token budget
  - schema: 24 lines, only 2 required fields (should be ~50+ lines with full spec)
  - quality_gate: SOFT scoring started at line 40 then was cut -- file ends mid-row
  - knowledge_card: 29 lines, Key Concepts table cut off mid-sentence
- **D09 architecture**: Described a production deployment team (Schema_Gen team, Vision-Ops) rather than the 13-ISO builder structure
- **D08 output_template**: Bare {{placeholders}} with no prose guidance -- users get no instructions
- **D02 memory**: kind=learning_record (universal gemma4 error)

### Comparison: gemma4 vs qwen3 for ACI
| Metric | gemma4:26b | qwen3:8b/14b |
|--------|-----------|-------------|
| D01 system_prompt INJECT | AVOIDED | Present in 80%+ |
| D02 memory kind | Present | Present (universal) |
| Truncation risk | HIGH (3 ISOs) | LOW |
| Domain accuracy | Medium (team-role drift) | Medium (financial drift) |
| Tools hallucination (D07) | Avoided | Present in 40% |

gemma4 introduced a NEW defect pattern (truncation) not seen in qwen3 audits. This is worse than
D01 because truncation leaves ISOs silently incomplete rather than wrong.

## D5 Scoring (Final)
| Dimension | Score |
|-----------|-------|
| D1 Structural completeness | 9.0 (13/13 PASS after fixes) |
| D2 Domain accuracy | 8.5 (ACI content is correct; minor protocol gaps before fixes) |
| D3 Density | 8.5 (all rebuilt ISOs target >= 0.85) |
| D4 CEX compliance | 8.5 (8F references, correct llm_functions after D01 check) |
| D5 Industry alignment | 8.5 (MCP, AutoGen, LangGraph, JSON-RPC cited in KC) |
| **OVERALL** | **8.6** |
