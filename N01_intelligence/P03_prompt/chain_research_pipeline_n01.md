---
id: chain_research_pipeline_n01
kind: chain
pillar: P03
nucleus: n01
title: "N01 Research Pipeline Prompt Chain"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: null
tags: [chain, prompt_chain, research_pipeline, n01, sequential_prompting, analytical_envy]
tldr: "5-step prompt chain for N01 research: DECOMPOSE -> SOURCE -> TRIANGULATE -> SYNTHESIZE -> GOVERN. Each step uses a discrete action prompt from action_prompt_n01.md. Chain output is a scored research brief."
density_score: 0.89
---

<!-- 8F: F1 constrain=P03/chain F2 become=chain-builder F3 inject=action_prompt_n01+reasoning_strategy_n01+system_prompt_n01_research+prompt_template_research_brief F4 reason=sequential prompting beats single-shot for complex research -- each step has sharper focus, and errors can be caught between steps F5 call=cex_compile F6 produce=chain_research_pipeline_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P03_prompt/ -->

## Purpose

A single LLM call cannot do deep research reliably.
This chain breaks the research pipeline into 5 discrete, controllable steps.
Each step has a clear input, output, and validation gate.

Benefits vs. single-shot:
- Error isolation (step 2 failure doesn't corrupt step 5)
- Intermediate validation (catch bias before synthesis)
- Context management (each step uses relevant context, not full dump)
- Retry granularity (retry step 3 without re-running steps 1-2)

## Chain Definition

```yaml
chain_id: research_pipeline_n01
kind: chain
steps: 5
max_tokens_per_step: 4000
retry_policy: max_2_retries_per_step
```

## Step Definitions

### Step 1: DECOMPOSE
```yaml
step_id: decompose
action_prompt: AP-01 (competitive analysis) or AP-02 (market sizing) per task type
input:
  - research_goal: string
  - target_entity: string
  - competitors: list[string] or null
output:
  - atomic_questions: list[string]  # 5-10 questions
  - query_variants: list[string]  # 3 per question (direct, comparative, signal)
  - source_requirements: dict  # per question: required source categories
validation:
  - atomic_questions.length >= 5
  - each question has comparative variant
  - source_requirements covers all question types
retry_on_fail: yes
```

### Step 2: SOURCE
```yaml
step_id: source
action_prompt: search_strategy_n01 + document_loader_n01
input:
  - atomic_questions: (from Step 1)
  - query_variants: (from Step 1)
  - source_requirements: (from Step 1)
output:
  - document_pool: list[DocumentChunk]
  - source_map: dict  # question -> [sources]
  - coverage_report: dict  # % of questions with 3+ sources
validation:
  - document_pool.length >= 10
  - coverage_report.triangulated_pct >= 0.80
  - all sources have URL and date
retry_on_fail: yes (escalate to L2/L3 sources)
```

### Step 3: TRIANGULATE
```yaml
step_id: triangulate
action_prompt: AP-04 (source triangulation)
input:
  - document_pool: (from Step 2)
  - source_map: (from Step 2)
output:
  - verified_claims: list[VerifiedClaim]  # claim + confidence + sources
  - contested_claims: list[ContestedClaim]  # two-sided evidence
  - unsupported_claims: list[str]  # flagged for removal
validation:
  - verified_claims.length >= 5
  - all claims have confidence score
  - no claim with 0 sources passes
retry_on_fail: yes (add sources for failed claims)
```

### Step 4: SYNTHESIZE
```yaml
step_id: synthesize
action_prompt: AP-08 (research synthesis)
input:
  - verified_claims: (from Step 3)
  - contested_claims: (from Step 3)
  - output_template: prompt_template_research_brief.md
output:
  - draft_brief: structured research brief (markdown)
  - comparison_table: if competitive analysis
  - confidence_matrix: per-section confidence
validation:
  - draft_brief contains all template sections
  - comparison_table.entity_count >= 2
  - confidence_matrix populated for all key sections
retry_on_fail: yes
```

### Step 5: GOVERN
```yaml
step_id: govern
action_prompt: quality_gate_advanced_n01 + bias_audit_n01
input:
  - draft_brief: (from Step 4)
  - verified_claims: (from Step 3)
output:
  - quality_score: float
  - gate_results: dict  # H01-H08 pass/fail
  - bias_scores: dict  # B1-B5 scores
  - final_brief: brief (auto-fixed for H07, H08) or REVISION_REQUIRED
validation:
  - all(H01-H08 pass)
  - bias_score.overall >= 7.0
  - quality_score >= 8.0
retry_on_fail: return to Step 4 with specific remediation instructions (max 2)
```

## Chain Execution

```python
def run_research_chain(research_goal: str, entity: str, competitors: list) -> Brief:
    context = {}
    for step in [decompose, source, triangulate, synthesize, govern]:
        result = step.run(context)
        if not step.validate(result):
            result = step.retry(result, context)
            if not step.validate(result):
                raise ResearchChainError(f"Step {step.id} failed after 2 retries")
        context.update(result)
    return context["final_brief"]
```

## Performance Targets

| Step | Expected Tokens | Expected Time |
|------|----------------|--------------|
| Step 1 Decompose | 1000 | 10s |
| Step 2 Source | 500 + API calls | 60s |
| Step 3 Triangulate | 2000 | 20s |
| Step 4 Synthesize | 4000 | 40s |
| Step 5 Govern | 2000 | 20s |
| Total | ~10000 | ~2.5 min |

## Comparison: Prompting Approaches

| Approach | Error Isolation | Context Efficiency | N01 Fit |
|----------|----------------|-------------------|---------|
| Single-shot | none | good | fails on complex tasks |
| Manual multi-step | medium | poor | operator-dependent |
| This chain (automated) | high | excellent | optimal |
| ReAct (tool-use loop) | medium | medium | use for exploratory tasks |
