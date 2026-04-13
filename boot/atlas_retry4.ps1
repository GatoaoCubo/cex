# Atlas retry: atoms 04, 06, 11, 18 (429 rate limited on first wave)
$cexRoot = Split-Path -Parent $PSScriptRoot
Set-Location $cexRoot

$runtimeDir = "$cexRoot\.cex\runtime"
$handoffPath = "$runtimeDir\handoffs\n01_task.md"

$failed = @(
    @{id="04"; topic="DSPy"; file="atom_04_dspy.md"; task="Fetch DSPy v2.6+ source for the GEPA optimizer. Document the Adapter system (ChatAdapter, JSONAdapter, XMLAdapter). Find DSPy-in-production case studies. Map the caching system. Document dspy.settings API. Enrich the atom."}
    @{id="06"; topic="LangChain+LangGraph"; file="atom_06_langchain_langgraph.md"; task="Fetch LangGraph Platform docs. Document Pregel execution model. Find Interrupt/Resume API for human-in-the-loop. Map prebuilt components. Document LangSmith dataset management API. Enrich the atom."}
    @{id="11"; topic="AgentScope"; file="atom_11_agentscope.md"; task="Fetch AgentScope Runtime v1.1 docs. Document ReMe 4-type memory system. Find ACEBench evaluation framework. Map all 10 hook types. Document A2A formatter. Enrich the atom."}
    @{id="18"; topic="Korea+India"; file="atom_18_korea_india.md"; task="Fetch PlayMCP marketplace API. Document Kanana-2 MoE architecture. Find Sarvam 105B tokenizer fertility. Map HyperCLOVA X Think. Document Indic LLM Arena. Search NEW 2026 releases. Enrich the atom."}
)

Write-Host "[RETRY] 4 failed atoms, 15s interval" -ForegroundColor Yellow

foreach ($atom in $failed) {
    $id = $atom.id
    $topic = $atom.topic
    $file = $atom.file
    $task = $atom.task

    $taskContent = @"
---
nucleus: N01
task: atlas_wave2_retry
atom: $id
topic: $topic
created: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
---

# Atlas Wave 2 RETRY: Deep Hydration of atom_$id ($topic)

## Your Task
You are N01 Research Nucleus. ENRICH an existing research atom with deeper detail.

## Existing Atom
Read: N01_intelligence/research/atlas/$file

## Deep-Dive Instructions
$task

## Rules
1. READ the existing atom first -- do NOT overwrite, ENRICH
2. quality: null in frontmatter
3. After writing, compile: python _tools/cex_compile.py N01_intelligence/research/atlas/$file
4. git add and commit with message: [N01-ATLAS] hydrate atom_$id $topic

## ON COMPLETION
git add N01_intelligence/research/atlas/$file N01_intelligence/research/compiled/ && git commit -m "[N01-ATLAS] hydrate atom_$id $topic"
"@
    $taskContent | Set-Content $handoffPath -Encoding utf8

    $proc = Start-Process powershell -ArgumentList @(
        "-NoProfile", "-NoExit", "-ExecutionPolicy", "Bypass",
        "-File", "$cexRoot\boot\n01.ps1"
    ) -WorkingDirectory $cexRoot -PassThru

    Write-Host "[RETRY] atom_$id ($topic) PID=$($proc.Id)" -ForegroundColor Green

    Start-Sleep -Seconds 15
}

Write-Host "[RETRY] All 4 relaunched" -ForegroundColor Cyan
