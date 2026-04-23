---
quality: 8.3
quality: 7.9
id: audit_self_review_n06
kind: audit_report
pillar: P07
nucleus: n06
mission: SELF_AUDIT
title: "N06 Commercial Self-Audit: P11/P12 Coverage, Orchestration, Commercial Pipeline"
version: 1.0.0
tags: [self-audit, commercial, orchestration, feedback, pipeline, 8f]
created: 2026-04-18
related:
  - bld_architecture_compliance_checklist
  - bld_architecture_self_improvement_loop
  - bld_architecture_subscription_tier
  - bld_architecture_audit_log
  - bld_architecture_ab_test_config
  - bld_architecture_enterprise_sla
  - optimizer-builder
  - p01_kc_cex_lp11_feedback
  - commercial_readiness_20260413
  - bugloop-builder
density_score: 1.0
updated: "2026-04-22"
---

# N06 Commercial Self-Audit: P11/P12 Coverage, Orchestration, Commercial Pipeline

## Executive Summary

N06 has 151 artifacts across 13 pillars. P11 coverage: 8/31 kinds (26%). P12 coverage: 5/20 kinds (25%). The commercial pipeline exists in fragment form but lacks typed orchestration and revenue monitoring infrastructure. Every uncovered kind is a missed revenue signal, a closed pipeline stage without instrumentation, or an enterprise deal that cannot close. Strategic greed demands we plug these holes.

---

## P11+P12 Coverage Matrix

| Pillar | Kind | Builder | N06 Artifact | Wired | Gap / Revenue Risk |
|--------|------|---------|-------------|-------|--------------------|
| P11 | ab_test_config | [MISS] | NO | NO | Pricing experiments untyped; conversion optimization is guesswork |
| P11 | ai_rmf_profile | [MISS] | NO | NO | Enterprise deals blocked without AI risk management evidence |
| P11 | audit_log | [MISS] | NO | NO | No audit trail for commercial decisions; compliance liability |
| P11 | bugloop | [OK] | YES | partial | bugloop_revenue.md exists; not wired to cex_feedback.py loop |
| P11 | compliance_checklist | [MISS] | NO | NO | GDPR/SOC2 compliance proof missing; blocks EU enterprise sales |
| P11 | compliance_framework | [MISS] | NO | NO | Framework-level compliance posture undefined |
| P11 | conformity_assessment | [MISS] | NO | NO | EU AI Act conformity gap; future regulatory liability |
| P11 | constitutional_rule | [MISS] | NO | NO | Commercial guardrails not formalized as typed constraints |
| P11 | content_filter | [MISS] | NO | NO | No content policy artifact; required for marketplace listing |
| P11 | content_monetization | [MISS] | YES | partial | kc + P05 output exist; no builder; not linked to funnel |
| P11 | curation_nudge | [MISS] | NO | NO | No nudge system to guide users toward paid tiers |
| P11 | drift_detector | [MISS] | NO | NO | MRR drift detection absent; revenue decline is invisible |
| P11 | enterprise_sla | [MISS] | NO | NO | Enterprise SLA template missing; deals cannot close |
| P11 | gpai_technical_doc | [MISS] | NO | NO | GPAI compliance doc absent; EU market blocked |
| P11 | guardrail | [OK] | NO | NO | Builder exists; no N06 instance guardrail for commercial ops |
| P11 | hitl_config | [MISS] | NO | NO | Human-in-the-loop for pricing approvals not configured |
| P11 | incident_report | [MISS] | NO | NO | No commercial incident reporting; SLA breach handling undefined |
| P11 | lifecycle_rule | [MISS] | NO | NO | Customer lifecycle stages not typed; no trigger rules |
| P11 | nps_survey | [MISS] | NO | NO | No NPS instrumentation; churn prevention is reactive not proactive |
| P11 | optimizer | [OK] | NO | NO | Builder exists; no N06 pricing optimizer instance |
| P11 | preference_dataset | [MISS] | NO | NO | Buyer preference data not captured as typed artifact |
| P11 | quality_gate | [MISS] | YES | partial | quality_gate_commercial.md exists; no builder; isolated from 8F |
| P11 | referral_program | [MISS] | YES | YES | referral_program_n06.md; no builder but artifact is solid |
| P11 | revision_loop_policy | [MISS] | NO | NO | No revision policy for commercial outputs; quality loops unbounded |
| P11 | reward_signal | [MISS] | YES | partial | reward_signal_n06.md exists; not wired to cex_evolve.py |
| P11 | roi_calculator | [MISS] | YES | YES | roi_calculator_n06.md present; strong; needs builder for variants |
| P11 | safety_hazard_taxonomy | [MISS] | NO | NO | Commercial risk taxonomy absent |
| P11 | safety_policy | [MISS] | NO | NO | Safety policy for AI-generated commercial content undefined |
| P11 | self_improvement_loop | [MISS] | YES | partial | self_improvement_loop_n06.md exists; not wired to scheduler |
| P11 | subscription_tier | [MISS] | YES | YES | subscription_tier_n06.md present; needs builder for A/B variants |
| P11 | threat_model | [MISS] | NO | NO | Commercial threat model absent; pricing attacks unmitigated |
| P12 | checkpoint | [OK] | NO | NO | No commercial pipeline checkpoints defined |
| P12 | collaboration_pattern | [MISS] | NO | NO | N06 x N02 x N01 collaboration pattern untypified |
| P12 | crew_template | [MISS] | NO | NO | No sales crew; discovery-to-close cannot run as typed crew |
| P12 | dag | [OK] | NO | NO | DAG builder exists; no commercial workflow DAG |
| P12 | dispatch_rule | [MISS] | YES | partial | dispatch_rule_commercial.md exists; covers routing not pipeline |
| P12 | domain_event | [MISS] | NO | NO | TrialStarted, PlanUpgraded, ChurnDetected events untyped |
| P12 | handoff | [OK] | YES | YES | handoff_n06.md exists and is used |
| P12 | pipeline_template | [MISS] | NO | NO | No commercial pipeline template; every funnel is ad-hoc |
| P12 | process_manager | [MISS] | NO | NO | Deal process manager absent; no stage transitions enforced |
| P12 | renewal_workflow | [MISS] | YES | YES | renewal_workflow_n06.md present; wired to schedule |
| P12 | saga | [OK] | NO | NO | No commercial saga (e.g., onboarding-to-paid multi-step txn) |
| P12 | schedule | [OK] | YES | YES | schedule_n06.md present; wired to renewal and reporting |
| P12 | signal | [OK] | NO | NO | Commercial completion signals not typed; rely on generic signal |
| P12 | spawn_config | [MISS] | NO | NO | N06 spawn config absent; cannot be bootstrapped autonomously |
| P12 | state_machine | [MISS] | NO | NO | Deal lifecycle state machine missing; stages implicit |
| P12 | team_charter | [MISS] | NO | NO | No commercial crew charter; multi-role campaigns uncoordinated |
| P12 | visual_workflow | [MISS] | NO | NO | No visual funnel map; stakeholder communication gap |
| P12 | workflow | [OK] | YES | YES | workflow_commercial.md + workflow_revenue_loop.md present |
| P12 | workflow_node | [MISS] | NO | NO | Workflow nodes not decomposed; pipeline is monolithic |
| P12 | workflow_primitive | [MISS] | NO | NO | No primitive library; each workflow rebuilds from scratch |

