#!/usr/bin/env pwsh
<#
.SYNOPSIS
  CEX Overnight Flywheel -- Continuous autonomous improvement loop.

.DESCRIPTION
  Three-phase flywheel that runs unattended:
    Phase 1: BOOTSTRAP -- generate artifacts for empty nuclei (N03, N05, N06, N07)
    Phase 2: EVOLVE    -- AutoResearch on all artifacts scoring < target
    Phase 3: CYCLE     -- cex_auto.py scan->plan->execute for remaining gaps

  Budget-tracked, crash-resilient, with full logging.
  Designed to run overnight via: .\boot\overnight.ps1

.PARAMETER MaxTokens
  Total token budget for the session (default: 500000)

.PARAMETER TargetScore
  Quality target for AutoResearch (default: 9.0)

.PARAMETER Threshold
  Score below which agent mode triggers (default: 8.5)

.PARAMETER MaxCycles
  Maximum number of full flywheel cycles (default: 50)

.PARAMETER Phase
  Run specific phase only: all, bootstrap, evolve, cycle (default: all)

.PARAMETER DryRun
  Preview without executing (no LLM calls, no git commits)

.EXAMPLE
  .\boot\overnight.ps1                              # full flywheel, default budget
  .\boot\overnight.ps1 -MaxTokens 1000000           # 1M token budget
  .\boot\overnight.ps1 -Phase evolve                # evolve only
  .\boot\overnight.ps1 -Phase bootstrap -DryRun     # preview bootstrap
  .\boot\overnight.ps1 -MaxCycles 100 -TargetScore 9.5  # aggressive
#>

param(
    [int]$MaxTokens = 500000,
    [float]$TargetScore = 9.0,
    [float]$Threshold = 8.5,
    [int]$MaxCycles = 50,
    [ValidateSet("all", "bootstrap", "evolve", "cycle", "farm")]
    [string]$Phase = "all",
    [switch]$DryRun,
    [switch]$Farm
)

# Farm mode: no budget limit, infinite cycles, all phases + knowledge mining
if ($Farm) {
    $MaxTokens = [int]::MaxValue
    $MaxCycles = [int]::MaxValue
    $Phase = "farm"
    # In farm mode, threshold = target so agent mode activates on ALL below-target artifacts
    # This is the key: heuristic can't push 8.8 -> 9.0, only LLM can
    $Threshold = $TargetScore
}

# ============================================================
# CONFIG
# ============================================================

$ErrorActionPreference = "Continue"
$CEX_ROOT = "C:\Users\PC\Documents\GitHub\cex"
$PYTHON = "python"
$LOG_DIR = Join-Path $CEX_ROOT ".cex\overnight"
$TIMESTAMP = Get-Date -Format "yyyyMMdd_HHmmss"
$LOG_FILE = Join-Path $LOG_DIR "overnight_${TIMESTAMP}.log"
$STATE_FILE = Join-Path $LOG_DIR "state.json"
$LOCK_FILE = Join-Path $LOG_DIR ".lock"

# Nucleus definitions
$NUCLEI = @{
    "N01" = @{ dir = "N01_intelligence"; identity = "Research Analyst"; domain = "intelligence" }
    "N02" = @{ dir = "N02_marketing";    identity = "Marketing Strategist"; domain = "marketing" }
    "N03" = @{ dir = "N03_creation";     identity = "Builder Architect"; domain = "creation" }
    "N04" = @{ dir = "N04_knowledge";    identity = "Knowledge Engineer"; domain = "knowledge" }
    "N05" = @{ dir = "N05_engineering";  identity = "DevOps Engineer"; domain = "engineering" }
    "N06" = @{ dir = "N06_brand";        identity = "Brand Architect"; domain = "brand" }
    "N07" = @{ dir = "N07_orchestration"; identity = "Mission Control"; domain = "orchestration" }
}

