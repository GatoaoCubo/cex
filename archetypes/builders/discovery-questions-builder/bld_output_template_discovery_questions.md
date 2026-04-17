---
kind: output_template
id: bld_output_template_discovery_questions
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for discovery_questions production
quality: 9.1
title: "Output Template Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, output_template]
tldr: "Template with vars for discovery_questions production"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p01_dq_{{slug}}
kind: discovery_questions
pillar: P01
title: "{{title}}"
version: "1.0.0"
author: "{{author}}"
created: "{{created}}"
updated: "{{updated}}"
domain: "{{domain}}"
quality: null
tags: [{{tags}}]
tldr: "{{tldr}}"
question_type: "{{question_type}}"
target_audience: "{{target_audience}}"
---
```

<!-- slug: lowercase-underscore identifier, e.g. saas_cfo_stage2 -->
<!-- title: Descriptive name, e.g. "CFO ROI Discovery - Stage 2" -->
<!-- domain: Sales domain context, e.g. "SaaS enterprise", "manufacturing" -->
<!-- question_type: "open-ended" | "probing" | "qualification" -->
<!-- target_audience: Buyer persona, e.g. "CFO", "IT Director", "Champion" -->

## Personas

| Persona | Role | Pain Points | Decision Criteria |
|---------|------|-------------|-------------------|
| {{persona_1}} | {{role_1}} | {{pain_1}} | {{criteria_1}} |
| {{persona_2}} | {{role_2}} | {{pain_2}} | {{criteria_2}} |

## Discovery Questions by Stage

### Stage 1: Qualification (BANT)
| Framework | Question | Intent |
|-----------|----------|--------|
| Budget | {{q_budget}} | Uncover spend authority |
| Authority | {{q_authority}} | Identify decision-maker |
| Need | {{q_need}} | Surface pain points |
| Timeline | {{q_timeline}} | Establish urgency |

### Stage 2: Solution Fit (MEDDIC)
| Criterion | Question | Expected Insight |
|-----------|----------|-----------------|
| Metrics | {{q_metrics}} | Quantify success criteria |
| Economic Buyer | {{q_economic_buyer}} | Confirm budget authority |
| Decision Criteria | {{q_decision_criteria}} | Understand evaluation factors |
| Identify Pain | {{q_pain}} | Deepen problem understanding |
| Champion | {{q_champion}} | Validate internal sponsor |

### Stage 3: Closing / Negotiation
| Scenario | Question | Goal |
|----------|----------|------|
| Urgency probe | {{q_urgency}} | Surface timeline drivers |
| Objection test | {{q_objection}} | Pre-handle blockers |
| Commitment | {{q_commitment}} | Move to next step |
