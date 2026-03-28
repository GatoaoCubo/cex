---
title: Self-Build Test Protocol
status: SPEC
version: 1.0.0
author: PYTHA
created: 2026-03-28
wave: 6B
quality: 9.0
purpose: Defines metrics, acceptance criteria, test matrix, and report template for Wave 6C self-build validation
---

# Self-Build Test Protocol
**Wave 6C Preparation** | **PYTHA** | **v1.0.0**

> Wave 6C will test whether CEX can reconstruct its own builders (self-build).
> This protocol establishes the measurement framework BEFORE tests run,
> so results are objective and reproducible.

---

## 1.1 Comparison Metrics (Quantitative)

For each reconstructed file vs. its original, measure these 5 dimensions:

### Structural Similarity
**Definition**: % of `##` section headers from the original that appear in the reconstructed file, in the same relative order.

**Algorithm**:
1. Extract all `##` headers from original → ordered list `O`
2. Extract all `##` headers from reconstructed → ordered list `R`
3. Compute longest common subsequence (LCS) of `O` and `R` (normalized text, lowercase, stripped)
4. `structural_similarity = len(LCS) / len(O) * 100`

**Why order matters**: A builder where SCHEMA appears after EXAMPLES violates the dependency contract (Section: Dependency Order in `_builder-builder/README.md`).

---

### Field Coverage
**Definition**: % of fields defined in the original's frontmatter + body sections that are present in the reconstructed file.

**Algorithm**:
1. Parse frontmatter YAML: collect all keys → set `F_orig`
2. Parse body sections: collect all `| Field |` table rows and `{{variable}}` slots → set `B_orig`
3. Total fields: `T_orig = F_orig ∪ B_orig`
4. Repeat for reconstructed file → `T_new`
5. `field_coverage = |T_orig ∩ T_new| / |T_orig| * 100`

**Note**: Field names are normalized (lowercase, hyphens→underscores) before comparison.

---

### Content Similarity
**Definition**: Jaccard similarity of token sets between original and reconstructed body text (frontmatter excluded, stopwords removed).

**Algorithm**:
1. Extract body text (below `---` second fence)
2. Tokenize: split on whitespace + punctuation → lowercase tokens
3. Remove stopwords: `{a, o, e, de, da, do, para, com, que, em, se, por, um, uma, no, na, os, as, ou}`
4. Build token sets `A` (original) and `B` (reconstructed)
5. `content_similarity = |A ∩ B| / |A ∪ B|`

**Range**: 0.0 (no overlap) to 1.0 (identical token sets)

**Why Jaccard, not cosine**: No heavy dependencies (numpy/sklearn not required). Works on token sets, suitable for structured markdown.

---

### Size Delta
**Definition**: Relative byte difference between reconstructed and original file.

**Formula**:
```
size_delta = |bytes_new - bytes_orig| / bytes_orig * 100
```

Expressed as a percentage (unsigned). A value of 0% = identical size; 50% = half or double the original.

---

### Quality Score (5D Rubric)
**Definition**: Manual scoring across 5 dimensions, scored 1-10 each, averaged.

| Dimension | What to Evaluate |
|-----------|-----------------|
| **Density** | Information per line. No padding, no filler phrases. |
| **Correctness** | Fields match the schema. No hallucinated constraints or invented examples. |
| **Structure** | Sections in the right order. Headers present. Tables well-formed. |
| **Actionability** | Instructions are executable. Examples are runnable. Gates are checkable. |
| **Specificity** | Values are concrete (not "some string" but `p12_sig_{event}.json`). |

`quality_5d = (density + correctness + structure + actionability + specificity) / 5`

Quality is **not automated** — requires LLM or human reviewer per file.

---

## 1.2 Acceptance Criteria (Pass / Warn / Fail)

| Metric | Pass | Warn | Fail | Justification |
|--------|------|------|------|---------------|
| Structural similarity | >= 85% | 70–84% | < 70% | Provided in handoff spec. 85% allows 1-2 minor renamed headers in a 13-section file. |
| Field coverage | >= 90% | 80–89% | < 80% | Provided in handoff spec. A missing required field (e.g., `satellite` in signal) is a hard defect. |
| Content similarity | >= 0.70 | 0.55–0.69 | < 0.55 | LLMs naturally paraphrase; Jaccard 0.70+ means shared vocabulary dominates. Below 0.55 signals conceptual drift or topic substitution. |
| Size delta | <= 20% | 20–35% | > 35% | Simple builders ~400 lines; ±20% (±80 lines) is normal template variance. >35% indicates truncation (too short) or hallucinated expansion (too long). |
| Quality 5D | >= 9.0 | 8.0–8.9 | < 8.0 | Provided in handoff spec. CEX quality standard: 9.0+ for pool eligibility. |

### Aggregate Verdict Rules

| Condition | File Verdict |
|-----------|-------------|
| ALL metrics Pass | **PASS** |
| 1+ metrics Warn, 0 Fail | **WARN** |
| 1+ metrics Fail (any) | **FAIL** |

### Builder-Level Verdict (from 13 files)

| Condition | Builder Verdict |
|-----------|----------------|
| >= 11/13 files PASS, 0 FAIL | **PASS** |
| >= 10/13 files PASS or WARN, <= 2 FAIL | **WARN** |
| > 2 files FAIL | **FAIL** |

