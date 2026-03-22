# Generator: P01 Knowledge Card

## QUANDO USAR
- Capturar fato de pesquisa, insight de mercado, pattern
- Documentar referencia tecnica (model specs, API docs)
- Registrar regra de negocio com metricas

## TIPOS DE KC (escolher template)

### Domain KC (negocio)
Template: KC_PYTHA_069 (density 92%)
- Quick Reference (YAML block) > Conceitos > Fases > Regras de Ouro > Flow > Comparativo
- Ideal para: estrategias, processos, mercado

### Meta KC (tecnico)
Template: KC_PYTHA_358 (density 88%)
- Summary > Spec Table > Patterns > Anti-Patterns > Application > References
- Ideal para: APIs, ferramentas, frameworks, configs

## PASSO A PASSO

1. SCOUT: buscar se KC similar ja existe (brain_query ou grep)
2. CLASSIFICAR: domain ou meta? (escolhe template)
3. EXTRAIR fatos atomicos (1 bullet = 1 fato, max 80 chars)
4. GERAR keywords (3+ head terms do dominio)
5. GERAR long_tails (2+ perguntas que alguem faria)
6. DEFINIR axioms (1+ regra que muda comportamento)
7. INCLUIR dados especificos (precos, %, APIs, datas)
8. CALCULAR density (estimar tokens uteis / total >= 0.8)
9. VALIDAR contra P01/_schema.yaml
10. SALVAR dual output (.md + .yaml)

## TESTE DE ESPECIFICIDADE
Cada frase: um dev pode agir sem ler docs externos?
- SIM: "Buy Box: Logistics 40%, Price 30%" -> mantem
- NAO: "Follow best practices" -> corta ou expande

## ANTI-PATTERNS
- Prosa corrida > 3 linhas
- Campos vazios (TBD, TODO, placeholder)
- Bullets genericos sem dados
- Secoes com < 3 linhas substantivas
- Code blocks com ... (truncados)
- quality YAML != quality body (delta max 0.5)

## DENSITY TIERS
- Elite (90-95%): Domain KCs com YAML blocks + ASCII flow
- High (80-88%): Spec tables + code examples
- Standard (70-78%): Good structure mas alguma prosa
- Low (<65%): REJEITAR ou refazer

---
*Generator v1.0 | Evidence: 7 golden KCs + 783 golden pool | 2026-03-22*