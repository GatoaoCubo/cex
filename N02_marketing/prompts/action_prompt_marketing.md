---
id: p03_ap_generate_marketing_strategy
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2023-10-01"
updated: "2023-10-01"
author: "action-prompt-builder"
title: "Generate Marketing Strategy for Customer Segment"
action: "Create targeted marketing strategies from customer profile data"
input_required:
  - "customer_profiles: List of JSON objects containing demographic and behavioral data"
  - "objectives: List of marketing objectives as strings"
  - "budget: Dictionary with 'total' as a float and breakdown by channel"
output_expected: "Structured marketing strategy document in JSON format including target audience, channels, and budget"
purpose: "To create a comprehensive marketing strategy for targeting specific customer segments effectively within budget constraints."
steps_count: 4
timeout: "30s"
edge_cases:
  - "Missing demographic data for a segment"
  - "Budget breakdown per channel exceeds total budget"
constraints:
  - "Do NOT assume default demographics for missing data"
  - "Ensure total budget aligns with allocated channel budgets"
domain: "marketing"
quality: null
tags: [action_prompt, marketing, strategy, customer, budget]
tldr: "Create a marketing strategy using customer data and budget constraints"
density_score: 0.87
---
## Context
Creating a focused marketing strategy requires analyzing customer profiles and aligning strategies with specific marketing objectives and budget constraints. This prompt guides the LLM in generating a targeted marketing strategy using provided data. Purpose: to enable marketers to implement tailored campaigns effectively.

## Input
| Item                | Type                       | Format   | Required |
|---------------------|----------------------------|----------|----------|
| customer_profiles   | List of JSON objects       | Array    | YES      |
| objectives          | List of strings            | Array    | YES      |
| budget              | Dictionary with float keys | JSON     | YES      |

## Execution
1. Analyze the provided customer profile data to identify key audience segments.
2. Match objectives with potential marketing channels and opportunities.
3. Derive marketing strategies aligned with these objectives and customer segments.
4. Ensure strategies fit within the budget constraints, clearly detailing allocations and expected outcomes.

## Output
Format: JSON
Structure:
```json
{
  "target_audience": "Millennial tech-savvy professionals",
  "channels": [
    "social_media",
    "email_campaigns",
    "influencer_marketing"
  ],
  "budget_allocation": {
    "social_media": 5000,
    "email_campaigns": 3000,
    "influencer_marketing": 2000
  },
  "expected_roi": 1.5
}
```

## Validation
- All sections in the output have corresponding input reflections (target_audience matched).
- Budget allocations do not exceed the total provided budget.
- Edge case: If demographic data is missing, an appropriate strategy uses alternative data.
- Output is a JSON object with all specified keys: target_audience, channels, budget_allocation, and expected_roi.