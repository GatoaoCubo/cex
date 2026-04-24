---
id: p12_wf_content_monetization
kind: workflow
8f: F8_collaborate
pillar: P12
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n06_commercial
title: Content Monetization Workflow
steps_count: 9
execution_mode: sequential
error_recovery: retry_with_mock_fallback
max_retries: 2
timeout_minutes: 30
quality: 9.1
updated: 2026-04-07
tags: [workflow, content-monetization, billing, credits, courses, checkout, ads, emails, N06]
tldr: Full 9-step content monetization workflow — PARSE through DEPLOY — with credit gating, PIX checkout, LLM course generation, ad validation, and email dispatch.
density_score: 0.93
axioms:
  - "ALWAYS validate credit balance before gating — never charge then fail."
  - "NEVER deploy checkout without testing PIX + card + boleto flows."
linked_artifacts:
  primary: p12_dr_content_monetization
  related: [p04_fn_content_monetization, p01_kc_brand_monetization_models, n06_output_pricing_page]
related:
  - p04_fn_content_monetization
  - p12_wf_builder_8f_pipeline
  - n06_kc_content_monetization
  - bld_architecture_chain
  - p11_qg_chain
  - p10_lr_chain_builder
  - p12_wf_content_factory_v1
  - p04_tpl_content_monetization
  - tpl_instruction
  - p12_wf_create_orchestration_agent
---

# Content Monetization Workflow

Full end-to-end workflow for N06 content monetization operations. Receives a product intent and produces a deployed monetization config with checkout, course, ads, and email artifacts.

**Pipeline**: PARSE → PRICING → CREDITS → CHECKOUT → COURSES → ADS → EMAILS → VALIDATE → DEPLOY

---

## Step 1: PARSE

**Agent**: N06 (content_monetization_builder)
**Action**: Extract product descriptor, audience, monetization goal, and provider config from raw intent.
**Input**: raw_intent (string or structured payload)
**Output**: `parsed_intent.yaml` — `{product_name, category, audience, payment_provider, currency, pipeline_steps}`
**Signal**: `monetization_parsed`
**Timeout**: 2 minutes

```yaml
output_schema:
  product_name: string
  category: enum [course, ebook, saas, ecommerce]
  audience: string
  payment_provider: enum [stripe, mercadopago, mock]
  currency: enum [BRL, USD]
  pricing_tier: enum [free, pro, enterprise]
```

---

## Step 2: PRICING

**Agent**: N06
**Action**: Load PIPELINE_COSTS, apply pricing_tier rules, estimate total credit consumption, resolve pack recommendation.
**Input**: `parsed_intent.yaml`
**Output**: `pricing_config.yaml` — `{estimated_credits, recommended_pack, tier_prices, margin_check}`
**Signal**: `pricing_resolved`
**Depends on**: Step 1

```yaml
pipeline_costs:
  PESQUISA: 75   # centavos BRL
  ANUNCIO: 50
  FOTO: 100
  FULL: 200
margin_check: cost_plus > 30%  # gate — fail if margin below threshold
```

---

## Step 3: CREDITS

**Agent**: N06
**Action**: Call `check_sufficient(user_id, estimated_cost)`. If sufficient → lock credits with idempotency_key. If insufficient → generate checkout URL for pack purchase and PAUSE workflow.
**Input**: `pricing_config.yaml` + user_id
**Output**: `credit_lock.yaml` — `{locked: bool, balance_before, idempotency_key}` OR `checkout_url` (pack purchase)
**Signal**: `credits_locked` OR `checkout_required`
**Depends on**: Step 2

**Branch logic**:
- Sufficient → continue to Step 4
- Insufficient → emit `checkout_required` signal → Step 4 (CHECKOUT for pack)

---

## Step 4: CHECKOUT

**Agent**: N06
**Action**: Create payment session for product OR credit pack, depending on credit_lock branch.
**Input**: `pricing_config.yaml` + provider config
**Output**: `checkout_session.yaml` — `{checkout_url, session_id, provider, amount_centavos, idempotency_key}`
**Signal**: `checkout_created`
**Depends on**: Step 3

**Provider logic**:
```
mercadopago:
  - create_preference(title, unit_price_centavos, payer_email)
  - PIX → immediate; boleto → 3 days; card → installments
  - webhook: IPN payment.approved → x-signature HMAC-SHA256 verify

stripe:
  - create_checkout_session(price_id, customer_id, mode)
  - webhook: checkout.session.completed
  - idempotency_key = session_id

mock:
  - Returns fake checkout_url immediately
  - No API calls — safe for dev/CI
```

---

## Step 5: COURSES

**Agent**: N06
**Action**: Execute sequential LLM chain: outline → modules × N → sales_page → email_sequence.
**Input**: `parsed_intent.yaml`
**Output**: `course_artifacts/` — `{outline.yaml, modules/*.yaml, sales_page.md, email_sequence.yaml}`
**Signal**: `courses_generated`
**Depends on**: Step 3 (credits locked)
**Timeout**: 15 minutes (LLM chain is slowest step)

```yaml
llm_chain:
  step_1: OutlineOutput   # title, modules[], target_audience, transformation_arc
  step_2: ModuleOutput    # per module: title, lessons[], duration_minutes, key_outcomes
  step_3: SalesPageOutput # headline, pain_agitation, mechanism, proof, offer, cta
  step_4: EmailSequenceOutput  # subject_lines[], bodies[], send_days[]

mock_fallback: true  # If LLM quota exceeded → return stub Pydantic objects
pydantic_validation: strict  # Each step validates output schema before passing to next
```

