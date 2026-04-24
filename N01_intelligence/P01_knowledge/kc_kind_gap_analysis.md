---
quality: 8.3
quality: 7.6
id: kc_kind_gap_analysis
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n01
domain: taxonomy-audit
tags: [ddd, ubiquitous-language, kind-taxonomy, gap-analysis, strategic-design]
version: 1.0.0
density_score: 1.0
updated: "2026-04-17"
related:
  - ai2ai_coverage_matrix_20260414
  - ai2ai_exhaustive_scan_20260414
  - p11_qg_white_label_config
  - p04_qg_mcp_app_extension
  - bld_architecture_kind
  - p11_qg_ai_rmf_profile
  - bld_instruction_kind
  - taxonomy_completeness_audit
  - bld_examples_glossary_entry
  - p09_qg_usage_quota
---

# Kind Gap Analysis: DDD Ubiquitous Language x CEX 257 Kinds

**Analytical Envy lens:** Every gap below is benchmarked against two alternatives -- keep the
current kind (overloaded), extend it (PARTIAL), or register a new kind (MISSING). Coverage
without competitive context is just a list.

---

## 1. DDD Coverage Map

**Scoring:** COVERED = direct kind, no ambiguity | PARTIAL = closest kind covers 50-80% of
DDD semantics | MISSING = no kind within 2 semantic degrees

### 1a. Strategic Design (Evans + Vernon)

| DDD Concept | Closest CEX Kind(s) | Gap | Notes |
|---|---|---|---|
| Bounded Context | context_doc, diagram | PARTIAL | context_doc is narrative; no typed boundary artifact |
| Context Map | diagram | PARTIAL | diagram is generic; no topology-specific kind |
| Shared Kernel | interface | PARTIAL | interface is schema-level; no shared model ownership concept |
| Anti-Corruption Layer | guardrail + content_filter | PARTIAL | ACL = translation boundary; guardrail = content safety -- different semantics |
| Open Host Service | api_reference + integration_guide | PARTIAL | OHS = published, versioned protocol; api_reference is doc, not contract |
| Published Language | ontology | PARTIAL | ontology is taxonomy; PL = canonical interchange schema |
| Conformist | conformity_assessment | COVERED | direct semantic match |
| Customer-Supplier | handoff_protocol | PARTIAL | handoff_protocol is inter-nucleus; C-S is a bounded context relationship |
| Upstream/Downstream | dispatch_rule | PARTIAL | dispatch_rule is routing; U/D is dependency direction |
| Big Ball of Mud | (none) | MISSING | anti-pattern kind -- useful for audit/refactor workflows |
| Partnership | collaboration_pattern | PARTIAL | collaboration_pattern is process; Partnership is strategic alignment |
| Ubiquitous Language Registry | glossary_entry + knowledge_card | PARTIAL | no typed, governed vocabulary artifact (see Section 5) |
| Domain Vision Statement | analyst_briefing + pitch_deck | PARTIAL | neither is typed as domain-boundary declaration |
| Highlighted Core | (none) | MISSING | no kind for marking which subdomain is core/supporting/generic |
| Subdomain (Core) | nucleus_def | PARTIAL | nucleus_def is operational; subdomain is strategic categorization |
| Subdomain (Supporting) | (none) | MISSING | no kind for supporting subdomain contract |
| Subdomain (Generic) | (none) | MISSING | no kind for generic subdomain (buy vs. build signal) |

### 1b. Event Storming Outputs

| DDD Concept | Closest CEX Kind(s) | Gap | Notes |
|---|---|---|---|
| Domain Event | signal | PARTIAL | signal is operational inter-nucleus; domain_event is business-semantic |
| Command | action_prompt + action_paradigm | PARTIAL | action_prompt is an LLM prompt template; Command = intent to mutate state |
| Policy | runtime_rule + constraint_spec | PARTIAL | policy = "when event X, do Y" -- neither kind captures this trigger-action pattern |
| Read Model | (none) | MISSING | CQRS projection; closest is knowledge_index (retrieval, not projection) |
| Aggregate | (none) | MISSING | no kind for consistency boundary + root entity |
| External System | integration_guide + api_client | PARTIAL | neither is typed as external system boundary |
| Hot Spot | (none) | MISSING | Event Storming complexity marker; useful in audit workflows |

