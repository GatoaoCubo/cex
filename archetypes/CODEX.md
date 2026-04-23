# RECORDS CODEX -- Biblia Universal de Meta-Construcao
## v6.0.0 | DNA do CEX | LIVING | Atualizado com dados reais

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
Dual: todo artifact .md tem compiled/ counterpart (.yaml ou .json per machine_format).

## 3. NAMING
Pattern: {lp}_{type}_{topic}.{ext}
Ex: p01_kc_ecommerce_br.md + .yaml (dual)
Regras: lowercase, snake_case, ASCII, max 50 chars

## 4. PASTAS
Brain: P01-P12 (cada com _schema.yaml, _generator.md, templates/, examples/)
Agent_groups: agent_groups/{name}/P01-P12 (instances reais)
Meta: archetypes/ (CODEX, GLOSSARY, MANDAMENTOS, ROADMAP, META_TEMPLATE)

## 5. SCHEMAS = _schema.yaml por pillar
12 schemas criados (78 kinds total). Validado no pre-commit.
Campos padrao: max_bytes, quality_min, frontmatter_required, body_structure
Campo obrigatorio v3.0: `machine_format` (yaml|json) — define formato compiled/.

## 6. GENERATORS = _generator.md por pillar
12 generators criados (P01-P12 CORE+QUALITY+SCALE). Instrucoes passo-a-passo.
Anti-patterns listados. Density tiers documentados.

## 7. META-TEMPLATE = archetypes/META_TEMPLATE.md
Template que gera templates. Shokunin: evolui durante uso.
Secoes por tipo documentadas. Regras de geracao definidas.

## 8. DUAL OUTPUT = .md (humano) + .yaml/.json (machine)
Todo artefato = 2 arquivos. Excecoes: _schema (so yaml), _generator (so md)
Campo obrigatorio em _schema.yaml: `machine_format` (yaml|json). 78 kinds: 64 yaml, 9 json.
Regra: todo example DEVE ter versao compilada em compiled/.
Compile: `python _tools/cex_compile.py --all` gera compiled/ em cada pillar.
Routing: archetypes/DECISION_MAP.md (arquivo -> pillar -> tipo -> format).

## 9. LIFECYCLE
CREATE > INDEX > READ > USE > RESULTS > NEW KC > repeat (flywheel)
ARCHIVE: quality<7 + age>30d. PROMOTE: used>10x + quality>9

## 10. DENSITY (DADOS REAIS)

| Tier | Density | Exemplo |
|------|---------|---------|
| Elite | 90-95% | KC_knowledge_agent_069 (domain, YAML blocks, ASCII flow) |
| High | 80-88% | KC_knowledge_agent_358 (spec table, code examples) |
| Standard | 70-78% | KC_builder_agent_029 (good structure, some prose) |
| Low | <65% | REJEITAR ou refazer |

## 11. INSIGHTS DA DESTILACAO
- 98% golden tem YAML frontmatter
- 82% golden tem 5+ bullets (bullets correlacionam com qualidade)
- 99% faltam keywords (maior gap do organization-core)
- Semantic Bridge em 60% dos golden templates (boost retrieval)
- ISO count = maturidade de agent (10=baseline, 17=maduro, 22+=golden)
- Skills com metricas reais tem confianca 2x vs sem dados
- 2 sub-templates de KC: Domain (density 92%) vs Meta (density 88%)

## 12. ANTI-FRAGILIDADE
68 CORE fixos + _custom/ extensivel. Promocao: 10x+quality>8=CORE.

## 13. ESTADO FINAL (v1.0.0 — 2026-03-22)

