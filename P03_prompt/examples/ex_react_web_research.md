---
id: p03_react_web_research
kind: react
pillar: P03
title: ReAct Web Research Agent with Tool Loop
tools_available: [search_web, extract_data, calculate]
quality: 9.0
---

# ReAct: Web Market Research

## Objective
Pesquisar precos e disponibilidade de um produto em multiplas fontes online, consolidando dados de pelo menos 3 fontes concordantes antes de emitir relatorio final. O agente deve usar tools em loop Thought-Action-Observation ate atingir criterio de parada.

## Tools

### search_web
Busca na web por query textual. Retorna lista de resultados com titulo, URL e snippet.
```json
{
  "name": "search_web",
  "description": "Search the web for information matching a text query",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query in natural language"
      },
      "num_results": {
        "type": "integer",
        "default": 5,
        "minimum": 1,
        "maximum": 10,
        "description": "Number of results to return"
      },
      "region": {
        "type": "string",
        "default": "br",
        "description": "Region code for localized results"
      }
    },
    "required": ["query"]
  },
  "returns": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "title": {"type": "string"},
        "url": {"type": "string"},
        "snippet": {"type": "string"}
      }
    }
  }
}
```

### extract_data
Extrai dados estruturados de uma URL usando seletores ou schema.
```json
{
  "name": "extract_data",
  "description": "Extract structured data from a URL using a provided schema",
  "parameters": {
    "type": "object",
    "properties": {
      "url": {
        "type": "string",
        "description": "URL to extract data from"
      },
      "schema": {
        "type": "object",
        "description": "JSON Schema defining the expected output structure"
      },
      "timeout_ms": {
        "type": "integer",
        "default": 10000,
        "description": "Request timeout in milliseconds"
      }
    },
    "required": ["url", "schema"]
  },
  "returns": {
    "type": "object",
    "description": "Extracted data matching the provided schema"
  }
}
```

### calculate
Executa calculos matematicos sobre dados coletados.
```json
{
  "name": "calculate",
  "description": "Perform mathematical calculations on collected data",
  "parameters": {
    "type": "object",
    "properties": {
      "expression": {
        "type": "string",
        "description": "Mathematical expression to evaluate (e.g., 'avg(29.99, 32.50, 27.90)')"
      },
      "precision": {
        "type": "integer",
        "default": 2,
        "description": "Decimal places in result"
      }
    },
    "required": ["expression"]
  },
  "returns": {
    "type": "object",
    "properties": {
      "result": {"type": "number"},
      "expression": {"type": "string"}
    }
  }
}
```

## Loop Format

```text
Thought: [O que sei ate agora e o que preciso descobrir a seguir]
Action: [tool_name]({parameters})
Observation: [resultado retornado pela tool]

Thought: [Analisar resultado — suficiente? Preciso de mais dados?]
Action: [next_tool_name]({parameters})
Observation: [resultado]

... (repetir ate stop_condition)

Thought: [Tenho dados de 3+ fontes concordantes. Posso consolidar.]
Final Answer:
## Market Research: {{product_name}}

### Sources
| # | Source | Price | Availability | URL |
|---|--------|-------|-------------|-----|
| 1 | [name] | R$ XX | [status]    | [url] |

### Analysis
- Price range: R$ [min] - R$ [max]
- Average price: R$ [avg]
- Best deal: [source] at R$ [price]
- Concordance: [N]/[total] sources agree within 10%

### Recommendation
[1-2 frases com acao recomendada]
```

## Stop Condition
Parar quando tiver dados de **3 ou mais fontes concordantes** (precos dentro de 10% de variacao entre si) OU quando atingir max_iterations.

## Max Iterations
5

## Error Handling
- Se search_web retorna 0 resultados: reformular query (adicionar/remover termos)
- Se extract_data falha (timeout/blocked): pular URL, tentar proxima da lista
- Se apos 5 iteracoes nao ha 3 fontes: emitir relatorio parcial com disclaimer

## Research Base
- ReAct pattern: Thought-Action-Observation loop (Yao et al. 2023)
- Stop condition baseada em concordancia, nao em quantidade fixa
- JSON Schema completo por tool permite validacao automatica de chamadas
