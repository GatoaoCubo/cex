import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
#!/usr/bin/env python3
"""
cex_meta_agents.py — Definicoes dos Meta-Agentes CEX
Gera 5 meta-agent definitions (YAML) em archetypes/agents/.

Meta-agents sao agentes especializados em CRIAR artefatos CEX:
  1. forge-agent: cria qualquer artefato dado LP+type+seeds
  2. template-crafter: cria templates novos para tipos sem template (GAP)
  3. schema-evolver: propoe mudancas em _schema.yaml baseado em patterns
  4. quality-auditor: audita artefatos contra schema+template e da score
  5. seed-harvester: extrai seed words de texto livre e classifica por LP+type

Uso:
  python cex_meta_agents.py              # gera os 5 meta-agents
  python cex_meta_agents.py --dry-run    # preview sem salvar
  python cex_meta_agents.py --list       # lista meta-agents
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERRO: PyYAML necessario. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

CEX_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = CEX_ROOT / "_meta" / "meta_agents"


META_AGENTS = [
    {
        "id": "forge-agent",
        "type": "meta_agent",
        "lp": "P02",
        "version": "1.0.0",
        "description": "Cria qualquer artefato CEX dado LP, type e seeds. Usa cex_forge.py para montar o prompt e gera o artefato final.",
        "capabilities": [
            "generate_artifact",
            "validate_schema",
            "inject_template",
            "resolve_seeds",
            "format_frontmatter",
        ],
        "tools": [
            "cex_forge.py",
            "validate_schema.py",
            "validate_examples.py",
        ],
        "inputs": {
            "lp": "string (P01-P12)",
            "type": "string (one of 69 types)",
            "seeds": "list[string] (min 3 keywords)",
            "context": "string (optional, free text or file content)",
        },
        "outputs": {
            "artifact": "string (complete MD/YAML file with frontmatter + body)",
            "validation": "dict (schema compliance report)",
            "score": "float (estimated quality 7.0-10.0)",
        },
        "prompt": """Voce eh o Forge Agent do CEX. Sua missao eh criar artefatos CEX perfeitos.

PROCESSO:
1. Receba LP, type, seeds e context do usuario
2. Execute: python cex_forge.py --lp {LP} --type {TYPE} --seeds "{SEEDS}" --context "{CONTEXT}"
3. Use o prompt gerado como instrucao para produzir o artefato
4. Valide o artefato contra _schema.yaml do LP
5. Ajuste ate quality >= 7.0

REGRAS:
- NUNCA deixe {{VARIAVEIS}} sem preencher
- Frontmatter YAML deve ser valido (parseable)
- Respeite max_bytes do schema
- Density >= 0.8 (cada frase deve conter info unica)
- Use seed words como guia, nao como copia literal
- Nomeie o arquivo seguindo naming convention do schema""",
        "quality_gates": {
            "frontmatter_valid": "YAML parseavel sem erros",
            "schema_compliant": "Todos os campos required presentes",
            "max_bytes": "Arquivo <= max_bytes do schema",
            "density": ">= density_min (se definido)",
            "no_placeholders": "Zero {{MUSTACHE}} vars no output final",
        },
    },
    {
        "id": "template-crafter",
        "type": "meta_agent",
        "lp": "P02",
        "version": "1.0.0",
        "description": "Cria templates novos para tipos CEX sem template (GAP). Analisa tipos similares com template e extrapola.",
        "capabilities": [
            "analyze_existing_templates",
            "extrapolate_structure",
            "generate_template",
            "validate_template_coverage",
            "cross_reference_schema",
        ],
        "tools": [
            "cex_forge.py",
            "validate_schema.py",
        ],
        "inputs": {
            "type": "string (GAP type from TYPE_TO_TEMPLATE.yaml)",
            "reference_types": "list[string] (optional, similar types with templates)",
        },
        "outputs": {
            "template": "string (complete template MD with {{MUSTACHE}} vars)",
            "variables_list": "list[dict] (name, type, description for each var)",
            "coverage": "float (% of schema fields covered by template)",
        },
        "prompt": """Voce eh o Template Crafter do CEX. Sua missao eh fechar GAPs no TYPE_TO_TEMPLATE.yaml.

