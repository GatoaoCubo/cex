---
id: p01_kc_brand_frameworks
kind: knowledge_card
pillar: P01
title: "Brand Strategy Frameworks Collection — Positioning, Identity, Voice, Narrative"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-strategy
quality: 9.1
updated: 2026-04-07
tags: [brand, frameworks, positioning, identity, voice, narrative, strategy]
tldr: "Universal brand strategy frameworks: Ries & Trout, Blue Ocean, JTBD, Value Proposition Canvas, Keller Pyramid, NNGroup Voice, StoryBrand, Hero Journey."
when_to_use: "When building brand strategy from scratch or auditing existing brand positioning."
keywords: [brand-strategy, positioning, identity, voice, narrative, frameworks]
density_score: 0.94
axioms:
  - "ALWAYS start with positioning statement before visual identity — strategy precedes aesthetics."
  - "NEVER use more than 2 frameworks simultaneously — pick 1 primary, 1 validation."
  - "ALWAYS validate positioning against JTBD — if it doesn't solve a real job, it's decoration."
linked_artifacts:
  primary: p01_kc_brand_book_patterns
  related: [p01_kc_brand_archetypes, n06_kc_competitive_positioning, n06_kc_icp_frameworks, n06_output_brand_book]
related:
  - p01_kc_brand_book_patterns
  - bld_meta_manifest_builder
  - p03_sp_brand_nucleus
  - p12_dr_commercial
  - p02_agent_commercial_nucleus
  - spec_n06_brand_verticalization
  - bld_meta_instructions_builder
  - bld_meta_memory_builder
---

# Brand Strategy Frameworks Collection

## POSITIONING

### Declaracao de Posicionamento Ries & Trout

**Author**: Al Ries & Jack Trout
**Source**: Positioning: The Battle for Your Mind (1981)
**Purpose**: Criar declaracao clara de posicionamento de marca
**Template**: Para {target_audience} que {need}, {brand} e {category} que {benefit} porque {reason_to_believe}.

**Fields**:
- `target_audience`: Publico-alvo especifico (demografico + psicografico) (ex: mulheres 25-45 que buscam praticidade no dia a dia)
- `need`: Necessidade ou problema do publico (ex: precisam de maquiagem duravel para rotina corrida)
- `brand`: Nome da marca (ex: BEAUTYFIX)
- `category`: Categoria de mercado em que a marca compete (ex: a linha de cosmeticos profissionais)
- `benefit`: Beneficio principal que diferencia a marca (ex: oferece 24h de fixacao sem retoque)
- `reason_to_believe`: Prova ou razao para acreditar no beneficio (ex: nossa formula patenteada com microparticulas de silicone)

**Example**:
- target_audience: mulheres 25-45 que buscam praticidade no dia a dia
- need: precisam de maquiagem duravel para rotina corrida
- brand: BEAUTYFIX
- category: a linha de cosmeticos profissionais
- benefit: oferece 24h de fixacao sem retoque
- reason_to_believe: nossa formula patenteada com microparticulas de silicone
- result: Para mulheres 25-45 que buscam praticidade no dia a dia que precisam de maquiagem duravel para rotina corrida, BEAUTYFIX e a linha de cosmeticos profissionais que oferece 24h de fixacao sem retoque porque nossa formula patenteada com microparticulas de silicone.

---

### Estrategia do Oceano Azul - Canvas

**Author**: W. Chan Kim & Renee Mauborgne
**Source**: Blue Ocean Strategy (2005)
**Purpose**: Identificar diferenciais criando novo espaco de mercado
**Template**: {'eliminate': 'Fatores que a industria compete mas podem ser eliminados: {eliminate_factors}', 'reduce': 'Fatores que podem ser reduzidos abaixo do padrao da industria: {reduce_factors}', 'raise': 'Fatores que podem ser elevados acima do padrao da industria: {raise_factors}', 'create': 'Fatores que a industria nunca ofereceu e podem ser criados: {create_factors}'}

