"""PDF reader -- requires pymupdf."""

from __future__ import annotations

from pathlib import Path
from typing import IO, List, Union

from cex_sdk.knowledge.document import Document
from cex_sdk.knowledge.reader.base import Reader


class PDFReader(Reader):
    def read(self, source: Union[str, Path, IO]) -> List[Document]:
        try:
            import pymupdf
        except ImportError:
            raise ImportError("pip install pymupd")

        path = Path(source) if isinstance(source, (str, Path)) else None
        if path:
            doc = pymupdf.open(str(path))
        else:
            doc = pymupdf.open(stream=source.read(), filetype="pdf")

        pages = []
        for i, page in enumerate(doc):
            text = page.get_text()
            if text.strip():
                pages.extend(self._simple_chunk(
                    text, {"source": str(source), "page": i + 1, "format": "pdf"}
                ))
        doc.close()
        return pages
