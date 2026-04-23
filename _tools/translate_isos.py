#!/usr/bin/env python3
"""
Translate Portuguese ISOs to English -- v2 (comprehensive pass).
N03 Builder Nucleus -- CEX ISO Translation Engine
Fixes: word ordering, missing vocabulary, full coverage.
"""
import os
import sys

# --- PHRASES: ordered LONGEST FIRST, then by specificity ---
# CRITICAL: "Produzir" MUST come before "Produz" etc.
PHRASES = [
    # --- Multi-word phrases (longest first) ---
    ("Especialista em construir", "Specialist in building"),
    ("Sabe tudo sobre", "Knows everything about"),
    ("Conhece padroes de", "Knows patterns o"),

    # --- "Produzir" variants (BEFORE "Produz") ---
    ("Produzir knowledge_card com frontmatter completo", "Produce knowledge_card with complete frontmatter"),
    ("Produzir model_card com frontmatter completo", "Produce model_card with complete frontmatter"),
    ("Produzir agent artifact com frontmatter completo", "Produce agent artifact with complete frontmatter"),
    ("Produzir chain com frontmatter completo", "Produce chain with complete frontmatter"),
    ("Produzir workflow com frontmatter completo", "Produce workflow with complete frontmatter"),
    ("Produzir skill com frontmatter completo", "Produce skill with complete frontmatter"),
    ("Produzir supervisor artifact com frontmatter completo", "Produce supervisor artifact with complete frontmatter"),
    ("Produzir router artifact com frontmatter completo", "Produce router artifact with complete frontmatter"),
    ("Produzir pattern artifacts com frontmatter completo", "Produce pattern artifacts with complete frontmatter"),
    ("Produzir guardrail com scope, rules, severity, e bypass policy",
     "Produce guardrail with scope, rules, severity, and bypass policy"),
    ("Produzir signals JSON com campos minimos e naming P12 corretos",
     "Produce JSON signals with minimal fields and correct P12 naming"),
    ("Produzir HARD gates (block) e SOFT gates (score contribution)",
     "Produce HARD gates (block) and SOFT gates (score contribution)"),
    ("Produzir", "Produce"),

    # --- "Produz" variants (AFTER "Produzir") ---
    ("Producesir", "Produce"),  # Fix v1 artifact first!
    ("Produces cards com dados concretos", "Produces cards with concrete data"),
    ("Produces cards with dados concretos", "Produces cards with concrete data"),
    ("Produz cards com dados concretos", "Produces cards with concrete data"),
    ("Produces agents densos com frontmatter completo e agent_package navegavel",
     "Produces dense agents with complete frontmatter and navigable agent_package"),
    ("Produz agents densos com frontmatter completo e agent_package navegavel",
     "Produces dense agents with complete frontmatter and navigable agent_package"),
    ("Produces directors densos com frontmatter completo e topologia de waves documentada",
     "Produces dense directors with complete frontmatter and documented wave topology"),
    ("Produz directors densos com frontmatter completo e topologia de waves documentada",
     "Produces dense directors with complete frontmatter and documented wave topology"),
    ("Produces routers densos que direcionam tasks para o destino correto baseado em patterns, prioridades, e confianca",
     "Produces dense routers that direct tasks to the correct destination based on patterns, priorities, and confidence"),
    ("Produz routers densos que direcionam tasks para o destino correto baseado em patterns, prioridades, e confianca",
     "Produces dense routers that direct tasks to the correct destination based on patterns, priorities, and confidence"),
    ("Produces payloads JSON curtos para", "Produces short JSON payloads for"),
    ("Produz payloads JSON curtos para", "Produces short JSON payloads for"),
    ("Produces patterns densos", "Produces dense patterns"),
    ("Produz patterns densos", "Produces dense patterns"),
    ("Produces skills densas com frontmatter completo e fases atomicas",
     "Produces dense skills with complete frontmatter and atomic phases"),
    ("Produz skills densas com frontmatter completo e fases atomicas",
     "Produces dense skills with complete frontmatter and atomic phases"),
    ("Produces daemon artifacts com frontmatter completo, lifecycle definido, e monitoring configurado",
     "Produces daemon artifacts with complete frontmatter, defined lifecycle, and configured monitoring"),
    ("Produz daemon artifacts com frontmatter completo, lifecycle definido, e monitoring configurado",
     "Produces daemon artifacts with complete frontmatter, defined lifecycle, and configured monitoring"),
    ("Produces", "Produces"),  # Keep as-is (already English)
    ("Produz", "Produces"),

    # --- Capability verbs (alphabetical, longest match first) ---
    ("Pesquisar e destilar conhecimento de qualquer dominio em fato atomico",
     "Research and distill knowledge from any domain into atomic facts"),
    ("Pesquisar specs de qualquer LLM", "Research specs of any LLM"),
    ("Pesquisar dominio do agente-alvo para definir persona, capabilities, e constraints",
     "Research the target agent domain to define persona, capabilities, and constraints"),
    ("Pesquisar dominio do supervisor-alvo para definir builders participantes, dependencias e wave topology",
     "Research the target supervisor domain to define participating builders, dependencies, and wave topology"),
    ("Research domain do agente-alvo for definir persona, capabilities, e constrain",
     "Research the target agent domain to define persona, capabilities, and constraints"),
    ("Pesquisar", "Research"),

    ("Analisar dominios de task e requisitos de roteamento para desenhar route tables",
     "Analyze task domains and routing requirements to design route tables"),
    ("Analisar dominio da habilidade para decompor em fases executaveis com trigger definido",
     "Analyze the skill domain to decompose into executable phases with defined trigger"),
    ("Analisar dominio da habilidade para decompor em fases executaveis",
     "Analyze the skill domain to decompose into executable phases"),
    ("Analisar", "Analyze"),

    ("Decompor missoes complexas em steps com agentes e dependencias",
     "Decompose complex missions into steps with agents and dependencies"),
    ("Decompor tarefas complexas em steps atomicos de prompt",
     "Decompose complex tasks into atomic prompt steps"),
    ("Decompose tasks complexas em steps atomicos e sequenciais",
     "Decompose complex tasks into atomic and sequential steps"),
    ("Decompor", "Decompose"),

    ("Definir data flow e context passing entre steps com tipos explicitos",
     "Define data flow and context passing between steps with explicit types"),
    ("Definir execucao sequencial, paralela, ou mixed com wave ordering",
     "Define sequential, parallel, or mixed execution with wave ordering"),
    ("Definir quality gates com metricas concretas e thresholds",
     "Define quality gates with concrete metrics and thresholds"),
    ("Definir restricoes de seguranca com enforcement concreto",
     "Define security restrictions with concrete enforcement"),
    ("Definir fallback routes e escalation logic para requests sem match",
     "Define fallback routes and escalation logic for unmatched requests"),
    ("Definir trigger preciso", "Define precise trigger"),
    ("Definir processo background com schedule e restart policy",
     "Define background process with schedule and restart policy"),
    ("Definir monitoring strategy", "Define monitoring strategy"),
    ("Definir wave topology com dependencias entre waves e builders por wave",
     "Define wave topology with dependencies between waves and builders per wave"),
    ("Definir bypass policies e audit trails", "Define bypass policies and audit trails"),
    ("Definir prompts de acao com input/output contracts claros",
     "Define action prompts with clear input/output contracts"),
    ("Define references with URL, reliability tier, e excerpt",
     "Define references with URL, reliability tier, and excerpt"),
    ("Define perspectivas with foco, filtros e bias declarados",
     "Define perspectives with focus, filters, and declared bias"),
    ("Define enumeracao with values finitos e nomeados",
     "Define enumeration with finite named values"),
    ("Definir", "Define"),

    ("Especificar error handling strategy", "Specify error handling strategy"),
    ("Especificar signals de completion/error por step", "Specify completion/error signals per step"),
    ("Especificar enforcement mode", "Specify enforcement mode"),
    ("Especificar edge cases e constraints para execucao robusta",
     "Specify edge cases and constraints for robust execution"),
    ("Especificar signal handling", "Specify signal handling"),
    ("Especificar", "Specify"),

    ("Mapear related_patterns e anti_patterns com cross-references",
     "Map related_patterns and anti_patterns with cross-references"),
    ("Mapear boundaries", "Map boundaries"),
    ("Mapear", "Map"),

    ("Classificar KC como domain_kc ou meta_kc e aplicar body structure correto",
     "Classify KC as domain_kc or meta_kc and apply correct body structure"),
    ("Classificar severity", "Classify severity"),
    ("Classificar", "Classify"),

    ("Documentar violacoes com exemplos concretos", "Document violations with concrete examples"),
    ("Documentar problem, solution, forces, consequences, e applicability",
     "Document problem, solution, forces, consequences, and applicability"),
    ("Documentar", "Document"),

    ("Recomendar modelo ideal dado um use case", "Recommend the ideal model for a use case"),
    ("Recomendar", "Recommend"),

    ("Gerar agent_package skeleton com 10 required builder specs",
     "Generate agent_package skeleton with 10 required builder specs"),
    ("Gerar", "Generate"),

    ("Calibrar nivel de detalhe entre concisao e completude",
     "Calibrate detail level between conciseness and completeness"),
    ("Calibrar", "Calibrate"),

    ("Posicionar agente no mapa de agent_groups e routing",
     "Position agent in the agent_group map and routing"),
    ("Posicionar", "Position"),

    ("Detectar boundary violations", "Detect boundary violations"),
    ("Detectar", "Detect"),

    ("Distinguir signal de handoff e dispatch_rule sem sobreposicao",
     "Distinguish signal from handoff and dispatch_rule without overlap"),
    ("Distinguir user_invocable (slash command) de agent-only (programmatic call)",
     "Distinguish user_invocable (slash command) from agent-only (programmatic call)"),
    ("Distinguir router de dispatch_rule", "Distinguish router from dispatch_rule"),
    ("Distinguir daemon de hook, skill, cli_tool, workflow, connector",
     "Distinguish daemon from hook, skill, cli_tool, workflow, connector"),
    ("Distinguir pattern de law (inviolavel) e workflow (executavel)",
     "Distinguish pattern from law (inviolable) and workflow (executable)"),
    ("Distinguir", "Distinguish"),

    ("Integrar spawn_config por agent_group", "Integrate spawn_config per agent_group"),
    ("Configurar health_check, PID file management, e resource limits",
     "Configure health_check, PID file management, and resource limits"),
    ("Configurar fallback_per_builder para resiliencia de dispatch",
     "Configure fallback_per_builder for dispatch resilience"),
    ("Configurar confidence thresholds, load balancing, e timeout policies",
     "Configure confidence thresholds, load balancing, and timeout policies"),
    ("Configurar", "Configure"),

    ("Compor scoring formulas com pesos por dimensao",
     "Compose scoring formulas with weights per dimension"),
    ("Modelar payload minimo e extensoes opcionais sem quebrar consumidores",
     "Model minimal payload and optional extensions without breaking consumers"),
    ("Estruturar phases com input/output claros por fase",
     "Structure phases with clear input/output per phase"),

    # Validate phrases
    ("Validar card contra validate_kc.py v2.0", "Validate card against validate_kc.py v2.0"),
    ("Validate artifact against quality gates", "Validate artifact against quality gates"),
    ("Validar artifact contra quality gates", "Validate artifact against quality gates"),
    ("Validar sinais contra gates duros de naming, status e timestamp",
     "Validate signals against hard gates for naming, status, and timestamp"),
    ("Validar", "Validate"),

    ("Define validation criteria for verificar output quality",
     "Define validation criteria to verify output quality"),

    # --- Domina phrases ---
    ("Domina agent identity design", "Masters agent identity design"),
    ("Domina prompt chaining, composicao sequencial", "Masters prompt chaining, sequential composition"),
    ("Domina prompt engineering conversacional", "Masters conversational prompt engineering"),
    ("Domina restart policies", "Masters restart policies"),
    ("Domina wave planning", "Masters wave planning"),
    ("Domina lifecycle design", "Masters lifecycle design"),
    ("Domina", "Masters"),

    # --- Complex noun phrases ---
    ("fatos atomicos pesquisaveis", "searchable atomic facts"),
    ("fato atomico", "atomic fact"),
    ("barreiras de qualidade com score numerico", "quality barriers with numeric scoring"),
    ("restricoes de seguranca e safety boundaries aplicadas a agentes e artefatos",
     "security restrictions and safety boundaries applied to agents and artifacts"),
    ("restricoes de seguranca", "security restrictions"),
    ("sequencias de prompts encadeados onde output A eh input B",
     "sequences of chained prompts where output A becomes input B"),
    ("sequencias de prompts encadeados", "sequences of chained prompts"),
    ("fluxos de trabalho com steps sequenciais e/ou paralelos que orquestram agentes, tools, e signals em runtime",
     "workflows with sequential and/or parallel steps that orchestrate agents, tools, and signals at runtime"),
    ("fluxos de trabalho com steps sequenciais", "workflows with sequential steps"),
    ("habilidades reutilizaveis com fases estruturadas e trigger definido",
     "reusable skills with structured phases and defined trigger"),
    ("habilidades reutilizaveis com fases estruturadas", "reusable skills with structured phases"),
    ("solucoes reutilizaveis de arquitetura nomeadas", "named reusable architecture solutions"),
    ("solucoes reutilizaveis de arquitetura nomea", "named reusable architecture solution"),
    ("solucoes recorrentes de arquitetura", "recurring architecture solutions"),
    ("processos background persistentes que executam continuamente ou em schedule",
     "persistent background processes that run continuously or on schedule"),
    ("processos background persistentes q", "persistent background processes that"),
    ("orquestradores de crew que despacham, sequenciam e coletam resultados sem executar tarefas",
     "crew orchestrators that dispatch, sequence, and collect results without executing tasks"),
    ("orquestradores de crew que coordenam multiplos builders sem executar tarefas diretamente",
     "crew orchestrators that coordinate multiple builders without directly executing tasks"),
    ("logica de roteamento task-to-agent_group com", "task-to-agent_group routing logic with"),
    ("prompts de acao task-focused com input/output", "task-focused action prompts with input/output"),
    ("prompts de acao task-focused com inpu", "task-focused action prompts with inpu"),
    ("prompts de acao", "action prompts"),
    ("definicoes completas de agente", "complete agent definitions"),
    ("eventos atomicos entre agentes", "atomic events between agents"),
    ("eventos atomicos emitidos", "atomic events emitted"),
    ("specs tecnicas de LLMs", "technical specs of LLMs"),
    ("specs tecnicas de LLM", "technical specs of LLMs"),

    # --- Domain-specific PT phrases (from various builders) ---
    ("configuracoes de inicializac", "initialization configurations"),
    ("configuracoes de inicializacao", "initialization configurations"),
    ("atribuicoes de fonte estruturadas with proveniencia", "structured source attributions with provenance"),
    ("atribuicoes de fonte estruturadas", "structured source attributions"),
    ("documentos de contexto de domain for h", "domain context documents for h"),
    ("documentos de contexto de domain", "domain context documents"),
    ("documentos de contexto", "context documents"),
    ("grafos aciclicos de dependencies", "acyclic dependency graphs"),
    ("grafos aciclicos de dependencias", "acyclic dependency graphs"),
    ("grafos aciclicos", "acyclic graphs"),
    ("regras de despacho that mapeiam", "dispatch rules that map"),
    ("regras de despacho", "dispatch rules"),
    ("testes end-to-end that verificam pipelines", "end-to-end tests that verify pipelines"),
    ("testes end-to-end", "end-to-end tests"),
    ("enumeracoes reutilizaveis with conjuntos", "reusable enumerations with sets"),
    ("enumeracoes reutilizaveis", "reusable enumerations"),
    ("registros de aprendizado persistentes", "persistent learning records"),
    ("registros de aprendizado", "learning records"),
    ("perspectivas especializadas aplicadas a artefatos", "specialized perspectives applied to artifacts"),
    ("perspectivas especializadas", "specialized perspectives"),
    ("receitas operacionais passo-a-passo par", "step-by-step operational recipes for"),
    ("receitas operacionais passo-a-passo", "step-by-step operational recipes"),
    ("receitas operacionais", "operational recipes"),
    ("instructions completes de delegacao", "complete delegation instructions"),
    ("instructions de delegacao", "delegation instructions"),
    ("entidades nomeadas (pessoas, tools, conceitos, organizacoes, projetos, servicos)",
     "named entities (people, tools, concepts, organizations, projects, services)"),
    ("entidades nomeadas", "named entities"),
    ("mapas cognitivos de d", "cognitive maps of d"),
    ("mapas cognitivos", "cognitive maps"),
    ("empacotam task, contexto, escopo e regras de commit for agent_groups executarem",
     "package task, context, scope, and commit rules for agent_groups to execute"),
    ("empacotam task, contexto, escopo", "package task, context, scope"),

    # Dispatch rule specific
    ("Produce dispatch_rules with fields minimos e naming P12 corrects",
     "Produce dispatch_rules with minimal fields and correct P12 naming"),
    ("Produce handoff markdown with fields mandatorys e naming P12 corrects",
     "Produce handoff markdown with mandatory fields and correct P12 naming"),
    ("Produce dag YAML with nodes, edges e topological order corrects",
     "Produce dag YAML with nodes, edges, and correct topological order"),
    ("Produce e2e_eval with stages, data_fixtures e expected_output complete",
     "Produce e2e_eval with stages, data_fixtures, and complete expected_output"),
    ("Produce context_doc with frontmatter complete e all os fields mandatorys",
     "Produce context_doc with complete frontmatter and all mandatory fields"),
    ("Produce rollback policies alinhadas with fix strategy",
     "Produce rollback policies aligned with fix strategy"),

    # --- Boundary/distinction phrases ---
    ("fronteira exata entre", "exact boundary between"),
    ("diferenca entre", "difference between"),
    ("e a distincao entre", "and the distinction between"),
    ("and the distinction between", "and the distinction between"),
    ("e a fronteira entre", "and the boundary between"),
    ("e a boundary entre", "and the boundary between"),
    ("sem sobreposicao", "without overlap"),

    # --- Common adjective/adverb phrases ---
    ("alta densidade", "high density"),
    ("densidade informacional", "information density"),
    ("destilacao de conhecimento", "knowledge distillation"),
    ("frontmatter semantico", "semantic frontmatter"),
    ("validacao via", "validation via"),
    ("data flow tipado entre steps", "typed data flow between steps"),
    ("composicao sequencial", "sequential composition"),
    ("com semantica operacional clara e baixo overhead",
     "with clear operational semantics and low overhead"),
    ("solucao recorrente", "recurring solution"),
    ("regra inviolavel", "inviolable rule"),
    ("execucao multi-step", "multi-step execution"),
    ("prontos para deploy", "ready for deployment"),
    ("prontos para dispatch", "ready for dispatch"),
    ("escopo mais amplo", "broader scope"),
    ("criteria definidos", "defined criteria"),
    ("scale declarada", "declared scale"),
    ("tools_provided e resources_provided definidos", "defined tools_provided and resources_provided"),

    # --- Meta ISO comments ---
    ("Este meta-file gera o", "This meta-file generates the"),
    ("de qualquer builder", "of any builder"),
    ("INPUT OBRIGATORIO", "REQUIRED INPUT"),
    ("NOTA:", "NOTE:"),
    ("kebab-case do tipo", "kebab-case of the type"),
    ("snake_case do tipo", "snake_case of the type"),
    ("Pillar do tipo-alvo", "Pillar of the target type"),
    ("geralmente igual a", "usually same as"),
    ("mas pode variar", "but may vary"),
    ("termos de routing/search", "routing/search terms"),
    ("frases naturais que ativam este builder", "natural phrases that activate this builder"),
    ("frases naturais que um user diria", "natural phrases a user would say"),
    ("camadas semanticas", "semantic layers"),
    ("Extrair do", "Extract from"),
    ("extrair de", "extract from"),
    ("Buscar em", "Look up in"),
    ("Buscar confusoes em", "Look up confusions in"),
    ("Acrescente", "Add"),
    ("frases sobre dominio, ferramentas, e o que produz",
     "sentences about domain, tools, and what it produces"),
    ("bullets descrevendo o que o builder PODE fazer",
     "bullets describing what the builder CAN do"),
    ("Padrao observado nos 4 builders existentes",
     "Pattern observed in the 4 existing builders"),
    ("contar campos em", "count fields in"),
    ("definir em", "define in"),
    ("Manter body sincronizado com frontmatter",
     "Keep body synchronized with frontmatter"),
    ("papel em CAPS", "role in CAPS"),
    ("tipos vizinhos no mesmo Pillar ou frequentemente confundidos",
     "neighboring types in the same Pillar or frequently confused"),
    ("o que o tipo EH em uma frase densa", "what the type IS in a dense sentence"),
    ("tipos confundidos", "confused types"),

    # --- Boundary table terms ---
    ("NAO EH:", "IS NOT:"),
    ("EH:", "IS:"),
    ("Por que NAO", "Why NOT"),
    ("Type correto", "Correct type"),
    ("Confusao", "Confusion"),
    ("QUAL modelo/thinking usar", "WHICH model/thinking to use"),
]

