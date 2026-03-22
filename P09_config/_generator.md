# Generator: P09 Config

## QUANDO USAR
- Documentar variavel de ambiente ou path do sistema
- Registrar permissao de acesso (read/write/execute)
- Criar feature flag (on/off, gradual rollout)
- Definir regra de runtime (timeouts, retries, limits)

## TIPOS (escolher template)

### env_config
Naming: `p09_env_{{scope}}.yaml` | Max: 512 bytes
- Campos: name, value, scope (dev/staging/prod), required, fallback
- Exemplo: `FIRECRAWL_API_KEY`, `RAILWAY_TOKEN`

### path_config
Naming: `p09_path_{{scope}}.yaml` | Max: 512 bytes
- Campos: path, purpose, relative_to, os_variants
- Exemplo: repo roots, build outputs, cache dirs

### permission
Naming: `p09_perm_{{scope}}.yaml` | Max: 512 bytes
- Campos: subject, action (read/write/exec), resource, condition
- Exemplo: satellite write access, API key scopes

### feature_flag
Naming: `p09_ff_{{feature}}.yaml` | Max: 256 bytes
- Campos: flag, state (on/off), rollout_pct, owner, expires
- Exemplo: `FIRECRAWL_ENABLED=true`, `MOCK_LLM=false`

### runtime_rule
Naming: `p09_rr_{{rule}}.yaml` | Max: 512 bytes
- Campos: rule, value, unit, context, escalation
- Exemplo: retry 3x, timeout 120s, max_concurrent 3

## PASSO A PASSO
1. SCOUT: verificar se config similar ja existe (grep no repo)
2. CLASSIFICAR: qual dos 5 tipos? (env, path, perm, flag, rule)
3. EXTRAIR valor atual e fonte (onde esta definido hoje)
4. DEFINIR scope: dev, staging, prod, ou all
5. INCLUIR fallback/default (o que acontece se ausente)
6. DOCUMENTAR dependencias (quem consome esta config)
7. VALIDAR contra P09/_schema.yaml
8. SALVAR no formato do tipo escolhido

## TESTE DE COMPLETUDE
Cada config: um dev pode configurar sem perguntar a ninguem?
- SIM: "FIRECRAWL_ENABLED=true, default false, affects enrichment" -> mantem
- NAO: "Set the API key" -> falta: onde obter, formato, scope

## ANTI-PATTERNS
- Config sem fallback/default (sistema quebra se ausente)
- Permissao sem scope (quem? onde? quando?)
- Feature flag sem owner (ninguem sabe quem desliga)
- Runtime rule sem unidade (timeout 120... segundos? ms?)
- Configs duplicadas em multiplos arquivos

---
*Generator v1.0 | Evidence: P01-P08 generators + 5 config types | 2026-03-22*