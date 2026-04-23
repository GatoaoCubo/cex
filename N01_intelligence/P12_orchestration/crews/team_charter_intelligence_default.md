---
id: team_charter_intelligence_default.md
kind: team_charter
pillar: P12
llm_function: GOVERN
charter_id: intelligence_default
crew_template_ref: p12_ct_competitive_intelligence.md
mission_statement: "Produce a validated competitive intelligence brief for a target domain, grounded on >=3 competitors, with quality >= 9.0 and full source trail."
quality_gate: 9.0
deadline: "2026-04-30T23:59:00-03:00"
deliverables:
  - "Raw data KC (knowledge_card P01) -- analyst output with >=3 competitors and source URLs"
  - "Intelligence brief KC (knowledge_card P01) -- synthesizer output with competitor matrix and >=2 patterns"
  - "Validated brief (knowledge_card P01) -- validator-attested with quality >= 9.0 and verdict: approved"
budget:
  tokens: 90000
  wall_clock_seconds: 2100
  usd: 3.00
domain_focus: "{{TARGET_DOMAIN}}"
competitor_scope: ">=3 named competitors with public market presence"
stakeholders: ["n01_intelligence", "n07_orchestrator"]
escalation_protocol: "If any role crosses budget ceiling or fails 2 consecutive revision cycles, emit signal_{role}_escalate.json to .cex/runtime/signals/. N01 reads and either extends budget or kills the crew."
termination_criteria: "ANY of: (1) validator emits verdict: approved; (2) token or wall-clock budget exhausted; (3) deadline passed; (4) 2 consecutive validator rejections on the same artifact (stuck loop)."
quality: null
density_score: 0.92
title: "Team Charter -- Intelligence Default"
version: "1.0.0"
tags: [team_charter, competitive_intelligence, intelligence, default]
tldr: "Default mission contract for competitive_intelligence crew; swap domain_focus and deadline per instance."
domain: "competitive intelligence governance"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p12_ct_competitive_intelligence.md
  - p02_ra_analyst.md
  - p02_ra_synthesizer.md
  - p02_ra_validator.md
  - bld_examples_team_charter
  - team-charter-builder
  - p01_kc_token_budgeting
  - p11_qg_crew_template
  - bld_collaboration_crew_template
  - p03_pt_orchestration_task_dispatch
---

## Mission Statement
Produce a validated competitive intelligence brief for **{{TARGET_DOMAIN}}**,
grounded on >= 3 named competitors, with all claims source-verified and final
quality >= 9.0 as attested by the validator role.

## Deliverables
1. Raw data KC (`knowledge_card` under P01) -- analyst output; >=3 competitors, source URLs required
2. Intelligence brief KC (`knowledge_card` under P01) -- synthesizer output; competitor matrix + >= 2 structural patterns
3. Validated brief (`knowledge_card` under P01) -- validator-attested; `verdict: approved`, quality >= 9.0

## Success Metrics
- Each deliverable quality >= 9.0 (validator-attested for final brief; 8.5 floor for intermediate)
- Wall-clock under 2100s for the full crew (3 roles x 700s avg)
- Token budget under 90000 total (30000 per role ceiling)
- All 3 a2a-task handoff signals present and archived
- Zero unresolved `[unverified]` tags in the final brief

## Budget
- Tokens: 90000 total (hard ceiling; 30000 per role)
- Wall-clock: 2100s (35 minutes)
- USD: ~3.00 at Sonnet pricing (roughly 30k input + 60k output tokens)

## Configuration
- `domain_focus`: replace `{{TARGET_DOMAIN}}` with the market/technology domain to analyze
- `competitor_scope`: adjust minimum competitor count if the domain is narrow (default: >= 3)
- `quality_gate`: default 9.0; lower to 8.5 for rapid-turnaround exploratory runs

## Stakeholders
- n01_intelligence (nucleus that owns the crew instance -- executes + monitors)
- n07_orchestrator (dispatches, monitors signals, consolidates on completion)
- Consumer of output: specified per run (N06 commercial, N02 marketing, or direct user)

## Escalation Protocol
If any role crosses its token or wall-clock ceiling, or if the validator rejects
the same artifact twice consecutively, emit `signal_{role}_escalate.json` to
`.cex/runtime/signals/`. N01 reads and either extends budget (with justification
logged to decision manifest) or kills the crew and archives partial work.

## Termination Criteria
ANY of:
1. validator emits `verdict: approved` (normal completion)
2. Token or wall-clock budget exhausted (partial work archived)
3. Deadline passed (2026-04-30T23:59 local -- update per instance)
4. 2 consecutive validator rejections on the same artifact (stuck revision loop)

## Instantiation (override defaults per run)
```bash
# Dry run (inspect resolved plan)
python _tools/cex_crew.py show competitive_intelligence

# Live run with this charter
python _tools/cex_crew.py run competitive_intelligence \
    --charter N01_intelligence/P12_orchestration/crews/team_charter_intelligence_default.md \
    --execute

# Override domain at CLI (set env var before run)
TARGET_DOMAIN="B2B SaaS security tools" \
python _tools/cex_crew.py run competitive_intelligence \
    --charter N01_intelligence/P12_orchestration/crews/team_charter_intelligence_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ct_competitive_intelligence.md]] | upstream | 0.50 |
| [[p02_ra_analyst.md]] | upstream | 0.42 |
| [[p02_ra_synthesizer.md]] | upstream | 0.42 |
| [[p02_ra_validator.md]] | upstream | 0.42 |
| [[bld_examples_team_charter]] | upstream | 0.28 |
| [[team-charter-builder]] | related | 0.26 |
| [[p01_kc_token_budgeting]] | upstream | 0.24 |
| [[p11_qg_crew_template]] | upstream | 0.22 |
| [[bld_collaboration_crew_template]] | related | 0.20 |
| [[p03_pt_orchestration_task_dispatch]] | upstream | 0.18 |