# --- Individual word translations (applied AFTER phrases) ---
# Sorted: longer words first to avoid substring collisions
WORDS = [
    # Multi-syllable words (longer first)
    ("organizacoes", "organizations"),
    ("configuracoes", "configurations"),
    ("configuracao", "configuration"),
    ("enumeracoes", "enumerations"),
    ("enumeracao", "enumeration"),
    ("inicializacao", "initialization"),
    ("especializadas", "specialized"),
    ("especificas", "specific"),
    ("especifiess", "specific"),
    ("especifica", "specifies"),
    ("reutilizaveis", "reusable"),
    ("reutilizavel", "reusable"),
    ("persistentes", "persistent"),
    ("orquestradores", "orchestrators"),
    ("operacionais", "operational"),
    ("atribuicoes", "attributions"),
    ("proveniencia", "provenance"),
    ("perspectivas", "perspectives"),
    ("dependencias", "dependencies"),
    ("dependencia", "dependency"),
    ("documentacao", "documentation"),
    ("comunicacao", "communication"),
    ("verificacao", "verification"),
    ("colaboracao", "collaboration"),
    ("passo-a-passo", "step-by-step"),
    ("conversacional", "conversational"),
    ("sequenciais", "sequential"),
    ("informacional", "informational"),
    ("aprendizado", "learning"),
    ("restricoes", "restrictions"),
    ("restricao", "restriction"),
    ("definicoes", "definitions"),
    ("definicao", "definition"),
    ("aplicacao", "application"),
    ("validacao", "validation"),
    ("composicao", "composition"),
    ("descricao", "description"),
    ("verificar", "verify"),
    ("empacotam", "package"),
    ("construir", "build"),
    ("sequenciam", "sequence"),
    ("executarem", "execute"),
    ("executar", "execute"),
    ("artefatos", "artifacts"),
    ("artefato", "artifact"),
    ("cognitivos", "cognitive"),
    ("cognitivo", "cognitive"),
    ("estruturadas", "structured"),
    ("estruturada", "structured"),
    ("nomeadas", "named"),
    ("nomeados", "named"),
    ("nomeada", "named"),
    ("nomeado", "named"),
    ("aplicadas", "applied"),
    ("aplicada", "applied"),
    ("alinhadas", "aligned"),
    ("alinhada", "aligned"),
    ("definidos", "defined"),
    ("definido", "defined"),
    ("declarada", "declared"),
    ("declarado", "declared"),
    ("declarados", "declared"),
    ("injetados", "injected"),
    ("injetado", "injected"),
    ("encadeados", "chained"),
    ("encadeado", "chained"),
    ("delegacao", "delegation"),
    ("instrucao", "instruction"),
    ("instrucoes", "instructions"),
    ("operacao", "operation"),
    ("operacoes", "operations"),
    ("funcao", "function"),
    ("funcoes", "functions"),
    ("criacao", "creation"),
    ("analise", "analysis"),
    ("pesquisa", "research"),
    ("execucao", "execution"),
    ("distincao", "distinction"),
    ("concisao", "conciseness"),
    ("completude", "completeness"),
    ("reusable", "reusable"),
    ("navegavel", "navigable"),
    ("pesquisavel", "searchable"),
    ("pesquisaveis", "searchable"),
    ("inviolavel", "inviolable"),
    ("executavel", "executable"),
    ("recorrente", "recurring"),
    ("recorrentes", "recurring"),
    ("estruturado", "structured"),
    ("complexas", "complex"),
    ("complexa", "complex"),
    ("complexos", "complex"),
    ("complexo", "complex"),
    ("atomicos", "atomic"),
    ("atomicas", "atomic"),
    ("atomico", "atomic"),
    ("atomica", "atomic"),
    ("concretos", "concrete"),
    ("concretas", "concrete"),
    ("concreto", "concrete"),
    ("concreta", "concrete"),
    ("corretos", "correct"),
    ("correta", "correct"),
    ("correto", "correct"),
    ("completos", "complete"),
    ("completas", "complete"),
    ("completo", "complete"),
    ("completa", "complete"),
    ("completes", "complete"),
    ("mandatorys", "mandatory"),
    ("mandatorio", "mandatory"),
    ("obrigatorio", "mandatory"),
    ("minimos", "minimal"),
    ("minimo", "minimal"),
    ("explicitos", "explicit"),
    ("explicito", "explicit"),
    ("paralelos", "parallel"),
    ("paralelo", "parallel"),
    ("sequencial", "sequential"),
    ("sequencia", "sequence"),
    ("multiplos", "multiple"),
    ("multiplo", "multiple"),
    ("finitos", "finite"),
    ("densidade", "density"),
    ("destilacao", "distillation"),
    ("conhecimento", "knowledge"),
    ("governanca", "governance"),
    ("seguranca", "security"),
    ("estrategia", "strategy"),
    ("identidade", "identity"),
    ("qualidade", "quality"),
    ("ferramenta", "tool"),
    ("ferramentas", "tools"),
    ("bibliotecas", "libraries"),
    ("biblioteca", "library"),
    ("dependencia", "dependency"),
    ("requisitos", "requirements"),
    ("requisito", "requirement"),
    ("metricas", "metrics"),
    ("metrica", "metric"),
    ("conceitos", "concepts"),
    ("conceito", "concept"),
    ("contexto", "context"),
    ("provedores", "providers"),
    ("provedor", "provider"),
    ("projetos", "projects"),
    ("projeto", "project"),
    ("servicos", "services"),
    ("servico", "service"),
    ("processo", "process"),
    ("processos", "processes"),
    ("habilidade", "skill"),
    ("habilidades", "skills"),
    ("agent_groups", "agent_groups"),
    ("agent_group", "agent_group"),
    ("roteamento", "routing"),
    ("despacho", "dispatch"),
    ("violacoes", "violations"),
    ("violacao", "violation"),
    ("enumeracao", "enumeration"),
    ("registros", "records"),
    ("registro", "record"),
    ("dominio", "domain"),
    ("dominios", "domains"),
    ("pilares", "pillars"),
    ("pilar", "pillar"),
    ("esquema", "schema"),
    ("exemplos", "examples"),
    ("exemplo", "example"),
    ("modelos", "models"),
    ("modelo", "model"),
    ("missoes", "missions"),
    ("missao", "mission"),
    ("memoria", "memory"),
    ("memorias", "memories"),
    ("tarefas", "tasks"),
    ("tarefa", "task"),
    ("campos", "fields"),
    ("campo", "field"),
    ("regras", "rules"),
    ("regra", "rule"),
    ("valores", "values"),
    ("valor", "value"),
    ("tipos", "types"),
    ("tipo", "type"),
    ("pesos", "weights"),
    ("peso", "weight"),
    ("escopo", "scope"),
    ("agentes", "agents"),
    ("agente", "agent"),
    ("fases", "phases"),
    ("fase", "phase"),
    ("nodes", "nodes"),
    ("fatos", "facts"),
    ("fato", "fact"),
    ("dados", "data"),
    ("dado", "data"),
    ("nomes", "names"),
    ("nome", "name"),
    ("mapas", "maps"),
    ("mapa", "map"),
    # Verbs remaining
    ("mapeiam", "map"),
    ("verificam", "verify"),
    ("executam", "execute"),
    ("orquestram", "orchestrate"),
    ("direcionam", "direct"),
    ("empacota", "packages"),
    ("sobreposicao", "overlap"),
    # Short connectors (careful -- context-dependent)
    (" corrects", " correct"),  # Fix v1 pluralization artifact
]

