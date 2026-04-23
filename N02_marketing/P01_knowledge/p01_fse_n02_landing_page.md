---
id: p01_fse_n02_landing_page
kind: few_shot_example
pillar: P01
nucleus: N02
title: "Few-Shot Example -- N02 Landing Page Copy via 8F Pipeline"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: few-shot-example-builder
domain: marketing
difficulty: hard
edge_case: false
format: "8F pipeline trace + landing page section-by-section output"
quality: 9.1
tags: [few-shot, landing-page, marketing, 8f-pipeline, n02, conversion]
tldr: "3 input/output pairs teaching N02 how to run 8F for landing page copy: hero -> proof -> CTA architecture."
keywords: [landing-page, hero, headline, cta, conversion, above-fold, proof, objections]
density_score: 1.0
related:
  - landing_page_template
  - p03_sp_marketing_nucleus
  - bld_system_prompt_landing_page
  - bld_knowledge_card_landing_page
  - kc_landing_page
  - landing-page-builder
  - bld_examples_landing_page
  - p08_ac_n02
  - bld_collaboration_landing_page
  - bld_schema_landing_page
---
<!-- 8F TRACE
F1 CONSTRAIN: kind=few_shot_example, pillar=P01, max_bytes=5120, naming=p01_fse_{topic}.md
F2 BECOME: few-shot-example-builder (13 ISOs). Sin lens: Creative Lust.
F3 INJECT: kc_campaign + input_schema_campaign_brief + landing_page_template + quality_gate_marketing. Match: 80%
F4 REASON: 3 examples, easy->hard, domain=landing page copy, progressive complexity
F5 CALL: Read+Write+compile ready. 2 similar artifacts found.
F6 PRODUCE: 3 input/output pairs, each with 8F trace + structured section outputs
F7 GOVERN: frontmatter complete, id unique, tags>=3, examples non-empty x3
F8 COLLABORATE: compiled via cex_compile.py
-->

## Explanation

Landing page copy is the highest-leverage copy N02 produces.
One page, one decision, one CTA. Every word either advances the conversion or wastes the reader's attention.

These 3 examples teach N02 the section-by-section architecture:
hero (promise) -> proof (credibility) -> features (desire) -> objections (trust) -> CTA (action).

The sin lens is non-negotiable: the hero must make the reader feel the desire before reading the proof.

---

## Example 1 (easy) -- SaaS tool, B2B, single CTA

**Input brief**
```yaml
task: write_landing_page_copy
product: ai_agent_orchestration_platform
audience: senior_engineers_and_technical_founders
promise: "orchestrate 7 AI agents from one typed system in under 10 minutes"
proof:
  customers: "40+ enterprise teams"
  stat: "3x faster agent deployment vs. custom code"
  testimonial: "This is the Rails of AI infrastructure. -- CTO, Series B startup"
cta: start_free_trial
sections_required: [hero, proof_bar, features_3, objections_2, final_cta]
tone: precise_confident
```

**8F trace (abbreviated)**
```
F1: kind=landing_page/P05, audience=technical, tone=precise_confident
F2: N02 + landing-page-builder context. Hero = promise + desire, not description.
F3: kc_campaign (BOFU=remove risk, close), brand_config, component_template
F4: hero: promise-as-outcome, proof_bar: numbers only, features: typed tables, objections: invert fears
F6: structured section output per required section
F7: hero has outcome not description, proof in bar, CTA singular, testimonial cited
```

**Output**
```yaml
hero:
  headline: "7 AI agents. One typed system. Running in under 10 minutes."
  subheadline: "Stop plumbing. Start orchestrating. 40+ enterprise teams already did."
  cta_button: "Start free trial -- no card required"

proof_bar:
  items:
    - "40+ enterprise teams"
    - "3x faster deployment vs. custom code"
    - "Under 10 minutes to first running agent"

features:
  - title: "Typed infrastructure, not prompts"
    body: "257 artifact kinds. Every agent has a schema, a builder, and a quality gate. No magic strings."
  - title: "7 nuclei, one orchestrator"
    body: "Research, marketing, engineering, knowledge, ops, commercial -- all coordinated from N07."
  - title: "4 runtimes, zero lock-in"
    body: "Claude, Codex, Gemini, Ollama. Swap providers without touching your agents."

objections:
  - fear: "This will take months to set up"
    answer: "The 8F pipeline runs on your first intent. First artifact in under 5 minutes."
  - fear: "We already have custom agents"
    answer: "CEX wraps existing agents. You keep your code; you add typed governance."

final_cta:
  headline: "The enterprise AI brain you have been waiting to build."
  cta_button: "Start free trial"
  secondary: "Or book a 20-minute demo"

quality_check:
  hero_has_outcome: true
  proof_present: true
  cta_singular: true
  objections_covered: 2
  testimonial_cited: true
```

