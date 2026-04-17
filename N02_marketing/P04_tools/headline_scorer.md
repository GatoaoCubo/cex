---
id: n02_tool_headline_scorer
kind: cli_tool
pillar: P04
title: "Headline Scorer — N02 Marketing Optimization Tool"
version: 1.0.0
created: 2026-04-07
author: n02_marketing
domain: headline_optimization
nucleus: N02
quality: 9.0
tags: [cli-tool, headline-scorer, N02, marketing, optimization, 4U, headlines]
tldr: "Scores headlines on 4 dimensions (Useful, Urgent, Unique, Ultra-specific), generates A/B variants, predicts relative CTR lift, and recommends the winner. Every headline enters a tournament — only the strongest survives."
density_score: 0.92
---

# Headline Scorer — Marketing Optimization Tool

## Purpose

Rapid headline evaluation and variant generation. Takes 1+ headlines, scores each on the 4U framework, generates optimized alternatives, and recommends the highest-potential winner. Designed for speed: score 10 headlines in 3 seconds, ship the best one.

## Pipeline

```
INPUT (1+ headlines)
    │
    ▼
┌──────────────────┐
│  4U SCORING      │
│  Useful: 1-3     │
│  Urgent: 1-3     │
│  Unique: 1-3     │
│  Ultra-spec: 1-3 │
│  Total: 4-12     │
└────────┬─────────┘
         │
    ┌────┼────┐
    ▼    ▼    ▼
 PATTERN  WORD  EMOTION
 DETECT   POWER  SCORE
    │    │    │
    └────┼────┘
         ▼
┌──────────────────┐
│  VARIANT GEN     │
│  3 alternatives  │
│  per input       │
└────────┬─────────┘
         │
    ┌────┼────┐
    ▼    ▼    ▼
 RANK   BEST  REPORT
 ALL    PICK  OUTPUT
```

## Usage

```bash
# Score a single headline
python headline_scorer.py "7 Ways to Double Your Email Open Rate"

# Score multiple headlines (comparison mode)
python headline_scorer.py --compare \
  "7 Ways to Double Your Email Open Rate" \
  "How to Get More Email Opens" \
  "Email Marketing Tips That Work"

# Score + generate variants
python headline_scorer.py --variants "Stop Losing Leads to Bad Copy"

# Score from file (one headline per line)
python headline_scorer.py --file headlines.txt

# Score with context (audience + funnel stage)
python headline_scorer.py --audience b2c --funnel tofu \
  "The CTA Mistake Costing You 40% of Conversions"

# Output JSON
python headline_scorer.py --format json "Your Headline Here"

# Tournament mode (score all, rank, pick winner)
python headline_scorer.py --tournament --file all_headlines.txt
```

## Scoring Framework: The 4U Method

### Dimension Definitions

| Dimension | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|
| **Useful** | No clear benefit | Implied benefit | Explicit, specific benefit |
| **Urgent** | No time pressure | Soft urgency hint | Strong deadline/consequence |
| **Unique** | Generic, anyone could say it | Some differentiation | Only YOUR offer fits this headline |
| **Ultra-specific** | Vague ("improve results") | Somewhat specific ("better ROI") | Exact ("37% more clicks in 14 days") |

### Scoring Examples

```
"Marketing Tips" → U:1 Ur:1 Un:1 Us:1 = 4/12 ❌ WEAK
Diagnosis: No benefit, no urgency, completely generic, zero specificity.

"How to Get More Leads" → U:2 Ur:1 Un:1 Us:1 = 5/12 ⚠️ BELOW AVERAGE
Diagnosis: Implied benefit (leads), but no urgency, generic, vague.

"7 Email Hacks That Doubled Our Reply Rate" → U:3 Ur:1 Un:2 Us:3 = 9/12 ✅ STRONG
Diagnosis: Specific benefit (reply rate), unique claim (our = story), ultra-specific (7, doubled).

"Last Day: Get 3x More Leads Before Price Doubles" → U:3 Ur:3 Un:2 Us:3 = 11/12 🔥 EXCELLENT
Diagnosis: All 4 dimensions firing. Specific, urgent, benefit-rich, numbered.
```

### Score Thresholds

| Total Score | Rating | Action |
|-------------|--------|--------|
| 4-5 | ❌ Weak | Rewrite completely |
| 6-7 | ⚠️ Below Average | Improve 2+ dimensions |
| 8-9 | ✅ Strong | Minor tweaks, test as-is |
| 10-11 | 🔥 Excellent | Ship immediately |
| 12 | 💎 Perfect | Rare. Celebrate then ship. |

---

## Power Word Detection

### Emotional Power Words (boost engagement)
```yaml
desire_words: [free, exclusive, secret, proven, guaranteed, instant, effortless]
fear_words: [mistake, warning, avoid, never, losing, failing, risk]
curiosity_words: [hidden, unexpected, strange, weird, shocking, little-known]
authority_words: [research, study, data, science, expert, Harvard, Stanford]
urgency_words: [now, today, limited, deadline, last, before, hurry, closing]
```

### Power Word Score
```
0 power words: -1 from total (flat, lifeless)
1-2 power words: +0 (baseline)
3+ power words: +1 bonus (careful — too many = spam feel)
```

---

## Pattern Detection

### High-Performance Headline Patterns

