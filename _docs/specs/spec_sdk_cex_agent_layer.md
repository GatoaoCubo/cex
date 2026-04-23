---
quality: 8.7
id: spec_sdk_cex_agent_layer
kind: constraint_spec
pillar: P06
title: "Spec -- CEXAgent: SDK Runtime Layer com 8F + Context + Signal"
version: 1.0.0
created: "2026-04-18"
author: n07_orchestrator
domain: sdk_runtime
quality_target: 9.0
status: SPEC
scope: cex_sdk + _tools
depends_on: [spec_full_coverage_plan, sdk_wiring_distribution]
tags: [spec, sdk, cex_agent, 8f, runtime, context_injection]
tldr: "Construir CEXAgent no cex_sdk -- camada inteligente que conecta chat() ao pipeline 8F real (KCs, schema, validator, signal), tornando o SDK CEX-aware e util para o N07 e para usuarios externos."
density_score: 0.95
updated: "2026-04-22"
---

## Problema

O cex_sdk hoje e transporte burro.

`chat()` chama o LLM sem contexto do CEX. Um usuario externo que faz
`from cex_sdk import chat; chat("o que e CEX?")` recebe "exchange de cripto".

O 8F pipeline -- com KCs injetados, schema validado, signal emitido -- existe
so nos `_tools/` como scripts CLI. Nao e acessivel como biblioteca.

Consequencias:
- SDK nao demonstra o valor do CEX para usuarios externos
- N07 invoca scripts que rodam 8F "na mao" (fragil, inconsistente)
- Trocar nucleus ou kind exige editar multiplos scripts
- Nenhum enforcement inline de qualidade (F7) nos tools

## Visao

`CEXAgent` e a camada que faltava entre `chat()` (transporte) e o 8F pipeline (logica).

```python
# HOJE -- burro
from cex_sdk import chat
chat("build an agent for sales")  # responde sobre CEX Exchange

# DEPOIS -- CEX-aware
from cex_sdk import CEXAgent
agent = CEXAgent(nucleus="n03", kind="agent")
result = agent.build("build an agent for sales")
# -> F1: kind=agent, pillar=P02 resolvido
# -> F3: kc_agent.md + examples injetados no prompt
# -> F6: artifact gerado com frontmatter correto
# -> F7: Validator.for_kind("agent") aplicado inline
# -> F8: signal emitido automaticamente
```

Para o N07: cada `python _tools/cex_8f_runner.py` passa a usar CEXAgent
internamente -- pipeline completo, nao mais chat() direto.

## Decisoes (autonomas -- usuario disse "quero tudo feito")

| Decisao | Escolha | Motivo |
|---------|---------|--------|
| Context injection | lazy load de KCs via filesystem | zero dependencia externa, funciona offline |
| KC path strategy | `N00_genesis/P01_knowledge/library/kind/kc_{kind}.md` | caminho canonico ja existente |
| F7 inline | `cex_sdk.schema.Validator.for_kind()` ja existente | reusar o que foi construido |
| Signal format | arquivo JSON em `.cex/runtime/signals/` | padrao atual do CEX |
| Provider fallback | OpenAI se Anthropic falhar, Ollama se ambos falharem | chain existente em nucleus_models.yaml |
| 8F trace | string retornada junto com artifact | visibilidade sem logging externo |
| Escopo W1 | CEXAgent core + context injection + validator + signal | base solida antes de wiring avancado |
| Escopo W2 | wire cex_8f_runner.py + cex_crew_runner.py para usar CEXAgent | impacto imediato nos tools que N07 usa |

## Arquitetura

```
cex_sdk/
  agent/                     <- NOVO modulo
    __init__.py              <- exporta CEXAgent, BuildResult
    cex_agent.py             <- classe principal
    context_loader.py        <- carrega KCs + examples do filesystem
    signal_emitter.py        <- emite signals para .cex/runtime/signals/
    f8_pipeline.py           <- orquestra F1->F8 usando pecas do SDK

_tools/
  cex_8f_runner.py           <- WIRE: usa CEXAgent internamente
  cex_crew_runner.py         <- WIRE: usa CEXAgent para cada role

cex_sdk/__init__.py          <- adiciona: from cex_sdk.agent import CEXAgent, BuildResult
```

## Artifacts

### Wave 1: CEXAgent Core (5 arquivos novos)

| Acao | Path | Kind | Est. Size | Notas |
|------|------|------|-----------|-------|
| CREATE | `cex_sdk/agent/__init__.py` | interface | 1KB | exporta CEXAgent, BuildResult |
| CREATE | `cex_sdk/agent/context_loader.py` | document_loader | 4KB | carrega KC + examples lazy |
| CREATE | `cex_sdk/agent/signal_emitter.py` | signal | 2KB | escreve JSON em .cex/runtime/signals/ |
| CREATE | `cex_sdk/agent/f8_pipeline.py` | workflow | 5KB | F1->F8 sequencial com trace string |
| CREATE | `cex_sdk/agent/cex_agent.py` | agent | 6KB | classe CEXAgent com build() + validate() + signal() |

