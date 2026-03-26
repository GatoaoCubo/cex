# CEX Quick Start — Primeiro Artefato em 5 Minutos

---

## Passo 1: Bootstrap

```bash
cd cex/
python _tools/bootstrap.py --name MeuProjeto --lps P01,P02,P03 --with-examples
```

Output: `MeuProjeto/` com schemas, generators, templates e examples prontos.

Para todos os 12 LPs:
```bash
python _tools/bootstrap.py --name MeuProjeto
```

## Passo 2: Escolher Pillar + Tipo

Abra o schema do Pillar desejado:
```bash
cat MeuProjeto/P01_knowledge/_schema.yaml
```

Tipos disponiveis em P01:
- `knowledge_card` — fato atomico pesquisavel (density > 0.8)

Cada tipo define: naming, constraints (max_bytes, density_min), frontmatter obrigatorio.

## Passo 3: Ler Generator

```bash
cat MeuProjeto/P01_knowledge/_generator.md
```

O generator contem:
- QUANDO USAR este Pillar
- PASSO A PASSO (10 steps)
- TESTE DE ESPECIFICIDADE
- ANTI-PATTERNS a evitar

## Passo 4: Usar Template

```bash
cp MeuProjeto/P01_knowledge/templates/tpl_knowledge_card_domain.md \
   MeuProjeto/P01_knowledge/meu_primeiro_kc.md
```

Preencher:
1. YAML frontmatter (id, type, lp, quality, keywords, long_tails, bullets, axioms)
2. MD body (title, summary, secoes por tipo)
3. Substituir `{{MUSTACHE}}` com valores reais
4. Substituir `[BRACKET]` com decisoes do autor

## Passo 5: Validar

Checklist manual:
- [ ] Frontmatter YAML completo (todos campos obrigatorios)
- [ ] Density >= 0.8 (sem prosa > 3 linhas, bullets max 80 chars)
- [ ] Naming segue pattern: `p01_kc_{{topic}}.md`
- [ ] Max 4KB
- [ ] Teste de especificidade: cada frase permite agir sem docs externos?

Com validadores (se `--with-tools`):
```bash
python MeuProjeto/_tools/validate_schema.py
```

---

## Exemplo Concreto: Knowledge Card

**Input**: Preciso documentar estrategia de Buy Box no Mercado Livre.

**Resultado**:

```yaml
# p01_kc_buybox_ml.yaml
id: p01_kc_buybox_ml
kind: knowledge_card
pillar: P01
title: "Buy Box Algorithm - Mercado Livre"
version: "1.0.0"
created: "2026-03-22"
author: human
domain: e-commerce
quality: 8.5
tags: [buybox, mercado-livre, algoritmo]
keywords: [buy box, mercado livre, full]
long_tails:
  - "como ganhar buy box mercado livre"
  - "fatores algoritmo buy box ml"
bullets:
  - "Logistics 40%: Full > Flex > Proprio"
  - "Price 30%: menor preco com frete gratis"
  - "Reputation 20%: verde > amarelo, cancelamento < 2%"
  - "History 10%: vendas ultimos 60 dias"
axioms:
  - "Full + menor preco = buy box garantido em 90% dos casos"
```

```markdown
# p01_kc_buybox_ml.md
# Buy Box Algorithm - Mercado Livre

Fatores do algoritmo de Buy Box do ML com pesos reais.

## Quick Reference
- Full > Flex > Proprio (40% do score)
- Menor preco com frete gratis (30%)
- Reputacao verde obrigatoria (20%)
- Historico 60 dias (10%)

## Regras de Ouro
- Full + menor preco = 90% win rate
- Cancelamento > 2% = perde buy box por 30 dias
- Frete gratis obrigatorio acima de R$79
```

---

## Proximo Passo

- Criar mais artefatos seguindo o mesmo flow
- Explorar P02 (agents), P03 (prompts), P04 (tools)
- Ler `archetypes/CODEX.md` para regras completas
- Consultar examples/ para referencia (use `--with-examples`)

---
*CEX Quick Start v1.0*
