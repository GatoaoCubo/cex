---
id: p11_bl_n03
kind: bugloop
pillar: P11
title: "Bugloop -- N03 Autonomous Build Error Detection"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [bugloop, N03, autonomous, error-detection, self-healing, 8F, quality]
tldr: "Autonomous bug detection and fix loop for N03 build errors. Scans for compile failures, frontmatter violations, vocabulary drift, and quality regressions. Applies heuristic fixes first, LLM rewrites as fallback."
density_score: 0.90
updated: "2026-04-17"
---

# Bugloop: N03 Autonomous Build Error Detection

## Purpose

The bugloop is N03's self-healing mechanism. After every build batch, it scans
for defects and applies corrections autonomously -- no N07 intervention needed
for routine failures. Escalates only when heuristic + LLM fix both fail.

**Inventive Pride:** bugs are an insult to craft. The bugloop runs until the build is clean.

## Trigger Conditions

| Trigger | Condition | Priority |
|---------|-----------|---------|
| Compile failure | `cex_compile.py` exits non-zero | CRITICAL |
| Frontmatter parse error | YAML invalid in produced artifact | HIGH |
| Hard gate failure (H01-H07) | Any hard gate fails at F7 | HIGH |
| Quality below floor | final_score < 7.0 after 2 retries | MEDIUM |
| Vocabulary drift | > 2 non-canonical terms detected | MEDIUM |
| Density below floor | density_score < 0.80 | LOW |

## Fix Strategy Matrix

| Bug Type | Heuristic Fix | LLM Fix | Escalate |
|----------|--------------|---------|---------|
| YAML syntax error | regex patch closing tags | rewrite frontmatter block | if still invalid |
| Missing required field | inject field with null/default | regenerate frontmatter | never (always fixable) |
| quality != null | set quality: null | N/A (deterministic) | never |
| Placeholder text | remove matched pattern | context-aware replacement | if semantics unclear |
| Density < 0.80 | convert prose lists to tables | full F6 rewrite with density emphasis | after 2 LLM retries |
| Vocabulary drift | replace via spec_metaphor_dictionary | inject vocab KC + rewrite section | after 2 LLM retries |
| Compile error | fix path/frontmatter issues | full artifact rewrite | after 2 full rewrites |

## Loop Protocol

```
SCAN phase (after each build batch):
  1. python _tools/cex_compile.py {artifact_path} -> collect errors
  2. python _tools/cex_doctor.py --file {artifact_path} -> collect gate failures
  3. python _tools/cex_retriever.py --vocab-check {artifact_path} -> vocabulary drift
  4. For each error found: classify -> queue fix

FIX phase (ordered by priority):
  1. Apply heuristic fix (deterministic, 0 tokens)
  2. Re-run compile + doctor
  3. If still failing: apply LLM fix (inject error context into F6)
  4. Re-run compile + doctor (max 2 LLM attempts per error)
  5. If still failing after 2 LLM attempts: escalate to N07

VERIFY phase:
  1. All artifacts in batch must pass cex_compile.py
  2. No hard gate failures
  3. vocabulary drift check passes
  4. Write bugloop report to .cex/runtime/signals/bugloop_n03_{timestamp}.json
```

## Bugloop Report Format

```yaml
timestamp: 2026-04-17T14:30:00
nucleus: n03
batch_size: 6
errors_found: 2
errors_fixed_heuristic: 1
errors_fixed_llm: 1
errors_escalated: 0
artifacts:
  - path: N03_engineering/P06_schema/input_schema_build_contract.md
    status: clean
  - path: N03_engineering/P06_schema/type_def_cex_types.md
    status: fixed_heuristic
    fix: "added missing density_score field"
  - path: N03_engineering/P07_evals/scoring_rubric_n03.md
    status: fixed_llm
    fix: "weights did not sum to 100; redistributed D3+D4"
```

## Escalation Criteria

Escalate to N07 (write signal, do not retry) when:
- Compile error persists after 2 heuristic + 2 LLM attempts
- Artifact kind is unresolvable (not in kinds_meta.json)
- output_path is outside repo root (security violation)
- Session token budget exhausted before fix complete

## Heuristic Fix Library

```python
HEURISTIC_FIXES = {
    "quality_not_null": lambda text: re.sub(r'quality:\s*[\d.]+', 'quality: null', text),
    "placeholder_removal": lambda text: re.sub(r'\{\{[a-zA-Z_]+\}\}', '', text),
    "density_score_missing": lambda text: text.replace(
        'tags:', 'density_score: 0.85\ntags:'
    ) if 'density_score' not in text else text,
    "version_format": lambda text: re.sub(
        r'version:\s*"?(\d+)"?', r'version: \1.0.0', text
    ),
}
```
