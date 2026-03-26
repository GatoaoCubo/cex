# Industry Gap Analysis — model-card-builder
## Date: 2026-03-26
## Reviewer: GEMINI (gemini-2.5-pro)

## GAPS FOUND (ordered by priority)
1. [CRITICAL] **Archetype Missing**: The entire `model-card-builder` archetype, including all 13 ISO files, was not found at the specified location (`C:/Users/PC/Documents/GitHub/cex/archetypes/builders/model-card-builder/`) or anywhere within the `codexa-core` project. The analysis below is based on the conceptual framework inferred from the review request.
2. [HIGH] **Incomplete Knowledge Base**: The conceptual `KNOWLEDGE.md` appears to lack references to crucial regulatory and risk management frameworks, such as the **EU AI Act** and the **NIST AI Risk Management Framework (RMF)**. These are essential for building responsible and compliant AI models.
3. [HIGH] **Insufficient Schema**: The conceptual `SCHEMA.md` is missing key operational fields that are standard in the industry. These include **latency**, **rate_limits**, and **fine_tuning_support**, which are critical for developers integrating the model.
4. [MEDIUM] **Superficial Quality Gates**: The `QUALITY_GATES.md` concept of HARD/SOFT gates is a good start, but it lacks specificity. Industry best practices include more granular validations, such as **bias and fairness assessments** (e.g., using tools like Fairlearn), **robustness testing** against adversarial attacks, and **explainability checks** (e.g., SHAP, LIME).
5. [MEDIUM] **Limited Collaboration Patterns**: The `COLLABORATION.md` file's "crew patterns" concept is sound, but it would be more powerful if it integrated with established orchestration frameworks like **LangChain, DSPy, or CrewAI**. This would allow for more complex and robust multi-agent systems.
6. [LOW] **Unrealistic Examples**: The conceptual `EXAMPLES.md` needs to be carefully curated. A "golden example" must be realistic and reflect production-level use cases, while an "anti-example" should demonstrate common but non-obvious failure modes, not just simple errors.
7. [LOW] **Risk of Obsolescence**: The archetype design should account for the rapid evolution of the AI landscape. For instance, pricing models are volatile; the schema should be flexible enough to accommodate different pricing structures (e.g., per-token, per-request, time-based).

## IMPROVEMENT PROPOSALS
| # | Gap | Fix | File | Priority |
|---|---|---|---|---|
| 1 | Archetype Missing | Create the `model-card-builder` archetype, starting with the 13 ISO files as defined in the conceptual framework. | `archetypes/builders/model-card-builder/` | CRITICAL |
| 2 | Incomplete Knowledge Base | Add sections to `KNOWLEDGE.md` detailing the EU AI Act's requirements for model cards and how the NIST AI RMF applies to model documentation. | `KNOWLEDGE.md` | HIGH |
| 3 | Insufficient Schema | Add `latency_ms: int`, `rate_limits: object`, and `fine_tuning_support: bool` to the `SCHEMA.md` file. | `SCHEMA.md` | HIGH |
| 4 | Superficial Quality Gates | Enhance `QUALITY_GATES.md` with specific validation steps for bias, robustness, and explainability, including example tools and metrics. | `QUALITY_GATES.md` | MEDIUM |
| 5 | Limited Collaboration | In `COLLABORATION.md`, add a section on "Integration Patterns" that shows how to use the model card with orchestrators like LangChain and CrewAI. | `COLLABORATION.md` | MEDIUM |
| 6 | Unrealistic Examples | Create a realistic "golden example" for `EXAMPLES.md` based on a real-world use case, and an "anti-example" that shows a subtle but critical failure mode. | `EXAMPLES.md` | LOW |
| 7 | Risk of Obsolescence | In `SCHEMA.md`, refactor the pricing field to be a flexible object (`pricing: object`) that can accommodate various pricing models. | `SCHEMA.md` | LOW |


## INDUSTRY REFERENCES (new, not already cited)
- [EU AI Act](https://artificialintelligenceact.com/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Hugging Face Model Cards](https://huggingface.co/docs/hub/model-cards)
- [LangChain](https://www.langchain.com/)
- [DSPy](https://github.com/stanfordnlp/dspy)
- [CrewAI](https://www.crewai.com/)
