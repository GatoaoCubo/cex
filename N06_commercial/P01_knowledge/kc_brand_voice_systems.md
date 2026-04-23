---
id: p01_kc_brand_voice_systems
kind: knowledge_card
pillar: P01
title: "Brand Voice Systems — Frameworks Universais para Voz e Tom de Marca"
version: 1.0.0
created: 2026-04-01
author: shaka_research
domain: brand-identity
quality: 9.2
updated: 2026-04-07
tags: [brand, voice, tone, brand-voice, nngroup, content-design, governance, messaging]
tldr: "Frameworks universais para sistemas de voz de marca: NNGroup 4D model, distincao voice/tone, matriz de canais, atributos, Do/Don't, governanca e scoring."
when_to_use: "When calibrating brand voice dimensions, building tone matrix per channel, or writing voice governance guidelines."
keywords: [brand-voice, tone-matrix, nngroup-4d, voice-governance, channel-calibration]
density_score: 0.94
axioms:
  - "Voice is WHO you are (constant). Tone is HOW you adjust (contextual). Never confuse them."
  - "ALWAYS include Do/Don't examples — guidelines without examples get ignored."
  - "NEVER calibrate voice without testing on 3+ channels — what works on social may fail in support."
linked_artifacts:
  primary: n06_output_brand_voice_guide
  related: [p01_kc_brand_archetypes, n06_schema_brand_voice_contract, p03_sp_commercial_nucleus]
related:
  - p01_kc_brand_book_patterns
  - ex_feedback_tone_correction
  - p01_kc_brand_frameworks
  - p01_kc_brand_archetypes
  - p01_kc_brand_voice_consistency_channels
  - brand_voice_templates
---

# Brand Voice Systems — Frameworks Universais

## 1. Distincao Fundamental: Voice vs Tone

| | Voice | Tone |
|--|-------|------|
| **O que e** | Personalidade da marca | Expressao contextual da personalidade |
| **Consistencia** | Constante — nao muda | Varia por contexto, canal e estado emocional do usuario |
| **Analogia** | Como voce fala com qualquer pessoa | Como voce ajusta dependendo de quem, quando e onde |
| **Exemplo** | Marca e "encorajadora e direta" (sempre) | Tom mais formal em termos legais; mais descontraido em social media |

> "You have the same voice all the time, but your tone changes. You might use one tone when out to dinner with your closest friends, and a different tone in a meeting with your boss." — Mailchimp Style Guide

**Regra pratica**: Se um atributo de voz muda dependendo do canal, e tom, nao voz.

---

## 2. NNGroup 4 Dimensoes de Tom de Voz

Modelo de Kate Moran (NNg, 2016, atualizado 2023). Cada dimensao e um espectro — nao binario.

### As 4 Dimensoes

| # | Dimensao | Polo A | Polo B |
|---|---------|--------|--------|
| 1 | Formalidade | Formal | Casual |
| 2 | Seriedade | Serio | Divertido / Humoristico |
| 3 | Respeito | Respeitoso | Irreverente |
| 4 | Entusiasmo | Factual / Matter-of-fact | Entusiastico |

**Escala de medicao**: cada dimensao usa escala Likert de 3 a 5 pontos para teste com usuarios.

### Perfil de Tom (como posicionar a marca)

O perfil da marca e sua posicao nas 4 dimensoes simultaneamente — expressado como ponto em espaco quadridimensional.

```
EXEMPLO: Marca fintech moderna
  Formalidade:   [===o=] Casual (4/5)
  Seriedade:     [==o==] Neutro (3/5)
  Respeito:      [o====] Respeitoso (1/5)
  Entusiasmo:    [====o] Entusiastico (5/5)
```

### Como o Tom Muda por Situacao

**Um erro, quatro tons** (NNg canonical example):

| Perfil | Copy |
|--------|------|
| Formal + serio + respeitoso + factual | *"We apologize, but we are experiencing a problem."* |
| + Casual | *"We're sorry, but we're experiencing a problem on our end."* |
| + Entusiastico | *"Oops! We're sorry, but we're experiencing a problem on our end."* |
| + Divertido + irreverente | *"What did you do!? You broke it! (Just kidding. We're experiencing a problem on our end.)"* |

### Insight Critico de Pesquisa (NNg)

**Trustworthiness explica 52% do willingness-to-recommend. Friendliness adiciona apenas 8% em cima disso.**