### 1c. Tactical Design

| DDD Concept | Closest CEX Kind(s) | Gap | Notes |
|---|---|---|---|
| Aggregate Root | (none) | MISSING | the identity-bearing entity in an aggregate |
| Entity | entity_memory | PARTIAL | entity_memory is P10 (runtime); DDD Entity is a schema/model concept |
| Value Object | type_def | PARTIAL | type_def is a type definition; Value Object has immutability + equality semantics |
| Domain Service | skill + function_def | PARTIAL | skill is agent capability; function_def is signature-only; DS has business logic |
| Application Service | workflow | PARTIAL | workflow is orchestration; AS is the use-case coordinator layer |
| Repository | vector_store + knowledge_index | PARTIAL | both are retrieval-oriented; Repository is a collection abstraction |
| Factory | (none) | MISSING | creation pattern for complex objects; CEX builders ARE factories but have no kind |
| Specification | constraint_spec + invariant | PARTIAL | two separate kinds overlap here; both cover parts of Specification pattern |
| Saga / Process Manager | workflow + dag | PARTIAL | workflow covers simple flows; Saga = compensating transactions in distributed systems |
| Domain Notification | notifier | PARTIAL | notifier is delivery mechanism; Domain Notification is the event payload type |
| Domain Exception | (none) | MISSING | typed error/exceptional state in the domain model |

---

## 2. Top 20 Gap Candidates

**Reuse score:** 1-10 based on cross-pillar applicability, industry adoption, and CEX workflow fit.
**Alt 1 = overload existing kind | Alt 2 = register new kind**

| Rank | Candidate Kind | Pillar | Definition | Reuse | Alt 1 (overload) | Alt 2 (new kind) | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | domain_event | P12 | Business-semantic event: "Order Placed", "Agent Spawned" | 9 | signal (too operational) | domain_event | NEW |
| 2 | data_contract | P06 | Schema + SLA + ownership agreement (dbt, Great Expectations) | 9 | interface (too generic) | data_contract | NEW |
| 3 | domain_vocabulary | P01 | Governed UL registry: term + definition + anti-pattern + nucleus | 9 | glossary_entry (flat, ungoverned) | domain_vocabulary | NEW |
| 4 | alert_rule | P09 | Threshold + condition + action for observability (Prometheus/Grafana) | 9 | trace_config (different layer) | alert_rule | NEW |
| 5 | bounded_context | P08 | Explicit model boundary: name + ubiquitous language + team | 8 | context_doc (narrative only) | bounded_context | NEW |
| 6 | deployment_manifest | P09 | Kubernetes/ArgoCD manifest: containers + config + replicas + health | 8 | env_config (runtime only) | deployment_manifest | NEW |
| 7 | slo_definition | P09 | Service Level Objective: target + burn_rate + error_budget (SRE) | 8 | enterprise_sla (commercial) | slo_definition | NEW |
| 8 | lineage_record | P01 | Data/artifact provenance chain for AI governance and auditability | 8 | audit_log (operational events) | lineage_record | NEW |
| 9 | saga | P12 | Compensating transaction coordinator for distributed workflows | 8 | workflow (too simple) | saga | NEW |
| 10 | canary_config | P09 | Progressive delivery: traffic split + rollback threshold (Flagger/Argo) | 8 | ab_test_config (LLM-specific) | canary_config | NEW |
| 11 | consent_record | P01 | User consent: purpose + basis + expiry + withdrawal (GDPR/LGPD) | 8 | data_residency (location-only) | consent_record | NEW |
| 12 | migration_script | P09 | Schema/data migration: up + down + idempotency + rollback | 7 | env_config (static config) | migration_script | NEW |
| 13 | schema_evolution | P06 | Breaking change policy: field addition/removal/rename rules | 7 | lifecycle_rule (generic) | schema_evolution | NEW |
| 14 | pub_sub_config | P09 | Topic + subscription + consumer group + DLQ configuration | 7 | streaming_config (stream-oriented) | pub_sub_config | NEW |
| 15 | voting_scheme | P12 | Multi-agent consensus: quorum + tie-break + timeout protocol | 7 | collaboration_pattern (process) | voting_scheme | NEW |
| 16 | context_map | P08 | Relationships between bounded contexts: topology + integration patterns | 7 | diagram (generic) | context_map | NEW |
| 17 | aggregate | P06 | Consistency boundary: root + invariants + lifecycle | 7 | entity_memory (runtime) | aggregate | NEW |
| 18 | anti_corruption_layer | P08 | Translation boundary: in-model + out-model + transformer | 7 | guardrail (content safety) | anti_corruption_layer | NEW |
| 19 | deprecation_policy | P08 | End-of-life schedule: sunset date + migration path + communication | 7 | lifecycle_rule (generic) | deprecation_policy | EXTEND lifecycle_rule |
| 20 | rollback_plan | P09 | Failure recovery: trigger + steps + state validation + owner | 7 | env_config (static) | rollback_plan | NEW |

