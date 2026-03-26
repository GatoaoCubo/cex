# CEX - Company Experience X
## Whitepaper v1.0 | O Cerebro Empresarial Universal

**Autores**: STELLA + EDISON + USER | **Data**: 2026-03-26

---

## 1. O Que Eh o CEX

CEX eh um framework de inteligencia artificial organizacional. Transforma
qualquer empresa em uma organizacao assistida por IA, onde cada departamento
tem seu proprio cerebro especializado.

**C** = Company. **E** = Experience. **X** = o nome da sua empresa.

CEX nao eh um chatbot. Eh uma **arquitetura de conhecimento** que organiza
tudo que uma empresa sabe, faz e decide em uma estrutura fractal navegavel
por humanos e por IAs.

---

## 2. O Problema

Empresas usam IA de forma fragmentada:
- ChatGPT pra emails, Copilot pra codigo, docs espalhados
- Conhecimento critico na cabeca de poucas pessoas
- Zero padronizacao entre departamentos

**Resultado**: a IA sabe muito sobre o mundo, mas nada sobre a SUA empresa.

---

## 3. A Solucao: 3 Dimensoes Fractais

### 3.1 Os 7 Nucleos (Setores)

| # | Nucleo | Faz o que | Exemplo |
|---|--------|-----------|---------|
| N01 | Inteligencia & Pesquisa | Sabe o que o mercado quer | Concorrentes, trends |
| N02 | Marketing & Comunicacao | Conta ao mundo quem voce eh | Anuncios, social |
| N03 | Producao & Engenharia | Constroi o produto | Codigo, design |
| N04 | Conhecimento & Seguranca | Protege e organiza o saber | T.I., compliance |
| N05 | Operacoes & Automacao | Faz tudo rodar | Deploy, logistica |
| N06 | Comercial & Financeiro | Gera receita | Vendas, pricing |
| N07 | Administracao | Coordena tudo | Estrategia, governanca |

### 3.2 Os 12 Pilares (LPs)

| Grupo | Pilares | Pergunta |
|-------|---------|----------|
| CORE | P01 Conhecimento, P02 Modelos, P03 Prompts, P04 Tools | O que a IA eh e sabe? |
| QUALITY | P05 Saida, P06 Schema, P07 Evals, P08 Arquitetura | Como performa? |
| SCALE | P09 Config, P10 Memoria, P11 Feedback, P12 Orquestracao | Como opera em escala? |

**7 Nucleos x 12 Pilares = 84 areas de conhecimento.**

### 3.3 Os 78 Tipos de Artefato

Cada pilar tem 4-10 tipos (knowledge_card, agent, skill...). 78 total.
Cada tipo tem schema + builder + template.

---

## 3.4 As 8 Funcoes LLM (Camada Acima)

Acima dos tipos e pilares, existe a logica de como LLMs raciocinam.
Todo sistema de IA — do prompt mais simples ao satellite mais complexo —
executa 8 funcoes na mesma ordem:

| # | Funcao | Em Portugues | Exemplo |
|---|--------|-------------|---------|
| 1 | BECOME | "Quem eu sou?" | Carregar persona do vendedor |
| 2 | INJECT | "O que eu sei?" | Buscar dados do produto |
| 3 | REASON | "Como penso sobre isso?" | Planejar a resposta |
| 4 | CALL | "Que ferramentas uso?" | Consultar estoque via API |
| 5 | PRODUCE | "O que entrego?" | Gerar a resposta final |
| 6 | CONSTRAIN | "Esta no formato certo?" | Validar contra template |
| 7 | GOVERN | "Passou no controle?" | Checar qualidade >= 7.0 |
| 8 | COLLABORATE | "Quem recebe agora?" | Passar pro proximo agente |

Um ChatGPT simples executa 1-2. Um agente executa 4-5. O CEX executa todas as 8.

---

## 4. Formato Dual: MD + YAML

O dilema foi resolvido com os DOIS:

| Arquivo | Quem usa | Funcao |
|---------|----------|--------|
| `p01_kc_funil.md` | Humano | Criar, editar, revisar (frontmatter YAML + corpo MD) |
| `compiled/p01_kc_funil.yaml` | Pipeline/RAG/Brain | Buscar, indexar, consumir (YAML puro) |

O `.md` eh a FONTE. O `compiled/` eh o OUTPUT. Sincronizados por `distill.py`.

| Camada | Formato | Motivo |
|--------|---------|--------|
| Artefatos (78 types) | `.md` + `compiled/.yaml` (DUAL) | Humano + maquina |
| Schemas | `.yaml` only | Definicao formal |
| Builders (13 ISO) | `.md` only | Instrucoes pra LLM |
| Meta-docs | `.md` only | Governanca humana |
| Tools | `.py` only | Codigo executavel |

---

## 5. Hierarquia (5 niveis)

| Nivel | Path | O que |
|-------|------|-------|
| L0 | `archetypes/builders/` | Moldes (fabricas que constroem) |
| L1 | `P01..P12/` | Schemas raiz (definem 78 types) |
| L2 | `N01..N07/` | Nucleos (setores da empresa) |
| L3 | `N{XX}/P{NN}/` | Pilar dentro do nucleo |
| L4 | `N{XX}/P{NN}/{type}/` | Tipo (onde artefatos vivem) |

---

## 6. Principios Inviolaveis

1. **Fractal**: mesma estrutura em cada nivel
2. **Denso**: density >= 0.8
3. **Dual**: artefatos em .md E compiled/.yaml
4. **Herdado**: schemas de nucleo herdam do root
5. **Construido**: builders constroem, humano revisa
6. **Validado**: quality gates, minimo 7.0
7. **Modular**: nucleos/pilares/types independentes
8. **Navegavel**: path = endereco semantico
9. **Versionado**: git, rastreavel
10. **Universal**: qualquer empresa, so muda o .env

---

## 7. Glossario

| Termo | Significado |
|-------|------------|
| CEX | Company Experience X |
| Nucleo | Setor/departamento (7) |
| LP | Learning Pillar (12) |
| Type | Tipo de artefato (78) |
| Builder | Fabrica de 1 tipo (13 ISO files) |
| Dual | .md (humano) + compiled/.yaml (maquina) |
| Density | tokens_uteis / tokens_total (min 0.8) |
| Golden | Artefato quality >= 9.5 |

---

*CEX Whitepaper v1.0 -- A estrutura que faz a IA entender a SUA empresa.*