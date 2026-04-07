---
id: p12_wf_gato_strategic_outreach
kind: workflow
pillar: P12
version: 2.0.0
mission_name: gato_strategic_outreach
goal: "Convert 471 ABC Paulista pet business prospects into GATO³ brand partners via multi-channel outreach"
execution_mode: mixed
steps_count: 8
timeout_ms: 7200000
error_recovery: retry_then_skip
quality: 9.0
tags: [workflow, outreach, lead-nurturing, gato, b2b, abc-paulista]
tldr: "4-wave outreach campaign — content → automation → execution → optimization — targeting vets, pet shops, groomers, and 24h hospitals across ABC Paulista with GATO³ sofisticado-acolhedor voice."
density_score: 1.0
persona: Ro
voice: sofisticado-acolhedor
language: pt-BR
---

# GATO³ Strategic Outreach Campaign

## Campaign Context

**Market**: 471 pet business prospects in ABC Paulista (Santo André, São Bernardo, São Caetano)
**Persona**: Ro — guia acolhedora, educadora de tutores, voz sofisticado-acolhedora
**Segments**: Veterinários (118), Pet Shops (203), Groomers (89), Hospitais 24h (61)
**Value Prop**: Educação que acalma, soluções que funcionam, casa que continua elegante.

## Quality Gates Between Waves

```yaml
wave_gates:
  gate_1_to_2:
    condition: "All 3 content assets score ≥ 8.5 via cex_score.py"
    validation: "Brand voice audit passes brand_validate.py"
    fallback: "Re-run failing step with Ro persona reinforcement"
  gate_2_to_3:
    condition: "Nurturing sequence has 5 touches + educational hooks"
    validation: "Email preview renders correctly on mobile (375px)"
    fallback: "Simplify sequence to 3 essential touches"
  gate_3_to_4:
    condition: "≥50% of prospects contacted in Wave 3"
    validation: "Response rate ≥ 5% (minimum viable signal)"
    fallback: "Pivot messaging angle before optimization wave"
```

## Steps

### Wave 1: Content (Parallel)

**Step 1: Copy Suite**
- Agent: n02_marketing
- Action: Create segment-specific outreach templates (4 segments: vets, pet shops, groomers, 24h hospitals)
- Input: handoff segments + GATO³ brand voice (brand_config.yaml)
- Output: outreach_copy_gato.md
- Signal: copy_complete
- Depends_on: []
- Timeout_ms: 900000
- On_failure: retry(2) → escalate_n07
- Success_metric: "4 segment templates, each with subject + 3-paragraph body + CTA"
- Voice_rule: "Ro introduces herself as parceira educacional, never sales rep"

**Step 2: Social Strategy**
- Agent: n02_marketing
- Action: Develop relationship building tactics for Instagram/Facebook/LinkedIn
- Input: segment profiles + GATO³ social handles
- Output: social_strategy_gato.md
- Signal: social_complete
- Depends_on: []
- Timeout_ms: 900000
- On_failure: retry(2) → escalate_n07
- Success_metric: "Per-platform playbook: 3 content pillars, posting cadence, engagement script"
- Voice_rule: "Instagram = warmth 5/5, LinkedIn = authority 4/5, Facebook = community 4/5"

**Step 3: Conversion Assets**
- Agent: n02_marketing
- Action: Build case studies, ROI calculator, partnership guide
- Input: GATO³ business impact framework + margin data from N06
- Output: conversion_assets_gato.md
- Signal: assets_complete
- Depends_on: []
- Timeout_ms: 1200000
- On_failure: retry(2) → escalate_n07
- Success_metric: "1 case study template, 1 ROI calculator spec, 1 partnership one-pager"
- Voice_rule: "Data-backed but warmth-first — numbers serve the story, not the other way"

### Wave 2: Automation

**Step 4: Nurturing Sequence**
- Agent: n02_marketing
- Action: Design 5-touch email automation with educational content
- Input: copy suite (Step 1) + conversion assets (Step 3)
- Output: nurturing_automation_gato.md
- Signal: automation_complete
- Depends_on: [copy_complete, assets_complete]
- Timeout_ms: 1200000
- On_failure: retry(2) → degrade_to_3_touch
- Success_metric: "5 emails, each ≤200 words, educational hook + soft CTA, 3-day cadence"
- Voice_rule: "Each email = Ro sharing one practical protocol. Never sell before email 4."
- Sequence_arc:
    - "E1: Bem-vinda — quem é a Ro, por que educação felina importa"
    - "E2: Protocolo prático — um problema real que Ro resolve"
    - "E3: Caso de sucesso — parceiro que já implementou"
    - "E4: Proposta de valor — como a parceria funciona"
    - "E5: Convite — próximo passo concreto"

