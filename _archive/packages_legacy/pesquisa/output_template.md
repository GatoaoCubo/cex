# OUTPUT TEMPLATE v4.0 | MONOBLOCO (2 CAMPOS)

## FORMAT RULE

```
OUTPUT = 1 bloco JSON com 2 campos:
       - productName: string
       - report: string (markdown)

A resposta final deve ser SOMENTE o bloco JSON.
NAO inclua texto antes ou depois.
```

---

## JSON STRUCTURE (2 CAMPOS)

```json
{
  "productName": "Nome do Produto/Marca",
  "report": "## Resumo Executivo\n\n[conteudo]\n\n## Brief\n\n[conteudo]\n\n..."
}
```

---

## TEMPLATE DO CAMPO `report`

O campo `report` deve conter este markdown:

```markdown
## Resumo Executivo

[2-3 paragrafos sobre o produto/marca, tracao, reputacao]

## Brief Validado

- **Categoria**: [Categoria > Subcategoria]
- **Publico**: [Perfil demografico]
- **Preco**: [Faixa em BRL]

## Head Terms (15)

1. termo1
2. termo2
[...ate 15]

## Longtails (30+)

- "query longtail 1"
- "query longtail 2"
[...ate 30+]

## Inbound (Marketplaces)

| Source | URL | Preco | Rating |
|--------|-----|-------|--------|
| ML | [url] | R$ X | X.X |
| Amazon | [url] | R$ X | X.X |
| Shopee | [url] | R$ X | X.X |

## Outbound (SERP/Social)

- **LinkedIn**: [seguidores, posts]
- **YouTube**: [inscritos, videos]
- **Google SERP**: [top results]

## Registro Juridico

- **CNPJ**: XX.XXX.XXX/XXXX-XX
- **Razao Social**: [nome]
- **Situacao**: [Ativa/Inativa]
- **Socios**: [nomes]

## Portfolio

[Lista de produtos/servicos oferecidos]

## Precificacao

| Tier | Preco | Descricao |
|------|-------|-----------|
| Entry | R$ XX | [desc] |
| Mid | R$ XXX | [desc] |
| High | R$ X.XXX | [desc] |

## Tracao Social

- **LinkedIn**: X.XXX seguidores
- **Instagram**: X.XXX seguidores
- **YouTube**: X.XXX inscritos
- **Newsletter**: X.XXX assinantes

## Reclame Aqui

- **Reputacao**: [Otima/Boa/Regular/Ruim]
- **Nota**: X.X/10
- **% Respondidas**: XX%
- **% Resolvidas**: XX%
- **Top Queixas**: [lista]

## Top 5 Concorrentes

### 1. [Nome Concorrente]
- **Preco**: R$ X.XXX
- **Rating**: X.X/5.0
- **Forca**: [diferencial principal]
- **Fraqueza**: [ponto fraco]
- **URL**: [link]

### 2. [Nome Concorrente]
[mesmo formato]

### 3. [Nome Concorrente]
[mesmo formato]

### 4. [Nome Concorrente]
[mesmo formato]

### 5. [Nome Concorrente]
[mesmo formato]

## Gaps & Oportunidades

### Gaps Identificados
- Gap 1: [descricao]
- Gap 2: [descricao]
- Gap 3: [descricao]

### Acoes Recomendadas
1. [Acao prioritaria]
2. [Acao secundaria]
3. [Acao terciaria]

## Compliance

- **ANVISA**: [Aplicavel? Requisitos?]
- **INMETRO**: [Aplicavel? Requisitos?]
- **CONAR**: [Claims a evitar/permitir]
- **CDC**: [Art.49, garantias]
- **LGPD**: [Coleta dados, base legal]

## URLs Pesquisadas

1. [url1]
2. [url2]
[...minimo 10 URLs]

---

**CONFIDENCE**: X.XX/1.00
- Fontes: X
- Queries: X
- Concorrentes: X
- Limitacoes: [se houver]
```

---

## EXEMPLO COMPLETO

```json
{
  "productName": "Viver de IA",
  "report": "## Resumo Executivo\n\nMarca brasileira de educacao e solucoes em IA aplicada a negocios. Escada de valor de R$17 a R$72.000.\n\n## Brief Validado\n\n- **Categoria**: Educacao > Cursos Online > IA para Negocios\n- **Publico**: Empresarios e empreendedores 25-50 anos\n- **Preco**: R$ 597 - R$ 72.000\n\n## Head Terms (15)\n\n1. viver de ia\n2. curso de ia para negocios\n...\n\n## Top 5 Concorrentes\n\n### 1. G4 Educacao - G4 AI Academy\n- **Preco**: R$ 2.997/ano\n- **Rating**: N/D\n- **Forca**: Marca forte, networking\n- **Fraqueza**: Programa intensivo 1 dia\n\n---\n\n**CONFIDENCE**: 0.78/1.00"
}
```

---

## SCHEMA (2 CAMPOS - STRINGS)

| Campo | Tipo | Descricao |
|-------|------|-----------|
| productName | string | Nome do produto/marca pesquisado |
| report | string | Markdown completo com toda a pesquisa |

---

## CORRETO vs ERRADO

### JSON deve ter SOMENTE 2 campos:
```
CORRETO:
{ "productName": "X", "report": "## Resumo\n\n..." }

ERRADO:
{ "productName": "X", "resumo": "X", "categoria": "X", ...mais campos }
```

### report deve ser STRING (nao objeto):
```
CORRETO: "report": "## Resumo\n\nTexto aqui"
ERRADO:  "report": {"resumo": "X", "categoria": "Y"}
```

### Newlines devem ser escapadas:
```
CORRETO: "report": "## Titulo\n\nParagrafo 1\n\nParagrafo 2"
ERRADO:  "report": "## Titulo
                    Paragrafo 1"
```

---

## LIMPAR CITACOES (OBRIGATORIO)

ANTES de gerar output, remover do texto:
- `citeturn*` (ex: citeturn2view0turn19search1)
- `:OaiMdDirective_Annotations`
- `[source0]`, `[source1]`
- Qualquer marcador interno do sistema

O output deve ser TEXTO LIMPO, sem referencias internas.

---

**v4.0** | Monobloco | 2-Field Schema | Citation Stripping | Single Code Block