**Example**:
- brand: ECOSMART - Eletronicos Sustentaveis
- canvas: {'eliminate': ['embalagens plasticas', 'manuais impressos extensos', 'obsolescencia programada'], 'reduce': ['variedade de modelos (foco em 3 SKUs)', 'custo de marketing tradicional'], 'raise': ['durabilidade (garantia 5 anos)', 'repairabilidade (pecas modulares)', 'transparencia de origem'], 'create': ['programa de trade-in com desconto', 'certificado de pegada de carbono', 'comunidade de usuarios reparadores']}
- strategy_curve: {'preco': {'industria': 5, 'ecosmart': 6, 'note': 'ligeiramente acima mas justificado'}, 'qualidade': {'industria': 6, 'ecosmart': 9, 'note': 'muito acima - foco principal'}, 'conveniencia': {'industria': 8, 'ecosmart': 7, 'note': 'ligeiramente abaixo'}, 'variedade': {'industria': 9, 'ecosmart': 3, 'note': 'muito abaixo - intencional'}, 'atendimento': {'industria': 5, 'ecosmart': 8, 'note': 'acima - comunidade ativa'}, 'inovacao': {'industria': 7, 'ecosmart': 7, 'note': 'par com industria'}, 'sustentabilidade': {'industria': 3, 'ecosmart': 10, 'note': 'diferencial maximo'}, 'exclusividade': {'industria': 4, 'ecosmart': 7, 'note': 'acima - nicho consciente'}}

---

### Framework Jobs-to-be-Done

**Author**: Clayton Christensen
**Source**: Competing Against Luck (2016)
**Purpose**: Entender o 'trabalho' que o cliente contrata o produto para fazer
**Template**: Quando {situation}, eu quero {motivation} para que eu possa {outcome}.

**Fields**:
- `situation`: Contexto ou gatilho que cria a necessidade (ex: estou saindo para o trabalho com pressa)
- `motivation`: Acao ou solucao desejada (ex: aplicar maquiagem rapidamente)
- `outcome`: Resultado final desejado (emocional ou funcional) (ex: parecer profissional o dia Planned sem preocupacao)

**Example**:
- brand: BEAUTYFIX
- primary_job: {'situation': 'estou saindo para o trabalho com pressa e sei que nao terei tempo para retoques', 'motivation': 'aplicar maquiagem que dure o dia inteiro', 'outcome': 'parecer profissional em todas as reunioes sem me preocupar com a aparencia', 'result': 'Quando estou saindo para o trabalho com pressa e sei que nao terei tempo para retoques, eu quero aplicar maquiagem que dure o dia inteiro para que eu possa parecer profissional em todas as reunioes sem me preocupar com a aparencia.'}
- secondary_jobs: [{'type': 'emotional', 'statement': 'Quando acordo cansada, quero me sentir bonita rapidamente para comecar o dia com confianca.'}, {'type': 'social', 'statement': 'Quando tenho evento apos trabalho, quero maquiagem que transicione bem para parecer arrumada sem refazer tudo.'}]
- competing_solutions: ['Maquiagem tradicional (precisa retoque)', 'Nao usar maquiagem (nao resolve necessidade emocional)', 'Levar necessaire para retoques (inconveniente)', 'Maquiagem permanente (caro e arriscado)']

---

### Canvas de Proposta de Valor

**Author**: Alexander Osterwalder
**Source**: Value Proposition Design (2014)
**Purpose**: Alinhar proposta de valor com perfil do cliente
**Template**: {'customer_profile': {'jobs': 'Tarefas que o cliente tenta realizar: {customer_jobs}', 'pains': 'Frustraccoes e obstaculos: {customer_pains}', 'gains': 'Beneficios e resultados desejados: {customer_gains}'}, 'value_map': {'products_services': 'O que oferecemos: {products_services}', 'pain_relievers': 'Como aliviamos as dores: {pain_relievers}', 'gain_creators': 'Como geramos ganhos: {gain_creators}'}}

**Fields**:
- `customer_jobs`: Lista de 3-5 tarefas principais do cliente
- `customer_pains`: Lista de 3-5 principais dores/frustraccoes
- `customer_gains`: Lista de 3-5 ganhos desejados
- `products_services`: Lista de produtos/servicos oferecidos
- `pain_relievers`: Como cada produto alivia uma dor especifica
- `gain_creators`: Como cada produto gera um ganho especifico

