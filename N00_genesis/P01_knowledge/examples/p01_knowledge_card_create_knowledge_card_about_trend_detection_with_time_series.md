---
id: p01_kc_trend_detection_time_series
kind: knowledge_card
pillar: P01
title: "Trend Detection with Time Series Analysis"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
domain: time_series_analysis
quality: 9.2
tags: [trend-detection, time-series, mann-kendall, changepoint, decomposition, knowledge]
tldr: "Trend detection applies Mann-Kendall (p<0.05), SMA/EMA windows, and PELT/BOCPD changepoint algorithms to identify directional shifts in temporal data"
when_to_use: "When analyzing temporal data for monotonic trends, structural breaks, or seasonally-adjusted slope estimation"
keywords: [trend-detection, time-series, mann-kendall, stationarity, decomposition]
long_tails:
  - How to detect statistically significant trends in time series with Python
  - When to use Mann-Kendall vs linear regression for trend detection
  - How to separate trend from seasonality before testing for trend direction
axioms:
  - ALWAYS test stationarity (ADF p<0.05) before applying parametric trend tests
  - NEVER report slope without checking residual autocorrelation (Durbin-Watson 1.5–2.5)
  - IF data contains seasonality THEN decompose via STL first THEN test trend component
linked_artifacts:
  primary: null
  related: [p01_kc_trend_detection_contract]
density_score: 0.88
data_source: "https://www.statsmodels.org/stable/tsa.html"
related:
  - p06_schema_trend_detection
  - p12_wf_weekly_fashion_content
  - p10_out_trend_report
  - kc_usage_report
  - p02_agent_test_ops
---
# Trend Detection with Time Series Analysis

## Quick Reference
```yaml
topic: trend_detection_time_series
scope: Statistical trend identification in temporal datasets
owner: builder_agent
criticality: high
libraries: statsmodels, scipy, pymannkendall, ruptures
```

## Key Concepts
- **ADF Test**: Augmented Dickey-Fuller; H0 = unit root; p<0.05 → series is stationary
- **Mann-Kendall**: Non-parametric monotonic trend test; τ ∈ [-1,1]; no normality assumption
- **Theil-Sen Slope**: Median of all pairwise slopes; outlier-resistant vs OLS regression
- **STL Decomposition**: Loess-based split into trend, seasonal, residual components
- **PELT**: Pruned Exact Linear Time changepoint detection; O(n) complexity; multiple breaks
- **BOCPD**: Bayesian Online Changepoint Detection; real-time, probabilistic hazard rate

## Strategy Phases
1. **Preprocess**: Check stationarity (ADF), fill gaps, resample to uniform frequency
2. **Decompose**: Apply STL if Ljung-Box p<0.05 (autocorrelation); extract trend component
3. **Test**: Run Mann-Kendall on trend component; p<0.05 confirms monotonic direction
4. **Quantify**: Compute Theil-Sen slope; units = Δvalue/Δperiod with 95% CI
5. **Detect breaks**: Apply PELT (`pen=np.log(n)`) or BOCPD for structural slope shifts
6. **Validate**: Durbin-Watson on residuals (1.5–2.5 = OK); ACF/PACF confirms white noise

## Golden Rules
- DECOMPOSE before testing if seasonal frequency is known (daily/weekly/annual)
- USE Mann-Kendall for ordinal or non-normal data; linear regression for prediction intervals
- SET PELT penalty to `np.log(n)` (BIC) for automatic model order selection
- REPORT τ sign (direction) AND Theil-Sen slope (magnitude) together, not separately

## Flow
```text
[Raw Series]
    → [ADF Test] → non-stationary? → [Difference or Detrend]
                 → stationary?    → [Ljung-Box autocorrelation?]
                                        YES → [STL Decompose]
                                        NO  → [Direct trend test]
    → [Trend Component]
    → [Mann-Kendall]  → p<0.05 → trend confirmed; τ gives direction
    → [Theil-Sen]     → slope magnitude + 95% CI
    → [PELT / BOCPD]  → structural breaks indexed by timestamp
    → [Report: direction, slope, breaks, Durbin-Watson]
```

## Comparativo
| Method | Type | Assumption | Best For | Library |
|--------|------|------------|----------|---------|
| Mann-Kendall | Non-parametric | None | Monotonic trend, ordinal data | `pymannkendall` |
| Linear Regression | Parametric | Normal residuals | Slope + CI, forecasting | `scipy.stats.linregress` |
| Theil-Sen | Non-parametric | None | Outlier-robust slope estimate | `scipy.stats.theilslopes` |
| STL + trend | Decomposition | Period known | Seasonal series | `statsmodels.tsa.seasonal` |
| PELT | Changepoint | Gaussian / Poisson | Multiple structural breaks | `ruptures` |
| BOCPD | Bayesian | Hazard rate prior | Online / streaming data | `bayesian_changepoint_detection` |
| HP Filter | Smooth trend | Quadratic penalty | Macro / quarterly series | `statsmodels.tsa.filters.hp_filter` |

## References
- statsmodels TSA: https://www.statsmodels.org/stable/tsa.html
- pymannkendall: https://github.com/mmhs013/pyMannKendall
- ruptures (PELT/BOCPD): https://centre-borelli.github.io/ruptures-docs/
- Related: p01_kc_trend_detection_contract (signal schema + confidence-evidence mapping)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_trend_detection]] | downstream | 0.28 |
| [[p12_wf_weekly_fashion_content]] | downstream | 0.27 |
| [[p10_out_trend_report]] | downstream | 0.22 |
| [[kc_usage_report]] | sibling | 0.20 |
| [[p02_agent_test_ops]] | downstream | 0.16 |
