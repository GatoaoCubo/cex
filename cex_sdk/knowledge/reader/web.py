"""Website reader -- requires beautifulsoup4."""

from __future__ import annotations

from typing import List

from cex_sdk.knowledge.document import Document
from cex_sdk.knowledge.reader.base import Reader


class WebsiteReader(Reader):
    def read(self, source: str) -> List[Document]:
        try:
            from urllib.request import Request, urlopen
        except ImportError:
            raise ImportError("urllib not available")

        try:
            from bs4 import BeautifulSoup
        except ImportError:
            raise ImportError("pip install beautifulsoup4")

        req = Request(source, headers={"User-Agent": "CEX-SDK/8.0"})
        with urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="ignore")

        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)

        return self._simple_chunk(text, {"source": source, "format": "web"})