Implicacoes:
- Tom playful em industrias serias (seguros) **aumentou** friendliness mas **diminuiu** trustworthiness
- Linguagem conversacional em industrias "secas" (banking) melhorou **ambos** friendliness E trustworthiness
- Conclusao: ajuste o tom ao contexto da industria, nao apenas a preferencia da marca

---

## 3. Sistema de 5 Dimensoes Estendido (Brunasena 5D)

Para marcas que precisam de granularidade adicional alem do modelo NNg:

| # | Dimensao | Escala 1-5 | Descricao |
|---|---------|-----------|-----------|
| 1 | Formalidade | 1 (muito formal) — 5 (muito casual) | Nivel de linguagem e protocolos |
| 2 | Seriedade | 1 (serio/grave) — 5 (humoristico) | Presenca de leveza e humor |
| 3 | Proximidade | 1 (distante/institucional) — 5 (intimo/quente) | Calor e relacionamento |
| 4 | Autoridade | 1 (humilde/aprendiz) — 5 (especialista/lider) | Nivel de expertise projetado |
| 5 | Intensidade | 1 (factual/neutro) — 5 (muito entusiastico) | Energia emocional |

**Template de perfil**:
```yaml
voice_profile:
  formalidade: 4      # casual, nao coloquial
  seriedade: 3        # leveza moderada, humor contextual
  proximidade: 4      # quente, acessivel
  autoridade: 4       # especialista sem arrogancia
  intensidade: 3      # energetico mas nao excessivo
```

---

## 4. Framework de Atributos de Voz: "We are X, not Y"

Pattern universal para definir voz com precisao. Cada atributo precisa de seu anti-atributo.

### Estrutura

```
Atributo: [PALAVRA POSITIVA]
Nao: [DISTORCAO NEGATIVA DO ATRIBUTO]
O que isso significa: [DESCRICAO 1-2 frases]
Exemplo: [FRASE QUE DEMONSTRA]
```

### Exemplo Completo (marca de tecnologia B2B)

| Somos | Nao somos | Significado |
|-------|-----------|-------------|
| **Claros** | Simples demais | Eliminamos jargao mas nao subestimamos a inteligencia do cliente |
| **Confiaveis** | Rigidos | Prometemos apenas o que entregamos, com dados que suportam cada afirmacao |
| **Humanos** | Informais demais | Escrevemos como pessoas, nao como corporacao — mas mantemos profissionalismo |
| **Diretos** | Bruscos | Vamos ao ponto sem rodeios, mas sempre com contexto suficiente |
| **Entusiasticos** | Exagerados | Genuinamente empolgados, mas sem hiperboles ou superlativos vazios |

### Anti-Patterns Comuns (o que evitar definir como atributo)

| Nao use | Por que | Use em vez |
|---------|---------|------------|
| "Inovador" | Toda empresa diz isso | "Direto ao experimentar" |
| "Apaixonado" | Cliche sem substancia | "Empenhado em [resultado especifico]" |
| "Autentico" | Vago e autodeclarado | "Transparente sobre limitacoes" |
| "De classe mundial" | Inutil sem evidencia | "Testado por X clientes em Y paises" |

---

## 5. Matriz de Tom por Canal

Como a VOZ (consistente) se expressa com TONS diferentes por canal:

| Canal | Tom | Formalidade | Humor | Comprimento | Prioridade |
|-------|-----|-------------|-------|-------------|------------|
| **Twitter/X** | Agudo, wit, rapido | 4/5 casual | Sim (se natural) | <280 chars | Relevancia + timing |
| **LinkedIn** | Substancial, profissional | 2/5 formal | Raro | 150-300 palavras | Credibilidade |
| **Instagram** | Aspiracional, visual-first | 4/5 casual | Sim | 1-3 frases | Emocao + estetica |
| **TikTok** | Conversacional, autentico | 5/5 casual | Essencial | Hook em 3s | Entretenimento |
| **Email marketing** | Pessoal, acionavel | 3/5 neutro | Contextual | 50-150 palavras | Abertura + clique |
| **Suporte** | Empatico, resolutivo | 3/5 neutro | Nunca | Claro e breve | Resolucao rapida |
| **Documentacao** | Preciso, neutro | 2/5 formal | Nao | Completo | Clareza tecnica |
| **Ads** | Urgente, beneficio-first | 3/5 neutro | Contextual | Headline < 6 palavras | Conversao |
| **Push notification** | Imperativo, direto | 4/5 casual | Nunca | < 30 chars | Abertura |