| Pattern | Detection Rule | Avg CTR Lift |
|---------|---------------|-------------|
| Number-first | Starts with digit (1-99) | +15-25% |
| How-to | Starts with "How to" | +10-20% |
| Question | Ends with "?" | +8-15% |
| Negative frame | Contains "stop/avoid/never/mistake" | +12-20% |
| Parenthetical | Contains (...) or [...] | +5-10% |
| Colon split | Contains ":" | +5-8% |

### Pattern Compatibility Matrix

| Pattern | TOFU | MOFU | BOFU |
|---------|------|------|------|
| Number-first | ★★★ | ★★ | ★ |
| How-to | ★★ | ★★★ | ★ |
| Question | ★★★ | ★★ | ★★ |
| Negative | ★★★ | ★★ | ★ |
| Parenthetical | ★★ | ★★ | ★★★ |
| Colon split | ★★ | ★★★ | ★★ |

---

## Variant Generation

For each input headline, generate 3 alternative variants using different angles:

### Variant Strategies

```yaml
variant_1_pain_reframe:
  strategy: "Rewrite from problem angle"
  input: "7 Ways to Get More Leads"
  output: "Stop Losing 73% of Your Website Visitors"
  
variant_2_specificity_boost:
  strategy: "Add numbers, names, or timeframes"
  input: "How to Write Better Headlines"
  output: "How to Write Headlines That Get 3x More Clicks (in 10 Minutes)"
  
variant_3_curiosity_gap:
  strategy: "Open a loop the reader must close"
  input: "Email Marketing Best Practices"
  output: "The One Email Trick That 91% of Marketers Miss"
```

### Variant Quality Rules
```
1. Every variant must score HIGHER than the original on 4U
2. Each variant uses a DIFFERENT pattern (avoid repetition)
3. At least 1 variant must include a number
4. At least 1 variant must be under 8 words (snappy)
5. Mark the ★ recommended variant
```

---

## Character Limit Validation

```yaml
platform_limits:
  email_subject: 50 chars (41 ideal — mobile preview cutoff)
  facebook_ad: 40 chars
  google_search: 30 chars per headline
  linkedin_ad: 70 chars
  blog_post: 60 chars (SEO title tag)
  twitter: 280 chars (full tweet as headline)
  push_notification: 65 chars

validation:
  under_limit: "✅ PASS"
  over_limit: "⚠️ OVER by [N] chars — truncated version suggested"
  multi_platform: "check all intended platforms simultaneously"
```

---

## Report Format

### Single Headline Report
```
╔══════════════════════════════════════════════════════╗
║  HEADLINE SCORE                                     ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  "7 Email Hacks That Doubled Our Reply Rate"         ║
║                                                      ║
║  Useful:        ★★★  (3/3) — clear benefit          ║
║  Urgent:        ★☆☆  (1/3) — no time pressure       ║
║  Unique:        ★★☆  (2/3) — "our" adds story       ║
║  Ultra-specific: ★★★  (3/3) — 7, doubled, reply rate ║
║                                                      ║
║  TOTAL: 9/12  ✅ STRONG                              ║
║                                                      ║
║  Pattern: Number-first (+15-25% CTR)                 ║
║  Power words: "hacks" (curiosity)                    ║
║  Chars: 43 ✅ (email: ✅ | fb: ⚠️+3 | google: ⚠️+13) ║
║                                                      ║
║  VARIANTS:                                           ║
║  V1: "Stop Losing Replies: 7 Fixes in 10 Min" (10)  ║
║  V2: "We Doubled Reply Rate — Here's the Secret" (9)║
║  ★V3: "Reply Rate Doubled in 7 Days (Copy This)" (11)║
╚══════════════════════════════════════════════════════╝
```

### Tournament Report (--tournament)
```
╔══════════════════════════════════════════════════════╗
║  HEADLINE TOURNAMENT — 10 contenders                ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  🥇 #7:  "Reply Rate Doubled in 7 Days"    (11/12)  ║
║  🥈 #3:  "3 CTAs That Convert 40% More"    (10/12)  ║
║  🥉 #1:  "Stop Losing Leads to Weak Copy"  (9/12)   ║
║  ...                                                 ║
║  💀 #9:  "Marketing Tips"                   (4/12)   ║
║                                                      ║
║  ★ RECOMMENDATION: Ship #7 as control,              ║
║    A/B test against #3.                              ║
╚══════════════════════════════════════════════════════╝
```

---

## Integration

| Direction | Target | Data |
|-----------|--------|------|
| Input ← | Any text with headlines | .md, .txt, stdin |
| Input ← | `brand_config.yaml` | Banned words / signature phrases |
| Output → | `copy_optimization_insights.md` | Winning patterns feed memory |
| Output → | `ab_testing_framework.md` | Top 2 headlines → A/B test queue |
| Output → | `copy_analyzer.py` | Headline score feeds overall copy score |
| Trigger | CLI or pipeline integration | Pre-publish quality gate |

## Dependencies

| Dependency | What | Why |
|------------|------|-----|
| `kc_campaign.md` | Campaign context | Funnel stage determines headline pattern priority |
| `knowledge_card_marketing.md` | 4U framework + headline patterns | Core scoring reference |
| `brand_voice_templates.md` | Tone/vocabulary settings | Variant generation respects brand voice |
| `ab_testing_framework.md` | Test queue | Tournament winners feed A/B pipeline |