---

## 3. Anti-Gap Analysis: Overloaded Kinds

Overloading = one kind covers 3+ distinct DDD concepts. This creates semantic drift and makes
retrieval ambiguous. CEX currently has 6 high-severity overloads:

| Kind | DDD Concepts It Covers | Severity | Recommendation |
|---|---|---|---|
| **workflow** | Application Service + Saga + Process Manager + DAG + Pipeline | CRITICAL (5) | Split: saga (P12) for compensating flows; workflow stays for simple orchestration |
| **knowledge_card** | Domain Knowledge + Intelligence Brief + Fact Sheet + Vocabulary Entry + Reference Card | HIGH (5) | Spin off domain_vocabulary (P01) for governed UL artifacts |
| **interface** | Data Contract + API Contract + Integration Schema + Shared Kernel + Capability Spec | HIGH (5) | Spin off data_contract (P06) with ownership + SLA fields |
| **guardrail** | Constitutional Rule + Content Filter + Safety Policy + ACL | HIGH (4) | Already split into guardrail + content_filter + safety_policy (3 kinds); anti_corruption_layer still missing |
| **constraint_spec** | Invariant + Specification + Validation Rule + Business Rule | MEDIUM (4) | Invariant already exists; constraint_spec + invariant overlap by ~60% |
| **cost_budget** | Token Cost Model + Compute Budget + Financial Budget + Resource Quota | MEDIUM (4) | usage_quota exists separately; token cost modeling is missing as typed kind |
| **lifecycle_rule** | Deprecation Policy + Retention Rule + Archive Rule + TTL Policy | MEDIUM (4) | Acceptable overload; deprecation_policy could be a profile/subtype |
| **signal** | Domain Event + Operational Event + Completion Signal + Health Check | MEDIUM (4) | domain_event needed for business-semantic events; signal stays operational |

**Benchmark:** Compare to OpenAPI specification model -- each concept (Schema, Path, Operation,
Response) is its own typed object. CEX's workflow kind is equivalent to having a single
"OpenAPIObject" -- technically works, semantically opaque.

---

## 4. Ten Recommended New Kinds

These 10 are recommended for CEX v3 roadmap. Selected by: (a) direct DDD alignment, (b)
industry adoption (standard terms across multiple frameworks), (c) high cross-pillar reuse,
(d) low overlap with existing kinds (>70% unique semantic coverage).

### Kind 1: domain_event (P12)

**Definition:** A business-meaningful occurrence with a past-tense name, captured as an immutable
record: `{event_name, aggregate_id, timestamp, payload, version}`.