---

## 6. Modelos de Voice de Empresas World-Class

### 6A. Mailchimp Voice (4 Tracos)

| Traco | Definicao | Anti-padrao |
|-------|-----------|-------------|
| **Plainspoken** | Clareza acima de tudo; sem metaforas floreadas | Jargao de marketing, plays emocionais baratos |
| **Genuine** | Relaciona-se com desafios reais; quente e acessivel | Corporativo, frio, distante |
| **Translators** | Desmistifica B2B-speak; educa genuinamente | Simplificacao excessiva, condescendencia |
| **Dry humor** | Sutileza, estoico, um toque eccentrico; winking nao shouting | Humor forcado, piadas exclusivas, condescendencia |

**Regra de ouro Mailchimp**: "Always more important to be clear than entertaining."

### 6B. Shopify Polaris Voice (4 Principios)

| Principio | Regra Central | Exemplo |
|-----------|--------------|---------|
| **Content + design** | Palavras sao parte do design; pese cada palavra | "+" nao "+ Add" |
| **Keep it lean** | Caminho mais curto e claro (abordagem Jenga) | Remova pontuacao se nao for necessaria |
| **Write like merchants talk** | Linguagem simples, contracoes, nivel 7o ano | "don't" nao "do not" |
| **Inspire action** | Comece com verbos; direcao unica por instrucao | "add apps" nao "you can add apps" |

**Teste de qualidade Shopify**: *"Read it out loud. Does it sound like something a human would say? Ship it."*

### 6C. Adobe Spectrum Voice (3 Caracteristicas + Espectro de 5 Tons)

**Voice Characteristics**:

| Caracteristica | Definicao | Regra de Governanca |
|----------------|-----------|---------------------|
| **Rational** | Claro e compreensivel | Decisoes de gramatica baseadas em pesquisa e testadas |
| **Human** | Amigavel, honesto, responsavel | Varie estilo e estrutura de sentencas para legibilidade |
| **Focused** | Conciso e simples | Descreva apenas o necessario, sem decoracao desnecessaria |

**Tone Spectrum (5 posicoes)**:

```
MOTIVACIONAL ←——————————————————→ SUPORTIVO
  Positivo e        Polido e      Neutro e      Profissional    Preocupado e
  encorajador    respeitoso      direto         e confiavel      empatico
  
[Motivational] [Helpful]     [Instructive]  [Reassuring]    [Supportive]
```

Tom pode cair entre posicoes (nao binario). Posicao correta depende das necessidades contextuais e estado emocional do usuario.

---

## 7. Padrao Do/Don't para Voice Guidelines

Estrutura universal para documentar guidelines de voz de forma acionavel:

### Template

```markdown
### [ATRIBUTO DE VOZ]

**DO:**
- [Comportamento especifico com exemplo]
- [Comportamento especifico com exemplo]
- [Comportamento especifico com exemplo]

**DON'T:**
- [Comportamento especifico com exemplo]
- [Comportamento especifico com exemplo]
- [Comportamento especifico com exemplo]

**EXEMPLO (mesma mensagem, dois tons):**
| Errado | Certo |
|--------|-------|
| [versao fora da voz] | [versao na voz] |
```

### Exemplo: Marca de Educacao Online

**Encorajador (nao condescendente)**:

**DO:**
- "Voce ja fez a parte mais dificil — continuar quando fica desafiador."
- "Cada erro e dados para a proxima tentativa."
- "Nao e sobre o tempo que voce leva, e sobre o que voce constroi."

**DON'T:**
- "Simples! Apenas siga estes passos faceis..." (minimiza a dificuldade real)
- "Qualquer um pode fazer isso." (pressao desnecessaria)
- "Voce nao e o primeiro a ter dificuldade aqui." (patronizante)

| Errado | Certo |
|--------|-------|
| "Erro! Por favor tente novamente." | "Isso nao funcionou. Vamos tentar de outra forma?" |
| "Voce PODE fazer isso! 🎉🎉🎉" | "Voce esta chegando la." |

---

## 8. Padrao de 10 Frases: Mesma Mensagem, Tons Diferentes

Tecnica para calibrar e documentar voz. Escrever a mesma mensagem em 5-10 tons para demonstrar a diferenca:

**Mensagem base**: "Houve um problema com seu pagamento."

