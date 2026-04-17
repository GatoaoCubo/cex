---
id: kno_few_shot_example_n01
kind: few_shot_example
pillar: P01
nucleus: N01
title: "N01 Few Shot Example"
version: "1.0.0"
quality: 9.1
tags: [few_shot_example, n01, p01, analytical_envy, prompting]
density_score: 0.98
---
<!-- 8F: F1=few_shot_example/P01 F2=kc_few_shot_example+tpl_few_shot_example F3=nucleus_def_n01+kc_few_shot_example+ex_few_shot_example_agent_creation+research_brief_contract F4=example for comparative grounded outputs
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P01_knowledge/kno_few_shot_example_n01.md -->

# N01 Few Shot Example

## Purpose
N01 few-shot examples should teach comparative rigor, not only format.
Analytical Envy means the example must demonstrate how to contrast claims, surface proof strength, and preserve uncertainty.
A pretty example that omits evidence pressure teaches the wrong habit.

## Properties

| Property | Value |
|----------|-------|
| Kind | `few_shot_example` |
| Pillar | `P01` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Main teaching job | grounded comparative output |
| Best count per prompt | 2 to 3 |
| Preferred diversity | common case, edge case, conflict case |
| Must include | input, output, evidence behavior |
| Must avoid | generic confident synthesis without proof |
| Primary downstream use | research prompts and comparison prompts |

## N01 Example Thesis
The few-shot example is a behavior injector.
For N01 it should teach the model to:
- name the comparison frame
- separate source tiers
- preserve freshness
- admit unresolved gaps
- produce action-ready synthesis

## Target Output Style
A good N01 example output usually contains:
1. short answer
2. evidence table
3. confidence assessment
4. comparison note
5. next research gap

This is more useful than long explanatory prose because it mirrors how N01 artifacts are consumed downstream.

## Example Pair

| Field | Content |
|-------|---------|
| input | "Compare two AI providers for fast-moving pricing intelligence research." |
| output focus | comparative recommendation with citations and caveats |
| lesson | do not collapse price, freshness, and source quality into one sentence |

## Example Input
```text
Question: Which provider is better for weekly competitor pricing scans, Vendor A or Vendor B?
Scope: global SaaS pricing pages, weekly refresh
Need: recommendation plus evidence quality notes
```

## Example Output
```markdown
Recommendation: Vendor A is the better default for weekly pricing scans because its official pricing pages are easier to parse consistently and the evidence is fresher.

Evidence Table
| Vendor | Evidence strength | Freshness | Limitation |
|--------|-------------------|-----------|------------|
| Vendor A | high | current quarter | some enterprise quotes hidden behind sales flow |
| Vendor B | medium | mixed | public pricing often incomplete by region |

Confidence
- Overall confidence: medium-high
- Why: two tier_1 sources support Vendor A, while Vendor B depends on one tier_1 and one tier_3 forum report

Analytical Note
- Vendor B may still win for enterprise bundles, but current public evidence is weaker

Gap
- Verify regional enterprise pricing with a second tier_1 source before externalizing the claim
```

## Why This Example Works

| Feature | Benefit |
|---------|---------|
| explicit recommendation | teaches decision orientation |
| evidence table | teaches structure |
| confidence block | teaches calibrated certainty |
| analytical note | teaches honest tradeoff handling |
| gap section | teaches next-step curiosity under discipline |

## Selection Rules
1. Use examples derived from real N01 task patterns.
2. Include at least one example with conflicting sources.
3. Keep examples short enough to preserve prompt budget.
4. Prefer examples whose output could become a reusable artifact fragment.
5. Replace examples when the market or schema materially changes.

## Coverage Mix

| Example type | Why needed |
|--------------|------------|
| standard compare | baseline output behavior |
| conflict case | teaches tension handling |
| sparse evidence case | teaches restraint |
| matrix extraction case | teaches tabular discipline |

## Anti-Patterns
- examples that only teach tone
- outputs with no citations or confidence
- overly long chain-of-thought dumps
- unrealistic toy inputs unrelated to N01 work
- contradictory output schema across examples

## Injection Guidance
Use examples during F3 when:
- the prompt requests a structured comparison
- the model tends to overgeneralize
- evidence conflict needs calibration
- output schema compliance is critical

Do not over-inject.
Two sharp examples beat six noisy ones.

## N01 Decision
The N01 few-shot example should make the model envy stronger analysis.
That means every demonstration has to show not just what to say, but how to earn the right to say it.