### Wave 2: Barrel + Wire (3 arquivos modificados)

| Acao | Path | Kind | Est. Size | Notas |
|------|------|------|-----------|-------|
| REWRITE | `cex_sdk/__init__.py` | interface | +5 linhas | adiciona CEXAgent no barrel export |
| REWRITE | `_tools/cex_8f_runner.py` | cli_tool | patch | usa CEXAgent se disponivel, fallback raw |
| REWRITE | `_tools/cex_crew_runner.py` | cli_tool | patch | usa CEXAgent por role |

### Wave 3: Spec + Docs (1 arquivo novo)

| Acao | Path | Kind | Est. Size | Notas |
|------|------|------|-----------|-------|
| CREATE | `_docs/specs/spec_sdk_cex_agent_layer.md` | constraint_spec | 5KB | este arquivo |

## Interface Publica (contrato)

```python
# cex_sdk/agent/cex_agent.py

@dataclass
class BuildResult:
    artifact: str          # conteudo gerado (frontmatter + body)
    kind: str
    pillar: str
    score: float           # resultado do Validator inline
    passed: bool           # score >= 8.0
    trace: str             # "F1:agent/P02 F3:2KCs F7:8.2/10 F8:signal_sent"
    errors: list[str]
    signal_path: str | None

class CEXAgent:
    def __init__(
        self,
        nucleus: str = "n03",
        kind: str = "",
        model: str = "claude-sonnet-4-6",
        repo_root: str = "",   # auto-detectado via __file__ se vazio
    ): ...

    def build(self, intent: str, *, system: str = "") -> BuildResult:
        """F1 -> F8: resolve kind, injeta KCs, gera, valida, sinaliza."""

    def validate(self, payload: dict) -> ValidatorResult:
        """F7 standalone: valida artifact sem gerar."""

    def signal(self, score: float, status: str = "complete") -> str:
        """F8 standalone: emite signal file."""
```

## Context Loader -- o que injeta

```python
# context_loader.py carrega em ordem:
# 1. kc_{kind}.md  -- N00_genesis/P01_knowledge/library/kind/
# 2. tpl_{kind}.md -- N00_genesis/compiled/ (se existir)
# 3. bld_instruction_{kind}.md -- archetypes/builders/{kind}-builder/ (se existir)
# 4. Primeiros 3 exemplos de examples/ do builder (se existir)
# Total injetado: ~4-8KB de contexto CEX-especifico
```

## Signal Format (compativel com CEX atual)

```json
{
  "nucleus": "n03",
  "status": "complete",
  "score": 8.5,
  "kind": "agent",
  "timestamp": "2026-04-18T22:00:00",
  "source": "cex_sdk.agent"
}
```

Salvo em: `.cex/runtime/signals/signal_{nucleus}_{timestamp}.json`

## 8F Trace (o que o usuario ve)

```
=== CEXAgent 8F TRACE ===
F1 CONSTRAIN : kind=agent, pillar=P02
F2 BECOME    : context loaded (kc_agent.md + 2 examples, 5.2KB)
F3 INJECT    : prompt assembled (system=builder, user=intent+context)
F4 REASON    : model=claude-sonnet-4-6, provider=anthropic
F5 CALL      : chat() -> 1847 chars
F6 PRODUCE   : artifact generated (frontmatter detected: yes)
F7 GOVERN    : score=8.7, gates=6/7, passed=True
F8 COLLABORATE: signal -> .cex/runtime/signals/signal_n03_20260418.json
=========================
```

## Done When

- [ ] `from cex_sdk import CEXAgent` funciona
- [ ] `CEXAgent(nucleus="n03", kind="agent").build("build X")` retorna BuildResult
- [ ] Context loader encontra kc_{kind}.md para kinds existentes
- [ ] Validator inline roda F7 sem chamar script externo
- [ ] Signal file escrito em .cex/runtime/signals/
- [ ] `cex_8f_runner.py` usa CEXAgent quando importavel
- [ ] ASCII compliance: cex_sanitize --check --scope cex_sdk/agent/ PASS
- [ ] 8F trace visivel no resultado
- [ ] `python -c "from cex_sdk import CEXAgent"` sem erro
- [ ] Commit: `[N03] cex_sdk agent layer: CEXAgent + context_loader + signal_emitter`

## Complexidade e Risco

| Componente | Risco | Mitigacao |
|------------|-------|-----------|
| context_loader path detection | medio -- paths variam por OS | usar Path(__file__).resolve() + fallback |
| KC nao existe para kind raro | baixo -- graceful skip | log warning, continua sem KC |
| Validator score vs qualidade real | medio -- heuristica, nao semantica | documentar limitacao, suficiente para F7 estrutural |
| Wire em cex_8f_runner.py | baixo -- try/except CEXAgent, fallback raw | nao quebra comportamento existente |

## Dispatch

```bash
bash _spawn/dispatch.sh solo n03 "build CEXAgent SDK layer per spec_sdk_cex_agent_layer.md"
```

N03 le este spec + constroi as 5 pecas do Wave 1 + wire do Wave 2.
N07 consolida e testa apos signal.
