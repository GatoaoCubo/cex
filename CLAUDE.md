# CLAUDE.md — CEX Entry Point

**Auto-loaded** | Toda sessao neste repo le este arquivo primeiro.

---

## VOCE ESTA NO CEX

CEX = Company Experience X. O cerebro empresarial.
Este repo eh o **diamante** (produto). NAO eh workshop.

## PRIMEIRO PASSO: /cex

Execute o protocolo `/cex` definido em `.claude/CEX_COMMAND.md`:
1. SCAN o repo (builders, nucleos, fill rate)
2. REPORT dashboard pro usuario
3. Aponte DOCS de referencia
4. ASK o que o usuario quer fazer

## DOCS CHAVE

| Doc | Path |
|-----|------|
| **Whitepaper** | `_docs/WHITEPAPER_CEX.md` |
| **Architecture (MOLDE)** | `_docs/ARCHITECTURE.md` |
| **CODEX** | `archetypes/CODEX.md` |
| **Comando /cex** | `.claude/CEX_COMMAND.md` |

## REGRAS

1. CEX = diamante. So produto final aqui. Reviews/plans vao pro codexa-core.
2. Artefatos = DUAL (.md + compiled/.yaml)
3. Density >= 0.8 | Quality >= 7.0
4. Path = endereco: `N{XX}/P{NN}/{type}/`
5. Builder constroi, humano revisa
6. Leia `_docs/ARCHITECTURE.md` antes de qualquer mudanca estrutural

## HIERARQUIA (5 niveis)

```
L0: archetypes/builders/     MOLDES (fabricas)
L1: P01..P12/                SCHEMAS ROOT (78 types)
L2: N01..N07/                NUCLEOS (7 setores)
L3: N{XX}/P{NN}/             LP POR NUCLEO (84)
L4: N{XX}/P{NN}/{type}/      INSTANCIAS (546 dirs)
```

## ENCODING

ASCII para configs. `nao` not `nao`. Excecao: conteudo user-facing.
