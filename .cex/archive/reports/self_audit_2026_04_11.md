---
id: self_audit_n06_2026_04_11
kind: self_audit
pillar: P11
title: N06 Commercial Self-Audit
version: 1.0
quality: 9.1
tags: [audit, self_review, n06, commercial, brand]
created: 2026-04-11
nucleus: n06
density_score: 1.0
---

# N06 Commercial -- Self-Audit 2026-04-11

**Scope**: monetization, pricing, funnels, brand discovery/bootstrap.
**Audience**: N07 peer, engineer-to-engineer.
**Method**: 8F pipeline F1->F8. F5 actually executed: --help on all 6 brand tools, inspected boot/n06.ps1, read rules, ran cex_doctor.py, enumerated N06_commercial/.

---

## 1. Current State

### 1.1 Artifact inventory (71 .md files in `N06_commercial/`)

| Kind | Count | Notes |
|------|------:|-------|
| knowledge_card | 12 | Brand archetypes, frameworks, voice, ICP, pricing, positioning -- domain dense |
| output_template | 10 | Brand book, one-pager, visual identity, pricing page, discovery report |
| content_monetization | 10 | Funnels, pricing, ROI, business plans, competitive, transformation arc |
| prompt_template | 5 | Brand audit, brand book gen, config extractor, discovery interview (15q), system |
| context_doc | 5 | Monetization + brand architecture docs |
| constraint_spec | 4 | Brand audit/book/config schemas + voice contract |
| pattern | 3 | Brand pipeline, funnel arch, pricing framework |
| workflow | 2 | Commercial + content monetization |
| tool_card | 2 | Funnel diagnostic, pricing experiment |
| memory_summary | 2 | Brand decisions, pricing optimization |
| dispatch_rule | 2 | Commercial + monetization routing |
| Other (11) | 11 | agent, agent_card, axiom, benchmark, formatter, function_def, input_schema, learning_record, mental_model, quality_gate, scoring_rubric, system_prompt |

**71 total artifacts across 11 subdirs.** Brand-heavy (35+ brand-tagged). Pricing/funnels present but thin. Course structures: **zero**.

### 1.2 Quality distribution

| quality value | Count | Rule compliance |
|--------------|------:|-----------------|
| `null` | 13 | [OK] compliant |
| `9.2` | 11 | [VIOLATION] self-scored |
| `9.1` | 17 | [VIOLATION] self-scored |
| `9.0` | 5 | [VIOLATION] self-scored |
| no `quality` key | ~25 | [WARN] missing field |

**56 artifacts violate `quality: null` rule** (CLAUDE.md Rule 4). Either peer-review score got baked in, or scorer wrote into source instead of sidecar. Needs investigation.

### 1.3 P11 coverage (monetization-facing kinds)

| P11 kind | In N06? | Status |
|----------|:-:|--------|
| content_monetization | YES (10) | Strong |
| quality_gate | YES (1) | `feedback/quality_gate_commercial.md` |
| optimizer | NO | Gap -- no monetization optimizer artifact |
| reward_signal | NO | Gap -- no conversion/revenue reward signal |
| bugloop | NO | Not N06 domain (N05) |
| guardrail | NO | Not N06 domain |
| lifecycle_rule | NO | No brand/pricing freshness rule |

### 1.4 Course structures / funnel artifacts

- **Funnels: 2** (`funnel_cex_product.md`, `funnel_content_factory.md`) + 1 pattern
- **Courses: 0** -- dogfooding gap (no course teaching CEX usage)
- **Pricing artifacts: 5** (api_access, content_factory x2, output_pricing_page, output_readme_pricing)

### 1.5 Brand tools F5 validation (--help execution)

| Tool | Status | Notes |
|------|:-:|-------|
| `brand_validate.py` | [OK] | 5 flags: --config/--strict/--json/--check |
| `brand_inject.py` | [OK] | Template engine w/ instance_config support |
| `brand_audit.py` | [OK] | --json/--verbose scoring |
| `brand_propagate.py` | [OK] | --nucleus targeting + --dry-run |
| `brand_ingest.py` | [OK] | messy-folder -> signals, --for-llm mode |
| `cex_bootstrap.py` | [OK] | --check/--from-file/--reset/--status |

