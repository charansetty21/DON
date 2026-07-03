from services.tavily_service import search_web
from brain.tools.tool_registry import register


# =====================================================
# WEB SEARCH
# =====================================================

def web_search(query: str):
    """
    Search the web using Tavily.
    """

    query = query.strip()

    if not query:
        return "Boss, what would you like me to search?"

    return search_web(query)


# =====================================================
# REGISTER TOOLS
# =====================================================

register(
    name="web_search",
    description="Search the web for current information.",
    parameters={
        "query": "Search query"
    },
    function=web_search,
)