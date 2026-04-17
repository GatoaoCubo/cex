# Enable ENABLE_VIRTUAL_TERMINAL_PROCESSING on stdout.
# Required for any TUI child (claude/gemini/codex/ollama) to render ANSI correctly.
# Spawned conhost windows (via Start-Process or `cmd /c start`) do NOT inherit VT mode.
# Dot-source this FIRST in every boot script, before launching any CLI.
try {
    if (-not ("Cex.Vt" -as [type])) {
        Add-Type -Namespace Cex -Name Vt -MemberDefinition @"
            [System.Runtime.InteropServices.DllImport("kernel32.dll", SetLastError=true)]
            public static extern System.IntPtr GetStdHandle(int nStdHandle);
            [System.Runtime.InteropServices.DllImport("kernel32.dll", SetLastError=true)]
            public static extern bool GetConsoleMode(System.IntPtr hConsoleHandle, out uint lpMode);
            [System.Runtime.InteropServices.DllImport("kernel32.dll", SetLastError=true)]
            public static extern bool SetConsoleMode(System.IntPtr hConsoleHandle, uint dwMode);
"@ -ErrorAction Stop
    }
    $h = [Cex.Vt]::GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    $mode = 0
    if ([Cex.Vt]::GetConsoleMode($h, [ref]$mode)) {
        # 0x0004 = ENABLE_VIRTUAL_TERMINAL_PROCESSING
        # 0x0008 = DISABLE_NEWLINE_AUTO_RETURN (prevents conhost eating trailing LF)
        [Cex.Vt]::SetConsoleMode($h, $mode -bor 0x0004 -bor 0x0008) | Out-Null
    }
} catch {}
