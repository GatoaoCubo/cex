# Self-Build Consolidated Report — Wave 6C
**Date**: 2026-03-28 | **Executor**: EDISON (Opus 4.6) | **Wave**: 6C
**Pipeline**: Motor 8F -> Crew Runner (dry-run) -> LLM Generation -> compare_builders.py

---

## Builder Results

| Builder | Complexity | Structural | Fields | Content | Size Delta | Verdict |
|---------|-----------|-----------|--------|---------|------------|---------|
| signal-builder | Simple | 100.0% | 100.0% | 0.98 | +0.4% | **PASS** |
| env-config-builder | Simple | 100.0% | 100.0% | 1.00 | +0.0% | **PASS** |
| quality-gate-builder | Medium | 100.0% | 100.0% | 0.95 | +3.0% | **PASS** |
| knowledge-card-builder | Medium | 100.0% | 100.0% | 1.00 | +0.1% | **PASS** |
| agent-builder | Complex | 100.0% | 100.0% | 0.94 | +0.1% | **PASS** |
| director-builder | Meta | 85.4% | 75.3% | 0.38 | +10.5% | **FAIL** |

## Summary
- **Total**: 6 builders tested
- **Pass**: 5 | Warn: 0 | Fail: 1
- **Average structural similarity**: 97.6%
- **Average field coverage**: 95.9%
- **Average content similarity**: 0.88
- **Conclusion**: CEX **can** self-build with quality >= 9.0 for Simple, Medium, and Complex builders. Meta builders (director) fail content similarity due to unique orchestration vocabulary.

---

## Per-Builder Detail

### 1. signal-builder (Simple) — PASS
- 13/13 files PASS
- Perfect structural and field scores
- Minor content delta in instruction file (0.84) due to Phase 2 step reorganization
- **Baseline validated**: simplest builder reconstructs near-perfectly

### 2. env-config-builder (Simple) — PASS
- 13/13 files PASS
- All metrics at ceiling (1.0 content, 0% size delta)
- Config-type builder (key=value schema) reconstructs identically
- **CONSTRAIN function validated**: env-config's restrictive schema aids reproduction

### 3. quality-gate-builder (Medium) — PASS
- 11/13 PASS, 2/13 WARN
- WARNs: manifest (content=0.60, paraphrased capabilities), output_template (size_delta=26.4%, expanded template)
- All structural and field scores at 100%
- **Self-referential recursion**: quality-gate-builder building quality gates about quality — no confusion detected

### 4. knowledge-card-builder (Medium) — PASS
- 13/13 files PASS
- Near-perfect across all metrics (content min=0.96)
- Abundant corpus references helped precision — the most-documented type reconstructs best
- **Corpus effect confirmed**: more examples in training = more faithful reconstruction

### 5. agent-builder (Complex) — PASS
- 12/13 PASS, 1/13 WARN
- WARN: manifest (content=0.62, different capability phrasing)
- Despite 30+ fields (most complex schema), structural and field coverage remained 100%
- **Complexity ceiling not reached**: even the most complex standard builder passes

### 6. director-builder (Meta) — FAIL
- 0/13 PASS, 1/13 WARN, 12/13 FAIL
- **Root cause**: content similarity collapsed (mean=0.38) — the agent generated structurally correct files but used generic orchestration language instead of CEX-specific vocabulary
- Structural similarity held (85.4% mean) — the 13-file template pattern transfers
- Field coverage dropped (75.3%) — director has unique fields (crew_composition, dag_edges, builder_registry) that the agent substituted with generic equivalents
- **Key insight**: meta-builders reference OTHER builders by name, creating a vocabulary dependency that generic reconstruction cannot satisfy

---

## Gap Analysis: Why director-builder Failed

| Gap | Metric Impact | Root Cause | Recommended Fix |
|-----|--------------|------------|-----------------|
| CEX-specific vocabulary | Content < 0.55 | Agent used generic terms ("orchestrator", "coordinator") instead of CEX terms ("crew", "DAG node", "builder registry") | Inject builder taxonomy as seed context in crew runner |
| Unique field names | Fields < 80% | `crew_composition`, `dag_edges`, `builder_registry` not in generic vocabulary | Add field glossary to meta-template injection |
| Template structure drift | Structural < 85% in 3 files | Output template and config have director-specific sections not in standard pattern | Add meta-builder section catalog to _builder-builder |
| Cross-reference density | Content spread | Director files name 10+ other builders; generic reconstruction cannot reproduce those names | Inject SUBAGENT_CATALOG or builder list as context |

## Conclusion

The self-build pipeline (Motor 8F -> Crew Runner -> LLM Generation -> Comparison) **works** for all standard complexity tiers:
- **Simple** (signal, env-config): near-perfect reconstruction (content > 0.98)
- **Medium** (quality-gate, knowledge-card): high fidelity with minor paraphrase variance (content > 0.95)
- **Complex** (agent): high fidelity despite 30+ fields (content > 0.94)
- **Meta** (director): **structural transfer works** but content fidelity requires CEX-specific vocabulary injection

### Actionable Next Steps
1. **Inject builder taxonomy** into crew runner prompts for meta-builder reconstruction
2. **Add field glossary** to _builder-builder meta-templates
3. **Re-test director-builder** with enriched context (Wave 6D candidate)
4. **Consider**: meta-builders may need a dedicated meta-template variant

---

*SELF_BUILD_CONSOLIDATED.md — EDISON Wave 6C | CEX v1.0.0 | 2026-03-28*
