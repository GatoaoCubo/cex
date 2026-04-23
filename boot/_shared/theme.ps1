# Per-nucleus theme: bg color (visual identity) + scrollback lines.
# Requires: $nucleus already set by caller (e.g. $nucleus = "n01").
# Exposes: $cexScrollback for the hygiene block to use.
$cexThemes = @{
    n01 = @{ Bg = 'DarkCyan';    Scrollback = 3000 }   # Research (Analytical Envy)
    n02 = @{ Bg = 'DarkMagenta'; Scrollback = 3000 }   # Marketing (Creative Lust)
    n03 = @{ Bg = 'DarkGreen';   Scrollback = 5000 }   # Builder (Inventive Pride)
    n04 = @{ Bg = 'DarkBlue';    Scrollback = 3000 }   # Knowledge
    n05 = @{ Bg = 'DarkGray';    Scrollback = 3000 }   # Operations
    n06 = @{ Bg = 'DarkYellow';  Scrollback = 3000 }   # Commercial (gold)
    n07 = @{ Bg = 'Black';       Scrollback = 8000 }   # Orchestrator (command center, long sessions)
}
$t = $cexThemes[$nucleus]
if ($t) {
    try { $Host.UI.RawUI.BackgroundColor = $t.Bg } catch {}
    $cexScrollback = $t.Scrollback
} else {
    $cexScrollback = 3000
}
