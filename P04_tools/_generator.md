# Generator: P04 Skill

## QUANDO USAR
- Documentar habilidade reutilizavel
- Criar skill nova com workflow em fases
- Padronizar ferramenta existente

## PASSO A PASSO
1. SCOUT: verificar se skill similar ja existe
2. DEFINIR frontmatter completo (name, trigger, phases, examples)
3. ESCREVER workflow em fases numeradas (input > process > output)
4. INCLUIR metricas reais se disponiveis (speedup, utilization)
5. LISTAR anti-patterns com exemplos concretos
6. VALIDAR contra P04/_schema.yaml
7. SALVAR dual output (.md + .yaml)

## FRONTMATTER = SINGLE SOURCE OF TRUTH
O frontmatter YAML de cada SKILL.md eh a fonte para:
- Routing e descoberta (Brain MCP)
- Invocacao automatica (trigger field)
- Documentacao (description + examples)

## METRICAS (opcional mas valorizado)
Skills com metricas reais tem confianca 2x maior.
Campos: speedup, utilization, latency, error_rate
Fonte: testes reais, nao estimativas

## ANTI-PATTERNS
- Skill sem trigger (ninguem sabe como ativar)
- Skill sem examples (ninguem sabe o que esperar)
- Metricas inventadas (prefira ausencia a mentira)
- Fases sem input/output claro

## TIPOS ADICIONAIS

### mcp_server
QUANDO USAR: Documentar servidor MCP (tools, resources, transport).
Naming: `p04_mcp_{{server}}.md + .yaml`
Schema: P04/_schema.yaml > types > mcp_server

### hook
QUANDO USAR: Definir pre/post processing hook (lifecycle event handler).
Naming: `p04_hook_{{name}}.md`
Schema: P04/_schema.yaml > types > hook

### plugin
QUANDO USAR: Documentar extensao plugavel (modulo opcional carregavel).
Naming: `p04_plug_{{name}}.md + .yaml`
Schema: P04/_schema.yaml > types > plugin

### client
QUANDO USAR: Documentar cliente de API externa (auth, endpoints, rate limits).
Naming: `p04_client_{{api}}.md + .yaml`
Schema: P04/_schema.yaml > types > client

### cli_tool
QUANDO USAR: Documentar ferramenta de linha de comando (flags, usage, examples).
Naming: `p04_cli_{{tool}}.md`
Schema: P04/_schema.yaml > types > cli_tool

### scraper
QUANDO USAR: Documentar extrator de dados web (target, strategy, anti-bot).
Naming: `p04_scraper_{{target}}.md + .yaml`
Schema: P04/_schema.yaml > types > scraper

### connector
QUANDO USAR: Documentar conector de servico externo (auth, endpoints, retry).
Naming: `p04_conn_{{service}}.md + .yaml`
Schema: P04/_schema.yaml > types > connector

### daemon
QUANDO USAR: Documentar processo background (lifecycle, health check, signals).
Naming: `p04_daemon_{{name}}.md + .yaml`
Schema: P04/_schema.yaml > types > daemon

## Dual Output

Cada artefato Tools tem duas versoes:

| Versao | Formato | Leitor | Onde |
|--------|---------|--------|------|
| Humana | .md com frontmatter | Desenvolvedores, revisores | `examples/` e `templates/` |
| Machine | .yaml ou .json (depende do tipo) | LLMs, pipelines, validators | `compiled/` |

### Como compilar
```bash
python _tools/cex_compile.py P04_tools/examples/p04_skill_exemplo.md
# -> gera P04_tools/compiled/p04_skill_exemplo.yaml
```

### O que muda no compilado
- Remove: headers decorativos, bold/italic, links, navegacao
- Mantem: identidade, regras, dados estruturados, exemplos
- Formato: YAML (skills) / JSON (mcp_server, client, connector) (definido em _schema.yaml → machine_format)

---
*Generator v1.0 | Evidence: 58 golden skills, 124 total | 2026-03-22*