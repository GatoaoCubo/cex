---
kind: output_template
id: bld_output_template_interactive_demo
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for interactive_demo production
quality: 9.1
title: "Output Template Interactive Demo"
version: "1.0.1"
author: n02_marketing
tags: [interactive_demo, builder, output_template]
tldr: "Template with vars for interactive_demo production"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

<!-- Interactive demo script template. Guided-tour + talk track structure. Replace all {{vars}}. -->

```markdown
---
id: p05_id_{{name}}
kind: interactive_demo
pillar: P05
quality: null
title: {{title}}
product: {{product_name}}
audience: {{audience}}
duration_minutes: {{duration}}
use_case: {{primary_use_case}}
---

## Demo Overview
**Goal:** {{demo_goal}}
**Success metric:** {{success_metric}}
**Target persona:** {{persona}} -- {{persona_pain_point}}

## Talk Track: Opening ({{opening_duration}}s)
{{opening_narrative}}

**Discovery questions to ask:**
1. {{discovery_q1}}
2. {{discovery_q2}}

## Demo Flow

| Step | Screen/Feature | Action | Talk Track | Objection | Response |
|---|---|---|---|---|---|
| 1 | {{screen_1}} | {{action_1}} | {{talk_1}} | {{objection_1}} | {{response_1}} |
| 2 | {{screen_2}} | {{action_2}} | {{talk_2}} | {{objection_2}} | {{response_2}} |
| 3 | {{screen_3}} | {{action_3}} | {{talk_3}} | {{objection_3}} | {{response_3}} |
| 4 | {{screen_4}} | {{action_4}} | {{talk_4}} | {{objection_4}} | {{response_4}} |
| 5 | {{screen_5}} | {{action_5}} | {{talk_5}} | {{objection_5}} | {{response_5}} |

## Feature Deep Dives (optional branching)
| Feature | When to show | Trigger | Talk track |
|---|---|---|---|
| {{feature_1}} | {{condition_1}} | {{trigger_1}} | {{track_1}} |
| {{feature_2}} | {{condition_2}} | {{trigger_2}} | {{track_2}} |

## Proof Points
| Claim | Evidence | Customer Reference |
|---|---|---|
| {{claim_1}} | {{evidence_1}} | {{reference_1}} |
| {{claim_2}} | {{evidence_2}} | {{reference_2}} |

## Talk Track: Close ({{close_duration}}s)
{{close_narrative}}

**CTA:** {{call_to_action}}
**Next step:** {{next_step}}
```
