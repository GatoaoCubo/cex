---
kind: quality_gate
id: p11_qg_mental_model
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of mental_model artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Mental Model"
version: "1.0.0"
author: builder_agent
tags: [quality-gate, mental-model, routing, P02, cognitive-map]
tldr: "Quality gate for mental_model artifacts: enforces routing rules, decision tree, domain map, and design-time-only scope."
domain: mental_model
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - p03_ins_mental_model
  - bld_collaboration_mental_model
  - mental-model-builder
  - bld_knowledge_card_mental_model
  - p11_qg_runtime_state
  - p03_sp_mental_model_builder
  - p11_qg_model_provider
  - p11_qg_model_card
  - bld_memory_mental_model
  - bld_schema_mental_model
---

## Quality Gate

# Gate: Mental Model

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Definition
A `mental_model` is a design-time cognitive map that tells an agent how to route, prioritize, and decide. It carries no runtime state and executes no logic. Gates here enforce that routing rules have confidence thresholds, decisions have if/then/else structure, and the artifact never encodes live session data — which belongs in runtime state artifacts.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_mm_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"mental_model"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `agent`, `domain`, `routing_rules`, `decision_tree`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `Routing Rules` section present in body | Model has no routing — central purpose missing |
| H08 | `Decision Tree` or `Priorities` section present in body | No decision structure — model cannot guide choices |
| H09 | `Domain Map` section present in body | Domain boundaries undefined — routing leaks |
| H10 | `routing_rules` list has >= 3 entries, each with `keywords` and `action` | Routing table too sparse to be useful |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names the agent and its primary routing concern |
| S02 | Routing rules have confidence thresholds | 1.0 | Each rule specifies a match confidence or keyword specificity level |
| S03 | Decisions have if/then/else structure | 1.0 | Decision tree entries follow: condition → then action → else action |
| S04 | Priorities ordered with rationale | 1.0 | `priorities` list is ranked and each rank has a one-line justification |
| S05 | Heuristics testsble | 0.5 | Each heuristic can be verified with a specific input example |
| S06 | Domain boundaries explicit | 1.0 | Domain Map states what the agent covers AND what it routes away |
| S07 | Personality traits defined | 0.5 | `personality` object with `tone`, `verbosity`, `risk_tolerance` |
| S08 | `tags` includes `"mental-model"` | 0.5 | Minimum tag for routing |
| S09 | Conflict resolution rules present | 1.0 | Documents what happens when two routing rules match simultaneously |
| S10 | No runtime state encoded | 1.0 | No session counters, active task lists, or live flags in body |
| S11 | Fallback action defined | 0.5 | `fallback` specifies action and escalation target when no rule matches |
| S12 | Density >= 0.80 | 0.5 | No filler: "this model helps", "generally speaking", "in most cases" |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|
| condition | New agent bootstrapping — routing rules are provisional and under observation from live sessions |

## Examples

# Examples: mental-model-builder

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Golden Example
INPUT: "Create mental model for a content-reviewer agent"
OUTPUT:
```yaml
id: p02_mm_content_reviewer
kind: mental_model
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
agent: "content-reviewer"
routing_rules:
  - keywords: [review, audit, check, validate]
    action: "execute quality review pipeline"
    confidence: 0.9
  - keywords: [grammar, spelling, typo, language]
    action: "run language quality checks"
    confidence: 0.85
  - keywords: [compliance, legal, policy, brand]
    action: "apply compliance ruleset"
    confidence: 0.8
  - keywords: [improve, rewrite, enhance, optimize]
    action: "route to content-writer agent"
    confidence: 0.7
decision_tree:
  - condition: "content has compliance flags"
    then: "prioritize compliance review before style"
    else: "start with language quality"
  - condition: "quality score < 7.0"
    then: "reject with specific gate failures"
    else: "approve with score annotation"
  - condition: "content exceeds 5000 words"
    then: "split into sections and review each"
priorities:
  - "compliance (legal/brand violations block publish)"
  - "factual accuracy (wrong data is worse than bad grammar)"
  - "density (no filler, >= 0.80)"
  - "language quality (grammar, clarity, tone)"
  - "formatting (tables, headers, structure)"
heuristics:
  - "when unsure about compliance, flag for human review rather than approve"
  - "when density < 0.70, reject immediately — no amount of editing fixes filler"
  - "when content mixes domains, review each domain section against its own rubric"
domain_map:
  covers: [content_quality, compliance, language, density]
  routes_to:
    content_creation: "content-writer"
    research: "research-agent"
    translation: "translator-agent"
tools_available: [brain_query, grep, read, glob]
personality:
  tone: "direct"
  verbosity: "concise"
  risk_tolerance: "low"
constraints:
  - "never approve content with compliance violations"
  - "never self-score quality (annotate, do not judge)"
  - "never rewrite content — flag issues, let writer fix"
fallback:
  action: "log unroutable request and return to sender"
  escalate_to: "orchestrator"
domain: "content_review"
llm_function: BECOME
quality: null
tags: [mental-model, content-review, quality, routing, P02]
tldr: "Design-time cognitive map for content-reviewer: 4 routing rules, 3-branch decision tree, compliance-first priority"
density_score: 0.91
```
## Agent Reference
content-reviewer: reviews content for compliance, accuracy, density, and language quality.
## Routing Rules
| Keywords | Action | Confidence |
|----------|--------|------------|
| review, audit, check, validate | execute quality review pipeline | 0.9 |
| grammar, spelling, typo, language | run language quality checks | 0.85 |
| compliance, legal, policy, brand | apply compliance ruleset | 0.8 |
| improve, rewrite, enhance, optimize | route to content-writer agent | 0.7 |
## Decision Tree
1. IF content has compliance flags THEN prioritize compliance ELSE start with language
2. IF quality score < 7.0 THEN reject with failures ELSE approve with annotation
3. IF content > 5000 words THEN split and review each section
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_mm_ pattern (H02 pass) | kind: mental_model (H04 pass)
- pillar: P02 (H07 pass) | 23 fields (H06 pass) | 4 routing rules (H08 pass)
- 3 decision conditions (H09 pass) | priorities: 5 items (S03 pass)
- heuristics: 3 items (S04 pass) | domain_map with covers+routes_to (S05 pass)
- personality complete (S06 pass) | tools: 4 items (S07 pass) | constraints: 3 (S08 pass)
- fallback with action+escalate_to (S09 pass) | density: 0.91 (S10 pass)
- keywords are specific nouns/verbs (S12 pass) | no filler (S11 pass)
## Anti-Example
INPUT: "Make a mental model for my agent"

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