| pillar | Schema | Generator | Templates | Examples | Completude |
|----|--------|-----------|-----------|----------|------------|
| P01 Knowledge | SIM | SIM | 3 | 7 | CORE completo |
| P02 Model | SIM | SIM | 1 | 4 | CORE completo |
| P03 Prompt | SIM | SIM | 1 | 4 | CORE completo |
| P04 Tools | SIM | SIM | 1 | 3 | CORE completo |
| P05 Output | SIM | SIM | 1 | 0 | template only |
| P06-P12 | SIM x7 | SIM x7 | 0 | 0 | generator only |
| **Total** | **12** | **12** | **7** | **18** | v1.0.0 |

**Metricas Acumuladas (6 Waves):**
- Wave 1: 42KB destilado, P01 schema v0, 1 golden example
- Wave 2: 12 schemas, 78 kinds, CORE+QUALITY+SCALE layers
- Wave 3: 12 generators, 7 templates, 18 examples, chain test PASS
- Wave 4: migration map (9916 arquivos), 12 golden migrados, 22 candidatos
- Wave 5: density report 88.6%, 3 validators, meta-docs v3
- Wave 6: bootstrap CLI, dogfood, ARCHITECTURE+CONTRIBUTING+CHANGELOG, v1.0 docs

## 14. HISTORICO DE DECISOES

| Wave | Decisao | Razao |
|------|---------|-------|
| W1 | Max file size = 4KB (nao 2KB) | Dados reais: golden avg ~3KB, 2KB truncava informacao |
| W1 | Dual output .md + .yaml | .md = leitura humana, .yaml = LLM embedding otimizado |
| W2 | 12 LPs (nao 8 ou 16) | Cobertura completa sem overlap: P01-P04 CORE = suficiente para 95% dos casos |
| W2 | 78 kinds fixos + _custom/ extensivel | Estabilidade do schema + flexibilidade para dominios especificos |
| W3 | Meta-template antes dos templates | Templates derivados de meta = consistencia garantida (DRY) |
| W3 | Generator APENAS para primary type | Secondary kinds: schema define, humano interpola. Gera mais tipos, menos overhead |
| W4 | Migration map primeiro, migrar depois | Classificar 9916 arquivos antes de migrar evita retrabalo de re-classificacao |
| W4 | 12 golden primeiro (nao 638) | Qualidade > quantidade. 12 perfeitos ensinam mais que 638 mediocres |
| W5 | Density >= 0.80 obrigatorio (nao 0.75) | Dados: todos os 18 examples ficaram acima de 0.85. 0.80 = floor real |
| W5 | Elite = 0.90+ (nao 0.95+) | 0.95 = apenas 1 example. 0.90 = 6 examples = tier saudavel |
| W6 | Bootstrap CLI antes de mass migration | CLI permite qualquer repo usar CEX; mass migration = apenas organization-core |

## 15. PRINCIPIOS CONSOLIDADOS (6 Waves)

| # | Principio | Origem |
|---|-----------|--------|
| 1 | Densidade > volume | W1: 783 golden > 9127 mediocres |
| 2 | Schema primeiro, generator depois | W2-W3: schema = contrato, generator = instrucao |
| 3 | Dados reais superam estimativas | W1: 4KB (nao 2KB), 0.88 avg (nao 0.75 assumed) |
| 4 | Flywheel: CEX gera CEX | W6: dogfood = framework auto-aplica seus proprios principios |
| 5 | 12 perfeitos > 638 mediocres | W4: golden migration prioriza qualidade sobre cobertura |
| 6 | Meta-template = fonte da verdade | W3: toda inconsistencia de template = falta de alinhamento com META_TEMPLATE |
| 7 | Bullets com 80 chars = scan rapido | W3: density analysis comprovou correlacao bullets-qualidade |
| 8 | id == filename stem (sempre) | W3: chain test revelou inconsistencias silenciosas sem essa regra |
| 9 | _custom/ para dominios, CORE fixo | W5: anti-fragilidade = 78 kinds estaveis + extensoes isoladas |
| 10 | Validate early, validate often | W3: chain test antes de escalar evitou propagacao de erros |

---
*CODEX v6.0.0 | 2026-03-27*