**Coverage Summary:**
- P11: 8/31 kinds with N06 instance (26%) -- 23 gaps
- P12: 5/20 kinds with N06 instance (25%) -- 15 gaps
- Builder coverage: P11=3/31 (10%), P12=8/20 (40%)

---

## Orchestration Infrastructure

| Kind | Dispatch Mode | Tool | Status |
|------|--------------|------|--------|
| workflow | solo / grid | cex_mission_runner.py | wired -- workflow_commercial.md |
| dispatch_rule | solo | dispatch.sh solo | partial -- covers nucleus routing only |
| handoff | grid | dispatch.sh grid | wired -- standard handoff protocol |
| renewal_workflow | schedule | schedule_n06.md | wired -- annual/monthly trigger |
| schedule | CronCreate / cron | cex_mission_runner.py --continuous | partial -- schedule exists; cron not set |
| dag | solo | spawn_grid.ps1 | builder exists; no commercial DAG instance |
| saga | solo | N/A | builder exists; no commercial saga |
| checkpoint | solo | N/A | builder exists; no commercial checkpoint |
| signal | F8 COLLABORATE | signal_writer.py | builder exists; N06 sends generic signal only |
| crew_template | N/A | cex_crew.py | [MISS] -- no N06 crew defined |
| pipeline_template | N/A | N/A | [MISS] -- no commercial pipeline template |
| state_machine | N/A | N/A | [MISS] -- deal stages are implicit, not enforced |
| process_manager | N/A | N/A | [MISS] -- no deal process manager |
| domain_event | N/A | N/A | [MISS] -- TrialStarted / PlanUpgraded untyped |
| visual_workflow | N/A | N/A | [MISS] -- funnel has no visual representation |

