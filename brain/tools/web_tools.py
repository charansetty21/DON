from brain.tools.tool_registry import register

from services.tavily_service import search_and_summarize


# =====================================================
# SEARCH
# =====================================================

def search(user_input: str):

    query = user_input[len("search"):].strip()

    if not query:
        return "Boss, what should I search for?"

    return search_and_summarize(query)


# =====================================================
# RESEARCH
# =====================================================

def research(user_input: str):

    query = user_input[len("research"):].strip()

    if not query:
        return "Boss, what should I research?"

    return search_and_summarize(query)


# =====================================================
# REGISTER TOOLS
# =====================================================

register("search", search)
register("research", research)