# Generator: P08 Architecture

## QUANDO USAR
- Documentar satelite (role, model, MCPs, constraints)
- Registrar pattern reutilizavel (ex: continuous batching, signal protocol)
- Definir lei operacional (regra inviolavel do sistema)
- Criar diagrama de arquitetura (fluxo, componentes, integracoes)

## TIPOS (ver _schema.yaml)
| Tipo | Naming | Uso |
|------|--------|-----|
| satellite_spec | p08_sat_{{name}}.md + .yaml | Spec de satelite |
| pattern | p08_pat_{{name}}.md + .yaml | Pattern reutilizavel |
| law | p08_law_{{number}}.md | Lei operacional |
| diagram | p08_diag_{{scope}}.md | Diagrama ASCII/Mermaid |
| component_map | p08_cmap_{{scope}}.yaml | Mapa de conexoes |

## PASSO A PASSO
1. SCOUT: verificar se doc similar ja existe (grep + brain_query)
2. CLASSIFICAR: satellite, pattern, law, diagram ou component_map
3. DEFINIR scope (o que este doc cobre e NAO cobre)
4. INCLUIR dados concretos (model, MCPs, latencia, boot time)
5. CRIAR diagrama ASCII (INPUT > PROCESS > OUTPUT, max 15 linhas)
6. MAPEAR dependencias (tabela: component | depends_on | protocol)
7. LISTAR constraints (limites reais: RAM, tokens, terminais, budget)
8. DOCUMENTAR failure modes (o que quebra e como recuperar)
9. VALIDAR contra P08/_schema.yaml (max_bytes: 1024-2048)
10. SALVAR no formato correto (.md para docs, .yaml para maps)

## ANTI-PATTERNS
- Satellite spec sem model/MCPs (spec incompleta)
- Pattern sem exemplo de uso real (teoria sem pratica)
- Law sem justificativa (regra arbitraria nao eh respeitada)
- Diagrama com > 15 linhas (perde legibilidade)
- Component map sem protocol (conexao sem contrato)
- Metricas estimadas como se fossem medidas

## QUALITY TIERS
- Elite (90%+): Spec completa + diagrama + failure modes + metricas reais
- High (80-88%): Spec com dados concretos + diagrama basico
- Standard (70-78%): Documentacao textual com estrutura clara
- Low (<65%): REJEITAR — arquitetura sem dados concretos eh opiniao

---
*Generator v1.0 | Layer: SCALE | 2026-03-22*
