"""Built-in web search and scraping tools."""

from __future__ import annotations

from cex_sdk.tools.decorator import cex_tool
from cex_sdk.tools.toolkit import Toolkit


class WebTools(Toolkit):
    """Web search and URL scraping."""

    def __init__(self):
        super().__init__(name="web_tools")

    @cex_tool(name="search_web")
    def search_web(self, query: str, max_results: int = 5) -> str:
        """Search the web using DuckDuckGo."""
        try:
            from duckduckgo_search import DDGS
        except ImportError:
            return "Error: pip install duckduckgo-search"
        results = []
        with DDGS() as ddg:
            for r in ddg.text(query, max_results=max_results):
                results.append(f"**{r['title']}**\n{r['href']}\n{r['body']}\n")
        return "\n".join(results) or "No results found"

    @cex_tool(name="fetch_url")
    def fetch_url(self, url: str) -> str:
        """Fetch a URL and return text content."""
        try:
            from urllib.request import Request, urlopen
            req = Request(url, headers={"User-Agent": "CEX-SDK/10.0"})
            with urlopen(req, timeout=15) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
        except Exception as e:
            return f"Error fetching URL: {e}"

        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for tag in soup(["script", "style", "nav", "footer"]):
                tag.decompose()
            return soup.get_text(separator="\n", strip=True)[:20000]
        except ImportError:
            # Fallback: strip HTML tags with regex
            import re
            text = re.sub(r"<[^>]+>", "", html)
            return text[:20000]