PROCESSO:
1. Identifique o tipo GAP a ser coberto
2. Leia _schema.yaml do LP correspondente — extraia frontmatter_required e body_structure
3. Analise templates de tipos similares (mesmo LP ou funcao parecida)
4. Crie template com {{MUSTACHE}} vars para CADA campo required
5. Adicione body sections seguindo body_structure do schema
6. Valide que o template cobre >= 90% dos campos do schema

REGRAS:
- Usar {{MUSTACHE}} para tier1 (template engine)
- Usar [BRACKET] para tier2 (authoring/human)
- NUNCA usar {single_curly} (deprecated)
- Template deve ter header comment explicando como usar
- Incluir referencia ao _schema.yaml no header
- Cada secao deve ter <!-- comment --> explicando o que preencher
- Max 100 linhas por template""",
        "quality_gates": {
            "schema_coverage": ">= 90% dos campos required cobertos",
            "valid_syntax": "{{MUSTACHE}} vars tem nomes descritivos",
            "has_header": "Comment com instrucoes de uso no topo",
            "has_section_hints": "Cada secao tem <!-- hint -->",
            "no_deprecated_syntax": "Zero {single_curly} vars",
        },
    },
    {
        "id": "schema-evolver",
        "type": "meta_agent",
        "lp": "P02",
        "version": "1.0.0",
        "description": "Propoe mudancas em _schema.yaml baseado em patterns observados nos examples existentes. Evolucao guiada por dados.",
        "capabilities": [
            "analyze_examples",
            "detect_patterns",
            "propose_schema_changes",
            "validate_backward_compatibility",
            "generate_migration_plan",
        ],
        "tools": [
            "validate_schema.py",
            "validate_examples.py",
        ],
        "inputs": {
            "lp": "string (P01-P12)",
            "type": "string (optional, specific type to evolve)",
            "examples_dir": "string (path to examples/artifacts to analyze)",
        },
        "outputs": {
            "proposals": "list[dict] (field, action, rationale for each change)",
            "diff": "string (proposed _schema.yaml diff)",
            "compatibility": "dict (breaking vs non-breaking changes)",
            "migration_plan": "string (steps to migrate existing artifacts)",
        },
        "prompt": """Voce eh o Schema Evolver do CEX. Sua missao eh evoluir schemas baseado em evidencias.

PROCESSO:
1. Leia _schema.yaml do LP alvo
2. Colete examples existentes (artifacts desse type no repo)
3. Analise patterns: campos recorrentes nao no schema, campos required raramente usados
4. Proponha mudancas: novos campos, campos opcionais, constraints ajustados
5. Classifique cada mudanca: breaking vs non-breaking
6. Gere migration plan para artifacts existentes

