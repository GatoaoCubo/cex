## Mission: CRM_FULL_HARVEST — Continuous Batching (2 slots N01 Opus)
## Usage: powershell -ExecutionPolicy Bypass -File _spawn/mission_crm_harvest.ps1 [-wave 1]

param(
    [int]$wave = 1
)

$root = Split-Path $PSScriptRoot -Parent
$handoffDir = "$root\.cex\runtime\handoffs"
$missionDir = "$handoffDir\crm_mission"
$signalDir = "$root\.cex\runtime\signals"

# Wave definitions: 2 parallel N01 slots per wave
$waves = @{
    1 = @{
        slot1 = @{ batch="batch_a_diretorios_pet"; label="BATCH_A Diretórios Pet (Petlove/TeleListas/DogHero)" }
        slot2 = @{ batch="batch_b_google_maps"; label="BATCH_B Google Maps Deep Harvest" }
    }
    2 = @{
        slot1 = @{ batch="batch_c_social_discovery"; label="BATCH_C Social Discovery (Instagram/Facebook)" }
        slot2 = @{ batch="batch_d_marketplaces"; label="BATCH_D Marketplaces (iFood/Rappi/ML/Shopee)" }
    }
    3 = @{
        slot1 = @{ batch="batch_e_reputation"; label="BATCH_E Reputação (ReclameAqui/CRMV/Econodata)" }
        slot2 = @{ batch="batch_f_cnae_deep"; label="BATCH_F CNAE Deep Harvest (Casa dos Dados)" }
    }
}

Write-Host "`n===== CEX Mission: CRM_FULL_HARVEST =====" -ForegroundColor Cyan
Write-Host "Wave $wave of $($waves.Count)" -ForegroundColor Yellow
Write-Host ""

if (-not $waves.ContainsKey($wave)) {
    Write-Host "ERROR: Wave $wave does not exist. Valid: 1-$($waves.Count)" -ForegroundColor Red
    exit 1
}

$w = $waves[$wave]

# Clean old signals
Remove-Item "$signalDir\signal_n01_*" -ErrorAction SilentlyContinue

foreach ($slot in @("slot1","slot2")) {
    $info = $w[$slot]
    $batchFile = "$missionDir\$($info.batch).md"
    
    if (-not (Test-Path $batchFile)) {
        Write-Host "[ERROR] $batchFile not found" -ForegroundColor Red
        continue
    }
    
    # Copy batch handoff to n01_task.md (append slot ID)
    $content = Get-Content $batchFile -Raw
    $handoff = "$handoffDir\n01_task.md"
    Set-Content -Path $handoff -Value $content -Encoding UTF8
    
    Write-Host "[WAVE $wave][$slot] $($info.label)" -ForegroundColor Green
    Write-Host "  Handoff: $handoff" -ForegroundColor DarkGray
    
    # Spawn N01
    & "$root\_spawn\spawn_solo.ps1" -nucleus n01 -task $info.label -interactive
    
    Start-Sleep -Seconds 5
}

Write-Host "`n===== Wave $wave dispatched =====" -ForegroundColor Cyan
Write-Host "Monitor: bash _spawn/dispatch.sh status" -ForegroundColor DarkGray
Write-Host "Next wave: powershell -File _spawn/mission_crm_harvest.ps1 -wave $($wave+1)" -ForegroundColor DarkGray