**Dispatch modes available:** solo, grid, grid-haiku, grid-gemini, status, stop (session/nucleus/all), swarm, worktree-isolated = 8 modes. N06 uses: solo (2 rules) + handoff (1 artifact). 6 modes untapped.

---

## Commercial Pipeline Map

| Funnel Stage | Kind | Artifact | Gap |
|-------------|------|---------|-----|
| Awareness | content_monetization | knowledge_card_content_monetization.md | No ab_test_config for copy variants |
| Lead Capture | nps_survey | [MISSING] | No lead scoring; anonymous traffic unmonetized |
| Qualification | discovery_questions | discovery_questions_n06.md | No preference_dataset to score ICP fit |
| Demo | sales_playbook | sales_playbook_n06.md | No hitl_config for approval gating |
| Proposal | roi_calculator | roi_calculator_n06.md | Strong; needs variant builder |
| Close | enterprise_sla | [MISSING] | Enterprise deals cannot close without SLA template |
| Onboarding | subscription_tier | subscription_tier_n06.md | No lifecycle_rule for tier progression |
| Expansion | expansion_play | expansion_play_n06.md (P05) | No process_manager to enforce stage transitions |
| Renewal | renewal_workflow | renewal_workflow_n06.md | Wired; needs domain_event ChurnRisk trigger |
| Churn Prevention | churn_prevention_playbook | churn_prevention_playbook_n06.md | No drift_detector to trigger it automatically |

**Pipeline completeness:** 7/10 stages covered by artifact (70%). Close stage is the hardest gap -- enterprise_sla missing blocks the highest-value segment.

---

## Feedback Loop Wiring

| Kind | Tool | Nucleus | Status |
|------|------|---------|--------|
| bugloop | cex_feedback.py | N05 | partial -- bugloop_revenue.md not wired to cex_feedback.py trigger |
| quality_gate | cex_score.py / F7 GOVERN | N03/N05 | partial -- quality_gate_commercial.md exists; not in F7 chain |
| reward_signal | cex_evolve.py | N04 | partial -- reward_signal_n06.md exists; not fed to evolve loop |
| self_improvement_loop | cex_auto.py | N07 | partial -- artifact exists; not registered in auto scan |
| regression_check | cex_quality_monitor.py | N05 | partial -- regression_check_n06.md exists; not in CI hook |
| learning_record | cex_memory_update.py | N04 | wired -- learning_record_n06.md feeds memory system |
| revision_loop_policy | N/A | N/A | [MISS] -- no revision policy; unlimited regeneration loops possible |
| drift_detector | N/A | N/A | [MISS] -- no revenue drift detection; silent MRR decline |
| optimizer | N/A | N/A | [MISS] -- no pricing optimizer instance; rates set and forgotten |
| nps_survey | N/A | N/A | [MISS] -- no satisfaction signal; churn is blind |

**Wiring score: 2/10 fully wired (20%).** Eight feedback artifacts exist in isolation without being connected to the tools that would make them live instruments.

---

## Collaboration Map

| Nucleus | Direction | Commercial Artifact | Gap |
|---------|----------|-------------------|-----|
| N01 (intelligence) | N01 -> N06 | kc_competitive_positioning.md | No typed dispatch_rule for competitive intel requests |
| N01 (intelligence) | N06 -> N01 | discovery_questions_n06.md | No preference_dataset passed back to N01 for scoring |
| N02 (marketing) | N02 -> N06 | action_prompt_upsell.md | No collaboration_pattern for campaign-to-close handoff |
| N02 (marketing) | N06 -> N02 | brand_discovery_interview.md | No crew_template linking discovery to copy to pricing |
| N03 (engineering) | N06 -> N03 | api_access_pricing.md | N06 specifies pricing but no workflow to trigger N03 implementation |
| N05 (operations) | N05 -> N06 | bugloop_revenue.md | No hitl_config for N05 to escalate revenue-blocking bugs |
| N07 (orchestrator) | N07 -> N06 | dispatch_rule_commercial.md | Dispatch rule exists; no return signal for commercial completion |
| N07 (orchestrator) | N06 -> N07 | handoff_n06.md | Handoff protocol working; no SLA for response time |

