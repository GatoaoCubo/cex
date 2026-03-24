# CEX — Cerebro Empresarial X

> Framework universal para organizar conhecimento de AI em 12 Leverage Points.

![version](https://img.shields.io/badge/version-v3.0.0-blue)
![LPs](https://img.shields.io/badge/LPs-12-green)
![density](https://img.shields.io/badge/density-88.6%25-brightgreen)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

**Estado**: v3.0.0 COMPLETE | 12 LPs | 73 tipos | 48 exemplos | 21 templates | 12 generators | 3 validators | 67+ compiled

---

## Quick Stats

| Item | Count | Status |
|------|-------|--------|
| Leverage Points | 12 | P01-P12 todos ativos |
| Schemas (_schema.yaml) | 12 | 68 tipos de artifact |
| Generators (_generator.md) | 12 | Instrucoes por LP |
| Templates | 7 | P01(3)+P02(1)+P03(1)+P04(1)+P05(1) |
| Examples (golden) | 18 | P01(7)+P02(4)+P03(4)+P04(3) |
| Validators | 3 | schema + generator + examples |
| Compiled artifacts | 67+ | All examples have .yaml/.json compiled version |
| Total files | 113+ | ~80KB |
| Density media | 88.6% | Elite:6 High:12 Standard:0 |

---

## Estrutura

    cex/
    ├── _meta/                     # DNA do framework
    │   ├── CODEX.md              # Biblia de meta-construcao (comece aqui)
    │   ├── MANDAMENTOS.md        # 10 leis imutaveis
    │   ├── META_TEMPLATE.md      # Template que gera templates
    │   ├── GLOSSARY.md           # Termos e definicoes
    │   ├── ROADMAP.md            # 6 ondas de desenvolvimento
    │   ├── DECISION_MAP.md       # LP -> type -> format routing table
    │   ├── MIGRATION_MAP.md      # 9916 arquivos classificados por LP
    │   ├── GOLDEN_CANDIDATES.md  # 22 candidatos de migracao
    │   ├── DENSITY_REPORT.md     # Analise dos 18 examples
    │   └── VALIDATION_REPORT.md  # Chain test pass (ATLAS)
    ├── _docs/                     # Documentacao tecnica
    │   └── ARCHITECTURE.md       # ASCII diagrams + LP map + data flow
    ├── _tools/                    # Validators + CLI
    │   ├── validate_schema.py    # Valida _schema.yaml files
    │   ├── validate_generators.py # Valida _generator.md coverage
    │   ├── validate_examples.py  # Valida density + frontmatter
    │   ├── cex_compile.py        # Compila .md examples para .yaml/.json
    │   └── validate_compiled.py  # Valida compiled artifacts
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
    ├── P12_orchestration/        # COMO coordena
    ├── CHANGELOG.md              # Historico de versoes
    └── CONTRIBUTING.md           # Guia de contribuicao

Cada LP contem: `_schema.yaml` + `_generator.md` + `templates/` + `examples/` + `compiled/`

---

## Getting Started

### 1. Entenda o DNA

    _meta/CODEX.md        # Variaveis, anatomia, naming, density tiers
    _meta/MANDAMENTOS.md  # O que nunca violar

### 2. Escolha o LP e leia o generator

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

### 3. Use o template, valide, contribua

    # Copie o template do LP
    cp P01_knowledge/templates/tpl_knowledge_card_domain.md meu_artifact.md

    # Edite, preencha frontmatter, densidade >= 0.80

    # Valide
    python _tools/validate_examples.py

---

## Dual Output Architecture

Every CEX artifact has two versions:

| Version | Format | Reader | Location |
|---------|--------|--------|----------|
| Human | `.md` with YAML frontmatter | Developers, reviewers | `examples/`, `templates/` |
| Machine | `.yaml` or `.json` | LLMs, pipelines, validators | `compiled/` |

### Machine Format by LP

| LP | Default Format | JSON exceptions |
|----|---------------|-----------------|
| P01-P03 | yaml | - |
| P04 | yaml | mcp_server, client, connector |
| P05 | yaml | - |
| P06 | yaml | input_schema, interface, output_schema |
| P07-P08 | yaml | - |
| P09 | yaml | feature_flag |
| P10-P11 | yaml | - |
| P12 | yaml | signal |

### Compile
```bash
python _tools/cex_compile.py P03_prompt/examples/ex_system_prompt.md
python _tools/cex_compile.py --all    # compile everything
```

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

## Documentacao

| Doc | Conteudo |
|-----|---------|
| [ARCHITECTURE.md](_docs/ARCHITECTURE.md) | ASCII diagrams, LP map, data flow, quality gates |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Como adicionar LPs, tipos, migrar, PR checklist |
| [CHANGELOG.md](CHANGELOG.md) | Historico de 6 waves + creditos por satellite |
| [_meta/CODEX.md](_meta/CODEX.md) | DNA completo, variaveis, anatomy, tiers |
| [_meta/MANDAMENTOS.md](_meta/MANDAMENTOS.md) | 10 leis imutaveis |

---

## License

MIT License — see [LICENSE](LICENSE) or use freely with attribution.

    CEX v3.0.0 | Cerebro Empresarial X
    Built with CODEXA satellites (STELLA + SHAKA + PYTHA + EDISON + ATLAS)
    2026-03-23

---

*v3.0.0 | 2026-03-23 | Leia: _meta/CODEX.md*