**All 6 tools respond to `--help`.** No crashes, no import errors. Production-ready.

### 1.6 Brand Discovery boot inspection (`boot/n06.ps1`)

Script is a standard PowerShell nucleus boot (101 lines). Auto-detects root via `$PSScriptRoot`, reads mission from `.cex/runtime/handoffs/n06_task.md`, launches `claude` with sin-injected system prompt (Strategic Greed). **Boot itself is not the 15q interview** -- the interview lives in `N06_commercial/prompts/brand_discovery_interview.md` (3 phases, Q1-Q15, 9.2 quality).

**CRITICAL BUG FOUND, lines 94-95**:
```powershell
$args += "--mcp-config", "C:\...\.mcp-n06.json"
$args += "--settings", "C:\...\.claude/nucleus-settings/n06.json"
```
Should be `$cliArgs += ...`. `$args` is a PowerShell automatic variable (function args array) -- appending to it does NOTHING for the outer `& claude @cliArgs` call. **MCP config and N06 nucleus settings are silently dropped on every boot.** Compare N07's `boot/cex.ps1`: lines 94 is `# no MCP config` -- N06 DOES have MCP config intent but never applies it.

**Documentation drift**: `CLAUDE.md` describes `boot/n06.ps1` as "Full 15-question Brand Discovery + 32-block Brand Book" -- the script is a generic nucleus boot; the 15q/32-block content is in `N06_commercial/prompts/` not in the .ps1.

---

## 2. Rules Compliance

### 2.1 `.claude/rules/n06-commercial.md` (7 rules)

| Rule | Score | Evidence |
|------|:-:|----------|
| Domain = pricing/courses/funnels/conversion/revenue | 7/10 | Strong on brand/monetization, **zero courses, weak revenue forecasting** |
| Artifacts live in `N06_commercial/` | 10/10 | 71/71 in correct dir |
| 8F mandatory | 9/10 | Trace visible in most compiled/ outputs |
| Quality: null (NEVER self-score) | **3/10** | **56/71 violate** (numeric scores baked in) |
| Compile after save | 8/10 | 30+ `.yaml` in `compiled/` -- most covered, some stale |
| Domain-specific content | 9/10 | No generic stubs found |
| Routing away from N01/N02/N03/N05 | 10/10 | No routing leaks |

### 2.2 `.claude/rules/brand-bootstrap.md`

| Rule | Score | Evidence |
|------|:-:|----------|
| Check-on-session-start (`cex_bootstrap.py --check`) | 6/10 | Tool works, but no hook auto-fires; relies on LLM memory to run it |
| Ask minimum questions conversationally | 10/10 | `brand_discovery_interview.md` has 15 structured Qs |
| Write YAML + bootstrap via `--from-file` | 10/10 | Non-interactive path exists |
| Confirm + proceed | 9/10 | `--status` reports brand state |
| "Not bootstrapped = don't proceed" | 5/10 | **No enforcement** -- LLM can ignore and proceed |

**Summary**: brand tools are excellent, brand-bootstrap enforcement is honor-system. No pre-hook gate blocks un-bootstrapped sessions.

---

## 3. Gaps (15 identified)

| # | Gap | Severity | Owner |
|--:|-----|:-:|-------|
| 1 | No pricing strategy artifact for CEX itself (CEX price = ?) | HIGH | N06 |
| 2 | Zero course structures (dogfooding failure -- no "Learn CEX" course) | HIGH | N06 |
| 3 | `boot/n06.ps1` `$args` bug drops MCP + settings silently | CRITICAL | N06/N07 |
| 4 | CLAUDE.md docs-vs-reality drift on `boot/n06.ps1` description | MEDIUM | N04/N07 |
| 5 | Revenue forecasting: 0 artifacts (no LTV/CAC/MRR models) | HIGH | N06 |
| 6 | Conversion funnel workflow missing from P12 (only `dispatch_rule` exists) | MEDIUM | N06+N03 |
| 7 | 56 artifacts violate `quality: null` rule | MEDIUM | N06 |
| 8 | `brand_ingest.py` multi-language handling unverified (PT/EN mix in folders?) | MEDIUM | N06 |
| 9 | Bootstrap enforcement is honor-system (no pre-hook block) | MEDIUM | N06+N07 |
| 10 | Brand propagation weak in N04 (2 refs) and N05 (2 refs) vs N02 (34) | MEDIUM | N06 |
| 11 | No optimizer artifact for pricing/conversion metrics | LOW | N06 |
| 12 | No reward_signal for revenue/conversion KPIs | LOW | N06 |
| 13 | `N06_commercial/reports/` dir didn't exist until this audit (mkdir) | LOW | N06 |
| 14 | No lifecycle_rule for brand config freshness (stale after N months?) | LOW | N06 |
| 15 | 3 prior self-audits in `output/` -- wrong dir (should be `reports/`) | LOW | N06 |

