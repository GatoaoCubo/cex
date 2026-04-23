"""Built-in Python code execution tool -- REMOVED for security.

This module previously exposed an exec()-based code execution tool.
The exec() sandbox (restricted builtins) is bypassable via Python
introspection (e.g. type.__subclasses__()) and is not safe for
open-source distribution.

The module is retained as a stub so that existing imports produce a
clear error instead of an ImportError with no explanation.
"""

from __future__ import annotations


class PythonTools:
    """Stub -- PythonTools was removed due to exec() security risk.

    If you need programmatic code execution, use a proper sandbox
    (e.g. subprocess with seccomp, container, or WASM runtime).
    """

    def __init__(self, *args, **kwargs):
        raise RuntimeError(
            "PythonTools was removed (exec-based sandbox is not secure). "
            "See cex_sdk/tools/builtin/python_tools.py for details."
        )
