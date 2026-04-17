# CEX Atlas Wave 2 -- 32 N01 instances via boot/n01.ps1 (PowerShell, interactive)
# Spawns boot/n01.ps1 directly in PS windows (same as spawn_solo.ps1 does)
# but skips kill-before-spawn since we WANT 32 concurrent N01 instances.
#
# Flow per atom:
#   1. Write task to .cex/runtime/handoffs/n01_task.md
#   2. Launch: powershell -NoProfile -NoExit -File boot/n01.ps1
#   3. boot/n01.ps1 reads n01_task.md, starts claude with full env
#   4. Wait 5s, repeat for next atom
#
# Usage: powershell -File boot/atlas_wave2.ps1

$cexRoot = Split-Path -Parent $PSScriptRoot
Set-Location $cexRoot

$runtimeDir = "$cexRoot\.cex\runtime"
$archiveDir = "$runtimeDir\handoffs\atlas_wave2"
$pidFile = "$runtimeDir\pids\atlas_wave2_pids.txt"

New-Item -ItemType Directory -Force -Path $archiveDir | Out-Null
New-Item -ItemType Directory -Force -Path "$runtimeDir\pids" | Out-Null
"" | Set-Content $pidFile -Encoding utf8

$sessionId = "atlas-" + [System.Guid]::NewGuid().ToString().Substring(0, 8)