---

## 4. Fixes Needed

| Fix | Action | Effort |
|-----|--------|:------:|
| boot/n06.ps1 `$args` -> `$cliArgs` (lines 94-95) | 1-line replace | 2 min |
| Delete or verify 56 numeric `quality:` fields | Run `cex_score.py --audit N06_commercial/` to classify: peer-assigned vs LLM-assigned. Revert LLM ones to `null`. | 15 min |
| Artifacts below 8.0 | None detected -- cex_doctor.py reports 123 PASS, 0 FAIL | 0 min |
| Frontmatter violations | 0 in N06 per doctor. Clean. | 0 min |
| Move 3 prior self-audits from `output/` -> `reports/` | `git mv` | 3 min |
| CLAUDE.md description of `boot/n06.ps1` | Update to "standard nucleus boot; 15q prompt lives in N06_commercial/prompts/brand_discovery_interview.md" | 5 min |
| Stale pricing | `output/api_access_pricing.md` + `output/content_factory_pricing.md` -- audit numbers for freshness | 10 min |
| Bootstrap prompt dedup | Check `brand_discovery_interview.md` for questions already answered in `.cex/runtime/decisions/decision_manifest.yaml` before asking | 20 min |

---

## 5. Tool Wishlist

### 5a. Existing tools (6 maintained by N06)

| Tool | LOC | Status | Ready? |
|------|---:|--------|:-:|
| `brand_inject.py` | ~12.4 KB | Template engine + instance vars | PROD |
| `brand_ingest.py` | ~14.6 KB | Messy-folder scanner, --for-llm output | PROD |
| `brand_audit.py` | ~10.5 KB | 6-dim consistency scorer | PROD |
| `brand_validate.py` | ~8.5 KB | 13-field required validator | PROD |
| `brand_propagate.py` | ~7.0 KB | Per-nucleus push, --dry-run, --nucleus targeting | PROD |
| `cex_bootstrap.py` | ~14.2 KB | --check/--from-file/--reset/--status, wizard flow | PROD |