---

## Step 6: ADS

**Agent**: N06
**Action**: Validate ad content against product facts. Run FABRICATION_PATTERNS regex. Score confidence. Retry flagged sections if score < 0.7.
**Input**: `course_artifacts/sales_page.md` + product_facts
**Output**: `validated_ads.yaml` — `{ad_copies[], confidence_scores[], validation_report}`
**Signal**: `ads_validated`
**Depends on**: Step 5
**Max retries**: 2 (retry-with-sections on score < 0.7)

```yaml
validation_gates:
  confidence_min: 0.7
  fabrication_check: true  # FABRICATION_PATTERNS regex scan
  factual_accuracy: product_facts_match
retry_strategy: regenerate_flagged_sections  # Not full retry — only low-score sections
```

---

## Step 7: EMAILS

**Agent**: N06
**Action**: Render email templates from `TEMPLATES` dict. Apply BRL formatting. Queue transactional + marketing sequences.
**Input**: `course_artifacts/email_sequence.yaml` + user_profile
**Output**: `email_queue.yaml` — `{emails[], types[], scheduled_at[], brl_formatted: true}`
**Signal**: `emails_queued`
**Depends on**: Step 5

```yaml
template_types:
  transactional: [purchase_confirmation, credit_alert, checkout_expired]
  marketing: [launch_sequence, abandoned_cart, upsell_offer]
brl_format: "R${amount/100:,.2f}"  # Always display from centavos
personalization: [user_name, product_name, checkout_url, credit_balance]
```

---

## Step 8: VALIDATE

**Agent**: N06
**Action**: Run quality gates. Block deployment if any gate fails.
**Input**: All previous step outputs
**Output**: `validation_report.yaml` — `{gates_passed, gates_failed, deploy_approved: bool}`
**Signal**: `validation_complete`
**Depends on**: Steps 2, 4, 6, 7

```yaml
gates:
  pricing_margin_above_30pct: true   # PIPELINE_COSTS margin check
  mock_fallback_exists: true         # Every payment path has mock mode
  webhook_idempotent: true           # event_id as idempotency key verified
  ad_confidence_above_07: true       # All ads passed validation
  pydantic_models_valid: true        # All course artifacts schema-valid
  brl_formatting_correct: true       # No floats in credit/price display
```

---

## Step 9: DEPLOY

**Agent**: N06
**Action**: Save monetization_config to instance. Emit signal. Archive run artifacts.
**Input**: `validation_report.yaml` (deploy_approved=true)
**Output**: `_instances/codexa/N06_commercial/content_monetization_config.md`
**Signal**: `monetization_deployed` → `.cex/runtime/signals/n06_monetization.json`
**Depends on**: Step 8 (deploy_approved=true)

```yaml
actions:
  - save: _instances/codexa/N06_commercial/content_monetization_config.md
  - compile: python _tools/cex_compile.py {path}
  - signal: write_signal('n06', 'monetization_deployed', score)
  - git: add + commit "[N06] monetization deployed: {product_name}"
```

---

## Workflow Signals

| Signal | File | Meaning |
|--------|------|---------|
| `monetization_parsed` | `.cex/runtime/signals/n06_parse.json` | Intent parsed |
| `pricing_resolved` | `.cex/runtime/signals/n06_pricing.json` | Costs estimated |
| `credits_locked` | `.cex/runtime/signals/n06_credits.json` | Balance sufficient |
| `checkout_required` | `.cex/runtime/signals/n06_checkout_req.json` | Pack purchase needed |
| `checkout_created` | `.cex/runtime/signals/n06_checkout.json` | Payment session ready |
| `courses_generated` | `.cex/runtime/signals/n06_courses.json` | LLM chain complete |
| `ads_validated` | `.cex/runtime/signals/n06_ads.json` | Confidence >= 0.7 |
| `emails_queued` | `.cex/runtime/signals/n06_emails.json` | Queue ready |
| `validation_complete` | `.cex/runtime/signals/n06_validation.json` | Gates passed |
| `monetization_deployed` | `.cex/runtime/signals/n06_monetization.json` | Config deployed |

## Error Recovery

| Step | Failure | Recovery |
|------|---------|----------|
| CREDITS | Insufficient balance | Pause; emit checkout_required; resume on payment.approved |
| CHECKOUT | Provider 5xx | Retry ×3 with backoff; fallback to mock on 3rd failure |
| COURSES | LLM quota exceeded | Mock fallback — return stub Pydantic objects |
| ADS | confidence < 0.7 | Retry-with-sections ×2; if still failing → flag for human review |
| VALIDATE | Gate failure | Return validation_report with failed gates; no deploy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fn_content_monetization]] | upstream | 0.40 |
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.40 |
| [[n06_kc_content_monetization]] | upstream | 0.34 |
| [[bld_architecture_chain]] | upstream | 0.33 |
| [[p11_qg_chain]] | upstream | 0.30 |
| [[p10_lr_chain_builder]] | upstream | 0.29 |
| [[p12_wf_content_factory_v1]] | sibling | 0.28 |
| [[p04_tpl_content_monetization]] | upstream | 0.28 |
| [[tpl_instruction]] | upstream | 0.27 |
| [[p12_wf_create_orchestration_agent]] | sibling | 0.27 |