# Artifact types each nucleus needs (kind -> subdirectory)
$CORE_ARTIFACTS = @(
    @{ kind = "agent";          subdir = "agents";        intent = "create agent for {domain} nucleus" }
    @{ kind = "system_prompt";  subdir = "prompts";       intent = "create system prompt for {domain} nucleus" }
    @{ kind = "knowledge_card"; subdir = "knowledge";     intent = "create knowledge card about {domain} best practices" }
    @{ kind = "agent_card";     subdir = "architecture";  intent = "create agent card for {domain} nucleus" }
    @{ kind = "workflow";       subdir = "orchestration"; intent = "create workflow for {domain} pipeline" }
    @{ kind = "quality_gate";   subdir = "quality";       intent = "create quality gate for {domain} artifacts" }
    @{ kind = "scoring_rubric"; subdir = "quality";       intent = "create scoring rubric for {domain} evaluation" }
    @{ kind = "dispatch_rule";  subdir = "orchestration"; intent = "create dispatch rule for {domain} routing" }
    @{ kind = "schema";         subdir = "schemas";       intent = "create schema contract for {domain} data model" }
    @{ kind = "output_template";subdir = "output";        intent = "create output template for {domain} reports" }
    @{ kind = "prompt_template";subdir = "prompts";       intent = "create prompt template for {domain} tasks" }
)

# ============================================================
# LOGGING
# ============================================================

function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$ts] [$Level] $Message"
    Write-Host $line
    Add-Content -Path $LOG_FILE -Value $line -Encoding UTF8
}

function Write-Banner {
    param([string]$Title)
    $border = "=" * 60
    Write-Log $border
    Write-Log "  $Title"
    Write-Log $border
}

# ============================================================
# STATE MANAGEMENT (crash recovery)
# ============================================================

function Load-State {
    if (Test-Path $STATE_FILE) {
        try {
            $raw = [System.IO.File]::ReadAllText($STATE_FILE, [System.Text.Encoding]::UTF8)
            # Guard against null-byte corruption
            if ($raw -and $raw[0] -ne "`0" -and $raw.Trim().Length -gt 2) {
                return $raw | ConvertFrom-Json
            }
            Write-Log "state.json corrupted (null bytes). Resetting." "WARN"
        } catch {
            Write-Log "state.json parse error: $($_.Exception.Message). Resetting." "WARN"
        }
    }
    return @{
        phase = "bootstrap"
        cycle = 0
        tokens_used = 0
        artifacts_created = 0
        artifacts_evolved = 0
        started_at = (Get-Date -Format o)
        last_checkpoint = $null
        bootstrap_done = @()
        evolve_queue = @()
    }
}

function Save-State {
    param($State)
    $State.last_checkpoint = (Get-Date -Format o)
    $json = $State | ConvertTo-Json -Depth 5
    [System.IO.File]::WriteAllText($STATE_FILE, $json, [System.Text.Encoding]::UTF8)
}

# ============================================================
# BUDGET TRACKING
# ============================================================

$script:TokensUsed = 0

$script:CreditsDepleted = $false

function Test-Budget {
    if ($script:CreditsDepleted) {
        Write-Log "CREDITS DEPLETED -- stopping all LLM calls" "FATAL"
        return $false
    }
    if ($script:TokensUsed -ge $MaxTokens) {
        Write-Log "BUDGET EXHAUSTED: $($script:TokensUsed)/$MaxTokens tokens" "WARN"
        return $false
    }
    return $true
}

function Test-CreditError {
    param([string]$Output)
    if ($Output -match 'Credit balance is too low|credits?.*exhaust|billing.*limit|payment.*required') {
        Write-Log "CREDIT ERROR DETECTED: $($Matches[0])" "FATAL"
        $script:CreditsDepleted = $true
        return $true
    }
    return $false
}

function Add-Tokens {
    param([int]$Count)
    $script:TokensUsed += $Count
    Write-Log "Tokens: +$Count (total: $($script:TokensUsed)/$MaxTokens)" "METRIC"
}

