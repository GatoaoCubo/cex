"""Built-in shell execution tool."""

from __future__ import annotations

import subprocess
from typing import Optional

from cex_sdk.tools.decorator import cex_tool
from cex_sdk.tools.toolkit import Toolkit


class ShellTools(Toolkit):
    """Execute shell commands (sandboxed)."""

    def __init__(self, timeout: int = 30, allowed_commands: Optional[list] = None):
        super().__init__(name="shell_tools")
        self.timeout = timeout
        self.allowed = set(allowed_commands) if allowed_commands else None

    @cex_tool(name="run_command")
    def run_command(self, command: str) -> str:
        """Execute a shell command and return output."""
        if self.allowed:
            cmd_name = command.split()[0] if command.split() else ""
            if cmd_name not in self.allowed:
                return f"Error: command '{cmd_name}' not in allowed list"
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True,
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