| Tom | Versao |
|-----|--------|
| Formal + serio | "Sua transacao nao foi processada. Entre em contato com sua instituicao financeira." |
| Neutro direto | "Houve um problema com seu pagamento. Verifique os dados e tente novamente." |
| Casual empatico | "Eita, seu pagamento nao passou. Acontece! Confira os dados do cartao e tente de novo." |
| Entusiastico | "Quase la! So precisamos resolver um detalhe no pagamento — dois segundos." |
| Suporte empatico | "Percebemos que o pagamento nao foi concluido. Podemos ajudar — o que preferir?" |
| Humoristico (contextual) | "Seu banco discordou desta compra. (Acontece com os melhores de nos.) Vamos tentar de novo?" |

**Uso**: Include 3-5 destas frases no brand guidelines para calibrar writers e LLMs.

---

## 9. Voice Governance: Como Manter Consistencia

### 9A. Estrutura de Responsabilidade

```
NIVEL 1 — Brand Owner (Head of Content / CMO)
  Define: principios de voz, score minimo, processo de aprovacao

NIVEL 2 — Voice Champions (representantes por equipe)
  Aplica: guidelines no dia a dia, revisa copy antes de publicar
  Treinamento: onboarding de 1h + checklist semanal

NIVEL 3 — All Writers / Contributors
  Executa: usa guidelines e templates
  Acesso: brand book + exemplos por canal
```

### 9B. Onboarding de Voice

```
Semana 1: Ler brand voice section (30 min) + 10 exemplos por canal
Semana 2: Escrever 5 pecas de copy, passar por voice champion
Semana 3: Calibration session (grupo) — compara versoes e discute
Ongoing: Quarterly voice audit (amostra de 20 pecas de copy publicadas)
```

### 9C. Voice para LLMs / AI Content

Para garantir que AI-generated content siga a voz da marca:

```markdown
## SYSTEM PROMPT TEMPLATE (brand voice block)

Voce escreve em nome de [MARCA]. Nossa voz e:
- [ATRIBUTO 1]: [descricao + exemplo]
- [ATRIBUTO 2]: [descricao + exemplo]
- [ATRIBUTO 3]: [descricao + exemplo]

SEMPRE:
- [regra especifica]
- [regra especifica]

NUNCA:
- [anti-padrao especifico]
- [anti-padrao especifico]

Tom por canal:
- Email: [descricao]
- Social: [descricao]
- Suporte: [descricao]

Exemplo de copy aprovado:
"[frase real na voz da marca]"
```

---

## 10. Voice Consistency Scoring

### 10A. Metodo de Score Manual (auditoria periodica)

Avaliar amostra de 20 pecas de copy publicadas contra checklist:

```
CHECKLIST POR PECA (0/1 por item):

[ ] Usa vocabulario aprovado (sem termos proibidos)
[ ] Comprimento correto para o canal
[ ] Tom correto para o canal
[ ] Ativo, nao passivo (preferencia por voz ativa)
[ ] Evita jargao (ou usa jargao correto do setor se apropriado)
[ ] Atributo de voz #1 presente
[ ] Atributo de voz #2 presente
[ ] Atributo de voz #3 presente
[ ] Nenhum anti-padrao identificado
[ ] Passa teste "soa como humano" (leitura em voz alta)
```

`Voice Consistency Score = (total de checkmarks) / (20 pecas * 10 itens) = % de 0-100`

Benchmark: >85% = excelente | 70-85% = bom | <70% = requer treinamento

### 10B. Metodo Automatizado (para times com volume alto)

```python
# Schema para avaliacao LLM-assistida
{
  "piece_id": "...",
  "channel": "social|email|support|docs|ads",
  "voice_score": 0-10,  # avaliacao holistica
  "attributes_present": ["lista dos atributos detectados"],
  "anti_patterns_found": ["lista de problemas"],
  "tone_match": true/false,  # tom correto para canal
  "recommendations": ["ajustes sugeridos"]
}
```

**Prompt para LLM evaluator**:
```
Avalie este copy em relacao a voz da marca [MARCA]:
[COPY]

Voz da marca: [BRAND VOICE BLOCK]
Canal: [CANAL]

Retorne JSON com: voice_score (0-10), attributes_present, anti_patterns_found, tone_match, recommendations.
```

---

## 11. Voice Development Process (Como Criar do Zero)