# ============================================================
# PHASE 1: BOOTSTRAP -- Generate artifacts for empty nuclei
# ============================================================

function Invoke-Bootstrap {
    param($State)

    Write-Banner "PHASE 1: BOOTSTRAP"

    foreach ($nKey in @("N03", "N05", "N06", "N07")) {
        $n = $NUCLEI[$nKey]
        $nDir = Join-Path $CEX_ROOT $n.dir

        # Count existing artifacts
        $existing = @()
        if (Test-Path $nDir) {
            $existing = Get-ChildItem -Path $nDir -Filter "*.md" -Recurse |
                Where-Object { $_.DirectoryName -notmatch "compiled" -and $_.Name -ne "README.md" }
        }

        if ($existing.Count -ge 10) {
            Write-Log "$nKey already has $($existing.Count) artifacts. Skipping bootstrap." "SKIP"
            continue
        }

        Write-Log "$nKey ($($n.identity)): $($existing.Count) artifacts. Bootstrapping..."

        # Check which artifact types are missing
        $existingKinds = @()
        foreach ($f in $existing) {
            $content = Get-Content $f.FullName -Raw -Encoding UTF8 -ErrorAction SilentlyContinue
            if ($content -match '^kind:\s*(\S+)') {
                $existingKinds += $Matches[1]
            }
        }

        foreach ($artifact in $CORE_ARTIFACTS) {
            if (!(Test-Budget)) { return $State }

            $kind = $artifact.kind
            if ($existingKinds -contains $kind) {
                Write-Log "  ${nKey}/${kind}: already exists. Skip." "SKIP"
                continue
            }

            # Already done in previous run?
            $doneKey = "${nKey}_${kind}"
            if ($State.bootstrap_done -contains $doneKey) {
                Write-Log "  ${nKey}/${kind}: done in previous run. Skip." "SKIP"
                continue
            }

            $intent = $artifact.intent -replace "\{domain\}", $n.domain
            Write-Log "  Building: ${nKey}/${kind} -- $intent"

            if ($DryRun) {
                Write-Log "  [DRY-RUN] Would run: cex_run.py '$intent' --execute" "DRY"
                continue
            }

            try {
                $result = & $PYTHON "$CEX_ROOT\_tools\cex_run.py" $intent --execute 2>&1 | Out-String

                # Check for credit/billing errors before anything else
                if (Test-CreditError $result) { return $State }

                # cex_run.py saves to its own path and reports it
                $savedRx = 'Saved:\s*(\S+\.md)'
                $artifactRx = 'Artifact created:\s*(\S+\.md)'
                $savedFile = ""
                if ($result -match $savedRx) { $savedFile = $Matches[1] }
                elseif ($result -match $artifactRx) { $savedFile = $Matches[1] }

                if ($result -match 'Quality gate.*PASS') {
                    $estTokens = [math]::Max(2000, [int]($result.Length / 4))
                    Add-Tokens $estTokens
                    Write-Log "  OK Created ${nKey}/${kind} -> $savedFile" "OK"
                    $State.artifacts_created++
                } elseif ($savedFile) {
                    Add-Tokens 2000
                    Write-Log "  WARN Created ${nKey}/${kind} -> $savedFile (gate unknown)" "WARN"
                    $State.artifacts_created++
                } else {
                    Write-Log "  FAIL ${nKey}/${kind} -- no artifact saved" "ERROR"
                    Write-Log "  OUTPUT: $($result.Substring(0, [math]::Min(500, $result.Length)))" "DEBUG"
                }

                $State.bootstrap_done += $doneKey

            } catch {
                Write-Log "  [FAIL] Failed ${nKey}/${kind} -- $($_.Exception.Message)" "ERROR"
            }

            Save-State $State

            # Small delay to avoid rate limits
            Start-Sleep -Seconds 2
        }
    }

    # Also bootstrap N01, N02, N04 missing kinds
    foreach ($nKey in @("N01", "N02", "N04")) {
        $n = $NUCLEI[$nKey]
        $nDir = Join-Path $CEX_ROOT $n.dir

        $existing = Get-ChildItem -Path $nDir -Filter "*.md" -Recurse |
            Where-Object { $_.DirectoryName -notmatch "compiled" -and $_.Name -ne "README.md" }

        $existingKinds = @()
        foreach ($f in $existing) {
            $content = Get-Content $f.FullName -Raw -Encoding UTF8 -ErrorAction SilentlyContinue
            if ($content -match '^kind:\s*(\S+)') {
                $existingKinds += $Matches[1]
            }
        }

        foreach ($artifact in $CORE_ARTIFACTS) {
            if (!(Test-Budget)) { return $State }

            $kind = $artifact.kind
            if ($existingKinds -contains $kind) { continue }

            $doneKey = "${nKey}_${kind}"
            if ($State.bootstrap_done -contains $doneKey) { continue }

            $intent = $artifact.intent -replace "\{domain\}", $n.domain
            Write-Log "  Filling gap: ${nKey}/${kind}"

            if ($DryRun) {
                Write-Log "  [DRY-RUN] Would build ${nKey}/${kind}" "DRY"
                continue
            }

            try {
                $result = & $PYTHON "$CEX_ROOT\_tools\cex_run.py" $intent --execute 2>&1 | Out-String
                $estTokens = [math]::Max(2000, [int]($result.Length / 4))
                Add-Tokens $estTokens
                $State.artifacts_created++
                $State.bootstrap_done += $doneKey
                Write-Log "  [OK] Gap filled: ${nKey}/${kind}" "OK"
            } catch {
                Write-Log "  [FAIL] Gap fill failed: ${nKey}/${kind}" "ERROR"
            }

            Save-State $State
            Start-Sleep -Seconds 2
        }
    }

    Write-Log "Bootstrap complete. $($State.artifacts_created) artifacts created."
    return $State
}

