---
kind: context-doc
nucleus: N06
pillar: P09
quality: null
date: 2026-04-02
type: self-review
author: n06_commercial
---

# N06 Self-Review — 2026-04-02

## Summary

| Item | Value |
|------|-------|
| Total artifacts (N06_commercial/) | 40 .md source + 13 compiled .yaml = **53** |
| Brand bootstrapped | **NO** ⚠️ CRITICAL |
| `.cex/brand/brand_config.yaml` | **MISSING** |
| Files with `{{BRAND_*}}` unresolved | **30** (system-wide) |
| Brand tools functional | **2 / 5** (brand_inject, brand_ingest OK; 3 crash on Windows) |
| Monetization templates (output/) | **9** — all awaiting brand_config |
| content-monetization-builder ISOs | **13 / 13** — complete |
| social-publisher-builder ISOs | **13 / 13** — complete, indirect N02 integration |
| Bootstrap paths implemented | **3 / 3** — chat, CLI, auto-detect |

---

## CRITICAL Gaps (must fix)

### 1. Brand not bootstrapped — blocks ALL brand-dependent features
`.cex/brand/brand_config.yaml` does not exist.
- Every output template (Brand Book, Pricing Page, Voice Guide, Discovery Report, Visual Identity, One Pager, Competitive Map, Transformation Arc, Brand Config) stays as a stub
- `brand_propagate.py` cannot push anything to any nucleus
- `brand_audit.py` cannot score any consistency
- N02 produces generic copy (no voice)
- N03 produces artifacts without palette
- N06 cannot produce any deliverable output until this file exists
- **Fix**: Run `/init` conversational flow → cex_bootstrap.py → brand_config.yaml

### 2. Three brand tools crash on Windows (UnicodeEncodeError)
`brand_validate.py`, `brand_propagate.py`, `brand_audit.py` all crash when printing the ❌ emoji on Windows console (cp1252 encoding).

**Error**:
```
UnicodeEncodeError: 'charmap' codec can't encode character '\u274c'
```

The scripts detect the missing config correctly (exit code 1) but the Python traceback replaces the intended error message, causing confusion. Any Windows user running these tools gets a crash, not a clear "brand not found" message.

**Fix needed**: Replace emoji chars with ASCII alternatives (`[FAIL]`, `[OK]`, `[WARN]`) or add `PYTHONIOENCODING=utf-8` env var requirement, or use `sys.stdout.buffer.write()` with explicit UTF-8 encoding in those 3 files.

---

## WARN Gaps (should fix)

### 3. No standalone funnel output templates
`N06_commercial/output/` has 9 templates — but none for:
- VSL (Video Sales Letter) — structure is documented in knowledge_card_commercial.md but no output template
- Email sequence — documented conceptually, no template
- Landing page (long-form sales page) — missing
- Order bump / OTO scripts — missing

The `workflow_content_monetization.md` describes a 9-step pipeline (PARSE→PRICING→CREDITS→CHECKOUT→COURSES→ADS→EMAILS→VALIDATE→DEPLOY) but there are no output artifacts for the ADS and EMAILS stages.

### 4. social-publisher-builder N02 integration is indirect
`social-publisher-builder` collaboration specifies crews with knowledge-card-builder, prompt-template-builder, cli-tool-builder — but does **not** define a direct handoff to N02 for caption generation. The `bld_collaboration_social_publisher.md` lists `prompt-template-builder` as the caption writer, not N02_marketing.

For brand-aligned social content, the flow should be: social-publisher-builder → N02 (caption generation in brand voice). This coupling is undocumented.

### 5. `N06_commercial/output/output_transformation_arc.md` — check content
Filename suggests a Transformation Arc output template, but was not confirmed to have VSL-ready content. Needs review to ensure it covers the BEFORE/AFTER/THROUGH arc with pricing anchor logic.

### 6. No deployed pricing model exists
`output_pricing_page.md` is an HTML template using `{{BRAND_*}}` variables. There is no filled-in, brand-specific pricing strategy document. The knowledge is present (`knowledge_card_commercial.md`, pricing frameworks excellent) but no artifact instantiates it for a real product.

---

## Brand System Status

| Tool | Status | Notes |
|------|--------|-------|
| `brand_validate.py` | PARTIAL — exits correctly (1), crashes on message | UnicodeEncodeError on Windows cp1252 with ❌ emoji |
| `brand_propagate.py` | PARTIAL — exits correctly (1), crashes on message | Same UnicodeEncodeError |
| `brand_audit.py` | PARTIAL — exits correctly (1), crashes on message | Same UnicodeEncodeError |
| `brand_inject.py` | OK — help loads, `--check` flag works | Functional |
| `brand_ingest.py` | OK — help loads, folder scan works | Functional |
| `cex_bootstrap.py --check` | OK — prints "NOT BOOTSTRAPPED" cleanly | No emoji, works on Windows |
| `.cex/brand/brand_config.yaml` | MISSING | Root cause of all brand gaps |
| `.cex/brand/brand_config_template.yaml` | EXISTS | Template is ready to fill |
| `.cex/brand/brand_config_schema.yaml` | EXISTS | Schema is ready to validate |