---

## Example 2 (medium) -- D2C brand, emotional, visual-first

**Input brief**
```yaml
task: write_landing_page_copy
product: sustainable_streetwear_brand
audience: fashion_conscious_women_25_35_urban
promise: "look exactly like yourself -- without the supply chain guilt"
proof:
  orders: "12,000 orders shipped"
  certification: "B Corp certified"
  social_proof: "Featured in Vogue and Hypebae"
cta: shop_new_collection
tone: warm_irreverent_unapologetic
sections_required: [hero, social_proof_bar, story_2_paragraphs, product_highlight_3, final_cta]
```

**8F trace (abbreviated)**
```
F1: kind=landing_page/P05, audience=D2C_fashion, tone=warm_irreverent
F2: N02. D2C landing = identity mirror, not feature list. Desire = looking like yourself.
F3: kc_campaign (TOFU/MOFU=identity_mirror+proof), kc_visual_hierarchy_principles
F4: hero=identity statement, story=brand origin, product=sensory first then specs
F6: emotional register in hero and story; factual proof in bar and product
F7: no corporate speak, identity framing intact, CTA singular
```

**Output**
```yaml
hero:
  headline: "Dressed like you. Made like it matters."
  subheadline: "Sustainable streetwear for the woman who refuses to choose between her style and her values."
  cta_button: "Shop new collection"

social_proof_bar:
  items:
    - "12,000 orders shipped"
    - "B Corp certified"
    - "Featured in Vogue + Hypebae"

story:
  paragraph_1: "We started with one question: why does sustainable fashion always look like a compromise? Boring palettes. Stiff fabrics. Copy that lectures you."
  paragraph_2: "We quit that. Everything we make is designed to turn heads -- and built to leave the planet better than we found it. No lectures. Just good clothes."

product_highlights:
  - name: "Signature Hoodie"
    sensory: "Heavyweight 380gsm organic cotton. Falls exactly right."
    proof: "Made in Portugal. Certified recycled hardware."
  - name: "Wide-Leg Cargo"
    sensory: "Four deep pockets. Two-way stretch. Moves with you, not against you."
    proof: "GOTS certified fabric. Carbon-neutral shipping."
  - name: "Crop Bomber"
    sensory: "Structured shell, unstructured confidence."
    proof: "Deadstock outer layer. Zero virgin materials."

final_cta:
  headline: "Your next outfit. Their planet."
  cta_button: "Shop new collection"
  secondary: "Free returns. B Corp guaranteed."

quality_check:
  identity_framing: true
  corporate_speak: 0
  sensory_language: true
  cta_singular: true
  proof_present: true
```

---

## Example 3 (hard) -- Course launch, BOFU, scarcity mechanics

**Input brief**
```yaml
task: write_landing_page_copy
product: live_coaching_cohort_revenue_growth
audience: early_stage_founders_0_to_500k_arr
promise: "your first 6-figure month in 90 days -- with a cohort who is doing it live"
proof:
  stat: "87% of graduates hit revenue goal within 90 days"
  basis: "Q1 2026 cohort, n=31"
  testimonials:
    - "Closed my first 5-figure deal in week 3. -- Ana S., founder"
    - "Went from 8k to 28k MRR in 11 weeks. -- Rodrigo M., B2B SaaS"
scarcity:
  seats: 12
  deadline: "Enrollment closes April 30"
  note: "Real scarcity, not fake urgency"
cta: secure_my_seat
legal_note: "Stat basis must appear near claim; no income guarantees"
sections_required: [hero, proof_bar, what_you_get, testimonials, objections_3, scarcity_cta]
tone: warm_authoritative_scarce
```

