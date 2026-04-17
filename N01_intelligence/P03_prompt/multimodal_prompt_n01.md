---
id: multimodal_prompt_n01
kind: multimodal_prompt
pillar: P03
nucleus: n01
title: "N01 Multimodal Research Prompts"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [multimodal_prompt, vision, charts, screenshots, n01, analytical_envy, image_analysis]
tldr: "Multimodal prompts for N01 research from visual sources: competitor UI screenshots, pricing table images, chart/graph analysis, LinkedIn profile screenshots. Extracts structured intelligence from images using Claude Vision."
density_score: 0.87
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P03/multimodal_prompt F2 become=multimodal-prompt-builder F3 inject=action_prompt_n01+data_extractor_n01+browser_tool_n01 F4 reason=competitor pricing pages, product screenshots, and charts are often better captured as images than parsed as HTML -- multimodal fills the gap in pure-text extraction F5 call=cex_compile F6 produce=multimodal_prompt_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P03_prompt/ -->

## Purpose

Some intelligence sources are inherently visual:
- Competitor UI screenshots (feature matrix capture)
- Pricing table images (when HTML is inaccessible)
- Financial charts (trend data in image form)
- LinkedIn profile screenshots (organizational data)
- App store screenshots (product feature evidence)

These multimodal prompts extract structured intelligence from images using Claude's vision capability.

## MP-01: Pricing Table Extraction

```
Image: {screenshot of pricing page}

Extract all pricing information from this image.
Output as JSON array. Include:
- tier_name: string
- price_monthly: float (USD)
- price_annual: float or null (USD)
- key_features: list[string] (all listed features)
- target_segment: string (inferred: individual / team / enterprise)
- cta_text: string (button text)

If the image is blurry or text is unreadable, return extraction_confidence < 0.5.
Never guess prices -- return null if not clearly visible.
```

## MP-02: Competitor UI Feature Analysis

```
Image: {screenshot of competitor product UI}

Analyze this UI screenshot for feature intelligence.
Output:
1. Product area (what part of the product is shown)
2. Visible features (list of UI elements and their function)
3. UX quality indicators (loading states, empty states, responsive design visible)
4. Competitive signals (anything that suggests a strategic product direction)
5. Missing features (common features NOT present that competitors offer)

Confidence note: visual inference from one screenshot has [confidence: 0.6-0.75].
Mark any inference beyond what is visually explicit as [INFERRED].
```

## MP-03: Chart / Graph Intelligence Extraction

```
Image: {chart or graph screenshot}

Extract the data from this chart.
1. Chart type (bar, line, scatter, pie, etc.)
2. X-axis: label and value range
3. Y-axis: label and value range
4. Data series: names and approximate values at key points
5. Trend direction: RISING / FALLING / STABLE / VOLATILE
6. Notable annotations or highlights in the chart

If approximate: provide range (e.g., "between 45-55%").
State extraction_confidence based on chart readability.
```

## MP-04: LinkedIn Profile Analysis

```
Image: {LinkedIn profile screenshot}

Extract professional intelligence:
1. Name and current title
2. Current company and inferred tenure
3. Previous companies (career trajectory)
4. Education background
5. Skills listed (visible)
6. Recent activity signals (if visible: posts, likes)

Strategic implication: what does this career trajectory signal
about the company's strategic direction?

[confidence: 0.7 for explicit fields; 0.5 for inferences]
```

## MP-05: Competitive Matrix Screenshot

```
Image: {feature comparison table image}

Extract the competitive matrix data:
1. Companies in columns (list)
2. Features in rows (list)
3. Cell values (yes / no / partial / price)
4. Highlighted cells (competitive advantages being claimed)

Output as JSON:
{
  "companies": [list],
  "features": [list],
  "matrix": [[values per row per company]],
  "highlighted": [{"company": str, "feature": str, "type": "advantage|gap"}]
}
```

## Usage Integration

```python
screenshot = browser_tool_n01.capture(url, selector=".pricing-table")
prompt = MULTIMODAL_PROMPTS["MP-01"]
result = claude.messages.create(
    model="claude-opus-4-6",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image", "source": {"type": "base64", "data": screenshot}},
            {"type": "text", "text": prompt}
        ]
    }]
)
structured_data = json.loads(result.content[0].text)
```

## Extraction Quality Notes

| Source Type | Expected Accuracy | Confidence Range |
|-------------|-----------------|-----------------|
| Pricing table (clean screenshot) | 92% | 0.85-0.95 |
| Complex UI screenshot | 75% | 0.65-0.80 |
| Chart (clean, labeled) | 85% | 0.75-0.90 |
| Chart (complex, small) | 60% | 0.50-0.65 |
| LinkedIn profile | 88% | 0.80-0.90 |

## Comparison vs. Alternatives

| Approach | Visual Data | Structured | N01 Fit |
|----------|------------|------------|---------|
| HTML parsing only | misses images | yes | fails on image-only data |
| OCR (Tesseract) | text from images | no | unstructured output |
| This (Claude Vision) | full image analysis | yes (JSON) | optimal |
| GPT-4V | full image analysis | yes | comparable, use for validation |
