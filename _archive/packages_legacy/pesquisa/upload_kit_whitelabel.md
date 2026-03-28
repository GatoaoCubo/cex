# UPLOAD KIT WHITE-LABEL | pesquisa_agent v4.0.0

**Package**: White-Label Ready | **Version**: 4.0.0 | **Date**: 2025-12-20
**Deploy Time**: 30 minutos | **Dificuldade**: Facil

---

## PARA QUEM E ESTE KIT

Agencias de marketing que querem oferecer AI de inteligencia de mercado para e-commerce como servico proprio (white-label).

**Resultado Final**: Seu cliente vera "ResearchPro da Agencia XYZ", NAO "ChatGPT" ou "CODEXA".

---

## ARQUITETURA WHITE-LABEL

```
+====================================================================+
|                    ANTES vs DEPOIS                                  |
+====================================================================+
|                                                                    |
|  ANTES (Generico):                                                 |
|  +-----------------+     +-----------------+                      |
|  |    Cliente      | --> |    ChatGPT      |                      |
|  +-----------------+     +-----------------+                      |
|         |                                                         |
|         v                                                         |
|  "AI generica, pesquisa manual"                                   |
|                                                                   |
+-------------------------------------------------------------------+
|                                                                   |
|  DEPOIS (White-Label):                                            |
|  +-----------------+     +------------------------+              |
|  |    Cliente      | --> | {{AGENT_NAME}}         |              |
|  +-----------------+     | by {{AGENCY_NAME}}     |              |
|         |                +------------------------+              |
|         v                                                         |
|  "Inteligencia de mercado exclusiva da minha agencia"             |
|                                                                   |
+====================================================================+
```

---

## CHECKLIST DE DEPLOY (30 minutos)

### Etapa 1: Definir Branding (5 min)

Preencha os placeholders:

```yaml
AGENCY_NAME: "_______________"      # Ex: "Agencia XYZ"
AGENCY_URL: "_______________"       # Ex: "www.agenciaxyz.com.br"
PRIMARY_COLOR: "#_______________"   # Ex: "#0D9488" (teal)
SECONDARY_COLOR: "#_______________" # Ex: "#14B8A6"
SUPPORT_EMAIL: "_______________"    # Ex: "research@agenciaxyz.com.br"
AGENT_NAME: "_______________"       # Ex: "ResearchPro", "MarketAI", "PesquisaMax"
```

### Etapa 2: Customizar System Instruction (10 min)

1. Abra `system_instruction_whitelabel.md`
2. Buscar e Substituir (Ctrl+H):
   - `{{AGENCY_NAME}}` -> seu nome de agencia
   - `{{AGENCY_URL}}` -> sua URL
   - `{{PRIMARY_COLOR}}` -> sua cor primaria
   - `{{SECONDARY_COLOR}}` -> sua cor secundaria
   - `{{SUPPORT_EMAIL}}` -> seu email de suporte
   - `{{AGENT_NAME}}` -> nome do seu agente
3. Salvar como `SYSTEM_INSTRUCTION_[SUA_AGENCIA].md`

### Etapa 3: Upload para Plataforma (10 min)

#### OpenAI Assistants

```yaml
1. Acessar: platform.openai.com/assistants
2. Criar novo Assistant
3. Nome: {{AGENT_NAME}}
4. Instructions: [COLAR conteudo customizado]
5. Model: gpt-4o ou gpt-4.1
6. Tools: Web Search (ON) + File Search (ON)
7. Vector Store: Criar e fazer upload dos arquivos do pacote
```

#### Claude Projects

```yaml
1. Acessar: claude.ai/projects
2. Criar novo Project
3. Nome: {{AGENT_NAME}}
4. Custom Instructions: [COLAR conteudo customizado]
5. Upload Knowledge: arquivos do pacote
6. Nota: Claude requer web search externo (MCP ou tool)
```

#### ChatKit / Custom

```yaml
1. System Prompt: [COLAR conteudo customizado]
2. Vector Store: Upload arquivos do pacote
3. Chunking: 800 tokens, 200 overlap (otimizado)
4. Temperature: 0.7
5. Tools: Web Search (ON) + File Search (ON)
```

### Etapa 4: Testar (5 min)

Envie este prompt de teste:

```
Faca uma pesquisa completa sobre:
Produto: Fone Bluetooth TWS
Categoria: Eletronicos > Audio
Objetivo: Entrar no Mercado Livre com preco competitivo
```

**Verificar**:
- [ ] Output e JSON monobloco com 2 campos (productName, report)
- [ ] 15 head terms identificados
- [ ] 30+ longtail queries geradas
- [ ] Minimo 3 marketplaces pesquisados (ideal 9)
- [ ] Top 5 concorrentes analisados
- [ ] Compliance (INMETRO/ANVISA) verificado
- [ ] URLs pesquisadas listadas (minimo 10)
- [ ] Confidence score no final (>= 0.60)
- [ ] Footer menciona {{AGENCY_NAME}}
- [ ] ZERO emojis em todo o output
- [ ] Sem mencao a "CODEXA", "ChatGPT" ou "Claude"

---

## PERSONALIZACAO AVANCADA

### Adicionar Logo

```html
<!-- Header customizado -->
<div class="agent-header">
  <img src="{{AGENCY_LOGO_URL}}" alt="{{AGENCY_NAME}}" />
  <h1>{{AGENT_NAME}}</h1>
  <p>Inteligencia de mercado para e-commerce brasileiro</p>
</div>
```

### Adicionar Cores da Marca

```css
:root {
  --primary: {{PRIMARY_COLOR}};
  --secondary: {{SECONDARY_COLOR}};
}

.research-output {
  border-left: 4px solid var(--primary);
}
```