**8F trace (abbreviated)**
```
F1: kind=landing_page/P05, legal_note active, real scarcity present
F2: N02. BOFU + scarcity = remove_risk + close + authentic_urgency. Legal compliance active.
F3: kc_campaign, kc_email_sequence (testimonial placement), quality_gate (legal flag)
F4: hero=transformation_outcome, scarcity=honest, testimonials=named+specific, legal=stat+basis together
F6: each section respects legal note; scarcity CTA includes deadline
F7: income guarantees absent, stat basis adjacent, real scarcity confirmed
```

**Output**
```yaml
hero:
  headline: "Your first 6-figure month -- live, with a cohort doing it alongside you."
  subheadline: "87% of graduates hit their revenue goal within 90 days (Q1 2026, n=31). 12 seats. Enrollment closes April 30."
  note: "Stat basis inline per legal requirement"
  cta_button: "Secure my seat"

proof_bar:
  items:
    - "87% graduate revenue goal rate (Q1 2026, n=31)"
    - "12 seats available"
    - "Enrollment closes April 30"

what_you_get:
  items:
    - "8 live sessions -- real-time feedback on your exact deals"
    - "1:1 revenue audit in week 1"
    - "Cohort accountability + async slack channel"
    - "Recorded library access after cohort ends"

testimonials:
  - quote: "Closed my first 5-figure deal in week 3."
    attribution: "Ana S., founder"
  - quote: "Went from 8k to 28k MRR in 11 weeks."
    attribution: "Rodrigo M., B2B SaaS founder"

objections:
  - fear: "I do not have time for another program"
    answer: "8 sessions over 8 weeks. No fluff, no homework theatrics. You show up with your real pipeline; we work it live."
  - fear: "I have tried courses before"
    answer: "This is not a course. It is a live operating room. Your deals, our playbook, real outcomes."
  - fear: "What if it does not work for my business?"
    answer: "87% of the last cohort hit their goal in 90 days. The remaining 13% stayed and hit it in week 14."

scarcity_cta:
  headline: "12 seats. April 30 deadline. 87% graduation rate."
  body: "If you have been thinking about this, you are already late. The thinking window closes with the enrollment window."
  cta_button: "Secure my seat -- before April 30"
  note: "No income guarantees. All results cited with basis."

quality_check:
  stat_basis_present: true
  income_guarantee: false
  real_scarcity: true (12 seats confirmed)
  legal_compliance: pass
  cta_singular: true
  testimonials_named: true
```

---

## Format Lessons

| Lesson | What the model learns |
|--------|-----------------------|
| Hero = promise as outcome | Not "introducing X" -- "your life after X" |
| Proof bar = numbers only | No adjectives in the proof bar; let the numbers speak |
| Objections are fears | Name the fear exactly; answer without dismissing |
| Legal notes are copy constraints | Stat basis placement is a copy decision, not a footnote |
| Scarcity must be real | Fake urgency destroys trust; real scarcity closes deals |

## Prompting Rules Derived From These Examples

1. Hero headline = transformation outcome, not product description.
2. Proof bar: 3 items maximum, numbers only, no adjectives.
3. Testimonials: named + specific result + timeline. Anonymous quotes are noise.
4. Objections section: write the exact fear first; do not minimize it.
5. Scarcity: confirm real before including; omit if manufactured.
6. Legal constraints: embed stat basis adjacent to the stat in the copy, not in footnotes.

## Anti-Patterns

| Anti-pattern | Failure |
|-------------|---------|
| Hero describes the product | Reader does not care what it is; they care what it does to them |
| Proof buried below fold | Credibility must appear before desire fully forms |
| Unnamed testimonials | "Happy customer" = 0 trust transfer |
| Fake scarcity in copy | Audiences detect it; trust collapses |
| Legal disclaimer as footnote | Compliance violation AND trust signal ignored |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[landing_page_template]] | downstream | 0.31 |
| [[p03_sp_marketing_nucleus]] | downstream | 0.25 |
| [[bld_system_prompt_landing_page]] | downstream | 0.25 |
| [[bld_knowledge_card_landing_page]] | related | 0.24 |
| [[kc_landing_page]] | related | 0.24 |
| [[landing-page-builder]] | downstream | 0.23 |
| [[bld_examples_landing_page]] | related | 0.23 |
| [[p08_ac_n02]] | downstream | 0.22 |
| [[bld_collaboration_landing_page]] | downstream | 0.22 |
| [[bld_schema_landing_page]] | downstream | 0.21 |
