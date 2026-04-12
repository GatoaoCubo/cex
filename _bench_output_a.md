---
id: bench_a
kind: knowledge_card
title: Prompt Caching
version: 1.0.0
quality: null
---

**Prompt Caching** é uma técnica para armazenar respostas anteriores a prompts, reduzindo custos e acelerando respostas futuras. Estratégias comuns:

1. **TTL (Time-to-Live)**  
   - *Descrição*: Respostas são armazenadas por um tempo fixo.  
   - *Casos de uso*: Tráfego previsível ou quando frescor é crítico.  
   - *Vantagens*: Simples e eficiente para padrões de uso previsíveis.  
   - *Desvantagens*: Pode obsolecer dados rapidamente.

2. **LRU (Least Recently Used)**  
   - *Descrição*: Remove a resposta menos recentemente usada quando a memória é limitada.  
   - *Casos de uso*: Ambientes com memória limitada e padrões de uso variáveis.  
   - *Vantagens*: Eficiente em memória e adapta-se a mudanças.  
   - *Desvantagens*: Pode descartar respostas úteis em padrões não previsíveis.

3. **Semântico**  
   - *Descrição*: Armazena respostas com base em similaridade de conteúdo.  
   - *Casos de uso*: Consultas complexas (chatbots, Q&A).  
   - *Vantagens*: Alta relevância para consultas semelhantes.  
   - *Desvantagens*: Mais complexo e demanda recursos de processamento.

| Estratégia | Descrição               | Caso de Uso                  | Vantagens                     | Desvantagens               |
|------------|-------------------------|-----------------------------|-------------------------------|---------------------------|
| TTL        | Tempo fixo de validade  | Tráfego previsível          | Simples, eficiente            | Risco de obsolescência    |
| LRU        | Memória limitada        | Uso variável                | Adapta-se a mudanças          | Pode descartar respostas úteis |
| Semântico  | Similaridade de conteúdo| Consultas complexas         | Alta relevância               | Complexo, demanda recursos |