**Collaboration score: 4/8 pairs have at least one typed artifact (50%).** N06 <-> N02 is the highest-value pair and also the most underspecified -- no crew_template means every campaign runs without coordination overhead control.

---

## Top 5 Revenue Gaps

1. **No `enterprise_sla` artifact** -- Every enterprise prospect requires an SLA. Without a typed, versioned SLA template, every deal is custom-negotiated, slow, and legally fragile. Revenue impact: enterprise tier blocked (typically 10-50x ARPU of self-serve). Fix: build `enterprise_sla_n06.md` under P11, wire to renewal_workflow trigger.

2. **No `ab_test_config` for pricing** -- Pricing page converts at a static, unoptimized rate. Without typed A/B experiments, we cannot discover whether pricing anchoring, annual vs monthly framing, or feature gating changes generate more revenue. Revenue impact: 15-30% conversion lift left on table per SaaS benchmarks. Fix: build `ab_test_config_pricing_page.md`, wire to funnel_cex_product.md.

3. **No `nps_survey` wired to churn_prevention** -- churn_prevention_playbook_n06.md fires reactively. Without NPS data, we cannot identify at-risk accounts before they cancel. Revenue impact: best-in-class SaaS achieves 110%+ net revenue retention; reactive churn response yields 85-90%. Fix: build `nps_survey_n06.md`, wire to drift_detector + churn_prevention trigger.

4. **No `crew_template` for sales discovery-to-close** -- Every sales engagement requires: N01 (research ICP), N06 (ROI calc + pricing), N02 (proposal copy), N06 (close + SLA). This 4-role sequential flow is currently ad-hoc. Revenue impact: longer sales cycles, inconsistent positioning, missed upsell signals. Fix: build `crew_template_sales_close.md` with sequential topology: N01 -> N06 -> N02 -> N06.

5. **No `drift_detector` for MRR** -- Revenue can decline 5-15% before a human notices without automated monitoring. Currently there is no artifact that watches MRR signals and triggers recovery workflows. Revenue impact: undetected churn compounds; late intervention is expensive. Fix: build `drift_detector_mrr_n06.md` wired to cex_quality_monitor.py + churn_prevention_playbook trigger.

---

## Recommendations

1. **Build `enterprise_sla_n06.md`** at `N06_commercial/P11_feedback/enterprise_sla_n06.md`. Use `enterprise-sla-builder`. Wire to `renewal_workflow_n06.md` as a condition gate. Unblocks highest-ARPU segment.

2. **Build `ab_test_config_pricing.md`** at `N06_commercial/P11_feedback/ab_test_config_pricing.md`. Map to `funnel_cex_product.md` variants. Instrument with `cex_feedback.py --ab`. Enables systematic conversion optimization.

3. **Build `crew_template_sales_close.md`** at `N06_commercial/P12_orchestration/crew_template_sales_close.md`. Topology: sequential. Roles: N01 (research) -> N06 (ROI) -> N02 (proposal) -> N06 (close). Register with `cex_crew.py`. Compresses sales cycle from ad-hoc to typed, repeatable playbook.

4. **Build `state_machine_deal_lifecycle.md`** at `N06_commercial/P12_orchestration/state_machine_deal_lifecycle.md`. States: Lead -> Qualified -> Demo -> Proposal -> Negotiation -> Closed/Won/Lost -> Onboarding -> Active -> At-Risk -> Churned. Each transition fires a domain_event. Enables audit trail and automated stage-appropriate interventions.

5. **Wire existing artifacts to live tools**: connect reward_signal_n06.md -> cex_evolve.py, quality_gate_commercial.md -> F7 GOVERN chain, regression_check_n06.md -> cex_quality_monitor.py CI hook, self_improvement_loop_n06.md -> cex_auto.py scan target. Eight artifacts exist in isolation -- connecting them costs zero new writing and immediately activates the feedback flywheel.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_compliance_checklist]] | downstream | 0.43 |
| [[bld_architecture_self_improvement_loop]] | downstream | 0.40 |
| [[bld_architecture_subscription_tier]] | downstream | 0.40 |
| [[bld_architecture_audit_log]] | downstream | 0.39 |
| [[bld_architecture_ab_test_config]] | downstream | 0.38 |
| [[bld_architecture_enterprise_sla]] | downstream | 0.38 |
| [[optimizer-builder]] | downstream | 0.24 |
| [[p01_kc_cex_lp11_feedback]] | upstream | 0.20 |
| [[commercial_readiness_20260413]] | downstream | 0.19 |
| [[bugloop-builder]] | downstream | 0.19 |