```
FASE 1: DESCOBERTA (1-2 semanas)
  a) Coletar exemplos de copy existente (30+ pecas de todos os canais)
  b) Entrevistar 5-10 stakeholders: "Descreva a marca em 3 adjetivos"
  c) Pesquisa com clientes: "Qual palavra descreve como nos comunicamos?"
  d) Benchmark: analisar voz de 3-5 concorrentes diretos

FASE 2: DEFINICAO (1 semana)
  a) Cluster os adjetivos coletados (afinidade map)
  b) Selecionar 3-5 atributos distintos (remover genericos)
  c) Para cada atributo: definir + anti-atributo + 3 exemplos
  d) Posicionar nas 4 dimensoes NNg

FASE 3: CALIBRACAO (1 semana)
  a) Escrever 10 versoes da mesma mensagem (diferentes tons)
  b) Workshop com equipe: qual versao soa "como nos"?
  c) Ajustar atributos com base no feedback
  d) Criar banco inicial de exemplos aprovados (20+ pecas)

FASE 4: DOCUMENTACAO
  a) Escrever voice section do brand book
  b) Criar Do/Don't por atributo
  c) Criar matriz de tom por canal
  d) Gravar video de 5 min "nossa voz em pratica"

FASE 5: ATIVACAO
  a) Training com todos os writers (1h)
  b) Adicionar voice block em sistema de prompts de AI
  c) Criar voice champion por equipe
  d) Agendar voice audit trimestral
```

---

## 12. Vocabulario: Palavras Aprovadas e Proibidas

### Template de Vocabulario de Marca

**USAR:**
| Categoria | Palavras/Frases Aprovadas |
|-----------|--------------------------|
| Acao | [verbos que refletem a personalidade] |
| Beneficio | [descricoes de valor sem hiperbole] |
| Suporte | [frases de empatia aprovadas] |
| Tecnico | [jargao do setor, se aplicavel] |

**EVITAR:**
| Categoria | Palavras/Frases Proibidas | Por que |
|-----------|--------------------------|---------|
| Corporativez | "synergy", "leverage", "holistic" | Vago e desumano |
| Hiperbole | "incrivel", "revolucionario", "nunca visto" | Perde credibilidade |
| Passividade | "foi implementado", "e possivel que" | Fraco e indireto |
| Condescendencia | "simples", "apenas", "so precisa" | Minimiza dificuldade real |
| Alarme | "AVISO:", "CRITICO:", "URGENTE:" em contextos normais | Gera ansiedade desnecessaria |

---

## 13. Aplicacao para N06 Brand Architect

**Para cada empresa que passa pelo N06**:

### Input necessario para gerar Voice System
```yaml
empresa: [nome]
setor: [industria]
publico: [descricao do ICP]
arquetipo: [resultado do Brand Core — bloco 11 do modelo 32]
tom_desejado:
  formalidade: [1-5]
  seriedade: [1-5]
  proximidade: [1-5]
  autoridade: [1-5]
  intensidade: [1-5]
concorrentes: [3 marcas para benchmark]
exemplos_aprovados: [3-5 frases que "soam como a marca"]
```

### Output do N06 (Voice Section do Brand Book)
```
1. Perfil de Voz (5 dimensoes com posicionamento)
2. 3-5 Atributos com anti-atributos e exemplos
3. Matriz de Tom por Canal (8 canais)
4. Do/Don't por atributo (3 itens cada)
5. Banco de 10 frases calibradas
6. Vocabulario aprovado e proibido
7. System prompt template para AI/LLMs
8. Voice Consistency Checklist
```

---

## Referencias

- NNGroup — "The Four Dimensions of Tone of Voice" — Kate Moran (2016, rev. 2023)
- Mailchimp Content Style Guide — Voice and Tone (styleguide.mailchimp.com)
- Shopify Polaris Design System — Voice and Tone
- Adobe Spectrum — Voice and Tone
- Content Design London — Voice and Tone
- Frontify Brand Guidelines Guide 2026

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_book_patterns]] | sibling | 0.23 |
| [[ex_feedback_tone_correction]] | downstream | 0.22 |
| [[p01_kc_brand_frameworks]] | sibling | 0.21 |
| [[p01_kc_brand_archetypes]] | sibling | 0.19 |
| [[p01_kc_brand_voice_consistency_channels]] | sibling | 0.15 |
| [[brand_voice_templates]] | downstream | 0.15 |
