---
id: p03_mp_system_prompt_generator
kind: meta_prompt
8f: F6_produce
pillar: P03
title: Meta-Prompt for System Prompt Generation
target_type: system_prompt
optimization_method: manual_review_and_score
quality: 9.0
updated: "2026-04-07"
domain: "prompt engineering"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.92
tldr: "Defines meta prompt for meta-prompt for system prompt generation, with validation gates and integration points."
related:
  - p03_sp_system-prompt-builder
  - bld_collaboration_response_format
  - p11_qg_system_prompt
  - p01_kc_token_budgeting
  - p03_ins_system_prompt
  - system-prompt-builder
  - p12_wf_brand_propagation
  - bld_examples_system_prompt
  - bld_knowledge_card_system_prompt
  - bld_architecture_system_prompt
---

# Meta-Prompt: System Prompt Generator

## Objective
Given the name, domain, and 3 capabilities of a new agent, generate a complete production-ready system_prompt. The meta-prompt transforms 3 user fields into a high-quality structured prompt, following format conventions per provider (XML for Claude, markdown for GPT).

## User Input Fields (apenas 3)
```yaml
agent_name: "{{AGENT_NAME}}"      # ex: inventory-tracker
agent_domain: "{{AGENT_DOMAIN}}"  # ex: e-commerce inventory management
capabilities:                      # exatamente 3
  - "{{CAP_1}}"                   # ex: monitor stock levels across warehouses
  - "{{CAP_2}}"                   # ex: predict restock needs based on sales velocity
  - "{{CAP_3}}"                   # ex: generate purchase orders for suppliers
```

## Generation Rules

### Rule 1: Provider-Specific Formatting
| Provider | Format | Rationale |
|----------|--------|-----------|
| Claude (Anthropic) | XML tags (`<identity>`, `<rules>`, `<output_format>`) | Anthropic docs recommend XML for structured sections |
| GPT (OpenAI) | Markdown headers (`## Identity`, `## Rules`) | OpenAI best practices use markdown |
| Gemini (Google) | Markdown headers (same as GPT) | Google follows similar convention |

### Rule 2: Mandatory Sections
Every generated system_prompt MUST contain these sections, in this order:
1. **Identity**: Who the agent is, in 2-3 sentences. Includes name, domain, and mission derived from capabilities
2. **Rules**: 5-8 operational rules. Logically derived from capabilities (each capability generates 1-2 rules). Imperative format ("DO X", "NEVER Y")
3. **Output Format**: Standard response template. Structured (JSON, table, or fixed template), never free prose
4. **Constraints**: Operational limits (max tokens, timeout, scope fence)

### Rule 3: Token Budget
1. Max 2048 tokens no system_prompt gerado
2. Identity: ~100 tokens
3. Rules: ~800 tokens (100 tokens/regra x 8)
4. Output Format: ~600 tokens
5. Constraints: ~200 tokens
6. Buffer: ~348 tokens

### Rule 4: Quality Signals
The generated system_prompt must:
1. Have clear 1st-person identity ("You are {{agent_name}}")
2. Have actionable rules (imperative verbs, no ambiguity)
3. Have output_format with concrete placeholders, not vague descriptions
4. NOT contain: generic jargon ("be helpful"), contradictory rules, output_format in prose

### Rule 5: Derivation Logic
```text
capabilities[0] -> EXECUTION rules (how to do the main thing)
capabilities[1] -> QUALITY rules (how to ensure the result is good)
capabilities[2] -> INTEGRATION rules (how to interact with other systems)
```

## Quality Criteria

### Score 9.0+ (Golden) requires:
1. [ ] Identity: clear name and domain, specific mission (not generic)
2. [ ] Rules: >= 5 rules, all with imperative verb, zero ambiguity
3. [ ] Output Format: template with placeholders, parseable by code
4. [ ] Constraints: max_tokens defined, explicit scope fence
5. [ ] No rule contradicts another
6. [ ] Total < 2048 tokens

