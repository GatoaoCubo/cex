---
id: p01_kc_systematic_debugging
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Systematic Debugging — 4-Phase Root Cause Methodology"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: debugging
quality: 9.1
tags: [debugging, root-cause, systematic-process, defense-in-depth, condition-based-waiting]
tldr: "4-phase debugging (root cause, pattern, hypothesis, implementation) with iron law: no fix without investigation first"
when_to_use: "Bug found — before any fix attempt, follow this systematic process"
keywords: [systematic-debugging, root-cause-analysis, defense-in-depth, flaky-tests, hypothesis-testing]
long_tails:
  - "How to debug systematically without thrashing or trial and error"
  - "When to stop trying fixes and question the architecture"
axioms:
  - "NEVER fix without root cause investigation first"
  - "ALWAYS test ONE hypothesis at a time with minimal change"
  - "NEVER accumulate multiple fixes simultaneously"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_reason]
density_score: null
data_source: "https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/"
related:
  - p12_wf_auto_diagnose
  - p03_sp_debug_ops
  - p01_kc_feedback_loops
  - p12_wf_auto_debug
  - n01_hybrid_review_wave1
  - p10_lr_bugloop_builder
  - p01_kc_self_healing_skill
  - p01_kc_skill_format_universal
---

## Summary

4-phase debugging methodology that raises first-time fix rate from 40% (random) to 95% (systematic).
Average time drops from 2-3h (thrashing) to 15-30min (structured process).
Iron law: no fix without root cause investigation first.
4 support techniques: root cause tracing, defense-in-depth (4 validation layers), condition-based waiting (eliminates flaky tests -- 60% to 100% pass rate) and test pressure levels.
Critical rule: 3+ failed fixes = architectural problem, not isolated bug.

## Spec

| Phase | Activity | Exit Criteria |
|-------|----------|---------------|
| 1. Root Cause | Read errors, reproduce, check changes, instrument | Understand WHAT and WHY |
| 2. Pattern | Find working examples, compare line by line | Identify differences |
| 3. Hypothesis | Formulate ONE theory, test with minimal change | Confirmed or new hypothesis |
| 4. Implementation | Create failing test, fix root cause, verify | Bug resolved, tests pass |

| Metric | Random | Systematic |
|--------|--------|------------|
| Average time | 2-3h | 15-30min |
| First-time fix rate | 40% | 95% |
| Fix threshold | -- | >= 3 failures = architectural problem |

| Support Technique | When to Use | Result |
|-------------------|-------------|--------|
| Root Cause Tracing | Error deep in call stack | Fix at source, not symptom |
| Defense-in-Depth | After root cause found | Bug becomes structurally impossible |
| Condition-Based Waiting | Tests with setTimeout/sleep | 15 flaky tests fixed, 40% faster |
| Test Pressure Levels | Train process under pressure | Systematic process beats thrashing |

Defense-in-depth: Entry Point (validar input) → Business Logic (validar semantica) → Environment Guards (NODE_ENV) → Debug Instrumentation (logging forense).

## Patterns

| Trigger | Action |
|---------|--------|
| Bug found | Phase 1: read complete errors, reproduce, git diff |
| Error in multi-component system | Instrument each boundary: log input and output |
| Root cause identified | Phase 3: ONE hypothesis, ONE change, test |
| Fix failed 3+ times | STOP -- question architecture with human |
| Flaky tests with setTimeout | Replace with condition-based waiting |
| Bug fixed | Defense-in-depth: 4 layers make bug impossible |

## Anti-Patterns

- "It's probably X, let me fix that" -- assume without verifying
- "Quick fix for now, investigate later" -- the problem returns
- "Just try changing X and see" -- thrashing without hypothesis
- Accumulate multiple fixes and test together -- impossible to isolate
- Fix where the error appears, not where it originates (symptom vs cause)

## Code

<!-- lang: typescript | purpose: condition-based waiting replaces flaky setTimeout -->
```typescript
async function waitFor<T>(
  condition: () => T | undefined,
  description: string,
  timeoutMs = 5000
): Promise<T> {
  const start = Date.now();
  while (true) {
    const result = condition();
    if (result) return result;
    if (Date.now() - start > timeoutMs)
      throw new Error(`Timeout: ${description} (${timeoutMs}ms)`);
    await new Promise(r => setTimeout(r, 10));
  }
}

// Antes: await new Promise(r => setTimeout(r, 50));
// Depois: await waitFor(() => getResult(), "result ready");
// Resultado: 15 flaky tests fixados, 60% -> 100% pass rate
```

```bash
# Root cause tracing: instrument boundary
echo "DEBUG: input=$input cwd=$(pwd)" >> /tmp/debug.log
# Trace upward to the source -- fix there, not at the symptom
```

## References

- source: https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/
- source: https://wizardzines.com/zines/debugging-guide/
- related: p01_kc_cex_function_reason

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_diagnose]] | downstream | 0.23 |
| [[p03_sp_debug_ops]] | downstream | 0.23 |
| [[p01_kc_feedback_loops]] | sibling | 0.22 |
| [[p12_wf_auto_debug]] | downstream | 0.21 |
| [[n01_hybrid_review_wave1]] | related | 0.18 |
| [[p10_lr_bugloop_builder]] | downstream | 0.17 |
| [[p01_kc_self_healing_skill]] | sibling | 0.15 |
| [[p01_kc_skill_format_universal]] | sibling | 0.15 |