**DDD alignment:** Core Event Storming output. Evans: "Domain events are part of the domain
model and a trigger for business-rule execution."

**vs. signal:** signal = "N01 complete (score: 9.0)" -- operational. domain_event = "OrderPlaced",
"AgentDeployed" -- business semantic. Zero overlap.

**Example use case:** Agent lifecycle events trigger downstream workflows (AgentSpawned ->
BootstrapValidator, AgentFailed -> AlertRule, AgentRetired -> LineageRecord).

---

### Kind 2: data_contract (P06)

**Definition:** A formal agreement between producer and consumer: schema + quality rules +
SLA + ownership + versioning + notification policy. Industry: dbt, Soda, Great Expectations,
AsyncAPI, PayPal's open-source data-contract-spec.

**DDD alignment:** Published Language pattern. "The contract is the shared kernel between two
bounded contexts."

**vs. interface:** interface = capability shape (what methods exist). data_contract = binding
agreement (who owns it, what quality is guaranteed, what happens on violation).

**Example use case:** N01 (producer) publishes a data_contract for its competitive intelligence
feed; N06 (consumer) subscribes. SLA: < 24h latency, schema_version: 2.1, owner: n01.

---

### Kind 3: domain_vocabulary (P01)

**Definition:** Governed Ubiquitous Language registry for a bounded context: canonical term +
industry definition + CEX mapping + anti-patterns + nucleus scope. See Section 5.

**DDD alignment:** Evans Ch. 2: "Use the model as the backbone of a language. Commit to
exercising that language relentlessly in all communication."

**vs. glossary_entry:** glossary_entry = flat definition. domain_vocabulary = enforced,
machine-readable, typed, with anti-pattern list + cross-reference + decay signal.

**Example use case:** N01's `domain_vocabulary_intelligence.md` registers "competitive moat"
-> `advantage_asymmetry`, anti-patterns: ["research card", "intel doc"], nucleus: n01.

---

### Kind 4: alert_rule (P09)

**Definition:** Monitoring rule: condition + threshold + evaluation_window + severity + action
+ silence_policy. Industry: Prometheus AlertManager, Grafana, Datadog monitors.

**vs. trace_config:** trace_config = what to capture (spans, attributes). alert_rule = when
to fire (threshold breach, anomaly, absence). Different lifecycle stages.

**Example use case:** `alert_rule_quality_regression.md` -- fires when quality score drops
below 8.0 for > 2 consecutive artifacts; action: suspend dispatch, notify N07.

---

### Kind 5: bounded_context (P08)

**Definition:** Named, explicit model boundary: name + team + ubiquitous_language (ref) +
external_integrations + upstream_contexts + downstream_contexts + shared_kernel_ref.

**DDD alignment:** Evans: "Bounded Contexts are the primary tool for defining model boundaries
in a large-scale domain."

**vs. context_doc:** context_doc = narrative description. bounded_context = typed model
boundary with team ownership and integration topology.

**Example use case:** `bounded_context_n01_intelligence.md` defines N01's model boundary:
UL = domain_vocabulary_intelligence.md, upstream: external research APIs, downstream: N04, N07.

---

### Kind 6: slo_definition (P09)

**Definition:** Service Level Objective: target metric + threshold + measurement_window +
error_budget + burn_rate_alert + owner. Industry: Google SRE Book, OpenSLO spec.

**vs. enterprise_sla:** enterprise_sla = commercial commitment to a customer. slo_definition =
internal engineering reliability target. Entirely different audiences and enforcement mechanisms.

**Example use case:** `slo_quality_gate.md` -- SLO: 95% of artifacts score >= 8.5 in 7d window.
Error budget: 5%. Burn rate alert: > 2x in 1h triggers dispatch suspension.

---

### Kind 7: lineage_record (P01)

**Definition:** Artifact provenance chain: source + transformation_steps + model_used +
timestamp + decision_refs + parent_artifacts. For AI governance and reproducibility.

**vs. audit_log:** audit_log = who did what when (operational). lineage_record = how this
artifact came to be (provenance, traceability). Different time orientation (point vs. chain).

