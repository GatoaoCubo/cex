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
12 generators criados (P01-P12 CORE+QUALITY+SCALE). Instrucoes passo-a-passo.
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

## 13. ESTADO ATUAL (2026-03-22)

| LP | Schema | Generator | Templates | Examples | Completude |
|----|--------|-----------|-----------|----------|------------|
| P01 Knowledge | SIM | SIM | 3 | 7 | CORE completo |
| P02 Model | SIM | SIM | 1 | 4 | CORE completo |
| P03 Prompt | SIM | SIM | 1 | 4 | CORE completo |
| P04 Tools | SIM | SIM | 1 | 3 | CORE completo |
| P05 Output | SIM | SIM | 1 | 0 | template only |
| P06-P12 | SIM x7 | SIM x7 | 0 | 0 | generator only |
| **Total** | **12** | **12** | **7** | **18** | Wave 5 |

**Metricas Wave 3+4:**
- Wave 3: 8 commits, 12 generators criados, 7 templates, 18 examples, chain test pass
- Wave 4: 2 commits, migration map (9916 arquivos), 12 golden migrados (4KC+3AGT+3PT+2SKL)
- Density media dos examples: 88.6% (Elite:6 High:12 Standard:0)

**Decisoes Tomadas:**
- Migration map: 9 categorias (KC, HOP, AGT, SKL, FAT, ADW, BLK, CHK/VAL, OUTROS)
- Density threshold: >= 0.80 obrigatorio, >= 0.90 = Elite/golden candidate
- Templates CORE: P01-P04 + P05 = 7 templates (P06-P12 aguardam Wave 5.3)
- Max file size: 4KB (ajustado de 2KB baseado em dados reais dos examples)
- Golden promotion: quality >= 9.5 + density >= 0.90 + cross-referenced

---
*CODEX v3.0 | Wave 5 | 2026-03-22*