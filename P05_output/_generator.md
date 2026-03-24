# Generator: P05 Output

## QUANDO USAR
- Definir formato de saida estruturado para agente/skill
- Criar parser para extrair dados de respostas LLM
- Padronizar formatacao (json, md, yaml) e naming rules

## TIPOS (escolher por necessidade)

| Tipo | Quando | Naming |
|------|--------|--------|
| output_schema | Definir campos obrigatorios da saida | p05_os_{{format}}.yaml |
| parser | Extrair dados de texto nao-estruturado | p05_parser_{{target}}.md + .yaml |
| formatter | Converter entre formatos (json>md, yaml>table) | p05_fmt_{{format}}.md |
| naming_rule | Padronizar nomes de arquivos/artefatos | p05_nr_{{scope}}.md |

## PASSO A PASSO
1. SCOUT: verificar se output similar ja existe (grep P05)
2. CLASSIFICAR tipo: schema, parser, formatter ou naming_rule
3. DEFINIR campos obrigatorios (tabela: field | type | required | example)
4. ESPECIFICAR formato de saida (JSON Schema, YAML template, ou regex)
5. INCLUIR exemplo concreto de output valido (min 1, ideal 2)
6. INCLUIR exemplo de output INVALIDO (mostra o que rejeitar)
7. DEFINIR error handling (o que retornar quando input eh malformado)
8. TESTAR contra 3+ inputs reais (nao hipoteticos)
9. VALIDAR contra P05/_schema.yaml (max_bytes constraint)
10. SALVAR dual output (.md + .yaml)

## ANTI-PATTERNS
- Schema sem examples (ninguem sabe o formato esperado)
- Parser com regex fragil (quebra em edge cases)
- Formatter sem fallback (crash quando input inesperado)
- Naming rule ambigua ("use descriptive names" vs "{{SAT}}_{{TYPE}}_{{NNN}}")
- Output schema sem max_bytes (saidas infinitas)

## QUALITY TIERS
- Elite (90-95%): Schema com JSON Schema + 3 examples + error handling
- High (80-88%): Schema com tabela de campos + 1 example
- Standard (70-78%): Formato descrito em prosa estruturada
- Low (<65%): REJEITAR — output sem estrutura clara

## Dual Output

Cada artefato Output tem duas versoes:

| Versao | Formato | Leitor | Onde |
|--------|---------|--------|------|
| Humana | .md com frontmatter | Desenvolvedores, revisores | `examples/` e `templates/` |
| Machine | .yaml otimizado | LLMs, pipelines, validators | `compiled/` |

### Como compilar
```bash
python _tools/cex_compile.py P05_output/examples/p05_output_exemplo.md
# -> gera P05_output/compiled/p05_output_exemplo.yaml
```

### O que muda no compilado
- Remove: headers decorativos, bold/italic, links, navegacao
- Mantem: identidade, regras, dados estruturados, exemplos
- Formato: YAML (definido em _schema.yaml → machine_format)

---
*Generator v1.0 | Evidence: 4 output types, P01-P04 patterns | 2026-03-22*
