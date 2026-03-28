# CEX Compile Report

**Date**: 2026-03-28
**Tool**: `_tools/cex_compile.py --all`
**Status**: PASS (194/194 compiled, 353/353 validated)

---

## Compilation Results

| Pillar | Examples | Compiled | Status |
|--------|----------|----------|--------|
| P01_knowledge | 85 | 85 | OK |
| P02_model | 16 | 16 | OK |
| P03_prompt | 17 | 17 | OK |
| P04_tools | 16 | 16 | OK |
| P05_output | 5 | 5 | OK |
| P06_schema | 9 | 9 | OK |
| P07_evals | 8 | 8 | OK |
| P08_architecture | 6 | 6 | OK |
| P09_config | 6 | 6 | OK |
| P10_memory | 9 | 9 | OK |
| P11_feedback | 8 | 8 | OK |
| P12_orchestration | 9 | 9 | OK |
| **Total** | **194** | **194** | **OK** |

## Validation Results

| Pillar | Compiled Files | Valid | Status |
|--------|---------------|-------|--------|
| P01 | 160 | 160 | OK |
| P02 | 28 | 28 | OK |
| P03 | 24 | 24 | OK |
| P04 | 29 | 29 | OK |
| P05 | 10 | 10 | OK |
| P06 | 17 | 17 | OK |
| P07 | 14 | 14 | OK |
| P08 | 11 | 11 | OK |
| P09 | 11 | 11 | OK |
| P10 | 17 | 17 | OK |
| P11 | 15 | 15 | OK |
| P12 | 17 | 17 | OK |
| **Total** | **353** | **353** | **OK** |

Note: 353 total includes 159 legacy compiled files (p01_* naming from prior run) + 194 current (ex_* naming). All are valid YAML/JSON.

## Errors Found + Fixed

None. Pipeline ran cleanly on first attempt.

## Pillars with Missing compiled/

None. All 12 pillars have compiled/ directories with valid outputs.

## ID/Kind Consistency

0 mismatches between source .md frontmatter and compiled output.

## Script Status

`cex_compile.py` handles:
- All 12 LP pillars (P01-P12)
- YAML and JSON output based on _schema.yaml machine_format
- Frontmatter parsing with date serialization
- Body section parsing (lists, code blocks, tables, prose)
- Output validation (re-parse after write)

No fixes needed for this run.