# ============================================================
# PHASE 2: EVOLVE -- AutoResearch on all artifacts < target
# ============================================================

function Invoke-Evolve {
    param($State)

    Write-Banner "PHASE 2: EVOLVE (target: $TargetScore)"

    # Collect all artifacts below target score
    $toEvolve = @()

    foreach ($nKey in $NUCLEI.Keys | Sort-Object) {
        $n = $NUCLEI[$nKey]
        $nDir = Join-Path $CEX_ROOT $n.dir

        if (!(Test-Path $nDir)) { continue }

        $files = Get-ChildItem -Path $nDir -Filter "*.md" -Recurse |
            Where-Object { $_.DirectoryName -notmatch "compiled" -and $_.Name -ne "README.md" }

        foreach ($f in $files) {
            $content = Get-Content $f.FullName -Raw -Encoding UTF8 -ErrorAction SilentlyContinue
            if ($content -match 'quality:\s*([\d.]+)') {
                $score = [float]$Matches[1]
                if ($score -lt $TargetScore) {
                    $toEvolve += @{
                        path = $f.FullName
                        relative = $f.FullName.Replace("$CEX_ROOT\", "")
                        score = $score
                        nucleus = $nKey
                    }
                }
            } elseif ($content -match 'quality:\s*null') {
                $toEvolve += @{
                    path = $f.FullName
                    relative = $f.FullName.Replace("$CEX_ROOT\", "")
                    score = 0
                    nucleus = $nKey
                }
            }
        }
    }

    # Sort: lowest scores first (most improvement potential)
    $toEvolve = $toEvolve | Sort-Object { $_.score }

    Write-Log "Found $($toEvolve.Count) artifacts below target $TargetScore"

    $evolved = 0
    $improved = 0

    # Track failed evolves this cycle to avoid retrying same artifacts
    # Convert evolve_tried from PSCustomObject (JSON load) to hashtable
    # PSCustomObject.ContainsKey() does not exist -- hashtable does
    if (-not $State.PSObject.Properties['evolve_tried']) {
        $State | Add-Member -NotePropertyName 'evolve_tried' -NotePropertyValue @{} -Force
    } elseif ($State.evolve_tried -is [PSCustomObject]) {
        $ht = @{}
        $State.evolve_tried.PSObject.Properties | ForEach-Object { $ht[$_.Name] = $_.Value }
        $State.evolve_tried = $ht
    }

    foreach ($item in $toEvolve) {
        if (!(Test-Budget)) { break }

        $rel = $item.relative
        $score = $item.score

        # Skip if already tried this cycle and didn't improve
        $triedKey = $rel
        if ($State.evolve_tried.ContainsKey($triedKey)) {
            $lastScore = $State.evolve_tried[$triedKey]
            if ($lastScore -eq $score) {
                continue  # silently skip -- already tried, same score
            }
        }

        Write-Log "  Evolving: $rel (current: $score)"

        if ($DryRun) {
            Write-Log "  [DRY-RUN] Would evolve $rel" "DRY"
            $evolved++
            continue
        }

        try {
            $result = & $PYTHON "$CEX_ROOT\_tools\cex_evolve.py" auto $item.path `
                --threshold $Threshold --budget 30000 --target $TargetScore 2>&1 | Out-String

            # Parse result
            if ($result -match '"tokens_used":\s*(\d+)') {
                Add-Tokens ([int]$Matches[1])
            } else {
                Add-Tokens 1000  # conservative estimate
            }

            $qualityRx = '"quality":\s*([\d\.]+)'
            if ($result -match $qualityRx) {
                $newScore = [float]$Matches[1]
                $delta = $newScore - $score

                if ($delta -gt 0) {
                    Write-Log ("  OK ${rel}: $score -> $newScore (+" + [math]::Round($delta, 1) + ")") "OK"
                    $improved++
                } else {
                    Write-Log ("  SKIP ${rel}: no improvement ($newScore)") "SKIP"
                }
            }

            if ($result -match '"mode_used":\s*"(\w+)"') {
                $mode = $Matches[1]
                Write-Log "  Mode: $mode" "METRIC"
            }

            $evolved++
            $State.artifacts_evolved++
            # Track what we tried so we don't re-try failures
            $State.evolve_tried[$triedKey] = $score

        } catch {
            Write-Log "  [FAIL] Error evolving $rel -- $($_.Exception.Message)" "ERROR"
            $State.evolve_tried[$triedKey] = $score
        }

        Save-State $State

        # Rate limit: small delay between artifacts
        Start-Sleep -Milliseconds 500
    }

    Write-Log "Evolve complete. $evolved processed, $improved improved."
    return $State
}

# ============================================================
# PHASE 3: CYCLE -- cex_auto.py for remaining gaps
# ============================================================

function Invoke-Cycle {
    param($State)

    Write-Banner "PHASE 3: AUTO CYCLE"

    if (!(Test-Budget)) {
        Write-Log "No budget for cycle phase." "WARN"
        return $State
    }

    $maxActions = [math]::Max(5, [int](($MaxTokens - $script:TokensUsed) / 5000))
    Write-Log "Running cex_auto.py cycle (max $maxActions actions)"

    if ($DryRun) {
        Write-Log "[DRY-RUN] Would run: cex_auto.py cycle --max $maxActions --dry-run" "DRY"
        return $State
    }

    try {
        $result = & $PYTHON "$CEX_ROOT\_tools\cex_auto.py" cycle --max $maxActions 2>&1 | Out-String
        Write-Log $result

        if ($result -match '(\d+)/(\d+) actions succeeded') {
            $passed = [int]$Matches[1]
            $total = [int]$Matches[2]
            Add-Tokens ($passed * 3000)
            Write-Log "Cycle: $passed/$total actions succeeded" "OK"
        }
    } catch {
        Write-Log "Cycle error: $($_.Exception.Message)" "ERROR"
    }

    return $State
}

# ============================================================
# PHASE 4: FARM -- Mine knowledge until rate-limited
# ============================================================

# Knowledge domains to farm (expands with each cycle)
$FARM_TOPICS = @(
    # Per-nucleus deep dives
    @{ nucleus = "N01"; topics = @(
        "create knowledge card about competitive intelligence OSINT techniques"
        "create knowledge card about market research data triangulation"
        "create knowledge card about trend detection with time series analysis"
        "create knowledge card about source credibility scoring frameworks"
        "create schema contract for benchmark comparison data model"
        "create output template for weekly market intelligence brief"
    )}
    @{ nucleus = "N02"; topics = @(
        "create knowledge card about conversion copywriting frameworks"
        "create knowledge card about brand voice consistency across channels"
        "create knowledge card about A/B testing for content optimization"
        "create knowledge card about SEO content strategy for e-commerce"
        "create output template for social media content calendar"
        "create schema contract for campaign performance metrics"
    )}
    @{ nucleus = "N03"; topics = @(
        "create knowledge card about prompt engineering best practices"
        "create knowledge card about multi-agent orchestration patterns"
        "create knowledge card about artifact quality evaluation methods"
        "create knowledge card about LLM output parsing and validation"
        "create schema contract for builder specification format"
        "create output template for artifact creation report"
    )}
    @{ nucleus = "N04"; topics = @(
        "create knowledge card about RAG chunking strategies comparison"
        "create knowledge card about vector embedding model selection"
        "create knowledge card about knowledge graph construction from documents"
        "create knowledge card about fine-tuning dataset preparation"
        "create knowledge card about Supabase pgvector setup for RAG"
        "create schema contract for training dataset quality metrics"
    )}
    @{ nucleus = "N05"; topics = @(
        "create knowledge card about CI/CD pipeline for LLM applications"
        "create knowledge card about Python testing strategies for AI agents"
        "create knowledge card about Docker containerization for AI services"
        "create knowledge card about API rate limiting and retry patterns"
        "create schema contract for deployment configuration"
        "create output template for system health dashboard"
    )}
    @{ nucleus = "N06"; topics = @(
        "create knowledge card about brand archetype theory and application"
        "create knowledge card about visual identity system design"
        "create knowledge card about pricing strategy for digital products"
        "create knowledge card about customer persona development"
        "create schema contract for brand audit scorecard"
        "create output template for brand book chapter"
    )}
    @{ nucleus = "N07"; topics = @(
        "create knowledge card about multi-agent task decomposition"
        "create knowledge card about autonomous agent error recovery"
        "create knowledge card about inter-agent communication protocols"
        "create knowledge card about agent performance monitoring"
        "create schema contract for mission execution plan"
        "create output template for orchestration status dashboard"
    )}
)

$RATE_LIMIT_BACKOFF = 60  # seconds to wait after rate limit

function Invoke-Farm {
    param($State)

    Write-Banner "PHASE 4: FARM (mining knowledge until rate-limited)"

    # Track what we've farmed
    if (-not $State.PSObject.Properties['farmed']) {
        $State | Add-Member -NotePropertyName 'farmed' -NotePropertyValue @() -Force
    }
    if (-not $State.PSObject.Properties['rate_limited_at']) {
        $State | Add-Member -NotePropertyName 'rate_limited_at' -NotePropertyValue $null -Force
    }
    if (-not $State.PSObject.Properties['farm_cycle']) {
        $State | Add-Member -NotePropertyName 'farm_cycle' -NotePropertyValue 0 -Force
    }

    $State.farm_cycle++
    $farmed = 0
    $rateLimited = $false

    foreach ($group in $FARM_TOPICS) {
        $nKey = $group.nucleus

        foreach ($intent in $group.topics) {
            # Skip if already farmed
            $farmKey = "${nKey}_$($intent.GetHashCode())"
            if ($State.farmed -contains $farmKey) {
                continue
            }

            if ($DryRun) {
                Write-Log "  [DRY-RUN] Would farm: $intent" "DRY"
                continue
            }

            Write-Log "  FARM ${nKey}: $($intent.Substring(0, [math]::Min(60, $intent.Length)))..."

            try {
                $sw = [System.Diagnostics.Stopwatch]::StartNew()
                $result = & $PYTHON "$CEX_ROOT\_tools\cex_run.py" $intent --execute 2>&1 | Out-String
                $sw.Stop()

                # Detect credit depletion (fatal -- stop entirely)
                if (Test-CreditError $result) { return $State }

                # Detect rate limit (Claude returns error)
                if ($result -match 'rate.?limit|429|too many|overloaded|capacity') {
                    Write-Log "  RATE LIMITED. Backing off ${RATE_LIMIT_BACKOFF}s..." "WARN"
                    $State.rate_limited_at = (Get-Date -Format o)
                    Save-State $State
                    Start-Sleep -Seconds $RATE_LIMIT_BACKOFF

                    # Retry once after backoff
                    $result = & $PYTHON "$CEX_ROOT\_tools\cex_run.py" $intent --execute 2>&1 | Out-String
                    if ($result -match 'rate.?limit|429|too many|overloaded|capacity') {
                        Write-Log "  Still rate-limited. Switching to heuristic work..." "WARN"
                        $rateLimited = $true
                        break
                    }
                }

                $savedRx = 'Saved:\s*(\S+\.md)'
                $savedFile = ""
                if ($result -match $savedRx) { $savedFile = $Matches[1] }

                if ($result -match 'Quality gate.*PASS') {
                    $farmed++
                    $State.artifacts_created++
                    $State.farmed += $farmKey
                    $elapsed = [math]::Round($sw.Elapsed.TotalSeconds)
                    Write-Log "  OK Farmed -> $savedFile (${elapsed}s)" "OK"
                } elseif ($savedFile) {
                    $farmed++
                    $State.artifacts_created++
                    $State.farmed += $farmKey
                    Write-Log "  WARN Farmed -> $savedFile (gate unknown)" "WARN"
                } else {
                    Write-Log "  FAIL Farm failed: no artifact saved" "ERROR"
                }

                Save-State $State
                Start-Sleep -Seconds 2

            } catch {
                Write-Log "  FAIL Farm error: $($_.Exception.Message)" "ERROR"
            }
        }

        if ($rateLimited) { break }
    }

    # If rate limited, do free heuristic work while waiting
    if ($rateLimited) {
        Write-Log "  Rate-limited. Running free heuristic evolve while waiting..." "INFO"
        $State = Invoke-Evolve $State
    }

    Write-Log "Farm cycle $($State.farm_cycle) complete. $farmed new artifacts mined."
    return $State
}

# ============================================================
# MAIN LOOP
# ============================================================

function Main {
    # Setup
    Set-Location $CEX_ROOT
    New-Item -ItemType Directory -Path $LOG_DIR -Force | Out-Null

    # Lock check (prevent double-run)
    if (Test-Path $LOCK_FILE) {
        $lockAge = (Get-Date) - (Get-Item $LOCK_FILE).LastWriteTime
        if ($lockAge.TotalHours -lt 12) {
            Write-Host "[FAIL] Another overnight session is running (lock age: $([math]::Round($lockAge.TotalMinutes)) min)"
            Write-Host "   Delete $LOCK_FILE to force restart."
            return
        }
        Write-Host "[WARN]  Stale lock found (age: $([math]::Round($lockAge.TotalHours, 1))h). Removing."
    }
    Set-Content $LOCK_FILE (Get-Date -Format o) -Encoding UTF8

    # Banner
    Write-Banner "CEX OVERNIGHT FLYWHEEL"
    Write-Log "Started: $(Get-Date -Format o)"
    Write-Log "Budget:  $MaxTokens tokens"
    Write-Log "Target:  $TargetScore"
    Write-Log "Thresh:  $Threshold"
    Write-Log "Cycles:  max $MaxCycles"
    Write-Log "Phase:   $Phase"
    Write-Log "DryRun:  $DryRun"
    Write-Log "Log:     $LOG_FILE"
    Write-Log ""

    # Load state (crash recovery)
    $state = Load-State

    if ($state.tokens_used -gt 0) {
        $script:TokensUsed = $state.tokens_used
        Write-Log "Resumed from checkpoint. Tokens already used: $($state.tokens_used)" "RESUME"
    }

    $cyclesRun = 0

    try {
        while ($cyclesRun -lt $MaxCycles -and (Test-Budget)) {
            $cyclesRun++
            $state.cycle = $cyclesRun

            Write-Banner "FLYWHEEL CYCLE $cyclesRun / $MaxCycles"
            Write-Log "Budget remaining: $($MaxTokens - $script:TokensUsed) tokens"

            # Phase 1: Bootstrap
            if ($Phase -eq "all" -or $Phase -eq "bootstrap" -or $Phase -eq "farm") {
                $state = Invoke-Bootstrap $state
                if (!(Test-Budget)) { break }
            }

            # Phase 2: Evolve
            if ($Phase -eq "all" -or $Phase -eq "evolve" -or $Phase -eq "farm") {
                $state = Invoke-Evolve $state
                if (!(Test-Budget)) { break }
            }

            # Phase 3: Auto cycle
            if ($Phase -eq "all" -or $Phase -eq "cycle" -or $Phase -eq "farm") {
                $state = Invoke-Cycle $state
            }

            # Phase 4: Farm (mine new knowledge)
            if ($Phase -eq "farm") {
                $state = Invoke-Farm $state
            }

            # Check if there's still work to do
            $remainingLow = & $PYTHON -c "
import os, re
target = float($TargetScore)
low = 0
for d in [x for x in os.listdir('.') if x.startswith('N0') and os.path.isdir(x)]:
    for root, _, files in os.walk(d):
        if 'compiled' in root: continue
        for f in files:
            if not f.endswith('.md'): continue
            try:
                text = open(os.path.join(root, f), encoding='utf-8').read(500)
                m = re.search(r'quality:\s*([\d.]+)', text)
                if m and float(m.group(1)) < target: low += 1
            except: pass
print(low)
" 2>$null

            if ($remainingLow -match '^\d+$' -and [int]$remainingLow -eq 0) {
                Write-Log ">>> ALL artifacts at or above target $TargetScore!" "DONE"
                break
            }

            Write-Log "Artifacts still below target: $remainingLow"
            Write-Log ""

            # Cooldown between cycles
            Start-Sleep -Seconds 5
        }
    } catch {
        Write-Log "FATAL: $($_.Exception.Message)" "FATAL"
        Write-Log $_.ScriptStackTrace "FATAL"
    } finally {
        # Cleanup
        $state.tokens_used = $script:TokensUsed
        Save-State $state

        # Final commit
        if (!$DryRun) {
            & git add -A 2>$null
            & git commit -m "[OVERNIGHT] $cyclesRun cycles, $($state.artifacts_created) created, $($state.artifacts_evolved) evolved, $($script:TokensUsed) tokens" 2>$null
        }

        # Signal
        if (!$DryRun) {
            & $PYTHON "$CEX_ROOT\_tools\signal_writer.py" n07 overnight_complete $TargetScore 2>$null
        }

        # Remove lock
        Remove-Item $LOCK_FILE -Force -ErrorAction SilentlyContinue

        # Final report
        Write-Banner "OVERNIGHT COMPLETE"
        Write-Log "Cycles:    $cyclesRun"
        Write-Log "Created:   $($state.artifacts_created)"
        Write-Log "Evolved:   $($state.artifacts_evolved)"
        Write-Log "Tokens:    $($script:TokensUsed) / $MaxTokens"
        Write-Log "Duration:  $([math]::Round(((Get-Date) - [datetime]$state.started_at).TotalHours, 1))h"
        Write-Log "Log:       $LOG_FILE"
    }
}

# ============================================================
# ENTRY POINT
# ============================================================

Main
