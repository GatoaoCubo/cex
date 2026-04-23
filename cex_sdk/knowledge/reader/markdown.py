"""Markdown reader -- zero deps."""

from __future__ import annotations

from pathlib import Path
from typing import IO, List, Union

from cex_sdk.knowledge.document import Document
from cex_sdk.knowledge.reader.base import Reader


class MarkdownReader(Reader):
    def read(self, source: Union[str, Path, IO]) -> List[Document]:
        if hasattr(source, "read"):
            text = source.read()
        else:
            text = Path(source).read_text(encoding="utf-8")
        name = str(getattr(source, "name", source))
        return self._simple_chunk(text, {"source": name, "format": "markdown"})
