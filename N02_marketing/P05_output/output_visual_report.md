---
id: p05_output_visual_report
kind: output_validator
pillar: P05
title: "Visual Report Template — Professional Long-Form"
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 9.2
tags: [output, template, report, print, tailwind]
tldr: "Professional report HTML — cover, executive summary, tables, charts, print-friendly."
density_score: 0.89
related:
  - p05_output_style_guide
  - p09_lpt_landing_page_template
  - p05_output_dashboard_ui
  - landing_page_petshop_crm
  - bld_examples_landing_page
  - p05_output_social_card
  - p01_kc_tailwind_patterns
  - p10_hos_html_output_visual_frontend
  - p09_ct_component_template
  - p10_dtc_design_token_contract
---

# Visual Report Template

## Purpose
Long-form professional report as styled HTML. Print-friendly with `@media print` rules.
Typography: Geist headings, Inter body, JetBrains Mono code blocks.

---

## Structure

```
1. Cover Page (title, date, logo, classification)
2. Table of Contents (auto-generated links)
3. Executive Summary (key findings, 3-5 bullets)
4. Section 1..N (heading hierarchy, content, data)
5. Data Tables (styled, alternating rows)
6. Chart Placeholders (dimensions for Recharts/Chart.js)
7. Conclusions & Recommendations
8. Appendix (raw data, methodology)
```

