# Generator: P11 Feedback

## QUANDO USAR
- Definir barreira de qualidade (pass/fail com score)
- Criar ciclo de correcao automatica (detect > fix > verify)
- Documentar regra de ciclo de vida (freshness, archive, promote)
- Estabelecer guardrail de seguranca
- Configurar otimizador de processo

## TIPOS (escolher template)

### quality_gate
Naming: `p11_qg_{{gate}}.yaml` | Max: 1024 bytes
- Campos: gate_name, metric, threshold, action_pass, action_fail
- Exemplo: pool score >= 8.0, density >= 0.8, tests pass

### bugloop
Naming: `p11_bl_{{scope}}.md + .yaml` | Max: 2048 bytes
- Campos: detect_trigger, fix_strategy, verify_command, max_retries
- Ciclo: detect > analyze > fix > verify > commit (ou retry)

### lifecycle_rule
Naming: `p11_lc_{{rule}}.yaml` | Max: 512 bytes
- Campos: resource, max_age, action (archive/delete/promote), condition
- Exemplo: handoffs > 7d -> archive, signals > 24h -> delete

### guardrail
Naming: `p11_gr_{{scope}}.yaml` | Max: 512 bytes
- Campos: boundary, trigger, action (block/warn/log), severity
- Exemplo: never push --force to main, never delete pool cards

### optimizer
Naming: `p11_opt_{{target}}.md + .yaml` | Max: 1024 bytes
- Campos: metric, current_value, target_value, action, frequency
- Exemplo: reduce boot time from 15s to 8s via lazy loading

## PASSO A PASSO
1. SCOUT: verificar se feedback loop similar ja existe
2. CLASSIFICAR: qual dos 5 tipos? (gate, bugloop, lifecycle, guardrail, optimizer)
3. DEFINIR metrica concreta (numero, nao adjetivo)
4. DEFINIR threshold com acao clara (pass/fail, nao "review")
5. Para bugloop: incluir max_retries e fallback apos esgotamento
6. Para guardrail: definir severidade (block vs warn vs log)
7. VALIDAR contra P11/_schema.yaml
8. SALVAR no formato do tipo escolhido

## TESTE DE ACIONABILIDADE
Cada feedback: o sistema sabe o que fazer automaticamente?
- SIM: "score < 7.0 -> reject, retry with expanded context" -> mantem
- NAO: "Review quality periodically" -> falta: quando, como, threshold

## ANTI-PATTERNS
- Quality gate sem threshold numerico (subjetivo)
- Bugloop sem max_retries (loop infinito)
- Lifecycle rule sem max_age (acumulo infinito)
- Guardrail sem severidade (tudo parece igual)
- Optimizer sem current_value (nao se mede progresso)

---
*Generator v1.0 | Evidence: Shokunin gates + bugloop skill + 11 active laws | 2026-03-22*