**Example**:
- brand: FITBOX - Marmitas Fitness
- customer_profile: {'jobs': ['Manter dieta equilibrada', 'Economizar tempo na semana', 'Controlar calorias e macros', 'Variar refeicoes sem perder praticidade'], 'pains': ['Falta de tempo para cozinhar', 'Marmitas saudaveis sao caras', 'Comida fitness e sem sabor', 'Dificuldade em calcular macros', 'Desperdicio quando compra ingredientes'], 'gains': ['Comer bem sem esforco', 'Economizar dinheiro vs delivery', 'Atingir metas de saude', 'Variedade sem monotonia', 'Praticidade no dia a dia']}
- value_map: {'products_services': ['Marmitas congeladas com macros calculados', 'Assinatura semanal personalizada', 'App com tracking de consumo', 'Cardapio rotativo (20+ opcoes)'], 'pain_relievers': ['Entrega semanal elimina tempo de preparo', 'Preco competitivo (R$18-25/refeicao)', 'Chef profissional = sabor garantido', 'Rotulos com macros detalhados', 'Porcoes individuais = zero desperdicio'], 'gain_creators': ['5min no micro = refeicao pronta', '30% mais barato que delivery saudavel', 'Resultados visiveis em 30 dias', '20 pratos novos por mes', 'App sincroniza com MyFitnessPal']}
- fit_analysis: {'pain_relief_coverage': '5/5 dores endereçadas', 'gain_creation_coverage': '5/5 ganhos criados', 'fit_score': 9.2}

---

## IDENTITY

### Unilever Brand Key

**Author**: Unilever
**Source**: Unilever Brand Development Framework
**Purpose**: Definir todos os elementos fundamentais da identidade de marca
**Template**: {'root_strengths': '{root_strengths}', 'competitive_environment': '{competitive_environment}', 'target': '{target}', 'insight': '{insight}', 'benefits': {'functional': '{functional_benefits}', 'emotional': '{emotional_benefits}'}, 'values_personality': '{values_personality}', 'reason_to_believe': '{reason_to_believe}', 'discriminator': '{discriminator}', 'essence': '{essence}'}

**Example**:
- brand: TERRAVIVA - Alimentos Organicos
- root_strengths: ['20 anos de agricultura familiar organica', 'Certificacao IBD desde 2005', 'Relacao direta com 50+ produtores locais', 'Rastreabilidade completa do campo a mesa']
- competitive_environment: ['Marcas organicas premium (Jasmine, Mãe Terra)', 'Supermercados com linha propria organica', 'Feiras de produtores locais', 'Hortas urbanas e CSA (agricultura suportada por comunidade)']
- target: Familias urbanas classe A/B, 30-50 anos, com filhos, que valorizam saude e sustentabilidade, dispostas a pagar mais por qualidade e procedencia, frequentam feiras organicas aos finais de semana
- insight: Os pais sentem culpa por nao ter tempo de cozinhar do zero para os filhos, e buscam atalhos que ainda permitam se sentir 'bons pais' alimentando a familia com qualidade
- benefits: {'functional': ['Alimentos sem agrotoxicos', 'Sabor mais intenso e natural', 'Maior durabilidade na geladeira', 'Informacao completa de origem'], 'emotional': ['Tranquilidade de estar cuidando da familia', 'Orgulho de apoiar pequenos produtores', 'Conexao com a natureza mesmo na cidade', 'Sensacao de escolha consciente']}
- values_personality: {'values': ['Autenticidade', 'Sustentabilidade', 'Comunidade', 'Transparencia', 'Cuidado'], 'personality': 'Como uma avo do interior: acolhedora, simples, honesta, que conta historias sobre de onde vem cada ingrediente'}
- reason_to_believe: ['QR code em cada produto com video do produtor', 'Certificacao IBD + Selo Organico Brasil', "Programa 'Conheca o Produtor' com visitas agendadas", 'Garantia de devolucao se nao gostar']
- discriminator: Unica marca organica que conecta cada produto a historia real do produtor via QR code, criando transparencia radical
- essence: Comida de verdade, gente de verdade

---

### Piramide de Ressonancia de Marca (Keller)

**Author**: Kevin Lane Keller
**Source**: Strategic Brand Management (2008)
**Purpose**: Construir brand equity atraves de 6 niveis de relacionamento
**Template**: {'salience': {'category_identification': '{category_identification}', 'needs_satisfied': '{needs_satisfied}', 'awareness_depth': '{awareness_depth}', 'awareness_breadth': '{awareness_breadth}'}, 'performance': '{performance_attributes}', 'imagery': '{brand_imagery}', 'judgments': '{brand_judgments}', 'feelings': '{brand_feelings}', 'resonance': '{brand_resonance}'}