## Complete HTML Skeleton

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{REPORT_TITLE}} — CODEXA</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; color: #1a1a2e; }
    h1, h2, h3, h4 { font-family: 'Inter', sans-serif; font-weight: 700; }
    code, pre { font-family: 'JetBrains Mono', monospace; }

    /* Print styles */
    @media print {
      body { font-size: 11pt; color: #000; }
      .no-print { display: none !important; }
      .page-break { page-break-before: always; }
      a { color: #000; text-decoration: none; }
      table { page-break-inside: avoid; }
      h2, h3 { page-break-after: avoid; }
    }

    /* Cover page */
    .cover {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
      color: white;
      padding: 80px;
    }
  </style>
</head>
<body class="bg-white">

  <!-- COVER PAGE -->
  <section class="cover page-break">
    <div class="mb-auto flex items-center gap-3 pt-8">
      <div class="w-10 h-10 rounded-lg flex items-center justify-center font-bold text-black bg-[#50C878]">C</div>
      <span class="text-xl font-bold">CODEXA</span>
    </div>
    <div>
      <p class="text-sm uppercase tracking-widest text-gray-400 mb-4">{{REPORT_TYPE}}</p>
      <h1 class="text-5xl font-bold mb-6 leading-tight">{{REPORT_TITLE}}</h1>
      <p class="text-xl text-gray-300 max-w-2xl">{{REPORT_SUBTITLE}}</p>
    </div>
    <div class="mt-auto pb-8 flex gap-8 text-sm text-gray-400">
      <span>{{DATE}}</span>
      <span>{{AUTHOR}}</span>
      <span>{{CLASSIFICATION}}</span>
    </div>
  </section>

  <!-- TABLE OF CONTENTS -->
  <section class="max-w-4xl mx-auto px-8 py-16 page-break">
    <h2 class="text-2xl font-bold mb-8 text-gray-900">Table of Contents</h2>
    <nav class="space-y-3">
      <a href="#summary" class="flex justify-between text-gray-700 hover:text-[#50C878] border-b border-dotted border-gray-300 pb-1">
        <span>1. Executive Summary</span><span class="text-gray-400">3</span>
      </a>
      <a href="#analysis" class="flex justify-between text-gray-700 hover:text-[#50C878] border-b border-dotted border-gray-300 pb-1">
        <span>2. Analysis</span><span class="text-gray-400">5</span>
      </a>
      <a href="#data" class="flex justify-between text-gray-700 hover:text-[#50C878] border-b border-dotted border-gray-300 pb-1">
        <span>3. Data & Findings</span><span class="text-gray-400">8</span>
      </a>
      <a href="#conclusions" class="flex justify-between text-gray-700 hover:text-[#50C878] border-b border-dotted border-gray-300 pb-1">
        <span>4. Conclusions</span><span class="text-gray-400">12</span>
      </a>
      <a href="#appendix" class="flex justify-between text-gray-700 hover:text-[#50C878] border-b border-dotted border-gray-300 pb-1">
        <span>Appendix</span><span class="text-gray-400">14</span>
      </a>
    </nav>
  </section>

  <!-- EXECUTIVE SUMMARY -->
  <section id="summary" class="max-w-4xl mx-auto px-8 py-12 page-break">
    <h2 class="text-3xl font-bold mb-6 text-gray-900">1. Executive Summary</h2>
    <div class="bg-gray-50 rounded-xl p-6 mb-8 border-l-4 border-[#50C878]">
      <p class="text-gray-700 leading-relaxed">{{EXECUTIVE_SUMMARY}}</p>
    </div>
    <h3 class="text-xl font-semibold mb-4">Key Findings</h3>
    <ul class="space-y-3">
      <li class="flex gap-3"><span class="text-[#50C878] font-bold">01</span><span>{{FINDING_1}}</span></li>
      <li class="flex gap-3"><span class="text-[#50C878] font-bold">02</span><span>{{FINDING_2}}</span></li>
      <li class="flex gap-3"><span class="text-[#50C878] font-bold">03</span><span>{{FINDING_3}}</span></li>
    </ul>
  </section>

  <!-- DATA TABLE EXAMPLE -->
  <section id="data" class="max-w-4xl mx-auto px-8 py-12 page-break">
    <h2 class="text-3xl font-bold mb-6 text-gray-900">3. Data & Findings</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-gray-100 text-left">
            <th class="px-4 py-3 font-semibold text-gray-700">Metric</th>
            <th class="px-4 py-3 font-semibold text-gray-700">Baseline</th>
            <th class="px-4 py-3 font-semibold text-gray-700">Current</th>
            <th class="px-4 py-3 font-semibold text-gray-700">Change</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-gray-200">
            <td class="px-4 py-3">{{METRIC_1}}</td>
            <td class="px-4 py-3">{{BASELINE_1}}</td>
            <td class="px-4 py-3 font-semibold">{{CURRENT_1}}</td>
            <td class="px-4 py-3 text-green-600">{{CHANGE_1}}</td>
          </tr>
          <tr class="border-b border-gray-200 bg-gray-50">
            <td class="px-4 py-3">{{METRIC_2}}</td>
            <td class="px-4 py-3">{{BASELINE_2}}</td>
            <td class="px-4 py-3 font-semibold">{{CURRENT_2}}</td>
            <td class="px-4 py-3 text-green-600">{{CHANGE_2}}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Chart Placeholder -->
    <div class="mt-8 h-64 bg-gray-100 rounded-xl flex items-center justify-center text-gray-400 border-2 border-dashed border-gray-300">
      <p>Chart: {{CHART_TITLE}} (600×256px — Recharts / Chart.js)</p>
    </div>
  </section>

  <!-- CONCLUSIONS -->
  <section id="conclusions" class="max-w-4xl mx-auto px-8 py-12 page-break">
    <h2 class="text-3xl font-bold mb-6 text-gray-900">4. Conclusions & Recommendations</h2>
    <div class="space-y-4 text-gray-700 leading-relaxed">
      <p>{{CONCLUSION_TEXT}}</p>
    </div>
  </section>

  <!-- APPENDIX -->
  <section id="appendix" class="max-w-4xl mx-auto px-8 py-12 page-break">
    <h2 class="text-3xl font-bold mb-6 text-gray-900">Appendix</h2>
    <h3 class="text-lg font-semibold mb-3">Methodology</h3>
    <p class="text-gray-600 text-sm mb-6">{{METHODOLOGY}}</p>
    <h3 class="text-lg font-semibold mb-3">Raw Data</h3>
    <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg text-xs overflow-x-auto"><code>{{RAW_DATA}}</code></pre>
  </section>

  <!-- Footer (print) -->
  <footer class="max-w-4xl mx-auto px-8 py-8 text-center text-xs text-gray-400 border-t border-gray-200">
    <p>CODEXA — Confidential — {{DATE}}</p>
  </footer>

</body>
</html>
```

## Template Variables

| Variable | Description |
|----------|-------------|
| `{{REPORT_TITLE}}` | Main title on cover |
| `{{REPORT_SUBTITLE}}` | Subtitle / description |
| `{{REPORT_TYPE}}` | "Technical Report", "Quarterly Review", etc. |
| `{{DATE}}` | ISO date or localized |
| `{{AUTHOR}}` | Author name / team |
| `{{CLASSIFICATION}}` | "Internal", "Confidential", "Public" |
| `{{EXECUTIVE_SUMMARY}}` | 2-3 paragraph summary |
| `{{FINDING_N}}` | Key findings (numbered) |
| `{{METRIC_N}}` / `{{BASELINE_N}}` / `{{CURRENT_N}}` / `{{CHANGE_N}}` | Table data |
| `{{CHART_TITLE}}` | Chart placeholder label |

## Print Output
- `Ctrl+P` or `window.print()` generates clean PDF
- Cover page on page 1, ToC on page 2
- Tables avoid page breaks
- Headers avoid orphaning

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_output_style_guide]] | sibling | 0.57 |
| [[p09_lpt_landing_page_template]] | sibling | 0.49 |
| [[p05_output_dashboard_ui]] | sibling | 0.47 |
| [[landing_page_petshop_crm]] | related | 0.45 |
| [[bld_examples_landing_page]] | upstream | 0.44 |
| [[p05_output_social_card]] | sibling | 0.37 |
| [[p01_kc_tailwind_patterns]] | upstream | 0.35 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.34 |
| [[p09_ct_component_template]] | sibling | 0.32 |
| [[p10_dtc_design_token_contract]] | downstream | 0.32 |
