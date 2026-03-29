---
id: p05_rf_engineering_nucleus
kind: response_format
pillar: P05
title: "Response Format: Engineering Nucleus"
version: "1.0.0"
created: "2023-10-20"
updated: "2023-10-20"
author: "response-format-builder"
target_kind: "engineering_output"
format_type: "markdown"
injection_point: "system_prompt"
sections: [Introduction, Main Content, Conclusion, Additional Notes]
sections_count: 4
domain: "engineering"
quality: null
tags: [response-format, engineering, structured-output]
tldr: "Engineering output format: markdown with Introduction, Main Content, Conclusion, and Additional Notes sections."
example_output: "see body"
composable: false
density_score: 0.88
linked_artifacts:
  primary: "engineering-nucleus-output"
  related: [p06_vs_engineering_validation, p01_kc_problem_definition]
---
## Format Overview
This response format defines the structure for engineering output, consisting of four markdown sections: Introduction, Main Content, Conclusion, and Additional Notes. It is designed to ensure that engineering queries and solutions are presented in a coherent and organized manner. Injected in the system_prompt to maintain consistency across interactions.

## Sections
| # | Section          | Description                                                   | Required | Constraints                  |
|---|------------------|---------------------------------------------------------------|----------|------------------------------|
| 1 | Introduction     | Brief overview of the engineering topic or problem addressed. | yes      | Prose, max 3 sentences       |
| 2 | Main Content     | Detailed analysis and solution recommendations.               | yes      | At least 2 subsections, list |
| 3 | Conclusion       | Summary of key points and solutions.                          | yes      | Prose, max 2 paragraphs      |
| 4 | Additional Notes | References or specific engineering standards if applicable.   | no       | Key-value pairs, optional    |

## Example Output
---
markdown
## Introduction
The focus of this document is to explore the structural integrity aspects of high-rise buildings and the associated engineering challenges.

## Main Content

### Subsection 1 - Problem Definition
The key concern is the impact of wind loads on structural stability, particularly in regions susceptible to cyclones.

### Subsection 2 - Analysis/Explanation
The analysis involves using finite element modeling to predict stress distribution across different structural components under varying wind pressures.

### Subsection 3 - Solution or Recommendations
It is recommended to employ reinforced steel in critical load-bearing areas and conduct regular inspections using non-destructive testing methods.

## Conclusion
The analysis has highlighted that proper material selection and design adaptations can significantly enhance structural resilience against wind load.

## Additional Notes
- Refer to the Engineering Standards Manual for detailed guidelines on material specifications.
- Assumptions are based on standard wind load parameters as per the Regional Building Code.
```

## Injection Instructions
- **Point**: system_prompt
- **Position**: After identity rules, before task instructions
- **Template**: "Respond using the following format: concise markdown sections with Introduction, Main Content, Conclusion, and Additional Notes."
- **Composable**: false — This format is self-contained and structured to guide clear and consistent engineering outputs.

## References
- https://engineeringnucleus.example.com (2023-10-20)
- Engineering Standards Manual
```