### Wave 3: Execution (Sequential by priority)

**Step 5: Veterinary Outreach**
- Agent: n02_marketing
- Action: Deploy professional partnership messaging to clinics (highest priority)
- Input: copy suite + clinic prospect list (118 vets)
- Output: vet_campaign_gato.md
- Signal: vet_complete
- Depends_on: [copy_complete, social_complete]
- Timeout_ms: 1800000
- On_failure: retry(1) → skip_to_step_6
- Success_metric: "118 personalized outreach messages deployed, tracking pixels active"
- Voice_rule: "Authority 4/5 + Warmth 4/5 — peer-to-peer professional tone"
- Segment_insight: "Vets value science-backed claims. Lead with research, close with relationship."

**Step 6: Pet Shops + Specialized**
- Agent: n02_marketing
- Action: Deploy volume messaging to pet shops, groomers, hospitals
- Input: copy suite + remaining prospect lists (353 prospects)
- Output: volume_campaign_gato.md
- Signal: volume_complete
- Depends_on: [copy_complete]
- Timeout_ms: 1800000
- On_failure: retry(1) → partial_deploy
- Success_metric: "353 messages deployed across 3 sub-segments with tracking"
- Voice_rule: "Warmth 5/5 — these are community businesses. Ro is a neighbor, not a vendor."
- Segment_insight: "Pet shops respond to margin + education story. Groomers want Instagram content."

### Wave 4: Optimization

**Step 7: Nurturing Activation**
- Agent: n02_marketing
- Action: Activate automated sequences for engaged prospects
- Input: automation (Step 4) + engagement data from Waves 2-3
- Output: nurturing_activation_gato.md
- Signal: nurturing_active
- Depends_on: [automation_complete, vet_complete, volume_complete]
- Timeout_ms: 900000
- On_failure: retry(1) → manual_activation
- Success_metric: "All engaged prospects (open ≥1 email OR clicked ≥1 link) enrolled in sequence"
- Voice_rule: "Personalize E1 greeting based on segment. Vets get 'Dra./Dr.', shops get first name."

**Step 8: Conversion & Optimization**
- Agent: n02_marketing
- Action: Deploy partnership proposals + A/B test optimization
- Input: conversion assets + qualified leads (response ≥ 1 interaction)
- Output: conversion_campaign_gato.md
- Signal: campaign_complete
- Depends_on: [nurturing_active]
- Timeout_ms: 1800000
- On_failure: retry(1) → report_partial_results
- Success_metric: "Partnership proposals sent to ≥30% of engaged leads, A/B on subject line + CTA"
- Voice_rule: "Decision stage — confident but never pushy. Ro presents, never pressures."
- AB_tests:
    - "Subject: 'Parceria educacional GATO³' vs 'Ro quer te conhecer'"
    - "CTA: 'Agendar conversa' vs 'Ver proposta completa'"

## Waves

```yaml
waves:
  - id: 1
    name: "Content Foundation"
    steps: [1, 2, 3]
    mode: parallel
    gate: gate_1_to_2
  - id: 2
    name: "Automation Build"
    steps: [4]
    mode: sequential
    gate: gate_2_to_3
  - id: 3
    name: "Market Execution"
    steps: [5, 6]
    mode: sequential_by_priority
    gate: gate_3_to_4
  - id: 4
    name: "Optimize & Convert"
    steps: [7, 8]
    mode: sequential
    gate: final_report
```

## Success Targets

| Metric | Target | Minimum Viable | Measurement Window |
|--------|--------|----------------|-------------------|
| Open Rate | 35%+ | 20% | 7 days post-send |
| Response Rate | 15%+ | 8% | 14 days post-send |
| Meeting Booked | 8%+ | 3% | 30 days post-campaign |
| Partnership Signed | 25%+ of meetings | 15% | 60 days post-campaign |
| NPS (Partners) | 8+ | 7 | 90 days post-onboard |

## Rollback Strategy

```yaml
rollback:
  wave_1_failure: "Re-brief with simplified 2-segment approach (vets + shops only)"
  wave_2_failure: "Manual email sends replace automation (slower but functional)"
  wave_3_failure: "Reduce to top-50 highest-value prospects, personalize deeply"
  wave_4_failure: "Direct phone outreach to warm leads, skip A/B testing"
  full_abort: "Pause campaign, run N01 research sprint on messaging mismatch"
```