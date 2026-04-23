---
kind: knowledge_card
id: bld_knowledge_card_pitch_deck
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for pitch_deck production
quality: 9.2
title: "Knowledge Card Pitch Deck"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pitch_deck, builder, knowledge_card]
tldr: "Domain knowledge for pitch_deck production"
domain: "pitch_deck construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_pitch_deck_builder
  - bld_tools_pitch_deck
  - bld_instruction_pitch_deck
  - pitch-deck-builder
  - p10_mem_pitch_deck_builder
  - p05_qg_pitch_deck
  - kc_pitch_deck
  - bld_output_template_pitch_deck
  - bld_examples_pitch_deck
  - p10_out_market_snapshot
---

## Domain Overview
A pitch deck is a concise, visual narrative used to communicate a business opportunity to investors, typically structured around problem/solution, traction, and funding ask. It serves as a high-level overview, emphasizing scalability, market potential, and team credibility. Unlike case studies, which focus on detailed narratives, or pricing pages, which highlight tiered offerings, pitch decks prioritize brevity and strategic alignment with investor priorities. Key slides often include problem/solution, market size, traction, team, and ask, with data-driven storytelling to validate assumptions and demonstrate ROI potential.

The structure adheres to venture capital (VC) norms, where clarity and confidence are critical. Investors evaluate execution risk, market opportunity, and unit economics, requiring pitch decks to balance technical depth with accessibility. Common frameworks like the Business Model Canvas or Lean Startup principles inform slide content, ensuring alignment with stages of startup growth and investor expectations.

## Key Concepts
| Concept               | Definition                                                                 | Source                          |
|----------------------|----------------------------------------------------------------------------|----------------------------------|
| Problem Statement    | Clear, specific description of a market pain point with quantified impact  | Harvard Business Review        |
| Solution             | Product/service that directly addresses the problem with unique value      | The Lean Startup (Eric Ries)   |
| Traction             | Metrics proving demand (e.g., users, revenue, partnerships)                | Startup School (accelerator)   |
| Ask                  | Specific funding amount, use of funds, and expected ROI                    | PitchBook Data                 |
| TAM/SAM/SOM          | Total Addressable Market, Serviceable Available Market, Serviceable Obtainable Market | Standard & Poor’s Reports      |
| CAC/LTV              | Customer Acquisition Cost vs. Lifetime Value                               | Bain & Company                 |
| Customer Segments    | Defined target markets based on demographics, behavior, or needs           | Customer Development Model     |
| Value Proposition    | Unique benefit delivered to customers                                      | Value Proposition Canvas       |
| Competitive Advantage| Sustainable edge over rivals (e.g., IP, network effects)                   | Porter’s Five Forces           |
| Go-to-Market Strategy| Plan for customer acquisition, pricing, and distribution                   | Harvard Business Review        |

## Narrative Arc (mandatory through-line)
problem -> why now -> solution -> market -> product -> business model -> traction -> team -> financials -> ask

## Slide Framework Reference
| Framework | Structure | Best For |
|---|---|---|
| 10-slide VC template | problem/why-now/solution/market/product/biz-model/traction/team/financials/ask (10 slides) | Series A/B fundraising |
| Compressed 7-slide structure | problem/solution/why-now/market/traction/team/ask (7 slides, compressed) | Pre-seed/seed |
| 10/20/30 rule | 10 slides, 20 minutes, 30pt minimum font | Demo Day / short-form pitches |
| Social proof deck | Social proof + market size emphasis | Consumer marketplace |

## Why Now? (mandatory slide)
The "Why Now?" slide is the most differentiated and most frequently missing slide.
It answers: what has changed in the world that makes this the right moment?
Catalysts: regulatory shifts, technology unlock (LLMs, new API), behavioral change post-pandemic, incumbent exit.

## Industry Standards
- 10-slide VC pitch deck template (classic structure)
- Accelerator application and fundraising milestones
- 10/20/30 rule (10 slides, 20 minutes, 30pt font)
- Business Model Canvas (Osterwalder & Pigneur)
- Lean Startup (Eric Ries)
- TAM/SAM/SOM framework
- Customer Development Model (Steve Blank)
- Porter’s Five Forces (competitive moat analysis)

## Common Patterns
1. Problem/solution narrative with data-driven validation
2. Traction slides using metrics (users, revenue, growth rates)
3. Ask aligned with stage-specific funding benchmarks
4. Visual storytelling (charts, icons, minimal text)
5. Team slide emphasizing relevant experience and network

## Pitfalls
- Vague problem statements without quantified impact
- Overhyping solution without addressing scalability risks
- Traction slides lacking context (e.g., no benchmarking)
- Unclear ask with no tie to milestones or ROI
- Ignoring competition or underestimating barriers to entry

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_pitch_deck_builder]] | downstream | 0.53 |
| [[bld_tools_pitch_deck]] | downstream | 0.44 |
| [[bld_instruction_pitch_deck]] | downstream | 0.42 |
| [[pitch-deck-builder]] | downstream | 0.42 |
| [[p10_mem_pitch_deck_builder]] | downstream | 0.38 |
| [[p05_qg_pitch_deck]] | downstream | 0.38 |
| [[kc_pitch_deck]] | sibling | 0.33 |
| [[bld_output_template_pitch_deck]] | downstream | 0.32 |
| [[bld_examples_pitch_deck]] | downstream | 0.28 |
| [[p10_out_market_snapshot]] | downstream | 0.26 |