---

## PRECOS SUGERIDOS PARA REVENDA

```
+--------------------------------------------------------------------+
|  Modelo de Precificacao Sugerido                                    |
+--------------------------------------------------------------------+
|                                                                    |
|  SERVICO              PRECO SUGERIDO    MARGEM                     |
|  ----------------     ---------------   ------                     |
|  Pesquisa Avulsa      R$ 397-597/un      Alta                      |
|  Pacote 5 pesquisas   R$ 1.497           Alta                      |
|  Retainer Mensal      R$ 3.497/mes       Alta                      |
|  (10 pesquisas/mes)                                                |
|                                                                    |
+--------------------------------------------------------------------+
```

### Sugestoes de Pacotes

**Pacote Bronze** (R$ 1.497/mes):
- 5 pesquisas completas/mes
- 9 marketplaces analisados
- Top 5 concorrentes por pesquisa
- Suporte email

**Pacote Prata** (R$ 2.997/mes):
- 15 pesquisas completas/mes
- Integracao com anuncio_agent
- Analise de tendencias Google Trends
- Suporte prioritario

**Pacote Ouro** (R$ 5.997/mes):
- Pesquisas ilimitadas
- Suite completa (pesquisa + anuncio + photo + ads)
- Monitoramento de concorrentes (semanal)
- Suporte dedicado (WhatsApp)

---

## CASOS DE USO

### 1. Lancamento de Novo Produto
**Problema**: Nao sabe se produto e viavel no mercado BR
**Solucao**: {{AGENT_NAME}} analisa 9 marketplaces em 5 minutos
**ROI**: Evita investimento em produto sem demanda

### 2. Agencia com Portfolio E-commerce
**Problema**: Pesquisa manual leva 4-8h por produto
**Solucao**: {{AGENT_NAME}} gera relatorio em 5 minutos
**ROI**: 95% reducao de tempo, 48x mais rapido

### 3. Consultor de Precificacao
**Problema**: Precificar sem dados de mercado
**Solucao**: {{AGENT_NAME}} mostra precos de 5+ concorrentes
**ROI**: Precificacao otimizada, +15-30% margem

### 4. Due Diligence de Fornecedor
**Problema**: Validar marca/fabricante antes de comprar
**Solucao**: {{AGENT_NAME}} consulta CNPJ, Reclame Aqui, redes
**ROI**: Evita golpes e fornecedores problematicos

---

## INTEGRACAO COM OUTROS AGENTES (Upsell)

### Suite Completa E-commerce

```
+---------------------------------------------------------------+
|  PIPELINE COMPLETO (4 agentes white-label)                     |
+---------------------------------------------------------------+
|                                                               |
|  1. PESQUISA -> pesquisa_agent (ESTE)                         |
|     Input: nome do produto                                    |
|     Output: analise de mercado, concorrentes, keywords        |
|                                                               |
|  2. MARCA -> marca_agent                                      |
|     Input: research_notes.md                                  |
|     Output: 32-blocos de estrategia de marca                  |
|                                                               |
|  3. ANUNCIO -> anuncio_agent                                  |
|     Input: research + brand                                   |
|     Output: titulos, keywords, bullets, descricao             |
|                                                               |
|  4. PHOTO -> photo_agent                                      |
|     Input: anuncio_completo.md                                |
|     Output: 9 prompts Midjourney/DALL-E                       |
|                                                               |
+---------------------------------------------------------------+
```

---

## TROUBLESHOOTING

| Problema | Causa | Solucao |
|----------|-------|---------|
| "CODEXA" aparece no output | Placeholder nao substituido | Buscar/substituir no system_instruction_whitelabel.md |
| Output nao e JSON | LLM ignorando formato | Adicionar enfase: "OBRIGATORIO: JSON monobloco" |
| Poucos marketplaces | Web search limitado | Verificar se tool web_search esta habilitado |
| Concorrentes faltando | Busca incompleta | Instruir: "Minimo 5 concorrentes OBRIGATORIO" |
| Confidence < 0.60 | Dados insuficientes | Verificar se web_search esta funcionando |

---

## QUALITY ASSURANCE

### Checklist Pre-Deploy

- [ ] Todos os 6 placeholders substituidos
- [ ] system_instruction_whitelabel.md sem mencao a "CODEXA"
- [ ] Todos os arquivos do pacote uploadados
- [ ] Chunking: 800 tokens, 200 overlap
- [ ] Tools: Web Search + File Search habilitados

### Checklist Pos-Deploy

- [ ] Teste com produto de cada categoria:
  - [ ] Eletronicos (INMETRO obrigatorio)
  - [ ] Beleza/Saude (ANVISA obrigatorio)
  - [ ] Moda (sem compliance especifico)
  - [ ] Alimentos (ANVISA obrigatorio)
- [ ] Validar output JSON (2 campos: productName, report)
- [ ] Verificar footer menciona {{AGENCY_NAME}}
- [ ] Verificar >= 10 URLs pesquisadas

---

## METRICAS DE SUCESSO

| Metrica | Baseline (manual) | Target ({{AGENT_NAME}}) | Melhoria |
|---------|-------------------|-------------------------|----------|
| Tempo por pesquisa | 4-8 horas | 5 minutos | 48-96x |
| Marketplaces cobertos | 2-3 | 9 | 3-4.5x |
| Concorrentes analisados | 3 | 5+ | 67%+ |
| Keywords descobertas | 10-20 | 45+ | 2-4x |
| Precisao compliance | 60% | 95% | +58% |

---

**Upload Kit White-Label v4.0.0**
**Status**: DEPLOY READY
**Quality Score**: 8.7/10
**Tempo de Deploy**: 30 minutos
