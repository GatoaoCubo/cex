---
id: bench_a
kind: knowledge_card
title: Prompt Caching
version: 1.0.0
quality: null
---

**Prompt Caching** é uma técnica para armazenar respostas anteriores a prompts, reduzindo custos e acelerando respostas futuras. Estratégias comuns incluem:

### 1. **TTL (Time-to-Live)**
- **Mecanismo**: Cache por tempo fixo.
- **Casos de uso**: Trabalhos com padrões repetitivos (ex: consultas frequentes).
- **Performance**: Alta velocidade, mas pode acumular dados obsoletos.

### 2. **LRU (Least Recently Used)**
- **Mecanismo**: Evicta o menos recentemente usado.
- **Casos de uso**: Dados dinâmicos com prioridade para novos (ex: logs em tempo real).
- **Performance**: Balanceia memória e relevância.

### 3. **Semântico**
- **Mecanismo**: Compara semelhança de conteúdo.
- **Casos de uso**: Consultas complexas (ex: chatbots com contexto).
- **Performance**: Alta precisão, mas mais computacional.

| Estratégia | Mecanismo       | Caso de Uso               | Performance       |
|------------|-----------------|---------------------------|-------------------|
| TTL        | Tempo fixo      | Padrões repetitivos       | Alta velocidade   |
| LRU        | Memória         | Dados dinâmicos           | Balanceada        |
| Semântico  | Similaridade    | Consultas complexas       | Alta precisão     |