# 32 atom topics with deep-dive hydration tasks
$atoms = @(
    @{id="01"; topic="A2A Protocol"; file="atom_01_a2a_protocol.md"; task="Deep-dive the A2A v0.3 SDK implementations. Fetch actual Python/JS SDK code from github.com/a2aproject. Document every class, method, and type. Find real-world A2A deployments (AWS Bedrock AgentCore, Google Cloud). Extract integration patterns. Write findings BACK into the existing atom file, enriching sections 11-13."}
    @{id="02"; topic="MCP Protocol"; file="atom_02_mcp_protocol.md"; task="Fetch the FULL MCP TypeScript SDK source from github.com/modelcontextprotocol/typescript-sdk. Document every exported class and interface. Find all MCP server implementations in the wild (filesystem, postgres, github, slack). Map each to a CEX kind. Catalog the MCP Inspector tool. Write enrichments back into the atom."}
    @{id="03"; topic="OpenAI Agents SDK"; file="atom_03_openai_agents_sdk.md"; task="Fetch openai-agents-python v0.13+ changelog for ALL breaking changes since v0.6. Document the full Voice pipeline API (VoicePipeline, SingleAgentVoiceWorkflow). Find all community extensions. Map the Responses API integration. Enrich the atom with implementation-level detail."}
    @{id="04"; topic="DSPy"; file="atom_04_dspy.md"; task="Fetch DSPy v2.6+ source for the GEPA optimizer implementation details. Document the Adapter system (ChatAdapter, JSONAdapter, XMLAdapter). Find DSPy-in-production case studies. Map the caching system (configure_cache). Document the dspy.settings API. Enrich the atom."}
    @{id="05"; topic="Semantic Kernel"; file="atom_05_semantic_kernel.md"; task="Fetch the SK Process Framework docs (GA Q2 2026). Document the Declarative Agent YAML spec format. Find the AutoGen merger migration guide. Map all 16+ vector store connectors with their config schemas. Document the MCP bidirectional bridge. Enrich the atom."}
    @{id="06"; topic="LangChain+LangGraph"; file="atom_06_langchain_langgraph.md"; task="Fetch LangGraph Platform docs (cloud deployment). Document the Pregel execution model in detail. Find the Interrupt/Resume API for human-in-the-loop. Map all prebuilt components (create_react_agent, ToolNode, etc). Document LangSmith dataset management API. Enrich the atom."}
    @{id="07"; topic="LlamaIndex"; file="atom_07_llamaindex.md"; task="Fetch LlamaIndex AgentWorkflow docs (the new workflow-based agent system). Document LlamaParse v2 full API with all 20+ parameters. Find PropertyGraphIndex implementation details. Map the Workflow checkpoint system. Document all 8 evaluator types with scoring formulas. Enrich the atom."}
    @{id="08"; topic="CrewAI"; file="atom_08_crewai.md"; task="Fetch CrewAI v0.100+ docs for the unified memory system (LanceDB). Document all 80+ event types with their payload schemas. Find the Flow decorator system implementation. Map the YAML configuration pattern (agents.yaml + tasks.yaml). Document enterprise tier features. Enrich the atom."}
    @{id="09"; topic="AutoGen AG2"; file="atom_09_autogen_ag2.md"; task="Fetch AG2 v0.9 Pattern classes source code. Document the GraphFlow API. Find the Microsoft Agent Framework declarative YAML agent spec. Map all termination mechanisms with examples. Document the Swarm deprecation migration path. Enrich the atom."}
    @{id="10"; topic="Haystack+Vercel"; file="atom_10_haystack_vercel.md"; task="Fetch Haystack Pipeline serialization format (YAML/JSON). Document all 28 retriever implementations with config params. Find Vercel AI SDK middleware system. Map the DataStreamProtocol wire format. Document useChat/useCompletion hook APIs. Enrich the atom."}
    @{id="11"; topic="AgentScope"; file="atom_11_agentscope.md"; task="Fetch AgentScope Runtime v1.1 docs. Document the ReMe 4-type memory system implementation. Find the ACEBench evaluation framework. Map all 10 hook types with examples. Document the A2A formatter implementation. Enrich the atom."}
    @{id="12"; topic="Dify"; file="atom_12_dify.md"; task="Fetch Dify plugin development SDK docs. Document all 23 node types with their full config schemas. Find the Knowledge pipeline internal architecture. Map the variable referencing syntax system. Document the MCP Server publishing feature. Enrich the atom."}
    @{id="13"; topic="MetaGPT+ChatDev"; file="atom_13_metagpt_chatdev.md"; task="Fetch MetaGPT v0.9+ source for the Role/Action/Message class APIs. Document the pub-sub message pool implementation. Find the Experiential Co-Learning shortcut mining algorithm. Map the SOP-to-prompt compilation process. Enrich the atom."}
    @{id="14"; topic="Coze+XAgent"; file="atom_14_coze_xagent.md"; task="Fetch Coze 2.0 Persistent Planning docs. Document the Skills Marketplace API. Find XAgent ToolServer Docker implementation. Map the Dual-Loop (outer planner + inner actor) state machine. Document the AskForHumanHelp protocol. Enrich the atom."}
    @{id="15"; topic="Qwen+DeepSeek"; file="atom_15_qwen_deepseek.md"; task="Fetch Qwen3 Hermes XML template spec. Document the MCP manager singleton architecture. Find DeepSeek V3.2 agentic training pipeline details (1800 environments). Map the reasoning_content field lifecycle. Document DeepSeek Strict mode JSON Schema validation. Enrich the atom."}
    @{id="16"; topic="MiniMax+Kimi+GLM"; file="atom_16_minimax_kimi_glm.md"; task="Fetch MiniMax M2.5 Interleaved Thinking API docs. Document Kimi Agent Swarm PARL training details. Find GLM-5.1 All Tools function list (6000+ tools). Map the CISPO RL algorithm. Document OK Computer native agent mode. Enrich the atom."}
    @{id="17"; topic="Japan Ecosystem"; file="atom_17_japan_ecosystem.md"; task="Fetch Sakana AI Darwin Godel Machine paper details. Document NEC cotomi Act browser operation log extraction. Find Fujitsu Takane MCP integration. Map NTT tsuzumi 2 architecture. Document PFN PLaMo edge deployment. Search for any NEW Japanese agent frameworks released 2026. Enrich the atom."}
    @{id="18"; topic="Korea+India"; file="atom_18_korea_india.md"; task="Fetch PlayMCP marketplace API documentation. Document Kanana-2 MoE architecture details. Find Sarvam 105B custom tokenizer fertility scores. Map HyperCLOVA X Think agentic capabilities. Document Indic LLM Arena evaluation protocol. Search for NEW 2026 releases. Enrich the atom."}
    @{id="19"; topic="Agent Taxonomy"; file="atom_19_agent_taxonomy_surveys.md"; task="Search for NEW agent taxonomy papers published Jan-Apr 2026. Find the Arunkumar 2026 POMDP formalization details. Document the CLASSic evaluation framework dimensions. Map all 5 action paradigms with real implementations. Cross-reference with atom_28 code agents. Enrich the atom."}
    @{id="20"; topic="Prompt Taxonomy"; file="atom_20_prompt_taxonomy.md"; task="Search for NEW prompt engineering papers 2026 (post-Schulhoff). Find implementation code for top 20 techniques. Document the DSPy optimizer-to-technique mapping. Map multimodal prompt techniques to real frameworks. Create a decision tree: which technique for which task type. Enrich the atom."}
    @{id="21"; topic="RAG Taxonomy"; file="atom_21_rag_taxonomy.md"; task="Search for NEW RAG papers 2026 (Agentic RAG, Graph RAG v2). Find NVIDIA chunking benchmark updated results. Document late chunking (Jina 2024) implementation. Map all reranker types with performance comparison. Create a RAG architecture decision tree. Enrich the atom."}
    @{id="22"; topic="Memory Taxonomy"; file="atom_22_memory_taxonomy.md"; task="Search for NEW memory papers 2026. Find the Anatomy of Agentic Memory (2602.19320) implementation code. Document the 3D-8Q taxonomy with concrete examples for each quadrant. Map consolidation mechanisms to real systems. Create a memory system design decision tree. Enrich the atom."}
    @{id="23"; topic="Multi-agent Protocols"; file="atom_23_multiagent_protocols.md"; task="Fetch the ProtocolBench evaluation results in detail. Document the ProtocolRouter adaptive routing algorithm. Find ACP (Agent Communication Protocol) latest spec. Map all 16 protocols from the survey with implementation status. Create a protocol selection decision tree. Enrich the atom."}
    @{id="24"; topic="NIST Vocabulary"; file="atom_24_nist_vocabulary.md"; task="Fetch the FULL NIST AI 100-3 CSV and verify all 511 terms have complete definitions. Find NIST AI 600-1 GenAI Profile implementation guides. Document the AI RMF Playbook practical guidance. Map NIST terms to ISO/IEC 42001 (AI Management System). Cross-reference with EU AI Act terminology. Enrich the atom."}
    @{id="25"; topic="Safety Taxonomy"; file="atom_25_safety_taxonomy.md"; task="Search for NEW safety papers 2026. Find ControlArena implementation code (UK AISI). Document all 8 guardrail frameworks with setup instructions. Map Constitutional AI principle categories to NIST risk categories. Create a safety implementation checklist for CEX. Enrich the atom."}
    @{id="26"; topic="Evaluation Taxonomy"; file="atom_26_evaluation_taxonomy.md"; task="Search for NEW eval papers 2026. Find AutoRubric implementation details. Document the CLASSic and CLEAR frameworks with scoring formulas. Map all 40+ benchmarks to CEX quality gate dimensions. Create an evaluation strategy decision tree. Enrich the atom."}
    @{id="27"; topic="Computer Use"; file="atom_27_computer_browser_agents.md"; task="Fetch Anthropic Computer Use v3 (20250728) tool spec. Document Playwright MCP a11y snapshot approach in detail. Find SoM (Set-of-Mark) implementation code. Map all 8 benchmarks with latest scores. Create a computer-use agent architecture decision tree. Enrich the atom."}
    @{id="28"; topic="Code Agents"; file="atom_28_code_agents.md"; task="Fetch Claude Code SDK headless mode API docs. Document Aider repo-map PageRank algorithm. Find Cursor background agent VM isolation details. Map all 9 edit format families with examples. Create a code-agent selection decision tree for different project types. Enrich the atom."}
    @{id="29"; topic="Voice+Realtime"; file="atom_29_voice_realtime.md"; task="Fetch OpenAI Realtime API v2 event list. Document Pipecat Frame-based pipeline architecture. Find LiveKit Room/Track/Plugin system. Map all VAD configurations across providers. Document Moshi S2S architecture details. Create a voice-agent architecture decision tree. Enrich the atom."}
    @{id="30"; topic="Reasoning+Thinking"; file="atom_30_reasoning_thinking.md"; task="Fetch Anthropic extended thinking API (budget_tokens, signatures). Document all 14 RL algorithms for reasoning (PPO through GRPO). Find process reward model (PRM) training details. Map test-time compute scaling laws. Create a reasoning strategy selection guide. Enrich the atom."}
    @{id="31"; topic="ML Ontologies"; file="atom_31_ml_ontologies.md"; task="Fetch MetaAutoML RDF/Turtle ontology and count exact individuals. Document AIO (Artificial Intelligence Ontology) LLM-era branch. Find the Papers With Code archive (post-shutdown July 2025). Map W3C ML Schema 25 classes with properties. Create an ontology ingestion priority matrix. Enrich the atom."}
    @{id="32"; topic="Vendor Glossaries"; file="atom_32_vendor_glossaries_adk.md"; task="Fetch Google ADK v1.x full class reference. Document all 5 agent types with constructor params. Find AWS Bedrock AgentCore A2A integration. Map HuggingFace smolagents tool system. Document Anthropic Claude tool_use schema evolution. Create a vendor SDK comparison matrix. Enrich the atom."}
)

