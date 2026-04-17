---
id: funnel_diagnostic_tool
kind: tool_card
pillar: P11
title: "Funnel Diagnostic Tool — Leak Detection & Fix Prioritization"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: funnel_optimization
quality: 9.0
tags: [tool, funnel, diagnostic, conversion, N06, optimization]
tldr: "Input funnel metrics → identify biggest leak → recommend fix → estimate ROI of fix. Prevents optimizing the wrong stage."
density_score: 0.88
---

# Funnel Diagnostic Tool

## Purpose

Most teams optimize the wrong funnel stage. They pour money into ads (ATTRACT) when the real leak is checkout friction (CONVERT). This tool takes stage-level metrics, identifies the highest-ROI fix, and recommends the action.

**ROI**: Fixing a 5% checkout abandonment → +$X/mo. Running more ads into the same broken checkout → -$Y/mo wasted. The diagnostic costs 10 minutes. The wrong optimization costs months.

---

## Input: Funnel Metrics

```yaml
funnel_input:
  attract:
    monthly_visitors: 0
    qualified_pct: 0.0      # % of visitors that match ICP
    cost_per_visitor: 0.00   # if paid channels
    
  engage:
    page_views: 0            # landing page views
    signups: 0               # email, trial, or account
    signup_rate: 0.0         # auto-calculated
    
  convert:
    trials_or_leads: 0
    paying_customers: 0
    conversion_rate: 0.0     # auto-calculated
    avg_deal_value: 0.00
    
  retain:
    active_customers: 0
    churned_this_period: 0
    churn_rate: 0.0          # auto-calculated
    
  expand:
    upgrades: 0
    nrr: 0.0                # net revenue retention
```

---

## Diagnostic Logic

### Stage Benchmarks

| Stage | Metric | Poor | Average | Good | Excellent |
|-------|--------|------|---------|------|-----------|
| ATTRACT | Qualified % | < 20% | 20-40% | 40-60% | > 60% |
| ENGAGE | Signup rate | < 3% | 3-8% | 8-15% | > 15% |
| CONVERT | Trial→Paid | < 2% | 2-5% | 5-10% | > 10% |
| RETAIN | Monthly churn | > 8% | 5-8% | 3-5% | < 3% |
| EXPAND | NRR | < 90% | 90-100% | 100-120% | > 120% |

### Leak Detection Algorithm

```
FOR each stage:
  gap = benchmark_good - actual_value
  revenue_impact = gap × downstream_volume × avg_deal_value
  fix_effort = estimated_hours × hourly_rate

SORT stages by (revenue_impact / fix_effort) DESC
RETURN top_leak = stage with highest ROI-to-fix ratio
```

### Priority Matrix

| Leak Location | Revenue Impact | Fix Effort | Priority |
|--------------|---------------|-----------|----------|
| CONVERT (checkout) | Very High | Low-Medium | 🔴 Fix first |
| RETAIN (churn) | High | Medium | 🔴 Fix second |
| ENGAGE (signup) | Medium-High | Medium | 🟡 Fix third |
| EXPAND (upsell) | Medium | Low | 🟡 Quick win |
| ATTRACT (traffic) | Varies | High ($$$) | 🟢 Fix last |

**Rule**: Never pour more traffic (ATTRACT) until CONVERT and RETAIN are healthy. It's pouring water into a leaky bucket.

---

## Output: Diagnostic Report

```markdown
# Funnel Diagnostic Report — [Product] — [Date]

## Summary
- **Biggest Leak**: [STAGE] — [metric] is [value] vs benchmark [target]
- **Revenue at Stake**: $[amount]/month if fixed to benchmark
- **Recommended Fix**: [specific action]
- **Estimated ROI**: [X]:1 over [N] months

## Stage-by-Stage Analysis

### ATTRACT ✅/⚠️/🔴
- Traffic: [N] visitors/month
- Qualified: [X]%
- Assessment: [healthy | needs work | critical]
- Action: [none | specific recommendation]

### ENGAGE ✅/⚠️/🔴
[...]

### CONVERT ✅/⚠️/🔴
[...]

### RETAIN ✅/⚠️/🔴
[...]

### EXPAND ✅/⚠️/🔴
[...]

## Fix Priority Queue
1. [Stage] — [action] — est. impact $[X]/mo — effort [N] hours
2. [Stage] — [action] — est. impact $[X]/mo — effort [N] hours
3. [Stage] — [action] — est. impact $[X]/mo — effort [N] hours
```

---

## Common Fixes by Stage

### ATTRACT Fixes
| Problem | Fix | Cost | Expected Impact |
|---------|-----|------|----------------|
| Low traffic | Content marketing (SEO) | Time | +50-200% in 3-6 months |
| Low traffic (urgent) | Paid ads | $$$ | +immediate, stops when budget stops |
| Unqualified traffic | Refine targeting | Low | +quality, may reduce volume |

### ENGAGE Fixes
| Problem | Fix | Cost | Expected Impact |
|---------|-----|------|----------------|
| Low signup rate | Rewrite value prop | Low | +30-100% signup |
| Low signup rate | Add social proof | Low | +10-30% signup |
| Low signup rate | Reduce form fields | Low | +10-25% signup |
| High bounce rate | Improve page speed | Medium | +5-15% engagement |

### CONVERT Fixes
| Problem | Fix | Cost | Expected Impact |
|---------|-----|------|----------------|
| Low trial→paid | Fix onboarding | Medium | +20-50% conversion |
| Cart abandonment | Simplify checkout | Low | +10-30% conversion |
| Cart abandonment | Add payment options | Low | +5-15% conversion |
| Price objection | Add social proof/ROI calc | Low | +10-20% conversion |

### RETAIN Fixes
| Problem | Fix | Cost | Expected Impact |
|---------|-----|------|----------------|
| High early churn | Improve first 7 days | Medium | -30-50% churn |
| Feature churn | Build requested features | High | -20-40% churn |
| Price churn | Introduce annual lock-in | Low | -15-25% churn |
| Silent churn | Add engagement emails | Low | -10-20% churn |

### EXPAND Fixes
| Problem | Fix | Cost | Expected Impact |
|---------|-----|------|----------------|
| No upsells | Create premium tier | Medium | +10-30% ARPU |
| No referrals | Add referral program | Medium | +5-15% new customers |
| Flat NRR | Usage-based pricing component | Medium | +10-25% NRR |

---

## Integration

| CEX Component | Role |
|---------------|------|
| `pattern_funnel_architecture.md` | Defines funnel stages (reference) |
| `pricing_optimization_memory.md` | Stores diagnostic results over time |
| Stripe MCP | Pulls conversion + churn data |
| N02 Marketing | Executes ATTRACT + ENGAGE fixes |
| N05 Operations | Executes RETAIN technical fixes |
| N03 Engineering | Builds checkout/UX improvements |
