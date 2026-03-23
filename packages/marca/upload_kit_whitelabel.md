# UPLOAD KIT WHITE-LABEL | marca_agent v2.0.0

**Package**: White-Label Ready | **Version**: 2.0.0 | **Date**: 2025-12-20
**Deploy Time**: 30 minutos | **Dificuldade**: Facil

---

## PARA QUEM E ESTE KIT

Agencias de marketing que querem oferecer AI de estrategia de marca como servico proprio (white-label).

**Resultado Final**: Seu cliente vera "BrandGenie da Agencia XYZ", NAO "ChatGPT" ou "CODEXA".

---

## ARQUITETURA WHITE-LABEL

```
+====================================================================+
|                    ANTES vs DEPOIS                                  |
+====================================================================+
|                                                                    |
|  ANTES (Generico):                                                  |
|  +-----------------+     +-----------------+                       |
|  |    Cliente      | --> |    ChatGPT      |                       |
|  +-----------------+     +-----------------+                       |
|         |                                                          |
|         v                                                          |
|  "AI generica, qualquer um pode usar"                              |
|                                                                    |
+--------------------------------------------------------------------+
|                                                                    |
|  DEPOIS (White-Label):                                              |
|  +-----------------+     +------------------------+                |
|  |    Cliente      | --> | {{AGENT_NAME}}         |                |
|  +-----------------+     | by {{AGENCY_NAME}}     |                |
|         |                +------------------------+                |
|         v                                                          |
|  "AI exclusiva da minha agencia"                                   |
|                                                                    |
+====================================================================+
```

---

## CHECKLIST DE DEPLOY (30 minutos)

### Etapa 1: Definir Branding (5 min)

Preencha os placeholders:

```yaml
# Copie e preencha:
AGENCY_NAME: "_______________"      # Ex: "Agencia XYZ"
AGENCY_URL: "_______________"       # Ex: "www.agenciaxyz.com.br"
PRIMARY_COLOR: "#_______________"   # Ex: "#0D9488" (teal)
SECONDARY_COLOR: "#_______________" # Ex: "#14B8A6"
SUPPORT_EMAIL: "_______________"    # Ex: "ai@agenciaxyz.com.br"
AGENT_NAME: "_______________"       # Ex: "BrandGenie", "MarcaAI", "StrategyBot"
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
6. Tools: File Search (ON)
7. Vector Store: Criar e fazer upload dos 7 arquivos
```

#### Claude Projects

```yaml
1. Acessar: claude.ai/projects
2. Criar novo Project
3. Nome: {{AGENT_NAME}}
4. Custom Instructions: [COLAR conteudo customizado]
5. Upload Knowledge: 7 arquivos
```

#### ChatKit / Custom

```yaml
1. System Prompt: [COLAR conteudo customizado]
2. Vector Store: Upload 7 arquivos
3. Chunking: 800 tokens, 200 overlap
4. Temperature: 0.7
```

### Etapa 4: Testar (5 min)

Envie este prompt de teste:

```
Crie uma estrategia de marca para:
Produto: Garrafa Termica Premium
Categoria: Casa > Utensilios
Publico: Profissionais urbanos 25-45
Preco: Premium (R$ 150-300)
```

**Verificar**:
- [ ] Output menciona {{AGENCY_NAME}} no footer
- [ ] 32 blocos gerados
- [ ] Sem mencao a "CODEXA", "ChatGPT" ou "Claude"
- [ ] Taglines com 40-60 caracteres
- [ ] Scores de validacao presentes

---

## ARQUIVOS PARA UPLOAD (7 files)

### Knowledge Base (Fazer upload)

| # | Arquivo | Tokens | Descricao |
|---|---------|--------|-----------|
| 1 | `quick_start.md` | ~700 | Guia rapido de uso |
| 2 | `prime.md` | ~800 | Identidade do agente |
| 3 | `instructions.md` | ~1500 | Workflow de 8 etapas |
| 4 | `data/input_schema.yaml` | ~700 | Validacao de inputs |
| 5 | `output_template.md` | ~2700 | Formato 32 blocos |
| 6 | `data/brand_archetypes.yaml` | ~3500 | 12 arquetipos + combinacoes |
| 7 | `data/quality_dimensions.yaml` | ~1400 | Framework 5D de qualidade |

**Total**: ~11,300 tokens no knowledge base

### System Instruction (NAO fazer upload - COLAR)

| Arquivo | Uso |
|---------|-----|
| `system_instruction_whitelabel.md` | Campo "Instructions" da plataforma |

---

## PERSONALIZACAO AVANCADA

### Adicionar Logo

Para ChatKit ou plataformas com UI customizada:

```html
<!-- Header customizado -->
<div class="agent-header">
  <img src="{{AGENCY_LOGO_URL}}" alt="{{AGENCY_NAME}}" />
  <h1>{{AGENT_NAME}}</h1>
  <p>Seu assistente de estrategia de marca</p>
</div>
```

### Adicionar Cores da Marca

```css
/* Cores customizadas */
:root {
  --primary: {{PRIMARY_COLOR}};
  --secondary: {{SECONDARY_COLOR}};
  --accent: {{ACCENT_COLOR}};
}
```

---

## PRECOS SUGERIDOS PARA REVENDA

```
+--------------------------------------------------------------------+
|  Modelo de Precificacao Sugerido                                    |
+--------------------------------------------------------------------+
|                                                                    |
|  PLANO AGENCIA     CUSTO BASE      PRECO SUGERIDO    MARGEM        |
|  --------------    ------------    ---------------    ------        |
|  Starter           R$ 297/mes      R$ 997/cliente     70%          |
|  Professional      R$ 697/mes      R$ 2.497/cliente   72%          |
|  Enterprise        R$ 1.497/mes    R$ 4.997/cliente   70%          |
|                                                                    |
|  MODELO POR USO:                                                    |
|  - Estrategia completa (32 blocos): R$ 297-497/unidade             |
|  - Secao individual (5 blocos): R$ 97/unidade                      |
|  - Retainer mensal ilimitado: R$ 1.997-4.997/mes                   |
|                                                                    |
+--------------------------------------------------------------------+
```

---

## TROUBLESHOOTING

| Problema | Causa | Solucao |
|----------|-------|---------|
| Placeholder aparece no output | Placeholder nao substituido | Buscar/substituir novamente |
| Output incompleto | Vector store sem indexar | Aguardar 2-3 minutos |
| Erro de formato | system_instruction mal colado | Copiar novamente todo o arquivo |
| Taglines fora do range | LLM ignorando restricao | Adicionar enfase no system_instruction |

---

## PROXIMOS PASSOS

1. [ ] Completar deploy do marca_agent (este kit)
2. [ ] Solicitar acesso aos outros agentes
3. [ ] Configurar dashboard white-label (ChatKit Pro)
4. [ ] Treinar equipe de vendas
5. [ ] Criar landing page para seu servico de AI

---

**Upload Kit White-Label v2.0.0**
**Status**: DEPLOY READY
**Quality Score**: 8.7/10
**Tempo de Deploy**: 30 minutos