**Why 11/13 threshold?** Two files (MEMORY.md and COLLABORATION.md) have high paraphrase variance by design — they contain experiential patterns and crew compositions that an LLM may legitimately express differently while remaining correct. These are candidates for WARN without blocking overall PASS.

---

## 1.3 Test Matrix (6 Builders)

| # | Builder | Complexity | Files | Field Count | Justification |
|---|---------|-----------|-------|-------------|---------------|
| 1 | `signal-builder` | Simple | 13 | 11 (4 req + 7 opt) | Fewest fields, JSON format, minimal body. Baseline sanity test. |
| 2 | `env-config-builder` | Simple | 13 | ~12 | Config type edge case: key=value schema, no body sections beyond table. Tests CONSTRAIN function. |
| 3 | `quality-gate-builder` | Medium | 13 | ~18 | Moderate structure. Quality domain is self-referential (the gate evaluates quality). Tests recursion awareness. |
| 4 | `knowledge-card-builder` | Medium | 13 | ~22 | Core CEX type. Most examples exist in corpus. Tests whether abundant references help or confuse reconstruction. |
| 5 | `agent-builder` | Complex | 13 | ~30 (18 frontmatter + 11 body sections) | Most fields, multiple object types, rich body. Stress test for field coverage. |
| 6 | `director-builder` | Meta | 13 | ~25 | Orchestrates other builders. Tests whether the model understands recursive builder invocation without looping. |

**Execution order**: 1 → 2 → 3 → 4 → 5 → 6 (ascending complexity, results inform next test).

---

## 1.4 Test Execution Steps

For each builder in the matrix, follow this sequence:

```
Step 1 — DECOMPOSE
  Motor 8F receives: "reconstroi o {builder}"
  Motor applies Edge Case 4.3 (Intent Meta):
    - verb: "reconstroi", object: "{builder}", domain: "meta"
    - Activates _builder-builder as primary in BECOME
  Output: execution_plan.json

Step 2 — DRY-RUN
  Crew Runner receives execution_plan.json with --dry-run flag
  For each active builder in the plan:
    - Renders the prompt (META_{FILE}.md + schema + seeds)
    - Writes prompt to: _tools/dry_run/{builder}/{file_name}.prompt.txt
  Output: 13 prompt files per builder (no LLM calls made)

Step 3 — EXECUTE
  Option A (automated): Crew Runner --execute reads each .prompt.txt,
    calls LLM (sonnet), writes output to: _tools/output/{builder}/{file_name}.md
  Option B (manual): Human pastes each prompt to LLM and saves output

Step 4 — COMPARE
  Run: python _tools/compare_builders.py \
    --original archetypes/builders/{builder}/ \
    --generated _tools/output/{builder}/
  Output: comparison_report_{builder}.json

Step 5 — CALCULATE
  Script computes all 4 automated metrics per file (structural, fields, content, size_delta)
  Quality 5D: manual scoring by reviewer per file

Step 6 — REPORT
  Populate report template (Section 1.5) with metric values
  Apply acceptance criteria (Section 1.2) per file and per builder

Step 7 — ACCEPT / REJECT
  PASS: builder moves to Wave 6D (deployment)
  WARN: document gaps, proceed with caveat
  FAIL: escalate to EDISON for schema analysis before retry
```

### Dependencies Between Steps

```
Step 1 (Motor 8F) ──────► Step 2 (Dry-run) ──────► Step 3 (Execute)
                                                           │
                                                           ▼
Step 6 (Report) ◄──── Step 5 (Calculate) ◄──── Step 4 (Compare)
                                                           │
                                                           ▼
                                                    Step 7 (Verdict)
```

---

## 1.5 Report Template

```markdown
# Self-Build Report: {builder}
**Date**: {YYYY-MM-DD} | **Executor**: {human|LLM} | **Wave**: 6C

## File-Level Results

| File | Structural | Fields | Content | Size Delta | Quality 5D | Verdict |
|------|-----------|--------|---------|------------|------------|---------|
| bld_manifest_{type}.md    | ?% | ?% | 0.?? | +?% | ?.? | PASS/WARN/FAIL |
| bld_system_prompt_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_knowledge_card_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_instruction_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_tools_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_output_template_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_schema_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_examples_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_architecture_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_config_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_memory_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_quality_gate_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |
| bld_collaboration_{type}.md | ?% | ?% | 0.?? | +?% | ?.? | ? |

## Aggregate

| Metric | Mean | Min | Max |
|--------|------|-----|-----|
| Structural similarity | ?% | ?% | ?% |
| Field coverage | ?% | ?% | ?% |
| Content similarity | 0.?? | 0.?? | 0.?? |
| Size delta | ?% | ?% | ?% |
| Quality 5D | ?.? | ?.? | ?.? |

## Summary

**Overall**: ?/13 PASS | ?/13 WARN | ?/13 FAIL
**Verdict**: {PASS|WARN|FAIL}

## Notable Gaps (if WARN or FAIL)

- File: {file} | Metric: {metric} | Expected: {threshold} | Got: {value}
- Root cause hypothesis: {brief analysis}
- Recommended action: {fix schema | fix template | adjust threshold | escalate to EDISON}

## Reviewer Notes

{freeform observations about content quality, correctness, surprising differences}
```

---

*SELF_BUILD_PROTOCOL.md — PYTHA Wave 6B | CEX v1.0.0 | 2026-03-28*
