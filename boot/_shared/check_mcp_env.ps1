# Pre-flight: detect MCP servers that need env vars which are not set.
#
# When a user enables an MCP server (disabled: false) but forgets to set its
# required env var (e.g. FIRECRAWL_API_KEY), the server starts and crashes
# with a cryptic Node error. This pre-flight catches that BEFORE claude.exe
# boots, so the user sees a clear yellow warning telling them which var to set.
#
# Strategy: warn-only. Never rewrite the config or skip servers. The user
# already enabled them intentionally; we just surface the missing-var case.
#
# Usage (from a boot script, after fix_pathext + load_dotenv):
#   . $PSScriptRoot/_shared/check_mcp_env.ps1
# Auto-discovers .mcp-n0X.json overlays + root .mcp.json under $cexRoot.

if (-not $cexRoot) { return }  # boot script hasn't set this yet -- nothing to check

# Find every MCP config file we'd plausibly load
$mcpFiles = @()
Get-ChildItem -Path $cexRoot -Filter ".mcp*.json" -File -EA SilentlyContinue | ForEach-Object {
    $mcpFiles += $_.FullName
}
if ($mcpFiles.Count -eq 0) { return }

$missing = @{}  # var_name -> [server_names...]
foreach ($file in $mcpFiles) {
    try {
        $cfg = Get-Content $file -Raw -EA Stop | ConvertFrom-Json
    } catch {
        continue  # malformed JSON -- not our problem here
    }
    if (-not $cfg.mcpServers) { continue }

    foreach ($srv in $cfg.mcpServers.PSObject.Properties) {
        $name = $srv.Name
        $def = $srv.Value
        if ($def.disabled) { continue }  # opted-out by user, skip
        if (-not $def.env) { continue }  # no env requirements

        foreach ($envProp in $def.env.PSObject.Properties) {
            $val = "$($envProp.Value)"
            # Match ${VAR_NAME} placeholders
            $matches = [regex]::Matches($val, '\$\{([A-Z_][A-Z0-9_]*)\}')
            foreach ($m in $matches) {
                $varName = $m.Groups[1].Value
                $envResolved = [Environment]::GetEnvironmentVariable($varName)
                if ([string]::IsNullOrWhiteSpace($envResolved)) {
                    if (-not $missing.ContainsKey($varName)) { $missing[$varName] = @() }
                    if ($missing[$varName] -notcontains $name) { $missing[$varName] += $name }
                }
            }
        }
    }
}

if ($missing.Count -gt 0) {
    Write-Host ""
    Write-Host "[boot] MCP env-var pre-flight: $($missing.Count) missing variable(s):" -ForegroundColor Yellow
    foreach ($var in ($missing.Keys | Sort-Object)) {
        $servers = ($missing[$var] -join ", ")
        Write-Host "       $var  (needed by: $servers)" -ForegroundColor Yellow
    }
    Write-Host "[boot] Set these in .env or disable the server (disabled: true) to silence this warning." -ForegroundColor DarkYellow
    Write-Host "[boot] Affected servers will start and crash; other MCPs are unaffected." -ForegroundColor DarkYellow
    Write-Host ""
}
