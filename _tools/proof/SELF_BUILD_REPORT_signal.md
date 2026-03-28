# Self-Build Report: signal-builder
**Date**: 2026-03-28 | **Executor**: EDISON (LLM) | **Wave**: 6C

## File-Level Results

| File | Structural | Fields | Content | Size Delta | Quality 5D | Verdict |
|------|-----------|--------|---------|------------|------------|---------|
| bld_manifest_signal.md        | 100% | 100% | 0.91 | +2.9% | - | PASS |
| bld_system_prompt_signal.md   | 100% | 100% | 0.98 | +0.8% | - | PASS |
| bld_knowledge_card_signal.md  | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_instruction_signal.md     | 100% | 100% | 0.84 | +1.5% | - | PASS |
| bld_tools_signal.md           | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_output_template_signal.md | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_schema_signal.md          | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_examples_signal.md        | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_architecture_signal.md    | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_config_signal.md          | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_memory_signal.md          | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_quality_gate_signal.md    | 100% | 100% | 1.00 | +0.0% | - | PASS |
| bld_collaboration_signal.md   | 100% | 100% | 1.00 | +0.0% | - | PASS |

## Aggregate

| Metric | Mean | Min | Max |
|--------|------|-----|-----|
| Structural similarity | 100% | 100% | 100% |
| Field coverage | 100% | 100% | 100% |
| Content similarity | 0.98 | 0.84 | 1.00 |
| Size delta | 0.4% | 0.0% | 2.9% |
| Quality 5D | - | - | - |

## Summary

**Overall**: 13/13 PASS | 0/13 WARN | 0/13 FAIL
**Verdict**: PASS

## Notable Gaps

None. All 13 files passed all 4 automated metrics with high margins.

The minor content similarity drop in `bld_instruction_signal.md` (0.84) is due to
slight restructuring of Phase 2 compose steps — the signal payload field list
was reorganized but all fields are present. Still well above the 0.70 PASS threshold.

## Reviewer Notes

Signal-builder is the simplest builder in the test matrix (fewest fields, JSON format,
minimal body). The near-perfect reconstruction validates that the meta-template pattern
produces consistent output for simple builders. This establishes the baseline for
comparing against more complex builders.
