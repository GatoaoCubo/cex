---
id: p01_kc_trend_detection_time_series
kind: knowledge_card
pillar: P01
title: "Trend Detection Algorithms for Time Series Analysis"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: time_series_analysis
quality: 0.0
tags: [trend-detection, time-series, algorithms, forecasting, signal-processing, knowledge]
tldr: "Trend detection in time series uses Mann-Kendall test (p<0.05 threshold), moving averages (SMA/EMA), and regression slopes to identify statistically significant directional changes"
when_to_use: "When analyzing time series data to identify upward, downward, or cyclic trends for forecasting or anomaly detection"
keywords: [trend-detection, mann-kendall, moving-average, regression-slope, time-series]
long_tails:
  - How to implement Mann-Kendall test for trend detection in Python
  - What is the optimal window size for moving average trend detection
  - How to detect seasonal trends vs linear trends in time series
axioms:
  - ALWAYS test for stationarity before applying trend detection algorithms
  - NEVER use trend detection on data with strong seasonality without detrending first
  - IF p-value < 0.05 in Mann-Kendall test THEN trend is statistically significant
linked_artifacts:
  primary: null
  related: [p01_kc_time_series_forecasting]
density_score: 0.87
data_source: "https://docs.scipy.org/doc/scipy/reference/stats.html#trend-tests"
---

# Trend Detection Algorithms for Time Series Analysis

## Quick Reference
| Parameter | Method | Typical Value | Decision Rule |
|-----------|---------|---------------|---------------|
| **p-value** | Mann-Kendall | < 0.05 | Significant trend exists |
| **ADF statistic** | Stationarity | < -3.45 (1%) | Series is stationary |
| **Window size** | Moving Average | 20-50 periods | Shorter = more sensitive |
| **λ (lambda)** | HP Filter | 1600 (quarterly), 14400 (annual) | Higher = smoother trend |
| **|t-statistic|** | Linear Regression | > 2.0 | Slope significantly ≠ 0 |

## Key Concepts
- **Mann-Kendall Test**: Non-parametric test for monotonic trend; H0: no trend, p<0.05 rejects null
- **Theil-Sen Slope**: Robust median-based slope estimator; outlier-resistant vs OLS regression
- **Moving Average Crossover**: SMA(short) vs SMA(long); bullish when short > long, bearish opposite
- **Linear Regression Slope**: β1 coefficient; positive = uptrend, negative = downtrend, |t-stat| > 2 significant
- **LOWESS/LOESS**: Locally weighted regression; smooths noise while preserving trend structure
- **Hodrick-Prescott Filter**: Decomposes series into trend + cycle; λ=1600 for quarterly, λ=14400 annual

## Strategy Phases
1. **Preprocess**: Remove outliers via IQR method, handle missing values, check for stationarity (ADF test)
2. **Decompose**: Separate trend from seasonal/cyclical components using STL or X-13-ARIMA
3. **Apply Tests**: Run Mann-Kendall for significance, calculate Theil-Sen slope for magnitude
4. **Validate**: Cross-validate on holdout period, compare multiple detection methods
5. **Interpret**: Contextualize trend strength, duration, and statistical confidence

## Golden Rules
- TEST stationarity first: non-stationary data produces spurious trends
- DETREND seasonal data: seasonal patterns mask underlying trends
- VALIDATE on out-of-sample data: avoid overfitting to historical patterns
- COMBINE methods: single algorithm may miss complex trend patterns

## Flow
```text
[Raw Data] -> [Stationarity Test] -> [Decomposition] -> [Trend Tests]
                     |                      |               |
                ADF p<0.05              STL/X-13      Mann-Kendall
                     |                      |               |
              [Differencing] -> [Detrended Series] -> [Slope + p-value]
```

## Comparison
| Method | Type | Pros | Cons | Best Use |
|--------|------|------|------|----------|
| Mann-Kendall | Non-parametric | Robust to outliers | No slope magnitude | Significance testing |
| Linear Regression | Parametric | Simple, interpretable | Sensitive to outliers | Clean linear trends |
| Theil-Sen | Non-parametric | Outlier resistant | Computationally intensive | Noisy data |
| Moving Average | Smoothing | Real-time capable | Lagging indicator | Trading signals |
| HP Filter | Decomposition | Separates components | End-point bias | Economic analysis |

## References
- Source: https://docs.scipy.org/doc/scipy/reference/stats.html#trend-tests
- Related: https://otexts.com/fpp3/decomposition.html
- Implementation: scikit-learn.preprocessing.detrend, scipy.stats.mannwhitneyu