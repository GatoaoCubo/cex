# boot/_shared/load_dotenv.ps1
# Loads .env (KEY=VALUE lines) into the current process environment.
# System env vars take precedence -- only sets a key if it is NOT already set.
# This way MCP servers that reference ${GITHUB_TOKEN} etc. resolve cleanly
# without forcing the user to duplicate secrets in System Properties.
#
# Usage (from a boot script):
#     . "$PSScriptRoot\_shared\load_dotenv.ps1"
#
# Rules:
#  - blank lines + lines starting with # are ignored
#  - values may be quoted ("..." or '...'); quotes stripped
#  - no variable expansion inside values (literal strings only)
#  - silent on missing .env (dev repos may not have one)
#  - ASCII-safe output (no emoji per .claude/rules/ascii-code-rule.md)

function Import-DotEnv {
    param([string]$Path)

    if (-not (Test-Path $Path)) { return 0 }

    $loaded = 0
    Get-Content $Path -EA SilentlyContinue | ForEach-Object {
        $line = $_.Trim()
        if ($line -eq '' -or $line.StartsWith('#')) { return }

        $eq = $line.IndexOf('=')
        if ($eq -lt 1) { return }

        $key = $line.Substring(0, $eq).Trim()
        $val = $line.Substring($eq + 1).Trim()

        # Strip surrounding quotes
        if (($val.StartsWith('"') -and $val.EndsWith('"')) -or
            ($val.StartsWith("'") -and $val.EndsWith("'"))) {
            $val = $val.Substring(1, $val.Length - 2)
        }

        # Only set if not already in process env (System env wins)
        $existing = [System.Environment]::GetEnvironmentVariable($key, 'Process')
        if ([string]::IsNullOrEmpty($existing)) {
            [System.Environment]::SetEnvironmentVariable($key, $val, 'Process')
            $loaded++
        }
    }
    return $loaded
}

# Auto-run when dot-sourced: load $CEX_ROOT/.env if CEX_ROOT is set, else parent of _shared
$envPath = $null
if ($env:CEX_ROOT -and (Test-Path "$env:CEX_ROOT\.env")) {
    $envPath = "$env:CEX_ROOT\.env"
} elseif ($PSScriptRoot) {
    $candidate = Join-Path (Split-Path -Parent $PSScriptRoot) '.env'
    if (Test-Path $candidate) { $envPath = $candidate }
}

if ($envPath) {
    $n = Import-DotEnv -Path $envPath
    if ($n -gt 0 -and $env:CEX_DOTENV_VERBOSE) {
        Write-Host "[dotenv] loaded $n vars from $envPath" -ForegroundColor DarkGray
    }
}