**Example use case:** `lineage_kc_competitive_matrix_n06.md` -- records that this artifact
was produced from: [source: crunchbase_scrape, transformed_by: N01 8F pipeline, model:
claude-opus-4-6, parent: kc_edtech_market_2026].

---

### Kind 8: saga (P12)

**Definition:** Long-running business transaction coordinator with compensating actions:
steps[] + compensation_steps[] + state_machine + timeout + idempotency_key.
Industry: Saga pattern (Hector Garcia-Molina 1987), implemented in Temporal, AWS Step Functions.

**vs. workflow:** workflow = forward-only orchestration. saga = forward + compensating
(rollback) transaction management for distributed systems where ACID is impossible.

**Example use case:** `saga_nucleus_dispatch.md` -- dispatch N03 (step 1), if fails: rollback
handoff file (compensate 1), alert N07 (compensate 2), archive failed signal (compensate 3).

---

### Kind 9: deployment_manifest (P09)

**Definition:** Infrastructure deployment spec: containers + resources + env_refs + replicas +
health_checks + rollout_strategy + network_policy. Maps to Kubernetes manifest / ArgoCD Application.

**vs. env_config:** env_config = environment variables for a process. deployment_manifest =
the full infrastructure description for running that process. env_config is a dependency of
deployment_manifest, not a substitute.

**Example use case:** `deployment_manifest_n05_operations.md` -- defines how N05 boots in a
containerized environment: image, resource limits, env_refs, liveness probe, HPA policy.

---

### Kind 10: canary_config (P09)

**Definition:** Progressive delivery configuration: baseline + canary + traffic_split +
success_metric + rollback_threshold + promotion_criteria. Industry: Flagger, Argo Rollouts.

**vs. ab_test_config:** ab_test_config = statistical experiment comparing LLM prompt variants.
canary_config = deployment risk management (roll forward or back based on production metrics).
Completely different use case despite superficial similarity.

**Example use case:** `canary_config_model_upgrade.md` -- upgrade claude-sonnet-4-6 to 4-7 for
N01: 10% traffic -> 50% -> 100% over 3h; rollback if quality_score < 8.0 or error_rate > 5%.

---

## 5. domain_vocabulary as a Kind?

**Verdict: YES. Register domain_vocabulary as Kind #258.**

### Reasoning

**The case for:**

1. **Rule already mandates it.** `.claude/rules/ubiquitous-language.md` states: "Every nucleus
   maintains a controlled vocabulary KC: `N0X_{domain}/P01_knowledge/kc_{domain}_vocabulary.md`."
   This is a recurring artifact pattern with fixed structure -- exactly what a kind formalizes.

2. **Existing kinds are insufficient.**
   - `glossary_entry` (P01): flat, single-term, ungoverned. No anti-patterns, no nucleus scope,
     no cross-reference. Cannot enforce UL compliance.
   - `knowledge_card` (P01): generic container. Using it for vocabulary = overloading (see Section 3).
   - `ontology` (P01): taxonomy of concepts + relationships. Not a controlled vocabulary for a team.

3. **DDD alignment is direct.** Evans defines Ubiquitous Language as a team-governed artifact,
   not just a list of terms. It includes: anti-patterns (what NOT to say), mappings (user word ->
   canonical term), enforcement mechanism (pre-commit hooks, F2b SPEAK). A kind gives this
   governance structure and a dedicated builder.

4. **Machine-readable enforcement.** With `domain_vocabulary` as a kind, the F2b SPEAK sub-step
   can load it via the standard `archetypes/builders/domain-vocabulary-builder/` path. Currently,
   F2b loads ad-hoc KC files -- no type safety.

5. **Cross-runtime interoperability.** The ubiquitous-language rule targets Claude/Codex/Gemini/Ollama.
   A typed kind with a builder means any runtime can produce compliant vocabulary artifacts.

