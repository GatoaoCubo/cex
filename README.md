# CEX - Cerebro Empresarial X

Framework universal de cerebro empresarial com 12 Leverage Points.
Cada arquivo neste repo e um Record denso, validado, dual-output.

**Estado**: Wave 5/6 | 12 LPs | 68 tipos | 18 exemplos | 7 templates | 12 generators

---

## Quick Stats

| Item | Count | Status |
|------|-------|--------|
| Leverage Points | 12 | P01-P12 todos ativos |
| Schemas (_schema.yaml) | 12 | 68 tipos de artifact |
| Generators (_generator.md) | 12 | Instrucoes por LP |
| Templates | 7 | P01(3)+P02+P03+P04+P05 |
| Examples (golden) | 18 | P01(7)+P02(4)+P03(4)+P04(3) |
| Total MD files | 46 | ~65KB |
| Density media | 88.6% | Elite:6 High:12 Standard:0 |

---

## Estrutura

    cex/
    ├── _meta/                     # DNA do framework
    │   ├── CODEX.md              # Biblia de meta-construcao (comece aqui)
    │   ├── DENSITY_REPORT.md     # Analise de densidade dos 18 examples
    │   ├── GLOSSARY.md           # Termos e definicoes
    │   ├── GOLDEN_CANDIDATES.md  # Fila de migracao do codexa-core (22 candidatos)
    │   ├── MANDAMENTOS.md        # Regras imutaveis
    │   ├── META_TEMPLATE.md      # Template que gera templates
    │   ├── MIGRATION_MAP.md      # 9916 arquivos classificados por LP
    │   ├── ROADMAP.md            # 6 ondas de desenvolvimento
    │   └── VALIDATION_REPORT.md  # Resultados do chain test
    ├── P01_knowledge/            # O que o agente SABE       (7 ex, 3 tpl)
    ├── P02_model/                # QUEM o agente EH          (4 ex, 1 tpl)
    ├── P03_prompt/               # COMO o agente FALA        (4 ex, 1 tpl)
    ├── P04_tools/                # O que o agente USA        (3 ex, 1 tpl)
    ├── P05_output/               # O que o agente ENTREGA    (0 ex, 1 tpl)
    ├── P06_schema/               # CONTRATOS de validacao
    ├── P07_evals/                # COMO medir qualidade
    ├── P08_architecture/         # COMO escala
    ├── P09_config/               # COMO configura
    ├── P10_memory/               # O que LEMBRA
    ├── P11_feedback/             # COMO melhora
    └── P12_orchestration/        # COMO coordena

Cada LP contem: `_schema.yaml` + `_generator.md` + `templates/` + `examples/`

---

## Getting Started

### 1. Entenda o DNA

    _meta/CODEX.md        # Variaveis, anatomia, naming, density tiers
    _meta/MANDAMENTOS.md  # O que nunca violar

### 2. Escolha o LP certo

| Voce quer criar... | LP | Tipo |
|--------------------|----|------|
| Knowledge card de dominio | P01 | domain_kc |
| Knowledge card meta/framework | P01 | meta_kc |
| Agent com capabilities | P02 | agent |
| System prompt / HOP | P03 | prompt_template |
| Skill invocavel | P04 | skill |
| Output schema de agent | P05 | output_schema |
| Metrica de avaliacao | P07 | eval_metric |
| Workflow de orquestracao | P12 | workflow |

### 3. Leia o generator do LP

    P01_knowledge/_generator.md   # Passo-a-passo + anti-patterns
    P02_model/_generator.md       # Estrutura de agent + exemplos
    P03_prompt/_generator.md      # Tipos de prompt + templates prontos
    P04_tools/_generator.md       # Skill anatomy + quality gates

### 4. Use o template como base

    P01_knowledge/templates/tpl_knowledge_card_domain.md
    P01_knowledge/templates/tpl_knowledge_card_meta.md
    P02_model/templates/tpl_agent.md
    P03_prompt/templates/tpl_prompt_template.md
    P04_tools/templates/tpl_skill.md

### 5. Regras de validacao

- YAML frontmatter obrigatorio: `id`, `type`, `lp`, `quality`, `tags`, `tldr`
- Density score >= 0.80 (declare `density_score` no YAML)
- Naming: `{lp}_{type}_{topic}.md` ex: `p01_kc_ecommerce_br.md`
- Max 4KB por arquivo (densidade > volume)
- Prosa em blocos > 3 linhas: converter em bullets

---

## Exemplos Destaque

| File | LP | Density | Por que ler |
|------|----|---------|-------------|
| p03_pt_action_prompt | P03 | 0.95 | Formato mais denso do repo |
| p04_skill_ml_ads | P04 | 0.91 | YAML I/O + funnel table |
| p01_kc_catalogo_proprio_mercado_livre | P01 | 0.92 | Domain mastery compacto |
| p02_agent_gateway | P02 | 0.87 | ASCII diagram + routing table |
| p01_kc_agent_orchestration_quickstart | P01 | 0.90 | Multi-agent mapping |

---

*v1.0.0 | Wave 5/6 | 2026-03-22 | Leia: _meta/CODEX.md*
