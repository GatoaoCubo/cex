# Generator: P10 Memory

## QUANDO USAR
- Criar modelo mental de agente ou satelite
- Configurar indice de busca (BM25, FAISS)
- Registrar aprendizado (sucesso ou falha)
- Capturar estado de sessao (snapshot efemero)
- Definir axioma (regra imutavel)

## TIPOS (escolher template)

### mental_model
Naming: `p10_mm_{{agent}}.yaml` | Max: 2048 bytes
- Campos: domain, identity, tools, constraints, routing_table
- Fonte: como o agente pensa, decide, prioriza

### brain_index
Naming: `p10_bi_{{index}}.yaml` | Max: 1024 bytes
- Campos: engine (BM25/FAISS), scope, embedding_model, rebuild_trigger
- Fonte: config de busca semantica ou keyword

### learning_record
Naming: `p10_lr_{{topic}}.md + .yaml` | Max: 2048 bytes
- Campos: event, outcome (success/fail), score, pattern, anti_pattern
- Fonte: resultado real de execucao (nao estimativa)

### session_state
Naming: `p10_ss_{{session}}.yaml` | Max: 1024 bytes
- Campos: satellite, task, progress_pct, context_tokens, last_action
- Fonte: snapshot do estado atual (efemero, descartavel)

### axiom
Naming: `p10_ax_{{rule}}.md` | Max: 512 bytes
- Campos: rule, rationale, scope, exceptions (se houver)
- Fonte: regra fundamental que nao muda

## PASSO A PASSO
1. SCOUT: verificar se memoria similar ja existe
2. CLASSIFICAR: qual dos 5 tipos? (model, index, record, state, axiom)
3. Para mental_model: mapear domain + tools + constraints
4. Para learning_record: incluir score real e evidencia
5. Para axiom: justificar POR QUE eh imutavel
6. DEFINIR decay: quando esta memoria expira ou precisa refresh?
7. VALIDAR contra P10/_schema.yaml
8. SALVAR dual output (.md + .yaml) quando aplicavel

## TESTE DE UTILIDADE
Cada memoria: alguem vai consultar isso no futuro?
- SIM: "SHAKA mental_model: research domain, firecrawl+brain MCPs" -> mantem
- NAO: "Session started at 14:30" -> session_state efemero, auto-descarta

## ANTI-PATTERNS
- Mental model sem constraints (agente sem limites)
- Learning record sem score (nao se sabe se foi bom)
- Axiom com excecoes demais (nao eh axioma, eh guideline)
- Session state persistido alem da sessao (memory leak)
- Brain index sem rebuild_trigger (indice fica stale)

## Dual Output

Cada artefato Memory tem duas versoes:

| Versao | Formato | Leitor | Onde |
|--------|---------|--------|------|
| Humana | .md com frontmatter | Desenvolvedores, revisores | `examples/` e `templates/` |
| Machine | .yaml otimizado | LLMs, pipelines, validators | `compiled/` |

### Como compilar
```bash
python _tools/cex_compile.py P10_memory/examples/p10_memory_exemplo.md
# -> gera P10_memory/compiled/p10_memory_exemplo.yaml
```

### O que muda no compilado
- Remove: headers decorativos, bold/italic, links, navegacao
- Mantem: identidade, regras, dados estruturados, exemplos
- Formato: YAML (definido em _schema.yaml → machine_format)

---
*Generator v1.0 | Evidence: 7 mental_models + 50 learning_records + brain indexes | 2026-03-22*