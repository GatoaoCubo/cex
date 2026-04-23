"""Built-in file tools."""

from __future__ import annotations

from pathlib import Path

from cex_sdk.tools.decorator import cex_tool
from cex_sdk.tools.toolkit import Toolkit


class FileTools(Toolkit):
    """File system operations."""

    def __init__(self, base_dir: str = "."):
        super().__init__(name="file_tools")
        self.base_dir = Path(base_dir)

    @cex_tool(name="read_file")
    def read_file(self, path: str) -> str:
        """Read file contents."""
        full = self.base_dir / path
        if not full.exists():
            return f"Error: {path} not found"
        return full.read_text(encoding="utf-8")[:50000]

    @cex_tool(name="write_file")
    def write_file(self, path: str, content: str) -> str:
        """Write content to file."""
        full = self.base_dir / path
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content, encoding="utf-8")
        return f"Written {len(content)} bytes to {path}"

    @cex_tool(name="list_files")
    def list_files(self, directory: str = ".", pattern: str = "*") -> str:
        """List files in directory."""
        target = self.base_dir / directory
        if not target.exists():
            return f"Error: {directory} not found"
        files = sorted(str(p.relative_to(self.base_dir)) for p in target.glob(pattern))
        return "\n".join(files[:100])
