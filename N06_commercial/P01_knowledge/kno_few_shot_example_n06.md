---
id: kno_few_shot_example_n06
kind: few_shot_example
pillar: P01
nucleus: n06
title: Commercial Few Shot Example
version: 1.0
quality: null
tags: [knowledge, few_shot_example, prompting, pricing, offers, sales]
---
<!-- 8F: F1=P01/few_shot_example F2=few-shot-example-builder F3=nucleus_def_n06.md,kc_few_shot_example.md,P01_knowledge/_schema.yaml,N06 commercial knowledge examples F4=teach_commercial_prompt_output_with_revenue_ranked_reasoning F5=apply_patch;python _tools/cex_compile.py F6=author_dense_markdown_artifact F7=frontmatter_ascii_density_linecount_review F8=N06_commercial/knowledge/kno_few_shot_example_n06.md -->

# Commercial Few Shot Example

## Purpose

| Field | Value |
|-------|-------|
| Goal | Teach N06 prompts to output concise commercial recommendations with revenue ranking and margin discipline |
| Business Lens | Strategic Greed wants examples that show how to push buyers upward without leaking value |
| Primary Use | injected into offer generation, pricing advice, ICP matching, and renewal rescue prompts |
| Failure Prevented | generic copy that sounds plausible but ignores ARPU, margin, and buying proximity |
| Format Taught | structured markdown with recommendation order, evidence, and cash-near next action |
| Difficulty | medium |

## Teaching Target

| Output Field | Why It Must Appear | Commercial Value |
|--------------|--------------------|------------------|
| primary_move | forces one leading recommendation | avoids diluted advice |
| value_case | explains why buyer should pay more | creates monetization narrative |
| proof_needed | names missing evidence | highlights what blocks conversion |
| risk_guard | prevents discount or feature leakage | protects margin |
| next_action | operationalizes the recommendation | shortens time to revenue |

## Input

```yaml
company_stage: growth
product_type: ai_automation_suite
customer_signal:
  segment: scale
  team_size: 42
  current_plan: starter_monthly
  monthly_usage_pct: 88
  integrations_requested: 3
  procurement_ready: true
constraints:
  max_discount_pct: 15
  margin_floor_pct: 65
  sales_cycle_days: 10
goal: move_customer_to_higher_value_offer_without_custom_scope_leak
```

## Output

```markdown
### Commercial Recommendation

| Field | Value |
|-------|-------|
| primary_move | Push annual Growth plan with integration pack add-on |
| revenue_rank | 1 |
| value_case | Customer is already near usage ceiling, has multi-seat demand, and procurement is ready, so annual expansion reduces friction and raises locked-in cash |
| proof_needed | Show ROI from automation throughput and admin time saved for 40+ seat teams |
| risk_guard | Do not offer custom enterprise features yet; keep discount at or below 10 percent and tie any concession to annual prepay |
| next_action | Send annual upgrade proposal with integration bundle and a 7-day close window |

### Why This Wins

1. Usage at 88 percent signals expansion pressure.
2. Procurement readiness lowers close friction.
3. Annual prepay improves cash collection and retention.
4. Integration demand justifies upsell without bespoke discounting.
```

## Why This Example Works

| Dimension | Reason |
|-----------|--------|
| realism | input mirrors a commercial account with actual buying signals |
| format lock | output always starts with recommendation table before explanation |
| greed lens | recommendation maximizes cash and retention, not just user happiness |
| guardrails | discount and scope limits are explicit |
| actionability | final step can be executed by sales or prompt pipeline immediately |

## Selection Policy

| When to Inject | Why |
|----------------|-----|
| pricing advice prompt | teaches revenue-ranked recommendation structure |
| bundle prompt | teaches guardrails against uncontrolled feature leakage |
| sales assist prompt | teaches proof and next-action fields |
| renewal rescue prompt | reusable pattern for value-case and risk guard |

## Anti-Drift Notes

| Failure Mode | Correction |
|--------------|-----------|
| model proposes many equal options | example shows one ranked primary move |
| model gives fluffy benefits | example ties value to usage and procurement signals |
| model discounts too early | example caps concession and trades it for annual commitment |
| model forgets action | example ends with explicit close motion |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| scale customer input | premium segment pressure is where retrieval matters most | makes example commercially relevant |
| annual plan push | cash collection and retention improve together | greed prefers locked-in revenue |
| proof field | prompts should reveal evidence gaps before selling harder | prevents weak positioning |
| risk guard field | discounts destroy value when unconstrained | margin discipline remains visible |
| next action field | recommendations without execution are dead weight | accelerates monetization loops |

## Adaptation Hints

| Variant | Change |
|---------|--------|
| renewal risk | swap primary_move to save offer with term extension |
| low-intent lead | keep proof_needed heavy and next_action lighter |
| enterprise expansion | add procurement, security, and rollout proof |
| bundle motion | keep one anchor offer and one add-on only |

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Kind | `few_shot_example` |
| Format Bias | recommendation table first |
| Main Lever | annual expansion with guardrails |
| Quality Goal | strong format compliance under monetization prompts |
| Injection Surface | pricing, offers, renewal, sales assist |
| Related Artifacts | `knowledge_card_content_monetization.md`, `kno_retriever_config_n06`, `mem_runtime_state_n06` |