# --- Trigger/keyword Portuguese->English ---
TRIGGER_TRANSLATIONS = {
    "documenta conhecimento X": "document knowledge X",
    "cria KC sobre Y": "create KC about Y",
    "destila fato Z": "distill fact Z",
    "documenta modelo X": "document model X",
    "qual modelo usar": "which model to use",
    "spec do LLM": "LLM spec",
    "emite signal": "emit signal",
    "gera completion json": "generate completion JSON",
    "notifica status do agent_group": "notify agent_group status",
    "Especifica o agent_group researcher para pesquisa de mercado":
     "Specify the researcher agent_group for market research",
}

KEYWORD_TRANSLATIONS = {
    "fato": "fact",
    "destilacao": "distillation",
    "densidade": "density",
    "conhecimento": "knowledge",
    "solucao": "solution",
    "recorrente": "recurring",
    "arquitetura": "architecture",
    "reutilizavel": "reusable",
    "pesquisar": "research",
    "mercado": "market",
    "concorrente": "competitor",
    "analise": "analysis",
}


def translate_text(text: str) -> str:
    """Apply phrase-level then word-level PT->EN translation."""
    result = text
    for pt, en in PHRASES:
        result = result.replace(pt, en)
    for pt, en in WORDS:
        result = result.replace(pt, en)
    return result