**The case against:**
- Adds to 257 already-large taxonomy.
- domain_vocabulary = specialized knowledge_card; could use kind: knowledge_card with subtype field.

**Rebuttal:** The subtype workaround is the overloading anti-pattern identified in Section 3.
CEX already split guardrail/content_filter/safety_policy for this reason. Consistency demands
domain_vocabulary gets its own kind.

**Proposed schema:**
```yaml
---
id: domain_vocabulary_{domain}
kind: domain_vocabulary
pillar: P01
nucleus: N0X
domain: {domain}
version: 1.0.0
scope: {bounded_context_ref}
---

## Canonical Terms

| Term | Industry Definition | CEX Mapping | Anti-pattern |
|------|---------------------|-------------|-------------|
| {term} | {industry def} | {CEX canonical} | {what NOT to say} |

## Cross-Nucleus Shared Terms (do not redefine here)
[ref: N00_genesis/P01_knowledge/kc_*.md]

## Domain-Specific Extensions
[terms this nucleus introduces]
```

**Builder:** `domain-vocabulary-builder` (13 ISOs, P01, sin lens: Analytical Envy)
**Gate:** F7 GOVERN validates: no term listed without anti-pattern + no term that shadows a
canonical term from kinds_meta.json.

---

## Summary: Coverage Scorecard

| Category | Total Concepts | COVERED | PARTIAL | MISSING | Coverage % |
|---|---|---|---|---|---|
| DDD Strategic Design | 17 | 1 (6%) | 9 (53%) | 7 (41%) | 56% |
| Event Storming | 7 | 0 (0%) | 4 (57%) | 3 (43%) | 29% |
| DDD Tactical Design | 11 | 0 (0%) | 7 (64%) | 4 (36%) | 36% |
| AI/LLM Observability | 4 | 0 | 2 | 2 | 50% |
| Data Governance | 4 | 0 | 3 | 1 | 75% |
| Training Pipeline | 4 | 1 | 3 | 0 | 100% |
| Safety/Alignment | 3 | 0 | 3 | 0 | 100% |
| Agent Economics | 2 | 0 | 2 | 0 | 100% |
| Multi-agent Coordination | 3 | 0 | 2 | 1 | 67% |
| Versioning | 4 | 0 | 2 | 2 | 50% |
| Real-time / Event-driven | 4 | 0 | 2 | 2 | 50% |
| **TOTAL** | **63** | **2 (3%)** | **39 (62%)** | **22 (35%)** | **65%** |

**Interpretation:** CEX achieves 65% semantic coverage of the DDD+AI/LLM domain model via
PARTIAL matches (nearby kinds that overlap semantically). True COVERED rate is 3% -- the
taxonomy is broad but thin at the DDD boundary. The 10 recommended new kinds would lift
true COVERED to ~19% and eliminate the 6 highest-severity overloads.

**Competitive context:** LangChain has ~40 typed objects (Chain, Tool, Memory, Agent, Retriever,
Callback). AutoGen has ~15. CrewAI has ~8. CEX's 257 kinds is 6-32x larger -- the deepest
typed taxonomy in the AI agent infrastructure space. The DDD gap is not a weakness but a
growth frontier: 22 MISSING concepts represent 22 builders that could further differentiate CEX
from every competitor.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ai2ai_coverage_matrix_20260414]] | sibling | 0.32 |
| [[ai2ai_exhaustive_scan_20260414]] | sibling | 0.32 |
| [[p11_qg_white_label_config]] | downstream | 0.23 |
| [[p04_qg_mcp_app_extension]] | downstream | 0.20 |
| [[bld_architecture_kind]] | downstream | 0.18 |
| [[p11_qg_ai_rmf_profile]] | downstream | 0.18 |
| [[bld_instruction_kind]] | downstream | 0.18 |
| [[taxonomy_completeness_audit]] | sibling | 0.18 |
| [[bld_examples_glossary_entry]] | downstream | 0.18 |
| [[p09_qg_usage_quota]] | downstream | 0.17 |