# --- Window grid layout (reuse spawn_solo.ps1 logic) ---
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Atlas {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@
Add-Type -AssemblyName System.Windows.Forms
$screen = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
# 8x4 grid for 32 windows
$cols = 8; $rows = 4
$cellW = [math]::Floor($screen.Width / $cols)
$cellH = [math]::Floor($screen.Height / $rows)

$total = $atoms.Count
$launched = 0
$handoffPath = "$runtimeDir\handoffs\n01_task.md"

Write-Host ""
Write-Host "=== ATLAS WAVE 2: $total ATOMS ===" -ForegroundColor Cyan
Write-Host "Boot: boot/n01.ps1 (PowerShell, interactive, sin-aware)" -ForegroundColor DarkGray
Write-Host "Model: claude-sonnet-4-6 (from nucleus_models.yaml)" -ForegroundColor DarkGray
Write-Host "Interval: 5 seconds between spawns" -ForegroundColor DarkGray
Write-Host "Session: $sessionId" -ForegroundColor DarkGray
Write-Host ""

foreach ($atom in $atoms) {
    $id = $atom.id
    $topic = $atom.topic
    $file = $atom.file
    $task = $atom.task
    $idx = $launched  # 0-based index

    # 1. Write task to n01_task.md (boot/n01.ps1 reads this on startup)
    $fullTask = @"
---
nucleus: N01
task: atlas_wave2_hydration
atom: $id
topic: $topic
created: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
---

# Atlas Wave 2: Deep Hydration of atom_$id ($topic)

## Your Task
You are N01 Research Nucleus. ENRICH an existing research atom with deeper implementation-level detail.

## Existing Atom
Read: N01_intelligence/P01_knowledge/atlas/$file

## Deep-Dive Instructions
$task

## Rules
1. READ the existing atom first -- do NOT overwrite, ENRICH
2. Add new sections or expand existing ones with implementation detail
3. Every claim must have a source URL
4. quality: null in frontmatter (never self-score)
5. After writing, compile: python _tools/cex_compile.py N01_intelligence/P01_knowledge/atlas/$file
6. git add and commit with message: [N01-ATLAS] hydrate atom_$id $topic

## Context
This is part of a 32-agent parallel hydration wave. You are one of 32 N01 instances,
each enriching one atom. Work autonomously. Do not wait for other agents.

## ON COMPLETION
1. Commit your work: git add N01_intelligence/P01_knowledge/atlas/$file N01_intelligence/compiled/ && git commit -m "[N01-ATLAS] hydrate atom_$id $topic"
2. Signal complete:

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'complete', 9.0)"
"@
    # Write to the canonical handoff path (boot/n01.ps1 reads this)
    $fullTask | Set-Content $handoffPath -Encoding utf8

    # Also archive a copy (n01_task.md gets overwritten by next spawn)
    $fullTask | Set-Content "$archiveDir\n01_atom_${id}_task.md" -Encoding utf8

    # 2. Launch boot/n01.ps1 in a new PowerShell window (same as spawn_solo.ps1 line 128)
    $bootPs1 = "$cexRoot\boot\n01.ps1"
    $proc = Start-Process powershell -ArgumentList @(
        "-NoProfile", "-NoExit", "-ExecutionPolicy", "Bypass",
        "-File", $bootPs1
    ) -WorkingDirectory $cexRoot -PassThru

    # 3. Position window in 8x4 grid
    $col = $idx % $cols
    $row = [math]::Floor($idx / $cols)
    $x = $screen.X + ($col * $cellW)
    $y = $screen.Y + ($row * $cellH)

    # Wait for window handle
    $hwnd = [IntPtr]::Zero
    for ($i = 0; $i -lt 6; $i++) {
        Start-Sleep -Milliseconds 300
        try { $proc.Refresh() } catch {}
        $hwnd = $proc.MainWindowHandle
        if ($hwnd -ne [IntPtr]::Zero) { break }
    }
    if ($hwnd -ne [IntPtr]::Zero) {
        [Win32Atlas]::MoveWindow($hwnd, $x, $y, $cellW, $cellH, $true) | Out-Null
    }

    # 4. Record PID
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$($proc.Id) n01-atlas-$id claude $sessionId $timestamp" | Add-Content $pidFile -Encoding utf8

    $launched++
    Write-Host "[$launched/$total] atom_$id ($topic) PID=$($proc.Id) grid=($col,$row)" -ForegroundColor Green

    # 5. Wait 5 seconds before next spawn (user-specified interval)
    if ($launched -lt $total) {
        Start-Sleep -Seconds 5
    }
}

Write-Host ""
Write-Host "=== ALL $launched ATLAS INSTANCES LAUNCHED ===" -ForegroundColor Cyan
Write-Host "Session: $sessionId" -ForegroundColor DarkGray
Write-Host "PIDs: $pidFile" -ForegroundColor DarkGray
Write-Host "Archive: $archiveDir" -ForegroundColor DarkGray
Write-Host "Monitor: Get-Content $pidFile" -ForegroundColor DarkGray