def translate_triggers_keywords(text: str) -> str:
    """Translate Portuguese triggers and keywords in frontmatter."""
    result = text
    for pt, en in TRIGGER_TRANSLATIONS.items():
        result = result.replace(pt, en)
    for pt, en in KEYWORD_TRANSLATIONS.items():
        result = result.replace(f'"{pt}"', f'"{en}"')
        result = result.replace(f', {pt},', f', {en},')
        result = result.replace(f'[{pt},', f'[{en},')
        result = result.replace(f', {pt}]', f', {en}]')
    return result


def process_file(filepath: str) -> bool:
    """Read, translate, and write back a single ISO file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='cp1252') as f:
                content = f.read()
        except (UnicodeDecodeError, OSError):
            print(f"  SKIP (encoding): {filepath}")
            return False

    original = content

    # Split frontmatter and body
    parts = content.split('---', 2)
    if len(parts) >= 3:
        pre = parts[0]
        frontmatter = parts[1]
        body = parts[2]

        # Translate frontmatter
        frontmatter = translate_text(frontmatter)
        frontmatter = translate_triggers_keywords(frontmatter)

        # Translate body
        body = translate_text(body)
        body = translate_triggers_keywords(body)

        content = pre + '---' + frontmatter + '---' + body
    else:
        content = translate_text(content)
        content = translate_triggers_keywords(content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main() -> int:
    list_file = sys.argv[1] if len(sys.argv) > 1 else None

    if list_file and os.path.exists(list_file):
        with open(list_file, 'r', encoding="utf-8") as f:
            files = [line.strip() for line in f if line.strip()]
    else:
        # Scan all builder ISOs
        files = []
        for root, dirs, filenames in os.walk('archetypes/builders'):
            for fn in filenames:
                if fn.endswith('.md'):
                    files.append(os.path.join(root, fn))

    print(f"Processing {len(files)} ISO files...")
    translated = 0
    skipped = 0

    for filepath in sorted(files):
        filepath = filepath.replace('\\', '/')
        if not os.path.exists(filepath):
            print(f"  NOT FOUND: {filepath}")
            skipped += 1
            continue

        if process_file(filepath):
            translated += 1
        else:
            skipped += 1

    print(f"\nDone: {translated} translated, {skipped} unchanged")
    return translated


if __name__ == '__main__':
    translated = main()
    sys.exit(0)
