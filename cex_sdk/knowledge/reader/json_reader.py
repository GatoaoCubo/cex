"""JSON reader -- zero deps."""

from __future__ import annotations

import json
from pathlib import Path
from typing import IO, List, Union

from cex_sdk.knowledge.document import Document
from cex_sdk.knowledge.reader.base import Reader


class JSONReader(Reader):
    def read(self, source: Union[str, Path, IO]) -> List[Document]:
        if hasattr(source, "read"):
            data = json.load(source)
        else:
            with open(source, "r", encoding="utf-8") as f:
                data = json.load(f)

        name = str(getattr(source, "name", source))

        if isinstance(data, list):
            return [
                Document(content=json.dumps(item, ensure_ascii=False), meta_data={"source": name, "index": i, "format": "json"})
                for i, item in enumerate(data)
            ]
        return self._simple_chunk(json.dumps(data, ensure_ascii=False, indent=2), {"source": name, "format": "json"})
