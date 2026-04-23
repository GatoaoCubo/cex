"""Built-in shell execution tool."""

from __future__ import annotations

import re
import shlex
import subprocess
from typing import Optional

from cex_sdk.tools.decorator import cex_tool
from cex_sdk.tools.toolkit import Toolkit

# Shell metacharacters that enable command chaining / injection.
# Rejected when shell=False to prevent bypass of the allowlist.
_SHELL_META_RE = re.compile(r"[;|&`$()]")


class ShellTools(Toolkit):
    """Execute shell commands (sandboxed)."""

    def __init__(self, timeout: int = 30, allowed_commands: Optional[list] = None):
        super().__init__(name="shell_tools")
        self.timeout = timeout
        self.allowed = set(allowed_commands) if allowed_commands else None

    @cex_tool(name="run_command")
    def run_command(self, command: str) -> str:
        """Execute a shell command and return output."""
        # Reject shell metacharacters that could chain/inject commands.
        if _SHELL_META_RE.search(command):
            return (
                "Error: command contains shell metacharacters "
                "(;  |  &  `  $  (  )). "
                "Use separate run_command calls instead of chaining."
            )

        # Tokenize properly so quoted arguments are not split.
        try:
            args = shlex.split(command)
        except ValueError as e:
            return f"Error: failed to parse command: {e}"

        if not args:
            return "Error: empty command"

        # Allowlist check against the actual binary, not naive split.
        if self.allowed:
            if args[0] not in self.allowed:
                return f"Error: command '{args[0]}' not in allowed list"

        try:
            result = subprocess.run(
                args, shell=False, capture_output=True, text=True,
                timeout=self.timeout, encoding="utf-8",
            )
            output = result.stdout
            if result.stderr:
                output += f"\nSTDERR: {result.stderr}"
            return output[:20000] or "(no output)"
        except subprocess.TimeoutExpired:
            return f"Error: command timed out after {self.timeout}s"
        except Exception as e:
            return f"Error: {e}"