---

## Bootstrap Flow Status

| Path | Status | Notes |
|------|--------|-------|
| `/init` (chat) | FUNCTIONAL | Fully documented in `.claude/commands/init.md` — 3 rounds of questions |
| `init.cmd` (double-click) | FUNCTIONAL | Checks `.bootstrapped` marker, calls `cex_bootstrap.py` |
| `boot/n06.cmd` | FUNCTIONAL | Loads 10 brand KCs, triggers N06 with brand discovery fallback |
| `boot/cex.cmd` (auto-detect) | NOT VERIFIED | Was not checked in this audit |
| `cex_bootstrap.py` (full run) | FUNCTIONAL | Interactive 13-question CLI, no emoji crashes |
| `cex_bootstrap.py --from-file` | NOT VERIFIED | YAML ingest path not tested |
| `brand_ingest.py` (folder scan) | FUNCTIONAL | Help verified, folder scan capability present |

---

## Monetization Readiness

| Area | Status | Evidence |
|------|--------|---------|
| Pricing frameworks | READY (knowledge) | `knowledge_card_commercial.md` — value-based, anchor, 3-tier, psychological pricing |
| Pricing template | TEMPLATE ONLY | `output_pricing_page.md` — HTML awaiting brand_config |
| Funnels (knowledge) | READY | VSL structure, funnel benchmarks in KC |
| Funnel templates | MISSING | No VSL, email sequence, or landing page output templates |
| Course structure | FRAMEWORK | content-monetization-builder has 9-stage pipeline |
| Course templates | MISSING | No instantiated course outline template |
| Social publishing | BUILDER READY | social-publisher-builder 13/13 ISOs |
| Social → N02 integration | INDIRECT | Via crew compositions, no direct handoff spec |
| Brazilian market | COVERED | Hotmart, Kiwify, PIX, BRL, parcelamento in KC |
| Upsell architecture | KNOWLEDGE ONLY | Documented in KC, no template artifact |

---

## Recommended Actions (priority order)

1. **[CRITICAL] Run `/init`** — Bootstrap brand_config.yaml. Nothing else matters until this exists. Use chat path (conversational) or `init.cmd`. Takes 5 minutes. Unlocks the entire system.

2. **[HIGH] Fix Unicode crash in 3 brand tools** — `brand_validate.py`, `brand_propagate.py`, `brand_audit.py` crash on Windows with emoji. Replace `\u274c` / `\u2705` with ASCII `[FAIL]` / `[OK]`. Affects every Windows user on first run.

3. **[MEDIUM] Create VSL output template** — `N06_commercial/output/output_vsl_template.md` with the 8-section VSL structure (hook, problem, revelation, proof, offer, CTA, guarantee, scarcity). Knowledge exists in KC; just needs a template artifact.

4. **[MEDIUM] Create email sequence template** — `N06_commercial/output/output_email_sequence.md` for onboarding, upsell, churn prevention. Covered in content-monetization-builder ISOs but no standalone output template.

5. **[MEDIUM] Document N02 handoff in social-publisher-builder** — Add N02_marketing as direct crew partner in `bld_collaboration_social_publisher.md`. Define explicit handoff: social-publisher-builder produces posting schedule → N02 writes captions in brand voice.

6. **[LOW] Verify `boot/cex.cmd` auto-detect path** — Confirm the third bootstrap path works as documented in CLAUDE.md.

7. **[LOW] Verify `cex_bootstrap.py --from-file`** — Test YAML ingest path with a minimal brand YAML to ensure it creates brand_config.yaml correctly.

---

## Impact Summary: Brand Empty → System Impact

```
brand_config.yaml MISSING
├── brand_propagate.py       → cannot inject → ALL nuclei run without brand context
├── brand_audit.py           → cannot score → brand consistency unknown
├── N06 output templates (9) → stub only   → no deliverables possible
├── N01 output templates (3) → BRAND_* unresolved → generic intelligence
├── N02 marketing artifacts  → generic copy → no voice match
├── N03 builders             → no palette injection → generic visual
└── CLAUDE.md check          → "Not yet bootstrapped" → correct warning shown
```

**Priority**: `/init` is the single action that unlocks the entire CEX system.
Without it, every nucleus operates in generic mode regardless of pipeline quality.
