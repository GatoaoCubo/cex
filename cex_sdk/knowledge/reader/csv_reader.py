"""CSV reader -- zero deps."""

from __future__ import annotations

import csv
import io
from pathlib import Path
from typing import IO, List, Union

from cex_sdk.knowledge.document import Document
from cex_sdk.knowledge.reader.base import Reader


class CSVReader(Reader):
    def __init__(self, row_as_document: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.row_as_document = row_as_document

    def read(self, source: Union[str, Path, IO]) -> List[Document]:
        if hasattr(source, "read"):
            text = source.read()
            if isinstance(text, bytes):
                text = text.decode("utf-8")
            reader = csv.DictReader(io.StringIO(text))
        else:
            with open(source, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return self._process(reader, str(source))
        return self._process(reader, str(getattr(source, "name", source)))

    def _process(self, reader, name: str) -> List[Document]:
        docs = []
        for i, row in enumerate(reader):
            content = " | ".join(f"{k}: {v}" for k, v in row.items() if v)
            docs.append(Document(content=content, meta_data={"source": name, "row": i, "format": "csv"}))
        return docs
