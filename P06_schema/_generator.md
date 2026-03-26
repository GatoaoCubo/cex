# Generator: P06 Schema

## QUANDO USAR
- Criar contrato de validacao (input/output entre agentes)
- Definir tipos customizados reutilizaveis
- Estabelecer interface de integracao entre componentes

## TIPOS (escolher por necessidade)

| Tipo | Quando | Naming |
|------|--------|--------|
| input_schema | Validar entrada de agente/skill | p06_is_{{scope}}.yaml |
| type_def | Definir tipo customizado (enum, struct) | p06_td_{{type}}.yaml |
| validator | Regra de validacao (pre-commit, quality gate) | p06_val_{{rule}}.yaml |
| interface | Contrato entre 2+ agentes (upstream/downstream) | p06_iface_{{contract}}.yaml |
| output_schema | Contrato de saida (complementa P05) | p06_os_{{scope}}.yaml |

## PASSO A PASSO
1. SCOUT: verificar se schema similar ja existe (grep P06)
2. CLASSIFICAR tipo: input, type_def, validator, interface ou output
3. MAPEAR campos (tabela: field | type | required | constraints | default)
4. DEFINIR validators (regras que rejeitam input invalido)
5. ESPECIFICAR error messages (claras, actionable, com exemplo do esperado)
6. CRIAR interface contract (se conecta 2+ agentes: quem envia, quem recebe)
7. INCLUIR exemplo valido + exemplo invalido (ambos concretos)
8. TESTAR compatibilidade com schemas adjacentes (P05 output, P03 prompt vars)
9. VALIDAR contra P06/_schema.yaml (max_bytes constraint)
10. SALVAR como .yaml (schemas sao YAML-first, .md opcional para docs)

## ANTI-PATTERNS
- Schema sem constraints (aceita qualquer coisa)
- Validator sem error message (falha silenciosa)
- Interface sem versao (breaking changes invisíveis)
- Type_def duplicando tipo builtin (string, int, bool)
- Required fields sem default (bloqueia execucao)

## QUALITY TIERS
- Elite (90-95%): JSON Schema completo + validators + interface tests
- High (80-88%): Tabela de campos + constraints + 1 example
- Standard (70-78%): Lista de campos com tipos basicos
- Low (<65%): REJEITAR — schema sem validacao nao eh schema

## Dual Output

Cada artefato Schema tem duas versoes:

| Versao | Formato | Leitor | Onde |
|--------|---------|--------|------|
| Humana | .md com frontmatter | Desenvolvedores, revisores | `examples/` e `templates/` |
| Machine | .yaml ou .json (depende do tipo) | LLMs, pipelines, validators | `compiled/` |

### Como compilar
```bash
python _tools/cex_compile.py P06_schema/examples/p06_schema_exemplo.md
# -> gera P06_schema/compiled/p06_schema_exemplo.yaml
```

### O que muda no compilado
- Remove: headers decorativos, bold/italic, links, navegacao
- Mantem: identidade, regras, dados estruturados, exemplos
- Formato: YAML (type_def) / JSON (input_schema, interface, output_schema) (definido em _schema.yaml → machine_format)

---
*Generator v1.0 | Evidence: 5 schema kinds, contract-driven design | 2026-03-22*
