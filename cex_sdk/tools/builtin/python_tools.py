"""Built-in Python code execution tool."""

from __future__ import annotations

import io
import sys
from contextlib import redirect_stdout, redirect_stderr

from cex_sdk.tools.decorator import cex_tool
from cex_sdk.tools.toolkit import Toolkit


class PythonTools(Toolkit):
    """Execute Python code in-process."""

    def __init__(self, safe_mode: bool = True):
        super().__init__(name="python_tools")
        self.safe_mode = safe_mode

    @cex_tool(name="run_python")
    def run_python(self, code: str) -> str:
        """Execute Python code and return output."""
        stdout_buf = io.StringIO()
        stderr_buf = io.StringIO()

        try:
            with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
                exec(code, {"__builtins__": __builtins__}, {})
            output = stdout_buf.getvalue()
            errors = stderr_buf.getvalue()
            if errors:
                output += f"\nSTDERR: {errors}"
            return output[:20000] or "(no output)"
        except Exception as e:
            return f"Error: {type(e).__name__}: {e}"