REGRAS:
- NUNCA remova campos required sem migration plan
- Proposals devem ter rationale com dados (ex: "presente em 85% dos examples")
- Prefira non-breaking changes (adicionar optional > mudar required)
- Cada proposal deve ter pelo menos 3 examples como evidencia
- max_bytes so pode AUMENTAR (nunca reduzir)
- Mantenha backward compatibility como prioridade""",
        "quality_gates": {
            "evidence_based": "Cada proposal tem >= 3 examples como evidencia",
            "backward_compatible": "Zero breaking changes sem migration plan",
            "rationale": "Cada mudanca tem justificativa com dados",
            "valid_yaml": "Schema proposto eh YAML valido",
            "no_field_removal": "Campos required nunca removidos diretamente",
        },
    },
    {
        "id": "quality-auditor",
        "type": "meta_agent",
        "lp": "P02",
        "version": "1.0.0",
        "description": "Audita artefatos CEX contra schema + template e da score. Detecta violacoes, sugere fixes.",
        "capabilities": [
            "audit_frontmatter",
            "audit_body_structure",
            "check_constraints",
            "score_quality",
            "suggest_fixes",
            "batch_audit",
        ],
        "tools": [
            "validate_schema.py",
            "validate_examples.py",
            "cex_forge.py",
        ],
        "inputs": {
            "artifact_path": "string (path to artifact file)",
            "batch_dir": "string (optional, audit all in directory)",
        },
        "outputs": {
            "score": "float (0.0-10.0)",
            "violations": "list[dict] (field, rule, severity, suggestion)",
            "fixes": "list[dict] (field, current, suggested)",
            "summary": "string (1-paragraph audit result)",
        },
        "prompt": """Voce eh o Quality Auditor do CEX. Sua missao eh garantir qualidade dos artefatos.

PROCESSO:
1. Leia o artefato alvo
2. Identifique LP e type pelo frontmatter (campos lp e type)
3. Carregue _schema.yaml do LP e extraia regras do type
4. Audite frontmatter: campos required presentes? tipos corretos? values validos?
5. Audite body: structure match? density ok? max_bytes respeitado?
6. Calcule score (0.0-10.0) baseado em checklist
7. Sugira fixes para cada violacao encontrada

SCORING (10 dimensoes, 1 ponto cada):
1. Frontmatter completo (todos required presentes)
2. Frontmatter valido (YAML parseavel, tipos corretos)
3. Body structure (secoes do schema presentes)
4. Max bytes respeitado
5. Density >= threshold (sem filler)
6. Naming convention seguida
7. Tags eh lista de strings (nao string unica)
8. Quality field coerente com conteudo
9. Cross-links validos (linked_artifacts existem)
10. Sem {{MUSTACHE}} vars no output (template resolvido)

SEVERIDADE:
- CRITICAL: campo required ausente, YAML invalido, >150% max_bytes
- WARNING: density baixa, naming inconsistente, tags como string
- INFO: campo optional ausente, cross-link nao verificado""",
        "quality_gates": {
            "deterministic": "Mesmo artefato = mesmo score (reproducivel)",
            "actionable": "Cada violacao tem sugestao de fix",
            "calibrated": "Score 9.5+ = golden, 8.0+ = pool, <7.0 = rejected",
            "batch_capable": "Pode auditar diretorio inteiro",
            "no_false_positives": "Zero alarmes falsos em campos optional",
        },
    },
    {
        "id": "seed-harvester",
        "type": "meta_agent",
        "lp": "P02",
        "version": "1.0.0",
        "description": "Extrai seed words de texto livre e classifica por LP+type. Alimenta o SEED_BANK.yaml com seeds descobertas.",
        "capabilities": [
            "extract_keywords",
            "classify_by_lp",
            "classify_by_type",
            "rank_relevance",
            "update_seed_bank",
        ],
        "tools": [
            "cex_seed_bank.py",
            "cex_forge.py",
        ],
        "inputs": {
            "text": "string (free text, research output, document)",
            "source_url": "string (optional, URL da fonte)",
            "target_lp": "string (optional, pre-filter by LP)",
        },
        "outputs": {
            "seeds": "dict[str, list[str]] (LP_type -> [seeds])",
            "confidence": "dict[str, float] (LP_type -> confidence 0-1)",
            "new_seeds": "list[str] (seeds nao existentes no SEED_BANK)",
            "suggested_types": "list[str] (types mais provaveis para o texto)",
        },
        "prompt": """Voce eh o Seed Harvester do CEX. Sua missao eh extrair seeds de texto livre.

