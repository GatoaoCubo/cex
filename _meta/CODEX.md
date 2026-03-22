# RECORDS CODEX -- Biblia Universal de Meta-Construcao
## v2.0 | DNA do CEX | LIVING | Atualizado com dados reais

---

## 0. PROPOSITO
DNA do CEX. Hierarquia: CODEX > _schema > _generator > templates > instances
Construido com dados de 9910 MD files, 783 golden, 42KB de destilacao.

## 1. VARIAVEIS
- Tier 1: {{MUSTACHE}} = template engine resolve na geracao
- Tier 2: [BRACKET] = humano/agente resolve na autoria
- {{BRAND_UPPER}} = York preenche no fork
- ${ENV_VAR} = sistema preenche no runtime
- __auto__ = lifecycle preenche automatico
- NUNCA {single_curly} (deprecated) nem [PLACEHOLDER]

## 2. ANATOMIA UNIVERSAL
YAML front: id, type, lp, quality, keywords(3+), long_tails(2+), bullets(3+), axioms(1+)
MD body: title, summary 1-line, secoes por tipo (ver meta-template)
Density >= 0.8 obrigatorio. Max 4KB (ajustado de 2KB baseado em dados).
Prosa > 3 linhas proibida. Bullets com max 80 chars.

## 3. NAMING
Pattern: {lp}_{type}_{topic}.{ext}
Ex: p01_kc_ecommerce_br.md + .yaml (dual)
Regras: lowercase, snake_case, ASCII, max 50 chars

## 4. PASTAS
Brain: P01-P12 (cada com _schema.yaml, _generator.md, templates/, examples/)
Satellites: satellites/{name}/P01-P12 (instances reais)
Meta: _meta/ (CODEX, GLOSSARY, MANDAMENTOS, ROADMAP, META_TEMPLATE)

## 5. SCHEMAS = _schema.yaml por LP
12 schemas criados (68 tipos total). Validado no pre-commit.
Campos padrao: max_bytes, quality_min, frontmatter_required, body_structure

## 6. GENERATORS = _generator.md por LP
4 generators criados (P01-P04 CORE). Instrucoes passo-a-passo.
Anti-patterns listados. Density tiers documentados.

## 7. META-TEMPLATE = _meta/META_TEMPLATE.md
Template que gera templates. Shokunin: evolui durante uso.
Secoes por tipo documentadas. Regras de geracao definidas.

## 8. DUAL OUTPUT = .md (humano) + .yaml (LLM)
Todo artefato = 2 arquivos. Excecoes: _schema (so yaml), _generator (so md)

## 9. LIFECYCLE
CREATE > INDEX > READ > USE > RESULTS > NEW KC > repeat (flywheel)
ARCHIVE: quality<7 + age>30d. PROMOTE: used>10x + quality>9

## 10. DENSITY (DADOS REAIS)

| Tier | Density | Exemplo |
|------|---------|---------|
| Elite | 90-95% | KC_PYTHA_069 (domain, YAML blocks, ASCII flow) |
| High | 80-88% | KC_PYTHA_358 (spec table, code examples) |
| Standard | 70-78% | KC_EDISON_029 (good structure, some prose) |
| Low | <65% | REJEITAR ou refazer |

## 11. INSIGHTS DA DESTILACAO
- 98% golden tem YAML frontmatter
- 82% golden tem 5+ bullets (bullets correlacionam com qualidade)
- 99% faltam keywords (maior gap do codexa-core)
- Semantic Bridge em 60% dos golden templates (boost retrieval)
- ISO count = maturidade de agent (10=baseline, 17=maduro, 22+=golden)
- Skills com metricas reais tem confianca 2x vs sem dados
- 2 sub-templates de KC: Domain (density 92%) vs Meta (density 88%)

## 12. ANTI-FRAGILIDADE
68 CORE fixos + _custom/ extensivel. Promocao: 10x+quality>8=CORE.

---
*CODEX v2.0 | Atualizado com destilacao real | 2026-03-22*