**Example**:
- brand: NATURA
- pyramid: {'salience': {'category_identification': 'Cosmeticos e perfumaria brasileira', 'needs_satisfied': 'Beleza, bem-estar, presente com significado', 'awareness_depth': '95% reconhecimento espontaneo no Brasil', 'awareness_breadth': 'Associada a ocasioes de presente, auto-cuidado, sustentabilidade'}, 'performance': {'primary_attributes': ['Ingredientes naturais brasileiros', 'Fragrâncias marcantes', 'Embalagens refil'], 'reliability': 'Alta - consistencia de qualidade', 'price_positioning': 'Premium acessivel', 'service': 'Consultoras como canal personalizado'}, 'imagery': {'user_profile': 'Mulheres conscientes, que valorizam brasilidade e sustentabilidade', 'usage_situations': 'Rotina diaria, presentes, momentos de auto-cuidado', 'personality': 'Autentica, acolhedora, consciente, brasileira', 'heritage': 'Empresa B Corp, compromisso ambiental desde fundacao'}, 'judgments': {'quality': 'Alta qualidade com ingredientes naturais', 'credibility': 'Expertise em biodiversidade brasileira', 'consideration': 'Top 3 em consideracao no segmento', 'superiority': 'Lider em sustentabilidade no setor'}, 'feelings': {'primary': ['warmth', 'self_respect', 'social_approval'], 'warmth': 'Conexao com natureza e brasilidade', 'self_respect': 'Escolha consciente e alinhada com valores', 'social_approval': 'Marca bem vista socialmente'}, 'resonance': {'loyalty': 'Alto indice de recompra (70%+)', 'attachment': 'Relacao emocional com linhas classicas (Ekos, Tododia)', 'community': 'Rede de 1.8M consultoras engajadas', 'engagement': 'Programa de fidelidade + conteudo educativo'}}

---

### 12 Arquetipos de Marca (Jung/Mark & Pearson)

**Author**: Carol S. Pearson & Margaret Mark
**Source**: The Hero and the Outlaw (2001)
**Purpose**: Definir personalidade de marca atraves de arquetipos universais

**Example**:
- brand: NATURA
- primary_archetype: {'id': 'caregiver', 'percentage': 75, 'manifestation': 'Cuidado com as pessoas e o planeta, relacionamento com consultoras'}
- secondary_archetype: {'id': 'explorer', 'percentage': 25, 'manifestation': 'Exploracao da biodiversidade brasileira, inovacao em ingredientes'}
- voice_blend: {'from_caregiver': ['Acolhedor', 'Protetor', 'Generoso'], 'from_explorer': ['Autêntico', 'Descobridor']}

---

## VOICE

### Dimensoes de Personalidade de Marca

**Author**: CODEXA Framework
**Purpose**: Posicionar tom de voz em 4 espectros complementares
**Template**: {'brand': '{brand_name}', 'positioning': {'formality': '{formality_value}', 'enthusiasm': '{enthusiasm_value}', 'humor': '{humor_value}', 'authority': '{authority_value}'}, 'summary': '{voice_summary}'}

**Example**:
- brand: NEOBANK_EXAMPLE
- positioning: {'formality': 2, 'enthusiasm': 4, 'humor': 3, 'authority': 3}
- summary: Tom casual e energico, com pitadas de humor inteligente, posicionando-se como especialista acessivel
- voice_dna: Amigo especialista que explica financas de forma descomplicada

---

### Matriz de Tom de Voz

**Purpose**: Mapear tom em matriz 2x2 para facil visualizacao
**Template**: {'brand': '{brand_name}', 'x_position': '{x_value}', 'y_position': '{y_value}', 'quadrant': '{quadrant_name}', 'voice_description': '{voice_description}'}

**Example**:
- brand: IFOOD
- x_position: 2
- y_position: 4
- quadrant: Amigo Divertido
- voice_description: Tom super casual e divertido, com humor leve e linguagem do dia-a-dia, criando conexao como amigo que entende sua fome

---

### Guia de Mensagens (Do's e Don'ts)

**Purpose**: Definir regras praticas de comunicacao da marca
**Template**: {'dos': {'description': 'Praticas recomendadas de comunicacao', 'min_items': 5, 'max_items': 8, 'format': 'Acao + Exemplo concreto'}, 'donts': {'description': 'Praticas a evitar', 'min_items': 5, 'max_items': 8, 'format': 'Acao + Alternativa correta'}, 'seed_words': {'description': 'Vocabulario proprietario da marca', 'min_items': 5, 'format': 'Palavra + Significado + Contexto de uso'}, 'example_phrases': {'description': 'Frases-modelo em diferentes contextos', 'min_items': 10, 'contexts': ['boas_vindas', 'confirmacao', 'erro', 'promocao', 'despedida']}}