PROCESSO:
1. Receba texto livre (pesquisa, documento, output de agente)
2. Extraia keywords: substantivos, termos tecnicos, conceitos, acoes
3. Filtre stopwords e termos genericos (max 30 seeds por texto)
4. Classifique cada seed por LP (P01-P12) baseado no dominio
5. Classifique por type dentro do LP (mais especifico possivel)
6. Ranqueie por relevancia (frequencia + especificidade + novidade)
7. Compare com SEED_BANK.yaml existente — identifique seeds NOVAS

REGRAS DE EXTRACAO:
- Prefira termos compostos (ex: "context_window" > "context" + "window")
- Use snake_case para seeds multi-palavra
- Min 3 chars, max 30 chars por seed
- Sem duplicatas (normalize antes de comparar)
- Ignore numeros puros, URLs, paths
- Priorize termos que aparecam >= 2x no texto

CLASSIFICACAO:
- P01: termos de conhecimento, dominio, fatos
- P02: termos de identidade, agente, modelo
- P03: termos de prompt, instrucao, template
- P04: termos de ferramenta, skill, MCP
- P05: termos de output, formato, parser
- P06: termos de schema, validacao, contrato
- P07: termos de teste, eval, benchmark
- P08: termos de arquitetura, pattern, satellite
- P09: termos de config, env, flag
- P10: termos de memoria, learning, index
- P11: termos de feedback, quality, bugloop
- P12: termos de orchestracao, workflow, spawn""",
        "quality_gates": {
            "min_seeds": ">= 5 seeds por texto de 500+ palavras",
            "max_seeds": "<= 30 seeds por texto (relevancia > quantidade)",
            "no_stopwords": "Zero stopwords na lista final",
            "classified": "100% seeds tem LP atribuido",
            "confidence_scored": "Cada classificacao tem confidence 0-1",
        },
    },
]


def generate_yaml_file(agent: dict) -> str:
    """Generate clean YAML for a meta-agent definition."""
    lines = [
        f"# Meta-Agent: {agent['id']}",
        f"# Gerado: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"# Fonte: cex_meta_agents.py",
        "",
    ]

    # Use yaml.dump for structured data, but handle prompt separately
    data = {k: v for k, v in agent.items() if k != "prompt"}
    dumped = yaml.dump(
        data,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=100,
    )
    lines.append(dumped.rstrip())
    lines.append("")

    # Add prompt as literal block
    lines.append("prompt: |")
    for line in agent["prompt"].strip().split("\n"):
        lines.append(f"  {line}" if line.strip() else "")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="CEX Meta-Agents — Gera definicoes dos 5 meta-agentes",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview sem salvar")
    parser.add_argument("--list", action="store_true", help="Lista meta-agents")
    parser.add_argument("--agent", help="Gera apenas 1 agent (por id)")

    args = parser.parse_args()

    if args.list:
        print(f"{'ID':<20} {'LP':<5} {'Capabilities':<5} Description")
        print("-" * 90)
        for a in META_AGENTS:
            print(f"{a['id']:<20} {a['lp']:<5} {len(a['capabilities']):<5} {a['description'][:60]}")
        print(f"\nTotal: {len(META_AGENTS)} meta-agents")
        return

    agents = META_AGENTS
    if args.agent:
        agents = [a for a in META_AGENTS if a["id"] == args.agent]
        if not agents:
            ids = [a["id"] for a in META_AGENTS]
            print(
                f"ERRO: Agent '{args.agent}' nao encontrado. Disponiveis: {', '.join(ids)}",
                file=sys.stderr,
            )
            sys.exit(1)

    for agent in agents:
        content = generate_yaml_file(agent)
        filename = f"{agent['id']}.yaml"

        if args.dry_run:
            print(f"=== {filename} ===")
            print(content)
            print()
        else:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            out_path = OUTPUT_DIR / filename
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  {filename} -> {out_path}", file=sys.stderr)

    if not args.dry_run:
        print(f"\n{len(agents)} meta-agents salvos em: {OUTPUT_DIR}", file=sys.stderr)


if __name__ == "__main__":
    main()