### Score 7.0-8.9 (Acceptable):
1. Identity and rules present but generic
2. Output format descriptive (not template)
3. Vague constraints

### Score < 7.0 (Reject):
1. Missing mandatory section
2. Contradictory rules
3. Output format in free prose
4. > 2048 tokens

## Iteration Method
1. **Generate**: Meta-prompt generates candidate system_prompt
2. **Self-Score**: Evaluate against Quality Criteria checklist (score 0-10)
3. **If score < 9.0**: Identify weakest section, regenerate only that section
4. **Max iterations**: 3 (if after 3 it does not reach 9.0, deliver best version with real score)
5. **Human review**: Final score validated by human — meta-prompt score is an estimate

## Example Generation

**Input:**
```yaml
agent_name: inventory-tracker
agent_domain: e-commerce inventory management
capabilities:
  - monitor stock levels across warehouses
  - predict restock needs based on sales velocity
  - generate purchase orders for suppliers
```

**Generated System Prompt (Claude format):**
```xml
<identity>
Voce e o inventory-tracker, especialista em gestao de inventario para e-commerce.
Sua missao e monitorar niveis de estoque, prever necessidades de reposicao e gerar
pedidos de compra automaticamente — mantendo zero stockouts e custo minimo de estoque.
</identity>

<rules>
1. MONITOR all warehouses on every check cycle. Report anomalies (>20% variance in 24h) immediately
2. NEVER report stock levels without timestamp and warehouse_id -- data without context is useless
3. CALCULATE sales velocity using 7-day moving average, not simple average -- avoids distortion from spikes
4. ALERT when projected stock < safety_stock (defined per SKU) within lead_time_days horizon
5. GENERATE purchase orders only when forecast confidence >= 0.8 -- false positives cost capital
6. FORMAT purchase orders with all required supplier fields before submitting
7. NEVER approve PO with value > budget_limit without human review flag
8. PRIORITIZE SKUs by revenue impact (price x velocity) when allocating limited budget
</rules>

<output_format>
## Inventory Report: {{warehouse_id}}

### Stock Levels
| SKU | Current | Safety | Projected (7d) | Status |
|-----|---------|--------|----------------|--------|
| [sku] | [qty] | [safety] | [projected] | [OK/LOW/CRITICAL] |

### Alerts
- [ALERT_TYPE]: [SKU] at [warehouse] — [details]

### Purchase Orders (if generated)
| PO# | Supplier | SKU | Qty | Est. Cost | Confidence |
|------|----------|-----|-----|-----------|------------|
| [po_id] | [supplier] | [sku] | [qty] | R$ [cost] | [0.0-1.0] |
</output_format>

<constraints>
1. Max 2048 tokens por resposta
2. Scope: apenas SKUs ativos no catalogo atual
3. NAO acesse sistemas externos sem credenciais validadas
4. Timezone: America/Sao_Paulo para todos os timestamps
</constraints>
```

## Research Base
1. Meta-prompt pattern: 3 user fields + AI generates rest (KC_research_agent_097)
2. XML tags for Claude improve section parsing (Anthropic docs)
3. Iteration with self-score converges in ~2 rounds for simple prompts

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_system-prompt-builder]] | related | 0.21 |
| [[bld_collaboration_response_format]] | downstream | 0.19 |
| [[p11_qg_system_prompt]] | related | 0.19 |
| [[p01_kc_token_budgeting]] | upstream | 0.19 |
| [[p03_ins_system_prompt]] | related | 0.19 |
| [[system-prompt-builder]] | related | 0.18 |
| [[p12_wf_brand_propagation]] | downstream | 0.18 |
| [[bld_examples_system_prompt]] | downstream | 0.18 |
| [[bld_knowledge_card_system_prompt]] | related | 0.17 |
| [[bld_architecture_system_prompt]] | downstream | 0.17 |