**Example**:
- brand: NEOBANK_EXAMPLE
- dos: [{'action': 'Use linguagem simples e direta', 'example': 'Seu cartao chegou! em vez de Confirmamos a entrega do seu meio de pagamento'}, {'action': 'Fale em primeira pessoa do plural (nos)', 'example': 'Estamos aqui pra ajudar em vez de A empresa esta disponivel'}, {'action': 'Celebre conquistas do cliente', 'example': 'Parabens! Voce ja economizou R$500 em anuidade'}, {'action': 'Use emojis com moderacao', 'example': 'Tudo certo por aqui! (com emoji positivo ocasional)'}, {'action': 'Explique termos tecnicos', 'example': 'IOF (um imposto do governo) em vez de so IOF'}, {'action': 'Seja transparente sobre custos', 'example': 'Essa operacao custa R$2,50 - mesmo que seja ruim'}]
- donts: [{'avoid': 'Usar jargao bancario', 'instead': 'correntista → cliente, operacao de credito → emprestimo'}, {'avoid': 'Ser excessivamente formal', 'instead': 'Prezado Senhor → Ola, Cliente'}, {'avoid': 'Culpar o cliente por erros', 'instead': 'Voce errou a senha → A senha digitada nao confere'}, {'avoid': 'Usar asteriscos e letrinhas', 'instead': 'Deixar condicoes claras no texto principal'}, {'avoid': 'Prometer e nao cumprir', 'instead': 'So comunicar o que podemos entregar'}, {'avoid': 'Ser frio em momentos dificeis', 'instead': 'Sabemos que isso e frustrante...'}]
- seed_words: [{'word': 'brand-card', 'meaning': 'The branded debit card (affectionate nickname)', 'usage': 'My brand-card arrived! / Pay with brand-card?'}, {'word': 'simplify', 'meaning': 'Make the complex simple', 'usage': 'We simplify the financial world'}, {'word': 'digital first', 'meaning': 'Digital experience priority', 'usage': 'Born digital first'}, {'word': 'Neo', 'meaning': 'Prefix for products and services', 'usage': 'NeoAccount, NeoInvest, NeoCrypto'}, {'word': 'humanized', 'meaning': 'Empathetic real support', 'usage': 'Humanized support, not robotic'}]
- example_phrases: {'boas_vindas': ['Ola! Que bom ter voce por aqui.', 'Bem-vindo ao roxinho! Estamos prontos pra ajudar.'], 'confirmacao': ['Tudo certo! Sua solicitacao foi processada.', 'Feito! Ja pode conferir na sua conta.'], 'erro': ['Ops, algo deu errado. Mas ja estamos resolvendo.', 'Hmm, nao conseguimos processar. Tenta de novo?'], 'promocao': ['Surpresa! Seu limite aumentou. Voce merece.', 'Boas noticias: desbloqueamos um beneficio pra voce.'], 'despedida': ['Qualquer coisa, estamos aqui. Ate mais!', 'Resolvido! Se precisar, e so chamar.']}

---

## NARRATIVE

### Jornada do Heroi (Campbell)

**Author**: Joseph Campbell
**Source**: The Hero with a Thousand Faces (1949)
**Purpose**: Estruturar narrativa de marca usando arquetipo universal
**Template**: {'hero': '{customer_persona}', 'mentor': '{brand_name}', 'journey': '{stages_filled}'}

**Example**:
- brand: CROSSFIT
- hero: Profissional sedentario, 35 anos, que quer mudar de vida
- journey: {'mundo_comum': 'Joao trabalha 10h/dia, come mal, esta 15kg acima do peso, nao tem energia', 'chamado': 'Apos exame medico preocupante, decide que precisa mudar', 'recusa': 'Ja tentei academia e desisti, nao tenho tempo, CrossFit e pra atletas', 'mentor': 'CrossFit aparece com proposta: comunidade que nao deixa desistir, treinos curtos e intensos', 'travessia': 'Primeira aula experimental - assustadora mas acolhedora', 'testes': 'Primeiras semanas duras, musculos doendo, mas comunidade apoiando', 'caverna': 'Primeiro WOD competitivo contra o tempo', 'provacao': 'Momento em que quer desistir no meio do treino, mas colegas gritando apoio', 'recompensa': 'Consegue fazer primeiro pull-up, perde 10kg em 3 meses', 'retorno': 'Volta ao escritorio com mais energia, colegas notam diferenca', 'ressurreicao': 'Completa primeiro campeonato local', 'elixir': 'Traz amigos para experimentar, vira exemplo no trabalho'}