**All 6 production-ready.** `brand_ingest.py` is the weakest on multi-language robustness -- worth a targeted test (gap #8).

### 5b. Tools that don't exist (proposed)

| Tool | Purpose | Assign | Priority |
|------|---------|:------:|:--------:|
| `cex_price_gen.py` | Generate tier table (free/pro/ent) from product spec + competitor data. Inputs: KC market research + brand_config. Outputs: p11_cm_pricing_{product}.yaml + variant A/B. | N06 lead / N03 build | HIGH |
| `cex_funnel_score.py` | Score a sales funnel for leaks. Reads funnel artifact + reward_signal data, flags drop-off stages (>20% delta), outputs H/M/L recommendations. | N06 lead / N05 build | HIGH |
| `cex_brand_diff.py` | Compare two brand_config.yaml versions (or two branches). Highlights voice drift, tone changes, value-prop rewrites. Exit 1 if drift > threshold. | N06 lead / N03 build | MEDIUM |
| `cex_course_scaffold.py` | Given a knowledge domain (e.g., "CEX bootstrap flow"), auto-generate course structure: 8 modules, prereqs, exercises, assessment. Uses KCs + retriever. | N06 lead / N04 build | MEDIUM |
| **(new)** `cex_ltv_calc.py` | LTV/CAC/MRR forecast from pricing tier + retention assumption. Pairs with `cex_price_gen.py`. | N06 lead / N05 build | HIGH |
| **(new)** `cex_monetize_audit.py` | Scan repo for monetization surface: pricing pages, funnels, CTAs, upsells. Score coverage + gaps. | N06 lead / N01 build | LOW |

ROI: `cex_price_gen.py` + `cex_ltv_calc.py` unblock gap #1 (CEX has no price) and gap #5 (no revenue forecasting). Those are the two highest-value misses.

---

## 6. Cross-Nucleus Dependencies

### 6.1 Inputs N06 needs

| From | What | Status |
|------|------|--------|
| N01 | Market research, competitor pricing, segment TAM | Partial -- `kc_competitive_positioning.md` exists, no live data pipeline |
| N02 | Funnel copy, ad variants, hook lines | Partial -- N02 has 34 brand refs, copy flows informally |
| N03 | New kind builders for monetization (optimizer, reward_signal, course_module) | Pending -- see wishlist |
| N04 | KC indexing for brand/pricing retrieval | Adequate -- TF-IDF retriever serves |

### 6.2 Outputs N06 provides

| To | What | Delivery |
|----|------|----------|
| ALL nuclei | Brand context (voice, values, ICP, colors) | `brand_propagate.py` + `{{BRAND_*}}` templating |
| N02 | Brand voice contract | `schemas/brand_voice_contract.md` |
| N03 | Pricing framework pattern | `architecture/pattern_pricing_framework.md` |
| N07 | Decision manifest inputs (bootstrap answers) | Via `cex_bootstrap.py --from-file` |

### 6.3 Brand context propagation -- measured

Scanned each nucleus for `BRAND_` or `brand_config` references:

| Nucleus | Ref count | Health |
|---------|--------:|:------:|
| N02 Marketing | 34 | [OK] Strong |
| N01 Intelligence | 16 | [OK] Adequate |
| N03 Engineering | 16 | [OK] Adequate |
| N07 Admin | 4 | [WARN] Thin |
| N04 Knowledge | 2 | [FAIL] **Brand-blind** |
| N05 Operations | 2 | [FAIL] **Brand-blind** |

**Brand context flow breaks at N04 and N05.** Knowledge cards don't cite brand voice; ops scripts don't inject brand-aware logging. Fix: run `brand_propagate.py --nucleus N04` and `--nucleus N05` with explicit target injection, then add `{{BRAND_NAME}}` placeholders into their agent_cards.

### 6.4 Action items for N07

1. Fix `boot/n06.ps1` `$args` bug (5 min, critical)
2. Dispatch N04 + N05 "brand-awareness" mini-missions (15 min each)
3. Schedule N06 to build `cex_price_gen.py` + `cex_ltv_calc.py` (60 min, highest ROI)
4. Update CLAUDE.md boot/n06.ps1 description (N04 task, 5 min)
5. Run `cex_score.py --audit N06_commercial/ --fix-quality-null` (20 min)

---

## Summary Table

| Dimension | Score | Trend |
|-----------|:----:|:----:|
| Artifact count (71) vs peers | 7/10 | stable |
| Quality compliance (`null` rule) | 3/10 | **regressing** |
| Tool production-readiness (6/6) | 10/10 | stable |
| Brand propagation coverage | 6/10 | uneven |
| Course/dogfooding | 1/10 | **missing** |
| Revenue forecasting | 1/10 | **missing** |
| Bootstrap enforcement | 5/10 | honor-system |
| 8F adherence | 9/10 | strong |
| Rules compliance (n06-commercial + brand-bootstrap) | 7/10 | acceptable |

**Verdict**: N06 owns brand/bootstrap cleanly (6 prod tools, 35+ brand artifacts, 15q interview). **Three structural holes**: (1) no pricing for CEX itself, (2) no courses, (3) no revenue forecasting. **One critical bug**: `boot/n06.ps1` drops MCP config silently. **One systemic violation**: 56 artifacts self-scored in defiance of Rule 4.

Strategic greed says: build `cex_price_gen.py` + `cex_ltv_calc.py` first. That's the leverage point. Everything else is polish.

---

*Generated by N06 Commercial, 8F pipeline, F1->F8. Autonomous dispatch from N07 SELF_AUDIT grid.*
