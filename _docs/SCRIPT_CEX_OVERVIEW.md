# CEX — Script de Apresentação (3 min)

## Para: Profissionais e entusiastas de IA
## Tom: Técnico-didático, direto, sem enrolação

---

O CEX é um dicionário tipado universal para agentes de inteligência artificial.

Imagine o seguinte problema: você quer que um LLM construa um agente. Você pede, e ele gera um arquivo markdown ou YAML com campos inventados na hora. Outro LLM gera campos diferentes. Outro modelo gera uma estrutura completamente incompatível. Não existe padrão. Cada geração é um acidente isolado.

O CEX resolve isso com uma taxonomia de 99 tipos — chamados "kinds". Cada kind tem um nome, uma definição, um esquema, e um builder com 13 arquivos de instrução. Quando qualquer LLM — Claude, GPT, Gemini, Llama — precisa gerar um artefato, ele consulta o builder daquele kind e produz algo estruturalmente compatível com todos os outros artefatos do sistema.

Esses 99 kinds se organizam em 12 pilares. Pilar 1 é conhecimento. Pilar 2 são agentes. Pilar 3 são prompts. Pilar 4 são ferramentas. E assim por diante, até o pilar 12 que é orquestração. Cada artefato pertence a exatamente um pilar — essa é uma regra imutável chamada "one kind, one pillar".

O motor de construção se chama Pipeline 8F — oito funções sequenciais que todo LLM executa para produzir um artefato. F1 Constrain carrega o esquema. F2 Become carrega a identidade do construtor. F3 Inject carrega o conhecimento relevante — knowledge cards, exemplos, memória. F4 Reason planeja a abordagem. F5 Call identifica ferramentas disponíveis. F6 Produce gera o artefato. F7 Govern valida com um checklist de 12 pontos. F8 Collaborate salva, compila para YAML, re-indexa, e sinaliza completude.

A validação em F7 usa dois métodos. O 12LP é um checklist de 12 pontos estruturais — frontmatter, schema, densidade, unicidade, boundary. O 5D é um scoring de 5 dimensões — integridade estrutural, densidade de conteúdo, acionabilidade, disciplina de boundary, e composabilidade. O score final é uma média ponderada. Abaixo de 8.0, o artefato não é publicado.

Acima da camada de 99 kinds, existem 7 núcleos. Cada núcleo é uma composição de 12 a 25 kinds que formam uma unidade operacional. N03, o Builder, é o mais importante — é a fábrica que constrói fábricas. Ele acessa todos os 99 builders e executa o pipeline 8F. N07 é o orquestrador — ele nunca executa, apenas despacha tarefas para os outros núcleos.

A arquitetura é multi-LLM por design. N03 usa Claude Opus para construção complexa. N05 usa Codex da OpenAI para revisão de código. N04 e N01 usam Gemini 2.5 Pro com janela de 1 milhão de tokens para conhecimento e pesquisa. N02 e N06 usam Claude Sonnet para escrita criativa. E como fallback gratuito, existe um provider Ollama que roda modelos locais com custo zero.

O sistema de orquestração suporta até 6 construtores em paralelo via grid dispatch, com continuous batching — quando um slot termina, o próximo da fila entra automaticamente. Cada construtor sinaliza completude via arquivos JSON, e um monitor detecta travamentos.

O que torna o CEX único é a auto-referência. O N03 se construiu usando o próprio pipeline 8F. Os artefatos que definem como construir artefatos foram construídos pelo sistema que eles definem. Isso é um Strange Loop intencional — um bootstrap paradox resolvido em 3 fases: gênesis manual, autopoiese onde o sistema se completa, e reescrita onde ele melhora seus próprios originais.

Para usar o CEX, você instala, dá boot com o comando "cex", e descreve o que quer em linguagem natural. O motor resolve a intenção para um kind, carrega o builder, e executa o pipeline 8F. O resultado é um artefato tipado, validado, compilado, e indexado — pronto para compor com outros artefatos do sistema.

O CEX não é um framework de agentes. É um dicionário de construção. Qualquer framework pode consumir os artefatos que ele produz. Qualquer LLM pode executar seus builders. A única coisa que o CEX opina é a estrutura — e essa estrutura é o que faz sistemas de IA escalarem com qualidade.