---

### StoryBrand Framework

**Author**: Donald Miller
**Source**: Building a StoryBrand (2017)
**Purpose**: Clarificar mensagem de marca usando estrutura narrativa
**Template**: {'one_liner': '{character} enfrenta {problem}. {guide} oferece {plan}. {call_to_action} para {success} e evitar {failure}.', 'brandscript': '{full_7_elements}'}

**Example**:
- brand: EVERNOTE
- brandscript: {'character': {'persona': 'Profissionais ocupados e criativos', 'want': 'Organizar ideias e nunca esquecer o que e importante'}, 'problem': {'external': 'Informacoes espalhadas em varios lugares (papeis, apps, emails)', 'internal': 'Ansiedade de estar esquecendo algo importante', 'philosophical': 'Ninguem deveria perder uma ideia brilhante por falta de organizacao'}, 'guide': {'empathy': 'Sabemos como e frustrante ter uma ideia incrivel e nao lembrar depois', 'authority': '250 milhoes de usuarios confiam suas ideias ao Evernote'}, 'plan': ['1. Baixe o app gratuito', '2. Capture qualquer ideia (texto, foto, audio)', '3. Encontre tudo instantaneamente com busca inteligente'], 'call_to_action': {'direct': 'Comece gratis agora', 'transitional': 'Baixe o guia: 10 formas de organizar sua vida'}, 'success': {'have': 'Todas as ideias organizadas em um lugar', 'feel': 'Tranquilidade de nunca perder nada importante', 'become': 'Uma pessoa mais produtiva e confiavel'}, 'failure': {'consequence': 'Continuar perdendo ideias valiosas e oportunidades por desorganizacao'}}
- one_liner: Profissionais ocupados lutam com informacoes espalhadas. Evernote captura e organiza tudo em um lugar. Baixe gratis e nunca mais perca uma ideia.

---

### Estrutura de Historia de Origem

**Purpose**: Criar narrativa fundacional autentica da marca
**Template**: Tudo comecou quando {spark}. No inicio, enfrentamos {struggle}. Foi entao que descobrimos {breakthrough}. Hoje, nossa missao e {mission}. Sonhamos com um mundo onde {future}.

**Example**:
- brand: AIRBNB
- story: {'spark': 'Brian e Joe nao conseguiam pagar aluguel em San Francisco. Colocaram colchoes de ar na sala e hospedaram convidados de uma conferencia de design.', 'struggle': 'Ninguem acreditava na ideia. Receberam 7 rejeicoes de investidores. Tiveram que vender caixas de cereal para sobreviver.', 'breakthrough': 'Perceberam que as pessoas nao queriam so um lugar para dormir - queriam experiencias locais autenticas e conexao humana.', 'mission': 'Criar um mundo onde qualquer pessoa pode pertencer em qualquer lugar.', 'future': 'Viagens serao sobre conexao humana, nao hoteis padronizados. Qualquer um pode ser anfitriao e transformar espaco vazio em renda.'}
- formatted: Tudo comecou quando Brian e Joe nao conseguiam pagar aluguel em San Francisco e colocaram colchoes de ar na sala. No inicio, enfrentaram 7 rejeicoes de investidores. Foi entao que descobriram que pessoas queriam experiencias locais autenticas. Hoje, sua missao e criar um mundo onde qualquer pessoa pode pertencer em qualquer lugar.

---

## SCORING

### Framework de Validacao 5D para Marca

| Dimension | Weight | Scale |
|-----------|--------|-------|
| Identity | 2.0 |  |
| Positioning | 2.0 |  |
| Voice | 2.0 |  |
| Visual | 2.0 |  |
| Narrative | 2.0 |  |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_book_patterns]] | sibling | 0.18 |
| [[bld_meta_manifest_builder]] | downstream | 0.18 |
| [[p03_sp_brand_nucleus]] | downstream | 0.17 |
| [[p12_dr_commercial]] | downstream | 0.17 |
| [[p02_agent_commercial_nucleus]] | downstream | 0.16 |
| [[spec_n06_brand_verticalization]] | downstream | 0.16 |
| [[bld_meta_instructions_builder]] | downstream | 0.16 |
| [[bld_meta_memory_builder]] | downstream | 0.15 |
