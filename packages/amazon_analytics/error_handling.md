# Amazon Analytics Agent — Error Handling

## Failure Mode 1: Insufficient Data Period

**Severity**: HIGH | **Frequency**: Common

Analysis period < 7 days produces unreliable signals. ACOS swings wildly between days.

**Detection**: `period_days < 7` or `clicks < 100`

**Recovery**:
```yaml
status: WARNING
error:
  code: INSUFFICIENT_DATA
  message: "Only {{N}} days of data. Minimum 7 days required."
  suggestion: "Wait for more data. Use 14-day window for strategic decisions."
partial_analysis: true
confidence: 0.45
```

**Prevention**: Enforce minimum 7-day window. Show confidence score based on volume.

---

## Failure Mode 2: ACOS Without Margin Context

**Severity**: CRITICAL | **Frequency**: Common

ACOS without margin context makes diagnosis meaningless. ACOS 20% is "Aceitavel" with 40% margin but means losing money with 18% margin.

**Detection**: `target_margin` not provided or `MPA < 0`

**Recovery**:
```yaml
status: CRITICAL
error:
  code: ACOS_EXCEEDS_MARGIN
  message: "ACOS {{X}}% exceeds margin {{Y}}%. MPA = {{Z}}%. Losing money on ads."
  recommendation: "Reduce ACOS to max {{Y}}% or ideally {{Y/2}}%."
```

**Prevention**: ALWAYS require `target_margin`. Calculate and display MPA prominently.

---

## Failure Mode 3: Misleading Organic vs Paid Split

**Severity**: MEDIUM | **Frequency**: Occasional

Ads boost organic visibility (halo effect). Stopping ads may crash organic sales too.

**Detection**: Organic drops > 20% after ad budget reduction

**Recovery**:
```yaml
status: WARNING
warning:
  code: ORGANIC_AD_DEPENDENCY
  message: "Organic sales may drop 20-40% if ads are paused."
  recommendation: "Never pause ads completely. Reduce gradually (20%/week)."
```

**Prevention**: Track organic sales trend during budget changes. Calculate TACOS always.

---

## Failure Mode 4: Seasonality Skew

**Severity**: MEDIUM | **Frequency**: Periodic

Black Friday, Prime Day, and holidays distort metrics. CPC spikes 30-40% during events.

**Detection**: Analysis period overlaps known seasonal events:
- Prime Day (July), Dia dos Pais (August), Black Friday (November), Natal (December)

**Recovery**: Flag seasonal context. Compare year-over-year, not week-over-week.

**Prevention**: Add seasonal context to all reports. Do NOT make bid changes based solely on seasonal data.

---

## Failure Mode 5: New vs Mature Product Comparison

**Severity**: HIGH | **Frequency**: Common

New product (Month 1) ACOS 35% is normal launch phase, not a crisis. Premature campaign termination kills maturation.

**Detection**: `product_age_months <= 3` with ACOS compared to mature benchmarks

**Recovery**: Apply age-adjusted benchmarks. Show maturation timeline.

```yaml
context:
  product_age: "1 month"
  maturity_phase: launch
  expected_acos_range: "25-40%"
  current_acos: 35
  verdict: "NORMAL for launch phase"
recommendation: "Do not panic. Focus on keyword harvesting. Reassess at month 3."
```

**Prevention**: Always ask product age. Show maturity-adjusted benchmarks.

---

## Failure Mode 6: Missing Buy Box Data

**Severity**: MEDIUM | **Frequency**: Occasional

Low conversion may be caused by Buy Box suppression, not listing quality.

**Detection**: `buy_box_percentage` not provided or < 50%

**Recovery**:
```yaml
warning:
  code: MISSING_BUY_BOX
  message: "Buy Box data not provided. Low conversion may be Buy Box issue."
  recommendation: "Check Seller Central > Business Reports > Buy Box %. If < 80%, fix pricing first."
```

**Prevention**: Include `buy_box_percentage` as recommended input. Flag low conversion + missing Buy Box.

---

## Error Codes Reference

| Code | Severity | Auto-Recovery |
|------|----------|---------------|
| `INSUFFICIENT_DATA` | HIGH | No (wait for data) |
| `ACOS_EXCEEDS_MARGIN` | CRITICAL | No (strategy change) |
| `ORGANIC_AD_DEPENDENCY` | MEDIUM | Yes (gradual reduction) |
| `SEASONAL_SKEW` | MEDIUM | Yes (flag + adjust) |
| `MATURITY_MISMATCH` | HIGH | Yes (adjust benchmark) |
| `MISSING_BUY_BOX` | MEDIUM | Yes (flag + estimate) |
| `INVALID_METRIC` | LOW | No (data correction) |
| `ZERO_IMPRESSIONS` | HIGH | No (check targeting) |

---

## Partial Data Protocol

When data is incomplete but partial analysis is possible:

1. Proceed with available fields
2. Add `data_quality_warnings` array to output
3. Mark estimates vs actuals in metrics_summary
4. Cap confidence: score max = 6.0 when > 2 fields missing
5. Add recommendation: "Completar dados para analise definitiva"

## Output Validation Checklist

Before returning any output, verify:
- `traffic_light` is not null
- `score` is between 0.0 and 10.0
- At least 2 recommendations present
- No recommendation without a metric reference
- `projected_improvement` is specific (not "will improve")
- `diagnosis` mentions at least one actual number
